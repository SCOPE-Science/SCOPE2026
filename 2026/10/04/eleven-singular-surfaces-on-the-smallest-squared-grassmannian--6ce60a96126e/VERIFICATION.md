---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

From assigned quartic F=det of hollow symmetric 4x4 Q, independently recomputed determinant, all six gradient factorizations and the unit normal Hessian determinant -32 a^2 b^2 c^2 along the generic plane using fresh local SymPy. Group variables as nonzero pair-vectors (a,f),(b,e),(c,d); all three nonzero forces af=be=cd=0, giving eight coordinate planes; exactly two nonzero produces af=be etc. giving one of three rank-4 smooth quadrics, and at most one nonzero is contained in closures. Each component is irreducible and 2D; derivative equations exclude all other support patterns over char≠2. The Hessian at generic plane is nonsingular ternary quadratic, hence transverse formal A1; the identity F=(af-be-cd)^2-4be cd gives transverse A1 at generic quadric (be invertible), and symmetry handles the remaining. Primary Theorem 3.5 proves prime ideal; the quartic is a normal 4D hypersurface by S2 and singular codim2 R1. Generic 2^3-to-1 coordinate square map and normality yield sign-group quotient; its 1|3 and 2|2 involution fixed loci give eight planes and three quadrics. Explicit characteristic and genericity limitations are respected. Symbolic computation is a consistency certificate for algebra, not a replacement for the exhaustive geometric argument.

## originality

PASS

Primary papers describe the precise quartic/hollow determinant and its hyperdeterminant slice, and a general sign-map degree, but the checked relevant sections do not provide the reduced eleven-component singular locus with A1 transverse germs. A hyperdeterminant ambient singular-locus classification does not automatically cover a fixed linear section, which may acquire singularities from tangency. Best-of-knowledge originality is supported for this natural complete local stratification.

## value

PASS

The smallest squared Grassmannian is a standard algebraic-geometric and statistical quartic. A complete reduced singular-stratum description, generic normal slice analytic type, normality and quotient fixed-locus interpretation are cohesive geometric invariants of this natural model. This is not an arbitrary low-degree numeric sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
