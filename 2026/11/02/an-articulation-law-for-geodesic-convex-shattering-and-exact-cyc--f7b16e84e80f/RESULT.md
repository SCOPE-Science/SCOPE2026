# An articulation law for geodesic-convex shattering and exact cycle-bouquet profiles

## Finding
For a finite connected simple graph \(H\), let \(\mathcal C(H)\) be the family of all geodesically convex vertex subsets, including the empty and full sets. Define its shattered-support polynomial by
\[
\Phi_H(z)=\sum_{S\subseteq V(H):\,\mathcal C(H)|_S=2^S}z^{|S|}.
\]
For a distinguished vertex \(r\), define the rooted trace polynomial
\[
\Psi_{H,r}(z)=\sum_{S\subseteq V(H)\setminus\{r\}:\,\mathcal C_r(H)|_S=2^S}z^{|S|},\qquad
\mathcal C_r(H)=\{C\in\mathcal C(H):r\in C\}.
\]
Let \(G\) be the one-vertex union of \(t\ge2\) finite connected simple graphs \(H_1,\ldots,H_t\), all identified at a single vertex \(r\) and otherwise vertex-disjoint. Then
\[
\boxed{\Phi_G(z)=\prod_{i=1}^t\Psi_{H_i,r}(z)+\sum_{i=1}^t(\Phi_{H_i}(z)-\Psi_{H_i,r}(z))-(t-1)z.}
\]
Writing \(\rho_i=\deg\Psi_{H_i,r}\) and \(d_i=\operatorname{VCdim}(\mathcal C(H_i))\), this also gives the exact dimension law
\[
\boxed{\operatorname{VCdim}(\mathcal C(G))=\max\left\{\sum_{i=1}^t\rho_i,\ \max_i d_i\right\}.}
\]

In particular, let \(B(m_1,\ldots,m_t)\) be the graph obtained by identifying one vertex of each cycle \(C_{m_i}\), where \(m_i\ge3\). Put \(h_i=\lfloor(m_i-1)/2\rfloor\) and
\[
T_m=\begin{cases}m(m^2-1)/24,&m\text{ odd},\\m(m-2)(m-4)/24,&m\text{ even}.\end{cases}
\]
Its **entire** shattered-support polynomial is
\[
\boxed{\begin{aligned}
\Phi_{B(m_1,\ldots,m_t)}(z)={}&\prod_{i=1}^t\left(1+(m_i-1)z+h_i^2z^2\right)+z\\
&+\sum_{i=1}^t\left[\left(\binom{m_i}{2}-h_i^2\right)z^2+T_{m_i}z^3\right].
\end{aligned}}
\]
For every \(t\ge2\), independently of the cycle lengths,
\[
\boxed{\operatorname{VCdim}(\mathcal C(B(m_1,\ldots,m_t)))=2t,\qquad
\#\{\text{maximum shattered supports}\}=\prod_{i=1}^t h_i^2.}
\]
As an explicit instance, a bouquet of \(t\) pentagons has polynomial
\[
(1+2z)^{2t}+z+6tz^2+5tz^3.
\]
For three pentagons, its coefficients in degrees zero through six are \(1,13,78,175,240,192,64\).

## Assumptions and scope
All graphs are finite, simple, connected and unweighted. A set is geodesically convex if it contains **every** shortest path between any two of its vertices; the empty set and singletons are convex. Shattering means that each Boolean trace on the support is realized by some convex set. The one-vertex union introduces no edges between different factors other than those through the shared root. The cycle-bouquet conclusion requires at least two cycles for its dimension and maximal-count formula; the displayed polynomial remains valid also for one cycle.

## Proof
**1. Geodesic decomposition at the articulation.** Every shortest path with both endpoints in a factor \(H_i\) remains in \(H_i\): a route leaving that factor would have to revisit \(r\) and could not be shortest. Every shortest path between distinct factors is a concatenation of shortest paths from one endpoint to \(r\) and from \(r\) to the other endpoint. Thus a convex set containing \(r\) is exactly a union of convex factor sets all containing \(r\); a nonempty convex set avoiding \(r\) is contained in one factor, where it is convex.

**2. Classification of shattered supports.** Let \(S\) avoid \(r\), and put \(S_i=S\cap(V(H_i)\setminus\{r\})\). If \(S\) meets at least two factors, it is shattered precisely when every \(S_i\) is shattered by the rooted family \(\mathcal C_r(H_i)\). Sufficiency follows by selecting rooted convex sets with each prescribed local trace and taking their union. For necessity, a nonempty prescribed trace in \(S_i\) can be combined with a positive selected point in another factor; any realizing convex hypothesis then contains \(r\), and its restriction to \(H_i\) supplies the prescribed rooted trace. The empty trace is always supplied by \(\{r\}\). If \(S\) lies in one factor, it is shattered precisely when it is shattered by that factor's full convex family, because restrictions of global convex hypotheses are convex and every local hypothesis is globally convex.

If \(S\) contains \(r\) and meets at least two factors outside \(r\), the trace with \(r\) negative and two points in distinct factors positive is impossible. Otherwise \(S\) lies in one factor and is shattered precisely when it is shattered there. The support \(\{r\}\) is included once globally but is counted in each factor. Hence the rooted product counts all multi-factor root-free supports and the rooted-shattered single-factor supports; each difference \(\Phi_{H_i}-\Psi_{H_i,r}\) adds the remaining single-factor supports and the root-containing supports. Correcting the \(t\)-fold count of \(\{r\}\) proves the stated identity.

For the dimension law, every shattered support has either size at most \(\sum_i\rho_i\) when it uses the rooted product, or at most \(\max_i d_i\) when it is confined to one factor. Both bounds are attained: concatenate locally maximal rooted-shattered supports in the root-free product, or embed a maximum shattered support from one factor. This proves the maximum formula.

**3. A rooted cycle.** Fix \(r\) in \(C_m\) and write \(h=\lfloor(m-1)/2\rfloor\). There are two sides of \(r\), each with \(h\) non-antipodal vertices; when \(m\) is even there is one additional antipodal vertex. Any two points on the same side are not shattered by rooted convex sets: the shorter path from \(r\) to the farther one contains the nearer one. A pair involving the antipode is not rooted-shattered because its convex hull with \(r\) is the entire cycle. Conversely, one point from each side forms a rooted-shattered pair: the two root-to-point short arcs realize the two singleton traces, while \(\{r\}\) and the full cycle realize the empty and double-positive traces. All nonroot singletons are rooted-shattered; three points cannot be rooted-shattered by this side/antipode obstruction. Therefore
\[
\Psi_{C_m,r}(z)=1+(m-1)z+h^2z^2.
\]

**4. The unrooted cycle.** Empty, one-point and two-point supports are shattered. Take three distinct cyclically ordered points, with positive arc gaps \(a,b,c\) summing to \(m\). The triple is shattered exactly when each gap is at most \(h\): if a gap is at least half the circumference, the remaining two gaps form a shortest path through the intervening selected point, forbidding a two-positive trace; if every gap is shorter than half the circumference, the short path between each pair avoids the third point, realizing all pair traces, while singletons, empty and full realize the others. No support of size four is shattered: for four successive selected points, the four adjacent two-gap sums add to \(2m\), so some such sum is at most \(m/2\), forcing the intermediate selected point into the shortest-path hull of its two neighbors.

Counting the shattered triples by choosing a starting vertex and positive gaps gives
\[
T_m=\frac m3\,\#\{(a,b,c)\in\{1,\ldots,h\}^3:a+b+c=m\}.
\]
For odd \(m=2k+1\), inclusion-exclusion gives \(\binom{2k}{2}-3\binom{k}{2}=k(k+1)/2\) ordered gap triples. For even \(m=2k\), the count is \(\binom{2k-1}{2}-3\binom{k}{2}=(k-1)(k-2)/2\). These are exactly the two displayed formulas for \(T_m\). Thus
\[
\Phi_{C_m}(z)=1+mz+\binom m2z^2+T_mz^3.
\]
Substituting the two cycle polynomials into the articulation identity proves the bouquet formula. Since each rooted factor polynomial has degree two with leading coefficient \(h_i^2>0\), and each correction has degree at most three, for \(t\ge2\) the product is the only contribution to degree \(2t\), proving both the exact VC dimension and the maximum-support count.

## Verification
The standalone standard-library program `verify_gluing.py` uses independent breadth-first shortest-path reconstruction and direct trace enumeration. It checks the full and rooted cycle profiles for cycle lengths \(3\) through \(12\), all \(1089\) ordered pairs from \(33\) small rooted graph representatives under one-vertex gluing, and six additional cycle-bouquet instances, including a three-pentagon bouquet. Run with `python3 verify_gluing.py`. Every comparison succeeded. These are finite consistency checks; the universal statements follow from the proofs above.

## Relationship to prior work
Thiessen and Gärtner (2022) study learning convex sets on graphs, including general VC and online-learning bounds; their Proposition 11 relates the VC dimension of a graph-convexity space to hull sets. It does not state a rooted shattered-support polynomial or an articulation identity. Chornomaz (2022) studies shattering-extremal set systems and convex geometries; the present calculation concerns a different object, an exact enumerator for all shattered supports of a graph-geodesic closure system, and does not assert that the families are shattering-extremal. Chepoi (2024) develops geodesic-convex separation and bounds on halfspaces; halfspaces are a restricted family rather than all convex sets. The standard cycle convexity facts and basic shattering definitions are not asserted to be new. The proposed contribution is the universal rooted gluing identity and its exact heterogeneous cycle-bouquet consequences.

## Limitations
The result treats **static** VC-shattering of all geodesically convex subsets, not online Littlestone dimension, halfspace-only hypotheses, edge-weighted graphs or arbitrary vertex overlaps. No independent scientific audit has been performed. The finite checker does not prove the all-parameter theorem. Historical priority under different terminology for rooted trace polynomials or one-point sums remains a residual risk.

## References
1. B. Chornomaz, *What Convex Geometries Tell About Shattering-Extremal Systems*, Electronic Journal of Combinatorics **29** (2022), P3.40, DOI: `10.37236/10750`, publicly available 2022-08-12.
2. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML-PKDD (2022), DOI: `10.1007/978-3-031-26412-2_22`, 2022 conference preprint openly available.
3. V. Chepoi, *Separation axiom \(S_3\) for geodesic convexity in graphs*, arXiv:`2405.07512`, first posted 2024-05-13.
