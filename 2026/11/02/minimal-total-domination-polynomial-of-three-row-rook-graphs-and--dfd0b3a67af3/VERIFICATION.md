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

# Reproduction

Run `python3 verify.py` using the standard Python 3 library. The program creates adjacency masks for each labeled rook graph \(K_3\square K_n\) with \(3\le n\le7\), checks every nonempty vertex subset against all open neighborhoods, and uses the private-neighbor condition for inclusion-minimality. It compares each complete size-frequency dictionary against the explicit polynomial coefficients.

Expected final line: `VERIFY_OK cases=5 tested_subsets=2396667`.

The checked total is exactly \(\sum_{n=3}^{7}(2^{3n}-1)=2,396,667\). This is exhaustive only for the five stated orders. The all-order proof is mathematical, not a computational induction. Formal proof-assistant verification and independent mathematical audit have not been performed.
