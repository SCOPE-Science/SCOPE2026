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

# Reproducibility and verification

The complete theorem follows from the explicit pair-state transfer matrix, the integer identity \(T^4=T^3+T\), the twenty small base triples, and induction in the three path lengths. This is a finite base for a rigorous infinite recurrence, not an empirical extrapolation.

`python3 verify_theta.py` reproduces (a) the matrix identity by exact multiplication, (b) cycle counts and their recurrence, (c) each base-table count by the matrix formula and an independent brute-force edge-subset test, (d) additional direct brute-force theta counts, and (e) the theta recurrence and cycle inequality over a larger bounded parameter grid. The script requires no network connection or third-party packages and completed with `VERIFY_OK`.

The machine check is not a proof of literature priority; the algebraic recurrence and induction are presented in `RESULT.md` for direct mathematical scrutiny. Independent audit has not been performed.
