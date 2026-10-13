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

## Reproduction
Run `python3 verify_rm_pair.py` using Python 3.8 or newer and no third-party packages. It constructs \(2^{m+1}\) affine words at every \(m\in\{2,3,4,5,6,7,8\}\), calculates cyclic pair weights directly, recomputes the complete claimed enumerator, and uses independent binary-row reduction to check each low-weight span and component count for every integer \(0\le\alpha\le2^m\). The expected terminal marker is `VERIFY_OK`.

## What is and is not verified
The tests are exhaustive at each tested length, not an infinite formal certificate. The all-length proof rests on the binary carry-transition identity and the strictly positive coefficient filtration, as shown in `RESULT.md`. The two highly relevant primary papers with full-text access limits are named in `REVIEW.md` and `AUDIT.json`. No independent external audit was performed.
