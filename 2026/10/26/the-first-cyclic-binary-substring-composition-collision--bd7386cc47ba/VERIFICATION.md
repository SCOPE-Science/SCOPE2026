---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The measurement counts all starts including wraparound and repeated windows. Rotation/reversal preserve it; complementation is not factored out. Complementary windows pair weight a at length k with R−a at length n−k, where R is total weight. My exhaustive replay marked rotations and reversals from each first unvisited binary string and grouped the resulting bracelets by separately sorted full-length window-weight lists, computed by prefix sums on the doubled word. Through n=11 there was no collision. At n=12 there were 224 bracelets and 223 observations, with sole nonsingleton class {001011001101, 001011010011}. Separately grouping by the complete ordered-lag two-point vector reproduced all 23 pairs in the CSV and the (length, count) breakdown (0,1),(3,17),(4,3),(5,2). Expansion of each squared window sum gives F_k=kR+2Σ_{d=1}^{k−1}(k−d)C_d, so second differences recover each C_d; there is no converse. A window of length 12q+s in either r-fold power adds 6q to the corresponding remainder weight and each base start occurs r times. A dihedral equivalence of the powers would restrict on twelve consecutive letters to one between the bases. This proves repetition for all r, not other lengths. Replay: python3 /workspace/review-replay.py 3 with the original homometric_pairs_n12.csv path as its argument.

## originality

PASS

The known homometry census accounts for the 23-pair baseline, not the reconstruction threshold or the unique collision for full cyclic window weights. Linear equicomposability and cyclic profiles at fixed short widths are different measurements. The expanded Resultary record 8e493cc5d8d2 uses the same full measurement and contains the same finite threshold, census and pair, plus new lengths. It is indexed under 2026-11-02, after the frozen 2026-10-26 entry. This establishes substantial catalogue overlap, but not a covering predecessor or the provenance of either derivation. The pass credits the finite full-histogram classification against established earlier work, not the baseline or an absolute priority claim.

## value

PASS

The first loss of reconstruction for the complete cyclic measurement is a natural cutoff, with meaningful distinction from the older two-point measurement. Identifying the sole failure at that cutoff makes the refinement quantitative and exposes exactly which ambiguity remains; the all-multiples construction shows it persists. The known 23-pair baseline alone would not justify value, and no all-length classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
