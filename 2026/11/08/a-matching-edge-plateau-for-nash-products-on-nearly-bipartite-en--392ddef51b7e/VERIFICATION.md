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

`VERIFY.py` is standalone Python 3, using only the standard library. Run `python3 VERIFY.py` to enumerate all set partitions in the tested ranges. Recorded output:

```
VERIFY_OK: 37 exact instances, 772452 unrestricted set partitions, plateau for a=4..100
```

The test checks the product, maximizing-partition count, and unique optimal coalition-size shape for the matching subgraph on \(4\le a\le10\) and \(1\le t\le\lfloor a/2\rfloor\), as well as the full hostility graph on \(4\le a\le6\), \(2\le b\le3\). The symbolic identity for the first two added edges is additionally tested for \(4\le a\le100\). Code enumeration is finite; it neither proves optimality at untested sizes nor establishes originality. The general theorem follows from the independent-set bound and convex majorization proof in `RESULT.md`.

Literature comparisons are limited by the unavailable full text of the closest foundational paper. Scientific review is same-model only; no independent validation has been performed.
