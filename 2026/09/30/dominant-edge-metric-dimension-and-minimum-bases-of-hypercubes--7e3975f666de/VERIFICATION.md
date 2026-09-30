---
{"schema_version":1,"independent_audit":{"status":"not_performed","evidence":null},"lean_verification":{"status":"not_performed","evidence":null},"expert_attestation":{"status":"not_performed","evidence":null}}
---

# Verification

`verify.py` constructs each binary hypercube directly, computes edge-distance vectors, checks the vertex-cover condition, and exhaustively searches all candidate subsets for dimensions one through four. It separately verifies both parity classes for every dimension from three through ten. The archived `verification_output.txt` records the exact minima and basis counts in the exhaustive range and terminates with `VERIFY_OK`.

This is same-source computational corroboration of finite cases. It is not an independent audit, Lean verification, expert attestation, or a substitute for the general proof.
