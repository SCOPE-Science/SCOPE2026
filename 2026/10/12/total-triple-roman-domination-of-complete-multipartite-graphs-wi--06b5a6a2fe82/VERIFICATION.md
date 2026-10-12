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

The theorem is proved analytically for arbitrary finite part sizes. The key reduced inequalities were re-derived directly from the definition: for a zero vertex in part \(V_i\), cancellation of one unit for each active neighbor gives \(E-E_i\ge3\); for a positive vertex of label below \(3\), it gives \(f(v)+E-E_i\ge3\). These reductions are the only nonstandard algebraic step in the lower bound.

The cited premises from the initiating paper were checked in accessible full text: the invariant definition, the general lower bound \(\gamma_t(G)+3\le\gamma_{[t3R]}(G)\), the characterization of value \(5\) by a universal vertex, and the nonexistence of value \(6\). The peer-reviewed article and the earlier public preprint agree on these points.

The bundled `verify_t3r.py` independently implements the definition. It exhaustively computes the minimum over all \(5^N\) labelings for each nondecreasing complete-multipartite profile with all parts at least two and \(4\le N\le8\), and checks the two general constructions on additional profiles. Passing these checks is supporting evidence only; the finite enumeration is not used to infer the infinite theorem.

Unproved limits: no claim is made about optimizer counts, part-size-one cases beyond the cited universal-vertex result, disconnected graphs, or other Roman-domination variants.
