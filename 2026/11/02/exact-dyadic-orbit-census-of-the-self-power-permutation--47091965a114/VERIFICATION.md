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

# Reproducibility and limits
The standalone verifier `verify_self_power.py` computes every odd state independently with `pow(x,x,2**k)`, traces all cycles and checks the predicted exact least period of each state and the exact number of cycles of every length for all \(1\le k\le15\). It checks all \(32,767\) distinct states in these moduli, all predicted cycle components, and the two-longest-cycles corollary for every tested \(k\ge6\). Execute `python3 verify_self_power.py` in the directory containing this file and the script. The proof in RESULT.md, not the bounded enumeration, supports the assertions for every \(k\ge1\). Independent audit: not performed.
