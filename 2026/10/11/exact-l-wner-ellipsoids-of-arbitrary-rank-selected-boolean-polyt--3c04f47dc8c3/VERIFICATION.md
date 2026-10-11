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
# Verification scope

The accompanying `verify_rank_shell_ellipsoids.py` uses the Python standard library only. To replay from the same directory, execute:

```sh
python3 verify_rank_shell_ellipsoids.py 11
```

The scripted checks enumerate all full-dimensional sets of allowed Hamming weights for dimensions 2 through 11, check exact rational membership of the cube moment in the moment polygon, evaluate candidate edge-optimal covariances, test representative squared distances for each rank under permutation symmetry, and test the eight-dimensional nonextremal-support example. The run passed 8089 cases with 44957 rank-layer inequalities, representing 5588288 binary vertices by orbit multiplicity. Floating-point roots and inequalities are not symbolic verification of all parameter values. The analytic certificate is the rank-covariance variational proof and moment-polygon boundary exhaustion in `RESULT.md`. No independent scientific audit has been performed.
