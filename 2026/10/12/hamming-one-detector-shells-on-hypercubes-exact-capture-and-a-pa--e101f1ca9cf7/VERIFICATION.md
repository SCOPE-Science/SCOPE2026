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

## Reproduction
Install Python packages listed in `requirements.txt`, then execute `python verify.py`. The script constructs real symmetric adjacency operators of dimensions \(2^n\) for \(2\le n\le7\), diagonalizes them, and forms the captured projector by singular-value decomposition of the detector restrictions in each eigenspace. It checks the analytical Hamming-distance formula against the full projector at all \(252\) sites; it also checks the bright-space dimensions for six hypercubes and the rank effects of origin and antipodal-shell detectors in ten further tests.

Observed standard output ends with:

`VERIFY_OK_shell_probabilities=252_dimensions=6_auxiliary=10`

The numerical eigenvalue tolerance is \(10^{-8}\), and the probability tolerance is \(5\cdot10^{-9}\). Actual runtime versions used for this check were Python 3, NumPy 2.3.5 and SciPy 1.17.0. This does not certify every dimension or every rate choice. Exact generality rests on the Walsh-rank, invariant-layer, and strictly dissipative spectral arguments in `RESULT.md`.

## Mathematical and scope checks
Walsh ranks are \(1\) at the two extreme energies, \(n\) at interior energies except for the single central even-dimensional energy, where the rank is \(n-1\). Layerwise affine functions have exactly \(n\) degrees of freedom at each interior Hamming weight and one degree at each endpoint; the missing even-dimensional direction is normalized using Walsh orthogonality. The resulting projector has positive diagonal in the unit interval in all tested cases, and its trace matches the captured rank. Increasing all losses at the antipodal shell does not alter this projector; adding the origin restores only the even-dimensional central mode. The argument is restricted to the stated idealized model and infinite-time survival, not pointwise convergence of protected density matrices.
