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
# Reproducibility and limitations

From the directory containing the embedded files, execute `python3 verify.py` using only the Python standard library. The script independently enumerates all permutations of orders two through eight (46,232 total), verifies exact inversion means and variances, matches the two corner-coordinate sums to maximum rank displacement, checks 36 exact first/second factorial-moment identities for corner-band events, and tests 25 pinned-arc remainder-permutation cases. Expected terminal line: `VERIFY_OK permutations=46232 factorial_moment_checks=36 conditional_remainder_checks=25`.

The calculations validate finite identities, not an asymptotic joint limit. The proof in `RESULT.md` establishes the infinite assertion using factorial moments, the independent inversion-digit central limit theorem, and a uniform conditional perturbation bound. No external certification or independent audit has been conducted.
