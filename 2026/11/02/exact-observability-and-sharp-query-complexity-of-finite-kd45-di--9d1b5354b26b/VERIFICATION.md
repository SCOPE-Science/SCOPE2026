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

The standalone standard-library Python script `checker.py` was executed directly using `python3 checker.py`. It returned `ALL_CHECKS_OK`, with two-agent pointed-profile counts \(1,2,7,26,91,302,967\) for carriers of sizes \(1\) through \(7\). It evaluated \(21{,}343\) ordered nonempty successor pairs in those cases and verified profile counts, zero-fiber sizes, complement symmetry, nonzero fiber sizes, and recovery from minimal positive inputs. It also evaluated \(50{,}001\) serial multi-agent successor-list configurations and the exact zero/separating witness pair through size four. Constant-row relations verify actual \(\mathsf{KD45}\) realizability.

The general adaptive lower bound is not certified by brute-force testing of every strategy; it follows from the all-zero adversarial path proof in `RESULT.md`. The historical novelty assessment is limited by incomplete access to a relevant 2018 full text. No external independent audit has been performed.
