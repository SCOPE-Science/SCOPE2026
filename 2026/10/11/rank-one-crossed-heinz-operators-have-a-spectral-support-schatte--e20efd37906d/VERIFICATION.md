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
# Verification of the rank-one crossed-Heinz theorem

The proof is analytic for every bounded positive Hilbert-space operator and rank-one positive input. It uses (i) a rank-two exterior-power singular-value identity; (ii) spectral-measure covariance and the strict monotonicity of positive power functions; (iii) the equality criterion for Cauchy–Schwarz in an \(L^2\) spectral space; and (iv) strict monotonicity of Schatten \(p\)-norms for rank-two operators.

Running `python3 verify_rank_one_heinz.py` checks the independently encoded exact rational example \(A=\operatorname{diag}(1,16,81)\), \(B=uu^*\), \(t=1/4\), and checks two-point/equal-power boundaries. Expected output:

```
RANK_ONE_CROSSED_HEINZ_EXACT_WITNESS_OK
RANK_ONE_CROSSED_HEINZ_BOUNDARY_IDENTITIES_OK
```

The code is finite and does **not** independently verify the infinite-dimensional theorem, full originality, or source coverage. No outside audit has taken place.
