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

The mathematical derivation uses independent invariant-operator sectors of sizes \(5\), \(5(n-1)\), and \(n^2-3n+1\) and a precise Routh–Hurwitz dominance argument. Their characteristic polynomials multiply to the all-size asserted expression. The coefficientwise equality is not inferred from numerical spectra.

The standalone `verify.py` constructs the full Lindblad operator on matrix units and checks eigenvalue multisets, Liouvillian gaps, and off-optimal comparisons for finite parameter grids. It also reconstructs the Laplace transform of a localized leaf-population difference using an independent linear solve, comparing against the displayed closed rational formula. Run `python verify.py` in an environment containing `numpy` and `scipy` as stated in `requirements.txt`.

All numerical checks are finite-dimensional and floating-point; no exhaustiveness for all graph orders or continuum parameters is asserted. The analytically proved domain is \(n\ge3\), \(g\in\mathbb R\setminus\{0\}\), and \(\gamma>0\), with a localized-leaf asymptotic statement as \(t\to\infty\). Zero dephasing, heterogeneous couplings, site disorder and graph-Laplacian hopping are outside this theorem.
