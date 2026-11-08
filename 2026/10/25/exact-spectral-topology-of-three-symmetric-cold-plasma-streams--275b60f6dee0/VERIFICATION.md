---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Derived P by multiplying the original dielectric equation by z(z-t)², and verified P(0)=-ut² and P(t)=-4t² so no spurious roots occur for u,t>0. Independently factored disc_z P=4t²Q and disc_t Q=-629856u(2u-1)³. For 0<u<1/4 Q has three real roots with negative product, positive sum, positive Q(0), and Q(2(1-u))<0: one negative and precisely two positive. For 1/4<u<1/2, Q(-1/2)<0<Q(-u) and Q(0)<0 ensure two negative and one positive root; at u=1/2 double negative root, above u=1/2 a single real positive root, at u=1/4 t=0 is excluded. For Q<0, cubic P has one positive real and a conjugate nonreal z pair, whose square roots give two growing oscillatory ω. For Q>0, real-root sign uses positive sum/product and sign of t[t+2(u-1)]: negative means one positive/two negative z, positive means three positive z. Boundary continuity identifies negative and positive double roots. IFT at (u,t)=(1/4,0), quadratic degeneracy near (u,t)=(0,2), and Q_{1/4} factorization establish the reported asymptotics and cutoff. All key symbolic identities plus exact rational u root counts for ten values and 23 independently sampled root-type cases were rechecked in independent_plasma_checks.py; finite checks are not the unrestricted proof. Degenerate real cutoffs can support secular growth.

## originality

PASS

Best-of-knowledge quantitative originality survives the primary texts that were actually readable: the submitted exact three-pole symmetric discriminant phase partition, u=1/4 disappearance of pure-imaginary growth, t_±=2±2√6√u+O(u), and t_-=3(1/4-u)+O((1/4-u)^2) were not established in the inspected 2009 electron-electron-ion article nor in accessible general abstracts. Crucially the 1978 Cuperman/Gomberoff/Roth paper investigates the SAME three-electron physics with broader hypotheses and its complete body is unavailable; its abstract already covers qualitative standing/travelling coexistence. Quantitative priority is therefore materially uncertain and this PASS is not a historical originality guarantee. The conclusion does not treat failed searches as proof.

## value

PASS

The symmetric three-electron cold longitudinal dispersion is a physically motivated multistream model. Its exact all-density split between nonoscillatory and oscillatory temporal growth, sharp finite-wavenumber transition ratio b/a=1/4, and singular square-root opening at dilute background distinguish two instability mechanisms and provide quantitative boundaries for further plasma stability comparisons. Although cubic discriminants and qualitative standing/travelling modes are classical, the complete natural one-parameter phase classification and endpoint scaling are non-arbitrary and useful mathematical invariants rather than a random numerical slice or routine normalization check. Does not claim kinetic or nonlinear physics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
