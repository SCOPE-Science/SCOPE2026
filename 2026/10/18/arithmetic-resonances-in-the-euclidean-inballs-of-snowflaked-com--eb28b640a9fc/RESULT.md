# Arithmetic resonances in the Euclidean inballs of snowflaked complete-bipartite transportation balls

## Finding
Let \(m\ge2\) be an integer and \(1<t<2\). On the disjoint union \(M=A\sqcup B\), with \(|A|=|B|=m\), give distinct same-part points distance \(t\) and cross-part points distance \(1\). In the canonical Euclidean zero-sum hyperplane \(H=\{x\in\mathbb R^{2m}:\sum_v x_v=0\}\), let
\[
P_{m,t}=\operatorname{conv}\left\{\frac{e_u-e_v}{d_t(u,v)}:u\ne v\right\}
\]
be the real Lipschitz-free unit ball. Define
\[
\Delta_m(t)=\min_{\substack{1\le a\le m-1\\0\le b\le m}}\bigl|at+(2-t)b-m\bigr|,
\quad
\mathcal E_m(t)=\{(a,b):1\le a\le m-1,\ 0\le b\le m,\ |at+(2-t)b-m|=\Delta_m(t)\}.
\]
Its **largest Euclidean inball** has exact radius
\[
\boxed{r_m(t)=\left[\frac m2\bigl(1+(t-1)^2\bigr)-\frac{\Delta_m(t)^2}{2m}\right]^{-1/2}.}\tag{1}
\]
The centered inball touches exactly
\[
\boxed{T_m(t)=2\sum_{(a,b)\in\mathcal E_m(t)}\binom ma\binom mb}\tag{2}
\]
facets. The complete set of maximal-ball centers has affine dimension zero or one:
\[
\boxed{\dim_{\mathrm{aff}}\mathcal C_m(t)=
\begin{cases}
0,&m\text{ odd},\\
1,&m\text{ even and }\mathcal E_m(t)=\{(m/2,m/2)\},\\
0,&m\text{ even and }\mathcal E_m(t)\ne\{(m/2,m/2)\}.
\end{cases}}\tag{3}
\]
For every even \(m\), the inradius reduces identically to \(r_m(t)=[m(1+(t-1)^2)/2]^{-1/2}\). For odd \(m\), \(\Delta_m(t)>0\) whenever \(t\) is irrational, whereas \(\Delta_m(3/2)=0\) for every \(m\ge3\). Thus an explicitly finite arithmetic resonance set controls equality in the sharp quadratic radius bound; in even size, extra resonances collapse the optimal-center segment to a point. For example, \(m=4\) has a one-dimensional family of centers at generic irrational \(t\), but a unique center at \(t=4/3\), where 88 facets touch instead of the generic 72.

## Assumptions and scope
All scalars are real. Distances are intrinsic to \(H\), with the inherited standard Euclidean inner product, not to a pointed-coordinate model or an arbitrary affine equivalent unit ball. The metric is a genuine finite metric because \(t<2\), and is the \(\alpha\)-snowflake of the unit-edge complete-bipartite graph metric when \(t=2^\alpha\), \(0<\alpha<1\). The Euclidean embedding of its transportation ball is fixed by the displayed molecules. A maximal inball is a Euclidean ball contained in \(P_{m,t}\), and \(\mathcal C_m(t)\subset H\) is the set of centers of all inballs of maximal radius.

Let \(Q_{m,t}=P_{m,t}^{\circ}\subset H\). Its points are centered functions \(f\) satisfying \(|f_u-f_v|\le d_t(u,v)\). A vertex of \(Q_{m,t}\) is equivalent to a facet of \(P_{m,t}\), with supporting equation \(\langle f,x\rangle=1\). This precise normalization makes its distance from the origin \(1/\|f\|_2\).

## Proof
**1. Extreme dual functions.** For any feasible function, join two points when their difference saturates their metric distance. The resulting tight graph is connected exactly at dual vertices. If connected, any midpoint decomposition has identical increments on every tight edge and so both summands agree up to a constant. Conversely, a non-tight connected component can be shifted slightly in both directions, using finite positive slack on crossing pairs. This elementary argument is valid for all real \(t\).

Suppose a dual vertex has oscillation \(t\) on \(A\), and translate its minimum on \(A\) to zero. Every value on \(B\) lies between \(t-1\) and \(1\). Tight connectivity forces every \(A\)-value to be either zero or \(t\), both occurring, and each \(B\)-value to be \(t-1\) or \(1\): any intermediate value has no tight edge. Conversely every such assignment has a connected tight graph (the two \(A\) levels are joined by tight same-part pairs; every \(B\) point is attached to its matching level). Symmetrically there is the disjoint \(B\)-split family. If neither part reaches oscillation \(t\), no same-part pair is tight. Tight cross paths have even length between same-part points, forcing their function difference to be an even integer; since its magnitude is less than \(t<2\), it vanishes. There are only two resulting dual vertices, constant on each part at levels separated by one. Hence these three types exhaust all dual vertices; the split types have cardinalities \((2^m-2)2^m\) each and the total is \(2(2^m-1)^2\). This enumeration is established prior art (see References) and is reconstructed here to justify the exact normal ranges.

**2. Squared normal lengths.** In one split family let \(a\in\{1,\ldots,m-1\}\) be the number of \(A\)-values equal to \(t\), and \(b\in\{0,\ldots,m\}\) the number of \(B\)-values equal to \(1\); the others in \(B\) equal \(t-1\). Write \(S=at+m(t-1)+b(2-t)\) for the sum of its \(2m\) values. Its sum of squared values is exactly \(tS-m(t-1)\). Subtracting the squared mean yields
\[
\|f-\bar f\mathbf1\|_2^2
=\frac m2\bigl(1+(t-1)^2\bigr)
-\frac{(at+(2-t)b-m)^2}{2m}.\tag{4}
\]
The other split family has the same distribution, with the two parts exchanged. Each of the two constant-on-part vertices has squared centered norm \(m/2\). If \(m\) is even, \(a=b=m/2\) gives zero error in (4). If \(m=2k+1\) is odd, \(a=k,b=k+1\) gives error \(t-1\). Consequently \(\Delta_m(t)\le t-1\) in every case, and (4) gives a strictly larger squared norm than \(m/2\) for \(1<t<2\). Thus the globally largest dual normal length squared is exactly the bracket in (1).

**3. Radius and contact count.** Central symmetry gives the sharp inradius at the origin: for any containing ball centered at \(c\), the opposite ball centered at \(-c\) also lies in \(P_{m,t}\); their Minkowski midpoint is the same-radius ball centered at zero. Equivalently, the opposite facet pair with maximum-length normal forces \(r\le1/\max_{f\in Q_{m,t}}\|f\|_2\), and the centered ball attains equality for every facet. Since the two split families are disjoint for \(1<t<2\), equality in (4) gives exactly the \(\mathcal E_m(t)\) split profiles on each side. Choosing the high-value subsets contributes \(\binom ma\binom mb\) distinct facets per profile, proving (1)--(2).

**4. Every optimal center.** Let \(U\subset H\) denote all centered facet normals attaining maximal norm. Because \(U\) contains opposite pairs, a center \(c\) supports a ball of radius \(r_m(t)\) only if \(\langle u,c\rangle=0\) for every \(u\in U\). Conversely, those equations imply that every contacting facet remains feasible with equality; finitely many other facets have strict slack at zero, so every sufficiently small \(c\in U^\perp\cap H\) is another optimal center. Therefore
\[
\dim_{\mathrm{aff}}\mathcal C_m(t)=\dim H-\dim\operatorname{span}U.\tag{5}
\]
For every minimizing profile, permuting the nontrivial core split inside \(A\) makes differences of contact normals span the \((m-1)\)-dimensional zero-sum subspace supported on \(A\). Exchanging the two parts does the same on \(B\). Thus \(\operatorname{span}U\) contains the direct sum of these subspaces, a codimension-one subspace of \(H\). An additional contrast direction appears exactly when some contact normal has unequal means on \(A\) and \(B\).

For even \(m\), \(\Delta_m(t)=0\), so the total uncentered sum of every contacting split normal is \(mt\). The means on the two parts are equal exactly when \(at=m t/2\), that is \(a=m/2\), then necessarily \(b=m/2\). Hence a one-dimensional center locus occurs precisely when the central profile is the sole minimizer.

For odd \(m\), if a contacting split normal had equal part means, its total sum would be \(2at\); the deviation from \(mt\) would have magnitude \(|2a-m|t\ge t\). But the minimizing deviation is at most \(t-1<t\), a contradiction. Hence the contacting normals span all of \(H\) and the center is unique. This proves (3).

**5. Arithmetic phenomena.** For odd \(m\) and irrational \(t\), the equation \((a-b)t=m-2b\) cannot hold: if \(a\ne b\) it would make \(t\) rational, and if \(a=b\) it would require \(m=2b\), impossible for odd \(m\). At \(t=3/2\), take integer \(a\) with \(m/3\le a\le2m/3\), \(1\le a\le m-1\), and set \(b=2m-3a\); this gives an allowed zero-error profile for every \(m\ge3\). For even \(m=4\), \(t=4/3\) admits the noncentral profiles \((a,b)=(1,4),(3,0)\) in addition to \((2,2)\), so (2)--(3) give 88 contacts and a unique center; any irrational \(t\) has only \((2,2)\), giving 72 contacts and a center segment. All assertions follow.

## Verification
The standalone `verify_inball.py` uses exact rational arithmetic for the metric inequalities, all predicted dual potentials, the normal-length formula, contact counts and tangent-normal span (with a numerical rank tolerance for the last step). Its independent NumPy/SciPy halfspace-intersection routine reconstructs the entire dual vertex set from all pairwise metric inequalities for each of six configurations with \(m=2,3\) and \(t\in\{4/3,3/2,7/4\}\). All six independently reconstructed sets match the proved classification. Nine further cases with \(m=4,5,6\) compare all classified vertices, exact extremal squared norms, contact multiplicities and optimal-center affine dimensions. The checker reports `ALL EXACT METRIC AND EUCLIDEAN-INBALL CHECKS PASSED`. Computed cases are corroborative; the infinite-family theorem rests on steps 1--5, not the finite enumeration. NumPy/SciPy are required only by the verification program, not the proof.

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018, Theorem 3.1 and Proposition 3.4) identify the corresponding facet normals for the ordinary unit-edge complete-bipartite graph at \(t=2\), and their arithmetic analysis is not an inradius theorem. Alexander, Fradelizi, García-Lirola and Zvavitch (2019/2020) establish foundational Lipschitz-free/transportation-polytope duality and decompositions. Cobollo, Guirao and Montesinos (2023) study numerical indices of two-dimensional Lipschitz-free spaces, rather than these growing-dimensional inballs.

A publicly available exact classification of the facet *count* throughout \(1<t<2\) establishes the normal families reused in proof step 1, but does not compute their Euclidean lengths, nearest-facet profiles, optimal-center dimension or arithmetic resonances. Separate complete-multipartite inradius studies concern the unit-edge graph endpoint \(t=2\), often with at least three parts, and do not imply the interior-parameter theorem here. The new claim is exclusively (1)--(3) and their parity/resonance consequences, not the previously known facet enumeration or tight-graph criterion.

## Limitations
The claim covers only the balanced two-part metric with \(m\ge2\) and the strict interior snowflake parameter \(1<t<2\). It does not assert continuity of facet counts at the endpoints, affine invariance of the Euclidean radius, or any result for unequal parts. The source literature uses several polar coordinate conventions; every formula above is for the zero-sum ambient Euclidean metric. Exact computation was independently repeated only through dual dimension five; larger finite tests rely on the reconstructed analytic classification and do not certify other dimensions. Independent scientific validation has not been performed. A differently named published result or table could still contain the same radius/center formula.

## References
1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, 2018-07-20, https://arxiv.org/pdf/1807.07678 (especially Theorem 3.1 and Proposition 3.4).
2. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public 2019-11-24, https://arxiv.org/pdf/1911.10642.
3. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, 2023-04-25, https://arxiv.org/pdf/2304.13183.
4. *Sharp facet-count transitions for snowflaked complete bipartite metrics*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-facet-count-transitions-for-snowflaked-complete-bipartite--e855a74da4ce .
5. *Exact Euclidean inradius and tangent-facet phase of complete multipartite symmetric edge polytopes*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-and-tangent-facet-phase-of-complete-mul--6a4ae3f39c96 .
