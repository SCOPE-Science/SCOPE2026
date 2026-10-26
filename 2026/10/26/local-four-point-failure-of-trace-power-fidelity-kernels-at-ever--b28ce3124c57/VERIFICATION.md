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

# Verification of the explicit four-state kernel

## Reproducible checks
Run `python verify.py` with Python 3.10 or later; no third-party packages are required. The script reports 270 exact rational checks of the common-denominator identity, 400 direct complex 2-by-2 matrix-product comparisons against the spectral formula, and checks of dimension scaling and the quartic coefficient. The precise count is stated only for tests actually executed.

## Analytic certificate
The strict result does not depend on sample meshes: the exact resolvent identity is
\[
H(s)=\frac{8q^4s(s-(1-q^2))}{(s+1-q^2)(s+(1+q)^2)(s+(1-q)^2)((s+1)^2-q^2(2-q^2))}.
\]
The two sets defining \(H\) have identical products, so \(\int_0^\infty H(s)ds=0\). Its sign changes once, at \(s=1-q^2\). Multiplication by the strictly increasing power \(s^r\) makes the integral positive for \(r>0\) in the convergence range; the fractional-power representation then forces the alternating eigenvalue to be strictly negative for \(0<r<1\). The quartic coefficient follows from an ordinary binomial expansion.

## Unproved limits
No global optimum over all density quadruples is asserted. The finite program does not establish originality, and no independent validation has been performed.
