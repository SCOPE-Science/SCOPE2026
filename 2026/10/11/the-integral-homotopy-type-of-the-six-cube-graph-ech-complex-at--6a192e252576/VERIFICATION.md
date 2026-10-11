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
# Reproducibility of the six-cube graph Čech calculation

The standalone `verify_q6_cech.py` requires Python 3.10 or later and SymPy. It takes no external scientific data or previous-run certificate. Run `python verify_q6_cech.py`.

The executed checker reconstructed 192 twelve-vertex generators and 626000 distinct nonempty faces, paired 312686 faces in an explicit matching, and topologically sorted all eleven associated gradient-path graphs. The only unmatched cells were one zero-cell, 98 three-cells, and 529 four-cells. The oriented degree-four Morse boundary was an integer matrix of shape 98 by 529 with 294 nonzeros; its Smith normal form had exactly 49 unit invariant factors. An independent mod-two elimination on that same reconstructed matrix returned rank 49. The checks completed successfully with the expected `OK` output.

The integer homology and wedge conclusion additionally depend on the mathematical validity of the facet-to-nerve identification, discrete Morse theory, the signed gradient-path reduction, and the Hurewicz/CW argument documented in `RESULT.md`. The checker verifies the finite combinatorial input and integer arithmetic, not a new theorem for unspecified cube dimensions. Independent audit has not been performed.
