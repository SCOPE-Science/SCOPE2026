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

The geometric input is the classical identification of the \(28\) odd theta characteristics and the \(63\) twelve-element Steiner complexes via evaluation on two-torsion. For a chosen symplectic coordinate basis, the integer incidence matrix is constructed using exact binary dot products.

Run `python3 verify_smith.py`. It verifies the row counts, column counts, and \(MM^{\mathsf T}=16I+11J\) identity, then constructs unimodular transformations from explicit elementary row and column operations. It checks every entry of the final diagonalization \(UMV\) and the successive divisibility relations. The Smith diagonal is \(1\) seven times, \(2\) fourteen times, \(4\) six times, and \(12\) once; no other nonzero diagonal entries occur.

With the SymPy dependency, run `python3 verify_hnf.py`. It separately rebuilds the incidence matrix, computes its exact Smith and Hermite normal forms, checks the index \(805306368\), and shows that all \(28\) basis-vector orders in the integral cokernel are exactly \(12\).

The code is a finite exact certificate of the integral statement, not a substitute for the classical geometry relating the matrix to quartic curves. The proof does not establish arithmetic Frobenius module isomorphism for different curves, and independent scientific validation has not been performed.
