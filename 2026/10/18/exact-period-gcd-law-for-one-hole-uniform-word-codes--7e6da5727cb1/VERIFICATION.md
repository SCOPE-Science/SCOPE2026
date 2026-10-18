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

The standalone `verify_onehole.py` uses two search algorithms independent of the claimed period–GCD calculation: letterwise KMP-state BFS tracking forbidden occurrence residues, and direct subset BFS over the factor NFA of the allowed block code. Both enumerate shortest obstructions, with independent transition implementations.

Command: `python3 verify_onehole.py` (Python 3 standard library only).

The recorded run (`verification_output.txt`) checked every binary missing block of lengths 2 through 8 (508 cases) and, independently with the factor NFA, every missing block of lengths 2 through 6 (124 cases). All distances agreed with the mathematical formula, and the example of length 25 was produced by the automaton BFS. The complete theorem for all finite alphabets with at least two letters and all lengths at least two is justified by the written proof, not inferred from finite checking.

A separate `python3 verify_residue_dp.py` checks the critical weighted-residue Hamilton path statement using an exact directed Held–Karp dynamic program for every one of the 1,022 formal period inventories with \(2\le k\le10\). Its output is recorded in `residue_dp_output.txt`. This is numerical corroboration for the constructive argument, not an infinite proof.

Independent scientific review has not been performed. Scientific priority beyond the cited inspected literature and indexed records is not independently certified.
