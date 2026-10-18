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

The included `verify_ind2_q4.py` works with Python 3.9+ and standard-library code only. Recompute using `python3 verify_ind2_q4.py`; expected output is in `verify_ind2_q4.out`. The program enumerates every nonempty subset of the 16 vertices, checks induced degree at most one, constructs each Morse matching pair from the stated pivot order, and visits every simplex and Hasse incidence in a full cycle-detecting topological sort. It then computes the unique potentially nonzero Morse boundary over the integers, with orientation signs and integer elimination, obtaining an exactly zero coefficient vector. Finally, an independent mod-two reduction of all original simplicial boundary columns reproduces the Betti numbers.

This verifies a finite combinatorial certificate; the deduction of the homotopy type also uses the mathematical discrete-Morse theorem and the degree-three Hurewicz isomorphism. There is no claim of mathematical originality certification, independent scientific audit, or results for higher-dimensional hypercubes.
