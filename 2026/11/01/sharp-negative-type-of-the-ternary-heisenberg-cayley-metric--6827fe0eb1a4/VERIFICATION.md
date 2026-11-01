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

# Verification of the Heisenberg distance-spectrum theorem

The distributed `CHECK.py` was executed using Python 3, SymPy and NumPy on the exact package bytes. It reported:

```
PASS: shell census; all Fourier blocks and multiplicities; rational endpoint bounds; 27-point numerical cross-check
pstar = 0.677622399811659; endpoint squared-Euclidean embedding rank = 22
```

The finite enumeration covers all 27 group elements and all 729 ordered pairs, establishes the shell counts, and matches direct power-distance matrices with the character/representation spectra. Symbolic identities are checked before floating-point tests. Rational endpoint inequalities use exact integer-power comparisons, with no dependence on approximate exponentiation for those inequalities. In particular the controlling eigenvalue is strictly negative at exponent \(2/3\), strictly positive at \(7/10\), and the other branches are strictly negative throughout the enclosed endpoint interval.

The analytic argument for the unique root and the interval property is in `RESULT.md`. Finite experiments, decimal root approximations and a successful script run do not constitute independent mathematical audit, and no numerical result is used as an infinite-exponent proof. Prior work is assessed only to the extent of the specified inspected sources and searches.
