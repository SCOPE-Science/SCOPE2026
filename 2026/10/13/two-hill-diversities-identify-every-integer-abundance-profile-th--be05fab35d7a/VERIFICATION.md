---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At each fixed, known positive integer census N, unlabeled profiles with positive species counts are the integer partitions of N. Shannon entropy is log(N)-log(Q)/N for Q=product n_i^(n_i) and population Simpson concentration is M2/N^2 with M2=sum n_i^2. Thus their equality is exactly equality of Q and M2; the Hill-number transformations are injective. An independent enumeration chose multiplicities c_j in descending part size j, between zero and the remaining census divided by j; the multiplicity of 1 is the final remainder. Every admissible profile has exactly one such choice sequence. The distinct implementation keyed Q by all prime valuations sum_j j*c_j*v_p(j), equivalent by unique prime factorization, and optionally added S=sum_j c_j. It checked 28,628 profiles over N=1 through 30, with partition counts matching the external p(N) table. It found no pair collisions through 23; exactly two at 24: (1^6,3^2,4^3) versus (2^9,6), with Q=12230590464, M2=72 and richness 11/10, and (1^4,4^2,6^2) versus (2^2,3^4,8), with Q=142657607172096, M2=108 and richness 8/7. There were no triple collisions through 29 and exactly one at 30: (1,4,4,4,4,4,9) versus (2,2,3,3,6,6,8), with S=7, Q=2^40*3^18 and M2=162. Replay: /workspace/branches/a268cca5-88ac-449b-95af-14789a6aeba8/audit_hill_partition_enum.py; captured census in audit_hill_partition_enum.txt in the same directory. The bundled verifier was inspected but not executed. The result is exact injectivity for each fixed N, not across different totals (scaling all counts preserves the diversities), and not a statement about approximate or estimated values.

## originality

PASS

The closest published scholarly result counts marginal entropy and Gini–Simpson values on the same integer partitions; the closest indexed findings concern rarefaction with Simpson or ranking reversals. Their actual conclusions differ from the exact joint equalities, both sharp cutoffs, and the complete first collision layers. Counts and definitions for the individual statistics are established prior work; lack of a hit alone is not the originality basis.

## value

PASS

The domain and invariant are canonical: integer census partitions and Hill orders 1 and 2, with order 0 as the natural additional observable. The exact first loss of joint information, all first failures, and the amount by which adding richness delays that failure give a concrete benchmark separating summaries that are lossless at small fixed totals from ones that are not. The answer is not obtainable from the published marginal counts alone and is not a randomly chosen small slice. Its significance is exact finite identifiability, not ecological inference at nonzero measurement error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
