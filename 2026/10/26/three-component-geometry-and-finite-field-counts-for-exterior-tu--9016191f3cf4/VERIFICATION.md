---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible mathematical checks

The attached `verify_square_zero_flags.py` contains all numerical steps used here; run `python verify_square_zero_flags.py` with NumPy available. The program constructs all five-coordinate portions of square-zero strictly upper-triangular matrices over fields of sizes two, three, four and five, derives the anticommutation test directly from elementary matrix products, and forms the finite adjacency matrix of admissible ordered pairs. The missing top-right coordinate is central and contributes exactly one arbitrary scalar per matrix. For every field, it computes the single tuple count from the square-zero list, the pair count by summing adjacency entries, and the triple count by taking the trace of the cubed adjacency matrix. Thus the triple test is exhaustive without constructing every triple explicitly.

Observed counts (tuple length one, two, three respectively): field order two: 28, 448, 6112; field order three: 153, 10449, 657801; field order four: 496, 96256, 19035136; field order five: 1225, 540625, 265065625. Each was compared against the closed formula, with exact integer equality in all twelve comparisons. The characteristic-two extension field of order four uses a polynomial presentation, not arithmetic modulo four.

The software tests only these four field sizes and tuple lengths one through three. It neither verifies generic irreducibility nor proves an infinite-field theorem. Those assertions are proved by the component and rank-one subspace arguments in RESULT.md. The unreduced scheme and all higher matrix sizes are outside the claim.

A second independent enumeration (`python verify_rulings.py`, no third-party packages) checked the exact common-image, common-kernel, and double-ruling counts for pairs over the prime fields of orders two, three and five. All three complete finite comparisons passed with the marker `RULINGS_INTERSECTION_OK`. These experiments support, but do not establish, the generic component assertions.
