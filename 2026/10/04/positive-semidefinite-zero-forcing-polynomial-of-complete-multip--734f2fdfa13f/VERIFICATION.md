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
# Verification

The standalone `verify.py` constructs each complete multipartite graph directly from its part sizes and implements the positive semidefinite color-change rule without using the theorem: after every force it recomputes connected components of the current white-induced graph and tests the unique-neighbor condition inside each component.

It exhaustively checks every initial blue subset for every integer-partition type of order \(2\) through \(10\). For each graph it compares the direct simulation with the structural criterion, builds the coefficient sequence by brute force, compares that sequence with the closed formula, and checks that the least nonzero exponent is \(N-\max_i n_i\).

Exact replay output:

`VERIFY_OK graph_types=128 subset_checks=64916 classification_checks=64916 coefficient_checks=1179 max_order=10`

The finite computation is a consistency check, not an exhaustive proof for unbounded order. The infinite result is established by the component argument in `RESULT.md`.
