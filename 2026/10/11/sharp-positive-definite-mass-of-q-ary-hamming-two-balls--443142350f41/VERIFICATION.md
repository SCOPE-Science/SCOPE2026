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

The supplied `check.py` is a standalone Python 3 standard-library script. Running `python check.py` verified 558 parameter pairs \((q,d)\) using exact rational arithmetic, including nine choices of \(q\) (among them nonprime prime powers) and all \(3\le d\le64\). It checked the defining Krawtchouk identities, normalized expected Fourier mass, dual-contact identity, nonnegativity at all Hamming weights, and the exceptional optimizer transition.

The same script computed all characters and all time-domain coefficients directly for six small groups: \(q=3\) and \(d=3,4,5\); \(q=4\) and \(d=3,4\); \(q=5\) and \(d=3\). The order-four additive character uses the \(\mathbb F_2^2\) representation. All checks passed. The general theorem is proved algebraically in `RESULT.md`, not inferred from these finite checks. No independent audit, external certification, or unperformed calculation is represented by this document.
