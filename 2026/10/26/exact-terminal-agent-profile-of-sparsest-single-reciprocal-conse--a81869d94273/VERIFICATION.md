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

# Reproduction and limits

Run \(`python3 verification.py`\) in a standard Python 3 environment. The script computes integer recurrence values, generates labeled directed graphs via every allowed order (deduplicating edge sets), verifies histogram formulas, and independently checks every graph candidate for the fixed dyad on three, four, and five agents by reverse-removal. The six-agent generation has 25392 unique graphs and verifies all four terminal-agent counts. It prints \(`ALL OK`\) on success. No packages, downloads, randomness, or external input files are needed.

These checks have been performed against the same content as the packaged script. They cover specified finite sizes only; the proof in RESULT.md supplies the all-sizes argument. The comparison with pre-existing A103353 totals is deliberate and explicitly disclaims novelty for those totals. Independent audit is not performed.
