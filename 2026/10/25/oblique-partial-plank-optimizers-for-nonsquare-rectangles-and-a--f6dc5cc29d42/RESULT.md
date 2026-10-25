# Oblique partial-plank optimizers for nonsquare rectangles and a cubic-root square limit

## Finding
For real \(a>b>0\) and \(0<W<2b\), define the axis-aligned rectangle \(R=[-a,a]\times[-b,b]\). Let \(\mathcal A_R(W)\) be the supremum of the total area of \(R\) covered by a **finite** union of Euclidean planks with sum of widths at most \(W\). Set \(t=a/b>1\), \(\alpha=W/(2b)\in(0,1)\). There is exactly one \(q>t\) solving
\[
(q-t)\sqrt{1+q^2}=\alpha(q^2-1).
\tag{1}
\]
Its value determines the **sharp covering profile**
\[
\boxed{\mathcal A_R(W)=4ab-\frac{\bigl(a+bq-(W/2)\sqrt{1+q^2}\bigr)^2}{q}.}
\tag{2}
\]
Among individual planks of width \(W\), all the maximizers, up to boundary sets, are exactly the two centered planks with unoriented normals \((1,q)/\sqrt{1+q^2}\) and \((1,-q)/\sqrt{1+q^2}\). In particular, an axis-parallel strip never attains (2) at an interior width. The optimal normal rotates strictly toward the short-side normal as \(W\) increases: \(q(W)\) increases from \(a/b\) to \(+\infty\) as \(W\) traverses \((0,2b)\).

The symmetric square boundary has a **singular, cubic-root unfolding**. At fixed \(W=\sqrt2 b\), if \(a/b=1+\varepsilon\downarrow1\), then
\[
\boxed{q-1=2\varepsilon^{1/3}+o(\varepsilon^{1/3}).}
\tag{3}
\]
This describes how an arbitrarily small rectangular anisotropy selects one of the square's symmetry-related optimizer branches at the critical width.

An exact rational example: \(a=2\), \(b=1\), \(W=\sqrt{10}/4\). Then \(q=3\) and \(\mathcal A_R(W)=53/16\), strictly greater than the best axis-parallel covered area \(\sqrt{10}\).

## Assumptions and scope
A plank of width \(W\) means \(\{x:|n\cdot x-c|\le W/2\}\) for a unit vector \(n\); planar Lebesgue measure is used. A finite family can have arbitrary directions, centers and positive widths, with total width at most \(W\). The theorem concerns \(a>b>0\) and \(0<W<2b\); equality \(a=b\) is a singular boundary and is not asserted as a new full square theorem. Reflections across the coordinate axes give the two unoriented maximizing normal lines. No uniqueness is asserted for decompositions of an optimal strip into multiple planks.

## Proof
**1. Reduction to a central plank.** The planar partial-plank theorem of Bakaev and Polyanskii [1, Theorem 12] says that the largest area covered by any finite plank family with prescribed total width is achieved by a single plank. For a fixed normal \(n\), the section-length density of the centrally symmetric rectangle along the coordinate \(n\cdot x\) is even and nonincreasing away from zero. Thus among parallel strips of width \(W\), a central strip maximizes captured area. At the orientation ultimately found below, its center is unique: the strip extends beyond the density's flat interval into its strictly sloping portion.

**2. Exact slice profile.** By reflections take \(n=(u,v)\) with \(u,v\ge0\), \(u^2+v^2=1\). Write \(w=W/2\), \(U=au\), \(V=bv\), \(S=U+V\), \(D=|U-V|\). Since \(w<b\le S\), full coverage by one strip is impossible. Convolution of the two projected coordinate intervals gives the uncovered area of the central plank as
\[
E(u,v)=\begin{cases}
4ab-4w\min\{a/v,b/u\},&0<w\le D,\\
(S-w)^2/(uv),&D<w<S,
\end{cases}
\tag{4}
\]
with endpoint cases interpreted by continuity. The two formulas agree at \(w=D\). Indeed, the density has a central plateau of height \(2\min\{U,V\}/(uv)\), with linear tails \((S-|z|)/(uv)\) extending to \(\pm S\).

**3. Restricting the normal to \(v\ge u\).** If \(a>b\) and \(u>v\), swap the components. This preserves \(uv\) and \(UV=abuv\), but decreases \(S\) strictly because \((a-b)(u-v)>0\). For fixed \(uv\), write \(D=\sqrt{S^2-4abuv}\). The expression (4) is a strictly increasing function of \(S\) whenever \(w<S\): in the tail regime it is \((S-w)^2/(uv)\), and in the plateau regime it is \(4ab-2w(S-D)/(uv)\), where \(S-D=4abuv/(S+D)\) decreases with \(S\). Therefore the swapped normal covers strictly more. Every maximizing normal has \(v\ge u\).

**4. Exact optimization on \(v\ge u\).** Put \(q=v/u\ge1\). The plateau regime in (4) is monotone toward the region \(D<w\): if \(q\le t=a/b\), it covers \(4wb/u\), increasing with \(q\); if \(q\ge t\), it covers \(4wa/v\), decreasing with \(q\). In the tail regime, minimizing the uncovered area is equivalent to minimizing the positive function
\[
H(q)=\frac{a+bq-w\sqrt{1+q^2}}{\sqrt q},\qquad
H'(q)=\frac{bq-a-w(q^2-1)/\sqrt{1+q^2}}{2q^{3/2}}.
\tag{5}
\]
Let \(T_\alpha(q)=q-\alpha(q^2-1)/\sqrt{1+q^2}\). Then \(\operatorname{sign}H'(q)=\operatorname{sign}(T_\alpha(q)-t)\). For \(q\ge1\),
\[
T_\alpha'(q)=1-\alpha\frac{q(q^2+3)}{(1+q^2)^{3/2}}.
\tag{6}
\]
The fraction in (6) is strictly decreasing for \(q>1\), since its derivative equals \(-3(q^2-1)/(1+q^2)^{5/2}\). Consequently \(T_\alpha\) first possibly decreases and then strictly increases, with no further turns. Also \(T_\alpha(t)<t\) and \(T_\alpha(q)\sim(1-\alpha)q\to\infty\). Therefore exactly one \(q>t\) satisfies (1). This is the unique minimum of \(H\) throughout the tail regime and, by the plateau monotonicity, the unique global minimizing \(q\ge1\). It indeed belongs to the tail regime: (1) implies
\[
D=\frac{b(q-t)}{\sqrt{1+q^2}}=w\frac{q^2-1}{q^2+1}<w.
\tag{7}
\]
Substitution gives (2). By the strict inequalities and strict unimodality away from the central plateau, the only optimal single-plank placements are the centered reflection-related ones.

**5. Monotonicity and the critical cubic root.** On the increasing branch containing the root, \(T_\alpha'(q)>0\). Implicit differentiation of \(T_\alpha(q)=t\) therefore yields
\[
\frac{\partial q}{\partial\alpha}=\frac{(q^2-1)/\sqrt{1+q^2}}{T_\alpha'(q)}>0.
\]
Letting \(\alpha\downarrow0\) gives \(q\downarrow t\). As \(\alpha\uparrow1\), no finite root can persist: \(T_1(q)<1<t\) for all finite \(q>1\), since \(\sqrt{1+q^2}<q+1\). Hence \(q\to\infty\). For the square-symmetry limit at \(\alpha=1/\sqrt2\), set \(q=1+h\). Direct Taylor expansion gives \(T_{1/\sqrt2}(1+h)=1+h^3/8+O(h^4)\). Hence \(t-1=h^3/8+O(h^4)\), proving (3).

## Verification
A self-contained Python 3 script, `verify_rectangle.py`, checks the exact algebraic example in rational arithmetic, the stationary equation, the slice formula and the angular global maximum against an independent 3200-angle grid across 500 deterministic random nonsquare rectangles and widths. It also tests the critical cubic-root law numerically. The script passed at package preparation. The all-parameter proof is the analytic argument above, not the finite tests.

## Relationship to prior work
Bakaev and Polyanskii [1] prove that a single plank suffices for every planar convex body, but do not determine the sharp oblique orientation or area profile of nonsquare rectangles. A prior square-only evaluation gives a two-regime explicit profile for \(a=b\); it does not imply the strict-rectangle uniqueness or singular cubic-root rounding. A published result titled *A complete translation-distance phase diagram for hypercube covariograms* [2] concerns equal-sided hypercubes and maximum overlap, not the unequal-sided rectangle's minimum-overlap or maximal-slab problem. The present claim is an explicit geometric optimization over aspect ratios, not an independent reproof of the general single-plank reduction.

## Limitations
Only finite families of planks and strictly nonsquare rectangles with widths below the minimum rectangle width are classified. No characterization of every multi-plank equality arrangement is claimed. The cubic-root limit is a one-sided shape perturbation at the critical square width. Exact novelty is conditional on the accessible published literature and database comparisons; unindexed or inaccessible classical geometric-optics and covariogram discussions may contain equivalent formulas. Independent audit has not been performed.

## References
[1] E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483v1, first posted 2026-07-29, especially Theorem 12 and Section 4; author-uploaded accessible full text: https://www.researchgate.net/publication/411033031_Optimal_partial_plank_coverings .

[2] *A complete translation-distance phase diagram for hypercube covariograms*, published mathematical research record, 2026-10-11, index identifier 5fadf7c81348; available abstract in the published-finding corpus mathematical research index.
