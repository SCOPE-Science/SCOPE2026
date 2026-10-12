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

`verify.py` performs four checks with exact integer/rational arithmetic: (1) the five support-count extremal bounds exclude every largest prime at least 389; (2) all ordered positive exponent compositions of 5 are enumerated; (3) monotone pruning is used only when the best possible continuation has abundancy at most 2; and (4) the exact survivor set is compared with the ten claimed families and `classification.json`.

Expected terminal line:

`VERIFY_OK count=121 min=945 max=442365 pmax_bound=383`

The finite enumeration is exhaustive only after the symbolic largest-prime cutoff. No claim is made for higher multiplicity layers.
