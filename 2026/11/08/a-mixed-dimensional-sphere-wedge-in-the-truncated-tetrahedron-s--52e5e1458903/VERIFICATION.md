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

Run `python3 verify_morse.py` and `python3 verify_mod2.py` using Python 3.10 or later; no third-party packages are needed. Their exact recorded outputs are `morse_output.txt` and `mod2_output.txt`. The scripts contain the complete graph construction and enumerate all 4095 nonempty masks, rather than assuming any external table.

The integral script verifies a matching of 428 face pairs and seven critical faces, then orients all 3432 nonempty face-poset covers, performs an exhaustive directed acyclicity test, and evaluates each coefficient of the three-by-three integer Morse attaching matrix. The independent script derives valid faces from all forbidden three-vertex connected subgraphs and computes the original simplicial boundary ranks over \(\mathbb F_2\), confirming \((1,0,0,3,3,0)\) as unreduced Betti numbers. The independent mod-two check is corroboration rather than proof of integral homotopy, which uses the signed Morse reduction plus the homotopy classification of attaching maps in dimension three.

Limits: The verification concerns exactly the finite graph defined in RESULT.md, and no claimed infinite-family extrapolation is made. The review of publication priority and the mathematical proof have not undergone independent external validation.
