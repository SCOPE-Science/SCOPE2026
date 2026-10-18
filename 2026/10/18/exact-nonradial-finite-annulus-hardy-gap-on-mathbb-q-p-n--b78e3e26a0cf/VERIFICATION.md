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

# Verification of the finite-annulus Hardy statement

The analytic verification consists of four parts. The exact shell measure and pairwise ultrametric distance reduce the ground-state deficit to the Toeplitz quadratic form \(B(sI-T_M(r))\). The tridiagonal inverse gives the positive cosine eigenvector and the unique scalar spectral angle, with \(M=1\) handled separately. Its **pointwise** annular eigen-equation proves the full-function positive integral remainder by direct expansion for every test function, which rules out angular improvements and proves equality rigidity. The endpoint equation and Taylor expansion yield the sharp shifted-width \(O(M^{-4})\) remainder.

The file `checker.py` is standalone Python 3.9+ and requires no third-party packages. Running `python checker.py` printed `PASS 858 finite algebraic/numerical diagnostics`. It checks eigenpair equations and Rayleigh inequalities for four parameter triples and several finite widths, a one-shell nonradial angular perturbation in \(\mathbb Q_2\), and finite large-width comparisons. The checks are finite and cannot independently certify the all-function theorem or publication priority.

Scientific limitations: the proof uses Sun's already established ground-state normalization; the improvement is on complete consecutive annuli only. No formal proof assistant or independent expert audit was used.
