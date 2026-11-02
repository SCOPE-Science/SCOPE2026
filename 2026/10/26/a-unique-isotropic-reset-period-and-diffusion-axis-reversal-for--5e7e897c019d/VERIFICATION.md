---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Positive-definite body mobility M gives positive Schur complement S=A-cc^T/m. Itô applied to F(theta)=-R(theta)Jc/m cancels the correlated W0 noise and yields each independent reset-cycle displacement Y=F(theta_tau)-F(0)+M_tau, with M conditionally centered. Angular first and second harmonics produce the exact centered covariance, its traceless part 2 beta h(u)(S0-gamma(u) H) and trace 2 beta tr(S)+||c||^2(1-e^-2u)/(m^2 tau). For c!=0, gamma=2m/(1+e^{2u}) bijectively decreases from m to 0, giving isotropy iff S0=alpha H with 0<alpha<m, unique tau* and perpendicular-to-parallel principal-axis swap. c=0 is correctly separated, near/far limits and positive definiteness hold. Independent numerical covariance, reset threshold and axis tests passed; the infinite-horizon assertion follows from independent cycles, not samples.

## originality

PASS

Full original Cleuren–Eichhorn source states the body-mobility model and drift but expressly leaves diffusion-enabled sorting to future work; the derived full tensor, iff alignment condition, unique threshold and axis swap were not found in inspected related resetting material. The iid-cycle CLT and angular harmonics are classical ingredients, not claimed novel.

## value

PASS

Exact necessary-and-sufficient design condition and unique reset period for isotropic long-time diffusion, with a sharp 90-degree axis reversal and drift-versus-dispersion trace law. This addresses physically motivated correlated translation/rotation noise absent from the uncoupled resetting model; generic tensors correctly have no exact isotropization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
