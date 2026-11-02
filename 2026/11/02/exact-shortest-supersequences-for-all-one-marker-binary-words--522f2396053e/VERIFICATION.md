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

# Verification

The proof in `RESULT.md` establishes the theorem for every integer \(k\ge1\) and \(r\ge1\). The code `verify_onehot.py` is an independent brute-force check that uses literal subsequence embeddings rather than the marker-interval proof as its oracle. It then separately verifies the interval criterion and coefficient-based counting predictions.

Run after extracting the embedded files:

```
python3 verify_onehot.py
```

The executed checker reported:

```
VERIFY_OK checked_hosts=227017 k_global=1..11 optimal_counts={1: 1, 2: 2, 3: 5, 4: 1, 5: 7, 6: 2, 7: 18, 8: 6, 9: 1, 10: 27, 11: 9} fixed_marker_profiles=52 integer_witness_k=1..2000
```

It enumerates all host strings of length at most \(L_k\) for \(1\le k\le11\), checks all \(k\) targets for each host, verifies the interval characterization, checks no shorter host covers, and compares the count of minimizers with the formula. It additionally enumerates all fixed-marker composition classes with \(1\le k\le8\), supported \(r\) and host length at most 19, and tests arithmetic/construction identities for \(1\le k\le2000\). These finite checks do not prove claims outside their finite ranges and do not establish novelty. Independent scientific auditing has not occurred.
