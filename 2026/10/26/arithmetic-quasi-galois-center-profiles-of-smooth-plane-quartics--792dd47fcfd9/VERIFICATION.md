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

# Exact computational verification

Requires Python 3 with SymPy 1.14.0 (another SymPy version may work but was not checked). Place the two scripts in a writable directory and run `python compute.py` and `python verify_independent.py`. They independently enumerate projective coefficient orbits and fixed-elation coefficient subspaces, use different monomial orders and Gröbner monomial orders, and save `quasi_census.json` and `independent.json`. Compare those files bytewise or structurally against the embedded reference JSON for the corresponding script; timestamps are not present in the outputs.

Reference claims: 168 projective transformations; 279 total orbits of nonzero quartic equations; 78 smooth orbits and 10,920 smooth quartic masks; exactly 21 nonidentity elations, 8,415 nonzero quartics invariant under at least one, 4,054 candidates after center-exclusion, 1,184 smooth invariants, and 17 smooth quasi-Galois orbits. The class-profile arrays in `independent.json` give the detailed nine triples in the finding.

For each chart, the code tests the unit ideal of the polynomial and both chart partial derivatives by a Gröbner basis over \(\mathbf F_2\). It thereby certifies absence of a geometric singular point in that chart. The three standard affine charts cover the projective plane, and the 168 projective matrices cover coordinate equivalences over \(\mathbf F_2\). The first and second programs reproduce the same 17-class and 1,184-equation statistics. The exact calculation is computationally executable but external independent validation was not performed.
