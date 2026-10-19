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

# Reproducible finite checks and logical boundaries

The included `checker.py` requires Python 3 and only its standard library. Run `python3 checker.py`; its final success marker is `VERIFY_OK`.

It enumerates every matrix and checks its square, entry by entry, for \(d=3,q=2\) over the two nonisomorphic length-two chain rings \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\). Both give \((512,672)\) in residue ranks zero and one. Dimension-two cases at \(q=2,3\) are additional consistency checks. It independently enumerates square-zero reductions and directly row-reduces \(NX+XN\) for \(d\le4\) over \(\mathbb F_2\) and \(d\le3\) over \(\mathbb F_3\), confirming each kernel dimension and summed stratum count. At \(d=4,q=2\) the three stratum counts are \((65536,107520,53760)\).

The checker does not test arbitrary prime powers or every matrix dimension. The uniform total-variation estimate is proved by the analytic tail bound in `RESULT.md`; it is not inferred from finite enumeration. No independent audit is claimed or supplied.
