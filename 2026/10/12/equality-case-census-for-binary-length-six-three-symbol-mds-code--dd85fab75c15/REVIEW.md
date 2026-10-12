# Self-review

## Correctness
**PASS.** The size bound \(16\) has a direct projection proof independent of computation. `verify.py` reconstructs all \(64\) binary words and the cyclic three-symbol metric, exhaustively enumerates all maximal cliques, and uses a separate increasing-order search to re-enumerate every size-\(16\) clique. It also checks every stated group element on every unordered word pair and directly verifies affine closure. The replayed counts are \(76\) maxima, orbit sizes \(4,4,12,24,32\), and an affine/nonlinear split of \(44/32\).

## Originality
**PASS.** The closest inspected prior result is Ding--Zhang--Ge's Singleton bound and linear MDS construction theory. Its bound specializes to the already-known ceiling \(16\), but neither that theorem nor the inspected linear construction results imply the number of equality cases, their natural-group orbit sizes, or the existence and unique orbit of \(32\) nonlinear maxima. Exact-parameter, alias, exact-number, and implication searches in published-finding corpus and the public literature found no covering statement. The foundational Yaakobi--Bruck--Siegel repository abstract was also inspected; a full-text copy from that record was unavailable, which remains an access risk rather than evidence of absence.

## Value
**PASS.** Three-symbol reading is the first window size beyond symbol-pair reading, and equality in the Singleton bound is the canonical extremal regime. A complete equality-case census exposing five symmetry types and a substantial nonlinear stratum gives a reusable finite benchmark for MDS b-symbol theory; the value does not depend on claiming a new optimum alone.

## Closest literature and limitations
The closest literature establishes the \(b\)-symbol framework, the general Singleton bound, and linear MDS constructions/criteria. The result here is exact only at \(q=2,n=6,b=3,d_3=5\), and its orbit statement concerns only the explicitly checked \(768\)-element translation--dihedral subgroup. An obscure or unindexed finite census remains the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
