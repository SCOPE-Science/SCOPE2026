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

# Reproducible checks

From the package directory run `python3 verification/check.py`. The script requires Python 3.9 or newer and no third-party packages. It uses exact `fractions.Fraction` arithmetic and builds every edge and vertex Laplacian without using the proposed potential formula to generate the projection.

On each connected complete multipartite profile it inverts the nonsingular matrix \(L+\mathbf 1\mathbf 1^{\mathsf T}/N\) by rational Gaussian elimination. Each source-edge potential is checked against all Kirchhoff equations, then every edge's absolute cut and cycle projection column sum is compared against the claimed closed formula. Both operator maxima are checked separately. Enumeration covers all unordered multipartitions with at least two parts and \(2\le N\le10\), plus profiles \((1,2,10)\), \((2,3,5)\), and \((3,4,4)\). It also checks the inequalities, formulas and strict cycle-minus-cut difference for \(K_{N-3,2,1}\) for every integer \(6\le N\le100\).

Actual output: `VERIFY_OK: 131 multipartitions, 3029 exact edge columns; 95 extremizer-reversal instances`.

Limitations: the finite checker does not establish any untested larger graph instance; the included paper proof gives all-integer quantifiers. Only the canonical orthogonal projection norms are examined. The verification does not constitute external or independent auditing.
