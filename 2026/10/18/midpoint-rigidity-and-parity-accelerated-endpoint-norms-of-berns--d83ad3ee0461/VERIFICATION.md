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

# Reproducibility

Run `python check_bernstein_overiteration.py` with Python 3 and SymPy installed. The file independently constructs the full binomial transition matrix, its interior restriction, and exact signed row measures, and checks the survival identity, martingale cancellations, unique candidate midpoint dominance at rational grid points, strict discrete concavity, the Perron eigenvector equation, and the special degree-four two-eigenvalue identity.

The program yields `PASS: 940 exact-rational finite assertions` for degrees 2 through 8 and selected positive powers. This is **finite corroboration**, not exhaustive verification of the universal quantifiers. The proof in RESULT.md supplies the strict-concavity induction, signed-measure identity, reflection symmetry, spectral splitting, and Perron asymptotic independent of numeric testing.

# Limits

No independent audit or independent replication is claimed. Asymptotics are for fixed degree; the general-degree constants implicit in the remainder were not evaluated. Historical-priority coverage is qualified in REVIEW.md.
