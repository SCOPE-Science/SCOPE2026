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
# Reproduction and verification

Run `python verify.py` with Python 3 and NetworkX installed, in the directory containing this file and `verify.py`. Its two independent paths are (i) direct enumeration of all cliques in the explicitly generated partition-transfer graph for \(1\leq n\leq15\), and (ii) the all-partitions multiplicity statistic. It also checks published values for \(1\leq n\leq25\) and reports \(n=26\) as a new prediction. The finite checks cannot certify the infinite formula: the proof of the formula is Steps 1–5 of `RESULT.md`. The wedge-of-spheres classification is cited from arXiv:2603.14370, not independently reproved. No independent audit has been performed.
