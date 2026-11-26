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

With n active bounds the remaining entry is C = k(A+B)-nB. The condition -A<C<B constrains k to an open interval of length one; at an endpoint the all-bound multiset is unique. Thus all vertices are a single permutation orbit, integral and primitive (both bounds occur; at the simplex endpoint B=1). On the sum-zero real representation its second-moment matrix has identical diagonal entries and identical off-diagonal entries, hence restricts to (R s/n)I. A nonzero functional has at least R/n nonzero evaluations by the squared-norm bound. A Demazure root would have only two nonzero evaluations, -1 and 1, since the ray sum vanishes. The interior-free orbit has at least n(n+1) vertices; the all-bound nonsimplex orbit has at least choose(n+1,2) with n≥3. The only exceptional nonsimplex case is n=3,A=B=1, where a root would vanish on two of the three opposite ray pairs; subtracting the resulting integral character equations gives equal coefficients in each pair of coordinates and an even evaluation on the remaining ray. At (n,1) the simplex evaluations are all congruent modulo n+1, again excluding a root. The complete toric root theorem therefore gives identity component T. Every lattice fan automorphism preserves primitive vertices and hence Q. For A<nB both coordinate bounds are facets: set the other entries to A/n or -B/n to exhibit relative interior points. Their normal lines are permuted, and the unique all-ones dependence forces one common signed scaling, which unimodularity makes ±1. Inversion preserves the facets' support values exactly for A=B. At the simplex endpoint only upper facets remain, so the common sign is positive. Finally T is characteristic, and any automorphism preserves its unique dense orbit; translating the image of the torus identity back to identity makes its restriction the group automorphism given by conjugation on T. Thus the fan group is an actual finite complement, not just a quotient of the expected size.

## originality

PASS

Passes for the full coprime parameter interval and endpoint distinctions only. The (2n−1,2) group result is explicitly known in a distinct indexed finding, and the family and structural toric tools are already known. Neither constitutes the family-wide root exclusion and precise component classification.

## value

PASS

This determines the connected and disconnected symmetries across a natural alpha-spectrum family in its actual lattice, including the centrally symmetric inversion jump and the potentially misleading simplex endpoint. The uniform orbit estimate and the endpoint arithmetic give a reason for rigidity beyond reiterating the previously computed specialization. The exact symmetry group is useful for identifying torus actions and possible equivariance in this family, without a claim about all toric Fanos.

The dated certificate retains the supplied scientific assessment, sources and limitations.
