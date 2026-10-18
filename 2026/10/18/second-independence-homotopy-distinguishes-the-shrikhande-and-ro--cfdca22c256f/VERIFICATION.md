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

Execute `python3 shr_rook_pair_certificate.py` from a directory containing the extracted package files. The program needs only the Python standard library and no external data, certificates or packages. Expected terminal marker: `SHRIKHANDE_ROOK_SECOND_INDEPENDENCE_WEDGES_VERIFIED`.

For each graph separately, the executable: builds the full adjacency relation; checks every vertex has six neighbors and each distinct pair has exactly two common neighbors; evaluates every one of the \(65536\) vertex subsets by both maximum-induced-degree and induced-component searches; checks every dimension's face count; builds all greedy element-matching pairs in the specified pivot sequence; verifies every codimension-one incidence, including a topological sort of the directed Hasse graph; and computes all boundary-matrix ranks over \(\mathbf F_2\) independently of Morse theory.

Numerical bounds checked in the actual run: \(1337\) and \(1193\) augmented faces; \(639\) and \(543\) match pairs; exactly one critical vertex plus \(57\) or \(105\) three-dimensional cells; \(4960\) and \(4224\) Hasse incidences; reduced mod-two homology concentrated in degree three with those multiplicities. The direct acyclic Morse construction supplies the integral homotopy result; mod-two checks alone would not.

The finite enumeration is exhaustive because there are only sixteen vertices per graph; it makes no claim about larger graphs, equivariant structures, or external independent verification. Recorded output appears in `certificate_output.txt`.
