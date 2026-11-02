---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each u in (0,1], H_u f(z)=[1-(1-u)z]^{-1}f(uz/[1-(1-u)z]); direct Möbius composition gives H_u H_v=H_uv. The H1 and Bergman-A1 preadjoint composition norms are O(u^{-1}), so the spectral radius of H_t on BMOA/Bloch is at most t^{-1}. For every 0<|w|<t^{-1}, s_k=(log w+2πik)/log t has Re s_k>-1, and independent H1 predual eigenvectors (1-z)^{s_k} and their J-images produce an infinite-dimensional adjoint eigenspace; the primal (w-H_t) range closure therefore has infinite codimension. Closedness of Fredholm essential spectrum yields the entire closed disk and, with the radius bound, equality for H_t. A local variable z=v/(1+v) shows each putative eigenfunction is a scalar z^k/(1-z)^{k+1}, not Bloch, so H_t has empty point spectrum. Strict convergence radius rho>t^{-1} ensures F(H_t)=Σa_jH_t^j converges and permits holomorphic spectral mapping in B(X) and the Calkin algebra. Factorization of F(z)-λ by finitely many zeros on a neighborhood of the compact disk leaves injective factors, proving F(H_t) has no eigenvalues even when distinct w share the same F-image. The same predual eigenspaces give infinite-codimensional range closures at all F(w), 0<|w|<t^{-1}. Inspected the actual 9822-byte RESULT.md and exact checker.py blob; the finite 21360 rational coefficient checks test semigroup and formal matrix identities only, not spectral Fredholm properties.

## originality

PASS

Earlier Galanopoulos–Mahillo–Oliva-Maza–Siskakis (October 15 2026) establishes BMOA/Bloch spectra conditional on the Mellin transform belonging to the extended Dunford–Riesz class E; a nonconstant geometric-lattice Mellin transform F(t^{z-1}) is nonconstant periodic along imaginary translates, violating the required sectorial limit at infinity. The 2024 Abadias–Oliva-Maza general operator-semigroup paper covers Hardy/Bergman/Dirichlet/Korenblum and is mathematically antecedent but, from material inspected, does not provide this BMOA/Bloch Fredholm disk without E. The all-interior infinite-codimensional obstruction, exact analytic F-image, and eigenvalue exclusion survive these comparisons; an older equivalent weighted-composition/cyclic-semigroup theorem remains a real originality risk.

## value

PASS

This is an all-parameter spectral and Fredholm-essential classification for natural discrete Hausdorff operators on two standard nonreflexive holomorphic function spaces. Infinite-codimensional residual obstruction throughout an analytic disk despite atomically supported positive measure distinguishes it sharply from generic boundary-Fredholm formulas; its exact spectral-image property is useful beyond the two-atom example. The exact hypothesis rho>t^{-1}, absence of point spectrum and failure of the prior sectorial assumption make this a motivated structural theorem, not an unmotivated coefficient calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
