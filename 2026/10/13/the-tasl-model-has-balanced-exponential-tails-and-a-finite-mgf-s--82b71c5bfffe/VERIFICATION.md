---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every α, the source density has strictly positive finite normalizer and logistic factor L(x)∼e^{−x} as x→+∞ and L(−x)∼e^{−x}. Polynomial Pα has equal leading powers on both signs: α²x^6 if α≠0 and 2x^4 if α=0. Consequently fα(±x)∼Aα x^m e^{−x}; integration yields matching left and right survival equivalents; both hazard limits equal 1; Mα(t) converges exactly for −1<t<1 and diverges at both endpoints because a positive polynomial remains after cancellation. For Y=μ+βX β>0, strip becomes |t|<1/β and endpoint hazard limits 1/β. Independent verification reconstructed exact normalization and sampled integrals; the unrestricted result is elementary asymptotic analysis, not sampling.

## originality

PASS

Best-of-knowledge PASS restricted to the TASL-specific full tail and MGF-domain correction. The original paper gives a formula for the MGF and the polynomial density, so strip and exponential class are mathematically implicit; it does not state the exact convergence domain or balanced tail ratios, and describes the distribution as heavy-tailed in the standard exponential-moment sense. Credit general logistic and polynomial-tilt asymptotics; claim only explicit identification and correction.

## value

PASS

A published reliability/probability model is classified as heavy-tailed and its parameter is advertised as controlling tail type. Showing all parameters retain the same exponential rate and a fixed nonempty positive MGF domain materially changes extrapolation and risk interpretation; both-sided hazard limits are useful. This is a motivated source-specific correction, not merely an arbitrary parameter substitution or a claim about visual kurtosis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
