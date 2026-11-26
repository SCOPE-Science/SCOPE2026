---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The stated Hermite functions are orthonormal under the stated Fourier convention. Differentiating the Gaussian Fourier transform in ξ gives the first two y-moments divided by the transform as −2iξ and 1/π−4ξ². This yields the cross-Wigner factor 4√π(x+iξ) and the diagonal h_1 factor 2(4πr²−1), both multiplying exp(−2πr²). Setting u=4πr² and b=|c|², the squared angular average divided by 4e^(−u) is (1−2b+bu)²+2ub(1−b); the phase disappears only after averaging. The polar measure du/4 then gives the asserted polynomial C+4Ub−(2U+V)b². At U≤0, the endpoint difference 2U−V=s²e^(−s)−t²e^(−t) is strictly negative, so neither an alternate endpoint nor an interior extremum ties b=0. At U>0,V≤0 the two endpoint derivatives are nonnegative and the polynomial increases to the unique maximum at 1. At U,V>0 the unique interior vertex improves on the endpoints by 4U²/(2U+V) and V²/(2U+V). The expansions U/δ→(s−1)e^(−s) and V/δ→(−s²+4s−2)e^(−s) yield the shell branches. At s=1 the first limit vanishes and the second is strictly positive, giving b_*→0; at s=2+√2 the second vanishes and the first is positive, giving b_*→1. These are radii in the dimensionless squared radial coordinate. The uniqueness is of the population, not of a phase representative. The all-annulus proof, not the reported finite quadrature, establishes these statements.

## originality

PASS

The verified distinct content is the exact all-annulus optimizer and coherent-state gain within the first two Hermite levels for the squared pure-state Wigner functional, including both thin-shell thresholds. The inspected unrestricted Wigner result gives existence, not the restricted coefficient optimization. The closest indexed exact annulus calculation is for a fixed Gaussian-window STFT, whose radial localization is linear in the populations; it does not have this nonlinear mechanism. Standard cross-Wigner polynomials and radial quadrature are not credited as new. This assessment is limited to inspected evidence, not a claim of priority.

## value

PASS

The vacuum and the first excited level are the simplest centered oscillator span where a relative coherence is possible. A rotationally invariant mask removes the mean interference in the signed functional but not its squared contribution. The closed optimizer proves when coherent states are necessary and by exactly how much they beat both eigenstates, and its two nontrivial shell boundaries give a compact benchmark for nonlinear Wigner localization. This is more than a diagonal mode crossing, though it is not the unrestricted problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
