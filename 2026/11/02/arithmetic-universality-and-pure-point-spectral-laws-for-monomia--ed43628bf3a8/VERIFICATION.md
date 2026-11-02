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

# Verification record

The proof in `RESULT.md` is analytic. Its critical finite-section identity is the exact arrow map \(e_{g b^j s}\mapsto e_{g a^j s}\), which yields \(\operatorname{rank}(T_N^j)=\lfloor N/(gM^j)\rfloor\) directly, without asymptotic approximations. This rank sequence determines the unit-weight Jordan paths uniquely; their sine eigenvectors and a uniformly summable geometric block tail complete the spectral argument. The exact all-cutoff unitary classification requires both forward and reverse implications, handled by the first two nonzero rank thresholds.

The standalone artifact `checker.py` executes with Python 3 and only its standard library. It builds the finite directed graph independently of the formula, checks each connected path and all power ranks across 272 ordered parameter pairs and 23 cutoff sizes, checks the complete block decomposition and same-parameter fingerprints, and checks elementary limiting-mass identities using exact rational arithmetic. The observed output was `PASS 61661 exact assertions over 272 parameter pairs, 23 truncation sizes, and 135 limiting checks.`

This finite computation does not prove the claims for arbitrarily large cutoffs or replace proof of weak measure convergence. No external independent audit, certification, or expert validation has been performed. Source access was sufficient for the current finite-section comparison against the two most relevant articles; broader historical coverage remains a stated originality risk.
