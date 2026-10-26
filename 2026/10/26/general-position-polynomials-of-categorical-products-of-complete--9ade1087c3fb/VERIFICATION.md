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
# Reproducible mathematical checks
The standalone program `gp_direct_verify.py` uses the literal product adjacency rule and breadth-first shortest-path distances to test the original geodesic definition, without assuming the structural classification. For all \(365056\) subsets across \(K_3\times K_3\), \(K_3\times K_4\), \(K_3\times K_5\), \(K_3\times K_6\), and \(K_4\times K_4\), it checks the induced-path equivalence, the complete polynomial, the distinct structural shapes, and the polynomial of inclusion-maximal sets. The code independently recalculates all expected coefficients by integer binomial formulas. Additional exact-arithmetic checks verify the coefficient valley for \(4\le p\le50\) with \(q=2p+4\). Run `python3 gp_direct_verify.py` with standard Python 3; no third-party packages are required. The accompanying stdout file `gp_direct_verification_output.txt` records successful execution and representative coefficient distributions.

These computations cover only finite parameter ranges, so they are not a proof for all dimensions. The infinite claim follows from the structural and elementary factorial/binomial arguments in `RESULT.md`. No independent audit or external certification is claimed.
