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

# Reproducibility

Run `python3 verify.py` using Python 3 and its standard library. The program enumerates direct circular words, groups them by their complete adjacent-pair profiles, tests each word's primitive period without any graph-theoretic assumption, and separately constructs an Euler tour followed by sorted first-return excursions for each profile. The constructed output is checked for exact profile equality and predicted primitive status. Finally, the number of exceptional profiles at every tested parameter is matched against the closed divisor sum.

Exhaustive ranges: \(q=1\) to length \(8\), \(q=2\) to length \(11\), \(q=3\) to length \(10\), and \(q=4\) to length \(8\). The strongest individual profile counts include \(95\) ternary profiles of length \(6\), of which \(8\) are exceptional, and \(3317\) quaternary profiles of length \(8\), of which \(16\) are exceptional. The program checks all source words in each specified range; it does not infer statements at untested lengths.

The theorem for all positive alphabet sizes and lengths is established by the separately written mathematical proof. No computational assumption, randomized test, external database, specialized solver, or unprovided dependency is needed. Independent mathematical audit has not been performed.
