# Scientific review: Heawood metric-basis exchange geometry

## Correctness

**PASS.** The domain is exactly the unweighted fourteen-vertex incidence graph of the Fano plane, with token-jump adjacency between minimum resolving sets. The incidence-signature argument excludes four-landmark sets, classifies each five-landmark set as a noncollinear point triple with two of its three tangents or the dual. Both independent exact programs enumerate the whole finite state space. The cyclic-line checker builds the adjacency by every removal/addition and computes every breadth-first distance. The binary-vector checker independently builds Fano incidence, checks all five-subsets and all pairwise overlaps, explicitly constructs 336 automorphisms, and repeats all-source breadth-first search. Both certify 168 bases, 420 edges, 56 disjoint triangles, common distance profile (1,5,18,49,71,24), the full pair-distance table, and precisely 4,368 shortest-path detours of one extra exchange. No unproved infinite extrapolation is used.

## Originality

**PASS, qualified.** The known metric dimension five of the Fano incidence graph is excluded from novelty: it appears in Héger–Takáts (2012), Remark 11. A later study of metric bases of symmetric-design incidence graphs (Tang–Zhou–Chen–Zhang, 2021) was identified and its accessible material examined; the unseen full text could cover aspects of the basis classification. Thus the count 168 is a necessary state-space description, not a separate priority claim. The meaningful new claim is the complete token-jump exchange-graph geometry (triangular partition, uniform eccentricity, all shell counts and sharp exceptional detours). Research-record searches on Heawood, resolving sets, exchange, metric bases and Fano incidence identified nearby mathematical themes but no statement implying these values. The dedicated literature on metric-basis reconfiguration was also checked at the accessible project-description level. Residual risk remains from unindexed or inaccessible work, including an unretrieved 2026 thesis; no absolute uniqueness or independent priority certification is asserted.

## Value

**PASS.** Reconfiguring an optimal resolving set models whether minimal landmark placements can change without temporarily losing location distinguishability. For a canonical highly symmetric cubic graph, exact connectivity, worst-case move cost, the 56 triangular local cells and the all-pairs one-extra-exchange bound provide a complete, reusable finite benchmark. The sharp non-isometry count distinguishes graph distance from the ambient Johnson-graph lower bound, information not implied by simply knowing the optimum size or how many solutions exist.

## Scope and limitations

The result is exact only for the Fano incidence graph. The extremal invariant is an ordinary metric basis, not an edge-metric basis or stronger resolving set. No claim is made of a short general symbolic expression for metric-basis exchange graphs of other designs. One relevant 2021 publisher full text and a 2026 thesis were inaccessible, and other historical computations may exist. Both supplied programs are complete finite checkers, not external certification. The verification remains subject to independent scholarly review.

Self-review: passed. Independent audit: not yet performed.
