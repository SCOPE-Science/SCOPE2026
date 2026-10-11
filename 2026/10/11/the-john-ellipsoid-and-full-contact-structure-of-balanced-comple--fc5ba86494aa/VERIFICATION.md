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

`CHECK.py` requires Python 3 and only its standard library. From the directory containing this file and `CHECK.py`, run `python CHECK.py`. The expected successful completion is `EXACT_PASS cases= 16 coordinate facet contacts= 100 transversal facet contacts= 494 all first/second John moments`. The script forms exact rational-quadratic-field matrices and checks coordinate and clique tangencies, positive moment weights, and both John moment identities, including the full second-moment matrix.

The tested pairs have \(1\le a\le4\), \(1\le r\le4\). Values below the asserted range \(a\ge2\), \(r\ge3\) are arithmetic boundary calibrations, not extensions of the stated theorem. Computational tests do not establish correctness at larger parameters. The unlimited-parameter result and strict eigenvalue ordering follow from the symbolic proof in `RESULT.md`. No independent external audit has been performed.
