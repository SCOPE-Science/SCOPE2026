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

The bundled checker performs a direct finite test of the defining parity axiom rather than merely re-evaluating the closed formula.

For each \(1\le n\le6\), it generates every set partition of \([n]\) as a restricted-growth string. For each partition it enumerates every orientation of every cross-block vertex pair. It then checks every choice of two vertices in one block and two vertices in another and rejects an orientation whenever the four directed edges have odd parity.

For every partition with \(k\) blocks, the brute-force accepted count is compared with
\[
2^{(k-1)n-\binom{k}{2}}.
\]
The checker then sums over partitions and compares the totals with the Stirling formula. It separately verifies the equivalent \(j=n-k\) layer formula and computes the Stirling transform for tuples with repeated coordinates.

Replay command:

`python3 artifacts/verify.py`

Observed output:

```
direct_a_n_1_to_6 [1, 3, 21, 313, 9585, 591841]
formula_a_n_0_to_10 [1, 1, 3, 21, 313, 9585, 591841, 72906689, 17809866625, 8598208478977, 8188495841984001]
all_tuple_b_n_0_to_8 [1, 1, 4, 31, 461, 13286, 757945, 86793311, 20019300954]
VERIFY_OK
```

This finite computation checks the local parity-to-count conversion and the global summation independently on all labeled partitions through six points. The proof in `RESULT.md` establishes the formulas for all \(n\).
