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
# Reproducibility and verification

Execute `python3 verify.py` with Python 3 and no external modules. The script checks the quartic Sylvester determinant identity, six partial derivatives, all 21 Buchberger pair reductions for the proposed Gröbner generators, the resultant leading-ideal Hilbert numerator and the exact affine normal form in characteristic two. Its expected final line contains `GF2 Hilbert numerator 1-6t^3+6t^4-t^6`.

The proof separately establishes the global Segre reduced support, the embedded quadric, the square-zero ideal and the conormal splitting; these geometric claims are not consequences of testing a finite number of field elements. No external independent review or validation is asserted. Potential earlier equivalent descriptions of the modular singular scheme remain a literature risk.
