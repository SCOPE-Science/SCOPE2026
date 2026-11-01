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
# Reproduction and limits

Run `python check.py` using Python 3 with NumPy and SciPy installed. The script compares the exact dipole derivatives with the classified weight regimes for exhaustive and randomly chosen finite weight vectors, and independently checks directional derivatives by matrix exponentiation of the unit-conductance cycle Laplacian. Exact combinatorial checks involve 5,458 exhaustively generated and 5,400 randomly generated weight profiles. Numerical checks include 160 directional derivatives, 30 strictly increasing witnesses, and 805 contractive finite-time dipoles. The checker prints the check counts and a final PASS assertion when it succeeds.

The checked profiles and times are finite samples. The proof for every cycle length, positive variation-weight vector, real signal and time is the algebraic transport/Euler-semigroup argument in RESULT.md; no infinite statement is inferred from enumeration or floating-point tests. The numerical tolerance only accommodates matrix-exponential roundoff. No independent audit has been performed.
