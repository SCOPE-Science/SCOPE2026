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

# Reproducibility and verification

Use Python 3 with no third-party packages: `python3 verify.py`. The output should reproduce the adjacent `verification_output.txt` file, including `VERIFY_OK`. The script constructs a proper vertex coloring with distinct equal-sized binary codewords, assigns directed incidence colors from the corresponding ordered differences, and examines all ordered directed two-paths. It independently implements the paired construction: matching partner arcs use a distinguished last color and all interpair arcs use coordinate differences.

The finite runs include complete graphs using middle-layer code sets at palette sizes two through eight, the paired construction for palettes one through eight (including the five-color twelve-vertex instance), and path/cycle instances on up to thirty original vertices. In total, 16,320 directed incidences and 819,942 ordered path constraints were checked. The executable includes assertions about all arcs having palette colors and about every ordered two-path having different consecutive incidence colors.

The proof of correctness for arbitrary graph size, the bipartite-cover lower bound, and the asymptotic upper coefficient are mathematical arguments in `RESULT.md`. No finite test certifies the infinite quantifiers, the absence of undiscovered prior work, or independent validation. The relevant 2023/2024 Priyamvada–Panda paper was not available in full text for statement-by-statement comparison.
