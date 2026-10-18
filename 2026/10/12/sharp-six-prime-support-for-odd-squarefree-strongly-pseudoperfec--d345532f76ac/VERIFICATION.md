---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For k<=4, the greatest odd squarefree abundance product is (4/3)(6/5)(8/7)(12/11)=768/385<2. For k=5, monotone prime factors and exact product bounds force 3,5,7 and q∈{11,13,17,19}; r is bounded by floor(32(q+1)/(3q-32)) = 384,64,30,25. Thus exactly 87 prime pairs are possible. Each has 16 complementary divisor pairs whose chosen/omitted sum reaches 2N iff a subset of their 16 pair weights sums to Delta=sigma(N)-2N. An independent meet-in-the-middle enumeration rebuilt all 87 candidate sets from prime enumeration and proved Delta unattainable in every case. The explicit six-prime witness 937365 has sigma=1935360 and five distinct omitted complementary pairs totaling 60630, leaving 2N=1874730. Finite certificate is exhaustive only due to the analytic reduction; source cases.csv/checker verified as actual package evidence.

## originality

PASS

The claimed incremental conclusion was compared by statement and implication against the most relevant primary work and indexed mathematical results. Known component statements are explicitly credited and are not themselves asserted as new. This is a best-of-knowledge priority judgment with the listed full-text and alias risks.

## value

PASS

The minimum distinct-prime support of odd squarefree strongly pseudoperfect numbers is a natural structural boundary for an actively studied divisor-sum class. Identifying the exact sharp threshold six, with a complete bounded arithmetic sieve and an existing attained witness, is an independently useful classification; it is not merely discovering the already-known example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
