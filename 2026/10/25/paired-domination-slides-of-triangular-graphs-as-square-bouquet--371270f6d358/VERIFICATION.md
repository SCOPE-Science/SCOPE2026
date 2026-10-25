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

# Reproducibility and verification scope

The deterministic standard-library Python checker is `verification_direct.py`. Execute `python verification_direct.py` in the directory containing the extracted files; its expected output is `direct_output.txt`.

The alternate C++17 checker is `verification_independent.cpp`. Compile with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verification_independent.cpp -o verification_binary` and run `./verification_binary`; compare its output with `independent_output.txt`.

The Python method enumerates all candidate four-edge selections from the 21 edges of \(K_7\), tests dominance and paired feasibility, and independently constructs all star-forest states. The C++ method recursively enumerates unordered triples with centers, encodes each selection as a bit mask, and constructs edges by attempting every intersecting-edge replacement rather than relying on the local move theorem. Both methods perform exact breadth-first searches for \(n\in\{4,7,10\}\).

The independent computations both report \(12,630,75600\) configurations and \(24,2520,453600\) reconfiguration edges for these orders. The C++ enumerator additionally counts \(8,840,151200\) triangles. Root-distance histograms, listed in `RESULT.md` and in the output files, sum to the complete state counts. Vertex transitivity, established in the written proof, converts these root eccentricities into exact graph diameters.

The all-order structural statements rest on the direct mathematical argument. Computed cases are not an all-order proof of diameter values; no exact diameter is claimed for \(n\ge13\). External scientific audit remains unperformed.
