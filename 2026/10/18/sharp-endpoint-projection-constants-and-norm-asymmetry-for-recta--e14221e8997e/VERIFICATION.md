---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and verification

Run `python verify.py` with the standard Python library. The program constructs graph-incidence potentials using exact rational coefficients, then forms the cut projection \(P_t\) and cycle projection \(Q_t=I-P_t^{\mathsf T}\) directly in the edge basis. It verifies the edge-orbit row and column formulas, zero divergence of every computed cycle column, idempotence of representative matrices, the four balancing parameter equations, and strict endpoint inequalities for unequal axes. The current package's script completed successfully, printing `PASS: 28641 exact-rational assertions`.

The computations use sizes \((3,4)\), \((3,5)\), \((4,5)\), and \((3,3)\) for matrix checks, with further exact-arithmetic inequality examples. They do not exhaust the infinite family. The proof in RESULT.md establishes the universal statement through symmetry, tensor identities, exact absolute sums, convexity, and algebraic factorization. No independent audit has been performed.
