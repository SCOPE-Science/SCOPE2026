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

Run `python3 verify.py` with Python 3 standard library. Its expected output is:

`VERIFY_OK q=3:9 q=9:63; each ordered two-symbol descendant occurs exactly twice`

The code builds the unique triple on three symbols and the twelve affine lines on nine symbols, selects a parallel class, checks block-pair uniqueness, counts all transmitted words, and enumerates every distinct one-deletion output. It rejects repeated codewords, missing pairs, or any output supported by a number of codewords other than two. This is an exact finite check for those two designs only. For arbitrary admissible \(q\), mathematical verification is the incidence proof plus the established Kirkman-system existence theorem. Other congruence classes and uniqueness up to design isomorphism remain outside the theorem.
