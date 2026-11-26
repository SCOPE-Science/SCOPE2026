---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the exact randomized Ritz-vector law

The proof uses the unitarily invariant null line of the test operator to give the eigenvector coefficient as a quotient of independent Gaussian linear forms. Integrating the ratio of their squared magnitudes gives the exact normalized angle CDF and mean. The expansion of that mean gives the logarithmic coefficient. The eigenvalue tail is an already covered property of the non-spectator root and is not the finding.

The accompanying `verify.py` uses Python 3, NumPy and mpmath. The recorded run checked six high-precision integral values, the uniform resonance, four small-angle cases and direct compressed pencils at four trial angles with 110,000 sketches per angle. The finite pencil checks compare the matrix structure, CDF and mean, and include an eigenvalue-tail diagnostic. Finite sampling neither proves the exact angle formula nor establishes the small-angle asymptotic.
