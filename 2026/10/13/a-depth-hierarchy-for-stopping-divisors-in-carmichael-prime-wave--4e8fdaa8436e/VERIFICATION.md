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

The universal claim is proved in `RESULT.md`; the computation below is supplementary.

`verify.py` performs exact integer arithmetic. It enumerates every Carmichael number through \(2{,}000{,}000\) by Korselt's criterion, enumerates each one's divisors, computes the least stopping divisor directly from \(d\lambda(d)>n\), and checks \(p_j^{j+1}<n\) for all applicable \(j\). It also checks the integer ceilings reported for \(B=10^{24}\).

The finite enumeration is not exhaustive for all Carmichael numbers and therefore is not used as proof of the infinite theorem. No external certificate or independent validation is claimed.
