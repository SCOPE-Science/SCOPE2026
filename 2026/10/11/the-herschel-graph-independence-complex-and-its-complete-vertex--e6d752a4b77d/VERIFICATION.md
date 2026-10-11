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

# Reproducibility and actual mathematical checks

Execute the two included standalone Python 3 scripts directly. Both use only the standard library and all graph and simplicial data are specified in the scripts, not fetched from a network or another package:

```
python3 verify_herschel_morse.py
python3 verify_herschel_homology.py
```

The discrete-Morse verifier enumerates all independent subsets of the eleven-vertex graph and each induced deletion and closed-neighborhood deletion. It checks each matching pair is an unused codimension-one face incidence. The complete directed Hasse diagram is constructed, reversing each matched incidence and orienting each other incidence downward, and acyclicity is proved by visiting all nodes in a topological sort. Critical-cell histograms for all 23 complexes are asserted exactly. For the two collapsible deletions it independently constructs full elementary collapse sequences and checks the free-face property at every step. Expected terminal marker: `HERSCHEL_MORSE_OK 23 faces 1465 incidences 3644 pairs 709`.

The independent chain verifier reconstructs the adjacency relation from a separate dictionary, verifies symmetry, derives the characteristic polynomial from integral power traces, enumerates all independent sets recursively (rather than by scanning all bitmasks), and computes every mod-two reduced boundary rank. For the full graph, it obtains the f-vector \((11,37,45,22,7,1)\) and augmented boundary ranks \((1,10,27,16,6,1,0)\). Expected terminal marker: `HERSCHEL_HOMOLOGY_OK 23`.

The homotopy proof is the complete acyclic-Morse reduction with one zero-cell and only one- or two-dimensional critical cells. Mod-two homology alone cannot establish that proof or integral torsion-freeness. The presented computation is a finite exhaustive verification of the exact displayed graph, not an infinite classification.
