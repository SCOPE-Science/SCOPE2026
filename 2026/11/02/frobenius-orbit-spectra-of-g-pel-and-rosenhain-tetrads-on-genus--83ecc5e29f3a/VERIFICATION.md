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

# Verification performed

`verify.py` uses only Python 3 standard library. Executed with `python3 verify.py > verification_output.txt`; the actual output is embedded and ends with `VERIFY_OK`. All 720 permutations of six elements, all 35 linear planes, all 140 affine tetrads, two independent enumerations of geometric tetrads, direct Frobenius cycle decompositions, and the stable-coset fixed-point formula were checked exhaustively. Each of the eleven tabulated spectra was compared to an explicit expected value; all weighted cycle counts and the minimal splitting-degree lcm condition were asserted.

# Limits

A finite exhaustive proof depends on the independent classical identification of the 16 Kummer nodes with genus-two two-torsion and its 60/80 tetrad affine-plane types. Reproduction is computationally exact but does not constitute a separate independent scientific audit. No claim about characteristic two, twists, or a complete literature priority search is made.
