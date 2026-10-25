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
The provided `verify_trap_rank.py` is executable with Python and NumPy. It computes the constant, centered-incidence and orthogonal-incidence projector matrices, then compares their restricted column ranks with the graph-theoretic formula for all 1023 nonempty sink sets of \(J(5,2)\), 500 seeded samples each of \(J(6,2)\), \(J(7,2)\), and \(J(8,2)\), and eight four-trap comparisons on larger graphs. Output: `PASS 2531 independent finite projector-rank checks; 4-cycle rank 8 vs triangle-with-tail rank 9`.

The verification is finite and numerical (projector identities are checked to a tolerance of \(10^{-10}\); rank is computed with a tolerance of \(5\times10^{-8}\)). These tests corroborate but do not certify the universal theorem. The universal domain, exact combinatorial rank statements, and nondecaying-subspace interpretation are established analytically in `RESULT.md`. No external scientific audit or validation has been performed.
