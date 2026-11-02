# Hilbert or regular polygon: the exact invariant-plane geometry of integer Lipschitz spaces

## Finding

Let \(\operatorname{Lip}_0(\mathbb Z)\) denote the **real** Banach space of functions \(f:\mathbb Z\to\mathbb R\) with \(f(0)=0\) and finite Lipschitz constant for the usual distance \(d(j,k)=|j-k|\). Translation acts by
\[
 (\tau_hf)(n)=f(n+h)-f(h),\qquad h,n\in\mathbb Z.
\]
Every two-dimensional real linear subspace \(X\subset\operatorname{Lip}_0(\mathbb Z)\) invariant under **all** \(\tau_h\) is linearly isometric to exactly one of the following: the Euclidean plane \(\ell_2^2\), or a normed plane whose closed unit ball is an affine image of the regular centrally symmetric \(N\)-gon for one even integer \(N\ge4\). Every one of these isometry types occurs. Each such \(X\) is automatically pointwise closed. The associated canonical two-dimensional quotient predual has the same list of isometry types.

For the regular \(N\)-gon case, the exact real Banach--Mazur distance is
\[
 d_{\mathrm{BM}}(X,\ell_2^2)=\sec(\pi/N).
\]
It equals \(1\) in the Euclidean case. Hence the possible distances are exactly
\[
 \{1\}\cup\{\sec(\pi/N): N=4,6,8,\ldots\},
\]
and the largest is \(\sqrt2\), attained by the square.

There is also a sharp arithmetic realization. For \(0<\theta<\pi\), let
\[
 f_{a,b}^{\theta}(n)=a(\cos(n\theta)-1)+b\sin(n\theta),\qquad
 X_\theta=\{f_{a,b}^\theta:a,b\in\mathbb R\}.
\]
When \(\theta/(2\pi)\) is irrational, \(X_\theta\) is Euclidean. When \(\theta/(2\pi)=p/q\) in lowest terms, its unit ball is an affine-regular \(N\)-gon, where
\[
 N=\begin{cases}q,&q\text{ even},\\2q,&q\text{ odd}.\end{cases}
\]
The canonical coefficient norm has the precise formula
\[
 \|f_{a,b}^{\theta}\|_{\mathrm{Lip}}
 =2\sin(\theta/2)\sup_{n\in\mathbb Z}
 |-a\sin((n+1/2)\theta)+b\cos((n+1/2)\theta)|.
\]
In particular, \(\theta\mapsto d_{\mathrm{BM}}(X_\theta,\ell_2^2)\) is continuous at every irrational \(\theta/(2\pi)\) and discontinuous at every rational one. At a rational \(\theta_0\), for every fixed coefficient pair \((a,b)\),
\[
 \lim_{\substack{\theta\to\theta_0\\\theta\ne\theta_0}}
 \|f_{a,b}^{\theta}\|_{\mathrm{Lip}}
 =2\sin(\theta_0/2)\sqrt{a^2+b^2}.
\]
The maximum multiplicative discrepancy between this punctured limit and the norm at \(\theta_0\), over nonzero coefficient pairs, is **exactly** \(\sec(\pi/N)\). This determines the complete arithmetic discontinuity profile, not merely whether the norms are polyhedral.

## Assumptions and scope

All scalars are real. Integer translations are two-sided, and their action is renormalized to preserve the value zero at the base point. The term *regular \(N\)-gonal plane* means a two-dimensional normed real space whose unit ball is a nonsingular linear image of a regular origin-symmetric \(N\)-gon; isometry types with different numbers of extreme points are distinct. Banach--Mazur distance is the infimum of \(\|T\|\|T^{-1}\|\) over linear isomorphisms. No assertion is made about invariant subspaces of dimension three or greater, complex-valued Lipschitz functions, or noninteger groups.

The *canonical quotient predual* of a pointwise-closed \(X\) is \(\mathcal F(\mathbb Z)/X_\perp\), where \(\mathcal F(\mathbb Z)^*=\operatorname{Lip}_0(\mathbb Z)\). Since \(X\) is finite-dimensional, this quotient is isometric to \(X^*\).

## Proof

**1. An exact intertwining of the translation action.** Define \(D:\operatorname{Lip}_0(\mathbb Z)\to\ell_\infty(\mathbb Z;\mathbb R)\) by
\[
 (Df)_n=f(n+1)-f(n).
\]
For every \(j<k\), the telescoping sum gives \(|f(k)-f(j)|\le(k-j)\|Df\|_\infty\), and taking neighboring integers proves \(\|f\|_{\mathrm{Lip}}=\|Df\|_\infty\). Conversely, any bounded two-sided sequence \(g\) has the unique primitive with value zero at zero, obtained by summing the coordinates between zero and \(n\), with signs reversed on negative indices. Hence \(D\) is an onto real-linear isometry. If \(B\) is the bilateral shift \((Bg)_n=g_{n+1}\), then \(D\tau_1=BD\). Thus a two-dimensional translation-invariant \(X\) corresponds to a two-dimensional \(B\)-invariant subspace \(Y=DX\). Invariance under all integer translations means \(B(Y)=Y\), not just forward invariance.

**2. Two-dimensional bilateral-shift representations.** The restriction \(S=B|_Y\) is a surjective real-linear isometry of \(Y\). Thus \(\|S^k\|=1\) for every integer \(k\). After complexification, its two eigenvalues have modulus one and it has no nontrivial Jordan blocks: powers in both directions would otherwise be unbounded. For every complex scalar \(\lambda\), the eigenspace of the bilateral shift in bounded scalar sequences is at most one-dimensional, since \(Bg=\lambda g\) forces \(g_n=g_0\lambda^n\). Therefore the only real possibilities in dimension two are (i) a nonreal conjugate pair \(e^{\pm i\theta}\), \(0<\theta<\pi\), or (ii) the two distinct real eigenvalues \(+1\) and \(-1\).

In case (ii), the sequences are \(g_n=a+b(-1)^n\), so \(\|g\|_\infty=\max(|a+b|,|a-b|)=|a|+|b|\); the unit ball is a parallelogram, linearly isometric to a square. In case (i), a real basis consists of \(\cos(n\theta)\) and \(\sin(n\theta)\), and every element is \(g_n=a\cos(n\theta)+b\sin(n\theta)\). Its norm is
\[
 \|(a,b)\|_\theta=\sup_{n\in\mathbb Z}|a\cos(n\theta)+b\sin(n\theta)|.
\]
If \(\theta/(2\pi)\) is irrational, the rotation orbit is dense in the unit circle, so this supremum is \(\sqrt{a^2+b^2}\). If \(\theta/(2\pi)=p/q\) with coprime integers \(p,q\), the orbit consists of the \(q\)th roots of unity, up to a rotation. Its centrally symmetrized set of supporting unit normals is a regular \(N\)-point set with \(N=q\) for even \(q\) and \(N=2q\) for odd \(q\). Intersecting the strips \(|u\cdot(a,b)|\le1\) produces a regular centrally symmetric \(N\)-gon, up to rotation. No other Banach geometries are possible.

**3. Realization and the pointwise-closed property.** For each even \(N\ge4\), choose \(\theta=2\pi/N\). Then \(\theta\in(0,\pi)\) and \(q=N\), so the above complex-eigenpair subspace realizes an \(N\)-gonal plane. For the Euclidean plane, choose any irrational \(\theta/(2\pi)\). Taking primitives through \(D^{-1}\) gives invariant subspaces of \(\operatorname{Lip}_0(\mathbb Z)\). Finite-dimensional linear subspaces of the Hausdorff product space \(\mathbb R^\mathbb Z\) are pointwise closed: indeed finitely many coordinate evaluations separate a basis, and pointwise limits retain its uniquely determined coefficients. The quotient predual is \(X^*\); the Euclidean disk is self-dual and the polar of a regular centered \(N\)-gon is another regular \(N\)-gon, proving the predual assertion.

**4. Exact Banach--Mazur distance, including arbitrary affine distortions.** Write the regular \(N\)-gon as
\[
 K=\bigcap_{j=0}^{N-1}\{x:u_j\cdot x\le r\},
\]
with unit outer normals \(u_j\) uniformly distributed around the circle. Its vertices \(v_j\) have common length \(R=r\sec(\pi/N)\). The identity position yields \(d_{\mathrm{BM}}(K,B_2)\le R/r\).

For the reverse bound consider *any* centered ellipse \(E=\{x:x^TQx\le1\}\), with positive definite symmetric \(Q\), for which \(E\subseteq K\subseteq tE\). The first containment implies \(u_j^TQ^{-1}u_j\le r^2\) for each facet, while the second implies \(v_j^TQv_j\le t^2\) for each vertex. The uniform angular configurations have isotropic second moments:
\[
 \frac1N\sum_j u_ju_j^T=\frac12I,
 \qquad \frac1N\sum_jv_jv_j^T=\frac{R^2}{2}I.
\]
Averaging the two inequalities gives \(\operatorname{tr}(Q^{-1})/2\le r^2\) and \(R^2\operatorname{tr}(Q)/2\le t^2\). Since \(\operatorname{tr}(Q)\operatorname{tr}(Q^{-1})\ge4\) for every positive definite \(2\times2\) matrix, it follows that \(t\ge R/r\). All linear Banach--Mazur comparisons correspond to such centered ellipses, so the lower bound is global. The Euclidean case has distance one.

**5. The arithmetic discontinuities.** Direct subtraction yields
\[
 f_{a,b}^\theta(n+1)-f_{a,b}^\theta(n)
 =2\sin(\theta/2)\bigl(-a\sin((n+1/2)\theta)+b\cos((n+1/2)\theta)\bigr).
\]
For irrational \(\theta/(2\pi)\), the norm is exactly \(2\sin(\theta/2)\sqrt{a^2+b^2}\). For rational \(p/q\), the normalized supremum is the support maximum over the \(N\) equally spaced unit directions and satisfies, uniformly in \((a,b)\),
\[
 \cos(\pi/N)\sqrt{a^2+b^2}
 \le \frac{\|f_{a,b}^\theta\|_{\mathrm{Lip}}}{2\sin(\theta/2)}
 \le \sqrt{a^2+b^2}.
\]
Both bounds are sharp in direction: the upper one at a supporting normal, the lower one at a bisector between adjacent normals. If a sequence \(\theta_j\ne\theta_0\) tends to a rational \(\theta_0\), every rational denominator along that sequence tends to infinity (apart from finitely many exceptions); irrational terms already realize the full circle. Therefore the normalized norms converge **uniformly over the Euclidean unit circle** to the Euclidean norm. If \(\theta_0\) is irrational, the same upper bound and the lower semicontinuity of a supremum of continuous functions give continuity. Thus discontinuity occurs exactly at rational \(\theta/(2\pi)\), with the sharp ratio specified in the finding. The Banach--Mazur distance is \(1\) at irrational parameters and \(\sec(\pi/N)\) at rational ones, so it has precisely the same discontinuity set.

## Verification

The five steps above prove the statements for every admissible subspace and parameter, including the irrational case; no finite enumeration is used to infer an infinite result. An optional standalone finite-angle checker in `CHECK.py` compares the exact normal-gap formula with dense angular sampling for selected small denominators; its output is corroborative only. The distance lower bound explicitly quantifies over arbitrary positive definite ellipse matrices, not just circular approximations.

## Relationship to prior work

Doucha's 2026 study of translation-invariant pointwise-closed subspaces of Lipschitz functions on graphs proves that every proper such subspace on \(\mathbb Z\) is finite-dimensional (Example 5.3) and describes canonical quotient preduals. It does not in its inspected main results or integer-line example classify the **isometric Banach geometries of the two-dimensional subspaces** or their exact Banach--Mazur distances. General finite-dimensional translation-invariant-space theory, exemplified by Anselone--Korevaar and Hare--Ward, concerns exponential/trigonometric spectral representation rather than the metric geometry of the Lipschitz norm. Lassak's regular-polygon work studies Banach--Mazur distances from parallelograms, not the isometry spectrum of invariant Lipschitz spaces. The representation and regular-polygon facts in the proof are elementary; the specific full invariant-plane classification and sharp arithmetic norm transitions are the contribution assessed here.

## Limitations

The claim is only for real two-dimensional subspaces on the integer path with invariance under the entire translation group. It does not classify higher-dimensional subspaces, arbitrary graphs, or all contractive projections onto the spaces. The exact regular-polygon comparison to Hilbert space uses standard planar geometry, which is not claimed to be new on its own. An older spectral-theoretic treatment could contain an equivalent Banach-geometric classification under different terminology; publication priority has not been independently established. The proof is a mathematical argument, not an independently certified formalization.

## References

1. M. Doucha, *Invariant pointwise closed subspaces of Lipschitz spaces and their preduals*, arXiv:2608.24143v1 (first publicly submitted 2026-08-25), especially Example 5.3 and the predual discussion.
2. P. M. Anselone and J. Korevaar, *Translation invariant subspaces of finite dimension*, Proc. Amer. Math. Soc. **15** (1964), 747--752, DOI:10.1090/S0002-9939-1964-0169048-7.
3. K. E. Hare and J. A. Ward, *Finite dimensional H-invariant spaces*, Bull. Austral. Math. Soc. **56** (1997), 353--361, DOI:10.1017/S0004972700031142.
4. M. Lassak, *Banach--Mazur distance from the parallelogram to the affine-regular hexagon and other affine-regular even-gons*, Results Math. **76** (2021), Article 62, DOI:10.1007/s00025-021-01368-8.
