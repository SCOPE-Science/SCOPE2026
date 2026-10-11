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

Run `python3 artifacts/verify.py` from the package root. The verifier reconstructs the 18-vertex, 27-edge LCF graph, forms the all-vertex-reduced Świątkowski particle-weight-three boundary, and checks the certified kernel vectors.

The decisive proof check is two-sided: rank modulo 3 is 6521, which forces rational rank at least 6521; seven independent integral kernel vectors force rational nullity at least 7 and hence rational rank at most 6521. Therefore the top kernel has rank 7. Because there is no degree-four chain group in particle weight 3 and the integral kernel is a subgroup of a free abelian group, the claimed integral group is free of rank 7.

The verifier also checks the edge count and valencies, the chain-group ranks, the relation `d2*d3=0`, and the degree-three boundary ranks modulo 2, 3, and 5. Finite-field ranks other than modulo 3 are consistency checks, not substitutes for the exact rank sandwich.

No claim is made about lower integral homology or torsion outside the top degree.
