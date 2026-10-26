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

Run `python3 verify.py` in a directory containing the embedded `verify.py`; no third-party libraries or network connections are needed. The exact output used for comparison is in `verification_output.txt`. The verifier generates graph neighborhoods of cyclic offsets \(\pm1,\pm2\), evaluates the fort condition directly on a bitset, separately tests the cyclic-gap characterization, and enumerates all subsets through the proposed minimum size.

Verified: 32,695 nonempty labeled subsets for \(6\le n\le14\) satisfy the exact gap criterion; 3,264,250 subset candidates of cardinality at most \(\lceil n/3\rceil\) for \(6\le n\le24\) contain no smaller forts and exactly the predicted number of minimum forts. The ten-vertex class with four-gaps has exactly five labeled members. Full recorded output ends in `ALL_CHECKS_PASS`.

Unproved by computation: the complete assertion for all larger \(n\). The unrestricted mathematical proof is the local-gap analysis, the incidence inequality, the equality-pattern classification, and rooted-word counting in RESULT.md. The checks do not independently establish bibliographic priority, authorship, or external mathematical validation.
