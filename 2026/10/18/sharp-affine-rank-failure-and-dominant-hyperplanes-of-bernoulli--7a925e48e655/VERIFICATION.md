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
# Reproducibility and scope

Run `python3 checker.py` from the extracted package directory. Only the Python standard library is required. The program executes exact rational affine-hyperplane enumeration and exhaustive retention-pattern tests, including every subset for cube dimensions 3 and 4. It independently confirms the dominant traces, largest nondominant intersection, and exact conditional type counts in those dimensions.

The main theorem for every dimension is proved analytically in `RESULT.md` by the Sperner antichain bound, complete hyperplane enumeration by n-point spanning sets, and Bonferroni bounds. The checker is finite corroboration, not an exhaustive proof in arbitrary dimension. The asymptotic error estimate applies only for fixed p strictly between zero and one. No independent scientific audit was performed.
