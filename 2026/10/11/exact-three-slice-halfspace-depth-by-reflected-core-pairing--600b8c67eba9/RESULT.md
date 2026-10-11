# Exact three-slice halfspace depth by reflected-core pairing
## Finding
For every integer \(d\ge 2\), let \(K\subset\mathbb R^d\) be a full-dimensional compact convex body, and let \(0\in\operatorname{int}K\) maximize its normalized halfspace depth. Put
\[
\delta(K)=\max_{x\in K}\inf_{\substack{G\text{ closed halfspace}\\x\in G}}\frac{|K\cap G|}{|K|}.
\]
For any \(0<r\le1\) satisfying the reflection inclusion \(-rK\subseteq K\), consider the three discrete slices
\[
S_r=(\{0\}\times rK)\cup(\{1\}\times K)\cup(\{2\}\times K).
\]
Equip them with the sum of their \(d\)-dimensional volumes. Then their **maximum normalized halfspace depth is exactly**
\[
\boxed{\max_{y\in S_r}\operatorname{depth}_{S_r}(y)
=\frac{\delta(K)+r^d}{2+r^d}},
\]
attained at \(y=(1,0)\). Here a point's depth is the minimum fraction of total slice volume contained in any closed ambient halfspace through that point.

In particular, for every \(d\)-simplex \(\Delta\) centered at its centroid and \(0<r\le1/d\), the exact maximum is
\[
\frac{(d/(d+1))^d+r^d}{2+r^d}.
\]
Writing \(\varepsilon=r^d/(2+r^d)\) for the fraction of total mass in the smallest slice, the simplex profile is **exactly linear**:
\[
\frac12\left(\frac{d}{d+1}\right)^d+
\left(1-\frac12\left(\frac{d}{d+1}\right)^d\right)\varepsilon,
\qquad 0<\varepsilon\le\frac1{2d^d+1}.
\]
For planar triangles this becomes \(2/9+7\varepsilon/9\) throughout \(0<\varepsilon\le1/9\), rather than only in the vanishing-mass limit.

## Assumptions and scope
The symbol \(|\cdot|\) denotes \(d\)-dimensional Lebesgue volume. Every closed halfspace in the definition of \(\delta(K)\) lies in \(\mathbb R^d\), whereas those defining \(\operatorname{depth}_{S_r}\) lie in \(\mathbb R^{d+1}\). Explicitly, for a Borel set \(E\subset\mathbb R^{d+1}\), let
\[
\mu_r(E)=\sum_{i=0}^2\left|\left\{x\in\mathbb R^d:(i,x)\in E\cap S_r\right\}\right|,
\qquad
\operatorname{depth}_{S_r}(y)=\inf_{H\ni y}\frac{\mu_r(H)}{\mu_r(S_r)},
\]
where \(H\) runs over closed ambient halfspaces. Thus \(\mu_r(S_r)=(2+r^d)|K|\). The origin is assumed to be a *global* maximizer of the ordinary halfspace depth on \(K\), not necessarily its centroid. Translating any halfspace-depth maximizer to the origin is always possible. Because that maximizer is interior, the condition \(-rK\subseteq K\) holds for all sufficiently small positive \(r\) for every such \(K\). The theorem does not assume that \(K\) is symmetric, smooth, a polytope, or a simplex.

## Proof
**Step 1: a lower bound at the middle depth maximizer.** Fix any closed halfspace \(H\subset\mathbb R\times\mathbb R^d\) containing \((1,0)\). Moving its boundary inward to pass through \((1,0)\) can only decrease its mass. Such a boundary halfspace is
\[
H=\{(i,x):\langle u,x\rangle+t(i-1)\ge0\}
\]
for some \((u,t)\ne(0,0)\). If \(u\ne0\), its middle section is the halfspace \(\langle u,x\rangle\ge0\), which, by the maximizing-depth hypothesis, captures at least \(\delta(K)|K|\) of \(K\).

Write \(B=\{x\in rK:\langle u,x\rangle<t\}\) for the part of the bottom slice excluded by \(H\). If \(x\in B\), then \(-x\in K\) because \(-rK\subseteq K\), and
\[
\langle u,-x\rangle+t>0.
\]
Thus the top slice contains the reflected copy \(-B\), of volume \(|B|\). The bottom slice contains \(|rK|-|B|\), so the combined mass of the two outer slices is at least \(r^d|K|\). Adding the middle mass yields
\[
\mu_r(H)\ge(\delta(K)+r^d)|K|.
\]
If \(u=0\), \(H\) contains all of the middle slice and at least one outer slice. Since \(r\le1\) and \(\delta(K)\le1\), the same lower bound holds. It also holds for all halfspaces whose boundaries initially missed \((1,0)\). Therefore
\[
\operatorname{depth}_{S_r}(1,0)\ge\frac{\delta(K)+r^d}{2+r^d}.
\]

**Step 2: sharpness at every candidate point.** For every \(x\in K\), by the definition of \(\delta(K)\), there is a closed \(d\)-dimensional halfspace through \(x\) with captured \(K\)-mass at most \(\delta(K)|K|\): the minimizing direction exists because the volume of a halfspace section of a full-dimensional convex body varies continuously with its unit normal. Choose such a direction \(u\), and a sufficiently large positive constant \(T\). The ambient halfspace
\[
\{(i,z):\langle u,z-x\rangle-T(i-1)\ge0\}
\]
passes through \((1,x)\), contains all of the bottom slice, and contains none of the top slice. Therefore its mass is at most \((r^d+\delta(K))|K|\), giving the desired upper bound for every middle-slice point. For every top-slice point \((2,x)\), the similarly tilted halfspace
\[
\{(i,z):\langle u,z-x\rangle+T(i-2)\ge0\}
\]
misses the bottom and middle slices, capturing at most \(\delta(K)|K|\) on top. For any bottom-slice point, the horizontal halfspace \(\{i\le0\}\) captures only \(r^d|K|\). Since both latter quantities are at most \((r^d+\delta(K))|K|\), no point of \(S_r\) can have greater depth than \((1,0)\). This proves the exact identity.

**Step 3: the simplex specialization and sharp reflection window.** Let \(\Delta=\operatorname{conv}\{v_0,\ldots,v_d\}\), with \(\sum_{i=0}^d v_i=0\). Grünbaum's sharp centroid halfspace inequality gives
\[
\inf_{G\ni0}\frac{|\Delta\cap G|}{|\Delta|}\ge
m_d:=\left(\frac d{d+1}\right)^d.
\]
Equality holds for a cap cut through the centroid parallel to any facet. More generally, every \(x\in\Delta\) has some barycentric coordinate at least \(1/(d+1)\); the parallel-facet cap on its vertex side has volume at most \(m_d|\Delta|\). Hence \(\delta(\Delta)=m_d\), attained at the centroid.

Let \(\lambda_j\) be barycentric coordinates. At the reflected vertex \(-rv_i\),
\[
\lambda_j(-rv_i)=\frac{1+r}{d+1}-r\mathbf 1_{\{i=j\}}.
\]
Thus \(-r\Delta\subseteq\Delta\) holds **if and only if** \(r\le1/d\): the condition is necessary at a vertex and sufficient at all vertices by convexity. Substitution of \(\delta(\Delta)=m_d\) into the exact identity gives the asserted profile. Since \(\varepsilon=r^d/(2+r^d)\), simple algebra gives \((m_d+r^d)/(2+r^d)=m_d/2+(1-m_d/2)\varepsilon\); the endpoint is \(\varepsilon=1/(2d^d+1)\). For \(d=2\), \(m_2=4/9\), yielding \(2/9+7\varepsilon/9\) and endpoint \(1/9\). Every bound is an equality, not merely an asymptotic estimate.

## Verification
The proof relies on an explicit volume-preserving reflection, elementary halfspace tilting, the standard sharp Grünbaum inequality at a simplex centroid, and barycentric coordinates. The standalone `verify.py` uses Python's rational arithmetic to clip the triangle with vertices \((-1,-1)\), \((2,-1)\), \((-1,2)\), checks 5,324 deterministic three-slice halfspace instances at four admissible rational radii, realizes the matching cap exactly, and checks the dimensional and normalized-mass identities. Executing `python3 verify.py` prints `VERIFY_OK 5390 exact-rational assertions`. Finite clipping checks illustrate the argument only; the all-body, all-dimension, all-halfspace theorem is proved by Steps 1--3.

## Relationship to prior work
Cheng and Basu (arXiv:2609.32953v1, 26 September 2026) prove that arbitrary admissible three-slice planar configurations have some point of normalized halfspace depth at least \(2/9\), and show that this bound is asymptotically sharp using one small homothetic triangle and two equal larger triangles. In their sharpness family, they derive the finite-parameter **upper bound** \(2/9+7\varepsilon/9\), but only take the limit \(\varepsilon\downarrow0\). The present exact theorem supplies the missing matching lower bound for the entire geometrically natural reflection-inclusion interval \(0<\varepsilon\le1/9\), proves that the middle centroid is an optimizer, and explains the mechanism through reflection of excluded mass. The general statement applies to arbitrary convex depth-maximizing cores in every \(d\ge2\), not only triangles.

A separate published refinement, *Equal-area three-slice centerpoints improve to \(8/27\)*, assumes all three slice areas are equal and derives translation rigidity by equality in Brunn--Minkowski. Its equal-area hypothesis does not apply to the unequal-slice regime \(0<r\le1/d\) of the present simplex profile, and its lower-bound statement is not the present exact maximum formula. Grünbaum's inequality controls one continuous slice and alone cannot supply the three-slice reflection pairing.

## Limitations
The exact structural identity requires both that \(0\) maximize the ordinary halfspace depth of \(K\) and that \(-rK\subseteq K\). No conclusion about the exact maximum beyond this reflection-inclusion interval is claimed. The simplex endpoint \(r=1/d\) is sharp for the inclusion hypothesis, not a claimed phase transition in depth after that endpoint. The all-dimensional theorem is specific to a stack consisting of one homothetic copy and two identical copies; it does not establish a universal depth formula for arbitrary three convex slices, four or more slices, or other mixed-integer lattice configurations. An unindexed equivalent reflection-pairing lemma remains a possible bibliographic risk.

## References
1. Hongyu Cheng and Amitabh Basu, *A centerpoint theorem for three planar convex bodies*, arXiv:2609.32953v1, first submitted 26 September 2026, https://arxiv.org/html/2609.32953v1. Relevant parts: Introduction, Theorem 1, its sharpness construction, and Conclusions.
2. Branko Grünbaum, *Partitions of mass-distributions and of convex bodies by hyperplanes*, Pacific Journal of Mathematics **10** (1960), 1257--1261. Sharp centroid halfspace inequality.
3. *Equal-area three-slice centerpoints improve to \(8/27\)*, publicly available result, https://raw.githubusercontent.com/published-finding corpus/2026/main/2026/10/4/SCOPE-equal-area-three-slice-centerpoints-improve-to-8-27--fd7da08a5159/RESULT.md. Compared for equal-area coverage.
