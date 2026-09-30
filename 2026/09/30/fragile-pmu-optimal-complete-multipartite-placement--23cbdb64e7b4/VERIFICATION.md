---
{"schema_version":1,"independent_audit":{"status":"not_performed","evidence":null},"lean_verification":{"status":"not_performed","evidence":null},"expert_attestation":{"status":"not_performed","evidence":null}}
---

# Verification

`verify.py` constructs complete multipartite graphs and simulates power domination directly from survivor sets. Using exact rational arithmetic, it compares direct survivor enumeration with the closed reliability formula for three failure probabilities, compares the greedy placement rule with exhaustive occupancy-vector optimization for every budget, checks marginal monotonicity, and verifies the stated closed-form budget regimes. The archived `verification_output.txt` reports the exact check counts and terminates with `VERIFY_OK`.

This is computational verification of finite test families, not an independent audit or a proof of the infinite theorem.

No Lean proof or proof-assistant check was performed. The Python verifier and its output support only the finite computational checks described above.
