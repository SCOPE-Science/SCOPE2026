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
# Reproduction instructions

Run `python verify.py` with Python 3 and no third-party packages. The script operates entirely on integer-coefficient polynomial lists and performs independent checks of the fiber formula, transfer-matrix traces, recurrence, and boundary coefficients. It does not access networks or external datasets.

The exhaustive literal \(\{0,1,2\}\)-assignment checks cover every assignment on the \(2n\) labeled vertices for \(3\le n\le6\), totaling \(597780\) assignments, including invalid assignments. The separate subset formula is checked for every subset of each cycle for \(3\le n\le12\). Matrix traces are computed exactly for orders up to \(14\), the recurrence is tested for \(4\le n\le14\), and minimum multiplicities are checked for \(3\le n\le14\).

Successful output is exactly:

`VERIFY_OK brute_orders=3..6 assignments=597780 subset_orders=3..12 trace_orders=3..14 polynomial_recurrence_orders=4..14 minimum_counts=3..14`

These are finite checks, not a proof for every \(n\). The general proof is provided in `RESULT.md`, including the local classification, the cyclic transfer, the characteristic polynomial, and a complete extremal gap count. No independent audit was performed.
