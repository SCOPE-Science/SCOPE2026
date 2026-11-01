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

The standalone file `verify.py` computes the signed edge-generator matrix directly from incidence matrices; compares the absolute off-diagonal pattern with line-graph adjacency; compares every edge-column's exact short-time derivative with matrix-exponential finite differences; and checks representative finite-time exponential envelopes. The script computes Perron-optimal positive gauges and verifies that all tested positive weights have logarithmic growth no smaller than the Perron exponent. It independently checks the strict-negative/zero/positive sign classification and the path spectral-gap identity. It additionally performs exact rational arithmetic checks on the generator column identity.

Executed successfully with Python 3, NumPy and SciPy:
`PASS: 1890 weighted-tree Perron/log-norm cases (424 path, 50 claw, 1416 other); 4400 rational column-derivative checks; 23 weighted-path spectral-gap cross-checks.`

All calculations are finite diagnostic tests. The proof of the universal statements is contained in `RESULT.md`. The source-literature comparison is documented in `REVIEW.md` and `AUDIT.json`, with remaining originality risks. No independent audit has been performed.
