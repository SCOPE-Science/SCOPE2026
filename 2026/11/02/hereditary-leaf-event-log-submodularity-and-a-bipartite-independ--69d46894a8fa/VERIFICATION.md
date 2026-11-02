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

Run `python verify.py` with standard Python 3. The program directly decodes Prüfer sequences, discards invalid multipartite edges, counts marked leaf events using decoded degrees, and checks every claimed event probability and pairwise all-set log-submodularity inequality for all unordered part-size profiles of total size three through seven. Observed: 36 part profiles, 64,538 admissible trees, 2,704 exact rational joint-event identities, 277,632 integer lattice comparisons; all passed. These checks do not prove the infinite all-size statement: the accompanying explicit counting argument and log-concavity proof do. Independent review has not been performed.
