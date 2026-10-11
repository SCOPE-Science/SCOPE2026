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

# Reproducibility and checks
Run `python3 verification.py`. The program uses the Python standard library only and deterministically reconstructs the fifteen nonempty tetrahedral faces and all 28 Hasse cover edges. It enumerates every nonempty matching, tests directed acyclicity with a topological sort, independently re-enumerates fixed orbit-block matchings for each permutation class, and evaluates signed simplex traces.

The exact observed totals are 14,720 ordinary Hasse matchings, 12,820 acyclic matchings, and face vector `(28, 300, 1544, 3932, 4632, 2128, 256)`; the five classwise ordinary Lefschetz numbers are `(100, 2, 0, 1, 0)`. The fourth-homology character is obtained by subtracting the degree-zero character. All 24 permutations satisfy their class identity, all character inner products yield nonnegative integers, and the program emits `VERIFY_OK` on success.

The homology concentration \(\widetilde H_4\cong\mathbb Z^{99}\), and its vanishing in all other degrees, are supplied by Scoville, arXiv:2604.18172v1, Table 2 and Theorem 20. The enumerator checks the independent face vector and Lefschetz calculations but does not rederive integral Smith normal forms for the homology concentration. It establishes no assertion beyond the specified finite tetrahedral complex. The rational Specht decomposition is the mathematical claim; no independent audit has been performed.
