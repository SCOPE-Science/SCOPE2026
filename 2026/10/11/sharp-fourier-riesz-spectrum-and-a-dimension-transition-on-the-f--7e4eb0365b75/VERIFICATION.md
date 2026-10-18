---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The vvᵀ cone has |X|=(q^m+1)/2 and averaged characters equal (1+Σ_{v∈F_q^m}phase(v))/(q^m+1). Independent bilinear character sums yield u=(1+q^{m-1})/N for equal/intersecting edge frequencies and v=(1+q^{m-2})/N for disjoint edges. Orthogonal edge-frequency differences give q^{m-1}(q-1)/N; unsigned complete-graph incidence diagonalization IᵀI=2I+A(J(m,2)) gives the star and cycle eigenvalues with multiplicities m-1 and E-m; the constant couples to the all-edges line in exact 2x2 block K. Positive-definiteness also follows by restricting vectors v to supports size≤2 and Fourier character independence. Exact symbolic determinant sign factor m(q-2)+4+q^{m-2}(4(q²-q+1)-m) determines the sole lower mode switch at m=4(q²-q+1)+1; fixed q, L+~(q-1)m²/(2q²), L-~4(q-1)/m. Independently assembled q=3,m=4 Fourier Gram and eigenvalues to numerical tolerance 2.7e-15 and derived symbolic factor and q=3,5,7,9,11 sign boundaries.

## originality

PASS

Eldar–Bölcskei geometrically uniform frames provide abstract Fourier diagonalization and are explicitly credited; those results do not compute this rank-one symmetric Veronese Gram or its sharp lower-eigenmode crossover. Published first-coordinate Fourier spectrum on rank-one matrices concerns nonzero rectangular rank-one matrices and rook rather than Johnson incidence representation. No inspected stronger formula yields all five multiplicities and the threshold for this singular symmetric cone.

## value

PASS

The natural family of off-diagonal Fourier samples on the finite-field quadratic Veronese variety has a full Riesz-spectrum and sharp condition-number transition. The switch from edge-cycle to constant-coupled mode at a natural finite dimension threshold gives nontrivial useful exact conditioning data for harmonic frames and finite-geometry sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
