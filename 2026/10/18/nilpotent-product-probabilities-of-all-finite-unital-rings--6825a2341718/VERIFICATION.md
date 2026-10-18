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

The general argument is mathematical: the Fitting-decomposition count gives \(q^{r^2-r}\) nilpotent \(r\)-square matrices; conditioning on the rank of the first factor gives \(q^{n^2-r}\) successful second factors; averaging kernel sizes gives \((2q^n-1)/q^{2n}\); nilpotence lifts across nilpotent ideals and hence across the Jacobson radical of a finite unital ring.

Reproduce finite checks with `python verify.py` from the same directory. The program uses only the Python standard library, enumerates the five full-matrix instances, confirms every rank-conditioned count, and additionally tests the dual-number, noncommutative-local, and triangular finite rings. Expected pair counts are listed in `RESULT.md`. Every test completed successfully when run from the packaged source. The code does not establish the theorem outside these finite instances; the preceding proof is responsible for general quantifiers. No external independent audit has been performed.
