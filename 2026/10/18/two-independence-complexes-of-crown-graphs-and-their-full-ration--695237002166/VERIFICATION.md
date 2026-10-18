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
# Verification

The self-contained checker `verify_crown.py` uses only the Python 3 standard library. Reproduce with `python3 verify_crown.py` and compare standard output byte-for-byte to `verification_output.json`.

For each \(n\in\{3,4,5,6,7,8\}\), the checker: (i) enumerates all subsets of the crown graph and identifies induced connected components using graph-edge BFS; (ii) independently enumerates the classified face patterns; (iii) constructs all stages of the pivot matching; (iv) checks every covering relation and verifies directed acyclicity by a complete Kahn topological sort; (v) checks the exact critical simplex set; and (vi) computes simplicial mod-two boundary ranks. All tests pass. The largest tested case has 714 nonempty faces, 346 matching pairs, and 2608 Hasse covering relations.

For each \(n\in\{3,4,5,6\}\), the checker also enumerates every \(S_n\times C_2\) group element, computes the fixed-simplex signed reduced Lefschetz number directly, and compares it with the symbolic character, testing respectively 12, 48, 240 and 1440 elements. All pass.

The general homotopy and representation claims are proved by all-parameter combinatorial reasoning in `RESULT.md`. Finite calculations are independent consistency checks, not a substitute for the proof. The rational character identity does not establish an integral equivariant module or an equivariant homotopy splitting.
