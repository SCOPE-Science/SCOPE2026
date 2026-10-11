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

# Reproduction

Run `python3 verify_chvatal.py` and `python3 crosscheck_homology.py` from the directory containing these files. Both programs use the Python 3 standard library only, with all graph data and mathematical checks embedded. Their verified final lines are:

```
CHVATAL_VERTEX_DICHOTOMY_VERIFY_OK orbits=4+8 chromatic=4_all_vertex_deletions=3 whole=S2 delete_A=point link_A=S1 delete_B=S2 link_B=point elementary_collapses=delete_A+link_B
CHVATAL_MOD2_CROSSCHECK_OK full_beta2=1 four_deletions_acyclic eight_deletions_beta2=1 four_links_beta1=1 eight_links_acyclic
```

The exact full-complex face vector is `(12,42,52,20)`; the representative Morse rows print `whole faces 126 pairs 62 incidences 320 critical {0: 1, 2: 1}`, `delete_A faces 99 pairs 49 incidences 243 critical {0: 1}`, `delete_B faces 98 pairs 48 incidences 239 critical {0: 1, 2: 1}`, `link_A faces 26 pairs 12 incidences 44 critical {0: 1, 1: 1}` and `link_B faces 27 pairs 13 incidences 47 critical {0: 1}`.

The primary verifier explicitly constructs the full directed incidence graphs and checks them acyclic, rather than inferring acyclicity from matched-pair counts. It also reconstructs actual legal elementary-collapse sequences for the two collapsible representatives. The secondary verifier reconstructs adjacency independently and checks reduced homology in characteristic two for all twelve deletions and all twelve links. This secondary test does not assert integral homotopy on its own. The proof uses discrete Morse theory and the canonical link-cone decomposition, not an external homology certification. Independent audit status: not performed.
