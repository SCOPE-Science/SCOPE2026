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

# Reproducible verification

The exact graph, allowed-face rule, deterministic pivot sequence, complete orientation of face-poset covers, and signed Morse cancellation recursion are all encoded in `verify_morse.py`. The script computes its own face enumeration and exact directed topological sort rather than relying on supplied numeric logs. It finds 20,651 nonempty faces, 10,319 matching pairs, all 120,222 nonempty codimension-one covers, thirteen critical cells, and the primitive rank-one integer boundary between critical dimensions six and five.

The independent `verify_mod2.py` recomputes face membership by checking every selected induced vertex's degree, then reduces every full simplicial boundary over \(\mathbb F_2\). It obtains reduced Betti numbers nine in degree five and one in degree six. Both programs were executed on the embedded sources; their recorded outputs appear in `morse_output.txt` and `mod2_output.txt`. Each must end in the literal line `PASS` when independently replayed with standard Python 3.

The exact integral homotopy claim is proved by the finite acyclicity check, the explicitly computed signed Morse differential, and the Hurewicz argument in `RESULT.md`. The field calculation alone cannot exclude torsion or identify attaching maps. No claim is made about other graphs or independence parameters. Independent audit has not been performed.
