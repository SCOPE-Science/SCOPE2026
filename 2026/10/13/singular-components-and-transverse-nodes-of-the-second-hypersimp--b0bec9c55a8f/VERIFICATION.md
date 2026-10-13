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

# Reproducibility and limits

With Python 3 and SymPy installed, run `python check_hollow.py`. The saved `check_output.txt` was generated from the actual packaged code with exact symbolic arithmetic. It records the fixed-seed derivative tests, Schur-complement identities, explicit isotropic Gram matrices and independence of three normal directions for matrix sizes five through eight. The proof of the all-size result appears in `RESULT.md`; the checker is finite and does not establish mathematical induction, irreducibility or uniqueness.

The Jacobian support formula is set-theoretic and yields the **reduced** singular locus, not an assertion of a radical Jacobian ideal. The local analytic normal forms apply only on specified nonempty open subsets; more singular intersections are outside the statement. This package has not received independent mathematical audit or external certification.
