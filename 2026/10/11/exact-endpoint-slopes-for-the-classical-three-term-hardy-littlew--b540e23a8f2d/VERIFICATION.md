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

`verify_endpoint_slopes.py` is a standalone exact-arithmetic checker. It verifies the Fourier convolution coefficients for \(G_\pm^2\), verifies the reduced reflected-root power sums used in the two derivative formulas, isolates the two algebraic roots by rational bisection, and certifies the signs using the positive expansion
\[
\log\frac{b}{a}=2\sum_{j\ge0}\frac{u^{2j+1}}{2j+1},
\qquad
u=\frac{b-a}{b+a},
\]
with an explicit rational geometric tail bound. No floating-point computation is used for the inequalities.

The exact certificate proves \(\Delta'(2)>0\) and \(\Delta'(4)<0\). Decimal values printed by the checker are only renderings of rational enclosures. The checker does not prove the already known global interior inequality \(\Delta(p)>0\) for every \(2<p<4\); that theorem is cited as prior work rather than claimed here.
