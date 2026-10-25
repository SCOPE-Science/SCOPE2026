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

The reproducible script `verify_icosahedral_double_homology.py` completed successfully from the packaged path. It enumerates all 4096 vertex subsets, constructs 6504 inclusion maps, verifies every applicable composition of consecutive differentials is zero, and checks all 26 global differential matrices by exact integer unit-pivot reduction. Every reduction leaves an all-zero residual, so every nonzero Smith factor of each differential is 1.

For induced subcomplexes of the \(2\)-sphere, reduced \(H_0\) and \(H_1\) are torsion-free; reduced \(H_2\) is nonzero only for the full sphere. Exact Smith decompositions construct the integral bases for the nonzero reduced \(H_0\) and \(H_1\) groups. `COMPUTATION.json` records the resulting chain dimensions, ranks, and bidegrees.

Limitations: the computation establishes the integral double homology of this one complex only. It does not establish a general torsion-freeness theorem or classify other triangulations.

The trusted importer initializes absent external channels as unperformed; research never assesses or authors those channels or resets old evidence.
