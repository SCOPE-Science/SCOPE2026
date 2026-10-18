# Sharp reflected mixed-volume recursion and symmetric-base extremality for homothetic frusta

## Finding
Let \(n\ge2\), let \(B\subset\mathbb R^{n-1}\) be any full-dimensional compact convex body, and let \(0\le t\le1\). Set
\[
F_t(B)=\operatorname{conv}\bigl(B\times\{0\},\ tB\times\{1\}\bigr),\qquad
\Psi_k(t)=\sum_{r=0}^{k-1}t^r.
\]
For \(0\le k\le n-1\), write \(M_k(B)=V_{n-1}(B[n-1-k],(-B)[k])\), where the mixed volumes use the standard Minkowski-polynomial normalization. Then **every reflected mixed-volume coefficient of the frustum is determined exactly by two neighboring base coefficients**:
\[
\boxed{V_n(F_t(B)[n-j],(-F_t(B))[j])
=\frac{\Psi_{n-j}(t)M_j(B)+\Psi_j(t)M_{j-1}(B)}{n}}
\quad(1\le j\le n-1).
\]
The ordinary volume is \(\operatorname{vol}_n(F_t(B))=\Psi_n(t)\operatorname{vol}_{n-1}(B)/n\). Consequently, for every \(1\le j\le n-1\),
\[
\boxed{\frac{V_n(F_t(B)[n-j],(-F_t(B))[j])}{\operatorname{vol}_n(F_t(B))}
\ \ge\ \frac{\Psi_{n-j}(t)+\Psi_j(t)}{\Psi_n(t)}.}
\]
This lower bound is attained simultaneously at every index by **every centrally symmetric base**. Conversely, for \(n\ge3\), equality at even one interior index forces \(B\) to be centrally symmetric. In the planar case all admissible bases are intervals and equality always holds.

For \(0\le t<1\), the sharp normalized value reduces to
\[
\boxed{R_{n,j}(t)=1+\frac{(1-t^j)(1-t^{n-j})}{1-t^n},}
\]
with \(R_{n,j}(1)=1\) by continuity. For each index the sharp value decreases strictly from \(2\) at the pyramid endpoint to \(1\) at the prism endpoint; for fixed \(t\in(0,1)\) it is maximal at the central index or central adjacent pair. In particular, every \(n\)-dimensional pyramid over a centrally symmetric \((n-1)\)-body has **all** nontrivial normalized reflected mixed volumes equal to \(2\).

Summing the Minkowski polynomial at coefficient parameter \(1\) yields the simultaneous sharp difference-body inequality
\[
\frac{\operatorname{vol}_n(F_t(B)-F_t(B))}{\operatorname{vol}_n(F_t(B))}
\ge \frac{2^{n+1}-2(1+t)^n}{1-t^n}\quad(0\le t<1),
\]
with continuous limit \(2^n\) at \(t=1\), and the same equality characterization. At the pyramid endpoint the exact minimum is \(2^{n+1}-2\).

## Assumptions and scope
The parameter \(t\) is the top-to-bottom positive homothety ratio; at \(t=0\) the top is a point and at \(t=1\) the body is a prism. The two bases are homothetic about a common center, not arbitrarily translated relative to one another. The height is one; changing the positive height applies an invertible affine map and multiplies all volumes equally. The base need not be symmetric, smooth or polyhedral. Its homothety center need not belong to the base. A centrally symmetric base means symmetric about some center, not necessarily the homothety center.

Mixed volume is defined by \(\operatorname{vol}_d(C+sD)=\sum_{k=0}^d\binom dk V_d(C[d-k],D[k])s^k\) for \(s\ge0\). The endpoints satisfy \(M_0(B)=M_{n-1}(B)=\operatorname{vol}_{n-1}(B)\). The notation \(\Psi_k(1)=k\) avoids division by zero at the prism endpoint.

## Proof
**1. Every horizontal section of a reflected Minkowski sum is explicit.** Put \(q=1-t\), fix \(s>0\), and consider height \(z\in[-s,1]\) in \(F_t(B)+s(-F_t(B))\). A decomposition uses height \(a\in[0,1]\) from \(F_t(B)\), and height \(z-a\in[-s,0]\) from its reflected dilate. The possible horizontal section for this decomposition is
\[
(1-qa)B+\bigl(s+q(z-a)\bigr)(-B),\quad
\max(0,z)\le a\le\min(1,z+s).
\]
When \(a\) increases by \(h\ge0\), **both nonnegative coefficients decrease by \(qh\)**. Thus the earlier section equals the later section plus \(qh(B-B)\), which contains zero. The sections are nested regardless of any symmetry or position of \(B\). Their union is therefore the section at the smallest feasible \(a\), giving the exact identities
\[
\bigl(F_t(B)+s(-F_t(B))\bigr)_z=
\begin{cases}
(1-qz)B+s(-B),&0\le z\le1,\\
B+(s+qz)(-B),&-s\le z\le0.
\end{cases}
\]
The formulas also hold for \(q=0\) and degenerate endpoint sections.

**2. Integrate the base Minkowski polynomial.** Let \(d=n-1\) and use the mixed-volume polynomial of \(B\) and \(-B\). Fubini's theorem and the exact sections give
\[
\operatorname{vol}_n(F_t(B)+s(-F_t(B)))=
\int_0^1\operatorname{vol}_d((1-qz)B+s(-B))\,dz
+\int_{-s}^0\operatorname{vol}_d(B+(s+qz)(-B))\,dz.
\]
For \(0\le k\le d\),
\[
\int_0^1(1-qz)^{d-k}\,dz=\frac{\Psi_{d-k+1}(t)}{d-k+1},\qquad
\int_{-s}^0(s+qz)^k\,dz=\frac{\Psi_{k+1}(t)}{k+1}s^{k+1}.
\]
These hold directly at \(t=1\) as well. Hence the coefficient of \(s^j\), for \(1\le j\le n-1\), equals
\[
\binom{n-1}{j}M_j(B)\frac{\Psi_{n-j}(t)}{n-j}
+\binom{n-1}{j-1}M_{j-1}(B)\frac{\Psi_j(t)}j.
\]
Apply \(\binom{n-1}{j}/(n-j)=\binom nj/n\) and \(\binom{n-1}{j-1}/j=\binom nj/n\), then compare with the defining Minkowski polynomial in dimension \(n\). This proves the exact mixed-volume formula. Direct integration of the original frustum sections proves the volume formula.

**3. Sharp lower bound and equality.** The Alexandrov--Fenchel inequalities make the positive sequence \(M_0(B),\ldots,M_d(B)\) log-concave. Since both endpoints equal \(\operatorname{vol}_d(B)\), every member is at least that value. In dimension \(d\ge2\), Minkowski's first mixed-volume inequality implies \(M_1(B)\ge\operatorname{vol}_d(B)\), with equality only if \(B\) and \(-B\) are translates: they have equal volume, so homothety in the equality condition must have factor one. This is equivalent to central symmetry. If the base is not centrally symmetric, then \(M_1(B)>\operatorname{vol}_d(B)\); log concavity and the equal endpoint values force all interior \(M_k(B)\) to be strictly larger than the base volume. For each \(1\le j\le d\), at least one of \(M_j,M_{j-1}\) is an interior member, and both factors \(\Psi\) are positive. Thus every claimed bound is strict for a nonsymmetric base. If \(B\) is centrally symmetric, its reflection is a translate, so all \(M_k(B)\) equal the base volume, proving simultaneous sharpness. When \(d=1\), every interval is centrally symmetric.

**4. Explicit sharp profile and endpoints.** Substitution of the constant base mixed-volume sequence gives \(R_{n,j}(t)=(\Psi_{n-j}+\Psi_j)/\Psi_n\). The geometric-series identity reduces this to the displayed product expression. With \(x=t^j\) and \(y=t^{n-j}\), the excess over \(1\) equals \((1-x)(1-y)/(1-xy)\). Its partial derivatives with respect to \(x\) and \(y\) are strictly negative for \(0<x,y<1\); both \(x\) and \(y\) increase with \(t\), proving strict decrease. Convexity of \(j\mapsto t^j+t^{n-j}\) gives the central-index maximizers. Expanding the equal-base formula before normalization gives
\[
\operatorname{vol}_n(F_t(B)+s(-F_t(B)))
=\frac{\operatorname{vol}_{n-1}(B)}{n(1-t)}
\left[2(1+s)^n-(t+s)^n-(1+ts)^n\right]
\]
for \(t<1\); the limiting prism case is immediate. Set \(s=1\), divide by the frustum volume, and apply the strict coefficient comparisons to conclude the difference-body result.

## Verification
The included `verify.py` checks 1,050 exact rational coefficient identities over dimensions \(2\) through \(21\), and performs 36 exact planar Minkowski-section integrations for triangular, square, and asymmetric pentagonal bases in three dimensions, including both endpoint frusta. The integral evaluations use convex hulls of planar Minkowski vertex sums and exact rational Simpson integration of quadratic section areas. The script reports `VERIFY_OK`. As a separate geometric comparison, convex hulls of all pairwise reflected vertices of the resulting three-dimensional polyhedra were checked in 36 configurations and agreed with the mixed-volume polynomial. The all-dimensional proof relies on exact sections and the classical mixed-volume inequalities, not on finite tests.

## Relationship to prior work
Fryš, Kotrbatý, Mouamine and Wang's October 5, 2026 preprint develops higher-order Godbersen inequalities and simplex equality rigidity, providing the motivating geometric setting. Kotrbatý and Mouamine established the ordinary sharp Godbersen inequality in July 2026, with the remaining equality classification obtained by Friedland, Putterman and Szusterman. Those global *upper* bounds are not claimed here; the contribution is a complete *exact coefficient recursion* and a sharp *lower* envelope inside the natural homothetic-frustum class.

The published exact calculation for one-vertex simplex truncations is a genuine **special case** of the present recurrence: when the base \(B\) is a simplex, the known identity \(M_k(B)=\binom{n-1}{k}\operatorname{vol}_{n-1}(B)\) recovers its previously published coefficient formula. No novelty is claimed for this special case. A published study of the Santaló point and volume product of arbitrary homothetic frusta treats the same geometric family, but its full theorem and proof concern polar volumes and not the reflected mixed-volume polynomial or its sharp centrally symmetric minimum. Both overlapping families were compared at the level of the full available mathematical statements, not merely their titles.

The recent Godbersen primary preprints were discoverable but their complete arXiv texts could not be retrieved through the available public-access routes; the published titles/abstracts establish global inequalities and equality conditions, but abstract-level inspection does not establish whole-document absence of this recursion. This is explicitly retained as a bibliographic priority risk. The general identities here are independently derived by the full horizontal-section argument above.

## Limitations
The upper and lower bases must be positive homothetic copies about one common center. Arbitrary frusta with skew, rotated, or unrelated end sections are not included. The claimed coefficientwise extremal result is within this class and does not imply a new universal Godbersen bound. The source's higher-order inequalities are not evaluated. The equality condition for nonsymmetric bases uses classical Alexandrov--Fenchel and Minkowski inequalities. Unindexed older formulas for pyramids, prisms, Cayley polytopes or mixed volumes could overlap historically; the present novelty assessment is same-model only, not an independent priority certification.

## References
1. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v1 (first public 5 October 2026), primary MSC2020 52A40.
2. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387v1 (22 July 2026).
3. O. Friedland, E. Putterman and M. Szusterman, *Equality case in the Kotrbatý--Mouamine inequality*, arXiv:2610.04527v1 (3 October 2026).
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published mathematical finding, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949.
5. *Universal Santaló and volume-product laws for homothetic frusta*, published mathematical finding, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359.
6. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition, Cambridge University Press, 2014; classical Minkowski mixed-volume polynomial and Alexandrov--Fenchel theory.
