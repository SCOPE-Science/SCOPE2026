---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The exact scaled mass and stiffness matrices are 4I+A_n and 2I−A_n, so T=B_r^−1(4I+A_n), B_r=(4+12r)I+(1−6r)A_n. At r≥1/6 the invertible diagonally dominant M-matrix B_r has nonnegative inverse, hence T≥0. For n=3 the cycle adjacency has eigenvalues 2,−1,−1, giving T=J/3+(I−J/3)/(1+6r), all entries nonnegative. For n≥4 and 0<r<1/6, exact cyclic Green kernel G_k=c[(-q)^k+(-q)^(n−k)]/[1−(-q)^n] has G_1<0,G_2>0; G_3=G_1 (n=4), G_3=G_2 (n=5), G_3<0 (n≥6). Therefore T_{0,2}=−6r(2G_2−G_1−G_3)<0. Fresh independent exact rational inverses passed 70 mesh-timestep instances n=3..12, proving selected finite examples only; the Green proof proves all n,r.

## originality

PASS

CRITICAL CLOSE MATCH: Chatzipantelidis–Horváth–Thomée (2015) Theorem 6.5 proves precisely the 1/6 timestep cutoff for one-dimensional uniform P1 consistent-mass Galerkin backward Euler on bounded intervals with homogeneous Dirichlet boundary conditions. This exact numerical threshold and negative second-bidiagonal mechanism are PRIOR and must not be presented as new. The assessed narrower difference is an all-n necessary/sufficient classification for a periodic circle, including exceptional n=3 and an explicit cyclic Green-function proof. The Dirichlet theorem does not literally imply the periodic topology and exceptional triangle case; originality is consequently qualified and limited to this boundary-condition classification, not discovery of the threshold.

## value

PASS

Periodic coupling creates wrap-around Green-function terms and a genuine n=3 exception to the all-n≥4 threshold; a complete necessary/sufficient positivity regime on the circle is useful for positivity-preserving finite-element heat solvers. The new mathematical value is the exact periodic topology classification, not merely recovering the already known 1/6 constant from Dirichlet FEM. This is a narrow but naturally motivated boundary extension with an explicit critical counterexample for each mesh size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
