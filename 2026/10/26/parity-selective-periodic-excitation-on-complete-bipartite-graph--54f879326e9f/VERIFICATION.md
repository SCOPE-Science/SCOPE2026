---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The synchronous update sends nonzero states up cyclically and the resting zero to 1 iff the opposite part is excited. A nonzero color cannot vanish before its forced procession ends; counting excitations over a periodic orbit enforces e_A(t)<=e_B(t-1)<=e_A(t-2), and the symmetric inequality. Periodicity then forces either both parts excited at every step (q-phase waves), exactly alternating active steps with an m-color two-step return cycle (2m phases), or no excitation (all-rest). Each nontrivial orbit requires full occupation of its prescribed residue palette on both parts, yielding surjection counts U_q and U_m; no lower periods remain because a progressing vertex visits each required color. The original proof gives these implications over all a,b,q. Independent complete functional-graph enumeration of 54 finite parameter triples classified 3434 periodic configurations and matched the formulas exactly.

## originality

PASS

The GHM and its multicolor lattice dynamics are established (Durrett–Griffeath 1993); the three-color graph theory of Gravner–Lyu–Sivakoff does not state this all-q labelled census on K_{a,b}. Published complete multipartite parity automata use binary parity rather than resting/refractory GHM. No located primary source implied the full equality of recurrent-state sets, strict orbit lengths, or zeta factors. Best-of-knowledge new structural enumeration, with unindexed dynamical catalogues a residual risk.

## value

PASS

Full recurrent-state and dynamical-zeta classification for a natural bipartite mean-field excitable network gives a sharp phase palette threshold and odd-q period q+1 not predicted by the three-color case. Structural theorem extends to arbitrary q and part sizes, not a brute-force finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
