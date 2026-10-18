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

# Verification and reproducibility

The attached `verify.py` is a complete Python standard-library program. Run `python3 verify.py` from a directory containing the script. Its recorded execution returned `VERIFY_OK 1533` together with the minimizing parameter \(1.7090130666055141\), squared coefficient of variation \(0.0016869660783161\), and worst-direction minimizer \(1.7320508075688772\).

The code numerically integrates the **pointwise support formula** without using the closed moments as a quadrature input, tests the independently derived closed moments at 16 nondegenerate aspect ratios, checks the exact derivative formula of the critical function at 499 points, verifies rational polynomial sign cases at 99 test points, and checks the derivative of the normalized variance at 400 further points. It also brackets and bisects the unique stationary equation and tests that the two anisotropy objectives select different cones.

For the **all-real-parameter** theorem, the relevant logical evidence is the analytic proof: the exact support-function reduction, the evaluated integrals, the positive-factor derivative identity, the two exhaustive sign cases for the polynomial-radical derivative on \((0,3]\), and the separate upper bound for every \(t\ge3\). The checker is corroborative only. Finite quadratures are not proofs of the displayed integral identities, and finite sign samples are not proofs of monotonicity. No exhaustive computational or external certification is claimed.
