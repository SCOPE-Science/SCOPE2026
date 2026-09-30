---
{"schema_version":1,"independent_audit":{"status":"not_performed","evidence":null},"lean_verification":{"status":"not_performed","evidence":null},"expert_attestation":{"status":"not_performed","evidence":null}}
---

# Verification

`verify.py` implements the coordinate construction from the proof. For every unordered triple of vertices of \(Q_n\) with \(1\le n\le7\), it builds the prescribed path and checks that the three target vertices occur, every consecutive pair differs in exactly one coordinate, no vertex repeats, and every nonconsecutive pair differs in more than one coordinate.

The archived output is `VERIFY_OK dimensions=1..7 triples=388620`. This is same-source computational corroboration, not an independent audit, Lean verification, expert attestation, or a substitute for the proof for arbitrary \(n\).
