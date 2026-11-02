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

# Computational verification

Execute `python3 verify.py` with the standard Python library. It constructs the graph edge sets explicitly, verifies every vertex has degree three, counts efficient dominating vertex sets directly by examining each closed neighbourhood, and separately counts two-colour assignments by examining the four edges adjacent to every edge. The tests include the named graphs K4, K3,3, triangular prism, cube, four-rung prism, the eight-vertex Möbius ladder, the Petersen graph and the twelve-vertex Möbius ladder.

Further checks independently enumerate all 70 labelled cubic graphs on six vertices, and evaluate the efficient-code count on Möbius ladders from half-length 2 through 8. Successful completion prints `VERIFY_OK`. The code contains no imported result or precomputed certificate for the general bijection. These finite experiments are checks and do not prove the infinite case.

# Mathematical verification boundaries

The proof of the bijection is the case analysis on two-colour incident-degree profiles, followed by a constructive reverse mapping. The classification of cubic vertex-transitive graphs of order a power of two relies on the published Knor–Potočnik Theorem 1.2. The Möbius count relies on their Lemma 2.2 and its propagation proof, plus a straightforward incidence double count. Neither the classification nor complete historical priority is independently certified by this script. Independent audit remains not performed.
