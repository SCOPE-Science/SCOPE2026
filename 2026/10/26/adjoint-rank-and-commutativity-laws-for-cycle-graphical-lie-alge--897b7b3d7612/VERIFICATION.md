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

# Reproducibility and scope

The included `verify.py` is a standalone Python 3 program without third-party dependencies. Run `python3 verify.py` in a directory containing the extracted file. It constructs every tested edge-bracket matrix directly, computes ranks by modular Gaussian elimination, and separately derives the support-component formula. It also builds and multiplies the transfer matrix over integer-coefficient polynomials, checks cyclic binary-word weights independently, and checks the exact mean and variance formulas using rational arithmetic.

The executed program returned `VERIFY_OK 14 direct matrix checks, 35 symbolic transfer checks`. Direct matrices were enumerated for cycles, paths, stars, disconnected forests and a triangle-with-leaf configuration over prime fields of orders two and three. Pattern coefficient checks covered field orders two, three, four, five and nine. The nonprime-order checks use the proven support-independence to count multiplicities and do not purport to implement extension-field arithmetic directly. Exhaustive enumeration at finite sizes is not an infinite proof; the universal argument, characteristic-polynomial calculation and finite-dependent CLT are given in `RESULT.md`.

The same mathematical argument works in characteristic two because the edge bracket is alternating, and all kernel equations compare nonzero vertex coefficients by field division. The cyclic formulas require a simple cycle of length at least four and a distinct central basis label for each edge. Independent verification has not been performed.
