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

# Reproduction
Run `python3 VERIFY.py` in the same directory as this file. The script requires only the Python 3 standard library and checks two separately implemented calculations: direct exact integer enumeration of all eligible multiples and carry-transition coefficient accumulation. It checks \(m=1,2,\ldots,8\), totaling \(87898\) positive multiples, and confirms the theorem's range, coefficient and minimum-next-weight predictions for every admissible test parameter \(m\ge2\).

# Mathematical boundaries
The uniform proof is in `RESULT.md`; experimental checks are consistency tests only. In particular, neither exhaustive testing for a bounded set of exponents nor a successful execution establishes independent audit of the unbounded statement. The cutoff is strict: \(0<N<2^{3m}\). No claim is made about all larger multiples.
