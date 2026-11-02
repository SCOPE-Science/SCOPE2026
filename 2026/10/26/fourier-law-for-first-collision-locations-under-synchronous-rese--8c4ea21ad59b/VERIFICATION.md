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

Because N is odd, 2 has a modular inverse and the center/difference coordinate pair is bijective. Each non-reset update moves one coordinate ±1 (probability 1/4 each) and leaves the other fixed; absorption is first difference hitting zero. Fourier transforming the center gives a tridiagonal Dirichlet recurrence with parameter alpha=acosh(2/(1-r)-cos k) and explicit cosh-ratio solution. Geometric renewal divides the unreset first-hit Fourier transform by its zero mode. The lazy difference-chain Poisson equations give E[S]=2i(N-i) and the displayed second factorial moment, producing the sharp derivative and correct absence of integer equality. Independent absorbing ordered-pair matrices matched all tested Fourier probabilities and means for N=3,5,7; the finite checks do not extend the universal proof.

## originality

PASS

The physically important distinction is between absorption at the first collision anywhere and hitting a designated diagonal vertex. The Suarez-Jimenez–Riascos–Boyer and Rubio-Gomez–Riascos–Mateos studies present target-specific first-encounter mean formulas, whereas here the entire winning-location distribution over all targets is computed. General renewal and interval limits are acknowledged as prior principles. Full primary recent PDF retrieval remained blocked, so a stronger hidden statement remains a risk, but no decisive covering comparison was found.

## value

PASS

Where two particles collide is physically meaningful for reaction placement; a first-collision-anywhere law goes beyond a mean at a prescribed node. The full Fourier law and sharp finite-cycle restart derivative identify an unintuitive parity effect (on C5, reset helps starts two graph steps apart but hinders adjacent ones), so the result is a motivated exact stochastic-transport classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
