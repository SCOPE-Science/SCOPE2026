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

The Zak sum factors on tensor products, giving exactly the stated windows and support. On a fundamental strip B=psi(u)>0; A is positive real for 0<u<1/2, vanishes at 1/2, and on 1/2<u<1 the ratio is R(u)exp(2 pi i v). Both differences in L'=d log R/du are positive there, and R has endpoints 0 and infinity, yielding precisely one positive-Jacobian preimage for each slit-plane root. At an integer u, B=0 but A is nonzero, so no factor of the coefficient polynomial can be identically zero and the simultaneous coefficient equations exclude such a pole. Off the poles, equality of monic polynomials forces exactly the d! permutations. The absolute complex determinant of the coefficient map is the absolute Vandermonde (evaluate coefficient variations at the simple roots); its real determinant is the square of that modulus. The product prefactor contributes |prod B_j|^(2d), and each ratio contributes 2 pi |rho_j|^2 L'(u_j). This is the displayed permutation-invariant positive determinant in paired orientation. The sign convention for c1 can also be checked directly by the single positive transverse zero in d=1; the general Zak line is the tensor product of the pullbacks of those coordinate lines. Therefore the Euler number of its d-fold direct sum is d!, giving the stated lower bound exactly in the transverse case. The frozen Python checker is finite floating-point corroboration for d=1 through 5, not a global zero search; it was inspected, not executed. The decision rests on the exact analytic reconstruction.

## originality

PASS

The classical signed bound, the exact bump pair and the tensor coefficient basis are already covered. The distinct supported claim is the explicit prescribed-root fiber with no boundary or additional solutions, all-positive transversality, and the exact common Jacobian. The closest inspected construction supplies the basis and no common base point, not that full fiber and derivative statement. No matching result was identified in the bounded comparisons.

## value

PASS

The Chern obstruction alone does not tell whether actual Zak windows with controlled support attain the minimum or contain extra cancelling zeros. The construction resolves this extremal realization question in every dimension and makes the complete fiber and its transversality quantitatively accessible, rather than recomputing a topological bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
