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

The claim follows from independent stationary-generator equations, an exact finite-cycle Green resolvent, a strictly positive derivative representation, and explicit hyperbolic asymptotics. These are full-domain analytical arguments. The finite computer checks below only provide corroboration.

The companion `voter_ring_verifier.py` is a self-contained Python 3 program using only standard-library modules. Run `python3 voter_ring_verifier.py` from a directory containing the file. Its completed execution returned:

```
Exact rational generator checks: 16 PASS
All-distance strict ordering checks: 200 PASS
Finite-size profile, domain-wall, memory-gap scaling checks: 36 PASS
```

The first group builds and solves the complete stationary generator for the joint initial/environment mixture, exactly in rational arithmetic, for both dynamical protocols at two cycle sizes and two rational reset rates. It is independent of the proof's resolvent derivation. The other groups inspect sign claims for finite parameter sets and convergence for four scaling parameters. They neither certify all real rates numerically nor prove the infinite-size limit by extrapolation.

No external independent audit or formal machine-checked proof is claimed.
