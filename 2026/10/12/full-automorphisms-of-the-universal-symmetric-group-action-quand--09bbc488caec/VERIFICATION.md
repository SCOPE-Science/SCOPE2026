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

# Reproducibility and limits

The complete proof in `RESULT.md` handles every integer \(n\ge3\). To reproduce the finite consistency tests, run `python3 verify.py` with a standard Python installation; no external packages or network are needed.

The verifier constructs permutations and group composition independently of symbolic formulas, computes all symmetric-group conjugacy classes and the centers of their centralizers in ranks three and four, enumerates every family of independently chosen central elements, transports each family by conjugation, tests transport consistency and checks the exact condition for preservation of the quandle operation for every group-label pair. Additional explicit natural-action checks confirm the two sides on element coordinates. It prints the kernel and outer index for ranks three through six by an independent partition-product calculation and ends with `VERIFY_OK`.

Observed output:

```
n=3 partitions=3 |K|=6 |Aut|=36 outer_index=1
n=4 partitions=5 |K|=96 |Aut|=2304 outer_index=8
n=5 partitions=7 |K|=2880 |Aut|=345600 outer_index=48
n=6 partitions=11 |K|=1658880 |Aut|=1194393600 outer_index=27648
VERIFY_OK
```

The checks at ranks five and six enumerate integer partitions but **not** all quandle automorphisms. At ranks three and four the script enumerates fiberwise parameters, not all permutations of the full underlying quandle set. The general completeness and non-inner threshold are established algebraically, not computationally. This is a self-review; no independent mathematical audit or external certification is claimed.
