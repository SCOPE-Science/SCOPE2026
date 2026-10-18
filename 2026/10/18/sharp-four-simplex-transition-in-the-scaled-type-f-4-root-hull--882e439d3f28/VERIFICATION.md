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

# Reproduction protocol

From the same directory as `RESULT.md`, run `python3 verify.py`. The Python program uses only the standard library. It checks all 178365 anchored five-root configurations using exact integer determinants and algebraic comparisons in \(\mathbb Q(\sqrt2)\), then checks all 42504 pure-long five-sets, their 48 maximizers, their pairwise four-vertex nonincidence, the explicit orthogonal short-long duality, and the three pure-short symmetry orbits of size 16 each.

Independently run `c++ -std=c++17 -O2 verify.cpp -o verify_f4 && ./verify_f4`. The C++ verifier independently computes integer determinants by permutation expansion; its five count groups, extremal determinants, and mixed-configuration strict gap agree with Python. Reproduction does not require internet access or downloaded primary papers.

The unrestricted optimum depends additionally on the self-contained vertex-optimization and rigidity proofs in `RESULT.md`. Finite calculation verifies every root-set case but cannot itself establish an optimization theorem over continuously many points. There is no independent audit of this finding.
