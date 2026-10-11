---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

After affine normalization the local transform is \(P(X,Y)=a+bX+cY+dXY\) on \(\mu_3^2\). In any row, either the affine function of \(Y\) is identically zero or it has at most one zero. Hence without a full zero row there are at most three zeros. If a row \(X=\alpha\) is identically zero, then \(P=(X-\alpha)(b+dY)\), so the zero set is either that row alone (3 zeros) or the union of a full row and a full column (5 zeros). Thus four zeros are impossible. Five explicit all-nonzero coefficient vectors attain zero counts \(0,1,2,3,5\). The actual exact verifier checks those witnesses in \(\mathbb Q(\omega)\) and all 126 four-row constraints, confirming that any all-nonzero rank-three null vector forced by four prescribed zeros actually has five zeros. Multiplying by the ambient fiber count \(3^{d-2}\) proves the result.

## originality

PASS

Delvaux--Van Barel and Bonami--Ghobber give global rank-deficiency/uncertainty information for \(F_3\otimes F_3\) and \(\mathbb Z_3^2\), but they do not give the complete spectrum for the specified four-column parallelogram. In particular, the global uncertainty function at physical support size four does not determine which intermediate output-support sizes are attainable on this geometry. Resultary returned no earlier implication-equivalent fixed-support theorem.

## value

PASS

This is the smallest ternary two-dimensional affine-parallelogram support problem and gives a complete exact spectrum, including an isolated forbidden intermediate size. It is a natural geometry-sensitive refinement of finite Fourier uncertainty rather than an arbitrary parameter census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
