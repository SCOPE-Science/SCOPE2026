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

Run `python verify.py` using Python 3.9 or later; only the Python standard library is required. The program directly constructs eleven independently described graphs, identifies their \((v,k,\lambda,\mu)\) parameters, forms both Gauss polynomial matrices, inverts the denominator over rational numbers, and compares 5,580 exact off-diagonal entries to both rational transition formulas. It additionally verifies exact row sums at five rational steps on each graph and sign changes of the critical quadratic for positive discriminant cases.

Observed execution:

`VERIFY_OK: 11 strongly regular graphs; 55 exact rational Gauss matrices; 5580 exact off-diagonal identities; stochastic row sums; finite-cutoff signs`

The proof for all connected unweighted noncomplete strongly regular graphs uses exact spectral identities in `RESULT.md`. These finite computations do not constitute a complete graph census, an infinite proof, an independent audit, or evidence for claims outside the theorem's stated domain. Publication priority is not guaranteed by negative literature search.
