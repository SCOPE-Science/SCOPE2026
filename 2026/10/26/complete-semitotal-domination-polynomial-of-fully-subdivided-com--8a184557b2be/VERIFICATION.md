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
# Reproducibility and verification

The supplied `checker.py` enumerates all nonempty vertex subsets of \(H_n=S(K_n)\) for \(n=3,4,5,6\). It constructs graph adjacency directly, builds masks of vertices at distance at most two by a two-step traversal, and applies the original domination and semitotal witness tests. It independently expands the stated combinatorial formula into coefficients using exact integer arithmetic and compares the lists coefficient by coefficient.

Run `python checker.py` in a directory containing the file. Its output must equal the complete JSON line stored in `checker_output.json` (a terminal newline is immaterial). The sizes checked are \(63\), \(1023\), \(32767\), and \(2097151\) nonempty subsets. Minimum multiplicities are \(14,37,91,171\). These are finite checks only. The infinite proof is in `RESULT.md`; no external or independent mathematical audit has occurred.
