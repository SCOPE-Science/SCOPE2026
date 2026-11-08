---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Walsh character diagonalization gives each Hamming-shell kernel as a finite Krawtchouk sum of R(2kh). Independently reconstructing shell numerators with symbolic exact rational algebra recovered the leading coefficients of Q4 and Q5, and the values of diagonal shells at h=3/2: -3/1804 for d=4 and -15549/349976 for d=5. Positive-coefficient off-diagonal numerators through d=4 and shells r=1..4 at d=5, plus two sign changes and rational sign witnesses for Q4,Q5, prove the advertised windows. G5 increases from negative to positive once, and its root lies below the first Q5 root. R(z)=1-z+z^2/2-z^3/6+z^4/36+z^5/108+... and (-L)^5 distance-five path sum 5! give coefficient -10/9. Pascal monotonicity extends the negative diagonal at h=3/2 to d>=4; spectral convergence to rank-one uniform projection gives eventual positivity for fixed d. The d>=6 claim does not classify all windows.

## originality

PASS

Theorem is specifically the exact all-step endpoint kernel positivity phases for unweighted Boolean hypercubes under unmodified two-stage Radau IIA. Classical absolute monotonicity and generic path-length sign criteria do not determine the four/five-cube algebraic intervals. The dimension-five distance-five failure is related to an already-known short-step path obstruction.

## value

PASS

Positivity of high-order RK endpoint steps is a natural structural question in numerical diffusion; the precise hypercube threshold and disconnected time-step windows illustrate nonmonotone positivity on a canonical graph family. The result is a complete useful classification for dimensions 1..5, with valid explicit higher-dimensional obstructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
