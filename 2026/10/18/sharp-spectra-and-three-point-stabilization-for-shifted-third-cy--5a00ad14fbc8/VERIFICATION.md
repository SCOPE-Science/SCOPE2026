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

# Finite verification and proof boundaries

Run `python verify.py` with a standard Python 3 interpreter from the directory containing the file. The included `verification_output.txt` is the output of one successful direct execution; the checker uses no external packages.

The computation verifies the pair formula for \(120000\) shift-index pairs, the three-point stabilization and additional shifts for \(30000\) cases, and independently enumerates complete periods, maximum gcds, all divisors and exact frequency counts for \(73\) shifts, plus a separate higher-prime-power case \(d=49\) with period \(29449\). Exact rational arithmetic is used for distribution checks. Examples appear in the output.

The finite ranges are not a proof for unrestricted shifts, indices or window lengths. The proof in `RESULT.md` supplies the required uniform argument: local unit/discriminant split, the ramified prime \(3\), three-point stabilization, simple-root lifting, CRT, and minimality of each prime-power period.

The closest general gcd-period results in arXiv:2409.01224v1 were read and compared; their abstract framework is explicitly acknowledged rather than claimed as original. Independent validation has not been performed.
