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

# Verification and reproducibility

The mathematical proof applies to every real \(\nu>2\), with centered symmetric interval radius \(r>0\). The normalized Student density and exact derivative of its log-ratio against the standard Gaussian are derived in `RESULT.md`. The key analytic checks are the strict Jensen inequality at the origin, normalization forcing the minimum log-ratio below zero, the exact derivative sign pattern, the tail equalities at the unique probability crossover, and uniform Student-tail/Gaussian-Mills asymptotics as degrees approach two.

Run `python verification.py` in an environment with Python 3 and SciPy. The script checks exact Hermite polynomial identities using rational arithmetic, and numeric density/central-tail crossing brackets for twelve chosen degrees. It also prints the leading endpoint consistency checks. These are spot checks only; the theorem and the sharp constant follow from the analytic proof, not from finite enumeration.

The large-degree expansion relies on the already-published local approximation in Ouimet (2022), arXiv:2201.05950v2, rather than a new independent derivation. No complete symbolic closed form of the unique radius is claimed. The statement has not been independently audited or externally certified.
