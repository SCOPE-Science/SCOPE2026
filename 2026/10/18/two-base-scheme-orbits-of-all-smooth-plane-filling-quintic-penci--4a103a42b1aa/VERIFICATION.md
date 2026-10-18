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

This classification is finite over \(\mathbf F_3\). The supplied source programs use exact modular arithmetic; they are not empirical estimates.

Run `python3 verify_geometry.py` alongside `enumerate_pencils.py`, with SymPy installed. It checks the \(576\) individual smooth forms by rational-eigenvector tests, constructs all \(2016\) qualifying pencils, reconstructs the full projective group, checks both orbit sizes, verifies algebraic-closure smoothness of both individual-curve orbits on all three affine charts, confirms rational tangents are independent, and computes chartwise Gröbner bases for each pencil representative. In the reduced case it checks radicalness, and in the nonreduced case it checks the degree-three factor to the fourth power, including irreducibility.

Separately run `g++ -std=c++17 -O2 verify_rref.cpp -o rref_checker && ./rref_checker`. This visits \(896260\) distinct two-dimensional RREF subspaces, independently of the smooth-generator-pair algorithm, and verifies that exactly \(2016\) satisfy the eigenvector criterion for all four projective members. Expected outputs are in `EXPECTED.txt`.

The geometric smoothness tests use the Jacobian ideal over the algebraic closure, not tests limited to \(\mathbf F_3\)-points. The pencil base-locus computations are exact finite Gröbner calculations over \(\mathbf F_3\). The statement excludes extensions of the finite field and does not certify the absence of other published formulations; no independent audit has been performed.
