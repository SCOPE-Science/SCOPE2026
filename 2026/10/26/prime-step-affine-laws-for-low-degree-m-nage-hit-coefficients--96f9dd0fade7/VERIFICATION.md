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
# Verification details

Execute `python3 verify.py` using Python 3 (standard library only). The checker constructs coefficients independently from the original integer hit-polynomial sum, computes the finite residue formulas from the claimed theorem, checks all degrees \(0\le r<p\) for seven primes through \(17\), all \(1\le n\le24\), and all \(0\le k\le4\), for 6,960 coefficient comparisons. It also checks the three-term congruence, degree-three counterexample \(p=3,n=1\), the special \(p=2,r=2\) case, and initial degree-two values from OEIS A000033.

This is a finite reproducibility check, **not** a computational proof of statements for infinitely many \(n\) or primes. The universal argument is the factorial truncation and two-binomial-term identity in RESULT.md. Scientific priority has been checked against the named accessible sources but is not guaranteed; independent verification has not been conducted.
