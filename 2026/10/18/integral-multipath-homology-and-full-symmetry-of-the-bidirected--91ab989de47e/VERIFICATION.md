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
# Reproduction and scientific limits

Run `python3 verify_prism_morse.py` from a directory containing the script. It requires only Python's standard library. The program enumerates all \(2^{18}\) possible arc sets; validates degree and cycle constraints; produces the specified acyclic matching; checks all \(2256\) Hasse covers; calculates the signed integral Morse differentials; checks cycle lifts and the full rational character; and verifies the group relations and Lefschetz traces.

Run `python3 verify_prism_independent.py`. This second implementation generates faces by a separate recursive branching scheme, computes all four boundary ranks modulo two and checks twelve signed simplicial Lefschetz identities without using the Morse projection. Its mod-two results cannot establish torsion-freeness in isolation; the integral proof is the exact zero-differential Morse reduction of the first script.

Recorded standard outputs are embedded in `verify_prism_morse_output.txt` and `verify_prism_independent_output.txt`. No random choices or downloaded data are required. Any failure of a count, group relation, chain boundary, acyclicity check or trace equality raises an exception and prevents the success message. The statements concern a single finite directed graph. No claim is made about all cyclic ladders or about a wedge-of-spheres homotopy type.
