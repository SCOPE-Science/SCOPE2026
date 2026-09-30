# Independent audit — 2026-09-30

**Record:** `2026/09/21/twice-subdivided-tree-products-monophonic-position--c9f8957aa251`  
**Audited repository:** `SCOPE-Science/SCOPE2026`  
**Audited current commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree SHA:** `eda4036c211eb8bd86982e33a06756d52f580dfc`  
**Disposition:** passed

The assignment snapshot remains current for this record: comparison from the dispatcher's source-tree-checked commit to current `main` showed no changed file under the assigned record path. The dated independent-audit targets were separately verified absent, and the current `VERIFICATION.md` blob guard was verified before staging this change-set.

## Correctness — PASS

PASS. The cited 2026 Cartesian-product theorem does establish the needed structure: for connected triangle-free factors, a maximum monophonic-position set of size at least three is layered over a leaf, and its projection to the other factor is independent with every pair at distance two. In a tree, three or more pairwise-distance-two vertices must share one common neighbour; otherwise the unique length-two paths create a cycle. In S_2(T) that common neighbour has degree at least three and therefore is an original base-tree vertex. The record's 19-vertex product path built from three length-three subdivided branches and the first four vertices from a leaf branch was independently checked combinatorially: all 19 vertices are distinct, every consecutive pair is adjacent, and there are zero nonconsecutive product adjacencies, so it is induced. It contains the three purported monophonic-position vertices and yields the contradiction. The asymmetric P_m square S_2(T) corollary follows by the same obstruction on the path-end orientation, while a path cannot contain three pairwise-distance-two projection vertices in the reverse orientation.

## Originality — PASS

PASS, with freshness/indexing risk. Chandran--Klavžar--Neethu--Tuite was published online on 11 September 2026 and gives the structural trichotomy, general bounds, the triangle-free bound, and a star-by-star tightness example. Its accessible full text does not state the twice-subdivided-tree exact family or the P_m asymmetric corollary. Targeted searches for monophonic position with subdivisions, twice subdivisions, trees and Cartesian products did not locate an equivalent result. Because the base paper is only weeks old, very recent or not-yet-indexed follow-up work is the principal residual originality risk.

## Scientific value — PASS

PASS. The theorem gives an exact infinite family with mp=2 despite arbitrarily large factor maximum degree, demonstrating arbitrarily large slack in the new triangle-free degree upper bound even for trees with leaves. The explicit induced-path obstruction is short, structural, and extends asymmetrically to path-by-subdivided-tree products.

## Independent checks

- Read the current open-access Theorem 3.18 proof and verified the layered-leaf and pairwise-distance-two consequences used by the record.
- Proved independently that pairwise-distance-two triples in a tree have a common midpoint.
- Encoded the 19 displayed product vertices and checked every pair: consecutive pairs are adjacent and no nonconsecutive pair is adjacent.
- Rechecked the P_m asymmetric orientation argument.

## Literature evidence

- https://doi.org/10.1007/s40314-026-03901-3 — Chandran, Klavžar, Neethu and Tuite (published online 11 Sep 2026), current open-access Cartesian-product monophonic-position paper.
- https://arxiv.org/abs/2412.09837 — Preprint/version history of the same Cartesian-product work.
- https://doi.org/10.1016/j.dam.2024.04.018 — Thomas, Chandran, Tuite and Di Stefano, foundational monophonic-position work cited by the record.

## Access notes

- No restricted full-text claim was needed beyond the sources described above.

## Limitations

- The theorem supplies a sufficient infinite family rather than a classification of all tree products with mp=2.
- Originality is especially sensitive to very recent or not-yet-indexed follow-up work because the principal antecedent was published in September 2026.
- The finite/combinatorial path check corroborates the local obstruction but the theorem still depends on the structural theorem from the cited product paper.

No GitHub write was performed by the audit chat. This file is staged only by the guarded `scope-audit-change-set-v1` publication plan.
