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

The finite part of the proof can be reproduced with `python3 verify.py` using Python's standard library. On the packaged script, execution produced:

`CERTIFICATE_OK selections=65536 strict=65534 exceptional=2`

The program enumerates all \(4^8\) radius assignments, excludes only the two specified alternating-parity cases, and verifies strictly positive leading principal minors for the other \(65,534\) integer matrices corresponding to the rational spectral ceiling \(317/200\). The algorithm uses exact integer arithmetic; division remainders are asserted zero at every Bareiss step. It constructs graph distances independently from bit-flip adjacency and verifies all ball sizes. The two exceptional matrices are handled analytically in RESULT.md by the \(3,1,1,1\) singular values of the cube's bipartite adjacency matrix and a strict active-ball check.

A separate symbolic check of 60 sampled matrices against direct leading-principal-minor determinants gave agreement, but the exhaustive scientific claim depends on the fully embedded program, not on that sample. This is a finite, mechanically replayable computation, not independent scientific validation. The theorem is limited to \(Q_3\); larger graphs have not been exhaustively checked by this certificate.
