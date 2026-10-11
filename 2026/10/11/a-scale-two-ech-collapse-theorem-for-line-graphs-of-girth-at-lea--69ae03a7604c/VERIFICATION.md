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

Run `python verify.py` using Python 3 and its standard library only. All code and definitions are included; no network access or supplementary files are needed.

The verifier independently builds the original graph's edge stars, the line-graph closed-neighborhood facets at scale two, and the full nonempty face sets. For each tested case it checks that every face outside the clique complex belongs to exactly one such facet and that toggling its unique central edge partitions the excess faces. It then removes paired faces in descending order of lower-face size, checking that each lower face has exactly one remaining strict coface. The surviving simplices must be exactly the flag complex. Euler-characteristic and degree-count kernel identities are also checked.

Tested graphs: a seven-vertex path; a five-cycle; a five-leaf star; the Petersen, Heawood and dodecahedral graphs; and two pentagons sharing one vertex. The script additionally confirms that the scale-two Čech nerve of a four-cycle is the boundary of a tetrahedron. Successful execution prints `VERIFY_OK`.

The finite tests do **not** prove the universal claim. The universal proof is the unique-connector lemma plus an explicit acyclic sequence of free-face removals; the graph nerve and integral cycle lattice arguments finish the proof. No independent audit has been performed.
