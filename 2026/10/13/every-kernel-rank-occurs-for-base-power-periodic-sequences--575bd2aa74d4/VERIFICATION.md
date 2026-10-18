---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Depth t decimations are constants, so at most 1+k+⋯+k^t distinct nodes; a period word with all symbols distinct attains it. Least period k^t forces a nonconstant depth-(t−1) chain whose t distinct ancestors cannot cycle because all depth≥t nodes are constants; plus two distinct constant outputs gives lower t+2. Interleave m≤k lower-exponent periodic child sequences with pairwise private nonzero symbols and shared 0: exact period multiplies k, and kernel rank is 2+Σ(q_j−1). For all except binary exponent-2 boundary, intervals I_m=[2+mt,2+m(B_{t−1}−1)] connect whenever B_{t−1}≥2t; direct base words 0001,0102,0012,0123 cover (2,2). Unsharing zeros among maximal children fills top k−1 ranks through B_t. Independent equality-pattern partition census confirms all intervals for (k,t)=(2,1),(2,2),(2,3),(3,1),(3,2), totaling 25,285 primitive patterns; finite enumeration is not the all-parameter proof.

## originality

PASS

Best-of-knowledge: the full primary magic-number paper explicitly confines complete classifications to coprime periods and identifies noncoprime cases as outside the result. This theorem resolves the natural base-power subfamily with a constructive no-gap rank spectrum, not reducible to the cited general maximum bound. Bosma’s binary-specific upper/lower questions are different. No directly covering published Resultary result found.

## value

PASS

The set of attainable k-kernel ranks of a canonical noncoprime family is a natural exact automatic-sequence invariant. The proof determines both universal sharp endpoints and every intermediate possible value across all bases/exponents, with a nontrivial interleaving induction and exceptional binary boundary. The precision can support future automata complexity classifications independently of a more general mixed-period theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
