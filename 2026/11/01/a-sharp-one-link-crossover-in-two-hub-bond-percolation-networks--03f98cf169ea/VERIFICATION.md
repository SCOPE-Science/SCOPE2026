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

# Mathematical verification

Run `python verify.py` with Python 3 and its standard library from the extracted directory. The run produced:

```
VERIFY_OK assertions= 45695
```

The code enumerates all retained-edge subsets for each candidate new link on every double-star with leaf classes \(1\) through \(4\), at four rational transmissibilities. For each subset it independently computes the sum of squared component sizes using a disjoint-set algorithm; it compares this to the analytic percolation gain formulas with exact `Fraction` equality. It also evaluates the analytic candidate-dominance identities on a broader integer/rational grid through leaf class size \(30\).

The exhaustive finite checks do not establish a statement for arbitrary \(a,b,p\). The proof in `RESULT.md` supplies that universal justification through an exact cycle-gain identity, strict comparisons, and a Bernstein-basis sign-variation certificate. The verification does not address empirical SIR model validity, independent human audit, or completeness of literature searches.
