---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The pure generators x_i^d cover Proj because every retained monomial has a d-th power built from the pure ones. On D_+(x_i^d), every retained ratio has z-total degree >=2 (all tangent-linear ratios deleted); for d>=5, ALL quadratic and cubic z-monomials occur and generate all degrees >=2, so the exact chart is B=k+m². Its normalization S=k[z1,..,zr], r=n-1, is finite integral and birational: z_j=z_j³/z_j², z_j satisfies T²-z_j², and away from m it becomes an isomorphism. Conductor m², cokernel spanned by r linear classes, exactly n distinct singular coordinate points and an exact global skyscraper sequence. For r>=2, 0→B→S→k^r→0 and regular S show depth(B_m)=1. The tangent quotient m²/m⁴ gives embedding dimension C(r+1,2)+C(r+2,3); length(B/m^(2(q+1)))=C(r+2q+1,r)-r proves multiplicity 2^r. Birational normalized hyperplane pullback O(d) gives degree d^r, H¹(OY)=nr, H^j=0 j>=2, and χ(OY(t))=C(dt+r,r)-nr (t>=0). An independently programmed monomial-semigroup/HS checker corroborated four (n,d) choices, not the infinite theorem.

## originality

PASS

Best-of-knowledge PASS: canonical simultaneous deletion of EVERY coordinate tangent monomial in arbitrary degree d>=5 and dimension r>=2 produces the same isolated local model plus full conductor, cohomology and Hilbert–Samuel invariants. Caviglia's original cubic pinched Veronese deletes one different monomial; Caviglia–Conca treats a one-point projection of the cubic surface. Maddox–Pandey Section 5 multi-pinch hypotheses require deleted monomials have maximal exponent STRICTLY BELOW d-1, while this family deletes vectors whose max exponent is exactly d-1. Their theorems therefore do not cover this tangent deletion, though monomial semigroup methods are well known. Possible implicit toric local-singularity classification remains genuine risk.

## value

PASS

Simultaneously removing all first-order coordinate tangent vectors is a geometrically intrinsic symmetric projection of the Veronese embedding, not arbitrary monomial slicing. Uniform depth-one nonnormal points, exact conductor/cokernel lengths, Hilbert–Samuel multiplicities and global irregularity give natural intrinsic invariants across every dimension and sufficiently high degree, unaddressed by known Koszulness results for single pinches. These enable subsequent work on singularities and nonnormal projective embeddings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
