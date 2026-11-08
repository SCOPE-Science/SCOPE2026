---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact identity a_(N-1)=sum_(k>=0)(2k-1)!! C(N,2k+1) yields a_(N-1)/N=sum c_k C(N-1,2k), c_k=(2k-1)!!/(2k+1). For 27|N the only nonintegral c_k are k=1,4, and the two binomial coefficients are 1 mod9; their combination (1+35)/3=12 is zero mod3. All other k>=2 terms have v3>=1 by finite base bound and exponential tail estimate. So a_(N-1)/N is a 3-adic unit. The established involution periodicity mod3^r and full vector of a_0..a_26 mod27 now reduce all n to three exceptional n mod9 classes: 4 -> valuation2, 6 -> valuation1, 8 -> v3(n+1), others zero. Independent integer recurrence mod729 confirmed 4000 indices; this is corroboration, not a proof of infinite period.

## originality

PASS

Best-of-knowledge originality for the exact stated theorem only; public primary comparison and published-record semantic searches found related methods but no prior statement implying the complete final claim. This is not proof of worldwide priority. Finite original table and OEIS A000085 individual sequence do not state corrected all-index v3

## value

PASS

The original paper specifically left odd-prime valuations of these partial sums as a question and printed a conflicting mod3 pattern. An all-index valuation law with a unique unbounded branch repairs that natural arithmetic gap; not an arbitrary small table extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
