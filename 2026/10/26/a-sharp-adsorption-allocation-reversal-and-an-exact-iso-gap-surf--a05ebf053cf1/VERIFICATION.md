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

# Verification record

The claimed quantity is the first positive eigenvalue of the negative generator of an irreducible reversible five-state chain. The proof establishes both the exact balanced eigenvalue and the full phase trichotomy by a surface Schur reduction, Sturm sign counting, and implicit differentiation of a simple root. The candidate domain is \(B>0\), \(d>0\), \(M>0\), with \(0<a<B\) and \(b=B-a\).

An independently implemented numerical checker, `gap_phase_checker.py`, was executed on its supplied source with NumPy, SciPy, and SymPy. It checked the exact generalized determinant factorization symbolically and constructed the original five-state generalized eigenproblem rather than evaluating the derived scalar root formula. The run passed 4,106 comparisons, testing randomized parameters on both sides of the transition and at the critical threshold, the spectral secular identity, and critical-plateau instances. The program prints a PASS line or raises an assertion on failure.

These numerical checks are finite and do not establish the infinite theorem. The proof does not address boundary allocations with exactly zero adsorption, extensions to arbitrary compartment chains, sampling uncertainty, or historical priority.
