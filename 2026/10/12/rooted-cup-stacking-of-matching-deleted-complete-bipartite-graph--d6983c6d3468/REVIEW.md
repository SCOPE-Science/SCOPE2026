# Scientific review

## Correctness — PASS
The exact distance layers are verified using the assumption that both part sizes are at least three. The necessity proof partitions cups by final moves to the root; every packet serving a nonroot cup from the target's part consumes an original cup from the opposite part. Only the unique deleted-edge partner can send a three-cup final packet, and that packet serves at most two cups from the target's part. This proves the sharp upper resource bound. A Hall matching in the complete bipartite remainder (at most one distinct excluded neighbor per vertex) constructs legal two-cup packets; deleted-edge endpoints additionally use one three-cup packet. Both parts and all boundary cases are covered. Independently implemented exhaustive state search confirmed 346 rooted cases, while 6,984 constructed sequences had every move and terminal state checked. All finite checking is supplementary to the proof.

## Originality — PASS (literature risk retained)
The 2023 initiating paper completely covers undeleted bicliques and diameter-two rooted matching criteria. The matched endpoints here have eccentricity three; the sharp one-unit extension beyond the complete-bipartite rooted threshold is not implied by that criterion. The later Hamilton-path result establishes stackability when a Hamilton path exists, but a bipartite graph with part sizes differing by two has no Hamilton path. In particular, the positive matched-side targets on \(K_{n+2,n}\) minus a nonempty matching are not consequences of that theorem. Targeted searches for cup stacking, its frog-jumping alias, crown graphs, deleted matchings, and target profiles identified no published theorem with the exact statement. Residual risk persists for terminology variants or unindexed sources; failed searches alone cannot prove novelty.

## Value — PASS
The class \(K_{m,n}\) minus a matching is a standard controlled perturbation of a fundamental bipartite family, and *which prescribed targets are attainable* is central to cup stacking. The theorem describes every root for every parameter value, revealing a sharp asymmetry invisible to global graph stackability. Notably, one deleted edge changes root feasibility on an infinite family of graphs without Hamilton paths, while the whole graph stays non-stackable. The packet proof exposes the precise extra resource supplied by a distance-three vertex and gives efficient constructive certificates, making this more than a scalar evaluation of a familiar invariant.

## Closest literature and limitations
Fay–Hurlbert–Tennant, arXiv:2310.06192, Lemma 10 and Corollary 12; Gregor–Merino–Mütze–Verciani, arXiv:2401.06189, Theorems 1, 6, 19. The conclusion does not extend by the presented argument to nonmatching deleted edges, part sizes below three, or arbitrary initial cup configurations. An exact equivalent under earlier frog-jumping terminology remains possible.

Self-review: passed. Independent audit: not yet performed.
