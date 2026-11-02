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

Derived the Cauchy–Binet determinant as a sum of strictly positively weighted squared sines of pairwise node-angle differences. For 2/3 Gauss nodes the common direction occurs at the displayed exact integer multiples of pi sqrt(3) and 10pi/sqrt(15), respectively. Four-node singularity would force rational a/b from both symmetric node pairs, whereas (a/b)^2=(23+4 sqrt(30))/7 is irrational. Continued fractions give infinitely many q with |q a/b-p|<1/q, and testing perpendicular direction yields the pi^2/q^2 eigenvalue upper bound. Undamped exact W/h has eigenvalues 1/2 ± |sin(omega h)|/(2|omega|h), so the operator-norm discrepancy tends to 1/2. Independent numeric weighted determinants and convergents corroborate the derivation but are not its proof.

## originality

PASS

The sampled-reachability rank criterion and older Gauss quadrature exactness explain the mechanism but do not directly furnish the precise Gauss-node arithmetic threshold, the lower-order resonance sets, or the near-resonant conditioning defect. The closest integrator literature concerns positive semidefinite Lyapunov evolution using different methods, so best-of-knowledge originality survives with specialized-priority risk.

## value

PASS

Positive definite rather than merely positive semidefinite quadrature is a natural rank-preservation design question. The sharp four-node threshold and infinite badly conditioned subsequence show rigorously that unconditional algebraic rank retention need not imply robust approximation, a structural warning for direct Gramian quadrature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
