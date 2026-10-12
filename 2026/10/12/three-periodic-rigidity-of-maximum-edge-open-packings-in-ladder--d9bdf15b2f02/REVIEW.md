# Review of the maximum ladder edge-open-packing classification

## Correctness — PASS

The proof independently derives the upper bound by assigning a distinct, pairwise independent leaf to each edge of an induced star forest. Equality forces a checkerboard independent set. Every selected centre in the other checkerboard has the full neighbourhood interval on the leaf class, so feasible equality patterns are precisely disjoint indexed interval covers; the four boundary-tile possibilities yield one or two covers per checkerboard depending on the residue modulo three. The counting treats the two coinciding index intervals in the four-cycle boundary as differently centred edge sets. The two checkerboard choices cannot represent the same optimum, since their union would exhaust the vertex set and induce a cycle. The packaged brute-force verifier checks ten orders and 5,592,390 endpoint subsets, with no discrepancy. Finite tests do not stand in for the proof.

## Originality — PASS with residual risk

The October 2026 paper by Das–Santra (arXiv:2610.02275v1) supplies general algorithms and the induced-star formulation, but no explicit two-rail ladder optimum-classification or modulo-three count in the inspected full text. The June 2024 graph-products paper of Brešar–Dravec–Hedžet–Samadi (arXiv:2406.04020v2) gives product bounds and the known inequality \(\rho_e^o(G)\le\alpha(G)\), rather than the exact ladder enumeration. The March 2024 algorithmic and 2022 introductory papers likewise do not state this enumerator in the inspected material. Searches for edge-open packing, induced star forests, Cartesian-product ladders, and equivalent one-sided efficient neighbourhood partitions uncovered no dominating result. Other relevant 2026 algorithmic preprints could not be read in full and could contain an unindexed special case; no absolute novelty certification is claimed.

## Value — PASS

The count of optimal solutions stays in \(\{2,4\}\) even as the number of vertices grows, and its period-three behaviour is explained by the unique interval-partition rigidity. This yields a full extremal classification, not merely a numerical value obtained from an already available algorithm. The ladder is a canonical Cartesian product and a basic test family for graph packing parameters; the classification separates the number of optimal edge packings from much larger collections of arbitrary feasible sets. It does not claim a new general inequality or algorithm.

## Limits

The theorem covers exactly the ordinary two-rail ladder with at least two rungs; the count is for labeled edge sets. Published work could contain an equivalent under another graph invariant or unpublished specialization. No independent external review is recorded.

Self-review: passed. Independent audit: not yet performed.
