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

The verification artifact `verify.py` performs two independent finite checks of the derived enumeration. First it explicitly constructs canonical rooted non-plane trees by enumerating all set partitions of each labelled leaf set into two or three child blocks and recursively combining the resulting subtrees. Second it computes the coefficients from the species recurrence and from the Lagrange-inversion formula. The three routes agree through seven explicitly generated leaves and through ten recurrence/coefficient terms. It checks the displayed orbit profile and the four-label anchor of three binary splits plus one 4-star.

Replay command: `python3 verify.py`. Expected terminal line: `VERIFY_OK`.
