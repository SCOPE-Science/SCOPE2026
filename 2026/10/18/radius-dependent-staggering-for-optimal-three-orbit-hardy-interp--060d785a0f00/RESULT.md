# Radius-dependent staggering for optimal three-orbit Hardy interpolation determinants

## Finding
Let \(m\ge1\) be an integer and \(0<r<s\le1\). Put \(R=r^m\), \(S=s^m\), and \(q=R/S\). The three sampling orbits are the roots of
\[
 z^m=S,\qquad z^m=R e^{i\alpha},\qquad z^m=R e^{i\beta},
\]
respectively. Let \(E_{\alpha,\beta}\) be the square evaluation matrix of the Hardy-orthonormal monomials \(1,z,\ldots,z^{3m-1}\), with one row per node. Set \(D(\alpha,\beta)=\det(E_{\alpha,\beta}^*E_{\alpha,\beta})\).

Define
\[
 t_* = \frac{1+q^2-\sqrt{1+34q^2+q^4}}{8q},
 \qquad \delta_*=\arccos(-t_*).
\]
Then \(-\tfrac12<t_*<0\) and \(0<\delta_*<\pi/2\). **There is exactly one maximizing unordered pair of powered phases**, modulo \(2\pi\):
\[
 \boxed{\{\alpha,\beta\}=\{\pi-\delta_*,\pi+\delta_*\}.}
\]
Its exact squared determinant is
\[
 \boxed{D_{\max}=m^{3m}(r^{2m}s^m)^{m-1}
 \left[4r^{2m}(1-t_*^2)
 \big(s^{2m}+r^{2m}-2(sr)^m t_*\big)^2\right]^m.}
\]
The standard regular-three-gon staggering \(\{2\pi/3,4\pi/3\}\) is strictly suboptimal whenever \(r<s\). For fixed \(r/s\in(0,1)\) and \(m\to\infty\), the squared determinant improves by the asymptotically sharp factor
\[
 \boxed{\frac{D_{\max}}{D_{\rm equal}}=\left(\frac43\right)^m(1+o(1)).}
\]
In the boundary limit \(r\uparrow s\), the optimal phases converge to the expected equally staggered offsets; that equality-of-radii case is not part of the strict-radius theorem.

## Assumptions and scope
The polynomial space is \(\mathcal P_{3m-1}=\{\sum_{j=0}^{3m-1}c_jz^j\}\subset H^2(\mathbb D)\), with coefficient norm \(\|p\|_{H^2}^2=\sum_j|c_j|^2\). For each phase, the corresponding orbit consists of every complex \(m\)-th root of the indicated number, with no distinguished starting node or ordering. The outer orbit has powered phase zero, which is an overall rotational normalization. The two inner orbits are unlabeled; swapping them is not a different configuration. The statement covers all \(m\ge1\), including the three-point case. The squared determinant is the product of squared singular values, or the Gram determinant. It measures total interpolation volume, *not* the least singular value or the spectral condition number.

## Proof
**1. Factorization of the entire determinant.** For a monic polynomial with roots \(\{z_j\}_{j=1}^m\) satisfying \(z^m=a\), the Vandermonde discriminant identity gives
\[
 \prod_{i<j}|z_i-z_j|^2=m^m|a|^{m-1}.
\]
For two disjoint root orbits \(z^m=a\) and \(w^m=b\), the resultant identity gives
\[
 \prod_{z^m=a}\prod_{w^m=b}|z-w|^2=|a-b|^{2m}.
\]
The Vandermonde formula for \(\det E\) and the three within-orbit and three cross-orbit products therefore yield, without an unverified normalization factor,
\[
 D(\alpha,\beta)=m^{3m}(r^{2m}s^m)^{m-1}
 |Re^{i\alpha}-Re^{i\beta}|^{2m}
 |S-Re^{i\alpha}|^{2m}|S-Re^{i\beta}|^{2m}.
 \tag{1}
\]
This identity also handles coinciding orbits: the determinant then vanishes.

**2. Exhaustive optimization over the two-torus.** Every unordered pair of angles is represented by
\[
 \alpha=\phi+\delta,\quad\beta=\phi-\delta,
 \qquad 0\le\delta\le\pi/2,
\]
modulo \(2\pi\), after choosing the shorter of the two circular gaps; \(\delta\) is half that gap. Put \(A=S^2+R^2\), \(B=2SR\) and \(x=\cos\phi\). Direct expansion gives
\[
 |S-Re^{i\alpha}|^2|S-Re^{i\beta}|^2
 =A^2-2ABx\cos\delta+B^2(x^2-\sin^2\delta).
\]
As a function of \(x\in[-1,1]\), this is strictly convex. Since \(\cos\delta\ge0\), the larger endpoint value occurs at \(x=-1\), strictly if \(\delta<\pi/2\). Thus every global maximizer away from \(\delta=\pi/2\) has \(\phi=\pi\). The first cross-orbit factor in (1) is \(4R^2\sin^2\delta\).

Put \(t=-\cos\delta\in[-1,0]\). The remaining one-dimensional objective, up to a positive factor independent of angles, is
\[
 F(t)=(1-t^2)(A-Bt)^2.
\]
Its derivative is
\[
 F'(t)=-2(A-Bt)(At+B-2Bt^2).
\]
Because \(A>B>0\), the first factor is everywhere positive on \([-1,0]\). The quadratic \(2Bt^2-At-B\) is strictly decreasing on \([-1,0]\), positive at \(-1\), and negative at \(0\). Thus precisely one critical point occurs in \((-1,0)\), with positive derivative before it and negative derivative after it. Its negative root is
\[
 t_* = \frac{A-\sqrt{A^2+8B^2}}{4B}
 =\frac{1+q^2-\sqrt{1+34q^2+q^4}}{8q}.
\]
At \(t=-1/2\), the quadratic equals \((A-B)/2>0\); hence \(-1/2<t_*<0\). This also proves \(F(t_*)>F(0)\), so even the degenerate half-gap case \(\delta=\pi/2\), where both endpoint choices of \(\phi\) tied, cannot maximize. It follows that \(\phi=\pi\) and \(t=t_*\) are forced, except for interchanging inner orbits. Substituting in (1) proves the exact maximum and optimizer.

**3. Strict comparison with equal powered staggering.** The equally spaced powered phases correspond to \(t=-1/2\). Since \(t_*>-1/2\) whenever \(R<S\) and \(F\) strictly increases up to \(t_*\), the optimal squared determinant is strictly larger. More precisely, after canceling phase-independent factors,
\[
 \frac{D_{\max}}{D_{\rm equal}}=
 \left[\frac{(1-t_*^2)(1+q^2-2qt_*)^2}{(3/4)(1+q^2+q)^2}\right]^m.
\tag{2}
\]
For \(q=(r/s)^m\to0\), the exact radical gives \(t_*=-2q+18q^3+O(q^5)\). The expression in brackets in (2) is \(4/3+O(q)\). Because \(mq\to0\), taking the \(m\)-th power yields \((4/3)^m(1+o(1))\), as asserted.

## Verification
The standalone file `check.py` builds actual monomial evaluation matrices and compares their numerical squared determinants with (1) for 30 parameter triples. It also performs ten independent global two-variable numerical optimizations and confirms their agreement with the exact optimizer and its strict advantage over equal staggering. All tests passed. Additionally, an independent exact symbolic calculation for \(m=2\), \(r=1/2\), \(s=1\), \(\alpha=\pi\), \(\beta=0\) gives both determinant formulas equal to \(50625/262144\); symbolic expansion yields \(t_*=-2q+18q^3+O(q^5)\). The global theorem rests on the proof, not on these finite tests.

## Relationship to prior work
Pan [1, sections 3–5] analyzes conditioning of Vandermonde matrices and the exceptional Fourier placements on one circle; it does not optimize the determinant for mixed-radius cyclic root orbits. Aubel and Bölcskei [2, section IV] give large-sieve-derived singular-value bounds for Vandermonde nodes in the disk, with no orbit-phase optimum. Classical logarithmic energy and Vandermonde-discriminant identities give the ingredients but not the all-size exact radius-dependent angular phase choice or its exponential contrast with equal staggering.

An especially relevant earlier interpolation construction by Sugiura and Torii [3] concerns quasi-equidistributed nodes formed through rotations of a unit-circle node family. Its accessible abstract addresses iterative interpolation and stability, not the displayed three-orbit two-radius determinant optimum; its complete text could not be compared. A related Hardy orbit-kernel theorem [4] optimizes regularity for nodes all on one radius and explicitly excludes mixed radii; its full mathematical statement and proof were checked for implication, and neither subsumes the two-radius theorem. The present theorem therefore makes no claim that the generic Vandermonde discriminant or the regular single-ring optimum is new.

## Limitations
The outer orbit radius and powered phase are fixed; both inner orbit radii must coincide, and the inner orbits have the same size as the outer orbit. The result does not optimize individual node angles without the regular-orbit constraint, the radii themselves, unequal cardinalities, or other polynomial bases. Determinant optimality does not imply best spectral condition number or noise amplification. Earlier unpublished or unindexed logarithmic-energy classifications and the inaccessible full text of [3] remain originality risks. Independent mathematical auditing has not been performed.

## References
[1] V. Y. Pan, *How Bad Are Vandermonde Matrices?*, arXiv:1504.02118, first posted 8 April 2015, https://arxiv.org/abs/1504.02118.

[2] C. Aubel and H. Bölcskei, *Deterministic Performance Analysis of Subspace Methods for Cisoid Parameter Estimation*, arXiv:1604.07196v1, first posted 25 April 2016, https://arxiv.org/abs/1604.07196.

[3] H. Sugiura and T. Torii, *Polynomial Interpolation on Quasi-Equidistributed Nodes on the Unit Disk*, SIAM J. Numer. Anal. 29 (1992), 1154–1165, DOI:10.1137/0729070.

[4] *Sharp determinant stability and conditioning of concentric Szegő orbit frames*, public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa/RESULT.md.
