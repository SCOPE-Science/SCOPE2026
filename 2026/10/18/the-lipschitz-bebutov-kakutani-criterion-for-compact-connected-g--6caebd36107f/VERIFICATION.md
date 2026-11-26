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

The Haar-normalized tent functions concentrate at the identity. The correlation formula uses only right invariance to bound the Lipschitz seminorm. For the Fourier convention used here, convolution multiplies matrices in order, and the involution becomes adjoint. Each correlation has positive semidefinite blocks, and on any fixed irreducible block all sufficiently late tents have invertible transforms; their positively weighted sum is therefore strictly positive definite on that block. Peter–Weyl gives injectivity without a uniform inverse bound. The kernel is a Lipschitz probability density; rewriting the integral with k(xb^{-1}) gives the stated Lipschitz bound after subtracting constants. Left convolution commutes with right shifts. The Jaworski–Chen observable embedding, shrunk around 1/2 and composed with Q, stays in [0,1], is 1-Lipschitz, and is still equivariant and injective. Compactness and the uniform topology give a topological embedding. The shift-fixed functions are precisely the constants. Connectedness enters only through the continuous embedding theorem.

## originality

PASS

Credit the existing connected Lie and Euclidean cases, the connected locally compact continuous-shift theorem, and the broader Borel embedding. The distinct claim is the continuous Lipschitz criterion on the compact connected non-Lie branch of Problem 1.3, for every compatible right-invariant metric. The convolution construction supports that claim without a priority assertion for every kernel ingredient.

## value

PASS

The theorem resolves a genuinely non-Lie part of an explicit embedding problem for all compact connected metrizable groups and for the specified metric rather than a smoothing-adapted replacement. The information-preserving convolution estimate also separates a reusable compact-group analytic step from the topological dynamics input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
