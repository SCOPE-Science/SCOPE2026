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

# Reproducibility of the integral Petersen torus-lattice computation

Run `python3 verify.py` with a standard Python 3 interpreter. This is a standalone executable that requires no external files, packages, or network access.

The code enumerates the Petersen graph directly as the Kneser graph on the ten two-subsets of five symbols, then constructs its unordered two-particle cubical complex with cell counts \((45,120,75)\). It checks the full exact signed cellular boundaries and \(\partial_1\partial_2=0\), all 12 pentagons, all six vertex-disjoint pentagon pairs, and all six 25-square product torus cycles. It asserts the reoriented integral sum of the six cycles vanishes *as a chain*.

The code independently calculates the mod-three rank 70 (and mod-two rank 69) of \(\partial_2\). Combined with the five explicitly independent cycles, this pins down the rational rank 70 and the free integral kernel rank five. It computes exact determinants of all six column-deletion five-by-five minors of the displayed cycle-coordinate projection: `[-1, 1, -1, 1, -1, 1]`. Since those minors are unimodular, every five cycles generate the full integral kernel, without a rational-to-integral leap.

All 120 automorphisms of the five-symbol Kneser graph are applied at the fully signed integer two-chain level, confirming the six consistently oriented cycles permute without signs. All six Sylow-five subgroups are explicitly enumerated, and their orbits are checked to give six *distinct* disjoint-pentagon partitions. The nonsplitting argument uses transitive integral invariants rather than computational approximation.

Expected output from actual execution:

```text
VERIFY_OK PETERSEN_10_15 CELLS_45_120_75
PENTAGONS_12 DISJOINT_PAIRS_6 TWO_TORUS_SQUARES_25_EACH
SIGNED_BOUNDARY_SQUARE_ZERO TORUS_BOUNDARIES_ZERO INVARIANT_SUM_ZERO
RANK_B2_MOD3_70 MOD2_69 KERNEL_INTEGRAL_RANK5
FIVE_BY_FIVE_UNIMODULAR_MINORS [-1, 1, -1, 1, -1, 1]
ALL_120_S5_ACTIONS_PERMUTE_SIX_REORIENTED_TORI
SIX_SYLOW5_SUBGROUPS_BIJECT_TO_PENTAGON_PAIRS
H2_EQUAL_Z6_MOD_DIAGONAL ANY_FIVE_TORI_INTEGRAL_BASIS
```

The checks prove a finite exact topological-chain calculation and its integral equivariance for this one graph; they are not a general topological theorem about every graph. None of the checks establishes absolute publication priority or constitutes an independent scientific audit.
