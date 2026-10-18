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
# Reproduction record

The included `verify.py` was executed with Python 3 and SymPy. It completed successfully and printed:

```
CERTIFIED: 1512 smooth equations, ten distinct zeta polynomials, and complete Cartier stratification
```

The verifier enumerates all nonzero forms in the 14-dimensional kernel of the seven rational-point evaluations, checks all projective transformation orbits, proves geometric smoothness via unit-ideal Gröbner bases on all three standard affine charts, and calculates the Hasse–Witt matrix with the coefficient formula in `RESULT.md`. It repeats the stable-rank calculation by direct binary matrix powers and checks its equality with the degree of the Weil numerator modulo two.

For point counting it constructs finite fields of degrees 1–6 using the irreducible binary polynomials represented as integer bitmasks `3,7,11,19,37,67`, counts projective zeros exactly, and recovers the degree-twelve zeta numerator by Newton identities and the functional equation. The output gives for each of ten masks its full degree-twelve numerator, extension point counts, and matrix ranks; the embedded source is sufficient without an earlier computation or externally stored tables.

These are exact finite checks proving a finite family statement. The arithmetic calculations are not an independent mathematical audit. Complete external review and other possible descriptions of the same isogeny classes are outside the verification performed.
