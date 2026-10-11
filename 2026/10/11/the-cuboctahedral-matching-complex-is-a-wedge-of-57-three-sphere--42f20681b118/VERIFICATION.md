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

# Reproducibility and limits

Execute `python3 verify_cubocta_morse.py` and `python3 verify_cubocta_mod2.py` with Python 3.10 or later from the directory containing these two programs. No third-party packages, external data, or online requests are needed. Both executables fully reconstruct the graph and compute the claimed results; they terminate with an assertion failure rather than printing `VERIFY_OK` if a required invariant is false.

`verify_cubocta_morse.py` checks the 12-vertex and 24-edge graph, the complete 2648-face census, the 1287 Morse pairs, all 9936 oriented Hasse incidences, the acyclic topological ordering, and the exact signed 65-by-8 Morse attaching matrix. Its eight selected row masks yield a diagonal unimodular minor, proving rank eight and primitiveness over the integers.

`verify_cubocta_mod2.py` independently enumerates faces by combinations of the 24 graph edges and independently reduces the full mod-two simplicial boundary matrices. Expected consecutive boundary ranks are 23, 181, 563, 496 and 32. The resulting reduced Betti ranks are zero except 57 in degree three; these are a consistency check only.

The proof uses standard discrete-Morse CW equivalence and degree classification of maps to wedges of 3-spheres. Neither executable proves general statements about arbitrary planar graphs or scans all published literature. No independent scientific audit is represented by these checks.
