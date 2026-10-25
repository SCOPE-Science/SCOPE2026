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

Run `python torus_checker.py` with Python 3 and SymPy installed. The program generates the cyclic facets, enumerates induced subcomplexes for all subsets of three through seven vertices, verifies edge multiplicities and six-cycle links, and computes exact integral presentation and inclusion matrices. The last line must state that integral, chain, and surface checks completed. It asserts successive compositions of inclusion maps vanish and that the integral horizontal survivor vector is `[1,0,1,0,0]`.

Expected complete horizontal matrix shapes are `(49,21)`, `(42,49)`, `(14,42)`, `(2,14)`, with nonzero Smith entries respectively twenty, twenty-nine, twelve and two copies of \(1\). These are complete integer presentations; the script tests saturation of all chosen coordinate lattices and local relation modules. Since the example has seven vertices, these are exhaustive checks, not samples from an unproved infinite family.

This calculation does not verify novelty against all existing literature and is not an independent audit. It computes double (co)homology, not a homotopy type for the moment-angle complex.
