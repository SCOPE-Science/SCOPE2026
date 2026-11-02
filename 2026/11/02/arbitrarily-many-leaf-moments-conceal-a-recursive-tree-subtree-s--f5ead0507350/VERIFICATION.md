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

## Reproducible finite checks
Execute `python3 verification/check.py` with Python 3. The program exhaustively enumerates all \(46{,}232\) increasing labelled recursive trees of sizes \(3\) through \(9\) by independent parent choices and computes from each parent list the descendant set of vertex \(2\) and the **whole-tree** leaf count. Its independent leaf-count recursion supplies unconditional laws; convolution supplies the proposed conditional laws. It verifies exact size uniformity, probability normalizations, conditional convolutions, all eligible raw moment orders at those sizes, difference of supports, and covariance values using `fractions.Fraction`. The executed outcome was `PASS: 202 exact-rational assertions; exhaustive recursive trees n=3..9 (46232 trees).`

## Boundaries of verification
The finite checker is not a proof of all sizes or all moment orders. Unlimited-size validity follows from the exact colour urn decomposition, independent uniform parent choices within colours, the Eulerian recursion and the connected-dependence cumulant argument in the proof. The historical novelty comparison includes an inaccessible high-priority older article; independent mathematical audit was not performed.
