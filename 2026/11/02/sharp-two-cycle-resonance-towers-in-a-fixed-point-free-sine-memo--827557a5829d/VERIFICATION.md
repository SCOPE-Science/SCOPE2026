---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The actual RESULT.md (Git blob 0faf225e618bf6f36892420b4de51c04f09922c7) treats F(x,y)=(alpha cos x+beta x sin(pi y),y+x) on the entire real plane, alpha,beta>0. A genuine two-cycle has first coordinates u,-u (u>0), and midpoint z satisfying alpha cos u=beta u cos(pi z) sin(pi u/2), 1=-beta sin(pi z) cos(pi u/2). The second equation excludes beta<1, and beta=1 requires u=2k and cos(2k)=0, impossible by irrationality of pi. For beta>1 the reduced scalar resonance equation (2n±t)Phi_beta(t)=alpha|cos(2n±t)| has Phi_beta(0)=0, Phi_beta'(0)=pi sqrt(beta^2-1)/2>0. Uniform derivative domination gives one root on each side of 2n for every large n; reconstruction of (cos pi z,sin pi z) prevents extraneous roots. A uniform Lipschitz estimate gives the stated O(n^-2) location remainder even for small |cos 2n|. Independently solved and checked 12 high-precision full orbit returns for beta=1.82,1.05. No global census outside two small windows is proved.

## originality

PASS

The prior 2023 map introduction supplies the exact FPFM3 model and numerical iterative plots, not the analytic threshold or remote two-cycle branches; other memristor maps have different nonlinearities. This is an analytic dynamics result, not merely a reparameterization of existing fixed-point-free examples.

## value

PASS

The model has no fixed points, so existence and sharp gain threshold for high-amplitude period-two orbits are natural missing dynamical information. The proof yields infinitely many distinct real-plane cycles and an explicit phase-sensitive asymptotic displacement, a substantial analytic addition beyond numerical plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
