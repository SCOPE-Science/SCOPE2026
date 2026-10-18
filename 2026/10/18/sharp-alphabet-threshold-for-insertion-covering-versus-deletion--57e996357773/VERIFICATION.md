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

# Reproducibility

Run `python3 verify.py` in the same directory as `verification_output.txt` (Python standard library only). Its three counters cover explicit binary robust witness checks, binary length-four avoidance constructions, and ternary/quaternary length-three constructions. It performs literal scattered-subsequence checks and exact enumeration; no probabilistic hash is involved. The proof in `RESULT.md` covers arbitrary positive \(R\) and arbitrary alphabet sizes, whereas the checker deliberately covers only the finite ranges printed in `verification_output.txt`.

Independent mathematical validation has not been performed.
