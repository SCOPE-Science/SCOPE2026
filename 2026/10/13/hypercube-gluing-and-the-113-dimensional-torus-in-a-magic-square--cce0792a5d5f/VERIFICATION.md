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

# Verification notes

The supporting program `check_hypercube.py` runs with the Python standard library and no other dependencies. Execute `python check_hypercube.py` from the extracted package. Expected output starts with `VERIFY_OK` and reports a 16-vertex, 128-edge connected multigraph with first Betti number 113, finite-field branch profile `(4, 4, 4, 4)`, and rational torus-character multiplicities 3, 7, 11, 15 by nonzero Hamming weight.

The program enumerates every projective point on the two-quadrics base over the single field \(\mathbb F_{17}\), not all complex points or all primes. It checks finite-field smoothness using exact Jacobian minors and independently checks the graph-character Fourier formulas by integer arithmetic. The characteristic-zero proof of geometric smoothness, the scheme-theoretic reduction, analytic ordinary nodes, and the exact generalized-Jacobian extension is fully supplied in `RESULT.md`; no finite sample is used as an infinite proof.

A second mathematical consistency check compares the nodal arithmetic genus \(16+128-16+1=129\) with hyperplane adjunction \(1+(64+3\cdot64)/2=129\). The program has no claim to independent validation, external certification, or exhaustion of the literature.
