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

# Verification and scope

The exact quantile is \(Q_a(u)=\log[-\log(1-u^{1/a})]\). Its derivative is verified symbolically by the chain rule. With \(B(w)=(e^w-1)[-\log(1-e^{-w})]\), direct differentiation yields \(B'(w)=e^w[-\log(1-e^{-w})]-1\) and \(B''(w)=e^w[-\log(1-e^{-w})-1/(e^w-1)]\). Their strict signs follow from \(z<-\log(1-z)<z/(1-z)\). The endpoint asymptotics and the integrated-quantile criterion are part of the written analytic proof. This reasoning, not finite tests, discharges the universal quantifiers.

The attached `verify.py` is self-contained Python 3 with only standard-library imports. Its executed checks cover 40,000 seeded real parameter and interval choices, plus diagnostic derivative comparisons and endpoint tests. The script uses `math.log1p` to avoid cancellation in extreme-tail calculations. It prints a `VERIFY_OK` line on success. No data download or external service is needed for replay.

Limits: the checker does not exhaust a continuum, establish novelty, prove a sharp scalar variance constant, or provide independent review. The derived convex-order comparisons rely on finite logarithmic moments, which follow from the specified exponential tails.
