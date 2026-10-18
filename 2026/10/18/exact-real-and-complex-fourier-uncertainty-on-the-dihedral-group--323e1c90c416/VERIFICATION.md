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

# Reproduction and verification

With Python 3, run `python3 checker.py` in this directory. Only the standard library is required. The program uses exact Gaussian integer pairs (not floating point), computes all four scalar Fourier blocks and the exact determinant of the two-dimensional block, and verifies the predicted support sizes and Fourier ranks of all sixteen field-indexed witness rows. It independently computes all \(56\) three-subset images under left translations and the displayed automorphisms, obtaining three disjoint orbits of sizes \(8,32,16\). It also checks the four positions of the exact identity used in the five-point obstruction.

These calculations confirm upper witnesses and finite orbit coverage. Analytic arguments in RESULT.md establish all lower bounds for arbitrary real or complex coefficients; checking finitely many proposed amplitudes alone would not prove those bounds. There is no dependency on numerical optimization, random seeds or external data. Independent audit is not performed.
