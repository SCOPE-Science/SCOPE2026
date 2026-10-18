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
# Verification

Run `python3 verify_torus.py` from a directory containing the standalone program; it has no third-party dependencies. The program reproduces exact rational inversions of the finite torus matrices for sizes \(3\times3\), \(3\times4\), \(4\times4\), \(3\times5\), and \(5\times5\), at three rational step sizes, checks the full off-diagonal and diagonal signs, row sums, and agreement with the independent Fourier formula. It checks strict numerical threshold ordering on all grids with periods \(3\) through \(8\) by bisection; evaluates the elliptic integral independently using the arithmetic–geometric mean; verifies the size-correction bound at those sample sizes; and uses exact rational finite sums with rigorous geometric remainders to certify \(0.588197<H_\infty<0.588198\).

The universal root-of-unity Fourier identity, monotonicity for every permitted integer pair, wrapped-walk bound, uniqueness of crossings, and infinite-lattice limit are proved analytically in `RESULT.md`. Numerical bisections and finite enumerations do not certify all sizes. No theorem prover or outside certificate is asserted.

Expected final line: `threshold 8 8 0.588200326833451` (last decimals may vary slightly by platform).
