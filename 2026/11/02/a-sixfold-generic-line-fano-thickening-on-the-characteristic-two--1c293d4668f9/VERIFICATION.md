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

The ordinary proof, local-coordinate expansion, and symbolic manipulations are contained in `RESULT.md`. Execute `python3 verify_segre.py` with Python 3 and no external packages.

The finite-field checker explicitly enumerates all projective lines of \(\mathbb P^3(\mathbb F_2)\), \(\mathbb P^3(\mathbb F_4)\), \(\mathbb P^4(\mathbb F_2)\), and \(\mathbb P^4(\mathbb F_4)\). It enforces all four coefficients of the restricted cubic, not simply pointwise vanishing on a short finite line. Its counts are respectively \(15\), \(27\), \(75\), and \(477\) lines on the relevant varieties. The 27 geometric lines on the cubic surface split into fifteen fixed lines and six Frobenius pairs.

An exact witness in \(\mathbb F_{32}\) provides a point of the smooth cubic at which the linear tangent form and square root of the quadratic tangent form are independent. A simultaneous transverse direction has cubic value \(19\ne0\), verifying that the coefficient of the surviving cubic normal variable is nonzero. Nonvanishing at one actual geometric point establishes a nonempty Zariski-open locus; the Hilbert-scheme equations and elimination in the written proof then establish the generic local algebra \(\overline{k(S)}[u,v]/(u^2,v^3)\).

The checker does not compute all geometric points of the Fano scheme in arbitrary extensions, nor does it derive the local Artin algebra merely by brute force. The 28 components and all-power counting formula rely on the geometric projection argument, standard cubic-surface line theorem, and Frobenius action on the Picard group. The calculation does not determine the nonreduced global scheme or local structure at intersections of components.

Self-review were completed; independent audit and independent validation have not been performed.
