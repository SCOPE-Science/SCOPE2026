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

# Reproducible verification

Run `python3 verification/verify.py` with SymPy installed. The exact output in `verification/verification_output.txt` ends with `ALL_CHECKS_PASSED`. The tests check the coefficientwise Grassmannian equation, the elimination chart with the square-zero parameter, Gröbner reductions of all pairwise products of the six scroll minors over characteristic zero and finite prime characteristics 2, 3, 5, 7, and the complete-intersection Hilbert function in degrees 0–12.

These finite checks are not an exhaustive proof for every prime characteristic. The complete proof in `RESULT.md` instead uses polynomial identities, the absence of lines on a smooth conic over any field, the regular-sequence criterion in a polynomial ring, the scheme-theoretic local chart, duality and cohomology. The tangent-cone multiplicity is deduced from the homogeneous quadratic complete intersection, not from sampled counts.

Self-review: passed. Independent audit: not yet performed.
