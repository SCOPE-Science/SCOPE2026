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

For each punctured character table B_i, full-table orthogonality gives B_i 1=B_i* 1=-1 and B_i*B_i=n_i I-J. The domain and dual centered blocks have dimension n_i-2, vanish under all cross-axis couplings, and have singular values sqrt(n_i) and inverse B_i*/n_i there. The complementary normalized axis indicators plus center give diag(0,-D)+(1,v)(1,v)^T, so the Schur complement -D proves the inverse and gives determinant magnitude product n_i^(n_i/2) after the centered blocks. Equal orders give -n on d-1 contrasts, and the two remaining eigenvalues have product -n and sum (d-1)(n-1); evaluating the polynomial at n gives the stated change of largest singular value at d=2. For the normalized forward restriction the sharp two-sided bounds are sigma_min/max divided by sqrt(|G|); the inverse stability norm is the reciprocal of the lower bound. Read the bundled checker and independently rebuilt four raw character matrices in independent_checks.py cross, including Z/4 and (Z/2)^2 in the same product (max SVD discrepancy 1.34e-15). These are corroboration; the orthogonal decomposition proves the full theorem.

## originality

PASS

Pass for the complete finite radius-one spectrum with unequal factor orders and its sharp sampling consequences. The homogeneous special cases have exact published coverage. The determinant and inverse are useful but not strong standalone originality claims: the published unitriangular support-poset factorization yields them by taking the one-coordinate Schur blocks separately. It does not preserve singular values and does not give the mixed-order finite spectrum.

## value

PASS

Radius-one support is a natural model for signals with a baseline and separate coordinate effects. Sampling on the same frequency cross is a square recovery problem; invertibility alone gives no noise amplification. The heterogeneous spectrum reduces the exact stability computation from a full character-dependent matrix to d+1 real dimensions and specified scalar blocks, even with noncyclic factors. The determinant by itself would not justify this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
