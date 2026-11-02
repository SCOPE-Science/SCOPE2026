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

The statement concerns exactly the two quantified confluence laws (D) and (U) on the fixed labelled order \(A\oplus B\oplus C\), with all levels nonempty and \(R\) an equivalence relation. The proof in RESULT.md establishes a disjoint five-type classification and counts every type. Its key witness steps use minimality of \(A\), maximality of \(C\), and the fact that two different points within \(B\) are incomparable.

Run the standalone standard-library verifier with `python3 checker.py`. The executed version reported:

```
CASES 56
TOTAL_LABELLED_EQUIVALENCES_EXAMINED 102487
TOTAL_VALID 4113
FORMULA 1 1 1 4
FORMULA 1 2 1 7
FORMULA 2 2 2 15
FORMULA 2 3 2 31
FORMULA 3 3 3 142
ALL_CHECKS_OK
```

The verifier enumerates all set partitions for each positive \((a,b,c)\) with \(3\le a+b+c\le8\), tests both existential quantifiers literally, tests the structural classification independently, checks all five type counts, and compares their sum to the formula. There are no random seeds, hidden inputs, internet dependencies, or unreported precomputed tables.

No finite census is presented as an infinite theorem by itself. The infinite-size quantification over arbitrary positive layer sizes rests on the explicit proof. Historical priority and additional modal completeness properties are not independently verified.
