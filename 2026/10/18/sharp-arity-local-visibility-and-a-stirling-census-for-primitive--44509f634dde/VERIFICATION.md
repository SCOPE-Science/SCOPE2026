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

The mathematical proof uses an exact profile invariant, a hitting-set argument and partition enumeration. Run `python3 verify.py` from the directory containing this document. The script requires only Python 3 standard-library modules; it checks all teams up to the first possible obstruction size for every pair \((k,r)\) with \(2\le k\le4\) and \(1\le r<k\), testing all omitted Boolean valuations.

The executed checker reported `PROJECTION_VISIBILITY_VERIFY_OK comparisons= 42980`. It found 160 minimally hidden pairs when \((k,r)=(4,2)\), and 16 when \((k,r)=(4,3)\), matching the exact formula. It also verified that none of the tested smaller teams hides any tuple, that every tested extremal witness has precisely the characterized disjoint supports, and that invisible tuples are unique in the relevant \(r\ge2\) cases.

These are finite checks only. They do not exhaust arbitrarily large \(k\), and the theorem's quantifiers are discharged by the proof in `RESULT.md`. There is no machine proof or independent audit claim.
