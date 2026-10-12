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

The proof uses only Kummer's carry theorem and complete parametrization of selected indices. For \(2\le q<p\), the selected index \(p+1\) gives zero carries. At \(q=p\), every selected index is \((p+1)d\), \(1\le d\le p-1\), and the two occupied base-\(p\) columns each force a carry, giving exactly two.

`verify.py` checks these carry counts and the corresponding Legendre-formula valuations for every prime \(p\le101\); it also computes the actual restricted integer GCD at the target row for primes \(p\le31\). Replay output:

`VERIFY_OK primes=26 pretarget_rows=1109 target_coefficients=1135 direct_gcd_rows=11`

The computation is finite corroboration only. It does not certify the infinite theorem, which is proved symbolically in `RESULT.md`. No independent audit or independent validation has been performed.
