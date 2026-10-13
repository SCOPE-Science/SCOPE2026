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

# Verification of the palindrome classification

The scope is **linear indexed binary palindromes**, with all sixteen length-four contiguous non-wrapping factors required. The shortest length is 24; the six words are in `RESULT.md` and `solutions.txt`.

`python3 verify_direct.py` enumerates all \(2^{\lceil L/2\rceil}\) palindromes of each length \(4\le L\le24\). It independently measures factor coverage and checks that the numbers of covering words are zero for lengths 4 through 23, and six at length 24, matching the six hard-coded witnesses. Its observed status was `DIRECT_OK`.

`python3 verify_orbit_dp.py` instead builds all length-fourteen prefixes by a last-three-bit/ten-orbit-mask dynamic program. Its invariants include generation of exactly \(2^j\) prefixes after \(j\) steps, for \(3\le j\le14\). It filters all-orbit coverage and palindromic center and obtains exactly six witnesses; its observed status was `ORBIT_DP_OK`, with 1,382 final states and 16,384 generated prefixes.

These programs check different presentations of the finite exhaustive claim. The mathematical minimum-length obstruction additionally follows from the four odd vertices of the reflected de Bruijn graph, independently of any computation. Completeness is finite, not extrapolated to larger factor length or alphabet size. No separate external audit is represented by this document.
