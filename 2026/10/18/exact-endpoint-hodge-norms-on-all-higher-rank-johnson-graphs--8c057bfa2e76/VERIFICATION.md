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

# Computational and analytical verification

The included `verify_johnson.py` can be executed using `python verify_johnson.py` with Python 3 and no third-party dependencies. It constructs the original graph and its grounded vertex Laplacian, solves the Poisson equation in exact rational arithmetic, sums every edge current in the test column, and compares the resulting two projection norms and effective resistance to the theorem. It also independently groups the vertex potentials by stabilizer orbit and checks their ordering and the two moment identities.

The exact cases \((n,k)=(4,2),(5,2),(6,3),(7,3),(8,3),(8,4),(9,4)\) passed. The first two are previously known controls; the remaining five cover higher Johnson ranks and include the balanced cases \((6,3)\), \((8,4)\). For the largest example there are 126 vertices and 1260 edges. Five additional exact-rational orbit-chain tests at \((n,k)=(10,5),(18,9),(40,20),(100,3),(100,50)\) passed, independently verifying the combinatorial recurrence and both moments for larger parameters. These finite exact checks corroborate, but do not replace, the symbolic proof for arbitrary integer parameters.

Analytical checks: verify that positive-vertex multiplicities obey detailed balance, that the level-difference tridiagonal matrix has positive inverse, that the total zero-potential and sign-changing edge contributions are not double counted, and that the trace normalization for the diagonal entry is \((\binom nk-1)/|E|\). All four checks are built into the derivation in `RESULT.md`.

The theorem is about specified orthogonal projections only. It does not establish unrestricted minimal projection constants or norms at non-endpoint exponents. A prior equivalent statement under another electrical-flow terminology remains a bibliographic risk. Independent review has not been performed.
