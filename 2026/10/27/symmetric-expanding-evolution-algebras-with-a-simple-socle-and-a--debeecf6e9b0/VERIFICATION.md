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

For connected d-regular G and char K !=2, choose nonzero lambda with B=A+lambda I invertible; over Q lambda=d+1 works by adjacency spectrum in [-d,d]. In the displayed natural basis x_{v,+/-}, all distinct products vanish and squares sum B_vw(xw++xw-), so structure matrix is B tensor J2 symmetric. Changing to f_v=xv++xv- and g_v=xv+-xv- gives f_v^2=g_v^2=2 sum_w B_vw f_w, f_vg_v=0. The square I=span f_v has dimension n; connectivity and invertibility imply it is simple. Multiplying any nonzero ideal element by a suitable f_v or g_v yields a nonzero square in I, whence I lies in every nonzero ideal. Every subspace above I is an ideal since E*E=I, so ideal lattice is {0} plus subspaces of E/I. The symmetrized support graph is G[K2], and fiber-even/odd Laplacian decomposition gives 2 Spec(L_G) plus n copies of 2(d+1), with gap exactly 2lambda2(G). For finite odd q>n+1 choose invertible shifted adjacency, giving 1+sum Gaussian binomial ideals. Direct symbolic graph-spectrum checks for n=2,3,4 passed. Uniform family does not impose unrealizable coefficient positivity or infer algebraic simplicity from graph connectedness.

## originality

PASS

Compared mathematical objects and implications, not merely similar titles: Giacomelli 2026 Theorem 3.8 asserts symmetric expansion implies algebraic simplicity, but its proof wrongly conflates connectedness with simplicity; this concrete family contradicts it under the paper’s undirected support definition. General theorem every subspace containing E² is an ideal does NOT imply there are no other nonzero ideals; that needs the simple square and essentiality proof. Tensor constructions alone do not determine connected blowup expansion with spectral gap 2lambda2(G). Residual priority risks documented, including uninspected plausible original sources; absence of search hits is not assumed to certify novelty.

## value

PASS

A concrete fixed-degree expander family where graph expansion fails to enforce simple symmetric evolution algebras directly refutes a published theorem, and simultaneously provides the full ideal lattice, simple essential square ideal, Laplacian spectrum and finite-field ideal counts. These nontrivial interacting algebraic and graph properties go well beyond a one-vertex counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
