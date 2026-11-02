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

# Verification of the directed-torus solid-metric dimension formula

The mathematical proof is self-contained in `RESULT.md`. Its critical steps are the ordered-pair equivalence, the four-case directed-distance lower-bound calculation, the expansion lemma, and the explicit expanding landmark sets in the two parameter regimes.

## Direct original-definition check

Run `python verify.py`. The script uses the directed distance
\(d((a,b),(i,j))=((i-a)\bmod m)+((j-b)\bmod n)\) and checks every distinct ordered pair of vertices against the constructed landmarks. It covers 83 pairs \((m,n)\) with \(3\le m\le9\), and separately checks row coverage, interval expansion, and exact cardinalities. Observed output:

```
DIRECT_ORDERED_PAIRS_OK 83 parameter_pairs
INTERVAL_EXPANSION_OK 83 parameter_pairs
EXACT_SIZES_OK 83 parameter_pairs
VERIFY_OK
```

## Independent minimum-cardinality spot checks

With NumPy and SciPy installed, run `python verify_milp.py`. This constructs a separate integer-programming problem, with a binary variable for every possible landmark and a covering inequality for every distinct ordered vertex pair. Ten exact optimum calculations were completed for \((m,n)=(3,3),(3,4),(3,6),(3,8),(4,4),(4,7),(4,9),(5,5),(5,8),(6,6)\), matching the formula in every case. Observed final line: `MILP_VERIFY_OK 10`.

The integer-programming checks are finite, and are not asserted to prove the infinite theorem. The proof does not depend on third-party computation. No independent external mathematical audit has been performed.
