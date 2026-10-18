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

The bird subsystem gives I_b*=mu_b(R0_b-1)/beta_b, so all-positive necessity and positivity of kappa coincide with R0_b>1. Substitution into the full human S/E/I/R equilibrium equations reduces to beta_h I_h^2+[kappa+mu_h(1-R0_h)]I_h -(mu_h R0_h/beta_h)kappa=0. Since beta_h>0 and constant term negative for kappa>0, one root is positive and one negative, and remaining compartments reconstruct positive. Expanding the exact positive root yields the three distinct kappa downarrow zero regimes. Independently checked rational constant terms for mu_h=2/5,beta_h=3/2,kappa=1/7,R0_h in {1/2,1,3/2}: -2/105,-4/105,-2/35. No stability conclusion asserted.

## originality

PASS

The 2026 source explicitly prints a stronger incorrect joint R0_b>1 AND R0_h>1 biological feasibility requirement, despite its own negative constant-term quadratic. Earlier zoonotic spillover papers establish the general concept but are stochastic or use a different model; the source-specific exact correction and singular response law are a meaningful result. Best-of-knowledge PASS, recognizing general reservoir-forcing priority.

## value

PASS

Changing a published feasibility region from a joint condition to reservoir-only threshold materially changes interpretation of human endemic burden and intervention strategy; the unique equilibrium and three critical response scalings are model-specific, mathematically useful corrections rather than a generic slogan about spillover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
