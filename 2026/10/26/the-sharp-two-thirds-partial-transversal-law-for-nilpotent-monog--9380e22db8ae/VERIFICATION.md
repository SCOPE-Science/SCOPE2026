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
# Verification of the sharp partial-transversal law

The program `verification/check_monogenic_transversals.py` constructs optimal witnesses from the two modular permutations for every integer \(n\) from 2 to 70. It validates distinct row indices, distinct column indices, distinct product indices, and the predicted formula for each witness. An exact dynamic program over all subsets of compatible nonzero-product cells, represented by used row/column/sum masks, computes the true optimum for each \(n\) from 2 to 12. The one additional zero-product cell is always achievable by \((0,0)\). Running the code with standard Python 3 prints `VERIFY_OK`.

These enumerations are finite checks only. The proof of the formula for all \(n\ge2\) is the integer-sum bound and its explicit odd/even parity constructions in `RESULT.md`. The code is not a formal proof and no external independent audit was conducted.
