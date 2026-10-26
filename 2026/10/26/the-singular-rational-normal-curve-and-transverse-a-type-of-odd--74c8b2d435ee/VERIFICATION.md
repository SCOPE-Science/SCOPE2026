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

# Checks and limits

**Symbolic identity.** Starting from Massri's transvectant coefficient formula (Equation (3)), set \(a_0=1,a_1=0\), solve the first two quadrics for \(a_{r-1}\) and \(a_r\), and obtain the exact residual equation \(F_r\) printed in `RESULT.md`. The nondegenerate antidiagonal Hessian has size \(r-4\) and no zero entries on the antidiagonal for any odd \(r\ge7\).

**Proof check.** Independently of numeric experiments, the moment-map differential rank criterion and the \(\mathfrak{sl}_2\) stabilizer classification identify the reduced singular support exactly. This forces the coefficient of the one-variable residual \(t^{(r+1)/2}\) after the analytic completion of squares to be nonzero. The transverse Jacobian algebra has dimension \((r-1)/2\).

**Exact computations.** Run `python3 verify_moment.py` from the directory containing the script. The standard-library-only program checks degrees \(7,9,11,13,15,17,19\), reconstructs the residual polynomial by integer binomial coefficients, checks the nondegenerate transverse Hessian and obtains nonzero stationary coefficients by exact rational Gaussian elimination. It prints the values and terminates with an assertion error if any test fails. These seven finite tests are not an infinite proof.

**Limits.** The statement applies to complex odd degrees at least seven and completed local analytic germs. It does not compute Jacobian scheme multiplicities, characteristic-dependent behavior, or projective global resolution data. The supporting 2013 source explicitly gives only one singular inclusion; the inaccessible arXiv:1202.5531v4 remains a possible literature-overlap risk. An independent audit has not been performed.
