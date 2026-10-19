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

A separate exhaustive finite-enumeration implementation `attractor_certificate.py` forms a bit mask of every occurrence of every nonempty *distinct factor* of each test word, with all intervals represented as zero-based inclusive position sets. It exhaustively tries one occurrence of each of the \(q\) letters, checks the exact attractor definition against the claimed canonical forbidden condition, and sums accepted sets to check the formula. No algebraic criterion is used inside the direct substring-factor test.

The replayed check passed: `ALL_PERIODIC_ATTRACTOR_CHECKS_PASSED instances 108 candidate_sets 117132`. It comprises every \(q\) from \(2\) to \(6\) and every \(k\) from \(1\) to \(4\), each \(0\le r<q\), plus \(q=3,4\) for \(5\le k\le8\). It includes all boundary cases \(k=1\), \(r=0\), \(r=q-1\). The explicit proof in `RESULT.md` covers all positive integers and does not infer the infinite claim from these checks.

Run `python3 attractor_certificate.py` with Python 3. No external packages required. Scientific scope is limited to injective periodic blocks. An independent audit has not been performed.
