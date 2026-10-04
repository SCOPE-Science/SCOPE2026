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

The theorem is proved for all lengths; finite computation is supplementary.

`verify.py` is a standard-library-only independent implementation. It computes the universality index and the number of distinct subsequences of the SAS length directly, exhaustively enumerates every binary word through length \(14\), checks the claimed maximum, tests the explicit extremizers through length \(31\), checks the transfer recurrence through twelve arches, and checks the Fibonacci product inequality over a much larger finite range. It terminates with `VERIFY_OK`.

`census.c` is a separate exhaustive implementation using integer dynamic programming for distinct subsequences. Compiled with a standard C compiler and run through length \(22\), it produced `census_22.txt`. The maxima match the theorem at every tested length.

These checks do not certify the infinite theorem by enumeration. The infinite proof rests on fixed-universality subsequence monotonicity, the two boundary matrices for minimal binary arches, a Fibonacci induction, exhaustive symbolic treatment of the six possible terminal length-three components and the two possible interior length-three arches, and the proved inequality \(F_aF_b\le 2F_{a+b-3}\) for \(a\ge2\), \(b\ge4\).
