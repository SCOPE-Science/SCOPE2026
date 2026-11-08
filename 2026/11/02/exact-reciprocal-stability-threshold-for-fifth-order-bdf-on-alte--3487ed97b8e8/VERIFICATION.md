---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The actual Lagrange-interpolation derivative coefficients yield the 4-dimensional difference companion update and the two-step Floquet characteristic quartic. Independently reconstructed this quartic with exact SymPy arithmetic from interpolation nodes; its Cayley transformed quartic has q4=-32 P(r), P(r)=r^3(4u^3-8u^2-95u-127), u=r+1/r. All 13 and 19 coefficients of the two required Hurwitz-determinant polynomials were recomputed exactly and are positive. The cubic has a unique root above 2 and yields R*=6.2884027455921725. Positive q4 gives four interior Floquet roots; q4=0 leaves a simple -1 root with three strictly interior, while negative q4 gives exactly one real multiplier below -1. The constant solution remains a simple extra Floquet multiplier 1. This proves strict damping only for 1/R*<r<R*, and endpoint zero-stability for a fixed two-periodic grid, not arbitrary variable meshes.

## originality

PASS

Earlier general variable-step stability frameworks, a known BDF5 unstable witness at ratio 10, and smooth-grid sufficient conditions are expressly excluded from the novelty claim. The evaluated exact reciprocal iff threshold, all exterior root counts and simple boundary multiplier survive the inspected comparisons; historical specialist original full texts remain an explicit priority risk.

## value

PASS

The sharp critical adjacent-step contrast gives a necessary-and-sufficient stability boundary for a standard high-order integrator in a natural fixed non-smooth periodic test family. It provides a useful counterbalance to conservative sufficient-ratio estimates, not just a restatement of an unstable sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
