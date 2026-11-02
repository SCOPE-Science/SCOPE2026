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

# Verification record

The proof in `RESULT.md` derives the result for every positive integer length from explicit parity, zero-run, and substitution statements. The companion executable `verify.py` was run with Python 3 and returned:

`VERIFY_OK: independent 2-adic construction, 120 exact factor lengths, class-level desubstitution, 13 complete binary necklace censuses`

Checks performed: the first \(2^{17}\) symbols of the morphic word agree with the separately coded \(\nu_2(i+1)\bmod2\) characterization; the computed factor languages in prefixes of lengths \(2^{15}\) and \(2^{17}\) agree for \(1\le n\le120\); direct cyclic-rotation checks yield the claimed counts in that range; for even lengths in this range, the actual accepted sets agree after morphic expansion of their half-length accepted sets; all indexed binary length-\(n\) words for \(1\le n\le13\) were also tested under the all-rotation predicate.

Limitations: comparison of two long finite prefixes does not by itself certify that every infinite-word factor has appeared. Enumeration at any finite cutoff cannot establish the infinite formula. The mathematical proof is independent of these finite cutoffs, and the checks do not establish originality or independent validation.

Reproduce by extracting `verify.py` from this finding and running `python3 verify.py`. The script uses only the Python standard library.
