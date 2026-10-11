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

# Verification details

The proof requires no external numerical package or computational certificate. Its critical statements were reconstructed during the same-model review:

1. Choose \(y^*\) attaining its dual norm at the distinguished target \(u\). Since UQNA supplies a subsequence of every maximizing sequence with image \(\theta u\), the composed functional \(f=y^*S\) has \(\|f\|=\|S\|\). This uses neither domain nor operator norm attainment.
2. Verify phase calibration: \(\operatorname{Re}f(w_n)\to\|S\|\) makes \((w_n)\) an operator-norming sequence. Each subsequence has a further subsequence converging in image to \(\theta u\); the real part of the supporting functional forces \(\theta=1\). Therefore all images converge to \(u\), not merely selected subsequences.
3. Identify \(f\) with a member of \(\ell_1(\Gamma)\). Exhaust its coefficient mass by finite sets \(F_n\). The signed/phased vector \(a_n\) attains exactly the mass on \(F_n\). Every tail unit vector \(z_n\) obeys \(\|a_n\pm z_n\|\le1\), and both scalar values have real part at least \(\|S\|-2\tau_n\). The calibrated implication makes both images tend to the same \(u\), so \(Sz_n\to0\).
4. Check quantifiers: failure of uniform operator tail convergence permits a sequence of witness vectors \(z_n\) of norm at most one. Its contradiction gives \(\|S-SP_{F_n}\|\to0\), not merely convergence on a fixed collection of vectors. Each \(SP_{F_n}\) is finite rank, hence \(S\) is compact.
5. Check imported coverage: [1, Corollary 3.11(a)] is about **UQNA compact operators** being dense in the compact ideal, which supplies the necessary reverse inclusion. The compact ideal is operator-norm closed. The distance to the identity in infinite dimensions follows because a compact operator maps the weakly null coordinate basis sequence to a norm-null one.

No computation can establish the all-index-set assertion merely by testing finite matrices; this verification is analytic. The theorem does not claim all compact maps are themselves UQNA and provides no independently audited certification.
