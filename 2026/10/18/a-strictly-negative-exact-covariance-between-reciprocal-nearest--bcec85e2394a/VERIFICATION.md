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

# Verification of the finite covariance and its conditional identity

Run `python verify.py` with Python 3 and only standard-library modules. The program checks each cyclic ordering for sizes \(n=5,6,7,8\), all high-gap counts \(0\le k\le n\), and the exact conditional covariance formula. It also checks the Dirichlet-simplex threshold distribution at eight rational radii, compares the resulting unconditional moment with the closed form, and checks the interpretation of the gap statistic as an actual reciprocal-nearest-neighbor count and isolated-vertex count on 9,000 independently reproducible point configurations. The completed output was:

```text
checked n= 5 permutations= 120
checked n= 6 permutations= 720
checked n= 7 permutations= 5040
checked n= 8 permutations= 40320
VERIFY_OK permutations= 46200 checks= 45131
```

The executable uses exact rational arithmetic for all finite enumerations and checks three illustrative large-size critical-window values numerically. The analytic Dirichlet simplex-volume argument, conditional rank calculation, and limits—not the finite computations—prove the infinite all-size statement. In particular, the verification does not establish any unknown general high-dimensional analogue, any unpublished priority claim, or an independently audited certificate.
