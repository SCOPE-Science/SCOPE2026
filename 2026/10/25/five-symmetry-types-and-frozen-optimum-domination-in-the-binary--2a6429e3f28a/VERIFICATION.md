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

# Reproducibility

Execute `python3 verify.py --exhaustive` with Python 3.8 or later; it requires only the standard library. This enumerates all 1,820 candidate four-sets of each parity, validates the ten-subspace coset descriptions, builds all 1,600 optimal total dominating sets, and tests perfect matchings using all 24 bijections between chosen parity blocks. It also enumerates 32 bitmask translations times 120 coordinate permutations, reconstructs all five global orbits and checks the independent 48-element parity-preserving stabilizer of a fixed block.

The direct exhaustive mode additionally scans every \(\binom{32}{8}=10{,}518{,}300\) labeled eight-vertex subset using graph adjacency, without assuming the parity-plane description, and confirms exactly 1600 are total dominating. An explicit scan finds zero legal single-token exchanges. The saved program printed `PARITY_FOUR_SETS_OK`, `OPTIMUM_COUNTS_OK`, five `ORBIT_OK` lines, `FIXED_PARITY_STABILIZER_OK`, `EXCHANGE_OK`, `FULL_8_SUBSET_EXHAUSTIVE_OK`, and `ALL_VERIFY_OK` on actual execution.

The analytical lower bound, structural characterization and exchange-isolation proof are in `RESULT.md`. No formal proof-assistant certification or independent human validation is claimed. Numerical checks establish only the specified finite graph.
