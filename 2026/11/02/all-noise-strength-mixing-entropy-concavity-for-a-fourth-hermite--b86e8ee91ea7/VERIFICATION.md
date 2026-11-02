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

With the accompanying `verify.py`, execute `python verify.py`. The script constructs \(\operatorname{He}_4\) and \(\operatorname{He}_8\) symbolically and evaluates Gaussian monomial moments by exact integer double factorials. All eight moment identities, four strict integer Cauchy ceilings, and the exact fractional derivative bounds are asserted. In particular the worst-case logarithmic error in the first derivative is \(1808355327013/45240320000<40\), the second-derivative correction is \(388378921813/22620160000<18\), and the remaining strict margins imply \(F''(t)\le-7a^2q^4\).

The universal Hermite convolution formula, positivity inherited by conditional expectation, differentiation identities, and scalar log-remainder inequality are justified analytically in `RESULT.md`. The script tests the arithmetic of this proof rather than sampling parameter values or purporting to certify originality. The domain is \(0<a\le1/100\), \(0<q\le1\), and \(0<t<1\); no more general claim is certified. Independent audit has not been performed.
