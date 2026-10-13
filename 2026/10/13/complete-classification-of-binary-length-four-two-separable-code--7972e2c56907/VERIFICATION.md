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

Run `python3 verify.py`.

The verifier performs complete finite checks:

1. Generate all \(16\) binary words of length \(4\).
2. Test every one of the \(11\,440\) seven-subsets and \(12\,870\) eight-subsets.
3. Construct every singleton and pair descendant by two independent methods and require their separability verdicts to agree.
4. Require exactly \(240\) valid seven-subsets and no valid eight-subset.
5. Generate all \(384\) binary Hamming isometries and partition the complete maximum set.
6. Recompute the orbit sizes, stabilizers, and pairwise Hamming-distance distributions.

The expected terminal line is:

`VERIFY_OK maximum=7 labeled_maxima=240 orbits=2 orbit_sizes=48,192 stabilizers=8,2`

The computation is exhaustive only for the stated finite domain.
