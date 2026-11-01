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

# Finite verification and limits

`verify_cube_matching.py` uses Python 3.9+ standard library and rebuilds all definitions from the binary coordinates of the cube. Run `python3 verify_cube_matching.py` and compare its standard output with `verification_output.txt`.

The exhaustive check obtains exactly \(107\) nonempty matching faces, distributed \((12,42,44,9)\) by dimension. It processes all \(252\) Hasse covers, reverses the \(51\) matching arrows and confirms acyclicity by visiting all \(107\) faces in an actual topological sort. The critical face set consists of one vertex and four triangles, establishing the integral homotopy input through Forman's theorem, not through a field-rank inference.

It constructs all \(48\) signed coordinate permutations, checks that each is distinct and computes the induced cube-edge permutation. For each group element it sums signed fixed simplices in degrees zero through three; Hopf trace yields the \(H_2\) character. The ten conjugacy-class outputs, including class multiplicities, match the direct sum of the specified three-dimensional sign-standard and one-dimensional sign representations with the prescribed central parity. Averaging gives zero \(S_4\)-invariants, zero full-group invariants and three \(C_2\)-invariants.

The mathematical theorem concerns only the ordinary matching complex of the three-dimensional cube and its natural action, not related complexes, integral symmetry lattices, or higher cubes. Published nonequivariant homotopy and its sphere count were established previously. The scientific review is not an independent audit.
