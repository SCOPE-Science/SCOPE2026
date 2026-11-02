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
The standalone deterministic Python program `verify_stability.py` was run against the exact source packaged here. It enumerates all permutations of \(2k\) labels for \(k=1,2,3,4\), checking the finite analogue \(B\le(k-1)F\) and \(d_{\rm TV}\le kF\) in each case; the total is 82,138 exact integer assertions. It separately checks the explicit sharp witnesses. `verification_output.txt` records the output.

The proof in `RESULT.md` is mathematical and works for arbitrary couplings, not just deterministic finite permutations. Numerical enumeration therefore supplements but does not certify the infinite statement. The priority comparison is self-review and does not constitute an independent audit.
