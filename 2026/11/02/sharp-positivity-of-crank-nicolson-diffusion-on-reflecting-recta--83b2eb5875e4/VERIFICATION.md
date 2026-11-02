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

# Reproducibility and verification scope

Run `python artifacts/verify.py` using Python 3 with `sympy` and `mpmath`. The verifier uses exact rational inverses for small rectangles, examines each matrix entry and all row sums, checks independent dense-matrix sign behavior across finite spectral thresholds, compares elliptic and angle-integral representations, and evaluates the odd/even asymptotic ratios using high-precision arithmetic.

The embedded plaintext replay record, `artifacts/verification.txt`, reports **2806 passed checks**. It includes the high-precision universal threshold, exponential rate and both finite-size amplitudes. Testing finite grids does not prove an all-grid theorem; the proof's core all-size ingredients are the Markov-resolvent diagonal reduction, the strict heat-kernel difference system on even cycles, the exact cosine spectrum, and an exponential-moment-controlled lattice-image expansion.

The threshold concerns one full Crank–Nicolson step for the unit graph Laplacian on a reflecting rectangle. The elliptic expression uses the modulus convention for \(K\). Floating-point representations of the constants do not certify exact inequalities. No independent mathematical audit has been performed.
