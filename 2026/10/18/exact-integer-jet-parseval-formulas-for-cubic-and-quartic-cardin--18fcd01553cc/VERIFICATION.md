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

The standalone `verify_spline_jets.py` was executed against the packaged filter definitions with Python 3 and SymPy. Recorded output appears in `verify_output.txt`.

Checks included: complete exact integer-knot filters from the truncated-power derivative representation; rational Laurent-correlation coefficient cancellation; invertibility of the complete diagonal-weight linear system; positivity and uniqueness of the weights; numerical checks of the independently written \(s=2-2\cos\theta\) polynomial forms; forty exact finite rational signal energy and finite-stencil reconstruction tests for each of the two spline degrees; and cubic Nyquist invariance. A successful execution reports 1,449 checked assertions.

These finite tests do not constitute a proof for all \(\ell^2\) sequences. The continuous Fourier-symbol identity plus discrete Plancherel, bounded convolution and density proves the infinite statement. A different frame norm, nonuniform grid, or additional degree is not checked. No external or independent validation has occurred.
