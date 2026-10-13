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
# Verification of folded-hypercube average mixing

The attached `verify.py` uses only the Python standard library. Execute `python3 verify.py` from a directory containing `verify.py`.

For each dimension \(3\le d\le9\), it builds the folded cube as the Cayley graph of a group with \(2^{d-1}\) elements and its \(d\) canonical generators. It checks each adjacency eigenvector independently at every vertex, constructs each spectral projector using integer Walsh sums, forms the complete Cesàro average-mixing first row from projector Schur squares, and Fourier-transforms that row with exact rational arithmetic. Every computed multiplier is compared with the formula, along with the full nullity and the smallest strictly positive eigenvalue.

Observed exact output:

```
d=3 vertices=4 nullity=0 exact_modes=4
d=4 vertices=8 nullity=0 exact_modes=8
d=5 vertices=16 nullity=0 exact_modes=16
d=6 vertices=32 nullity=1 exact_modes=32
d=7 vertices=64 nullity=0 exact_modes=64
d=8 vertices=128 nullity=0 exact_modes=128
d=9 vertices=256 nullity=0 exact_modes=256
VERIFY_OK dimensions=3..9 adjacency_tests=87376 eigenmodes=508
```

**Scope and limits.** These are finite exact tests of \(87{,}376\) adjacency eigenvector–vertex identities and \(508\) complete spectral multipliers; they are not an exhaustive computation of every dimension, and the absence of a failing finite case would not prove the theorem. The all-dimensional claim is established separately by orthogonal Fourier decomposition and an exact parity-binomial identity in RESULT.md. Independent external audit has not been performed.
