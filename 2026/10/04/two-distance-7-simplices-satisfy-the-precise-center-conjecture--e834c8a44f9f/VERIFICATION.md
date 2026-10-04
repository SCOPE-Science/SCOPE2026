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

Run `python3 verify.py` with a standard Python 3 interpreter. A successful replay prints `VERIFY_OK` followed by the exact census totals.

The verifier is deterministic and uses only integer arithmetic for the scientific certificates. It enumerates all labeled degree-two and degree-three regular graphs on eight vertices, proves that the listed relabeling orbits are pairwise disjoint and exhaustive, and checks vertex-transitivity by exact automorphism search over all \(8!\) permutations.

For each of the four non-vertex-transitive graph types, it constructs the Cayley--Menger matrix of every facet and evaluates its determinant with fraction-free Bareiss elimination. The determinant has degree at most \(6\) in the squared-length ratio \(t\), so equality with a proposed degree-at-most-six factorization at seven distinct integer values certifies the entire polynomial identity. The script checks the required facet formulas and determinant-difference factorizations exactly.

The proof then uses only these certified identities and elementary algebra over the real domain \(t>0\). For two distinct lengths \(t\ne1\); the only alternative common factor \(t^2-3t+1\) makes the relevant Cayley--Menger determinants vanish and is therefore incompatible with a nondegenerate simplex. No numerical search, floating-point tolerance, or finite sampling is used to infer the infinite theorem.

Limit: the verifier certifies only the two-distance dimension-\(7\) theorem stated in the package. It does not address simplices with three or more edge lengths or higher dimensions.
