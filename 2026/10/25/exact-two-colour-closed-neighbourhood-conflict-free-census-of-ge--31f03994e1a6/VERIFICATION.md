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

The polynomial elimination argument in `RESULT.md` is valid in \(\mathbb F_2[t]/(t^n+1)\) for all \(n\ge3\) and \(1\le k<n/2\). It does not assume the modulus square-free. A full direct binary-colouring enumeration tests all \(2^{2n}\) assignments for each admissible \(k\) and \(3\le n\le8\), checking unique colours directly in every four-vertex closed neighbourhood. A separate exhaustive test takes all \(2^n\) outer words for \(3\le n\le17\) and \(k\le6\), constructs inner words using the outer equations, and checks the remaining closed neighbourhoods directly. Both implementations agree with a third calculation of \(\deg\gcd(t^n+1,h_k)\) by exact binary polynomial Euclidean division. The certificate is the human-readable mathematical proof plus the standalone, independently runnable `checker.py`; finite computations do not prove the infinite theorem by themselves.

Execute `python3 checker.py` from the extracted package directory; no external modules, network access, or extra files are required. Re-running the program tests the same finite cases but does not constitute independent mathematical review.
