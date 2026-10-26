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

Run `python verify.py` in the directory containing the extracted source. The code constructs residue-graph shortest paths using only the four semigroup generators. It independently obtains Apéry minima, enumerates every candidate pseudo-Frobenius gap by exact generator-membership tests, compares the computed sets with the closed formulas, and checks the gap and sum conditions. It passed for all integers from five through thirteen inclusive. Computation is finite and does not establish the unrestricted result, which is proved symbolically in `RESULT.md`. No independent mathematical audit has taken place.
