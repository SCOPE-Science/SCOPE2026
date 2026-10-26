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

Run `python3 CHECKER.py` from the directory containing these documents. The checker performs an exact rational identity check for \(25/27\), a dense deterministic scan of real coefficient ratios, random complex kernel tests using a fixed seed, and explicit angular sharpness witnesses. A successful run reports the exact count and the sharp numerical ratio. The proof's two decisive algebraic reductions are \(r=x^{-1}\Rightarrow\partial_r F/2=-2/x\) and \(r=2/x-x\Rightarrow\partial_r F/2=2(2x^2-3)/x^3\); these can be reproduced with elementary expansion. All computations are supplementary to the analytic argument and none is used to infer a universal inequality from finite sampling.

No independent audit has been performed. The historical originality assessment is limited by the inaccessible full text of the 1984 Bonsall article and by possible unindexed earlier computations.
