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

The proof is symbolic for every \(0<p<1\) and every integer \(d\ge1\). The critical steps are:

1. Substitute the four displayed eigenfunctions into the exact \(4\times4\) probabilistic Laplacian and normalize them in the reversible measure.
2. Apply spectral resolution to the normalized Kronecker sum to obtain the independent additive convolution at the corner.
3. Parametrize each one-coordinate spectral value by two signs, giving at most \((d+1)^2\) sums and proving distinctness for irrational \(p\).
4. Identify the cyclic subspace with the span of nonzero spectral projections of the corner state; the rank-one oracle preserves this span.
5. Check that the zero spectral weight equals \(1/\operatorname{vol}(G_d)\), so the normalized zero projection is the constant initial state.

The included `verify.py` uses only the Python standard library and exact `Fraction` arithmetic. Running

```text
python3 verify.py
```

returns `VERIFY_OK`. It checks the matrix eigenpairs, corner weights, product law, moments, support counts and the source's four \(d=5\) parameter examples. These finite computations are consistency checks only; they do not certify the infinite quantified statement by enumeration.
