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

The analytic proof is the primary verification. Its critical steps are:

1. Parseval applied to the square of the four-term polynomial gives the exact seven self-convolution fibers.
2. Phase alignment gives an upper bound depending only on the four coefficient moduli.
3. Grouping the two outer and two inner squared moduli reduces the bound to a one-variable function \(h(r)\).
4. The derivative identity
\[
h'(r)=-\frac{2r(r^3+3r^2-3r-3)}{(1+r^2)^3}
\]
shows that the unique positive root \(\rho\) is the global maximizer.
5. Equality in every modulus inequality forces the pattern \((1,\rho,\rho,1)\); equality in every collision triangle inequality forces affine-linear phases.

`verify.py` performs an independent numerical replay of the exact moment formula, the cubic root, the algebraic polynomial for the sharp value, the extremizer, and randomized coefficient vectors. Random tests are only corroborative and do not establish the universal inequality.

Unproved limits: no assertion is made for finite cyclic sampling, arbitrary four-point spectra, or exponents other than \(4\). Literature searches cannot exclude an equivalent older result hidden under substantially different terminology.
