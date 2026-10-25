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
# Reproduction

Execute `python3 verify.py` from this directory with a standard Python 3 interpreter. The script needs no third-party library or network access. Its output is recorded in `verification_output.txt`; success ends with `VERIFY_OK`.

The verifier independently defines the faces by forbidden Petersen open neighborhoods, by complementary total dominating vertex sets, and by forbidden triangles in the original graph on five labels. It enumerates every possible graph edge set, proves acyclicity of the supplied discrete-Morse matching by topological sort of all face–coface incidences, computes the exact signed integer four-to-three Morse boundary using oriented cancellations, and checks the full mod-two simplicial homology independently. It evaluates the signed Lefschetz formula under each of the 120 five-label permutations. The final rational character decomposition follows because a rank-one action of the symmetric group is either sign or trivial and the sign hypothesis gives an impossible negative trivial multiplicity in degree three.

The program establishes no statement outside five labeled graph vertices. It does not eliminate potential identical prior results from literature inaccessible in full and is not an independent expert audit.
