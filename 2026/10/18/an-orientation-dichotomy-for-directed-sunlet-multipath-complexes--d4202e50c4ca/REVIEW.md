# Self-review

## Correctness — PASS

The proof identifies every forbidden face from the edge-by-edge directed paths definition: pairwise conflicts are exactly between each pendant and one consecutive rim arc, and the only directed cycle is the full core rim. The face polynomial follows from local join factors and the equality of the two cyclic transition counts. In a mixed orientation an inward-to-outward transition provides an unconstrained rim arc; pairing it with every pendant-containing lower face in decreasing size is an explicit valid elementary collapse to the rim boundary. For a uniform orientation the pairwise-conflict complex is a crosspolytope boundary with one facet removed, a PL ball. The induced rotation character follows from the sign on the oriented rim boundary. All quantifiers are \(n\ge3\) and all pendant orientation words. The standalone verifier confirms complete faces, face enumerators, mod-two homology and free-face collapses for all orientations through \(n=6\), without using the finite tests as the proof for arbitrary \(n\).

## Originality — PASS with residual risk

The closest primary result is Caputi–Collari–Di Trani–Smith, arXiv:2208.04656v1, which classifies the coherently oriented bare polygon and some other directed graph families, but not the orientations of all its pendant edges or the inclusion of its rim complex. The earlier path-poset paper arXiv:2110.11206 treats definitions and other examples. The blow-up/matching theorem in arXiv:2401.01248v1 assumes no oriented cycles and therefore does not cover directed sunlets. The later arXiv:2601.05670v1 studies bidirectional polygons and a different two-edge T-operation, not this full family. Indexed mathematical results on bidirected double stars and bidirectional polygons do not imply the statement. Direct searches of the exact object, aliases, face polynomial and strongest relative-collapse formulation found no equivalent classification. Unindexed/unpublished equivalent work remains a residual risk; a negative search is not a uniqueness proof.

## Mathematical value — PASS

The underlying sunlet is a standard unicyclic graph; the result classifies all \(2^n\) orientations of its pendant edges by **simple-homotopy type** and identifies a sharp orientation-sensitive transition, rather than supplying an arbitrary small finite example. The mixed-case collapse retains the original directed cycle's fundamental class via a canonical map, whereas uniform orientations fill it in. The exact polynomial describes finer orientation dependence than the homotopy types, and the cyclic sign calculation determines the remaining symmetry action. The explicit relative-collapse mechanism is potentially reusable for other cycle-containing multipath complexes; no broader theorem is claimed.

## Limitations

One pendant at every rim vertex and a coherently oriented simple core cycle are essential. The classification is not asserted for arbitrary coronas, multileaf attachments, bidirected rims, or other directed homology functors. Independent replication and external mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
