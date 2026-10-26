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
# Reproducibility and limitations

All C arithmetic is exact over the field with two elements; the two implementations generate congruence orbits through different generating systems. Each identifies the same 13 representatives and 9,999,360 invertible matrices. Independent GF(4) evaluation checks five projective parameter values per line and thereby proves vanishing of each restricted degree-three polynomial. The direct F2 coefficient criterion independently produces identical counts. No sampling and no probabilistic primality or numerical approximation are used.

To reproduce: compile `verification/census.c` and `verification/crosscheck.c` with `cc -std=c11 -O3`, run each, and compare with the embedded expected text outputs. Execute `python3 verification/lines_gf4.py` and compare with `verification/lines_gf4.expected.txt`. The line condition concerns scheme containment, not just rational point membership.

The computational proof depends on the transparent finite enumeration and the stated generator-group lemma; no external certificate of independence or expert validation is asserted. The historical 13-class congruence count is acknowledged as prior work. The stated scientific limitations and unreviewed source-access risk remain.
