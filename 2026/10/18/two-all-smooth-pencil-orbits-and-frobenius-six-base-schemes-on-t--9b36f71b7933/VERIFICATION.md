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

# Reproducibility and limits

Run `python3 artifacts/verify.py` and compare its full standard output byte-for-byte to `artifacts/expected.json`. It uses only the Python 3 standard library. Run `python3 artifacts/verify_symbolic.py` and compare its output to `artifacts/symbolic_expected.json`; this requires SymPy. Both comparisons passed before packaging using these exact files.

The first verifier performs 127 exact GF(2) rank tests for the 15-dimensional degree-four Jacobian map, checks cubic singularities independently over fields with 2, 4 and 8 elements, constructs all 12 anticanonical pencils and all 12 coordinate/Cremona automorphisms, proves two six-element orbits, checks the irreducible degree-six residue fields by polynomial arithmetic, and substitutes each algebraic point directly into its two defining cubics. Rational basepoint absence is separately checked at all 13 rational points of the blow-up (four ordinary plane points and three points on each exceptional line).

The second verifier independently runs algebraic-closure smoothness Gröbner tests on all three affine projective charts of each cubic, enumerates every qualifying pencil, and computes full elimination/resultants for the two representative pencils. Each resultant has the irreducible sextic factor and one linear factor associated with a blown-up center.

Completeness rests on the finite coefficient space and the mathematical regular-sequence criterion; the extension-field check alone is not substituted for that argument. Reducedness of the six-point base follows because its six distinct points exhaust the anticanonical intersection number six. Verification is same-model only; no independent audit or claim of computational independence beyond the stated separately implemented exact methods is made.
