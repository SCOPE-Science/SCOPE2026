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

# Exact finite verification
Run `python3 verify_franklin_pmc.py` followed by `python3 verify_franklin_chain.py` using standard Python 3 in a directory containing the supplied files. The complete actual output from both programs is in `verification_output.txt`. Each script terminates with an assertion if any check fails.

The first independently constructs the Franklin LCF graph and tests its 17 perfect matchings by recursion and direct exhaustive edge-mask enumeration. It checks that all 321 first-stage elementary collapses have a uniquely available maximal coface. It then records 56 second-stage pairs, checks that all 377 matched pairs are disjoint, and exhaustively proves acyclicity by topological sorting every directed incidence in the full face poset. The resulting one critical zero-cell and six critical two-cells imply the integral homotopy classification by the discrete-Morse CW theorem.

The same program enumerates all adjacency-preserving vertex permutations, finding precisely 48, and computes exact orientation-sensitive fixed-simplex traces for each. Lefschetz identity and complete integral homotopy yield the rational degree-two character and invariant dimension zero.

The separate second program enumerates the entire graph-edge power set directly, distinguishing ordinary from extendible matchings. It recomputes each boundary matrix over \(\mathbb F_2\), verifying reduced homology rank six in degree two and zero in all other degrees. This corroborative finite-field calculation does not substitute for the exact integral homotopy proof. No infinite-family theorem or external independent audit is claimed.
