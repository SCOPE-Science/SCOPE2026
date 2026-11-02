# Two distinct endpoint-irreversibility peaks under anisotropic Gaussian resetting

## Finding
For a two-coordinate harmonically confined Brownian diffusion with simultaneous Poisson resets and independent Gaussian reset coordinates, the reset-cycle *endpoint symmetrized KL divergence per unit time* need not be unimodal in the reset frequency. In the explicit parameter choice below it has **at least two strict local maxima** separated by a local minimum. Four derivative signs admit finite exact-rational certificates; numerical curve fitting is unnecessary.

## Assumptions and scope
Let \(B_1,B_2\) be independent standard Brownian motions, and between global reset events let
\[
 dX_j(t)=-\mu_j X_j(t)\,dt+\sqrt{2\mu_j}\,dB_j(t),\qquad (\mu_1,\mu_2)=(1/2,50).
\]
Reset events follow one independent Poisson process of adjustable rate \(r>0\). Each event replaces the full vector by an independent centered Gaussian vector with independent coordinate variances \(q_1=1/2\), \(q_2=9/10\). The equilibrium covariance without resetting is the identity matrix. The reset-age interval \(T\) between consecutive events is exponential with rate \(r\); events and reset draws are independent.

Conditional on elapsed no-reset time \(t\), the covariance is diagonal, with
\[
 v_j(t)=1-(1-q_j)e^{-k_jt},\qquad (k_1,k_2)=(1,100),\quad k_j=2\mu_j.
\]
For Gaussian densities \(P,Q\), define the *symmetric* KL divergence \(D_{\mathrm J}(P,Q)=D_{\mathrm{KL}}(P\Vert Q)+D_{\mathrm{KL}}(Q\Vert P)\). Set \(G(t)=D_{\mathrm J}(\mathcal N(0,\operatorname{diag}(q_1,q_2)),\mathcal N(0,\operatorname{diag}(v_1(t),v_2(t))))\), and define the cycle endpoint-divergence rate
\[
 \mathcal J(r)=r\,\mathbb E\big[G(T)\big].
\]
It is a specified information-theoretic cycle functional; it is not assumed to equal the full physical stochastic entropy production of an implemented reset protocol.

Then \(\mathcal J\) has a strict local maximum in \((1,3)\) and another strict local maximum in \((20,200)\), and a local minimum in \((3,20)\).

## Proof
For \(0<q<1\) define
\[
 g_q(s)=\frac{(1-q)^2(1-e^{-s})^2}{2q[1-(1-q)e^{-s}]},\qquad F_q(u)=u^2\int_0^\infty e^{-us}g_q(s)\,ds\quad(u>0).
\]
The elementary zero-mean one-dimensional Gaussian KL formulas yield the coordinatewise symmetric KL contribution \(\tfrac12(v/q+q/v-2)=(v-q)^2/(2qv)\). Changing time variables \(s=k_jt\) in the exponential renewal integral gives
\[
 \mathcal J(r)=F_{1/2}(r)+100F_{9/10}(r/100),\qquad
 \mathcal J'(r)=F'_{1/2}(r)+F'_{9/10}(r/100).
\]

For \(q\in(0,1)\) put \(a=1-q\) and \(C=a^2/(2q)\). The geometric series identity
\[
 \frac{(1-z)^2}{1-az}=1+(a-2)z+q^2\sum_{n=2}^\infty a^{n-2}z^n,\qquad 0\le z\le1,
\]
is absolutely and uniformly convergent on the stated interval. Termwise Laplace integration and differentiation therefore give the exact identity
\[
 F_q'(u)=C\left[1+(a-2)\frac{u(u+2)}{(u+1)^2}
 +q^2\sum_{n=2}^\infty a^{n-2}\frac{u(u+2n)}{(u+n)^2}\right].
\]
For positive \(u,n\), the factor \(u(u+2n)/(u+n)^2=1-n^2/(u+n)^2\) lies strictly between zero and one. If \(S_{q,K}(u)\) truncates this derivative at \(n=K\ge2\), its remainder satisfies
\[
 0<F_q'(u)-S_{q,K}(u)<\frac{a^{K+1}}2.
\]
Thus every tested derivative lies in a *rational* interval obtained from exactly two finite sums. With \(K=250\) and \(r\in\{1,3,20,200\}\), the enclosed derivative signs, respectively, are
\[
 (+,-,+,-).
\]
The included exact-rational verifier recomputes these enclosures directly; its displayed decimal values are for orientation only. The lowest absolute derivative among the four tests is still greater than \(10^{-4}\), whereas the stated geometric remainder is smaller than \(2^{-251}+0.9^{251}\), proving strict inequalities without floating-point assumptions.

The convergent power/Laplace formula is real-analytic in \(r>0\). By continuity and the opposite endpoint derivative signs, \(\mathcal J\) has a local maximum inside each of \((1,3)\) and \((20,200)\), and a local minimum inside \((3,20)\). As the function is nonconstant analytic, all local extrema can be selected to be strict (an analytic function cannot be locally constant on a nonempty interval without being constant everywhere). This proves the claim.

## Verification
Run `python3 verify_multiscale.py` in the package directory. The verifier uses Python's standard-library `fractions.Fraction`, computes each of the four derivative bounds with a sum cut off at 250, and asserts that both endpoints have the required sign. It prints derivative estimates near \(0.0324223802823\), \(-0.00122207137082\), \(0.00169843994092\), and \(-0.000160306147998\). The proof is the geometric-series identity and exact tail bound; the code provides an independently replayable arithmetic certificate for the four finite rational evaluations.

## Relationship to prior work
Farago (2026) studies the thermodynamic resetting cycle and a symmetric-KL formulation in a harmonic potential; the present example uses its natural Gaussian endpoint-divergence observable but exhibits **two** separated rate maxima from two relaxation scales. The component Gaussian formula and renewal-rate representation are not new. Mori, Olsen and Krishnamurthy (2022/2023) study total stochastic entropy production of resetting with random reset positions, a different and broader physical functional. Gupta, Olsen and Krishnamurthy (2025) study work costs of recurrent erasure. General facts about sums of single-scale responses being multipeaked are not claimed as novel; the claim is the rigorously certified explicit two-coordinate Gaussian resetting witness.

## Limitations
The conclusion is existential, for this particular two-dimensional diagonal trap and reset Gaussian; it does not determine the total number of stationary points or which peak is globally highest. The cycle endpoint KL rate need not be the full physical entropy production. Stronger general spectral, control or multimodal-response results may subsume the observation. Exact rational enclosures do not independently establish scientific priority.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression* (first submitted 27 May 2026), arXiv:2605.28445. https://arxiv.org/abs/2605.28445
2. F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes* (first submitted 28 Nov 2022), arXiv:2211.15372; Phys. Rev. Research 5, 023103 (2023). https://arxiv.org/abs/2211.15372
3. S. Gupta, K. S. Olsen and S. Krishnamurthy, *Thermodynamic cost of recurrent erasure*, Communications Physics (2025), https://doi.org/10.1038/s42005-025-02277-w
