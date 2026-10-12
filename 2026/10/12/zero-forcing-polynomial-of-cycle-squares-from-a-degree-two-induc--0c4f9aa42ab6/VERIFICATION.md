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

# Exact reproduction and limits

Run `python3 verify.py` with Python 3.8 or later and no third-party packages. The exact integer-polynomial certificate uses transition states `(a,b,c,d)` and appends the bit `e` if and only if the central bit `c` does not have three or more selected neighbors among `a,b,d,e`. Dynamic path counting constructs the polynomial trace at lengths 1 through 16. Polynomial Newton identities reconstruct **all** coefficients of `det(I-uT)` and compare them exactly, including the coefficientwise zero terms, with the seven-term polynomial stated in `RESULT.md`.

The same executable independently builds the cycle-square adjacency rule at every vertex and simulates ordinary forcing until no legal step remains. It compares each outcome with the induced-degree criterion and with the trace enumerator for all `2^n` subsets at each labeled order `n=7,...,14`, totaling **32640** subsets. It checks the coefficient for minimum zero forcing size and the maximum failed-set size independently at each order. The executed output was:

```
VERIFY_OK transfer_states=16 determinant_degree_u=8 traced_powers=16 cycle_orders=7..14 exhaustive_subsets=32640 coefficient_and_forcing_checks=passed
```

The unrestricted theorem is supplied by the combinatorial equivalence plus the exact fixed-size transfer identity and formal trace/determinant calculation, **not** by extrapolation from the eight finite tested graphs. No external mathematical validation has been performed. The checker does not test arbitrary graph families outside the specified cycle squares, and it does not settle originality.
