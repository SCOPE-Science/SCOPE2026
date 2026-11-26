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

The projective conormal bundle is irreducible of dimension N-1, and its scheme fibre is cut out by F and its first derivatives. Independently of the cited hypersurface theorem, generic finiteness onto the image follows once the isolated contact below is exhibited. At a coordinate vertex the available quadratic coefficients are unrestricted for pairs of distinct factors. The alternating polar form of any such quadratic has rank at most r-1, and the triangle plus disjoint pairs attains r-1 with radical vector (1,1,1,0,...) on which the quadratic is 1. These are open conditions on the conormal bundle, using coordinate homogeneity. Eliminate the r-1 nonsingular transverse derivative equations formally: the transverse coordinates have order at least two and F becomes t^2 times a unit, whereas the remaining derivative has order at least two. This gives exactly the length-two local algebra, not just an inseparable differential. For distinct contacts differing in j factors, the two radius-one Hamming balls meet in two vectors for j=1,2 and none for j>=3. The pair locus has dimension r+j and imposes 2r+2-e_j independent linear conditions on the hyperplane. Thus its incidence dimension is at most N-r+j-2+e_j<N-1 when r>=5. For r=3, write the pencil M(z)=z_0 A_0+z_1 A_1. Tangency forces both z-derivatives of det M(z) to vanish: the adjugate is a scalar multiple of the right-kernel times left-kernel vector when the rank is one, and is zero when the rank is zero. Hence beta=0 on the dual. Conversely a nonzero determinant quadratic on beta=0 has a unique geometric root, and on the open locus of linearly independent A_0,A_1 the pencil has rank one there; the two kernels and vanishing determinant derivatives give the unique tangent point. This open is nonempty (for example M=[[0,z_1],[z_1,z_0]]). The polar pairing of beta is nonsingular so the reduced quadric is smooth. Shrinking the reduced dual to avoid images of bad conormal loci and applying generic finiteness and flatness yields length two and exactly one geometric point in a general fibre. This proves separable degree one and purely inseparable degree two. The attached finite symbolic checks were read, not executed.

## originality

PASS

Best-of-knowledge support is for the uniform exact degree and scheme structure for all odd binary Segre products. The characteristic-two Cayley quadric for r=3 and qualitative Segre nonreflexivity are background. The inspected exact matches for analogous degree-two phenomena concern different incidence morphisms; no available inspected statement supplied the uniform degree assertion. The decisive older Segre paper could not be inspected in full independently, so a stronger prior implication remains possible.

## value

PASS

The exact degree of the conormal projection is an intrinsic numerical invariant of a natural infinite family. The result distinguishes a doubled unique contact from higher inseparability or multiple geometric contacts, distinctions not settled by nonreflexivity alone. The length-two mechanism, rather than the known small-format equation, is the informative part.

The dated certificate retains the supplied scientific assessment, sources and limitations.
