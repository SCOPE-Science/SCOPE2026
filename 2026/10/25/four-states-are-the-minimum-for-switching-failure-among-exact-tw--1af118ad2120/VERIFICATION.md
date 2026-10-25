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

# Reproducibility and limitations

Run `python3 verify.py` using the companion script in this package. The script requires only Python's standard library. It checks rational matrix identities for the four-state bit-shift example, exact mixing at two homogeneous steps, positivity of the perturbed kernels, and both orders of alternation through twenty time steps at seven rational values of \(\varepsilon\). It also enumerates feasible three-state rational kernels with denominator up to six and checks that their centered matrices are strict Euclidean contractions.

An actual run returned:

```
EXACT_FOUR_STATE_ALGEBRA_PASS 280 switching cases
THREE_STATE_FINITE_GRID_PASS 14 feasible rational kernels (denominator at most 6)
VERIFY_OK
```

The grid check is **not** an exhaustive proof over real entries or arbitrary time. The proof of the all-real lower-dimensional contraction is the support-overlap and compactness argument, independent of the grid. The all-time four-state identities follow from the displayed algebraic induction. Scientific priority remains subject to external review; no independent audit has been conducted.
