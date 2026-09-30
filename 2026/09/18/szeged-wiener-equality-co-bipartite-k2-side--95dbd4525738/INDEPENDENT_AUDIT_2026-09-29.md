# Independent audit — 2026-09-29

Record: `2026/09/18/szeged-wiener-equality-co-bipartite-k2-side--95dbd4525738`  
Assigned and audited source tree: `9c097a26abbfe3024e2260f1bfbf6b0ab0dc489f`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **repaired**

## Correctness

**independently_supported**. The polynomial formula and equality classification are correct. They are exactly the xy-adjacent specialization of the earlier n−2-clique record after exchanging the meanings of C and D (and harmlessly swapping A/B labels). Independently, the defining distance count yields eta=8ab+2c(a+b)+3d(a+b)+4cd−4d, and the integer equality equation leaves only (1,1,0,q−2) for q≥8 plus, at q=8, the label-swapped (1,0,1,6) exceptional type. The committed standard-library verifier exhaustively checks 10,165 two-connected parameter quadruples for q≤20 and is consistent with the theorem.

## Originality

**requires_provenance_repair**. The original record's 'originality PASS' language is not sustainable against the repository's own chronology. The broader record `szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8` was committed at 2026-09-18 03:47:31 UTC and already contained the adjacent-case formula and the same equality classification under a different C/D convention. This co-bipartite record was committed later, at 16:45:35 UTC. Therefore it cannot be presented as a separate discovery. The corrected record is retained as an alternate derivation and reproducibility package for a specialization of the earlier same-day result.

## Scientific value

**useful_corroborating_specialization**. After provenance repair, the record still has value as a compact specialization with a transparent diameter-two derivation and an exhaustive verifier. Its scientific value is corroborative/reproducibility-oriented rather than an independent advance beyond the earlier broader SCOPE theorem.

## Evidence and literature checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/c0fc87c28df975025d87707c9327bc68127a1d1c
- https://github.com/SCOPE-Science/SCOPE2026/commit/ee5c15cc4854aeb7f2bc365710ddbce1f7699f25
- https://github.com/SCOPE-Science/SCOPE2026/tree/c0fc87c28df975025d87707c9327bc68127a1d1c/2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8
- https://arxiv.org/abs/2609.20025
- https://doi.org/10.1016/j.amc.2017.05.047

## Limitations

- The corrected record makes no separate originality claim relative to the earlier broader SCOPE record.
- The theorem is only the adjacent-outside-vertices co-bipartite specialization of the high-clique classification.
- The global Zhang–Li equality problem remains open.
