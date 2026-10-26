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

# Verification record

The standalone verifier `triangular_verify.py` can be run with `python triangular_verify.py` using a standard Python 3 interpreter. It constructs every six-neighbour update directly, computes independent convolution powers with symmetric-difference supports, and uses exact GF(2) Gaussian elimination to compare ranks against the stated algebraic formulas.

It checked all 256 ordered graph sizes with circumferences between 3 and 18 inclusive: at the predicted sharp depth, the rank is the predicted recurrent dimension, and one update earlier the rank is strictly larger. It also checks 102,912 individual labelled trajectories in seven selected small toroidal graphs and nine exact last-step rank instances for dyadic square and rectangular tori.

The recorded output in `verification_output.txt` is reproducible. These computations test examples; only the proof in `RESULT.md` establishes the universal family. A successful program run is not external or independent audit evidence.
