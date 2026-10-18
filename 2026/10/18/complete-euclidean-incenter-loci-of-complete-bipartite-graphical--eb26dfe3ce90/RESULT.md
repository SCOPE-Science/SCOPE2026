# Complete Euclidean incenter loci of complete-bipartite graphical zonotopes

## Finding

For integers \(2\le p\le q\), let \(A\) and \(B\) be disjoint classes of orders \(p\) and \(q\), set \(n=p+q\), and consider the centered graphical zonotope
\[
 Z_{p,q}=\sum_{i\in A,\,j\in B}\left[-\tfrac12(e_i-e_j),\tfrac12(e_i-e_j)\right]
 \subset H=\{z\in\mathbb R^{n}:\sum_i z_i=0\}.
\]
Its maximum intrinsic Euclidean-ball radius is
\[
 r_{p,q}=\begin{cases}1,&(p,q)=(2,2),\\ \frac p2\sqrt{\frac{n}{n-1}},&\text{otherwise}.\end{cases}
\]
(The radius is already implied by the published weighted-graph cut-expansion formula [3]; this article does **not** claim it as new.) The new classification is that the affine dimension of the **entire set** \(\mathcal I_{p,q}\subset H\) of centers of balls of radius \(r_{p,q}\) is
\[
 \boxed{\dim\operatorname{aff}\mathcal I_{p,q}=\begin{cases}
 1,&p=q=2,\\ p-1,&2\le p<q,\\0,&3\le p=q.
 \end{cases}}
\]
For \(p<q\), every such center has zero coordinates on \(B\), but its \(A\)-coordinates vary in a full-dimensional centrally symmetric polytope in the zero-sum subspace of \(\mathbb R^A\); for \(p=q\ge3\), the origin is the **only** center. Explicit inequalities for all rectangular centers are provided below.

There is an additional exact classification for \(p=2<q\). Writing the coordinates in the order \(A,A,B,\ldots,B\), put
\[
 F_q=\left\lfloor\frac{(q+2)^2}{4}\right\rfloor,
 \qquad T_q=\frac q2-\sqrt{\frac{F_q}{q+1}}>0.
\]
Then
\[
 \boxed{\mathcal I_{2,q}=\{(t,-t,0,\ldots,0): |t|\le T_q\}}.
\]
The origin-centered maximum ball contacts exactly \(2q\) facets, whereas an endpoint-centered maximum ball contacts exactly \(2q+E_q\) facets, where
\[
 E_q=\begin{cases}\binom q{q/2},&q\text{ even},\\
 2\binom q{(q-1)/2},&q\text{ odd}.
 \end{cases}
\]
In the exceptional \(K_{2,2}\) case,
\[
 \boxed{\mathcal I_{2,2}=\{t(1,1,-1,-1):|t|\le1-\sqrt3/2\}}.
\]
The central ball there contacts four facets, and either endpoint-centered ball contacts eight facets. For every \(p=q\ge3\), the origin-centered ball contacts exactly \(2(p+q)\) facets.

## Assumptions and scope

All edge-segment generators have unit Euclidean length in incidence coordinates up to the factor \(1/2\) shown, and all balls, distances, and affine dimensions use the induced Euclidean metric on \(H\). The result includes \(p=q=2\) but not stars with a singleton part, other graphs, other Euclidean realizations, or nonuniform edge weights. A "contact facet" means a facet whose supporting hyperplane is tangent to the specified maximal ball. Opposite facets count separately.

Here is a compact exact description of **every** center for \(p<q\), stronger than a dimension formula. For \(1\le a\le p-1\), define the explicit positive constants
\[
 \beta_a=\min_{0\le b\le q}\left\{
 \frac{a(q-b)+b(p-a)}2
 -\frac p2\sqrt{\frac{(a+b)(n-a-b)}{n-1}}\right\}.
\]
Then
\[
 \boxed{\mathcal I_{p,q}=\left\{(x,0_B):
 \sum_{i\in A}x_i=0,\quad
 \left|\sum_{i\in T}x_i\right|\le\beta_{|T|}
 \text{ for all }\varnothing\ne T\subsetneq A\right\}.}
\]
This is a finite cardinality-indexed inequality classification and can be evaluated with \(O(pq)\) scalar candidate evaluations before constructing its symmetric coordinate inequalities.

## Proof

**1. Exact cut inequalities and ball containment.** For each nonempty proper vertex set \(S\subsetneq A\sqcup B\), let \(s=|S|\), \(a=|S\cap A|\), and \(b=|S\cap B|\). Write \(D(S)=|\delta(S)|=a(q-b)+b(p-a)\) and \(v_S=\mathbf1_S-(s/n)\mathbf1\in H\), so \(\|v_S\|_2=\sqrt{s(n-s)/n}\). Since the support function of the centered graphical zonotope satisfies \(h_Z(v_S)=D(S)/2\),
\[
 Z_{p,q}=\{z\in H:|\langle z,v_S\rangle|\le D(S)/2
 \text{ for every }\varnothing\ne S\subsetneq A\sqcup B\}.
\]
For completeness, if \(u\in H\) has minimum \(m\) and maximum \(M\), the level-set decomposition \(u=\int_m^M v_{\{i:u_i>t\}}dt\) shows that satisfying all these cut inequalities bounds \(\langle z,u\rangle\) by the zonotope's support function \(\tfrac12\sum_{ij\in E}|u_i-u_j|\). The support-function criterion for convex-body membership proves the displayed equality; no facet-completeness assumption is needed. Consequently a ball with center \(c\) and radius \(r\ge0\) is contained in \(Z_{p,q}\) **if and only if**
\[
 \boxed{|\sum_{i\in S}c_i|+r\sqrt{\frac{s(n-s)}n}\le\frac{D(S)}2\quad\text{for every such }S.}\tag{1}
\]
Central symmetry shows that the origin is an incenter: if \(c+rB_H\subset Z\), then \(-c+rB_H\subset Z\), so their midpoint ball \(rB_H\subset Z\). Thus the largest radius is the smallest cut ratio \(D(S)/(2\|v_S\|)\).

**2. A sharp singleton-cut transition.** The Laplacian of \(K_{p,q}\) has nonzero eigenvalues \(p\) with multiplicity \(q-1\), \(q\) with multiplicity \(p-1\), and \(n\) once. Its spectral gap is \(p\). Applying the Rayleigh inequality to \(v_S\) yields
\[
 D(S)=v_S^{\mathsf T}Lv_S\ge\frac pn\,s(n-s).
\]
For \(n\ge6\), every \(2\le s\le n-2\) satisfies \(s(n-s)\ge2(n-2)>n^2/(n-1)\). Hence every such cut has
\[
 \frac{D(S)}{2\|v_S\|}>\frac p2\sqrt{\frac n{n-1}}.
\]
Singleton cuts in \(B\) have \(D=p\) and attain equality; those in \(A\) have \(D=q\), giving equality only for \(p=q\). For \(n=5\), necessarily \((p,q)=(2,3)\). Each two-vertex cut has at least three crossing edges; since \(s(n-s)=6\), its ratio is strictly above the singleton-\(B\) ratio. Complementation handles three-vertex cuts. For \(n=4\), necessarily \(K_{2,2}\). Its mixed two-vertex cuts have \(D=2\), \(\|v_S\|=1\), giving radius \(1\), while all other cuts have strictly larger ratios. This establishes the radius and exhaustively identifies the closest *cut-support hyperplanes*. A cut is a facet exactly when both induced shores are connected; every closest cut listed above has this property.

**3. Rigidity, freedom, and exact rectangular center inequalities.** If a cut satisfies equality at the origin in (1), its two opposite supporting facets must both contain the centered optimal ball. For any other optimal center, (1) forces \(\sum_{i\in S}c_i=0\). For \(p<q\), the equality cuts are precisely the singleton vertices of \(B\), and so \(c_j=0\) for every \(j\in B\). Their projected normals have rank \(q\) in the \((n-1)\)-dimensional \(H\). For \(p=q\ge3\), the singleton cuts at every vertex are equality cuts and force \(c=0\). For \(K_{2,2}\), the equality mixed cuts force \(c=t(1,1,-1,-1)\).

For \(p<q\), substitute \(c=(x,0_B)\) into (1). If \(a=0\) or \(a=p\), the cut sum of \(c\) is zero, and (1) already holds at the origin. If \(1\le a\le p-1\), it becomes \(|\sum_{i\in T}x_i|\le g_a(b)\), where
\[
 g_a(b)=\frac{a(q-b)+b(p-a)}2
 -\frac p2\sqrt{\frac{(a+b)(n-a-b)}{n-1}},
 \qquad T=S\cap A.
\]
Every subset of \(B\) of each cardinality \(0\le b\le q\) exists, so the joint condition is exactly the stated \(\beta_a=\min_b g_a(b)\). Every \(\beta_a\) is *strictly positive*: the only cut-hyperplane equalities at the origin are the singleton-\(B\) cuts and their complements, neither of which has \(1\le a\le p-1\). Hence this system contains a relative neighborhood of \(0\) in \(\{(x,0_B):\sum_Ax_i=0\}\), and its affine dimension is exactly \(p-1\). For balanced \(p=q\ge3\) the center is unique, as already shown.

**4. Exact two-row segment and endpoint contacts.** For \(p=2<q\), the zero-sum \(A\)-subspace is one-dimensional, so write \(x=(t,-t)\). Cuts with exactly one \(A\) vertex and \(b\) vertices in \(B\) have \(D=q\), yielding
\[
 |t|\le\frac q2-\sqrt{\frac{(b+1)(q+1-b)}{q+1}},\qquad0\le b\le q.
\]
The product \((b+1)(q+1-b)\) has integer maximum \(F_q=\lfloor(q+2)^2/4\rfloor\). This proves the segment and its strict positive length. At \(t=0\), only the \(2q\) oriented singleton-\(B\) facets touch. At either nonzero endpoint, the same \(2q\) facets touch and, additionally, one oriented mixed-cut facet is tangent for each \(B\)-subset with \(b=q/2\) if \(q\) is even, or \(b=(q-1)/2\) or \((q+1)/2\) if \(q\) is odd. Distinct such subsets give distinct facets and exhaust equality in (1). The binomial formula for \(E_q\) follows. Finally, for \(K_{2,2}\), the mixed-cut equalities give \(c=t(1,1,-1,-1)\); its singleton inequalities give \(|t|\le1-\sqrt3/2\), strictly stronger than the two pure-shore inequalities \(|2t|\le1\). The two mixed complementary cut pairs give four always-contacting oriented facets, and the four singleton facets contribute one additional orientation each at a segment endpoint. All claims follow.

## Verification

The standalone standard-library script `checker.py` enumerates all nontrivial cuts for every \(K_{p,q}\) with \(2\le p\le q\) and \(p+q\le14\), computes exact integer squared support-distance comparisons, and calculates rational ranks of active cut normals. It verifies 36 complete-cut profiles and the predicted dimensions. A separate 75-digit numerical cross-check enumerates all cuts at both explicit endpoint centers of \(K_{2,q}\) for \(3\le q\le11\), verifying all inequalities and contact-pair counts. Invoke `python3 checker.py`; the replay passed. These finite checks corroborate but do not replace the spectral, exact-cut, and equality proofs above.

## Relationship to prior work

Padrol, Pilaud, and Poullot [1] treat graphical zonotope deformation geometry, and Chapoton and Pilaud [2] treat the complete-bipartite graphical zonotope as a shuffle in the standard family. Their inspected full texts address combinatorial and realization questions, not all Euclidean inball centers. The published weighted graphical-zonotope cut-expansion theorem [3] already establishes the numerical inradius in greater generality but expressly does not classify nonunique Chebyshev centers. A published result [4] determines the **Löwner** ellipsoid and its contact **vertices** for precisely these complete-bipartite zonotopes; the outer ellipsoid does not determine the incenter locus or inner contact facets. This result claims only the complete all-center classification, its dimensional transitions, and the explicit two-row endpoint contact count as new.

## Limitations

The classification is specific to the standard unit-edge graphical zonotope and its intrinsic Euclidean metric, not any affine equivalent realization. It does not classify centers for arbitrary graph or edge weights. The radius alone is previously covered and is included only to normalize the novel center results. No independently audited mathematical proof is claimed. Unindexed formulations of this incenter classification remain a possible bibliographic risk.

## References

[1] A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted November 24, 2021.

[2] F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first posted January 18, 2022.

[3] *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, published-finding corpus public research record 2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab, RESULT.md, inspected full text.

[4] *Exact Löwner ellipsoid and contact vertices of complete-bipartite graphical zonotopes*, published-finding corpus public research record 2026/10/11/SCOPE-exact-l-wner-ellipsoid-and-contact-vertices-of-complete-bipartit--3af21ae2f6c8, RESULT.md, inspected full text.
