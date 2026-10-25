---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The positive logistic two-species model has common equilibrium E=(1,1). Its two seasonal Jacobians J_A=[[-a,b],[0,-a]], J_B=[[-a,0],[-c,-a]] are Hurwitz, and the duty-weighted average has eigenvalues −a ± i sqrt(bc theta(1−theta)), also Hurwitz for a,b,c>0. Exponentiation of nilpotent shears yields monodromy M=e^{−aT}[[1,b theta T], [−c(1−theta)T,1−bc theta(1−theta)T²]], with normalized trace 2−z², det 1, z=T sqrt(bc theta(1−theta)). For z>2 its negative real eigenvalues are −exp(±2 arcosh(z/2)); otherwise spectral radius=1. Therefore local Floquet instability iff z>2 cosh(aT/2), and at equality multipliers exactly −1 and −e^{−2aT}. Maximizing w/cosh(w) via 1−w tanh(w), uniquely zero at w tanh w=1, gives the sharp one finite open period band when a/nu<0.662743419..., with one isolated neutral tangency at equality. Solving theta(1−theta)>C_T gives a unique symmetric duty-share interval. Independent code directly multiplied monodromy matrices and checked formula on 576 parameter sets plus root bounds; universal assertions follow by exact matrix algebra and monotonicity, not parameter sampling.

## originality

PASS

A qualitative stability reversal when alternating individually stable systems is already established by Cima–Gasull–Mañosa, and the generic product-of-exponentials Floquet criterion is Gökçek 2004. Ji–Strugarek give sharp seasonal thresholds for cooperative concave population dynamics, but those monotone hypotheses exclude the negative season-B cross derivative; their threshold can be one-sided instead of the present centered duty band. The present claimed contribution is this specific positive logistic two-species family and complete exact joint period–duty threshold, not Floquet theory or Parrondo paradox in general. The 2026 Chowdhury ecological-network forcing preprint was only inspectable at abstract level, so broader implicit coverage remains possible.

## value

PASS

Switching the direction/sign of ecological feedback is a natural controllable seasonal mechanism, and the exact one-band period window is nonobvious despite stable frozen and averaged systems. The analytic duty-centering law, universal critical constant and sharp boundaries give useful complete model-specific stability information, not a mere numerical example of a known paradox.

The dated certificate retains the supplied scientific assessment, sources and limitations.
