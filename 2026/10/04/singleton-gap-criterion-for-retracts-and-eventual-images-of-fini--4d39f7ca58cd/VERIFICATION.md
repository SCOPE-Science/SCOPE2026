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
# Verification

`verify_retracts.py` performs an exhaustive finite replay independent of the symbolic proof. For each listed level-size vector it enumerates every nonempty subset, then enumerates every pointwise-fixing map from the ambient weak order to that subset until it either finds an order-preserving retraction or proves none exists by exhaustion. It compares that exact answer with the singleton-gap criterion.

The checked level-size vectors and expected numbers of retract subsets are \((2,2)\mapsto13\), \((2,2,2)\mapsto53\), \((2,3,2)\mapsto96\), \((1,2,2)\mapsto25\), \((2,1,2)\mapsto28\), and \((1,2,3,1)\mapsto78\). The replay terminates with `VERIFY_OK` only if all subsets match and all six counts agree.

These finite computations test the implementation and boundary cases; they are not used to infer the theorem for arbitrary height or level sizes. The general claim rests on the explicit necessity and sufficiency proof in `RESULT.md`.
