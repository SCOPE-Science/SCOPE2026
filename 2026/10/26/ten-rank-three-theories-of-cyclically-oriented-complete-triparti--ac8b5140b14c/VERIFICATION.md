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

# Verification record

Run `python3 verify_cyclic_tripartite.py` with Python 3.10 or later, from the directory containing the program. It requires only the Python standard library. `verify_output.txt` contains the output of an execution from these exact source bytes.

The verifier constructs all twenty-seven size triples in \(\{1,2,3\}^3\). Its first implementation recursively computes quantifier-rank signatures from complete equality and directed-edge atomic diagrams and all available vertex extensions. It verifies one rank-one type, three rank-two types, and ten rank-three types. It checks that the pointed rank-two type is exactly the oriented three-coordinate cutoff profile, and that equality of the resulting unpointed footprint agrees with the rank-three signatures in all 729 ordered pairs of capped structures.

The second implementation is a direct two-sided Ehrenfeucht–Fraïssé game with Spoiler allowed to choose a side on every move; it checks all 378 unordered capped pairs at both rank two and rank three. Restricting each move to already used vertices and one new representative per class is complete because permutations of unused vertices within a class fix every already selected vertex and preserve every arc. The two independent implementations agree. Additional checks replace every capped parameter three by six and test the rank-three truncation boundary, certify the nine-vertex maximum of minimal representatives, and confirm that the exceptional merger at rank three is distinguishable at rank four.

These checks corroborate the exact finite table. The deduction for arbitrary positive parameters rests on the full Ehrenfeucht–Fraïssé argument in `RESULT.md`, not on a search bounded by the machine. Neither an external referee nor a formal independent proof assistant has validated the result.
