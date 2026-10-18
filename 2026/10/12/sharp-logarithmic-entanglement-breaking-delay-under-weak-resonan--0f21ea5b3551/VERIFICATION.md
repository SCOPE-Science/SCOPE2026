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

The Bloch generator has damping eigenvalues with negative real part and fixed Bloch vector (0,-2Ω/(1+2Ω²),1/(1+2Ω²)). Its stationary-state determinant Ω^4/(1+2Ω²)^2 is positive for Ω>0, giving eventual Choi-PPT and finite EB; Ω=0 amplitude damping retains negative PPT eigenvalue -exp(-t)/2. In the scaling t=4log(1/Ω)+s, the exact y,z spectral projectors give slow Ω² exp(-s/2) and fast Ω⁴ exp(-s) terms. Schur complement of the reference-partial-transposed 4x4 Choi matrix tends after Ω^-4 to 1/2 diag(1-exp(-s),1+exp(-s)); other two eigenvalues tend to 1/2. Qubit PPT iff EB and composition monotonicity squeeze T_EB=4log(1/Ω)+o(1). Independent finite-dimensional Bloch-Choi eigenvalue calculations verified convergence of both fixed-s profiles (e.g. Ω=0.01: -0.8574 at s=-1 versus limit -0.85914; +0.31555 at s=+1 versus limit +0.31606); finite calculations do not prove the joint limit.

## originality

PASS

Hanson-Rouze-Franca proves eventual EB of primitive quantum Markov semigroups for fixed Ω but not the weak-drive singular onset, exact coefficient 4 or universal scaled Choi-PPT boundary. Resonant optical Bloch dynamics, Choi-PPT criterion, and undriven damping are already known; no direct coverage of the asymptotic first-passage time was identified.

## value

PASS

The entanglement-breaking lifetime is a natural operational quantum memory invariant, and weak resonant driving separates infinite zero-drive lifetime from a sharp divergent finite lifetime. The exact log coefficient and transition profile quantify a physically motivated singular regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
