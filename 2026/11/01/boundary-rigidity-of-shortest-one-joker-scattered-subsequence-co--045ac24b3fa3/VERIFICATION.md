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

The theorem is proved for every integer \(q\ge2\) and \(k\ge1\) using (1) fixed-symbol multiplicity, (2) two-run targets that force identical prefix symbol counts, (3) an absent-word obstruction that forces universality of both ordinary sides, and (4) the greedy arch lemma for minimum-length ordinary universal words.

The standalone `verify.py` checks the theorem by exhaustive enumeration of all balanced hosts at minimum length for \(q=2\) and \(k\le7\), \(q=3\) and \(k\le4\), \(q=4\) and \(k\le3\), and \(q\in\{5,6\}\) and \(k\le2\). The exact comparison examined 61,609 partial hosts across 18 parameter pairs and found 5,213 matches to the predicted class. Greedy wildcard-subsequence matching was also compared against a separate dynamic-programming matcher for 1,625,493 input pairs, with exact agreement.

Command: `python3 verify.py`.

```text
VERIFY_OK parameter_cases=18 exhaustive_hosts=61609 satisfying_hosts=5213 matcher_agreement_cases=1625493
```

The empirical range is finite. The proof, rather than the enumeration, supplies the all-length conclusion; independent scientific audit has not been performed.
