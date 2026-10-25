---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For each prime p≡3 (mod 8), the quadratic character identities (-1/p)=(2/p)=-1 yield a∈F_p× with a²=-2. The four distinct sites 0, u=(0,1), v=(a,0), v-u carry values (1,-1,ζ,-ζ) and their unnormalized Fourier evaluations at the four sites are pairwise exactly canceling; this establishes σ_p≤4 uniformly, including p=3. For the lower bound p≡3 mod4 implies x²+y² anisotropic. One-point Fourier diagonals never vanish; two-point principal determinant reduces to ζ^{Q(w)}−1 with nonzero w. On any three-point support translate to {0,u,v}; principal determinant (ζ^A−1)(ζ^B−1)−(ζ^C−1)². If C=0 it cannot vanish. If C≠0, all roots nontrivial and comparing positive sines with the unit phase forces A+B=2C as ordinary integers and equality in the sine midpoint identity forces A=B=C; then Q(u−v)=0 contradicts anisotropy. The normalization 1/p is nonzero and does not affect zeros. All quantifiers are analytically proved; checks are finite corroboration only.

## originality

PASS

Best-of-knowledge exact invariant σ_p=4 for every prime p≡3 mod8: Zhou 2026 Proposition 3 supplies self-disjoint support 2p-2 and treats the p≡3 mod4,d=2 minimum as difficult; it already covers p=3, but not the uniform four-point p≥11 witness. Prior published 3×3 minor and three-sparse spectrum results imply parts of the lower bound but not the new four-point construction. Primary cyclic Fourier, Fourier-support cardinality and finite ternary incidence results do not by their stated implications cover the uniform coincident-support condition. Publisher abstract of a plausible 2007 broader paper is not enough to certify noncoverage; retain substantive residual priority risk. O PASS is qualified and not a historical priority certificate.

## value

PASS

The smallest support size with self-disjoint physical and Fourier supports is a natural principal Fourier-matroid invariant explicitly singled out as difficult for p≡3 mod4 in Zhou 2026. The sharp σ_p=4 is an exact infinite-family classification, improving the concrete prior size 2p−2 construction strictly for p≥11; matching impossibility of 1,2,3 points matters independently. The sqrt(-2) arithmetic witness and anisotropy obstruction give structurally meaningful reasons for the congruence restriction; no general downstream theorem or paper-sized claim is needed. It is not simply a table lookup or a renaming of an established numerical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
