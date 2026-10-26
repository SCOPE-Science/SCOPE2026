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

# Exact reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. This execution printed `PASS exact assertions: 31990`.

The checker enumerates every word of each fixed binary composition for all lengths \(6\le n\le13\); directly counts \(001\) and \(010\) at every consecutive start; and compares independently enumerated rational expectations, mixed moments and covariances to the closed forms. It separately checks the original overlap moment identity, the reduced polynomial formula, and the sharp sign and polynomial-slack identities on all admissible grid points with \(1\le a\le80\), \(2\le b\le80\).

All arithmetic uses exact Python integers and `fractions.Fraction`; no random draws, floating-point tolerances, or network resources are involved. The finite checks test the implementation and boundary behavior but do not replace the unlimited exact counting argument and sign proof. No separate external validation has been obtained.
