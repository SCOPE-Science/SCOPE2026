# Antithetic pairing restores A-stability and suppresses stochastic fluctuations in randomized implicit RK2

## Finding
Take the implicit randomized two-stage Runge–Kutta scalar test-equation step of Bochacik and Przybyłowicz, with parameter \(U\in[0,1]\) and scalar Dahlquist argument \(z\). Apply two consecutive equal-size steps with complementary parameters \(U\) and \(1-U\), independently regenerating \(U\) between pairs. The paired amplification is
\[
B(z,U)=\frac{1+z+U(1-U)z^2}{1-z+U(1-U)z^2}.
\]
For every \(\operatorname{Re}z<0\) and every \(U\in[0,1]\), \(|B(z,U)|<1\). Consequently the paired random integrator is *pathwise and mean-square A-stable*, regardless of the probability law of \(U\), even though the original independently randomized uniform-parameter method is not mean-square A-stable.

More sharply, for the scalar autonomous equation \(y'=\lambda y\), fixed \(\lambda<0\), \(T>0\), and nonzero deterministic \(x_0\), use independent \(U_j\sim\mathrm{Uniform}[0,1]\) per pair, step size \(h=T/(2N)\), and denote the final output by \(X_h\). Then
\[
h^{-5/2}(X_h-\mathbb E X_h)\ \Rightarrow\ \mathcal N\left(0,\frac{T\lambda^6x_0^2e^{2\lambda T}}{90}\right).
\]
For the original method with independent uniform parameters *at every step*, using the same total number of implicit stage evaluations, the final output \(Y_h\) obeys
\[
h^{-3/2}(Y_h-\mathbb E Y_h)\ \Rightarrow\ \mathcal N\left(0,\frac{T\lambda^4x_0^2e^{2\lambda T}}{12}\right).
\]
Thus complementary pairing both cures the unbounded mean-square stability region obstruction and reduces finite-horizon centered stochastic fluctuations from order \(h^{3/2}\) to \(h^{5/2}\). These are centered fluctuation statements, not claims that total numerical bias is order \(h^{5/2}\).

## Assumptions and scope
The source's two equivalent implicit randomized RK2 schemes have scalar test-equation amplification \(R(z,u)=1+z/(1-uz)=(1+(1-u)z)/(1-uz)\). One draw is reused only for the adjacent complementary pair, and different pairs are iid. The paired result holds for any parameter law supported on \([0,1]\). The Gaussian limits require uniform iid draws, \(\lambda<0\), \(T>0\), fixed \(x_0\ne0\), and grids for which \(N=T/(2h)\) is an integer. The independently randomized comparison uses \(2N=T/h\) independent uniform draws. All calculations are in exact arithmetic for the scalar test problem; no nonlinear or time-inhomogeneous stability is asserted.

## Proof
Write \(c=u(1-u)\in[0,1/4]\). Direct multiplication gives
\[
R(z,u)R(z,1-u)=\frac{1+z+cz^2}{1-z+cz^2}=B(z,u).
\]
The polynomial \(1-z+cz^2\) has no root in the open left half-plane: its roots have positive real part when \(c>0\), while at \(c=0\) the sole root is \(1\). More directly,
\[
|1-z+cz^2|^2-|1+z+cz^2|^2=-4\operatorname{Re}z(1+c|z|^2)>0
\]
for \(\operatorname{Re}z<0\). Thus every pair strictly contracts. Since \(U\) is supported on a compact set, \(\mathbb E|B(z,U)|^2<1\) for each such \(z\), yielding mean-square decay of all paired iterates. This is the claimed A-stability, *not* L-stability: \(B(z,u)\to1\) as \(z\to-\infty\) whenever \(0<u<1\).

For \(z\) close to zero and \(c\in[0,1/4]\), uniformly in \(c\),
\[
\log B(z,u)=2z+(2/3-2c)z^3+O(z^5).
\]
For uniform \(U\), elementary integration yields \(\mathbb EC=1/6\), \(\operatorname{Var}(C)=1/180\), for \(C=U(1-U)\). Put \(z=\lambda h\). Since \(N=T/(2h)\), the centered log product differs from \(-2\lambda^3h^3\sum_{j=1}^N(C_j-\mathbb EC)\) by a random centered remainder \(o_{\mathbb P}(h^{5/2})\); the difference between centering by \(\log\mathbb EX_h\) and by the mean log is \(O(Nh^6)=O(h^5)\). The ordinary bounded-iid central limit theorem, followed by exponentiation and \(\mathbb EX_h\to x_0e^{\lambda T}\), gives limiting variance
\[
(2\lambda^3)^2\,\frac{T}{2}\,\frac1{180}\,x_0^2e^{2\lambda T}=\frac{T\lambda^6x_0^2e^{2\lambda T}}{90}.
\]
For the independent comparator, uniformly in \(u\),
\[
\log R(\lambda h,u)=\lambda h+(u-1/2)\lambda^2h^2+O(h^3).
\]
The centered iid sum of \(T/h\) terms has variance asymptotic \(T\lambda^4\operatorname{Var}(U)h^3\), and \(\operatorname{Var}(U)=1/12\). The same central limit and delta-method argument gives the second displayed limit. All remainders are uniform because \(u\in[0,1]\), and centering by the expectation changes the logarithmic expansion only at order \(Nh^4=O(h^3)\) or smaller in the comparison after cancellation of common deterministic terms, with the random remainder centered; the covariance corrections are negligible at the stated scales.

## Verification
Run `python3 check.py` with Python 3.10 or later and no third-party dependencies. The script compares 441 paired-amplification identities using exact rational arithmetic; checks 288 complex-parameter cases; verifies the exact uniform moments \(\mathbb EC=1/6\) and \(\operatorname{Var}(C)=1/180\); and reproduces the leading finite-time variances using 65-digit decimal arithmetic and deterministic midpoint quadrature. These finite checks test the implementation only; the infinite-horizon and limit claims follow from the proof above. The exact variance identity for \(N\) pairs is \(\operatorname{Var}(X_h)=x_0^2[(\mathbb EB^2)^N-(\mathbb EB)^{2N}]\) for real arguments; the comparator has the analogous expression with \(R\) and \(2N\).

## Relationship to prior work
Bochacik and Przybyłowicz (2024) define the original randomized implicit RK2 step, prove that the two implicit variants have the same scalar amplification, and identify its failure of mean-square A-stability under independent uniform draws. Standard adjoint-method composition is an older known order-restoration technique: the exact symmetric rational form and second-order consistency by themselves are not asserted as novel. The finding here is the *joint stochastic conclusion* that complementary sampling changes the sampled product to a pathwise A-stable random integrator and suppresses the centered finite-horizon Gaussian fluctuation scale by one power of the underlying step size, with explicit variance coefficients. General stochastic theta-method stability results for SDEs treat a different source of randomness (stochastic dynamics rather than randomized method parameters). Related randomized SDIRK schemes use different Butcher coefficients and are not a covering implication.

## Limitations
The A-stability assertion is for the scalar linear test equation and for observation at the end of each complementary pair; an intermediate single step can increase magnitude. The scalar Gaussian limits do not establish nonlinear mean-square A-stability, matrix nonnormal contractivity, or improved deterministic bias. Other symmetric-composition or stochastic-integrator literature may contain equivalent formulations; targeted published-source and mathematical-record searches are not exhaustive. Independently confirmed originality and correctness remain unperformed.

## References
1. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1, first submitted 2024-04-29; full text arXiv:2404.19059v3, Sections 1.2 and 3.
2. E. Hairer, C. Lubich, and G. Wanner, *Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations*, Springer, 2002/2006, composition and symmetry background.
3. D. J. Higham, *Mean-Square and Asymptotic Stability of the Stochastic Theta Method*, SIAM Journal on Numerical Analysis, 2000. Different SDE-randomness model.
4. D. Pesterev and collaborators, *Numerical Integration Schemes Based on Composition of Adjoint Multistep Methods*, Algorithms 15 (2022), 463. Background on adjoint compositions.
