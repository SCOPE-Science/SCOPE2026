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

# Verification of the prime-support bound

The embedded script `verify_sandor_support.py` uses only Python's standard library and integer arithmetic. Execute `python verify_sandor_support.py` from the directory containing the script. It generates smallest-prime-factor data, the exact Dedekind psi values via multiplicative prime-power recurrence, the distinct-prime-factor count and an exact totient sieve. It checks all \(3\le n\le300000\) with \(\omega(n)\le5\): the scaled inequality \(385\varphi(\psi(n))\le384n\), and the equality criterion \(n=2^a3^b\cdot385\) with \(a,b\ge1\). It also confirms \(\varphi(\psi(2))=2\), \(\psi(2310)=6912\), \(\varphi(6912)=2304\), and \(\psi(39270)=124416\), \(\varphi(124416)=41472\).

The observed run returned `VERIFY_OK`; it checked 299731 eligible integers in the interval, 22 sharp-equality integers, and found 39270 as the first positive violation among all integers up to 300000, with 23 positive violations in that interval. The exhaustive interval is finite; it must not be confused with the unbounded mathematical proof in `RESULT.md`. The general inequality and all equality cases rest on four symbolic case arguments and exact prime-factor products. Scientific overlap risk and lack of independent audit remain explicitly documented.
