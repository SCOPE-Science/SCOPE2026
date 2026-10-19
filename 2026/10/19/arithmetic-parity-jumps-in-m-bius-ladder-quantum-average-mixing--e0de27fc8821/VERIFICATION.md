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
# Verification notes
The result follows from the all-order spectral and algebraic-integer proof in `RESULT.md`. The standalone exact checker `verify.py` is provided to corroborate its main identities independently of symbolic or floating-point eigensolvers.

Execute `python3 verify.py` using Python 3 and only the standard library. The checker constructs cyclotomic polynomials by exact monic integer division, forms the exact roots-of-unity representation of each \(\lambda_k=2\cos(\pi k/n)+(-1)^k\), determines all equal-energy groups for \(3\le n\le120\), and computes the Fourier-support counts from ordered pairs. This avoids tolerance-induced false coincidences. It checks that the rank is \(n+3\) for \(n\equiv3\pmod6\), \(n+2\) for \(n\equiv2\pmod4\), and \(n\) otherwise, as well as the exact index set and cross-parity group sizes.

The actual extracted-source run printed:
```
VERIFY_OK exact_cyclotomic_orders=118 graph_vertices=6..240 exceptional_orders= 49
```

This is not an exhaustive check beyond the finite range and is not an independent audit or validation. The all-parameter conclusion depends on the written norm lemma, the proof of the only opposite-parity collision types, and the Fourier counting identity. The calculation does not address weighted, magnetic, or non-Cesàro models.
