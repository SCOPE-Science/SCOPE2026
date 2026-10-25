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

# Reproducible mathematical verification

Run `python3 verify.py` with Python 3.9 or newer (standard library only). The included `verification_output.txt` is the direct output from the same standalone script and is reproducible.

For every \(m\in\{1,2,3,4,5\}\) and \(k\in\{4,5\}\), the program constructs the bouquet graph, computes \(\alpha(G[S])\) exactly for all vertex subsets by recurrence, reconstructs its robust-clique faces, and checks all faces outside the central link are partitioned among the interiors of \(\binom m{k-1}\) explicitly constructed balls. It checks each ball intersects the link in exactly the claimed join boundary, and that pairwise intersections of distinct balls stay in the link. For \(k=4\) it performs exact mod-two boundary-rank reductions and verifies the complete reduced Betti vector against the claimed sphere-wedge ranks.

These enumerations cover at most 16 vertices and do **not** establish the infinite family alone; that is proved by the exact face characterization and CW cofiber quotient in `RESULT.md`. No integral Smith computation is needed, since the quotient explicitly exhibits the integral homotopy type. No independent external audit or formal proof certification was performed.
