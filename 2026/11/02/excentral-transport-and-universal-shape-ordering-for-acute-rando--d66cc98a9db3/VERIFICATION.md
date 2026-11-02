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

# Verification of the conditional excentral shape law

The analytical proof is given in `RESULT.md`. The included `verification.py` is a standalone supplementary reproducibility check requiring Python 3, NumPy, SciPy and SymPy; run it with `python verification.py`. It verifies all three independent ingredients before printing `ALL_CHECKS_PASSED`.

**Exact affine structure.** Symbolically verify that the \(3\times3\) matrix with off-diagonal entries \(1/2\) is doubly stochastic, has determinant \(1/4\), and maps the simplex corners to the acute-region corners. The uniform push-forward follows from the Jacobian; this last fact is mathematical analysis, not a numerical inference.

**Deterministic shape comparison.** At 17,296 positive rational barycentric triples of denominator at most 48, check simplex constraints, weak majorization, and strictly improved normalized area, perimeter and inradius away from the equilateral triple. The complete assertion is proved separately using majorization and strict trigonometric concavity; the rational mesh is not exhaustive on a continuum.

**Conditional-law distribution diagnostic.** With reproducible seed `20261025`, transport 350,000 independent Dirichlet samples and compare them with independently generated Dirichlet samples accepted by the acute criterion, using sample coordinate means and two-sample Kolmogorov–Smirnov distances for area, perimeter and inradius. The measured acute frequency is approximately one-quarter, with the observed shape-score distances all below 0.003. These are finite checks, not a replacement for equality in law.

**Analytic perimeter and variance identities.** The complete proof evaluates the beta marginal integrals to obtain \(\mathbb E[P]=12/\pi\) and \(\mathbb E[P\mid\mathcal A]=48/\pi^2\). The affine centered map gives \(V(X)\mid\mathcal A\stackrel{\mathrm d}=V(X)/4\), with means \(1/6\) and \(1/24\).

There is no infinite/computer-assisted certification or external independent validation. The source-comparison caveats in `REVIEW.md` apply to the claim of novelty.
