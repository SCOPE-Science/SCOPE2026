---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The k-step derivative map is bijective on length-n q-ary words and a literal length-k tandem duplication inserts exactly k zeros in the derivative; irreducible trunk and zero-signature composition are invariant root coordinates. A common one-duplication descendant between equal-weight signatures occurs exactly at L1 distance two, equivalent to moving one unit between zero runs. For n<=3k every fiber has signature weight at most one, unless weight two with the zero trunk (single signature); thus both one-error and unlimited optima choose one word per root. At n=3k+1 the only trunk lengths are 2k+1 (weight0), k+1 (weight1 clique) or 1 (weight2). A nonzero length-one trunk has three signatures (2,0),(1,1),(0,2) forming P3, whose unique maximum independent set is its two endpoints; each of the q-1 roots contributes an extra codeword per q^k prefix. Hence first gap q^k(q-1), and the fiberwise independent-choice count yields the exact maximizer product with factor 2^((k-1)(q-1)) and factors (w+1)^(binom(k+1,w)(q-1)^w). Our independent literal duplication-output enumerator, not the uploaded verifier log, rebuilt fiber conflict graphs for (q,k,n)=(2,2,7),(3,2,7),(2,3,10), verifying maxima (84,80),(1719,1701),(776,768); the binary q2,k2 product gives 2176782336. The all-q,k assertion rests on the complete fiber-type proof, not finite tests.

## originality

PASS

Jain--Farnoud--Schwartz--Bruck 2016 already prove the derivative insertion rule, root classification and optimal unrestricted-error code cardinality and their Theorem 20 relates bounded errors to constant-weight L1 signature codes. These are strong foundations and must not be claimed new. Lenz--Wachter-Zeh--Yaakobi give finite bounds, Kovačević--Tan asymptotic behavior, and later small constant-weight work handles local cases. None of the inspected exact cited theorems states the across-all-parameter first equality-to-gap boundary at 3k+1 or counts every labeled optimum at that boundary. The new result is a natural complete first-onset census, not an independent discovery of trunk metrics.

## value

PASS

The minimal blocklength where one-error correction strictly outperforms unlimited-error correction is a natural finite-blocklength coding boundary. An explicit sharp threshold for every alphabet and duplication length, with exact equality-case count, informs channel-design tradeoffs and reveals when the P3 signature fiber first appears. The result is not an arbitrary small code table; it classifies all parameters at the first structural transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
