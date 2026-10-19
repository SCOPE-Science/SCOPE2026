# Sharp pathwise and isotropic mean-square safety frontiers for planar residual-sketch PLSS

## Finding
For the unweighted residual-history Projected Linear Systems Solver (PLSS), a symmetric, nonsingular real \(2\times2\) system admits three exact first-iteration residual-safety regimes, even though the same algorithm solves that system in at most two iterations in exact arithmetic. Write the singular values of the matrix as \(a\ge b>0\) and \(\kappa=a/b\ge1\). For a uniformly distributed initial residual direction, the squared residual after one step satisfies
\[
\mathbb E\frac{\|r_1\|_2^2}{\|r_0\|_2^2}=\frac{(\kappa-1)^2}{2\kappa},
\qquad
\sup_{r_0\ne0}\frac{\|r_1\|_2}{\|r_0\|_2}=\frac{\kappa-\kappa^{-1}}2.
\]
Consequently the first step is nonexpansive for every initial residual precisely when \(\kappa\le1+\sqrt2\), whereas it is nonexpansive in expected squared Euclidean norm under isotropic initialization precisely when \(\kappa\le2+\sqrt3\). For \(\kappa>1+\sqrt2\), the exact probability of a strict first-step residual increase is
\[
\Pr\{\|r_1\|_2>\|r_0\|_2\}=\frac2\pi\arctan\!\left(\frac{\sqrt{\kappa^4-6\kappa^2+1}}{\kappa^2+1}\right),
\]
which tends to \(1/2\) as \(\kappa\to\infty\); the probability is zero at and below that threshold. These statements are unchanged when either signed eigenvalue of the symmetric matrix changes sign.

## Assumptions and scope
Fix an invertible real symmetric \(A\in\mathbb R^{2\times2}\), a consistent equation \(Ax=b_{\mathrm{rhs}}\), and any starting vector \(x_0\) with nonzero residual \(r_0=b_{\mathrm{rhs}}-Ax_0\). The first PLSS sketch column is \(S_1=r_0\); the weighting matrix is the identity, as in the original Euclidean minimal-correction method. The next sketch is the accumulated residual history \(S_2=[r_0,r_1]\) whenever \(r_1\ne0\). No damping, restarts, regularization, independent resampling, or finite-precision arithmetic is assumed. For probability statements, \(r_0/\|r_0\|_2\) is uniformly distributed on the unit circle; its nonzero magnitude may be fixed, or randomized independently with finite second moment. A symmetric matrix may be definite or indefinite: only its two singular values enter the claimed laws. The expectation of the ratio is over direction and is not a claim of a conditional expected contraction at later steps.

## Proof
The Euclidean minimum-correction formula in the cited PLSS algorithm, with \(S_1=r_0\), reads
\[
p_1=\frac{\|r_0\|_2^2}{r_0^{\mathsf T}A^2r_0}\,Ar_0,
\qquad
r_1=r_0-Ap_1.
\]
The denominator is strictly positive for \(r_0\ne0\). Orthogonally diagonalize \(A\), with signed eigenvalues of magnitudes \(a,b\), and take \(r_0=\rho(\cos\theta,\sin\theta)\). Direct substitution gives
\[
\frac{\|r_1\|_2}{\|r_0\|_2}=
\frac{(a^2-b^2)|\sin\theta\cos\theta|}
{a^2\cos^2\theta+b^2\sin^2\theta}.
\tag{1}
\]
Since the update involves \(A^2\), eigenvalue signs do not appear. Put \(t=|\tan\theta|\). Equation (1) becomes
\[
F_\kappa(t)=\frac{(\kappa^2-1)t}{\kappa^2+t^2},\qquad t\ge0.
\]
Differentiation gives the unique positive maximizer \(t=\kappa\) for \(\kappa>1\), with maximum \((\kappa-\kappa^{-1})/2\); for \(\kappa=1\) the factor vanishes identically. Solving the maximum-at-most-one inequality yields \(\kappa\le1+\sqrt2\), with equality included.

For the exact squared average, put \(P=a^2\), \(Q=b^2\) and use the elementary angular logarithmic integral, valid for all \(P,Q>0\),
\[
L(P,Q):=\frac1{2\pi}\int_0^{2\pi}\log(P\cos^2\theta+Q\sin^2\theta)\,d\theta
=2\log\frac{\sqrt P+\sqrt Q}{2}.
\]
For completeness, the equality follows by writing the integrand as \(\log(c+d\cos2\theta)\) with \(c=(P+Q)/2\) and \(d=(P-Q)/2\), factoring \(c+d\cos u=C|1+we^{iu}|^2\) with \(C=(\sqrt P+\sqrt Q)^2/4\), \(|w|<1\), and averaging the convergent Fourier series of the final logarithm. Dominated differentiation is permitted on any compact subset of \(P,Q>0\); hence
\[
-\partial_P\partial_QL(P,Q)=\frac1{2\pi}\int_0^{2\pi}
\frac{\sin^2\theta\cos^2\theta}{(P\cos^2\theta+Q\sin^2\theta)^2}\,d\theta
=\frac1{2\sqrt{PQ}(\sqrt P+\sqrt Q)^2}.
\]
Multiply by \((P-Q)^2\) to obtain \((a-b)^2/(2ab)=(\kappa-1)^2/(2\kappa)\). Solving this factor-at-most-one inequality for \(\kappa\ge1\) yields \(\kappa\le2+\sqrt3\), including equality.

For the strict-growth event \(F_\kappa(t)>1\), rearrangement gives \(t^2-(\kappa^2-1)t+\kappa^2<0\). Its discriminant \(\Delta=\kappa^4-6\kappa^2+1\) is positive for \(\kappa\ge1\) exactly when \(\kappa>1+\sqrt2\). The two positive roots are \(t_\pm=(\kappa^2-1\pm\sqrt\Delta)/2\), and their product is \(\kappa^2\). Under uniform angular direction, \(t=|\tan\theta|\) has distribution function \(\Pr\{t\le u\}=2\arctan(u)/\pi\). Therefore
\[
\Pr\{F_\kappa(t)>1\}=\frac2\pi(\arctan t_+-\arctan t_-)
=\frac2\pi\arctan\frac{\sqrt\Delta}{\kappa^2+1}.
\]
This proves the probability formula and its limit \(1/2\).

Finally the exact first sketch condition is \(r_0^{\mathsf T}r_1=0\). If \(r_1\ne0\), the two real vectors \(r_0,r_1\) form a basis, so the second PLSS projection imposes \(S_2^{\mathsf T}r_2=0\) with nonsingular \(S_2^{\mathsf T}A^2S_2\), forcing \(r_2=0\). If \(r_1=0\), termination was already achieved. In particular, first-step mean-square expansion does not contradict the established two-step finite termination.

## Verification
Run the standalone `verify.py` with Python 3.9 or later. It checks 6,948 exact-rational equalities and inequalities for the first-step residual, eigenvalue-sign invariance, sharp-threshold polynomial tests, orthogonality and the full-rank second sketch. It additionally uses deterministic angular quadrature at several condition numbers to check the analytically proved mean-square and strict-growth-probability formulas numerically. These finite tests are corroboration only: the proof of the general statements is the algebra, angular integral, quadratic inequality, and rank argument above. The script has no external data dependencies.

For instance, \(\kappa=3\) gives worst-case first-step gain \(4/3>1\) but mean-square factor \(2/3<1\); \(\kappa=4\) gives mean-square factor \(9/8>1\). Both systems solve in at most two exact residual-sketch steps.

## Relationship to prior work
Brust and Saunders (arXiv:2207.07615) introduced PLSS, derived the minimum-correction update formula and proved finite termination for residual-history sketches. Their subsequent structured-sketch study (arXiv:2407.00746v1) gives the broader weighted-sketch framework and again emphasizes finite termination. Classical spectral extremal inequalities already control worst-case growth for Rayleigh-type steps. Those definitions, generic identities, and qualitative finite-termination conclusions are prior work, not new contributions here. The specific additional classification is the exact isotropic first-step second moment, its sharp separate safety threshold, and the angular probability of first-step growth in relation to the deterministic frontier. No claim is made that the maximal-gain expression alone is new.

## Limitations
The classification is exact only for real symmetric invertible \(2\times2\) systems with the specified Euclidean PLSS residual-history sketch and uniform angular initialization. It does not provide dimension-free or higher-dimensional expected bounds, describe conditional distributions after the first step, or quantify finite-precision instability. The prior-work search has not excluded every equivalent formulation in broader steepest-descent or sketch-and-project literature. The results concern relative Euclidean residual, not solution error or a deterministic arbitrary-direction average. The two-step conclusion assumes exact arithmetic and an exact projected solve.

## References
- J. J. Brust and M. A. Saunders, *PLSS: A Projected Linear Systems Solver*, arXiv:2207.07615, first public submission 2022-07-15, https://arxiv.org/abs/2207.07615; relevant Eq. (1.8), Secs. 2 and 4.
- J. J. Brust and M. A. Saunders, *Structured Sketching for Linear Systems*, arXiv:2407.00746v1, public 2024-06-30, https://arxiv.org/abs/2407.00746; relevant Sec. 2, Eqs. (2.1)–(2.4), and finite termination discussion.
