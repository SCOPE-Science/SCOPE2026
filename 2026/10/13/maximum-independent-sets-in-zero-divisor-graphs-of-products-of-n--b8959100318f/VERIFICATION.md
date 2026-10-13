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

The standalone `verify.py` artifact was read from its actual packaged path and replayed.

For products with two through five factors, it forms all nonempty proper supports, pairs each support with its complement, and exhaustively enumerates every one-side-per-pair selection. It rejects selections containing disjoint supports, computes the maximum weight among the surviving intersecting families, and checks both
\[
\alpha=\sum_{\{S,S^c\}}\max\{w(S),w(S^c)\}
\]
and the predicted count
\[
2^\tau.
\]

The tested parameter tuples include unequal-weight, tied-weight, and multiple-tie cases. In rank three it additionally checks agreement with the published formula
\[
n_1n_2+n_1n_3+\max\{n_1,n_2n_3\}.
\]

The equivalent absolute-difference formula is checked independently for all test tuples, and larger six- and seven-factor tuples are checked algebraically without exhaustive family enumeration.

Exact replay output:

```text
q= (3, 3) alpha= 2 ties= 1 max_families= 2
q= (3, 5) alpha= 4 ties= 0 max_families= 1
q= (3, 3, 3) alpha= 12 ties= 0 max_families= 1
q= (7, 5, 5) alpha= 64 ties= 0 max_families= 1
q= (3, 4, 7) alpha= 36 ties= 1 max_families= 2
q= (3, 3, 3, 3) alpha= 44 ties= 3 max_families= 8
q= (3, 3, 4, 4) alpha= 81 ties= 2 max_families= 4
q= (3, 4, 5, 7) alpha= 234 ties= 1 max_families= 2
q= (3, 3, 3, 3, 3) alpha= 160 ties= 0 max_families= 1
q= (3, 3, 3, 4, 5) alpha= 368 ties= 0 max_families= 1
large q= (3, 3, 3, 3, 3, 3) alpha= 512 ties= 10 max_families= 1024
large q= (3, 4, 5, 7, 8, 9) alpha= 21226 ties= 0 max_families= 1
large q= (5, 5, 5, 5, 5, 5, 5) alpha= 59136 ties= 0 max_families= 1
VERIFY_OK
```

Finite enumeration is corroborative only. The arbitrary-rank conclusion is proved by the complementary-pair upper bound and the positive-logarithm intersection argument.
