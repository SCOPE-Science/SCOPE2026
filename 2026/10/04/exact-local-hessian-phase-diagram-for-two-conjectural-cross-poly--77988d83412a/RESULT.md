# Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers
## Finding
Let
\[
M_n=\left\{a\in\mathbb S^{n-1}:\sum_{j=1}^n a_j=0\right\},\qquad
\Phi_n(a)=\operatorname{vol}_{n-1}(B_1^n\cap a^\perp).
\]
Consider the two normals appearing in the maximizer conjecture of Brazitikos--Pandis,
\[
p_n=\frac{1}{\sqrt2}(1,-1,0,\ldots,0)
\]
and
\[
q_n=\left(-\sqrt{\frac{n-1}{n}},\frac{1}{\sqrt{n(n-1)}},\ldots,\frac{1}{\sqrt{n(n-1)}}\right).
\]
The spherical Hessian of \(\log\Phi_n\) at \(p_n\), restricted to \(T_{p_n}M_n\), has exactly two eigenvalues:
\[
-3\quad\text{with multiplicity }n-3,
\qquad
\frac{n-8}{n}\quad\text{with multiplicity }1.
\]
Consequently, \(p_n\) is a strict local maximizer for \(3\le n\le7\), is quadratically degenerate in exactly one tangent direction for \(n=8\), and is a saddle for every \(n\ge9\).

At \(q_n\), permutation symmetry of the last \(n-1\) coordinates makes the restricted Hessian scalar. Its exact eigenvalue is
\[
\frac{3}{68},\quad -\frac{2393}{7865},\quad -\frac{5899}{9762},\quad -\frac{2290207}{2630733},\quad -\frac{16822403}{15129624}
\]
for \(n=4,5,6,7,8\), respectively. Thus \(q_4\) is a strict local minimum, whereas \(q_n\) is a strict local maximum for \(5\le n\le8\). In particular, the two conjectural maximizer configurations are simultaneously strict local maxima in dimensions \(5,6,7\). The proposed global switch at \(n=6\) therefore does not coincide with a local-stability bifurcation.

## Assumptions and scope
The cross-polytope is \(B_1^n=\{x\in\mathbb R^n:\sum_j|x_j|\le1\}\). The constraint \(\sum_j a_j=0\) is exactly the condition that the central hyperplane \(a^\perp\) pass through the barycenter of the facet \(\operatorname{conv}\{e_1,\ldots,e_n\}\). Normals are taken on the unit sphere, so local statements are intrinsic to \(M_n\).

The result is a local second-variation theorem. It does not prove the global maximizer conjecture. At \(n=8\), the theorem identifies a one-dimensional quadratic null direction at \(p_8\) but does not classify the sign of the first nonzero higher-order term there. No assertion about the local type of \(q_n\) for \(n\ge9\) is needed or made.

## Proof
Brazitikos--Pandis use the standard section formula
\[
\Phi_n(a)=\frac{2^n}{\pi(n-1)!}I_n(a),\qquad
I_n(a)=\int_0^\infty\prod_{j=1}^n\frac{dt}{1+a_j^2t^2}.
\]
The positive prefactor is independent of \(a\), so the Hessians of \(\log\Phi_n\) and \(\log I_n\) agree.

Let \(a\in M_n\), let \(h\in T_aM_n\) be a unit tangent vector, and use the great-circle path
\[
a(s)=a\cos s+h\sin s.
\]
For
\[
g(s,t)=\prod_j(1+a_j(s)^2t^2)^{-1},
\]
write \(\ell_j(s,t)=-\log(1+a_j(s)^2t^2)\). At \(s=0\),
\[
\ell_j'=-\frac{2a_jh_jt^2}{1+a_j^2t^2},
\]
\[
\ell_j''=-\frac{2(h_j^2-a_j^2)t^2}{1+a_j^2t^2}
+\frac{4a_j^2h_j^2t^4}{(1+a_j^2t^2)^2}.
\]
At both \(p_n\) and \(q_n\), symmetry and the tangent constraints give \(\sum_j\ell_j'=0\), hence
\[
\frac{d^2}{ds^2}\log I_n(a(s))\Big|_{s=0}
=\frac{\int_0^\infty g(0,t)\sum_j\ell_j''(0,t)\,dt}{\int_0^\infty g(0,t)\,dt}.
\]
Differentiation under the integral is justified by the displayed rational majorants; the resulting integrands decay at least as \(t^{-2}\).

For \(p_n\), the tangent equations give \(h_1=h_2\) and \(\sum_{j\ge3}h_j=-2h_1\). Under the permutation group of the last \(n-2\) coordinates, the tangent space splits orthogonally into a zero-sum subspace of dimension \(n-3\) and one collective direction. On the zero-sum subspace one may take \(h_1=h_2=0\), \(\sum_{j\ge3}h_j=0\), \(\sum_{j\ge3}h_j^2=1\). Since
\[
g(0,t)=\left(1+\frac{t^2}{2}\right)^{-2},
\]
the second-log-derivative factor is
\[
-\frac{t^4}{1+t^2/2}.
\]
The beta integrals give
\[
\int_0^\infty g(0,t)\,dt=\frac{\pi\sqrt2}{4},
\qquad
\int_0^\infty g(0,t)\left(-\frac{t^4}{1+t^2/2}\right)dt
=-\frac{3\pi\sqrt2}{4},
\]
so this eigenvalue is \(-3\).

For the collective unit vector, write \(h_1=h_2=r\) and \(h_3=\cdots=h_n=z\). The tangent and normalization equations give
\[
r^2=\frac{n-2}{2n},\qquad z^2=\frac{2}{n(n-2)},\qquad 2r+(n-2)z=0.
\]
Substitution gives the second-log-derivative factor
\[
-\frac{4t^4(t^2+6-2n)}{n(t^2+2)^2}.
\]
After multiplication by \(g(0,t)=4/(t^2+2)^2\), the numerator is
\[
\frac{16\bigl((2n-6)t^4-t^6\bigr)}{n(t^2+2)^4}.
\]
Using
\[
\int_0^\infty\frac{t^{2m}}{(t^2+2)^k}\,dt
=\frac12\,2^{m+1/2-k}B\left(m+\frac12,k-m-\frac12\right),
\]
one obtains
\[
\int_0^\infty g(0,t)\sum_j\ell_j''\,dt
=\frac{\pi\sqrt2}{4}\frac{n-8}{n}.
\]
Division by \(I_n(p_n)=\pi\sqrt2/4\) gives the claimed collective eigenvalue.

For \(q_n\), put
\[
b^2=\frac{1}{n(n-1)},\qquad c^2=\frac{n-1}{n}.
\]
The tangent equations force \(h_1=0\) and \(\sum_{j=2}^n h_j=0\). The permutation action on the last \(n-1\) coordinates is irreducible on this sum-zero space, so the Hessian is scalar there. It is therefore enough to use
\[
h=\frac{1}{\sqrt2}(0,1,-1,0,\ldots,0).
\]
The base integrand and its second-log-derivative factor reduce to
\[
g(0,t)=\frac{1}{(1+c^2t^2)(1+b^2t^2)^{n-1}},
\]
\[
\sum_j\ell_j''
=\frac{2n^2(n-1)t^4(-n^2+3n+t^2)}{(n^2-n+t^2)^2\bigl((n-1)t^2+n\bigr)}.
\]
Exact rational integration gives the five values displayed in the Finding for \(4\le n\le8\). The signs then give the local classifications. Since the two tangent-space eigenvalues at \(p_n\) are both negative exactly for \(n\le7\), while the scalar eigenvalue at \(q_n\) is negative for \(5\le n\le8\), dimensions \(5,6,7\) form the announced bistable window.

As a consistency check with the conjectured global switch, the two candidate section values satisfy
\[
\frac{I_5(q_5)}{I_5(p_5)}=\frac{1573\sqrt{10}}{5000}<1,
\qquad
\frac{I_6(q_6)}{I_6(p_6)}=\frac{8135\sqrt{15}}{31104}>1.
\]
These inequalities compare only the two candidates and are not used to claim global optimality.

## Verification
The standalone script `artifacts/verify_hessian.py` reconstructs the rational second-variation factors, evaluates the sparse beta integrals symbolically, and independently integrates the dense cases \(4\le n\le8\) in exact arithmetic using SymPy. It also checks the two candidate-value ratios in dimensions \(5\) and \(6\). Running it with the packaged dependency version returns `VERIFY_OK`.

The proof of the general sparse spectrum is analytic and does not rely on finite sampling. The dense sign claims are restricted to the explicitly integrated dimensions \(4\) through \(8\); no numerical extrapolation is used.

## Relationship to prior work
Brazitikos--Pandis introduce exactly this constrained cross-polytope problem. Their Theorem 5.1 determines the minima, while Conjecture 5.2 proposes that the maximum is attained at \(p_n\) for \(n<6\) and at \(q_n\) for \(n\ge6\). Their Section 5 proceeds through elementary symmetric polynomials and does not state the local Hessian spectrum of the section-volume functional at either conjectural maximizer.

The present calculation separates the proposed global transition from local stability: \(q_n\) is already a strict local maximizer at \(n=5\), while \(p_n\) remains a strict local maximizer through \(n=7\). This local coexistence is not implied by the conjectured global statement. The older Nayar--Tkocz cross-polytope convexity theorem concerns coordinate dilations of a fixed section and does not vary the normal inside the facet-barycenter constraint.

## Limitations
The global maximizer problem remains open. Quadratic degeneracy of \(p_8\) is not resolved to higher order. The dense local computation is asserted only in dimensions \(4\) through \(8\), despite suggestive behavior outside this range. Search-based originality checks cannot exclude unindexed or unpublished work.

## References
1. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1, 2026, especially Section 5 and Conjecture 5.2.
2. P. Nayar and T. Tkocz, *On a convexity property of sections of the cross-polytope*, Proc. Amer. Math. Soc. 148 (2020), 1271--1278, DOI 10.1090/proc/14777.
3. A. Koldobsky, *An application of the Fourier transform to sections of star bodies*, Israel J. Math. 106 (1998), 157--164, DOI 10.1007/BF02773465.
