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

# Computational checks and scope

Execute `python3 verify_retraction_graph.py` with standard Python 3.8+; no third-party packages are required. Its projective line normalizations and rank-one outer-product matrices enumerate the graph for nine combinations \(q\in\{3,5\}\), \(n\in\{3,4\}\) and selected isotropic/nonisotropic \(u\) under standard dot product. For each pair it checks the defining commute equation by explicit matrix multiplication. Additional full linear-map enumeration at \((q,n)=(3,3)\) examines all \(3^9\) matrices for each of three \(u\), verifies idempotence, rank one, and the algebra-homomorphism law for all basis pairs, then compares exact sets with projected image/kernel construction. The verification command completed with `VERIFY_OK 9 graph configurations and 3 all-linear-map checks`.

Sample independently computed graph sizes: for \((q,n)=(3,3)\), \(u=(1,0,0)\) gives \((12,4)\) and \(u=(1,1,0)\) gives \((12,5)\); for \((q,n)=(3,4)\), \(u=(1,0,0)\) gives \((144,1026)\). These checks are exhaustive only in the stated finite test cases. The general odd-prime-power and arbitrary-dimensional assertions are established by the paper proof, not by finite runs. No independent mathematical audit has been conducted.
