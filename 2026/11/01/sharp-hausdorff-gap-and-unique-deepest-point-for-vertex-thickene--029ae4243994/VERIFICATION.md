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

The universal proof is given in `RESULT.md`; the standalone `verify.py` provides independent rational finite diagnostics. It implements exact nearest-point projection of each scaled barycentric coefficient vector onto all \(d+1\) caps, using a sorted active-set method for the remaining coordinate simplex. This is algebraically distinct from the proof's radial trial point. It checks the exact maximum at each centroid, the global sharp bound, the pointwise stability envelope, and off-centroid strictness in all positive-gap cases.

Command executed against the included program:

```sh
python verify.py
```

Actual output:

```
PASS 16848 exact rational checks of projection/bound/rigidity
PASS exact formula at every centroid and all tested boundary regimes
```

It covers Euclidean simplex dimensions \(2\) to \(6\), nine dilation parameters, and both small full grids and seeded interior rational samples; all calculations use `fractions.Fraction`. The test count refers to rational input vectors, not distinct continuous cases. These tests cannot certify the universal theorem or its historical novelty. Boundary and uniqueness arguments remain mathematical, as reconstructed in the proof. The self-review passed; no independent mathematical audit or external proof certification has been performed.
