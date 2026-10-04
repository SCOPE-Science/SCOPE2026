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
The finite replay is `verify.py`.

It checks the growth cutoffs used to force \(v\le4\) when \(p\equiv1\pmod4\) and \(v\le5\) when \(p\equiv3\pmod4\). It then exhausts the analytically bounded ranges and confirms that the maximum divisibility exponents in the non-Mersenne \(p\equiv3\pmod4\) branch are \(0,1,1,2,2\) for \(v=1,\ldots,5\).

The enumeration intentionally admits composite candidates. This is an over-enumeration: every prime candidate is included, while no probabilistic primality test is needed.

The infinite branch \(p=2^\alpha-1\) is not certified by enumeration; it is handled symbolically in the proof using LTE.
