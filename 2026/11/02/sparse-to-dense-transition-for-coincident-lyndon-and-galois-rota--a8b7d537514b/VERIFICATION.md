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

An indexed circular word containing 00 has lexicographically minimal rotation starting 00, while at alternating position 2 a 01 zero-start rotation is smaller, so coincidence requires strictly positive zero gaps. For positive gaps a<b, the first mismatch is at one-based position a+2; the shorter gap wins both lex/alternating orders precisely when a is odd. With a unique minimum odd gap the common chosen rotation is forced. For k=2 count unequal gap pairs with odd smaller gap to obtain z^5/((1−z)(1−z^4)); for k=3 tied odd minima occur as (a,a,b) and still coincide, yielding z^7/((1−z)^2(1−z^6)). For fixed k≥2, anchoring a unique positive odd minimum gap gives generating function z^(3k−1)/((1−z)^(k−1)(1−z^(2k))); tied minima are O_k(n^(k−2)), yielding C_{n,k}=n^(k−1)/(2k!)+O(n^(k−2)), half the standard primitive necklace count. At k/n→α>0, cyclic 00 avoidance is ≤(n/(n−k)) exp(−k²/n) fraction of indexed words and nonprimitive words are exponentially negligible, giving exponential coincidence decay (zero when k>n/2). Independently enumerated ordinary and alternating minimum full rotation classes for 2≤n≤15,k≤3. Exact counts only k≤3; for k≥4 only leading profile.

## originality

PASS

Best-of-knowledge originality PASS for the precise stated claim, not a priority certificate. Coincidence of canonical minimum rotations can be recast as a condition on circular compositions of the runs of ones: the shortest positive gap is odd and unique (sufficient), while even/zero minimum is forbidden; for k=3 odd minimum is also sufficient even in ties. The source is not merely counting ordinary Lyndon words or all generalized Lyndon words. Hendrian–Köppl–Yoshinaka–Shinohara 2024 develop Galois-word detection, factorization, and minimum-rotation algorithms; Dolce–Restivo–Reutenauer 2019 provide generalized Lyndon factorization. Algorithms computing the two minima do not supply the fixed-content coincidence distribution, even though an implementation could enumerate small n. Principal residual risk: Specialized unpublished enumeration of coincidence of generalized Lyndon minima might exist.

## value

PASS

The intersection of ordinary Lyndon and alternating Galois canonical representatives is a natural combinatorial/string-normalization statistic. Its exact small-content enumerations and sharp fixed-sparse versus positive-density phase transition make a useful complete asymptotic classification in two regimes, not a restatement of algorithms for computing either representative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
