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

The proof was checked directly from the defining integral. With \(p=f/\Delta_F\) and \(q=g/\Delta_G\), write
\[
D=\mu_Y-2\mu_X+A,\qquad A=\int_a^b x\frac{p^2}{q}\,dx.
\]
For a moving lower endpoint, the normalization derivatives are \(\partial_a p=h_{1X}p\) and \(\partial_a q=h_{1Y}q\); for a moving upper endpoint they are \(\partial_b p=-h_{2X}p\) and \(\partial_b q=-h_{2Y}q\). Applying Leibniz's rule to \(\mu_X\), \(\mu_Y\), and \(A\), then substituting \(A=D-\mu_Y+2\mu_X\), reproduces the two claimed formulas term by term.

The null-model check is exact: if \(X=Y\), then \(D\equiv0\) for every admissible interval. The corrected identities reduce to zero. The published equations (14) and (15) instead reduce to \(h_1(1-a)\) and \(h_2(b-1)\), which are generally nonzero.

The included `verify_endpoint_derivatives.py` is a supplementary replay. For exponential rates \(1.3\) and \(0.7\) on \((0.5,2)\), the analytic derivatives match centered finite differences to better than \(10^{-10}\). The checker does not certify the general theorem; the symbolic derivation does.

Limits: the verification assumes positive truncation masses, positive reference endpoint densities, and sufficient regularity for endpoint differentiation. It does not assess the truth of every later theorem in the source; it establishes that proofs relying on the printed endpoint identities require replacement.
