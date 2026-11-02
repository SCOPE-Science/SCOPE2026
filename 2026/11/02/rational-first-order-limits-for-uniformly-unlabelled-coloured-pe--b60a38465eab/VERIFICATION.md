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

Run `python checker.py` with Python 3 (standard library only). A successful execution prints exactly `ALL_CHECKS_OK`. The script independently enumerates coloured word rotation classes for small parameters, reproduces finite necklace multiset generating-function coefficients through degree \(35\), tests exact marked-necklace identities and known partition coefficients, and checks the limiting fixed-point probabilities numerically for \(q=2,3\). It also tests two-colour simultaneous absence events against the independent geometric prediction.

The general all-sentence assertion is proved symbolically using the isolated pole, a quantitative long-cycle word-occurrence lemma, and standard finite bounded-degree Hanf threshold locality. These infinite statements are not established by the finite checks. The zero-one law for the uncoloured case is earlier literature; only the rational exponentially convergent statement for \(q\geq2\) is assessed as a new contribution. No independent audit has been performed.
