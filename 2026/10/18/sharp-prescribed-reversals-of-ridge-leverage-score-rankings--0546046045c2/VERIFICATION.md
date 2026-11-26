---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each row a, every component on ker(A^T A)=ker A is zero. Each distinct positive eigenspace therefore contributes one simple pole with numerator equal to the squared norm of the projected row. Combining the q poles gives a polynomial of degree at most q−1 over a denominator positive for λ>0; the identically zero numerator is a separate case, and a simple positive zero changes sign. For sharpness, let P and Q be the prescribed monic numerator and pole denominator. Evaluating the cleared rational identity at −d_k gives residues P(−d_k)/Q'(−d_k); both sides of the cleared identity have degree ≤q−1 and agree at q points. Split the residues divided by d_k into positive and negative parts, scale by ε and take square roots to obtain the first two rows x and y of U. The frozen strict bound on ε makes I−xx^T−yy^T positive definite. Its square root completes U to q orthonormal columns with q+2 rows, so A=U diag(sqrt(d_k)) has the required spectrum and the required difference of two scores for that same A. This covers repeated positive modes in the upper bound, q=1, and the rank-deficient case, without using λ=0. In the frozen three-mode example the mass of the two rows is 28/45 and the signed residues are (5,−18,14)/30, giving the two stated simple crossings. The separate replay `python /workspace/review_checks/frozen_probes.py` checks that identity at rational points and an exact alternative two-mode isometry crossing at λ=2. No frozen checker was executed.

## originality

PASS

Best of current knowledge for the precise ridge-row theorem, especially fixed-spectrum realization with arbitrary prescribed simple positive crossings. The pole-count bound is elementary after spectral decomposition and interpolation of a signed Cauchy transform is classical; those observations are not standalone originality claims. The inspected papers and indexed records do not supply the joint realization of both rows of one real data matrix with the stated spectrum and row budget.

## value

PASS

Score-based deterministic selection motivates an exact question: can a ranking obtained at one penalty be reused as the penalty varies? The sharp bound depends on spectral diversity rather than row count. The thin common-matrix realization provides an explicit obstruction to assuming even a single reversal, or that reversal locations are constrained once a singular spectrum is fixed. That converse, not just counting polynomial zeros, gives a usable exact boundary. No whole-sort, runtime, or statistical improvement is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
