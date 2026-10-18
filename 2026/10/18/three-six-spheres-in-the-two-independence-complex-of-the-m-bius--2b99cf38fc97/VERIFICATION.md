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

# Verification of the exact finite certificate

Execute `python3 verify_mk_ind2.py` using Python 3.8 or later. The script constructs the graph from its definition and independently enumerates all nonempty vertex-subsets, all forbidden three-vertex paths, the 3,400 pairs of its deterministic 16-stage vertex-toggle matching, and all 35,104 Hasse relations. Reversing the matched covers gives a directed acyclic graph: its complete topological sort visits every one of the 6,812 faces. Exactly 12 critical cells remain, distributed as one degree-zero, one degree-four, four degree-five and six degree-six cells.

Using exact signed integer chain projection, the script computes the full \(1\times4\) and \(4\times6\) Morse differential matrices recorded in RESULT.md and verifies that their composition is zero. The first five-cell has degree \(-1\) on the unique four-cell, yielding a contractible CW subcomplex. After contracting it, the six-cell attachment matrix has a \(3\times3\) minor of determinant \(+1\); Hurewicz and integral changes of sphere bases identify the homotopy cofiber as the wedge of three six-spheres.

A separate original-chain mod-two boundary rank computation yields \((0,15,105,407,917,1147,693,120)\) in dimensions zero through seven, corroborating three reduced degree-six Betti generators. This test by itself does not rule out odd torsion or nontrivial higher attaching maps; the integral Morse and homotopy arguments do.

The exact recorded execution output is supplied as `verify_mk_ind2.out`. The exhaustive finite check does not constitute independent audit or a classification beyond the specified graph.
