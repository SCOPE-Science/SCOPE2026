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

Execute `python3 verify.py` using Python 3 and no third-party packages. The script independently enumerates every pair of functions on one, two, three and four points, calculates both compositions and the image cardinalities, and compares each resulting rank-pair tally with the inclusion–exclusion formula in the theorem. It also checks the recurrence \(F_{N+1}(k)=(k+1)F_N(k)+kF_N(k-1)\), the empty-color boundary and symmetry at a wider finite range.

The exact joint counts from exhaustive enumeration have totals \(1,6,63,976\) in dimensions one through four. Passing the executable produces `VERIFY_OK`.

The exhaustive enumeration is limited to these finite domains. The LDP, its tails and its rate function require the mathematical uniform bounds and optimization supplied in `RESULT.md`; computational evidence does not substitute for this proof. Independent mathematical audit has not been performed.
