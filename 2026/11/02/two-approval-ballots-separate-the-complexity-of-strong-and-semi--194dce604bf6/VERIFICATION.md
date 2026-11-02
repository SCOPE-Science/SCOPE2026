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

Execute `python3 verify.py` in the directory containing this file. The checker uses Python 3 standard library only and performs exact integer arithmetic. Its expected output is:

```text
PASS exhaustive_profiles=67028 independently_checked_committees=4822 cubic_cases=3
```

The reported exhaustive profiles range over labeled voters, nonempty singleton/pair ballots, up to five candidates and four voters. Every admissible committee size is checked for the component-maximum identity. Direct coalition enumeration is limited to the first 25 profiles at each size. Tests on the complete graph \(K_4\) and three-dimensional cube \(Q_3\) compare actual SSJR membership against vertex-cover membership for every relevant committee.

The unbounded proof consists of the two-approval forced-star lemma, a one-vertex hitting property per component, and the standard cubic-graph vertex-cover reduction. Finite test success alone does not establish these results. Unindexed prior publication is possible; independent audit has not been performed.
