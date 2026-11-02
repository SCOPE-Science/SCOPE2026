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

# Numerical and analytical verification

Run `python verify.py` with NumPy and SciPy in the same directory as the extracted files. On the original packaged source, this produced `PASS: 101 numerical consistency checks (no infinite-limit certification)`.

The script compares two mathematically different exact finite-population integral representations of the synchronized-reset success probability, checks its range and elementary geometric-renewal identities, and performs scaled numerical evaluations at several subcritical and supercritical coefficients and five critical-window parameters. These calculations check signs, factors and normalization without requiring an astronomical number of explicit particle paths. For example, at \(\log N=200\), the measured ratios to the subcritical theoretical leading terms are approximately \(0.9918\), \(0.9844\), and \(0.9447\) for \(a=0.25,0.50,0.75\); they tend slowly near the critical boundary. At \(\log N=700\), the critical ratio at \(z=0\) is approximately \(0.5746\) versus its limiting value \(0.5\), consistent with slow logarithmic convergence and not a certification of that limit.

The proof in RESULT.md, not numerical tests, supports the infinite-population conclusions. Critical noncomputational ingredients are the Brownian reciprocal hitting-time Gamma law, the Gumbel exponential-moment convergence for \(a<1\), the exact moment-generating function of the tilted Gamma law and its Gaussian limit, and the regenerative Laplace-transform argument. The separate prior-literature comparison and its limits are in REVIEW.md and AUDIT.json. No independent mathematical review or certification is asserted.
