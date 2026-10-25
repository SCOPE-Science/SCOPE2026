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

# Reproducibility and mathematical limits

Execute `python3 verify.py` with Python 3.10 or later. The program independently constructs the ten-vertex Kneser graph, enumerates all 120 Hamiltonian-path edge sets and their 10,212 subsets, and computes an acyclic discrete-Morse matching with 5,092 pairs (including the empty-face pair). It verifies acyclicity through a topological sort of all 58,830 directed face incidences, then evaluates the \(4\times24\) integer signed Morse differential, finding zero for every entry.

An independent full mod-two simplicial boundary calculation yields ranks `[1,14,91,354,891,1455,1446,720,120]` by simplex size. Exhausting every one of the \(2^{15}\) graph-edge masks gives 10,372 linear-forest masks and exactly 160 outside the containment complex; minimal obstructions comprise ten six-edge and thirty eight-edge forests, each a full \(S_5\)-orbit. The packaged `verification_output.txt` records the program's result and final `VERIFY_OK` marker.

**What these checks prove.** The mathematical bridge from the finite acyclic matching and exact integer Morse differential to the integral homotopy wedge is the classical discrete Morse CW equivalence, together with the Hurewicz isomorphism for the four-connected five-skeleton. A successful script run alone is not an independent verification of the correctness of its implementation or of any unenumerated generalization. No independent audit has been performed.
