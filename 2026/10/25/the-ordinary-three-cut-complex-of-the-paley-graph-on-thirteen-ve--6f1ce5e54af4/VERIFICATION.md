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

Run `python3 verify_paley13.py` in the same directory as this file with a standard Python 3 installation. No external libraries, network access, precomputed data files, or probabilistic choices are required.

A successful execution prints:

`VERIFY_OK; faces=(13,78,143,78), tetrahedra=C4:39+diamond:39, unimodular boundary ranks=(12,66,76), pi1=1, dual bettis=(0,1,2)`

The checker reconstructs all thirteen graph vertices and all seventy-eight unordered pairs of graph vertices; tests the \((13,6,2,3)\) strongly regular parameters and induced six-cycle vertex links; classifies each eligible four-set and rules out five-faces; verifies every one of the \(8192\) subsets against the dual definition; applies the complete triangular presentation to kill all \(66\) fundamental-group generators; checks the two integer chain relations; and reduces signed integer boundary matrices by explicitly integral, unimodular operations. It rejects any nonzero residual block that would invalidate the claimed rank or torsion conclusion.

The exact finite calculation proves only statements about this specified graph. The dual wedge-of-spheres homotopy and the original cut-complex homology follow through the separately stated Hurewicz–Whitehead and combinatorial Alexander duality arguments. No independent audit is asserted.
