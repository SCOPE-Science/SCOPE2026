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

Run `python3 verify.py` after extracting the accompanying file. The checker is self-contained, imports `fractions` and `itertools` from the Python standard library, and performs exact comparisons without numerical tolerances. It has been run successfully: `PASS: 9900 exact parameter profiles; 504900 cardinality comparisons; 69394 individual subsets.`

The checks include positive definiteness, facet supporting inequalities, strict/non-strict contact classification, endpoint coincidence, the simplex John moment identities, and the positive weight inequalities and second-moment identities of the capped-cube certificate. Individual subset masks are also reconstructed independently for low-dimensional cases. These finite tests do not certify the infinite theorem. The proof in RESULT.md proves it symbolically for all stated integer parameters; John optimality uses actual positive first/second moment contact identities and the established John characterization. No independent mathematical validation has been performed.
