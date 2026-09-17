# Saturation of fans with sufficiently many pendant edges

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.

Research date: 16 September 2026. This is a researcher self-assessed result, not independent validation.

## Claim

All graphs are finite, simple, undirected, and containment means ordinary, not induced, subgraph containment. A graph G is H-saturated if G contains no copy of H but adding any missing edge creates one. Write sat(n,H) for the minimum number of edges in such an n-vertex graph. The operation A join B adds all edges between the vertex-disjoint graphs A and B; below it is written as \(A\vee B\).

**Theorem.** For all integers
\[
t\ge3,\qquad q\ge4t,\qquad n\ge q+2t+1,
\]
let
\[
H_{t,q}=K_1\vee(tK_2\cup qK_1).
\]
Then
\[
\boxed{\operatorname{sat}(n,H_{t,q})=n+3t-4.}
\]
Moreover, up to isomorphism the unique minimum saturated graph is
\[
\boxed{K_1\vee\big((t-1)K_3\cup(n-3t+2)K_1\big).}
\]
Here multiples and unions denote vertex-disjoint unions. Equivalently, the forbidden graph is a t-triangle friendship graph with q additional leaves attached to its common vertex. The extremal graph consists of t-1 copies of K4 sharing one common vertex, with all remaining vertices leaves at that vertex.

The statement gives an explicit, uniform large-q answer to Hua and Peng [HP26, Section 6, Problem 3], together with uniqueness. It does not resolve the range 1 <= q < 4t. The threshold 4t is a sufficient condition from the proof; no optimality is claimed.

## Starting result and residual problem

Hua and Peng [HP26, Theorem 1.4, p. 3; proof in Section 5] prove that for every q >= 1 and n >= q+5, sat(n,H_{2,q})=n+2, with the unique extremal graph a K4 with all additional vertices leaves at one vertex. Their Section 6, Problem 3 asks for sat(n,H_{t,q}) for t >= 3 and q >= 1. The present theorem solves an infinite, explicitly specified range of that question for every t, including every admissible host order in that range.

The upper construction and matching-saturation facts are established ingredients, not claimed as new. The residual step is proving that every H_{t,q}-saturated graph with at most n+3t-4 edges has a universal vertex when q >= 4t. Pendant edges make the usual argument that saturated graphs have diameter two invalid: an added edge can create a pendant edge of H without closing a triangle. The proof below excludes that possibility using the hub degree requirement and the edge budget.

## Proof

Put C=3t-4 and D=q+2t-1. Thus D >= 6t-1 and n >= 6t+1. The common vertex of the triangles and pendant edges of H will be called its hub. Its degree in H is D+1. Every edge of H either lies in a triangle or is a pendant edge incident to the hub.

### 1. Construction

Let
\[
G_* = K_1\vee((t-1)K_3\cup(n-3t+2)K_1),
\]
and let v be its universal vertex. Its edge count is
\[
(n-1)+3(t-1)=n+C.
\]
Every vertex other than v has degree at most 3, so it cannot be the hub of H. The neighbourhood of v has matching number t-1, so v also cannot be the hub of an H-copy. Thus G_* is H-free.

A missing edge xy joins different components of G_*-v. After adding it, choose one edge in each of the t-1 triangles, avoiding x and y. This is possible because each triangle contains at most one of x and y. These t-1 edges and xy form a matching of size t. There remain n-1-2t >= q vertices in the neighbourhood of v, which supply the pendant vertices. Therefore G_* is H-saturated, and sat(n,H) <= n+C.

### 2. Forcing a universal vertex

Let G be any n-vertex H-saturated graph with m=e(G) <= n+C. It is not complete, since n >= |V(H)|. Whenever a nonedge is added, the new H-copy has a hub whose degree in the original G is at least D. In particular, Delta(G) >= D.

There is no isolated vertex u. Indeed, for each x != u, the added edge ux lies in no triangle, so it must be a pendant edge in the new H-copy, with x as hub. Consequently d_G(x) >= D for every x != u. This implies
\[
2m\ge(n-1)D>2(n+C),
\]
contrary to the edge bound. The strict inequality follows from D >= 6t-1, n >= 6t+1, and t >= 3.

If delta(G) >= 2, the degree sum gives
\[
\Delta(G)\le 2m-2(n-1)\le2C+2=6t-6<D,
\]
another contradiction. Thus G has at least one leaf.

Two nonadjacent leaves must have a common neighbour. To see this, add the edge between them. Both endpoints then have degree two, so neither is the hub of H. The edge must therefore lie in a triangle, requiring a common neighbour in G.

We first exclude an isolated K2 component. Its two endpoints are leaves; a third leaf would be nonadjacent to them and could not have a common neighbour with either, so there would be exactly two leaves. For any other vertex x, all vertices other than these two leaves and x have degree at least two, and hence
\[
d_G(x)\le2m-2-2(n-3)\le2C+4=6t-4<D.
\]
Adding an edge from an endpoint of the K2 to x creates no triangle and would require x to be a hub of original degree at least D. This is impossible.

It follows that no two leaves are adjacent. If there are at least two leaves, the common-neighbour observation shows that they all have the same neighbour v. If there is just one leaf, let v be its neighbour. Let l be the number of leaves and k=n-l-1 the number of other vertices besides v. Each of those k vertices has degree at least two, and d(v) >= l. For any such vertex x,
\[
2m\ge l+l+d(x)+2(k-1)=2n+d(x)-4,
\]
so
\[
d(x)\le2C+4=6t-4<D. \tag{1}
\]

Fix a leaf u at v. Suppose some vertex x is outside N[v]. It is not a leaf, because all leaves are adjacent to v. Adding ux creates no triangle: u's only original neighbour is v, and xv is absent. Thus ux must be a pendant edge of the new H-copy. Its hub is x, since u has degree two after addition. This requires d_G(x) >= D, contradicting (1). Consequently v is universal.

This proves the structural statement for every saturated graph within the stated edge budget, not just a chosen extremizer.

### 3. Reduction to matching saturation

Set R=G-v, N=n-1, and r=e(R). We have
\[
r\le C+1=3t-3,\qquad N\ge6t.
\]
If R contained a matching of size t, its endpoints together with v and any q remaining vertices would give H in G. Hence R is tK2-free.

For any missing edge xy of R, saturation gives an H-copy in G+xy. Each vertex other than v has degree at most r+2 <= 3t-1 in G+xy, less than the required hub degree q+2t >= 6t. Thus the hub must be v, and its t petal edges form a matching of size t in R+xy. Therefore R is tK2-saturated.

Since 2r <= 6t-6 < N, R has an isolated vertex. We now use a standard matching-saturation fact, with a proof supplied to make the dependence explicit.

**Matching lemma.** If R is tK2-saturated, has an isolated vertex, and has at least two vertices, then R is a disjoint union of odd cliques. Writing their orders as 2a_i+1, one has sum_i a_i=t-1 and
\[
e(R)=\sum_i a_i(2a_i+1)\ge3(t-1).
\]
Equality holds precisely when each a_i is 0 or 1, that is, when R is a disjoint union of t-1 triangles and isolated vertices.

**Proof of the lemma.** Write nu(R) for the maximum matching size. Adding an edge increases nu by at most one. Because there is a nonedge and R is saturated, nu(R)=t-1. The Tutte--Berge formula states
\[
|V(R)|-2\nu(R)=\max_{S\subseteq V(R)}\big(o(R-S)-|S|\big),
\]
where o counts odd-order components. Choose a maximizing set S and let z be an isolated vertex. We have z not in S: moving an isolated z from S to its complement increases the displayed expression by two. If x belonged to S, adding zx would leave R-S unchanged, so its original deficiency would still bound the new matching number by t-1. Saturation rules this out. Hence S is empty, and o(R)=|V(R)|-2(t-1).

Adding a missing edge inside a component does not change o(R), so it cannot increase the matching number, again by the formula with S empty. Saturation therefore forces each component to be complete. If an even-order component existed, joining one of its vertices to z would merge an even component and a singleton into one odd component, leaving o unchanged. This too is impossible. All components are odd cliques. Their matching numbers are a_i, giving sum a_i=t-1. Finally a(2a+1)-3a=2a(a-1) >= 0 for nonnegative integers a, with equality precisely for a in {0,1}. This proves the lemma.

The lemma gives r >= 3t-3, whereas r <= 3t-3. Thus equality holds throughout, R consists of t-1 triangles and n-3t+2 isolated vertices, and G is isomorphic to G_*. This proves both the saturation formula and uniqueness. QED.

## Relationship to existing results

The equivalent formulations checked were: a fan/friendship/Dutch windmill graph with q pendant edges at its centre; a cone over a matching plus isolated vertices; and equality in the cone upper bound
\[
\operatorname{sat}(n,K_1\vee F)\le n-1+\operatorname{sat}(n-1,F),
\quad F=tK_2\cup qK_1.
\]
For host order at least 2t+q, adding isolated vertices to the forbidden matching does not change containment or saturation. Thus the right side is n+3t-4 in the present range. The equality assertion, and the necessity of the cone structure, are the research content.

- **Hua--Peng [HP26].** Theorem 1.4 covers t=2, whereas Section 6, Problem 3 explicitly asks for t>=3. Their proofs use small cycle counts specific to two petals. Section 6 also asks about connectedness of extremizers when many isolates are added below a cone; our conclusion supplies the stronger universal-vertex property for matching bases in the stated range.
- **Cameron--Puleo [CP22].** Section 2, Lemma 5 proves the general cone upper bound. Section 3, Lemmas 6--7 imply sat(n,H_{t,q})=n+O(1). More explicitly, H_{t,q} has weight 3: a petal edge has weight 3, a pendant edge weight q+2t, and a hub-to-petal edge weight q+2t+1. Substitution into the explicit lower bound at the end of the proof of Lemma 4 yields only n-1. It does not yield n+3t-4 or uniqueness. Their proof of Lemma 7 combines precisely that lower bound and the cone upper bound; following it leaves the additive gap unresolved.
- **Hu--Luo--Peng [HLP24], quoted as HP26 Theorem 1.1.** The exact cone/join equality requires that F have no isolated vertices. Substituting tK2 is legitimate but substituting tK2 union qK1 is not. Isolated vertices can be removed before taking the join for the base saturation number, but not from the resulting forbidden graph: after the join they become pendant vertices. This distinction prevents a direct deduction.
- **Zhang et al. [ZCHYJ25], Theorem 1.3 and Section 4.** The abstract, the opening of Section 4, and the conclusion specify linear forests without isolated vertices. The sentence immediately before Theorem 1.3 in the introduction says "with isolated vertices", creating an apparent coverage clue. The proof's Claim 1 requires every new edge to complete a triangle, including when an endpoint is the hub, which requires the base to have no isolates. We therefore do not treat that inconsistent introductory sentence as a proved theorem covering the present target. The subsequent universal-vertex argument uses diameter two and a 2-connected diameter-two edge bound. Neither applies here until the new pendant-edge obstruction is addressed. The degree-budget argument in Step 2 is that residual step.
- **Fuller--Gould [FG23], Section 2, Theorem 3 and Lemmas 4--6.** These give the known fan saturation formula and construction without pendant edges, and explain the diameter-two argument. The generalized friendship family in their Theorem 3 consists of equal-size cliques intersecting in a common clique; it does not represent a mix of triangles and pendant edges. Neither subgraph inclusion nor adding leaves gives monotonicity of saturation numbers sufficient to prove our lower bound.
- **Zhou--Kamiyama [ZK26], Theorems 2--4 and Section 3.** Theorem 4 quotes Mader's structural theorem for matching-saturated graphs; the matching lemma above is a standard special case, not a new contribution. Their new saturation formula and structural results concern vertex-disjoint triangles, not triangles sharing a hub, and their hypotheses cannot be substituted to give Step 2.

## Reproducible checks and limitations
Run `python3 artifacts/verify_pendant_fans.py`. It requires only Python's standard library. The observed output was:

```text
Matching predicate vs generic embedding: 10440 agreements
All 32768 labeled graphs, t=2 q=1 n=6: min=8, formula=8; 60 labeled winners, one isomorphism type
16 constructions: edge formulas and freeness passed; 6472 additions passed, 700 independently checked
Small positive and negative controls passed
```

The two predicates are recursive maximum matching in each eligible neighbourhood and a generic injective edge-preserving map search. The latter does not use the matching characterization. The construction tests cover t=3,4,5,6; q=4t,4t+1; and n=q+2t+1,q+2t+3. All missing-edge additions are checked; the four t=3 constructions also receive the generic embedding check. The exhaustive small case directly compares computed values and isomorphism types with HP26 Theorem 1.4. These are checks of implementation and construction, not an exhaustive test of the new lower bound. That lower bound rests on the proof.

The earlier exploratory `artifacts/fan_probe.py` is retained but is not evidence for the theorem. Random search cannot certify a saturation minimum. An attempted NetworkX installation failed a package-integrity check; the final verification uses no downloaded dependency.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

Searches included cone/join saturation, matching plus isolates, fan/friendship/windmill synonyms, pendant-edge extensions, generalized friendship graphs, universal-vertex extremal characterizations, and foundational matching results. The strongest accessible general proofs were checked as described above. Evidence identifiers and passage locations are recorded in REVIEW.md.

The following sources were not obtained through available channels; this is **ACCESS_LIMITATION**, not a statement that they do not cover the result.

1. **Jinze Hu, Shengjin Ji, Chenke Zhang (2025), _Some results on the saturation number of graphs_, DOI 10.1016/j.dam.2025.04.038.** Highest concern: its abstract discusses relationships between saturation of disjoint unions of cliques and generalized friendship graphs. Such a family could include our target if singleton cliques are permitted by the operative theorem. Full-text acquisition by DOI and exact title was unsuccessful. The theorem's singleton-clique hypotheses and proof remain unverified. The available abstract asserts results for **some** generalized friendship graphs, without stating the parameters or a result for pendant extensions. This is substantial possible relevance, but no concrete assertion of coverage of this claim was located. HP26's introduction separately says existing nonempty-base join results exclude isolates, and its Problem 3 explicitly poses this family; this is corroborating context, not a substitute for the unread paper.
2. **S. Hu, Z. Luo, Y. Peng (2024), _Saturation numbers of joins of graphs_, DOI 10.1016/j.dam.2024.06.024.** Its general join equality is potentially stronger. Acquisition failed (retrieval). The theorem statement quoted in HP26 Theorem 1.1 and ZCHYJ25's introduction excludes isolated vertices, so that quoted result does not apply. Further consequences of the original proof remain unverified; no concrete extension permitting isolates was found.
3. **Zhang, Lu and Yu (2024), _A note on the minimum size of matching-saturated graphs_, DOI 10.1016/j.dam.2024.01.017; and L. Kaszonyi and Z. Tuza (1986), _Saturated graphs with minimal number of edges_, DOI 10.1002/jgt.3190100209.** These are foundational for the matching step and could contain useful structural arguments or general cone observations. Both full texts were unavailable. We claim no novelty for the matching lemma or cone upper construction. Accessible later sources attribute these ingredients to older work. Possible further implications of the originals remain unverified; no concrete covering claim for the pendant-fan result was located.

The assessment must be revised if a source supplies such coverage. The present result is not claimed to be a major general saturation theorem or a resolution of the all-q problem.

## References

- [HP26] Xinying Hua and Yuejian Peng, _Saturation numbers for joins of graphs and characterization of extremal graphs_, arXiv:2606.22011v2, June 2026. https://arxiv.org/abs/2606.22011
- [CP22] Alex Cameron and Gregory J. Puleo, _A lower bound on the saturation number, and graphs for which it is sharp_, Discrete Mathematics 345 (2022), 112867. DOI 10.1016/j.disc.2022.112867; inspected arXiv:2004.05410v2. https://arxiv.org/abs/2004.05410
- [HLP24] S. Hu, Z. Luo and Y. Peng, _Saturation numbers of joins of graphs_, Discrete Applied Mathematics 357 (2024), 300-309. DOI 10.1016/j.dam.2024.06.024. Original inaccessible; theorem inspected through the precise quotations above.
- [ZCHYJ25] Chenke Zhang, Qing Cui, Jinze Hu, Erfei Yue and Shengjin Ji, _Some results on minimum saturated graphs_, arXiv:2510.10458v1; DOI 10.1016/j.dam.2025.12.040. https://arxiv.org/abs/2510.10458
- [FG23] Jessica Fuller and Ronald J. Gould, _On fan-saturated graphs_, Involve 16 (2023), 637 ff. DOI 10.2140/involve.2023.16.637.
- [ZK26] Xiaoteng Zhou and Naoyuki Kamiyama, _Universal Vertices and Saturation Numbers for Disjoint Triangles_, arXiv:2606.25321v1, June 2026. https://arxiv.org/abs/2606.25321
