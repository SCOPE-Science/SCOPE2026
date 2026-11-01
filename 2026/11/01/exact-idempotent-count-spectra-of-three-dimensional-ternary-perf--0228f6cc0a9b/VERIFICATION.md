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

# Reproducibility and limits

The included `census.py` is self-contained Python 3 standard-library code. Run `python3 census.py` in the directory containing it; the asserted output starts with `VERIFY_OK`. The companion `census_output.txt` records one actual completed run.

The code enumerates all \(3^9=19683\) matrices, identifies the \(11232\) invertible ones with both a determinant test and rank elimination, solves the quadratic idempotent equations in two ways (all \(27\) vectors and seven nonempty support indicators), and checks simplicity by two independent graph-reachability methods. Orbit counts are checked both by stabilizer/Burnside weights and by explicit disjoint orbit enumeration for the full \(48\)-element monomial basis-change group. The checker confirms the four histograms, representative matrices, and the mean-one consistency identity. Exact integer arithmetic is used throughout.

This is a finite exhaustive certificate, not an infinite general proof, a formal proof-assistant certificate, or independent validation. The literature search cannot exclude an unindexed or implicitly stronger earlier theorem; the manuscript identifies the known unstratified orbit total separately.
