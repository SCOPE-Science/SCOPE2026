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

# Verification and limits

The standalone `verify.py` is independent executable Python 3 using only the standard library. It performs three substantive checks: (i) computes all eight exact Venn multinomial orbit contributions; (ii) compares the resulting triple coefficient with a separate two-block-anchored count for every integer \(4\le r\le25\); (iii) directly enumerates all \(126\) vertices of \(K(9,4)\), all compatible pairs, all compatible triples, and their eight orbit profiles using bit intersections. The output ends `VERIFY_OK` when every assertion holds.

The direct small-graph count is \(6,300\) compatible unordered pairs and \(163,800\) compatible unordered triples. The polynomial's \(r=11\) cubic coefficient is \(9,693,705,696,717,042,000\). Finite checks do not certify the infinite theorem: its universal argument rests on exact neighborhood geometry, the impossibility of four selected sets, and the multinomial decomposition of all admissible triples. No independent validation is asserted.
