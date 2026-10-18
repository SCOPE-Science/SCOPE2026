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
# Reproducibility and checks

Execute `python3 verify.py` using Python 3.9 or later, from this package directory. No third-party modules or remote resources are required. The program regenerates all graph data without a preloaded face list. It checks 8,951 Shrikhande and 7,343 rook augmented simplices, all 32 graph triangles each, and exactly 4,466 or 3,658 matching pairs. It constructs the complete oriented Hasse digraphs, topologically sorts their 48,288 and 37,744 arcs to verify acyclicity, and computes every signed gradient path projection needed for the integer dimension-six-to-five Morse differential. The full-rank integer minors have determinants \(+1\) and \(-1\); their row or column coordinates are described in `RESULT.md`.

The verifier independently reduces all original simplicial boundary matrices modulo two, using full face sets rather than the Morse matching, and reproduces the nonzero Betti ranks of nine in dimension six and fifteen in dimension five. The generated output from the completed run is embedded as `check_output.txt`. Both computations are finite and exact, not numerical approximations. The full integer homotopy conclusion additionally uses the standard discrete-Morse CW equivalence and the degree classification of attaching maps into wedges of five-spheres. The assertions do not extend to larger graphs or predict analogous results for all strongly regular graphs. Independent scientific validation has not yet been performed.
