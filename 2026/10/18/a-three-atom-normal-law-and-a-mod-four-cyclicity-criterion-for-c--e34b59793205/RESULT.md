# A three-atom normal law and a mod-four cyclicity criterion for centrally symmetric hexagons

## Finding
Let \(P\) be a strictly convex, centrally symmetric Euclidean hexagon with all interior angles strictly greater than \(\pi/2\). A **normal through an interior point** \(x\) means a line joining \(x\) to a boundary point \(q\) and perpendicular to at least one supporting line of \(P\) at \(q\); distinct contact points are counted once. Let \(N_P(x)\) be the number of such contacts. Then

\[
P\text{ is cyclic}\quad\Longleftrightarrow\quad N_P(x)\equiv0\pmod4\text{ for almost every }x\in P.
\]

More precisely, if \(P\) is cyclic and \(X\) is area-uniform in \(P\), the complete law is supported on \(\{4,8,12\}\) and has the form
\[
\Pr(N_P(X)=4)=\Pr(N_P(X)=12)=\nu(P),\qquad
\Pr(N_P(X)=8)=1-2\nu(P).
\]
Write the vertices counterclockwise as \(v_0,v_1,v_2,-v_0,-v_1,-v_2\), with common circumradius \(R\). For \(i=0,1,2\), put \(e_i=v_{i+1}-v_i\), \(u_i=e_i/\lVert e_i\rVert\), and \(s_i=\lVert e_i\rVert/2\). Then the parameter is an exact finite polygon-area expression,
\[
\nu(P)=\frac{\operatorname{area}\bigl(P\cap\bigcap_{i=0}^{2}\{x:|x\cdot u_i|\le s_i\}\bigr)}{\operatorname{area}(P)}.
\]
The numerator is obtained without quadrature by intersecting twelve explicit half-planes and applying the shoelace formula. Specifically, use the six original edge half-planes and the six inequalities \(\pm x\cdot u_i\le s_i\); enumerate intersections of pairs of boundary lines with nonzero determinant, retain feasible points, order the distinct vertices cyclically, and sum their successive determinants.

For a regular hexagon, \(\nu(P)=1/3\), so the three normal counts \(4,8,12\) are **equiprobable**. For the nonregular cyclic hexagon whose successive central arc gaps in one semicircle are \(\pi/2,\pi/4,\pi/4\), direct exact half-plane intersection gives \(\operatorname{area}(P)=1+\sqrt2\) and the three-strip intersection area \(5-3\sqrt2\) at circumradius one. Hence \(\nu(P)=8\sqrt2-11\), proving that the probability parameter varies with shape. The law also implies \(\operatorname{Var}(N_P(X))=32\nu(P)\).

## Assumptions and scope
The ambient space is the Euclidean plane. Strict convexity of a polygon means that every interior angle is less than \(\pi\) and there are six genuine vertices; no smoothness is asserted. Central symmetry is about the origin after translation. The all-obtuse hypothesis is used for the reverse implication (detecting noncyclicity), while cyclic central hexagons automatically satisfy it. All assertions about normal counts hold off a finite union of exceptional lines and thus for almost every area-uniform point. A normal is counted by its boundary contact, not by the continuum of supporting lines at a polygon vertex.

## Proof
**(1) Side–vertex balance.** Fix an interior point \(x\) outside the finite set of degeneracy lines. Consider \(f(q)=\lVert q-x\rVert^2\) on the oriented boundary of an arbitrary convex polygon. On every open edge, \(f\) is strictly convex, so its interior critical points are strict local minima and correspond exactly to orthogonal foot contacts. At a vertex \(v\), with neighboring vertices \(a,b\), the condition that \([v,x]\) be normal is \((x-v)\cdot(a-v)>0\) and \((x-v)\cdot(b-v)>0\); it is exactly the strict local-maximum condition for the one-sided derivatives of \(f\). A vertex cannot be a local minimum: since \(x-v\) is a nonzero positive combination of the inward edge vectors \(a-v,b-v\), both corresponding scalar products cannot be negative. The continuous periodic boundary function therefore has equally many edge-interior minima and vertex maxima. If \(S_P(x)\) is the number of edge-interior orthogonal feet, then \(N_P(x)=2S_P(x)\).

**(2) Paired side-foot strips.** For a side \([a,b]\), put \(e=b-a\). Its foot is internal exactly when \(a\cdot e < x\cdot e < b\cdot e\). The opposite side \([-a,-b]\) has the corresponding interval \(-b\cdot e < x\cdot e < -a\cdot e\). These two intervals coincide if and only if \((a+b)\cdot e=0\), equivalently \(\lVert a\rVert=\lVert b\rVert\). Thus for a centrally symmetric *cyclic* hexagon the opposite sides are activated together, and, since their endpoints lie on a circle centered at the origin, each side pair contributes two feet precisely on the slab \(|x\cdot u_i|<s_i\). It follows that \(N_P(x)=4\sum_{i=0}^2\mathbf1_{\{|x\cdot u_i|<s_i\}}\).

For an interior point, a closest boundary point cannot generically be a vertex (the preceding no-vertex-minimum argument), hence at least one side foot exists. Paired activation makes the sum at least one, so \(N_P(x)\in\{4,8,12\}\). The maximum-count region is exactly the intersection of the three strips with \(P\), yielding the stated polygon-area expression for \(\nu(P)\).

**(3) Balance of the two extreme masses.** Hug's theorem on the average number of interior normals, in the cyclic centrally symmetric polygon equality case (restated explicitly in Domokos–Lángi, Section 3.1), gives \(\mathbb E N_P(X)=8\). With support \(\{4,8,12\}\), this reads \(4p_4+8p_8+12p_{12}=8\) together with \(p_4+p_8+p_{12}=1\), hence \(p_4=p_{12}\). Combined with step (2), this proves the complete law.

**(4) Mod-four rigidity.** Conversely, suppose \(P\) is centrally symmetric and all six interior angles are strictly obtuse. If it is not cyclic, at least one edge \([a,b]\) has \(\lVert a\rVert\ne\lVert b\rVert\). The two side-foot intervals from step (2) are therefore distinct reflected intervals. Their endpoint sets differ; at least one endpoint is an unpaired threshold where precisely one of the two opposite-side foot indicators changes. The associated line through an endpoint perpendicular to the side enters the interior of \(P\) along a positive-length segment, because the incident interior angle is strictly obtuse. Threshold lines arising from the other two nonparallel edge directions cannot coincide with this line, and their finitely many crossings may be avoided. Crossing at a generic interior point of its segment therefore changes \(S_P\) by exactly one and \(N_P\) by exactly two. Both adjacent open chambers have positive area, and they cannot both have normal counts divisible by four. Thus noncyclicity forces a positive-area set with \(N_P(x)\equiv2\pmod4\), proving the contrapositive.

**(5) The exact examples.** In a regular hexagon of circumradius one, the three foot slabs have halfwidth \(1/2\) and directions separated by \(\pi/3\). Their intersection is a regular hexagon of circumradius \(1/\sqrt3\), entirely inside \(P\), so its area ratio is \(1/3\). For arc gaps \(\pi/2,\pi/4,\pi/4\), vertices \((1,0),(0,1),(-1/\sqrt2,1/\sqrt2)\) and their negatives give the announced exact areas by solving the active linear inequalities and applying the shoelace formula. In the latter case \(\nu(P)=(5-3\sqrt2)/(1+\sqrt2)=8\sqrt2-11\).

## Verification
Run `python3 hexagon_normal_checker.py` from the directory containing this result and the supplied standalone checker. Its seeded independent side-foot/vertex-contact enumeration is compared pointwise against the paired-strip classification for 250,000 sampled points from five cyclic hexagons; polygon clipping and sampling independently compare the three probabilities. It also tests an obtuse noncyclic hexagon with 40,000 points and observes normal counts congruent to two modulo four. The checker confirms the regular ratio \(1/3\) numerically at machine precision and reports maximum empirical frequency discrepancy below \(0.005\) for its cyclic tests. Finite checking supports, but does not establish, the almost-everywhere or universal assertions; those are proved in the preceding steps.

## Relationship to prior work
Hug (1995) established bounds for average normal counts and the equality characterization for centrally symmetric cyclic polygons; Domokos and Lángi (arXiv:1406.0813, 2014) explicitly summarize the cyclic-polygon equality \(\mathbb E N=8\). That prior expectation is used in step (3), and is not presented as new. The present theorem instead determines the *full* three-point distribution for cyclic centrally symmetric hexagons, supplies a shape-dependent exact parameter and equidistribution example, and proves the converse almost-everywhere mod-four characterization among obtuse centrally symmetric hexagons. Prior work on regular odd polygons' average normal counts concerns a different parity and does not provide these distributions.

## Limitations
No distributional statement is made about hexagons that are not cyclic; the converse divisibility criterion requires all six interior angles to be strictly obtuse. The exact probability parameter is an explicit constant-size polygon-area computation, not a universal elementary expression in arbitrary arc gaps. The result is not a stable reconstruction theorem from noisy data, nor a classification of all polygons. Hug's original 1995 paper was not inspected in full; its relevant mean/equality theorem is quoted and checked in the accessible full 2014 account. Historical priority beyond the inspected sources and independent verification remain open.

## References
1. D. Hug, *On the mean number of normals through a point in the interior of a convex body*, Geometriae Dedicata **55** (1995), 319–340. DOI: 10.1007/BF01266322.
2. G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813, first submitted 2014-06-03; full author manuscript hosted at `https://real.mtak.hu/16578/1/DomokosLangi_revised.pdf`.
