---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A scalar unitary at each vertex gauges away the rank-one phase; a geometric progression of phases rotates the entire superdiagonal. Thus twice the numerical radius is the norm of the Hermitian sum. In its even/odd bipartition the cross block is B=P Q*, one endpoint vector in each column per edge. P*P and Q*Q are exactly the odd/even overlap Grams. Cycling factors in BB* identifies all nonzero eigenvalues, with multiplicities, with those of G_o G_e; zeros do not affect the radius even at singular endpoints. Positive adjacent entries make the product irreducible for r>0, and any increased overlap increases an entry, making strict Perron comparison applicable. At r=0 orthogonal incident directions split the path precisely at equal signs; the longest remaining path has L edges. At r=1 all edge vectors agree at each shared vertex, giving the ordinary scalar path. For the analytic derivative, let sigma=2 cos(theta), and let x=P*f and y=Q*g be the incidences of the normalized odd and even singular vectors. Their pairing is y*x=sigma and G_e x=sigma y, G_o y=sigma x. The derivative of the simple top eigenvalue against one Gram overlap is therefore twice the product of the opposite endpoint incidences, or 4 psi_j psi_(j+2), with psi the normalized sine path vector. Differentiating sqrt(lambda)/2 gives the stated coefficient with no extra factor of two. An exact independent characteristic polynomial check for (++-) gives lambda(lambda^2-3 lambda+2-r^2). The supplied NumPy script was inspected as bounded supporting evidence, not run or relied upon for general validity.

## originality

PASS

Credit the sharp alternating-word value and ordinary path sine spectrum as prior. The supported difference is an all-word rank-one spectral reduction, giving strict order and endpoint equality cases and a localized first variation at fixed length. No retrieved comparator gives or directly implies that combination. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

The orientation question is motivated by the known alternating optimum. A dimension-free exact finite Gram law provides comparisons the scalar optimum alone cannot make; the zero-overlap run statistic and the nonuniform defect slope explain what invalidates simple defect counting. The result is useful for open paths with a fixed rank-one operator, not claimed for general rank or cyclic closures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
