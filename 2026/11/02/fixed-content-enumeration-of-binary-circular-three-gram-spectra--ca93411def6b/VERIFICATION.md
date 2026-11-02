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

# Verification record

Run `python3 verify_profiles.py` with Python 3 and no external dependencies. The executable independently computes circular three-factor multisets by direct indexed windows, checks all fixed-content coefficients through length eighteen, realizes all nonnegative connected flows through length twenty-two using an Eulerian algorithm, and verifies the sharp collision boundary and padding witnesses. Actual replay: `VERIFY_OK; direct_words=524286; constructed_profiles=4654; n<=18; constructions<=22; padded_pairs<=26`.

The analytic enumeration uses balance equations plus connectedness of the positive-edge de Bruijn multigraph. The rational generating functions and asymptotic law are proved symbolically in `RESULT.md`; finite enumeration is supporting evidence only. The specializations and the first-collision argument use all cyclic windows, including wraparound for very short words. No independent audit, formal proof assistant or external certification is claimed.
