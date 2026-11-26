# Antithetic pairing restores A-stability and suppresses stochastic fluctuations in randomized implicit RK2

## Finding
Take the implicit randomized two-stage Runge–Kutta scalar test-equation step of Bochacik and Przybyłowicz, with parameter \(U\in[0,1]\) and scalar Dahlquist argument \(z\). Apply two consecutive equal-size steps with complementary parameters \(U\) and \(1-U\), independently regenerating \(U\) between pairs. The paired amplification is
\[
B(z,U)=\frac{1+z+U(1-U)z^2}{1-z+U(1-U)z^2}.
\]
For every \(\operatorname{Re}z<0\) and every \(U\in[0,1]\), \(|B(z,U)|<1\). Consequently the paired random integrator is *pathwise and mean-square A-stable*, regardless of the probability law of \(U\), even though the original independently randomized uniform-parameter method is not mean-square A-stable.

More sharply, for the scalar autonomous equation \(y'=\lambda y\), fixed \(\lambda<0\), \(T>0\), and nonzero deterministic real \(x_0\), use independent \(U_j\sim\mathrm{Uniform}[0,1]\) per pair, step size \(h=T/(2N)\), and denote the final output by \(X_h\). Then
\[
h^{-5/2}(X_h-\mathbb E X_h)\ \Rightarrow\ \mathcal N\left(0,\frac{T\lambda^6x_0^2e^{2\lambda T}}{90}\right).
\]
For the original method with independent uniform parameters *at every step*, using the same total number of implicit stage evaluations, the final output \(Y_h\) obeys
\[
h^{-3/2}(Y_h-\mathbb E Y_h)\ \Rightarrow\ \mathcal N\left(0,\frac{T\lambda^4x_0^2e^{2\lambda T}}{12}\right).
\]
Thus complementary pairing removes the obstruction to mean-square A-stability and reduces finite-horizon centered stochastic fluctuations from order \(h^{3/2}\) to \(h^{5/2}\). These are centered fluctuation statements, not claims that total numerical bias is order \(h^{5/2}\).

## Assumptions and scope
The source's two implicit randomized RK2 schemes have scalar test-equation amplification \(R(z,u)=1+z/(1-uz)=(1+(1-u)z)/(1-uz)\). One draw is reused only for the adjacent complementary pair, and different pairs are iid. The paired stability result holds for any parameter law supported on \([0,1]\). The Gaussian limits require uniform iid draws, \(\lambda<0\), \(T>0\), fixed real \(x_0\ne0\), and grids for which \(N=T/(2h)\) is an integer. The independently randomized comparison uses \(2N=T/h\) independent uniform draws. All calculations are in exact arithmetic for the scalar test problem; no nonlinear or time-inhomogeneous stability is asserted.

## Proof
Write \(c=u(1-u)\in[0,1/4]\). Direct multiplication gives
\[
 R(z,u)R(z,1-u)=\frac{1+z+cz^2}{1-z+cz^2}=B(z,u).
\]
For \(\operatorname{Re}z<0\),
\[
 |1-z+cz^2|^2-|1+z+cz^2|^2=-4\operatorname{Re}z(1+c|z|^2)>0.
\]
Thus the denominator is nonzero and every pair strictly contracts. For fixed \(z\) in the open left half-plane, the maximum \(\rho(z)=\max_{u\in[0,1]}|B(z,u)|\) exists and satisfies \(\rho(z)<1\). After \(j\) pairs, the magnitude is at most \(\rho(z)^j\) times the initial magnitude, giving both pathwise and mean-square decay. The intervening single step is bounded by the finite constant \(\max_u |R(z,u)|\), so odd iterates also decay, though not necessarily monotonically. This is not L-stability: \(B(z,u)\to1\) as \(z\to-\infty\) whenever \(0<u<1\). For the independent uniform method take \(z=-x\), \(x>2\). On \(0\le u\le1/x\), \(|R(-x,u)|=|1-x/(1+xu)|\ge x/2-1\); hence \(\mathbb E|R(-x,U)|^2\ge (x/2-1)^2/x\to\infty\). Independence then rules out mean-square A-stability.

For real \(z=\lambda h\) and small \(h\), both amplification factors are positive uniformly in the parameter. The Taylor expansions are uniform:
\[
 \log B(z,u)=2z+(2/3-2c)z^3+O(z^5),
 \qquad
 \log R(z,u)=z+(u-1/2)z^2+O(z^3).
\]
For the first expansion, \(\log B=\log(1+w)-\log(1-w)\) with \(w=z/(1+cz^2)\); for the second, subtract the power series of \(\log(1-uz)\) from that of \(\log(1+(1-u)z)\). For uniform \(U\), integration gives \(\mathbb EC=1/6\), \(\operatorname{Var}(C)=1/180\) for \(C=U(1-U)\), and \(\operatorname{Var}(U)=1/12\).

For either method let \(F_h\) be its random factor at argument \(\lambda h\), let \(M=N\) for \(B\) and \(M=2N\) for \(R\), and let \(S_h=\sum_{j=1}^M \log F_{h,j}\). Write \(\mu_h=\mathbb ES_h\); in both cases \(\mu_h\to\lambda T\). The output is \(x_0e^{S_h}\), so no logarithm of a negative output is needed. The leading centered summands are \(-2\lambda^3h^3(C_j-\mathbb EC)\) and \(\lambda^2h^2(U_j-1/2)\), respectively. The sum of the centered Taylor remainders has \(L^2\) norm \(O(\sqrt M h^5)\) in the paired case and \(O(\sqrt M h^3)\) in the independent case, by independence and the uniform bounds. Thus the iid central limit theorem gives normal limits for \((S_h-\mu_h)/h^{5/2}\) and \((S_h-\mu_h)/h^{3/2}\), respectively, with variances \(T\lambda^6/90\) and \(T\lambda^4/12\).

To center by the expectation of the output, write \(W_h=\log F_h-\mathbb E\log F_h\). Then \(W_h\) is centered and uniformly \(O(h^3)\) for the pair or \(O(h^2)\) for a single step. It follows by Taylor expansion of the exponential that \(\log\mathbb E e^{W_h}=O(h^6)\) or \(O(h^4)\), respectively. Consequently
\[
 \log\bigl(\mathbb E e^{S_h}\bigr)-\mu_h=M\log\mathbb E e^{W_h}
 =\begin{cases} O(h^5)&\text{paired},\\ O(h^3)&\text{independent}.\end{cases}
\]
These centering differences remain negligible after exponentiation and division by the respective fluctuation scales, since \(\mu_h\to\lambda T\). The delta method applied to \(x_0e^{S_h}\) about \(\mu_h\) then multiplies each log variance by \(x_0^2e^{2\lambda T}\), giving the stated output variances for either sign of \(x_0\).

## Verification
Run `python3 check.py` with Python 3.10 or later and no third-party dependencies. The script compares 441 paired-amplification identities using exact rational arithmetic; checks 288 complex-parameter cases; verifies the exact uniform moments \(\mathbb EC=1/6\) and \(\operatorname{Var}(C)=1/180\); and reproduces the leading finite-time variances using 65-digit decimal arithmetic and deterministic midpoint quadrature. These finite checks test the implementation only; the infinite-horizon and limit claims follow from the proof above. The exact variance identity for \(N\) pairs is \(\operatorname{Var}(X_h)=x_0^2[(\mathbb EB^2)^N-(\mathbb EB)^{2N}]\) for real arguments; the comparator has the analogous expression with \(R\) and \(2N\).

## Relationship to prior work
Bochacik and Przybyłowicz (2024) define the original randomized implicit RK2 step, derive the common scalar amplification, and identify failure of mean-square A-stability under independent uniform draws. At the level of scalar stability functions \(R(z,1-u)=1/R(-z,u)\) is the adjoint of \(R(z,u)\). Moreover \(B(z,u)\) factors as the two implicit-midpoint stability functions at arguments \(2uz\) and \(2(1-u)z\). Thus the pair's scalar stability can also be read directly from classical midpoint stability; neither midpoint stability nor symmetric composition is claimed as novel. The distinct quantitative result is the centered Gaussian comparison for the two couplings, with the fluctuation scale suppressed by one power of the underlying step size and explicit variance coefficients. This scalar factorization is not asserted as an equivalence for nonlinear equations or for methods randomized through the SDE itself.

## Limitations
The scalar A-stability contraction is asserted at the end of each complementary pair; an intermediate single step can increase magnitude. The scalar Gaussian limits do not establish nonlinear mean-square A-stability, matrix nonnormal contractivity, or improved deterministic bias. Other symmetric-composition or stochastic-integrator literature may contain equivalent formulations; targeted searches are not exhaustive.

## References
1. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1, first submitted 2024-04-29; full text arXiv:2404.19059v3, Sections 1.2 and 3.
2. E. Hairer, C. Lubich, and G. Wanner, *Geometric Numerical Integration: Structure-Preserving Algorithms for Ordinary Differential Equations*, Springer, 2002/2006, composition and symmetry background.
3. D. J. Higham, *Mean-Square and Asymptotic Stability of the Stochastic Theta Method*, SIAM Journal on Numerical Analysis, 2000. Different SDE-randomness model.
4. D. Pesterev and collaborators, *Numerical Integration Schemes Based on Composition of Adjoint Multistep Methods*, Algorithms 15 (2022), 463. Background on adjoint compositions.
