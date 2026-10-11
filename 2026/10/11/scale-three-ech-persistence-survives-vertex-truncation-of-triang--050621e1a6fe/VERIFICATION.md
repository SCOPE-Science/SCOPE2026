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

# Reproducibility and mathematical checks

The argument for all triangle-free graphs is the explicit free-face proof in `RESULT.md`; `verify.py` is a finite consistency test only. Run `python3 verify.py` using the Python standard library from the directory containing this file. It enumerates the oriented incidences, the even/odd Čech generating faces, and all simplices of the relevant finite complexes, then checks each individual elementary collapse in all four stages. A lower simplex must have exactly one surviving codimension-one coface, and the upper simplex must be maximal in the surviving complex. It checks equality of the stage targets, connected graph Euler ranks, and the triangle-exclusion boundary example by independent mod-two boundary reduction.

The deterministic check set consists of a one-edge graph, a four-vertex path, a degree-four star, cycles of lengths four and five, the complete bipartite graph on parts of sizes two and three, the cube, the Petersen graph, and thirty additional connected triangle-free graphs built using fixed-seed edge insertion. Each finite example satisfies the graph hypotheses before its collapse test. Successful execution prints `VERIFY_OK 38 triangle-free examples total elementary collapses [1588, 2798, 1162, 106]`, with counts for the four separate collapse stages. It additionally prints `C3 sharpness: H2 mod 2 scale2=0, scale3=2`.

A finite suite neither proves the theorem for arbitrary order nor certifies that all possible graph embeddings or publication records have been enumerated. The general relative collapse rests on the combinatorial uniqueness conditions and the descending-order free-face argument, which are independent of computational size. The comparison of prior publications remains subject to residual unindexed-literature risk. No independent audit or external certification has been performed.
