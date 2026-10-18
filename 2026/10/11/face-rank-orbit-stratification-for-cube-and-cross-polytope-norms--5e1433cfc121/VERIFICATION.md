---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For l1, equality throughout ||Tx||<=sum|x_i| ||Te_i||<=1 forces active source columns to be supported in the target support (also over C by equality of the triangle inequality); invertibility forces s(x)<=s(y). Conversely column-stochastic perturbations y+epsilon h_i with independent zero-sum h_i and weighted zero mean provide s independent nonnegative columns of norm 1, extendable to an invertible contraction. For linfty, an output modulus-one coordinate forces its row to vanish at every input coordinate of modulus below one; invertibility forces r(y)<=r(x). Conversely exact active rows and epsilon-corrected remaining rows give a block triangular invertible map with row l1 norms <=1. Faces have real dimensions s-1 on l1 or delta_F(n-r) on linfty, delta_R=1, delta_C=2; the support strata are open and dense in the relative sphere and form precisely n ordered classes. Complex matrices use xbar_i at active coordinates and phase-normalized isometries; positive real constructions extend over C.

## originality

PASS

The primary original semigroup-dynamics article supplies the real two-dimensional l1 two-stratum example and shows that flat outputs are attainable from any input; it does not classify each finite-dimensional l1 and linfty reachability preorder nor the exact chain of all n face-rank strata over BOTH real and complex scalars. Published semantic corpus results found other cube/crosspolytope geometric constants and contractive projection bounds, not this invertible-contraction orbit theorem. The full exact support-rank classification with constructive invertible witnesses is a substantive additional result beyond the source example.

## value

PASS

The detailed orbit preorder is a natural invariant of the semigroup of contractive automorphisms, and knowing exactly when a boundary vector can reach another strictly strengthens the source flat-point existence result. It yields a complete n-level face-rank stratification and dense open orbits in both dual coordinate norms, with real/complex uniformity and constructive witnesses. That is a structural classification, not an isolated illustrative calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
