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

From the basis law XY=rho(X) tensor gamma(Y). A basis sandwich of any element of nonzero augmentation yields every basis element up to the same nonzero scalar. Thus proper ideals lie in J. Multiplication by each basis element on either side forces P into an ideal with images U,V; the image conditions give I contained in H, and the same multiplication identity proves sufficiency. P already realizes both images, proving uniqueness. Split each sum map using a coordinate basis vector, so the two non-annihilator summands of H already belong to P; inclusion of R0 tensor C0 induces the asserted canonical quotient. The dimension of P follows by its intersection V tensor U, and counting planes in that quotient gives the stated polynomial. Products of augmentation-zero elements range over a spanning set of R0 tensor C0, using the chosen sum-one vectors; this space annihilates A on both sides. The radical designation also follows in the unitization since J is nilpotent and the quotient of the unitization by J is k x k. For the geometric assertion, on the rank loci the images of the universal ideal bundle are subbundles. Universal H and P are subbundles over the base Grassmannians with quotient the specified vector bundle. Taking I/P and taking inverse images are mutually inverse regular constructions; the dimension and smooth geometric irreducibility follow on the reduced strata in every characteristic. Independent reproduction: python3 -B /workspace/reproductions/rectangular_ideals.py grows subspaces as sets of vectors via one-dimensional extensions and tests both multipliers from the basis law on every word. For (m,n,q)=(2,3,2),(3,2,2) it scanned 2825 subspaces each and got histogram (1,3,4,4,4,1,1); for (2,2,3),(2,2,4) it scanned 212 and 529 and got (1,1,2,1,1). The finite checks corroborate the algebraic argument, not the scheme geometry or arbitrary-field assertion by extrapolation.

## originality

PASS

The supported distinct claim is the combination of all proper linear ideals with their dimension census and reduced rank-stratum geometry for the bare rectangular band. Neither the standard rank-one sandwich description, the known radical context, nor the inspected nearby semigroup and quiver theorems determine this census and geometry without a further analysis of the common invariant subspaces. This is a bounded priority judgment, not a claim to a new product law or radical theory.

## value

PASS

The full ideal locus of these natural nonunital semigroup algebras is meaningfully richer than the semigroup ideal structure or the radical alone. The canonical fibers give both the exact dimension-by-dimension finite-field counts and geometric structure of each rank stratum across all rectangle sizes and field characteristics. This is structural information, not an isolated census or a general claim about components of the full scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
