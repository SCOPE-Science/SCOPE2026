---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For A=x coth(x), R=A'/(2x) and P=A-x²R, the positive dispersion branch has stationary points exactly when B=F(x,gamma)=R d(P,gamma)², where p d²-gamma d=1. The partial fraction expansion R(x)=2 sum_(k>=1) pi²k²/(x²+pi²k²)² is positive and strictly decreasing, P'=-x²R'>0. Thus F is strictly decreasing in x and increasing in signed gamma, from c0(gamma)²/3 to 0; there is precisely one positive global minimum when B<Bc and none otherwise, and its location strictly increases in gamma at fixed B. Taylor R=1/3-2x²/45+..., P=1+x^4/45+... yields onset x/sqrt(1-B/Bc)->sqrt(15/2) and minimum-speed quadratic correction. Large x gives P~x/2, R~1/(2x); explicit fixed-gamma inversion yields B^-1/2+gamma B^-1/4/sqrt2 -gamma^3 B^1/4/(16sqrt2)+O_gamma(B^1/2), with identically zero constant term; fixed-B gamma->infinity gives x~(2/B)^1/3 gamma^2/3. Independently computed stationary selectors and bisections tested onset across both gamma signs, strict order for B=.01,.1,1, weak B=1e-6 and strong gamma up to 10000, supporting but not establishing the global proof.

## originality

PASS

The exact finite-depth linear dispersion and shear/Bond threshold are explicitly preexisting in Ellingsen–Brevik and in Gao–Milewski–Wang 2021, and the qualitative shift of the wavenumber with shear was already observed. The audited theorem is scoped to global all-signed-shear strict minimizer ordering at fixed B together with an exact universal onset constant, cancellation of the weak-capillarity constant term and the strong-shear 2/3 scaling. The accepted 2021 OA manuscript §2.1 equations (10)-(13) and subsequent numerical figures identify the threshold and minima, not these quantified asymptotics or an all-real-parameter monotone stationary selector proof. Risk of an older asymptotic calculation remains.

## value

PASS

The selected wavenumber is a natural, physically meaningful phase-speed scale. The full all-shear monotonicity statement and singular parameter limits quantify when/how a distinct wavepacket scale emerges, and the cancellation of an expected asymptotic term is a structural fact beyond the known threshold and qualitative plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
