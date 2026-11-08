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

Sum/difference of positive swap logarithms force gamma<1 and S=4A(z)/(1-gamma), with A(z)=atanh(z)/z strictly increasing. The true 2-step derivative is (P DF)^2. Its Schur expressions factor through q(z)=(1-z²)A(z), q strictly decreases from 1 to 0. z_- and z_+ are unique, with unique crossing where q(z)=z² and gamma S=2. At crossing B has trace -2, determinant 1 (nonhyperbolic; no nonlinear boundary claim). Independent direct-root, orbit exchange and Schur algebra checks agree with numerical gamma*. All restrictions are local and off-diagonal.

## originality

PASS

Antiphase two-cycles and bifurcation diagrams of the same symmetric Ricker model are documented in Kulakov et al. 2022, and Goldar et al. 2026 give generic period-two/Jacobian criteria. The complete explicit exchange-orbit parameterization, both growth boundaries, and coupling-independent exact cutoff are not implied by these numerical/general statements without a new analysis. Historical priority with older full-text bifurcation studies remains uncertain.

## value

PASS

A natural symmetric ecological time-sharing orbit receives a complete analytic existence-and-local-stability phase diagram, including a sharp universal upper limit on cross-species competition; this is more informative than a graph or numerical sampling of dynamic regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
