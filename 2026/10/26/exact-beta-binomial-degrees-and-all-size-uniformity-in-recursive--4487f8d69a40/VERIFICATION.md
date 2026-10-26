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

Execute `python verify_degrees.py` in Python 3. The standard-library-only checker uses exact fractions to enumerate the full state distribution of the recursive twin-duplication process through six vertices for \(q\in\{1/7,1/3,1/2,3/5,6/7\}\), recomputes sampled-vertex and founder degree histograms, and checks their beta-binomial formulas for every degree. It independently checks both stated distribution recurrences, with exact rational arithmetic, through size \(45\) at the same five join probabilities.

The program completed with `PASS 10821 exact assertions on finite graph distributions and recurrences`. These finite checks do not prove the infinite statement; the proof in RESULT.md matches recurrences analytically and uses the beta-mixture law. The result does not validate a quenched empirical degree law. Independent audit: not performed.
