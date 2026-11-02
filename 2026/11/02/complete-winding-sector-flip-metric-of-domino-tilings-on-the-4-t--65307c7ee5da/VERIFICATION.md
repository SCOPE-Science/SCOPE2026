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

# Reproducibility and bounds

Every new numerical statement can be recomputed without retrieving external datasets. With Python 3, run `python3 verify_primary.py`. With any C++17 compiler, run `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`.

The first executable exhaustively generates all perfect matchings recursively by the smallest uncovered cell, independently constructs the 24 elementary torus face flips and all connected components, then performs BFS from all 3,108 states. It reports the 15 signed-flux sectors and their exact statistics. It stops with `PRIMARY_CERTIFICATE_OK` after testing all its accounting assertions.

The second executable generates matchings as injective assignments from 12 black cells to white neighbors, encodes them in a different representation, constructs each face transition by exchanging partners of opposite black corners and independently BFSes from all configurations. It stops with `ALTERNATIVE_CERTIFICATE_OK` after comparing size, flip edge count, component profiles and total within-component shortest-path sum.

All 15 full distance histograms of the two extracted executable implementations were compared to `sector_metrics.json`. The 163 nonzero sector-distance bins, sector radii, diameters, edge counts and Wiener values agreed exactly. Every component's ordered-pair histogram has total equal to the square of the component size. Both programs reconstruct their adjacency lists and distances; the sector JSON file is not a hidden dependency.

The proof is exhaustive **only** for the precisely defined finite torus and local move. Numerical evidence here has no bearing by itself on larger tori, arbitrary topological surfaces, or Markov-chain mixing. External independent scientific validation has not been performed.
