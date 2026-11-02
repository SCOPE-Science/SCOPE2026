---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For x length n, exactly t(x) first symbols of noninitial runs are deleted; y is subsequence, t(y)<=t(x), so |y|+t(y)<=n. Conversely each y with m+t(y)<=n is realized by duplicating the first symbol of every noninitial output run; append alternating singleton runs whose first symbol is deleted to pad to any n, possible for q>=2. Distinct channel outputs bound a zero-error code from above and one preimage for each attains the count. Counting output words by transitions yields the GF and characteristic-root capacity (including q=2 and n=1). Independent exhaustive direct input map for q=2 n<=11, q=3 n<=7, q=4 n<=5 matched every binomial count and allowed output condition; all n follow from explicit construction.

## originality

PASS

Chen–Milenkovic–Ribeiro–Sima 2026 define exactly the original-input contextual deletion model and develop capacity bounds for the extremal p=1 channel, with numerical Table I restricted to k=2,..,8. The threshold k=1 has a different simple exact output criterion, absent from their inspected theorem/table; the binary golden-ratio capacity matches a previously known baseline restricted-word rate at k=2, not an exact threshold-one capacity theorem. Con–Ribeiro 2025 covers different input-correlated synchronization error models. Originality is for exact finite-n output range, optimum and q-ary extension, not the Fibonacci recurrence as a method.

## value

PASS

Exact capacity and optimal all-blocklength code size for a natural deterministic boundary case of a current contextual nanopore deletion model is a meaningful extremal classification. The elementary proof is independently useful and not an arbitrary small length sample; it supplies explicit preimages and covers arbitrary alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
