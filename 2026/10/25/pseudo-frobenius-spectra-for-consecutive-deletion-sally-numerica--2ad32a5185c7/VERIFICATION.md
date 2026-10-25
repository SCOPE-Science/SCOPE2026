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

The standalone `verify.py` program uses two different computational representations of membership: an Apéry shortest-path computation on residues modulo the multiplicity, and, for the smaller cases, a separate forward dynamic program. It enumerates actual gaps and evaluates the defining pseudo-Frobenius condition against every minimal generator. For all admissible parameters through multiplicity 48 it tests the exact gap sets, pseudo-Frobenius sets, Frobenius number, genus, Cohen–Macaulay type, almost-symmetry defect and the all-position type bijection.

Command: `python3 verify.py --max-e 48`

Observed output: `VERIFY_OK cases=10857 checked_gap_counts=530299 e_max=48`.

The infinite assertions follow from the symbolic interval arguments and Apéry-socle proof in `RESULT.md`, not from extrapolating the finite run. Checks do not establish novelty or independent scientific validation. The known symmetric cases and related prior formulas are acknowledged in `RESULT.md` and `REVIEW.md`.
