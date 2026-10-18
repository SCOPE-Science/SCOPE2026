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
# Verification

The reproducible artifact `verify.py` is a Python 3 standard-library-only program. Execute `python3 verify.py` from the extracted package directory. It prints `VERIFY_OK total_automorphism_cases=492` after completing all assertions.

The program constructs every generating closed neighborhood, every face of the auxiliary cone complex and every proposed free collapse pair for \(1\leq n\leq5\). It checks the actual codimension-one cofaces **at the time of deletion**, verifies the exact residual face set, rebuilds all \(2^{n-1}\binom{n+1}{2}\) higher-dimensional square faces and triangulating pairs, and checks the vertex correspondence under affine automorphisms. For \(1\leq n\leq4\), all automorphisms are enumerated; for \(n=5\), the additional 50 cases are deterministic samples. Independent orbit-barycenter fixed-point subcomplexes for three-cycles are built and their full mod-two homology computed in dimensions three through five. Signed Lefschetz traces of the original simplicial nerve and cubical two-skeleton are independently computed and compared as consistency checks.

The expected collapse-pair counts for \(n=1,2,3,4,5\) are \(0,4,40,256,1344\), with square counts \(1,6,24,80,240\). These finite checks do not assert any inference from tested cases to untested dimensions. The all-dimensional proof rests instead on the unique-neighborhood argument, the explicitly equivariant collapse, the complete square-incidence identification, and the fixed-coordinate argument.

The cubical model is an unpointed equivariant homotopy equivalence; no canonical equivariant sphere-wedge model and no independent audit are asserted.
