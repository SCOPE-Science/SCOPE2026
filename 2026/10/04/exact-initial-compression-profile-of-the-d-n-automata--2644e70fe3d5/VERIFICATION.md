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

The proof is symbolic and does not depend on finite computation. The supplied `artifacts/verify.py` gives two corroborating checks:

1. It exhaustively constructs the power automaton for every integer \(n\) from 4 through 18. For every target through the claimed boundary, it computes the true shortest distance and the number of shortest words. It verifies distance \(3s-2\), exactly one shortest word, and strict failure at the next target.
2. It directly replays the explicit witnesses and the saturation boundary for every integer \(n\) from 4 through 300.

Running the script with a standard Python 3 interpreter prints `VERIFY_OK`.

The infinite proof remains the primary evidence. Finite checks do not establish the theorem beyond the tested range.
