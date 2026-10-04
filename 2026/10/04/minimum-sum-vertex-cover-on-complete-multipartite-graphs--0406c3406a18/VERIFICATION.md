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

The proof was checked against the defining edge-cover-time objective and against the equivalent prefix identity
\[
\operatorname{cost}(\sigma)=\sum_{k=0}^{N-1}|E(G_k)|.
\]
The critical inequality is the exact two-part transfer for maximizing the remaining-count squared sum under capacities. If remaining counts \(r_i,r_j\) with \(i<j\) are consolidated toward the larger-capacity part \(j\), the squared sum changes by either \(2r_ir_j\) or \(2(n_j-r_i)(n_j-r_j)\), both nonnegative. Repetition yields the largest-capacity-first remaining profile and therefore the smallest-part-first deletion profile.

`verify_complete_multipartite_msvc.py` then performs an independent finite replay from the definition. It enumerates every integer multipartition of orders \(2\) through \(8\), every labeled vertex ordering, every cross-part edge, and every cover time. It checks \(58\) graph types and \(925310\) orderings. It also verifies the complete-bipartite specialization and the illustrative value \(\operatorname{msvc}(K_{1,2,4})=26\). The stored replay output ends with `ALL CHECKS PASSED`.

The enumeration is finite and does not certify cases above order eight; those cases are covered by the proof, not by extrapolation from computation. Independent audit has not been performed.
