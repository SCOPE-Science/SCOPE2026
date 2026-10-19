# A sharp smoothing-order stability frontier for two-dimensional residual-minimal two-grid correction

## Finding

Consider real symmetric positive-definite two-dimensional systems with a normalized spectrum \(\{1,\kappa\}\), \(\kappa>1\). For a freely chosen one-dimensional coarse space, the *same* normal-equations residual-minimizing correction may be placed before or after a single nonexpansive Richardson smoothing step. The two orders have identical eigenvalues for each coarse space, but their exact worst-case Euclidean operator norms and stability properties differ.

Let \(A=\operatorname{diag}(1,\kappa)\), \(D=I-A/\kappa\), and for any nonzero real vector \(p\) define
\[
C_p=I-p(p^{\mathsf T}A^2p)^{-1}p^{\mathsf T}A^2.
\]
The map \(C_p\) is the error map for an exact minimal-Euclidean-residual coarse correction over \(\operatorname{span}\{p\}\). In the conventional naming of two-grid cycles, \(T_{\mathrm{pre}}=C_pD\) smooths *before* correcting and \(T_{\mathrm{post}}=DC_p\) corrects *before* smoothing.

Over every one-dimensional coarse space, the sharp Euclidean norms are
\[
\boxed{\sup_p\|T_{\mathrm{pre}}\|_2=1-\kappa^{-1},}
\]
\[
\boxed{\sup_p\|T_{\mathrm{post}}\|_2=(1-\kappa^{-1})
\begin{cases}1,&1<\kappa\le\sqrt2,\\
\dfrac{\kappa^2}{2\sqrt{\kappa^2-1}},&\kappa\ge\sqrt2.
\end{cases}}
\]
The post-smoothed operator is uniformly Euclidean-nonexpansive for all coarse lines exactly when \(\kappa\le\kappa_*\), where \(\kappa_*>1\) is the unique root above one of
\[
\kappa^3-\kappa^2-4\kappa-4=0,\qquad \kappa_*\approx2.875129794.
\]
Beyond this threshold some coarse line and initial error give a strict one-step Euclidean amplification, although the underlying Richardson smoother is strictly contractive and both orderings have spectral radius strictly below one. In particular the post-smoothed worst-case norm grows as \(\kappa/2\), while the pre-smoothed worst-case norm stays below one.

An explicit witness is \(\kappa=3\) and \(p=(\sqrt7,1)^{\mathsf T}\). Here \(\|T_{\mathrm{post}}\|_2=3\sqrt2/4>1\) but \(\|T_{\mathrm{pre}}\|_2\le2/3\). Hence the two orderings can have opposite one-cycle Euclidean stability on the very same matrix and coarse line.

For each fixed coarse line, both propagators satisfy \(T^j=\lambda^{j-1}T\) for all integers \(j\ge1\), where \(\lambda\in[0,1-\kappa^{-1}]\) is their common nonzero eigenvalue. Thus the theorem explicitly distinguishes transient one-step risk from asymptotic convergence in an otherwise elementary SPD example.

## Assumptions and scope

All operations use exact real arithmetic and Euclidean solution-error norms (not residual norms). The system is \(Ax=b\) with \(b\) arbitrary; because the iteration is affine, the error propagators do not depend on \(b\). The coarse correction is the unique least-squares minimizer over an affine line with direction \(p\); its normal-equation weight is \(A^{\mathsf T}A=A^2\). The smoother is precisely one Richardson iteration with step \(1/\kappa\), so \(D=\operatorname{diag}(1-1/\kappa,0)\). Each pair of operations uses the *same fixed* coarse line; this is not a comparison of independently evolving Anderson-acceleration and NGMRES history spaces.

Scaling a generic SPD matrix \(\operatorname{diag}(\mu,L)\) by \(\mu>0\), with \(\kappa=L/\mu\), and taking Richardson step \(1/L\), gives exactly the same formulas. Orthogonal changes of basis do not change these operator norms. The optimization is over all nonzero coarse vectors, including eigendirections.

## Proof

Parameterize a coarse line by \(p=(c,s)^{\mathsf T}\), where \(s,c\ge0\) and \(c^2+s^2=1\). Changing coordinate signs does not change the norms, so this loses no generality. Write \(\Delta=c^2+\kappa^2s^2\) and \(d=1-1/\kappa\). Direct substitution in the normal-equation correction gives
\[
C_p=\frac1\Delta
\begin{pmatrix}\kappa^2s^2&-\kappa^2cs\\-cs&c^2\end{pmatrix},\qquad
D=\begin{pmatrix}d&0\\0&0\end{pmatrix}.
\]
Consequently
\[
T_{\mathrm{pre}}=\frac d\Delta
\begin{pmatrix}\kappa^2s^2&0\\-cs&0\end{pmatrix},\qquad
T_{\mathrm{post}}=\frac d\Delta
\begin{pmatrix}\kappa^2s^2&-\kappa^2cs\\0&0\end{pmatrix}.
\]
Both have rank at most one. Taking their sole nonzero singular values yields the *exact pointwise* formulas
\[
\|T_{\mathrm{pre}}\|_2=\frac{ds\sqrt{\kappa^4s^2+c^2}}{c^2+\kappa^2s^2},\qquad
\|T_{\mathrm{post}}\|_2=\frac{d\kappa^2s}{c^2+\kappa^2s^2}.
\]
For the pre-smoothed expression, the difference between the squared denominator and the numerator without \(d^2\) is
\[
(c^2+\kappa^2s^2)^2-s^2(\kappa^4s^2+c^2)
=c^2\bigl[1+2(\kappa^2-1)s^2\bigr]\ge0.
\]
Therefore \(\|T_{\mathrm{pre}}\|_2\le d\), with equality for \(s=1\).

For the other order, set \(u=s\in[0,1]\) and maximize \(f(u)=\kappa^2u/[1+(\kappa^2-1)u^2]\). Its derivative has the sign of \(1-(\kappa^2-1)u^2\). If \(\kappa\le\sqrt2\), the maximum is at \(u=1\) and equals one. Otherwise the maximum is attained at the unique interior point \(u=(\kappa^2-1)^{-1/2}\), with value \(\kappa^2/[2\sqrt{\kappa^2-1}]\). This proves both sharp envelopes, including equality cases.

For \(\kappa>\sqrt2\), the inequality \(\sup_p\|T_{\mathrm{post}}\|_2>1\) is equivalent (all factors positive) to \(\kappa^2(\kappa-1)>4(\kappa+1)\), or \(h(\kappa)=\kappa^3-\kappa^2-4\kappa-4>0\). For \(\sqrt2\le\kappa\le2\), \(\kappa^2(\kappa-1)\le4<4(\kappa+1)\), so \(h(\kappa)<0\). For \(\kappa\ge2\), the derivative \(h'(\kappa)=3\kappa^2-2\kappa-4\) is strictly positive; since \(h(2)=-8<0<h(3)\), there is precisely one crossing. For \(1<\kappa\le\sqrt2\), both envelopes equal \(d<1\).

Finally, both matrices have trace \(\lambda=d\kappa^2s^2/\Delta\) and determinant zero. Direct matrix multiplication (or the rank-one Cayley-Hamilton identity) gives \(T^2=\lambda T\) for either ordering. Since \(\lambda\le d<1\), their common spectral radius is strictly below one and \(T^j=\lambda^{j-1}T\) for every integer \(j\ge1\). In the extremizing post-smoothed configuration, \(\lambda=d\kappa^2/[2(\kappa^2-1)]\), which tends to \(1/2\), while \(\|T_{\mathrm{post}}\|_2\sim\kappa/2\). Hence the one-step amplification is a genuine finite-horizon phenomenon despite asymptotic stability.

## Verification

The standalone `check.py` implements the correction from its original matrix definition, independently evaluates the closed norm formulas, tests both extrema and the polynomial threshold, and compares rank-one powers and eigenvalues. It passed 1,510 combinations of coarse line and condition number with numerical tolerances stated in the code, plus extremizer and threshold checks. These finite numerical checks corroborate the algebraic identities; the calculus proof above establishes the global suprema and the uniqueness of the threshold.

To reproduce, run `python check.py` with Python 3, NumPy, and SciPy installed. The program constructs the exact two-by-two operators using floating-point arrays solely for testing. It is not an interval-arithmetic certificate.

## Relationship to prior work

Adler, He, Hu and Lefebvre (2026, arXiv:2609.13091, first available September 11, 2026) exhibit the shared two-grid interpretation of Anderson acceleration and nonlinear GMRES and derive residual-minimal correction projectors with \(A^{\mathsf T}A\) weights and different smoothing placements. The matrix formulas and their two-grid connection are established prior work, not asserted here as novel. The present result addresses a different optimization question: exact maximization of Euclidean one-cycle error norms over every coarse line, the sharp stability transition, and exact power laws for this two-dimensional SPD regime.

He (2026, arXiv:2603.25983) studies Richardson/NGMRES equivalences and monotonicity properties; these do not on their reported scope give this two-order Euclidean-norm envelope. General multigrid smoothing and oblique-projection stability are established areas, so the result should not be interpreted as inventing order effects or guaranteeing novelty beyond all prior literature.

## Limitations

The model uses an arbitrary *fixed* coarse line and exact normal-equations residual minimization. A practical adaptive acceleration scheme has history-generated coarse spaces and may use different norms; the result does not assert identical bounds for all versions of Anderson acceleration, NGMRES, or multigrid. It evaluates Euclidean solution error, not the \(A\)-energy or residual norm; the latter can behave differently. The source manuscript was accessible only in part for the comparison, and the remaining uninspected sections pose an originality risk. Numerical verification is not an independent audit.

## References

1. J. H. Adler, Y. He, X. Hu, S. Lefebvre, *A Unified Two-Grid Framework for Anderson Acceleration and Nonlinear GMRES*, arXiv:2609.13091v1 (2026-09-11). https://arxiv.org/abs/2609.13091
2. Y. He, *Properties of Nonlinear GMRES Applied to the Preconditioned Richardson Iteration*, arXiv:2603.25983 (2026-03-27). https://arxiv.org/abs/2603.25983
3. A. Reusken, *On maximum norm convergence of multigrid methods for elliptic boundary value problems*, SIAM J. Numer. Anal. 31 (1994), 378–392. https://doi.org/10.1137/0731020
