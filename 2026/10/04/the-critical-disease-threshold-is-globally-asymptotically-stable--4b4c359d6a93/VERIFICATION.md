---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Let \(\bar S=\Lambda/d_1\). The differentiated delay-compensating functional \(W_0=\Phi(S)+I+\beta\int_{t-\tau_1}^t S(s)I(s)\,ds\) satisfies exactly \(W_0'=-d_1(S-\bar S)^2/S+(\beta\bar S-d_2)I-IQ/(1+I)\); the package symbolic checker reconstructs this cancellation. Adding \(cQ\), with \(c\|h\|_\infty\le1\), and using the age-transport mass balance gives at \(\beta\bar S=d_2\) a nonpositive derivative with coercive dissipation in \(S-\bar S\) and \(Q\). Source boundedness plus an eventual positive lower bound on \(S\) makes the squared susceptible deviation integrable and uniformly continuous, so Barbalat yields \(S\to\bar S\). Bounded \(I\) gives bounded \(\dot I\), hence bounded \(\ddot S\); the derivative form of Barbalat gives \(\dot S\to0\), and the susceptible equation then forces \(I\to0\). The predator mass inequality then gives \(Q\to0\), and the characteristic formulas give the asserted age-profile convergence. This closes the source's strict threshold to the equality without relying on finite simulation.

## originality

PASS

The exact same-model World Scientific article was inspected in full-text sections containing the equations and disease-free theorem. It proves global disease-free stability for \(\Lambda\beta<d_1d_2\) and instability for the strict reverse inequality, leaving equality unstated. The current argument supplies a new critical Lyapunov--Krasovskii balance and an attraction proof specific to the coupled predator-age recruitment. Targeted Resultary search found no same-model equality theorem. A related 2026 AIMS paper was attempted through ordinary public routes and then authorized institutional access; the institutional tool returned no verified PDF and was not retried.

## value

PASS

The equality is the exact nonhyperbolic boundary between the source's extinction and invasion regimes. Closing the threshold from a strict to a closed condition for the full allowed delay and fertility class is a substantive dynamical result, and the proof exposes the model-specific cancellation responsible for it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
