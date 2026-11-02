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

# Reproducible verification

Execute `python verify.py` with SymPy installed. This program was executed against the local packaged source: `Exact algebra and 1907 finite rational tests passed`.

The symbolic portion verifies for every symbolic \(k\) the affine fourth-return composition, repelling two-cycle coordinates, complementary-strip return formula and exact distance between the repelling pair and periodic intervals. The rational portion checks seven positive rational \(k>1\) values, full endpoint conventions, exact four-cycle identities, strip-preimage lengths for ten survival depths, special boundary trajectories and transient entrance for many rational initial points. All arithmetic in the rational tests uses `fractions.Fraction`.

These computations test formulas and implementations but cannot establish the quantified theorem for all real parameters and all initial conditions. The proof's interval exhaustiveness, expanding survivor exclusion, and recurrence decomposition establish those global assertions independently.

The literature novelty assessment is self-review only; it is not an independent audit or a guarantee that unindexed earlier literature contains no equivalent statement. The original 2021 full text and a 2022 comparative chapter were inaccessible beyond partial public material.
