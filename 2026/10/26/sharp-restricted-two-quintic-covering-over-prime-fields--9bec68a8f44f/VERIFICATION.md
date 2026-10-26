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

# Verification and limits

Run `python3 verify_quintic.py` from the same directory as this file. The verifier uses only the Python standard library and exact integers. It enumerates all primes through 240, obtains nonzero fifth-power values both directly and using primitive roots, and independently determines restricted pair sums by pair enumeration and residue complement lookup. The missing-residue lists for all eleven primes congruent to one modulo five are checked against the explicit mathematical certificate, including the exact six nonempty lists. The primes two and three are separately checked.

For every prime congruent to one modulo five at least 241, no finite computation is assumed. The mathematical proof uses the smooth genus-six Fermat quintic and a bound of at most forty excluded rational points. A strict Hasse–Weil inequality follows from the exact check `(241-39)**2>144*241` and monotonicity of `(p-39)**2-144*p` above 241. The verifier checks the endpoint inequality, not the Hasse–Weil theorem itself.

The 2017 paper and 2023 power-residue decomposition preprint were inspected in accessible full text. The later Karabulut paper's full text could not be accessed; only its abstract was available, which is noted as an originality limitation. No independent external mathematical audit is claimed.
