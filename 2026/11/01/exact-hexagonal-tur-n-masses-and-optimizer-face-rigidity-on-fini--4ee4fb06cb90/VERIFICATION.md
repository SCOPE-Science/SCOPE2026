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

# Mathematical verification

Run `python checker.py` from the directory containing the standalone checker. Python 3 is required; NumPy and SciPy are optional additions for independently optimizing all six real Fourier coefficients by linear programming.

The recorded execution produced `CHECK_PASS orders=5..90 grid_modes= 86 Fourier_inequalities= 247035 LP_instances= 17`. The checker enumerates all \(86\) moduli from \(N=5\) through \(N=90\), and for each checks every \(N^2\) Fourier mode, the exact set of minimizing frequencies, and the positivity and complete zero set of the invariant optimizer. It also compares exact optimum formulas against separate numerical linear programs for \(N=5,\ldots,21\), including unconstrained complex Fourier coefficients represented by six real variables, and checks the signed cubic asymptotics at four larger orders.

The proof for arbitrary \(N\) does **not** depend on finite enumeration: cosine gap smoothing proves the all-order minimum, the support symmetry gives optimality, two nonsingular three-by-three matrices give full complex uniqueness for nonmultiples of three, and the two Fourier-zero equalities plus strict positivity of every other Fourier mode give the four-dimensional resonant face. The trigonometric expansions control the remainder terms. Numerical calculations use floating point and appropriate tolerances; they do not imply exact all-order positivity without this proof.

Public-source overlap searches were necessarily bounded. The full text of two plausible older sources (toroidal-graph spectral preprint and continuous-hexagon Turán work) was not available in the inspection pathway. No independent mathematical audit or validation is claimed.
