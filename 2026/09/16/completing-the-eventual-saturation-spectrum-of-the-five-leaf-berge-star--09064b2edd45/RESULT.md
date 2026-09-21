# Completing the eventual saturation spectrum of the five-leaf Berge star

This is a computer-assisted mathematical result with a same-model review, not independent validation. The new part treats orders not divisible by five.

## Exact claim

A simple 3-uniform hypergraph is a pair H=(V,E) with E a subset of the three-element subsets of V. A Berge-K_{1,5} consists of distinct vertices v,x_1,...,x_5 and distinct hyperedges e_1,...,e_5 with {v,x_i} contained in e_i. H is saturated if it contains no such configuration but adding any missing triple creates one. Let ES(n) be the set of edge counts of saturated hypergraphs on n vertices. Put

\[
s(n)=\left\lceil\frac{4n}{3}\right\rceil-3.
\]

**Theorem.** There exists N such that, for every integer n>=N, writing r for n modulo 5, the following table gives ES(n). All intervals denote integer intervals.

| r | ES(n) | Status |
|---|---|---|
| 0 | [s(n),2n-5] union {2n} | Prior result [B], body of Section 5 |
| 1 | [s(n),2n-4] union {2n-2} | New completion |
| 2 | [s(n),2n-4] | New completion |
| 3 | [s(n),2n-5] | New completion |
| 4 | [s(n),2n-4] | New completion |

In particular, for all sufficiently large n=5q+r,

\[
\operatorname{ex}_3(n,\mathrm{Berge}\text{-}K_{1,5})
=10q+\binom r3.
\]

The extremal-number assertion follows because every hypergraph free of the forbidden configuration can be extended to a saturated one. No uniqueness assertion is made.

The equivalent deficit formulation, with d=2n-|E|, excludes precisely

\[
D_1=\{0,1,3\},\quad D_2=D_4=\{0,1,2,3\},\quad
D_3=\{0,1,2,3,4\}
\]

from the integer interval [s(n),2n]. Thus the auxiliary deficit does not hide a different invariant: the theorem determines edge counts of inclusion-maximal Berge-star-free hypergraphs, equivalently inclusion-maximal hypergraphs of maximum Berge degree at most four.

## Starting point and residual problem

Bushaw, English, Heath, Johnston and Rombach [B] prove an eventual full interval from the saturation number to 5n/3 (Theorem 3.1, pp. 11 and 15-16). Their Theorem 1.3 leaves only constantly many unresolved edge counts at the top for general orders. Section 5 settles the top range when 5 divides n: Proposition 5.1 excludes deficits 1 through 4, and Theorem 5.13 constructs deficits at least 5 in the upper range.

The residual investigated here is the exact upper boundary for the four other residues, including both missing values and constructions for every admissible value. The boundary is inferred from their stated divisibility restriction; it is not quoted as a separately numbered open problem. The new content consists of the small-deficiency exclusions and a complete set of construction certificates that closes the residue cases. The lantern method and the underlying component estimates are explicitly credited to [B].

## Proof

### 1. Link matching and deficiency

For v in V(H), let L(v) have vertex set N(v) and an edge xy for each triple vxy in H. The Berge degree b(v) is the maximum size of a system of distinct representatives for the edges of L(v): each link edge chooses one of its endpoints, and chosen endpoints must be distinct. This is the matching number of the bipartite incidence graph between link edges and link vertices, not the ordinary matching number of L(v).

If t(v) is the number of tree components of L(v), then

\[
b(v)=|N(v)|-t(v).
\]

For a tree component one can assign all edges distinct representatives by rooting the tree; for a cyclic component choose a spanning unicyclic subgraph, orient its cycle cyclically and its attached trees away from the cycle to represent every vertex. These also give the corresponding upper bounds. This proves the identity, which is Lemma 2.1 of [B].

Consequently a free hypergraph has degree at most six. A link with five edges must be K_4 minus one edge; a link with six edges must be K_4. All links with at most four edges are allowed. These are the degree consequences of [B, Observation 5.2]. In particular |E(H)|<=2|V(H)|.

Define

\[
\Delta(H)=\sum_v(6-\deg_H(v))=6|V(H)|-3|E(H)|=3d.
\]

We use the following local facts from [B, Observations 5.3-5.4 and Claims 5.5-5.7, pp. 23-26]. Their proofs do not use divisibility of the total order.

1. If |N(v)|>=5, then Delta(N[v])>=9.
2. Adjacent degree-six vertices in a saturated hypergraph lie in a complete five-vertex component.
3. A component of order at least ten containing a vertex with at least five neighbors has deficiency at least 13.
4. In a component other than K_5^(3), if every vertex has at most four neighbors, every degree is at most four.

Here are the relevant mechanisms, including why the order assumption in [B, Section 5] is not needed for these facts. Codegrees are symmetric. A vertex in a link of degree 1, 2, or 4 forces the corresponding neighboring hypergraph vertex to have deficiency at least 2, 1, or 2, respectively. Thus, writing L_i for the number of degree-i vertices in L(v),

\[
\Delta(N[v])\ge 6-|E(L(v))|+2L_1+L_2+2L_4.
\]

The allowable links with at least five vertices are precisely the eleven graphs in [B, Observation 5.2/Table 1]; substituting them gives a minimum of 9. Two adjacent degree-six links force a five-vertex component, which saturation completes.

For fact 3, suppose the component deficiency is at most 12. Neighborhoods of size at least seven are immediately excluded by Table 1. A six-neighbor vertex already consumes at least 12 deficiency; all remaining vertices would have degree six and be independent by fact 2. With at least three such vertices their incident edges exceed the remaining degree capacity in the six-neighbor set. For a five-neighbor vertex v, at most three outside vertices can have degree below six. Some outside degree-six vertex z therefore has a neighbor x in N(v). The link at x must be the five-vertex tree with degree sequence (3,2,1,1,1). Its degree-three vertex is z, and v is the leaf not adjacent to z. Symmetry forces N(v) intersect N(z) to be a two-vertex component of L(v). The other two neighbors of z lie outside N[v] and each have deficiency at least two. Hence the component deficiency is at least 9+2+2=13, a contradiction. These are exactly the local cases of [B, Claim 5.6].

For fact 4, a degree-six vertex with no neighborhood larger than four closes a five-vertex component. For a degree-five vertex v with link K_4 minus ad, adding vad cannot create a five-leaf star centered at v. A proposed new center a or d cannot gain a fifth neighbor: the two other link vertices already have their four neighbors inside N[v], forcing any possible fourth neighbor of a back into N[v]. This contradicts saturation. This is [B, Claim 5.7].

### 2. A finite reduction for deficits at most four

Remove all K_5^(3) components of a saturated H and call the residual R. R is saturated: any new forbidden configuration caused by adding a triple entirely in R has its center in that triple, so it cannot use an edge of a removed component. Its deficiency is unchanged, and its order is congruent to n modulo five.

Every nonempty non-K_5 component has deficiency at least six. For components of order at most five, saturation forces a complete hypergraph, since six distinct core vertices would otherwise be needed after adding a triple. The possible connected components here are an isolated vertex, K_3^(3), K_4^(3), and K_5^(3), with deficiencies 6,15,12,0. For larger components, fact 1 or fact 4 gives the required lower bound.

Suppose Delta(R)<=12. If some component has a vertex with at least five neighbors, its deficiency is at least nine and its order is at most nine by fact 3. No second residual component fits the remaining deficiency, since that would cost at least six. If no such vertex exists, fact 4 gives 2|V(R)|<=Delta(R)<=12. Therefore

\[
|V(R)|\le9.
\]

Deficit zero forces R empty. Deficit one is impossible. At deficit two, no large neighborhood is possible, and |V(R)|<=3. Saturation on at most three vertices and deficiency six force a single isolated vertex. Thus deficit two occurs only at residue one.

At deficit three, in the absence of a large neighborhood |V(R)|<=4, and none of the complete hypergraphs of those orders has deficiency nine. With a large neighborhood, the residual order is one of 6,7,8,9. The finite exclusion below rules out all four.

At deficit four and residue three, the residual order can only be 3 or 8. Order three must be K_3^(3), whose deficit is five. The finite exclusion below rules out order eight with deficit four.

### 3. Finite exclusion, checked by two exhaustive methods

The following five instances have no saturated simple 3-graph:

| Order | Edges | Deficit |
|---|---|---|
| 6 | 9 | 3 |
| 7 | 11 | 3 |
| 8 | 13 | 3 |
| 9 | 15 | 3 |
| 8 | 12 | 4 |

The accompanying standard-library Python code is part of this computer-assisted proof. Completeness of the enumeration follows as follows. In every row the average degree is greater than four. Choose a maximum-degree vertex and relabel it 0. Its degree is five or six, and its link is respectively K_4 minus an edge or K_4. Relabel its four neighbors as 1,2,3,4, with missing pair 34 in the degree-five case. This is an exhaustive symmetry reduction; no transitivity of the whole hypergraph is assumed.

`dense_stars.py` enumerates consistent complete links using the structural classification. It branches on the next vertex link and removes complete K_5 components. The six-vertex exclusion is also checked by `small_stars.py`, which enumerates all 2^20 labelled hypergraphs without symmetry reduction.

The independent `audit_dense.py` builds its link domains by enumerating every subset of up to six link edges and calculating the incidence matching number directly. It branches on individual triples, propagates the edges forced by surviving link domains, and prunes only contradictions and valid degree/edge-count bounds. It does not exclude K_5 components. Every complete candidate at the target edge count is tested against the definition of saturation. The complete independent runs gave:

| (order,deficit) | Nodes with maximum degree 5 | Nodes with maximum degree 6 | Saturated witnesses |
|---|---|---|---|
| (6,3) | 5 | 27 | 0 |
| (7,3) | 5 | 25 | 0 |
| (8,3) | 11 | 53 | 0 |
| (9,3) | 5 | 91 | 0 |
| (8,4) | 87 | 207 | 0 |

Branching yes/no on a triple partitions all surviving completions. Filtering a vertex domain by assigned triples removes only incompatible links. Intersections and unions of a nonempty domain give logically forced present/absent triples. Summing minimum and maximum degrees over domains gives valid lower and upper bounds on three times the target edge count. These observations justify every pruning rule in the independent enumeration.

Positive controls avoid a vacuous checker: at (6,4), both maximum-degree branches find three saturated labelled representatives; at (9,5), the degree-five branch finds six and the degree-six branch finds none. These counts agree with the original enumeration. Complete enumeration on six vertices gives the histogram {6:90, 7:8400, 8:1290, 10:6}, with no nine-edge example. On orders at most five, it finds only the complete hypergraphs. Local ranks in that enumeration are checked both by the tree-component identity and by augmenting-path matching.

Sections 1-3 prove all asserted upper exclusions, for every order where they apply, without an asymptotic assumption.

### 4. Constructions for every deficit at least five in the upper range

If G is saturated and every vertex of G has Berge degree four, then G disjoint union H is saturated for any saturated H. For a missing crossing triple, choose its vertex v in G and one of its vertices outside G. The outside vertex represents the new edge, and a size-four system of distinct representatives in the old link at v represents four old edges. An internal missing triple is handled by the saturation of its component. This also proves freeness of the disjoint union.

K_5^(3) has this property. So does the 5-lantern L of [B, Construction 3.2]. Explicitly, take vertices u_i,v_i and three-element sets X_i, for i=1,2,3, all disjoint. Its edges are {u_1,u_2,u_3}, {v_1,v_2,v_3}, the three sets X_i, and all {w,x,y} with w in {u_i,v_i} and {x,y} a pair in X_i. It has 15 vertices, 23 edges, and deficit 7. Its saturation and all fifteen Berge degrees have been checked directly, independently of the source's construction proof.

`artifacts/seeds.json` contains explicit edge lists for a saturated seed G_{r,d0} for every r=1,2,3,4 and d0=5,6,...,11. Its order is congruent to r modulo five, its edge count is 2|V|-d0, and its order is at most 16. The actual orders are:

| r / d0 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 11 | 11 | 11 | 11 | 16 |
| 2 | 7 | 7 | 7 | 12 | 12 | 12 | 12 |
| 3 | 3 | 8 | 8 | 8 | 13 | 13 | 13 |
| 4 | 9 | 9 | 9 | 9 | 9 | 14 | 14 |

For any integer 5<=d<=n/3 choose the unique d0 in {5,...,11} congruent to d modulo seven, and put q=(d-d0)/7. Form the disjoint union of G_{r,d0}, q lanterns, and enough K_5^(3)'s to reach n vertices. The order before padding is at most

\[
16+15q\le16+\frac{15d}{7}\le16+\frac{5n}{7}\le n
\]

when n>=56, and it is congruent to n modulo five. Padding is therefore possible. The construction is saturated by the disjoint-union argument, and has deficit d. It realizes every integer in [ceil(5n/3),2n-5].

The seeds were found using deterministic greedy construction and disjoint unions (`seed_stars.py`). The proof relies on their stored finite certificates, not on an assumption that random search succeeds. `verify_seeds.py` checks every missing triple with a separate subset-DP implementation of distinct representatives. It imports neither the matching implementation nor the link classification. All 40 stored seed records pass, including the 28 needed here. No assertion that every seed is new or that every seed has Berge degree four at every vertex is needed.

### 5. Remaining points and the lower interval

Deficit two at residue one is realized by one isolated vertex plus complete five-vertex components. Deficit four at residue one is realized by the six-vertex sun S_5 from [B, Construction 4.2], plus complete five-vertex components. Its vertices are w_0,w_1,x_0,x_1,x_2,x_3, with edges {w_i,x_j,x_{j+1 mod 4}} for i=0,1 and j=0,1,2,3. It has eight edges, is saturated, and every vertex has Berge degree four; these facts were independently checked.

Deficit four at residue two is realized by two isolated vertices plus complete five-vertex components. Deficit four at residue four is realized by K_4^(3) plus complete five-vertex components. Each small residual is vacuously saturated, and the padding lemma applies.

Finally [B, Theorem 3.1] supplies every integer from the saturation number through floor(5n/3), for all sufficiently large n without a divisibility restriction. Austhof and English [A, Section 3, Theorem 3.1 in the acquired version] give

\[
\operatorname{sat}_3(n,\mathrm{Berge}\text{-}K_{1,5})
=\min_{1\le a\le4}\left\{\left\lceil\frac{4(n-a)}3\right\rceil+\binom a3\right\}
=\left\lceil\frac{4n}{3}\right\rceil-3.
\]

The last equality follows by considering a=1,2,3,4; a=3 attains the minimum. The upper and lower constructed integer intervals are adjacent. This completes the proof for residues one through four. The residue-zero row is [B, Proposition 5.1 and Theorem 5.13], with the same lower endpoint. One may take N to be at least 56 and at least the thresholds in the two cited eventual results. No explicit numerical value for their thresholds is asserted.

## Reproduction and observed checks

From the workspace root, run:

```sh
python3 artifacts/verify_seeds.py
python3 artifacts/audit_dense.py
python3 artifacts/small_stars.py
```

These require Python 3 with `int.bit_count` and only the standard library. The first command independently verifies all stored positive certificates. It also compares the lantern's computed 23 edges against the source formula 2+3*(binom(4,3)+binom(3,2)), checks the sun's eight edges and all its ranks, compares the saturation minimum with s(n) for all 296 orders from 5 through 300, and verifies 31,387 padding edge-count calculations. All checks passed. The numerical comparisons support, rather than replace, the symbolic arguments above.

The second command checks the five negative instances and two positive controls. The third checks every labelled hypergraph through order six. The original link-domain enumerator can additionally be run as `python3 artifacts/dense_stars.py n d` for the desired residual order and deficit.

## Prior work, originality and limitations

The theorem is a completion of a specific unresolved boundary in [B], not a new general saturation method. The lower interval, saturation minimum, local link classification, component estimates, lantern and sun are prior work. The new mathematical residual is the exact feasible-deficiency determination for nonzero order residues and the seed certificates that fill all upper-range values. In particular, arbitrary saturated components cannot simply be combined: the rank-four padding condition or a separate saturation check is essential.

The standard extremal formulation was also checked. [G, Theorem 12] yields only ex<=2n for this parameter choice. [K, Theorem 16, pp. 15-18] classifies equality under the relevant divisibility condition. Substituting k=1, ell=5, uniformity 3 gives equality at 2n when 5 divides n; its nondivisible ceiling bound does not determine the deficits here. Its proof assumes at least the divisible extremal edge count, so its equality cases do not settle positive deficiency. Its remark following the proof suggests an extension of the extremal construction to nondivisible orders. That suggestion is acknowledged as prior motivation, not treated as a proved theorem or as our conjecture. The exact spectrum, including gaps below the maximum, requires more.

[Z, Theorems 1.10-1.11] concern Berge forests with at least two stars. [F, Theorem 2.1 and Corollary 2.8] give forest bounds with divisibility restrictions and recover the same single-star bound where applicable. Their stated hypotheses and the inspected proof mechanisms do not provide the finite-deficiency exclusions above. No claim is made about uninspected portions of these sources.

The acquired v1 of [B] has inconsistent introductory endpoints in Theorem 1.4: they disagree with Proposition 5.1, Theorem 5.13, and the saturation minimum. We use the body results and the independently inspected saturation formula, not that introductory display. Several arithmetic typographical issues in its construction displays are also avoided by using explicit verified edge lists. This report gives an eventual spectrum, not the least threshold, and includes a finite computer-assisted proof rather than a purely handwritten classification of all residual hypergraphs.

### Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

No plausible novelty-threatening work remained entirely inaccessible after the available alternate routes were tried. The publisher acquisition of [K] failed (retrieval); its identified arXiv preprint was then obtained and the relevant statements and proof were inspected (retrieval). The publisher version itself was not obtained through available channels, so differences from the inspected preprint remain unverified. [B] and [F] were also acquired as arXiv v1 mirrors; these are not guarantees of the latest publisher revisions. No specific unresolved covering claim in an unavailable version was identified. A preliminary erroneous DOI request for [K] and timed-out searches were not used as novelty evidence. The search scope and source locations are recorded in REVIEW.md. Later evidence of coverage would require revising the assessment.

## References

- **[B]** Neal Bushaw, Sean English, Emily Heath, Daniel P. Johnston, Puck Rombach, *The Saturation Spectrum of Berge Stars*, [arXiv:2502.17686v1](https://arxiv.org/abs/2502.17686). Acquired retrieval. Relevant: Lemma 2.1; Theorem 3.1; Construction 3.2; Construction 4.2; Section 5, especially Observations 5.2-5.4, Claims 5.5-5.7, Proposition 5.1 and Theorem 5.13.
- **[A]** Erica Austhof and Sean English, *Nearly-Regular Hypergraphs and Saturation of Berge Stars*, Electronic Journal of Combinatorics (2019), [DOI:10.37236/8363](https://doi.org/10.37236/8363). Acquired retrieval; Section 3, Theorem 3.1 and proof, pp. 7-8 of acquired text.
- **[G]** Daniel Gerbner, Abhishek Methuku, Cory Palmer, *General lemmas for Berge-Turan hypergraph problems*, European Journal of Combinatorics 86 (2020), 103082, [DOI:10.1016/j.ejc.2020.103082](https://doi.org/10.1016/j.ejc.2020.103082). Acquired retrieval; Theorems 7 and 12, the latter on p. 10 of acquired text.
- **[K]** Omid Khormali and Cory Palmer, *Turan numbers for hypergraph star forests*, European Journal of Combinatorics 102 (2022), 103506, [DOI:10.1016/j.ejc.2022.103506](https://doi.org/10.1016/j.ejc.2022.103506). Inspected [arXiv:2001.05631v1](https://arxiv.org/abs/2001.05631), retrieval; Lemma 11, Theorems 12 and 16 and the remark after Theorem 16.
- **[Z]** Lin-Peng Zhang, Hajo Broersma, Ligong Wang, *Turan numbers of general star forests in hypergraphs*, Discrete Mathematics 348 (2025), 114219, [DOI:10.1016/j.disc.2024.114219](https://doi.org/10.1016/j.disc.2024.114219). Publisher-layout full text acquired from the published source; Theorems 1.8-1.11, pp. 3-4.
- **[F]** Junpeng Zhou, Daniel Gerbner, Xiying Yuan, *On Turan problems for Berge forests*, [arXiv:2506.16140v1](https://arxiv.org/abs/2506.16140). Acquired retrieval; Section 2.1, Theorem 2.1, Corollary 2.8, and the proof of Theorem 2.1 in Section 3.
