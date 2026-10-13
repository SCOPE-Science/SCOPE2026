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

`verify.py` uses exact integer polynomial arithmetic only. It reconstructs the six diagonal-entry polynomials of \(X(t)\) and \(Y(t)\) from the source coefficient vectors, computes
\[
\operatorname{tr}(X(t)^{*2})+\operatorname{tr}(Y(t)^{*2})-2F(t)^2,
\]
and checks equality with \(-2(t^2+3)Q(t)\) coefficient by coefficient.

For the rational-root certificate, the script verifies that \(Q\) is monic, that \(Q(r)\equiv r^{14}\pmod3\), and that after \(r=3u\) every nonconstant coefficient contribution is divisible by \(3^8\) while the constant term is exactly \(3^7\).

The source's displayed matrix at \(t=2\) is also checked directly: every squared row has sum \(100962050\), each squared main diagonal has sum \(55622784\), and the defect is \(-45339266\), agreeing with the symbolic formula.

The checker does not enumerate algebraic values of \(t\), and the theorem makes no claim about them. It also does not test unrelated order-\(6\) bimagic constructions.
