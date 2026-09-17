# A six-cycle construction for weak rainbow saturation of C4

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.

Research result and same-model assessment, 17 September 2026. This document does not constitute independent validation.

## Claim and definitions

All graphs are finite and simple. A copy of a graph is a subgraph, not necessarily induced. An edge-colored graph is rainbow when its edges have pairwise distinct colors.

Following Li, Ma and Xie [2, Introduction], an edge-colored graph G on n vertices is **weakly C4-rainbow saturated** if there is a fixed ordering e_1,...,e_M of the missing edges such that, for every list of pairwise distinct colors gamma_1,...,gamma_M in the natural numbers, inserting e_j with color gamma_j creates a rainbow C4 containing e_j at every step. The new colors may equal initial colors. The initial graph need not be rainbow-C4-free. Write rwsat(n,C4) for the minimum number of initial edges over such colored graphs.

**Theorem.** For every pair of integers q >= 5 and t >= 3, a rainbow-colored K_q with t otherwise vertex-disjoint six-cycles attached at one common clique vertex is weakly C4-rainbow saturated. Consequently, for every integer n >= 20, putting q = 5 + (n mod 5),

\[
\operatorname{rwsat}(n,C_4)
\leq \binom q2+\frac{6(n-q)}5
\leq \frac65 n+\frac{126}5.
\]

In particular, the asymptotic upper coefficient improves from 4/3 in Bo, Lian and Liu [1, Theorem 1.5] to 6/5. This disproves the candidate lower bound rwsat(n,C4) >= 4n/3 - o(n) that motivated the construction. It does not determine the optimal coefficient.

## Proof

Let Q be a clique of order q, choose v in Q, and put R = Q minus {v}. For each i in {1,...,t}, introduce five distinct new vertices a_i,b_i,c_i,d_i,e_i and the six edges of

\[
v a_i b_i c_i d_i e_i v.
\]

Different cycles intersect only at v. There are no other initial edges outside Q. Assign pairwise distinct colors to all initial edges. Put S = {c_1,...,c_t}, and let W be the set of all 5t vertices outside Q.

Call an edge **old** if it is present initially and **new** otherwise, even after it has been inserted. Fix an arbitrary injective coloring of all new edges. Old colors are injective, and new colors are injective, but an old color can equal a new color. We exhibit an insertion order independent of this coloring. Witness cycles may depend on the coloring.

We first record a switching observation, also used in [1, proof of Theorem 1.5, Case 2, especially (S2.5)]. Suppose u,w are distinct vertices outside R, all edges from {u,w} to R are already present and new, and uw is missing. Choose distinct x,y in R such that the old color of xy differs from the color assigned to uw. Such a pair exists because |R| >= 4 and all clique edges have distinct colors. Consider the two cycles

\[
u w y x u,\qquad u w x y u.
\]

The four spokes uy,ux,wy,wx are distinct new edges, so at most one has the color of xy. The color of uw differs from all four spoke colors and from the color of xy. At least one of the two cycles is therefore rainbow. We will refer to this observation as switching through R.

Insert the following groups of edges in the stated order. Within each group, use any predetermined ordering of its specified missing edges. Skip edges already present.

1. **Insert v c_i for every i.** The paths v a_i b_i c_i and v e_i d_i c_i consist of old edges and have disjoint color sets. At least one avoids the color of v c_i, giving a rainbow C4.

2. **Insert c_i x for every i and x in R.** For each y in Q minus {v,x}, use the path c_i v y x. Its first edge is new and its last two edges are old. The colors of c_i x and c_i v are distinct. As y varies, all old edges vy,yx appearing in these paths are distinct. Each of these two forbidden colors can therefore spoil at most one choice of y. Since q-2 >= 3, one path avoids both forbidden colors and gives a rainbow C4.

3. **Complete the clique on S.** All spokes from S to R are now new and present, so switching through R inserts every missing c_i c_j.

4. **Insert w x for every w in {b_i,d_i}, every i, and x in R.** Put f = w c_i, an old edge. If the color of wx differs from that of f, consider paths w c_i s x with s in S minus {c_i}. The last two edges are new, and these two-edge sets are disjoint for distinct choices of s. Among all new edges, at most one has the color of f. There are at least two choices of s, so one path avoids this collision. Its two new edges also have colors distinct from each other and from the new edge wx. If instead wx has the color of f, use the entirely old path b_i a_i v x when w=b_i, or d_i e_i v x when w=d_i. The old edges on that path are distinct and none is f, so all avoid the color of wx. Both cases give a rainbow C4.

5. **Insert all missing edges from {b_i,d_i : 1 <= i <= t} to S.** Each endpoint now has all its spokes to R new and present. Switching through R applies. Edges b_i c_i and d_i c_i were old and are skipped.

6. **Insert v w for every w in {b_i,d_i} and every i.** Choose s in S minus {c_i}, and r in S minus {s}. The path w s r v has three new edges: ws was inserted in group 5, sr in group 3, and rv in group 1. Together with the new edge vw these form a rainbow C4. All four vertices are distinct.

7. **Insert w x for every w in {a_i,e_i}, every i, and x in R.** Set z=b_i when w=a_i, and z=d_i when w=e_i, and let f=wz, an old edge. If wx has a color different from f, consider the paths w z s x with s in S minus {c_i}. Their last two edges are new, from groups 5 and 2, and the two-edge sets for distinct s are disjoint. At most one new edge has the color of f. The at least two choices of s therefore supply a rainbow witness. If wx has the color of f, use the old path w v y x with any y in Q minus {v,x}. Its three old edges are distinct and different from f, giving a rainbow witness in this case as well.

8. **Insert every remaining missing edge within W.** Every vertex of W now has all its spokes to R new and present, by groups 2, 4 and 7. Switching through R applies to every such insertion.

Every path used has distinct vertices, and all its edges precede the current insertion. In particular, no witness depends on the internal order within a group. At the end, Q was a clique initially; edges from v to W are either old or supplied by groups 1 and 6; edges from R to W come from groups 2, 4 and 7; and all edges within W are supplied by group 8 or earlier. Thus the resulting graph is K_(q+5t). Since the new coloring was arbitrary, the required universal coloring property holds.

The initial graph has n=q+5t vertices and m=binom(q,2)+6t edges. For n>=20 choose q=5+(n mod 5), so 5<=q<=9 and t=(n-q)/5>=3. Then

\[
m=\frac65n+\binom q2-\frac65q.
\]

The last two terms are increasing for integer q between 5 and 9 and attain 36-54/5=126/5 at q=9. This proves the stated bound. For n divisible by 5 the stronger explicit bound is m=6n/5+4. QED.

## Relation to prior work and value

Bo, Lian and Liu [1, Theorem 1.5] prove, for ell>=4 and n>=10 ell,

\[
n+\frac{n}{6\ell}\leq \operatorname{rwsat}(n,C_\ell)
\leq \frac{\ell(n-4\ell)}{\ell-1}+\binom{6\ell}{2}.
\]

For C4 this gives 25n/24 <= rwsat(n,C4) <= 4n/3+764/3 when n>=40. Their Section 4 construction uses six private vertices per C4 gadget and eight initial edges, with each gadget absorbed into the clique before the final cross-gadget completion. Their Case 2, steps (S2.1)--(S2.5), was inspected; the switching observation above is credited to that proof.

The new step is to use cheaper pure six-cycles and first complete the new-edge clique on their opposite vertices c_i. That clique supplies two competing paths for each degree-two neighbor in groups 4 and 7. A single gadget does not supply these witnesses. The construction couples the gadgets before absorbing their other vertices, rather than substituting a parameter in the earlier bound. It saves 2n/15 in the asymptotic upper bound, a 10 percent reduction in its leading coefficient. The common clique costs only a bounded number of edges.

Li, Ma and Xie [2, Theorem 1.2] prove that the normalized weak rainbow saturation number has a limit for every fixed nonempty graph. Combining this with [1] and the present theorem gives

\[
\frac{25}{24}\leq \lim_{n\to\infty}\frac{\operatorname{rwsat}(n,C_4)}n\leq\frac65.
\]

Their Theorem 1.3 gives a general upper bound with coefficient 2 for C4; Proposition 4.3 gives coefficient 3/2 when there is the specified degree-two induced P4, including C4. Neither yields the present bound. The earlier 3/2 conjecture discussed there had already been disproved by [1]; that disproof is not claimed here.

The foundational paper [3, Section 6] supplies the same weak definition and questions. The alternative notation wsat(n,R(H)) in [4] describes the same rainbow weak-saturation framework; its Theorem 1.6 concerns complete graphs and does not specialize to C4. Proper rainbow saturation [5, Theorems 1.5--1.6] uses a different quantifier over proper colorings and gives coefficient 11/6 for C4, not this guarantee. Ordinary weak saturation, fixed-palette rainbow saturation, and static rainbow saturation must not be conflated with the universal injective-new-color property proved here.

## Reproducible finite verification

The proof above covers all q>=5 and t>=3 without computation. The supplementary standard-library script [check_c4.py](artifacts/check_c4.py) independently enumerates all length-three paths available at each insertion, rather than only the witness paths in the proof.

Because old and new colors are separately injective, their equality relations form a partial matching between old and new edges. A four-cycle fails to be rainbow exactly when this matching contains some old/new pair from that cycle. Thus a bad coloring at an insertion exists exactly when a partial matching hits every cycle's clause of old/new pairs. The checker solves this finite condition exhaustively by branching on a shortest remaining clause. Every partial matching can be realized by a full coloring using fresh colors elsewhere, so the check treats the exact predicate, not a relaxation.
Run from the record directory:

```sh
python3 artifacts/check_c4.py
```

The saved output is [check_c4_results.txt](artifacts/check_c4_results.txt). All insertions passed for (q,t)=(5,3),(6,3),(7,3),(8,3),(9,3),(5,4), with respectively 20,21,22,23,24,25 vertices and 28,33,39,46,54,34 initial edges. The solver also agreed with direct enumeration of all partial matchings on all 4096 triples of clauses in a 2-by-2 collision system. Negative controls (q,t)=(5,1),(5,2) failed at group 4; the script instantiated their collision patterns as actual colors and separately checked that no rainbow C4 existed at the failing insertion. These controls concern this order, not impossibility of all orders for those graphs.

Actual computed edge counts at n=40,100,1000,10000 are 52,124,1204,12004, compared to the cited upper-bound expressions 924/3,1164/3,4764/3,40764/3. The script checks these comparisons and the new formula with integer arithmetic. Finite verification is supplementary evidence, not the proof of the infinite family.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

The search covered weak rainbow saturation of C4 and K_(2,2), weak saturation with respect to the family of rainbow copies R(C4), the equivalent asymptotic coefficient 1.2 or 6/5, cycle-gadget constructions, and general bounds that could specialize to C4. The existence of families with average degree at most 12/5+o(1) is the same density objective. The old/new collision formulation was checked as an equivalent universal-coloring condition, not proposed as a separate invariant. Source inspection included the closest construction and proof [1, Section 4], the stronger general bounds [2, Theorem 1.3 and Proposition 4.3], and the distinctions from adjacent saturation notions described above.

Screening covered the initial C4 target, the 6/5 construction, K_(2,2), the coefficient 1.2 and broader coverage, and alternative rainbow-family notation and cycle constructions. These searches informed primary-source inspection; search misses alone are not evidence of novelty.

No plausible novelty-threatening source whose full text could not be obtained was identified. The inspected versions were accessible preprints, including [1] arXiv v1, [2] arXiv v1, [3] arXiv v2, [4] arXiv v2 and [5] arXiv v1. This is a limitation on version coverage: publication metadata does not establish that every later revision has been checked. No unresolved concrete covering clue was identified. Only the cited relevant sections are claimed as inspected, not every proof in every paper. If a later source demonstrates equivalent or stronger coverage, this assessment must be revised.

## References and evidence locations

1. Bo, Lian and Liu, *Weak rainbow saturation numbers of paths, stars and cycles*, [arXiv:2609.03823v1](https://arxiv.org/abs/2609.03823v1). Theorem 1.5; Section 4, Case 2, (S2.1)--(S2.5). Acquired retrieval; theorem at extraction offsets 7987 and 42008; construction/proof inspected at 38000--45000 and 47700--52150.
2. Li, Ma and Xie, *Weak Rainbow Saturation Numbers of Graphs*, [DOI:10.1002/jgt.23211](https://doi.org/10.1002/jgt.23211), inspected [arXiv:2401.11525v1](https://arxiv.org/abs/2401.11525v1). Introduction, Theorems 1.2--1.3, Proposition 4.3 and Question 4.4. retrieval; offsets 0--12500 and 33900--40100.
3. Behague, Johnston, Letzter, Morrison and Ogden, *The rainbow saturation number is linear*, [DOI:10.1137/23M1566881](https://doi.org/10.1137/23M1566881), inspected arXiv:2211.08589v2. Section 6, weak saturation definition and questions. retrieval; contexts at offsets 25105--29073; introduction at 0--4500.
4. Chakraborti, Hendrey, Lund and Tompkins, *Rainbow saturation for complete graphs*, [DOI:10.1137/23M1565875](https://doi.org/10.1137/23M1565875), inspected arXiv:2212.04640v2. Definitions and Theorem 1.6. retrieval; relevant contexts 7976--10800.
5. Halfpap, Lidicky and Masarik, *Proper rainbow saturation numbers for cycles*, [DOI:10.1016/j.disc.2026.115053](https://doi.org/10.1016/j.disc.2026.115053), inspected arXiv:2403.15602v1. Definition and Theorems 1.5--1.6. retrieval; offsets 0--8350.

The evidence offsets refer to the acquired text extractions, not printed page numbers. The scope is a new upper bound for C4; optimality, a matching lower bound, a result for all longer cycles, and smaller n are not established.
