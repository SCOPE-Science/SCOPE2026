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

The following checks were performed against the cited primary source and the proof above.

1. Fan--Li define \(P=\mathbf P^{n-1}\), \(L=\mathcal O_P(-1)\), \(H=\operatorname{Tot}_P(L\oplus Q)\), and prove that \(W\to H\) is an affine torsor under an additive line bundle.
2. They identify \(H_0=V(r)\) with \(\operatorname{Tot}_P(Q)\) and identify \(F\) scheme-theoretically as \(W\times_H H_0\).
3. Their proof of the Grothendieck-class formula explicitly uses that an affine torsor under a line bundle is Zariski locally trivial with fiber \(\mathbf A^1\), which is exactly the local hypothesis needed for affine-bundle homotopy invariance of Chow groups.
4. Applying homotopy invariance twice gives \(\operatorname{CH}^*(W)\cong\operatorname{CH}^*(P)\) and \(\operatorname{CH}^*(F)\cong\operatorname{CH}^*(P)\).
5. The tautological coordinate \(r\) is a section of the pullback of \(L\), so \(\mathcal O_H(H_0)\cong\pi_H^*L\). Scheme-theoretic flat pullback gives \(\mathcal O_W(F)\cong\rho^*L\); hence \([F]=-h\) and \(N_{F/W}=\rho_F^*\mathcal O(-1)\).
6. Since \(W\) is smooth, \(\operatorname{Pic}(W)=\operatorname{CH}^1(W)\); the relation \(h^n=0\) and nonvanishing of \(h^j\) for \(j<n\) are the standard projective-space Chow-ring relations.

Limits: no claim is made for the larger-Jordan-block models. No computational enumeration or floating-point evidence is used.
