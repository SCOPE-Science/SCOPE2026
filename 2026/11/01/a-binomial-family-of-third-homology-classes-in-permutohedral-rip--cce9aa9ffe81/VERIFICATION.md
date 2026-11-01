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

# Reproducibility checks

From the directory containing the attached files run `python3 verify_rips.py` and `python3 verify_independent.py`. Both use only the Python standard library. The first builds the adjacent-swap Cayley graph, its distance-two square, all maximal cliques and every subface, and calculates all mod-two simplicial boundary ranks. It checks expected maximal-clique counts as well as the complete face and boundary-rank vectors for \(1\leq n\leq6\). The second independently uses discordant-pair distances, direct clique recursion, and **row-based** binary elimination for \(n=5,6\).

The verified six-letter finite data are \(720\) vertices, \(6840\) edges, \(15360\) triangles, \(12060\) tetrahedra, \(4320\) four-simplices and \(720\) five-simplices. The ranks of successive boundaries in degrees one through five are \((719,6121,8370,3600,720)\). In particular the third reduced mod-two Betti number is \(12060-8370-3600=90\), and the second is \(15360-6121-8370=869\). At five letters, the corresponding third homology is zero.

Both exact finite programs were run from the attached package inputs, and their outputs were captured in `verification_output.txt`. Their computations are proofs of the stated finite ranks. The argument for all \(n\geq6\) is separately established by the deletion/insertion factorization in `RESULT.md`; no experiment at larger sizes is treated as a proof. No independent external audit was conducted. Integral, rational, equivariant and other-scale claims are outside the verified domain.
