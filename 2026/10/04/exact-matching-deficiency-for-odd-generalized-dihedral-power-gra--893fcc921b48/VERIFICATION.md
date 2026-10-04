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
The proof was reconstructed directly from the generalized-dihedral multiplication law and from the definitions of the power and enhanced power graphs.

Exact symbolic checks:
- Every element \(at\) in the nontrivial coset satisfies \((at)^2=1\).
- A coset involution has no power-graph neighbor except \(1\).
- Enhanced adjacency would force commutation; inversion excludes commutation with a nonidentity element of the odd-order kernel, and two distinct coset involutions cannot commute.
- The nonidentity kernel elements split into disjoint inverse pairs, each of which is an edge.
- Since all coset vertices have the same unique neighbor, at most one of them can occur in a matching, giving the sharp upper bound.

`artifacts/verify.py` constructs the groups from the semidirect-product law for kernels \(C_3\), \(C_5\), \(C_9\), and \(C_3\times C_3\). It constructs both graphs from first principles, checks the pendant-coset property, and computes maximum matchings by exact bit-mask dynamic programming. The replay returns `VERIFY_OK`.

Finite computation is not used to justify the universal statement.
