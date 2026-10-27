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

# Verification and limits

Execute `python verify.py` from the directory containing the supplied files. Standard Python 3 is the only runtime dependency. The checker enumerates every set partition on up to eight labelled elements and, separately, all pairs of set partitions through six elements. It tests exact induced partition probabilities, exact pair factorial moments, exact restricted class first moments, and exact two-agent triple and wedge means. It does not establish asymptotic independence or finite-model limit laws; those rely on the stated factorial-moment and finite-rank logical proofs. Independent audit has not been performed.
