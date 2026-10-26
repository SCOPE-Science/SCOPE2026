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

# Reproducibility of the four-cube color census

Execute `python3 verify.py` in a directory containing the supplied file. It has no external dependencies. Expected standard output is included verbatim in `verification_output.txt`.

The first exhaustive algorithm normalizes the root and its degree-four neighborhood, enumerates all \(216\) allowed second-layer assignments, eliminates all local parity violations, and finishes the last five vertices under properness and neighborhood oddness. It produces exactly \(20\) normalized colorings; the root-data orbit has size \(96\).

The independent second exhaustive algorithm fixes the root color and assigns the even-parity cube vertices first: of \(4^7\) possibilities, \(54\) pass the odd-vertex parity test. Exactly \(12288\) corresponding odd-vertex tuples survive immediate properness, of which \(480\) also meet all even-vertex odd-neighborhood conditions; multiplying by four root colors gives \(1920\).

Additional checks count affine direction multisets for even dimensions \(2,4,6,8\), compare all normalized colorings against affine identities, verify the nonlinear seed on the original graph, and directly test its lifts in dimensions \(4,6,8,10,12\). These last finite lift checks illustrate, but do not prove, the all-dimension statement; the rigorous proof is the even-multiplicity argument in `RESULT.md`.

The exact number of all colorings in dimensions six and greater is unproved. No independent external review or validation has been performed.
