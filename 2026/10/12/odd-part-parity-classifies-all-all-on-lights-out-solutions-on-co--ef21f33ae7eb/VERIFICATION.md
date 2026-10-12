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

# Computational verification and limitations

Run `python3 verify_lights_out.py` using Python 3.10 or later. The standalone program constructs the graph directly from each multipartition, generates exact bit-mask toggle columns, exhaustively iterates every press subset by Gray code, compares the complete press-count distribution to the stated formula, and independently reduces the closed-neighborhood matrix over \(\mathbb F_2\). It does not use the theorem's symbolic part equation to generate candidate press patterns.

`verification_output.txt` contains the actual run result: \(363\) ordered profiles and \(579194\) press subsets, maximum graph order \(15\), all checks passing. The finite check verifies the implementation on those inputs only; no inference from those instances is used to establish the theorem for unbounded input. Infinite validity follows from the partwise parity equations in `RESULT.md`.

No independent audit or external proof certification has been performed.
