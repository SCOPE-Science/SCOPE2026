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

Run `python3 verify_pappus_magnitude.py` in a standard Python 3 environment. No third-party modules are required.

The verifier performs the following exact checks:

1. Reconstructs the 18-vertex graph from LCF \([5,7,-7,7,-7,-5]^3\), checks 27 edges, cubic degree, girth \(6\), diameter \(4\), and distance shells \((1,3,6,6,2)\).
2. For every ordered endpoint pair \((x,y)\), enumerates all length-four magnitude chains in degrees \(2,3,4\).
3. Builds the magnitude boundaries over \(\mathbb F_2\) by deleting precisely the smooth interior points.
4. Verifies the chain condition on every endpoint block.
5. Computes exact boundary ranks by binary Gaussian elimination and checks the complete local data for each endpoint distance.
6. Sums endpoint blocks and checks global chain dimensions \((1296,2916,1458)\), boundary ranks \((1260,1404)\), and homology dimension \(252\).

A successful replay prints `VERIFY_OK`. The bundled `verification_output.txt` is the output from the checked package path.

The verification establishes only the stated finite \(\mathbb F_2\) claim. It does not certify integral torsion or other bidegrees.
