# A sharp condition-number envelope for the first mixed–split extended-Krylov orthogonalization gap

## Finding

For the inverse-leading extended-Krylov algorithms of Lund and Schweitzer, the ratio of the third mixed-channel to split-channel orthogonalization indicators has a **sharp lower envelope determined solely by spectral condition number**. Unlike the qualitative strict inequality already available for positive-definite matrices, the envelope becomes arbitrarily large as the matrix approaches a scalar multiple of the identity while the third step remains nonbreaking.

Fix \(\kappa>1\). For \(0<p<1\) put
\[
Q_\kappa(p)=\frac{(\kappa-1)^2p(1-p)[1+(\kappa^2-1)p]}{[1+(\kappa-1)p]^2[\kappa^2-(\kappa^2-1)p]}.
\]
There is a unique maximizer \(p_*=x_*/(1+x_*)\), where \(x_*>0\) is the unique positive root of
\[
\kappa+\kappa^2(2\kappa-1)x+(\kappa-2)x^2-\kappa^2x^3=0.
\]
Set \(\Gamma(\kappa)=Q_\kappa(p_*)^{-1/2}\). For every admissible nonbreaking instance, the local ratio satisfies
\[
\boxed{\frac{\rho_3^{\mathrm M}}{\rho_3^{\mathrm S}}>\Gamma(\kappa)>1.}
\]
The first inequality is **best possible but never attained** among nonbreaking third steps. For example, \(\Gamma(2)=2.8835477563\ldots\), and \(\Gamma(10)=1.1597773406\ldots\). The limits are
\[
\Gamma(\kappa)\sim\frac2{\kappa-1}\quad(\kappa\downarrow1),\qquad \lim_{\kappa\to\infty}\Gamma(\kappa)=1.
\]

## Assumptions and scope

Let \(A\in\mathbb R^{n\times n}\), \(n\ge3\), be real symmetric positive definite, with \(\operatorname{cond}_2(A)\le\kappa\), and let \(v_1=v/\|v\|_2\). The starting vector must have nonzero projection onto at least three distinct eigenspaces of \(A\). This guarantees that \(v_1\), \(A^{-1}v_1\), and \(Av_1\) are linearly independent; the first three basis vectors and both local indicators are therefore well-defined and positive.

In the inverse-leading variants, first compute
\[
m=\langle v_1,A^{-1}v_1\rangle,\quad \nu=\|(A^{-1}-mI)v_1\|_2,\quad v_2=\frac{(A^{-1}-mI)v_1}{\nu}.
\]
At the third-vector step the mixed-channel candidate is \(w_{\mathrm M}=Av_2\), and the split-channel candidate is \(w_{\mathrm S}=Av_1\). For the orthogonal projector \(P\) onto \(\operatorname{span}\{v_1,v_2\}\), define
\[
\rho_3^{\mathrm M}=\frac{\|(I-P)w_{\mathrm M}\|_2}{\|w_{\mathrm M}\|_2},\qquad
\rho_3^{\mathrm S}=\frac{\|(I-P)w_{\mathrm S}\|_2}{\|w_{\mathrm S}\|_2}.
\]
These are the local loss-of-orthogonality predictors defined in the cited algorithm study; no claim is made about end-to-end solution accuracy or achieved floating-point orthogonality.

## Proof

**1. Exact third-step identity.** From the definition of \(v_2\),
\[
Av_2=\frac{v_1-mAv_1}{\nu}.
\]
Consequently, \((I-P)Av_2=-(m/\nu)(I-P)Av_1\). Let \(\mu\) be the discrete unit spectral measure of \(A\) induced by \(v_1\), and write
\[
m=\int\lambda^{-1}\,d\mu,\qquad t=\int\lambda\,d\mu,\qquad s=\int\lambda^2\,d\mu.
\]
Since \(\|Av_1\|_2^2=s\) and \(\|Av_2\|_2^2=(1-2mt+m^2s)/\nu^2\), the two nonzero projection residuals cancel in the ratio and give
\[
\gamma_3^2:=\left(\frac{\rho_3^{\mathrm M}}{\rho_3^{\mathrm S}}\right)^2
=\frac{m^2s}{1-2mt+m^2s},\qquad
\gamma_3^{-2}=1-T(\mu),\quad T(\mu)=\frac{2mt-1}{m^2s}.
\]
The denominator is positive because the active spectrum has at least three values. Cauchy–Schwarz gives \(mt\ge1\). Therefore \(T>0\), while nonconstancy implies \(1-2mt+m^2s>0\), so \(T<1\).

**2. All spectral measures reduce to endpoints.** Rescale the smallest eigenvalue to one. Every admissible \(\mu\) is supported in \([1,\kappa]\). The functional \(T\) is continuous on the compact space of probability measures on this interval and has a global minimum. Its three moment partial derivatives are
\[
T_m=\frac{2(1-mt)}{m^3s}\le0,\quad
T_t=\frac2{ms}>0,\quad
T_s=-\frac{2mt-1}{m^2s^2}<0.
\]
For a minimizing measure \(\mu_*\), its derivative in the direction of a point mass at \(\lambda\) is \(\phi(\lambda)-\int\phi\,d\mu_*\), with
\[
\phi(\lambda)=\frac{T_m}{\lambda}+T_t\lambda+T_s\lambda^2,
\quad \phi''(\lambda)=\frac{2T_m}{\lambda^3}+2T_s<0.
\]
Minimality implies \(\phi(\lambda)\ge\int\phi\,d\mu_*\) for all \(\lambda\in[1,\kappa]\). Integrating and using the minimum of \(\phi\) forces \(\mu_*\) to be supported on the global minimizers of \(\phi\). Strict concavity puts all such minimizers at \(1\) or \(\kappa\). A one-point mass gives \(T=1\), whereas a nontrivial endpoint mixture gives \(T<1\); thus a minimizing measure uses both endpoints.

**3. Solve the remaining scalar extremum.** Let \(p\) be the mass at one and \(1-p\) the mass at \(\kappa\). Substitution into \(1-T\) gives exactly \(Q_\kappa(p)\). The derivative has the sign of
\[
P_\kappa(p)=\kappa(1-p)^3+\kappa^2(2\kappa-1)p(1-p)^2+(\kappa-2)p^2(1-p)-\kappa^2p^3.
\]
Indeed the positive derivative multiplier is \(\kappa(\kappa-1)^2/[ (1+(\kappa-1)p)^3(\kappa^2-(\kappa^2-1)p)^2]\). Setting \(x=p/(1-p)>0\) gives
\[
\frac{P_\kappa(p)}{(1-p)^3}
=\kappa+\kappa^2(2\kappa-1)x+(\kappa-2)x^2-\kappa^2x^3.
\]
The nonzero coefficients of this polynomial have exactly one sign change for every \(\kappa>1\). Descartes' rule, its positive value at zero, and its negative leading coefficient imply exactly one positive root. Since \(Q_\kappa\) vanishes at both ends and is positive inside, that stationary point is its unique global maximum. The preceding variational reduction proves the claimed universal lower envelope.

**4. Sharpness and nonattainment.** The two-point endpoint measure uniquely maximizes the inverse-square ratio, but has a two-dimensional Krylov space and therefore a zero third-step residual; it is excluded by the nonbreakdown assumption. Fix any \(c\in(1,\kappa)\), let \(A_\varepsilon=\operatorname{diag}(1,c,\kappa)\), and take a unit vector with squared spectral weights
\[
((1-\varepsilon)p_*,\ \varepsilon,\ (1-\varepsilon)(1-p_*)),\qquad0<\varepsilon<1.
\]
All three modes are active, the condition number is exactly \(\kappa\), and the ratio tends to \(\Gamma(\kappa)\) as \(\varepsilon\downarrow0\). A nonbreaking instance cannot use only endpoint support, so the inequality is strict. Finally \(Q_\kappa(p)/(\kappa-1)^2\to p(1-p)\) uniformly for \(p\in[0,1]\) as \(\kappa\downarrow1\), giving the small-contrast asymptotic. For large \(\kappa\), evaluating \(Q_\kappa\) at \(p=1-\kappa^{-1/2}\) shows its maximum tends to one, so \(\Gamma(\kappa)\to1\).

## Verification

The standalone Python script `verify.py` uses rational arithmetic to compare the independent weighted-orthogonal-projection formulas for both candidates against the exact spectral-moment identity, and checks the symbolic derivative identity and cubic transformation on rational grids. It passed 779 independent channel comparisons, 779 rational interval checks, 1,639 derivative identity checks and 1,495 cubic-basis checks. An additional independent numerical spectral-envelope sweep covered 7,000 randomly chosen measures; this numerical sweep is supplementary and is not required to reconstruct the proof. The universal statement relies on the exact argument above, not finite tests.

## Relationship to prior work

Lund and Schweitzer (2026), Algorithm 1, Algorithm 2 and Theorem 8, define the mixed/split candidates and show the qualitative inequality \(\rho_k^{\mathrm M}>\rho_k^{\mathrm S}\) for every \(k\ge3\) when \(A\) is positive definite. That algorithm and strict inequality are prior work, not claimed here. Their Theorem 8 does not provide the present condition-number-dependent sharp lower envelope for \(\gamma_3\) or the unique cubic extremizer.

Jagels and Reichel (2009) establish recurrence structures for extended Krylov spaces and orthogonal Laurent polynomials; their comparison is structural rather than an optimization of the two candidate normalization ratios. Rinelli and Vandebril (2026) develop spectral-measure and orthogonal-polynomial correspondence in block Krylov methods, not this sharp mixed/split local metric. General moment-extremal inequalities may provide another formulation of the endpoint-reduction argument, so exhaustive historical priority is not asserted.

## Limitations

The bound concerns only the first nontrivial inverse-leading channel comparison, \(k=3\). It is a local error-amplification *indicator*, not an upper or lower bound on actual accumulated loss of orthogonality, backward error, or matrix-function approximation error. The equality profile is a limiting two-point spectral measure where the third step breaks down; actual eligible matrices strictly exceed the bound. Complex Hermitian analogues follow by the same spectral calculation, but are not separately claimed. No assertion is made for indefinite or nonsymmetric matrices, inexact inner solves, or subsequent iterations. The novelty comparison is self-review and historically nonexhaustive; no independent mathematical audit has been performed.

## References

1. K. Lund and M. Schweitzer, *On the stability of basis construction in extended Krylov subspace methods*, arXiv:2610.21603v1, first public October 15, 2026. https://arxiv.org/html/2610.21603v1
2. C. Jagels and L. Reichel, *The extended Krylov subspace method and orthogonal Laurent polynomials*, Linear Algebra and its Applications 431 (2009), 441–458. https://www.math.kent.edu/~reichel/publications/ext.pdf
3. M. Rinelli and R. Vandebril, *Block Krylov subspaces and orthogonal matrix polynomials: a structural correspondence with applications to unitary matrices*, arXiv:2605.16954v1 (2026). https://arxiv.org/html/2605.16954v1
4. V. Simoncini and Y. Wang, *Stabilized Krylov Subspace Recurrences via Randomized Sketching*, Numerical Linear Algebra with Applications 32 (2025), e70022. https://doi.org/10.1002/nla.70022
