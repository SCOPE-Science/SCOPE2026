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

# Verification protocol

Run `python verify.py` using Python 3 and the NetworkX and SymPy libraries.

The program constructs all graph vertices, edges, independent simplices and all graph automorphisms from the definitions. It checks the face vector \((16,96,272,376,240,72,16,2)\), the augmented mod-\(101\) boundary ranks \((1,15,81,191,181,58,14,2)\), and an explicit integral four-cycle with \(100\) terms. The cycle boundary vanishes over the integers. Exact SymPy rational ranks are \(58\) for the degree-five boundary and \(59\) when adjoining the cycle, establishing rational nontriviality.

For all \(96\) graph automorphisms the program checks that the induced action on the top class is the bipartition sign and that signed simplicial Lefschetz traces equal the derived full-group formula. It checks the cube quotient, the induced \(S_4\)-action on four antipodal pairs, the two-element kernel and the three quotient fixed-subspace dimensions.

The homology result is rational. The checker does not claim an integral equivariant representation classification, an all-parameter theorem, or independent external validation.
