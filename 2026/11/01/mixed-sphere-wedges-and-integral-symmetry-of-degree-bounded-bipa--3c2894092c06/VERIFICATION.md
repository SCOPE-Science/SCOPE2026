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

# Reproducibility and checked limits

The standard-library script `verify_bipartite.py` enumerates the simplices of the exact vertex-set complex from the bounded induced-degree condition. For \((m,n,r)=(3,3,2),(4,4,2),(4,5,2),(5,5,3)\), it constructs every simplicial boundary and compares ranks over both \(\mathbb F_2\) and \(\mathbb F_3\) with the homology predicted by the analytic theorem. For \((3,3,2),(4,4,2),(4,5,2),(4,4,3)\), it enumerates all part-preserving permutations and, when the parts are balanced, all part-exchanging permutations, calculating orientation signs on every fixed simplex and checking the reduced Lefschetz numbers against the two integral module characters. The finite output is in `verification_output.txt` and finishes with `VERIFY_OK`.

The proof of the infinite-family claim does **not** follow from the computations: it uses the exact face decomposition, integral simplex-skeleton chain contraction, nullhomotopic inclusions and the integral long exact sequence of a pair. Mod-prime agreement alone cannot exclude arbitrary torsion, but the proof supplies a free integral lattice model. The check does not establish novelty in every unindexed source or any external independent mathematical certification.
