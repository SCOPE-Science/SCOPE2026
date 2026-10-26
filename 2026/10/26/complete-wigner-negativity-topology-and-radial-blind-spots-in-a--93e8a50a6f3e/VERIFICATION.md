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

# Reproducibility

Install NumPy and run `python verify.py` in a directory containing `verify.py`. The script produces a `VERIFIED ... checks` message and raises an exception if an assertion fails. In the recorded execution, it printed `VERIFIED 521 checks; equal-rate onset= 0.23856269445149794 2:1 topology split= 0.17275338080786104`.

## Checked quantities

The program reconstructs the full nine-dimensional Liouvillian from qutrit ladder and nonlinear jump matrices, verifies that the published density matrix is stationary, normalized and positive at eleven independently chosen rate pairs, confirms a zero Liouvillian eigenvalue, compares the Wigner polynomial with a separately evaluated Fock-component representation on a finite phase-space grid, and tests the predicted negativity classes and both exact thresholds.

## Logical limitations

These finite numerical checks do not establish an infinite parameter classification or certify the global topology of negative regions. The separate analytic argument uses the exact angular range of a cosine, a strictly positive radial quadratic leading term, explicit discriminants and monotonicity on the two illustrative parameter rays. The numerical phase-space grid alone can miss small near-threshold negative regions. The result concerns the stationary truncated model, not the full infinite-dimensional oscillator. Independent audit has not been performed.
