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
The proof has two independent parts.

For \(r\ge1/3\), the backward Euler operator factors into two commuting second-order resolvents \((s_\pm I-X)\) with real \(s_\pm>2\), or one repeated factor at the endpoint. Their Green kernels are explicitly positive geometric kernels, so their convolution is strictly positive. Preservation of constants gives total kernel mass one and therefore the range principle.

For \(0<r<1/3\), the two factor parameters are a nonreal conjugate pair. The decaying characteristic roots are \(q\) and \(\overline q\), so the real Green coefficients are a nonzero exponentially damped cosine sequence. A nontrivial circle rotation necessarily enters the negative cosine half-plane, proving that at least one Green coefficient is negative.

The bundled `verify.py` checks the shift-polynomial factorization using exact rational arithmetic and evaluates the closed Green formula at \(r=1/10\), where the distance-three coefficient is strictly below \(-1.7\times10^{-4}\). This numerical witness is not used to prove the universal subthreshold sign change.

No finite-boundary or periodic-size classification is claimed.
