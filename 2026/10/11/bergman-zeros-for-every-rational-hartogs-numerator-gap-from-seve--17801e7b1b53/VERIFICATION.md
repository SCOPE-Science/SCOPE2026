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

Reconstructed the primary equation (3.21) as Q=m^2 s^k+sum_{j=1}^{m-1} s^e[j+(m-j)s^k][m-tau+tau s], with e=floor((kj-1)/m) and tau=kj-me. For n=kq+r, each exponent block has affine endpoints a(q+1)+floor(ar/k)+1 and (a+1)(q+1)+floor((a+1)r/k), with final endpoint m-1. Summing 1,j,j^2 symbolically proves degree at most three in q; the joint quadratic summands ensure that bound. A separately authored exact rational reconstruction summed these endpoints, rather than interpolating four samples, for all 84 reduced residues at k=7,...,17. Chebyshev conversion gave F=A+qB+((k+r)q^2+(k/3)q^3)H, with H=(2+cos theta)|sum_{j=0}^{k-1}exp(ij theta)|^2>=0. Coefficient identities for q^2,q^3 were checked exactly in every residue. Integer-scaled de Casteljau subdivision at depths 4,6,6,6,7,8,8,8,8,9,9 respectively showed every Bernstein coefficient of A and B exceeds 1/200. Hence F>(1+q)/200 for every q>=0. All phi(k) residues (6,4,6,4,10,4,12,6,8,8,16) are included. Auxiliary direct-formula comparisons at q=0,1,2,3,4,13 check indexing but are not the infinite argument. Reciprocity, degree 2k, nonzero endpoints and strict circle positivity give exactly k roots inside and k outside, counted with multiplicity. Each interior root realizes product coordinates (s,s) using sqrt-modulus domain points; this is not z=w, and the kernel denominator is nonzero.

## originality

PASS

Best-of-knowledge originality of the exact normalized positivity and root-count claim. The claim covers all coprime n for each gap 7 through 17, not merely selected infinitely many n per gap. Fixed gaps 1 through 6 and the n=1 integer family do not imply this coverage. The common Bernstein method does not make the new parameter-uniform statements duplicates. Searches alone are not the novelty argument; the inspected primary statements and mathematical implication comparisons below are decisive within the documented scope.

## value

PASS

This gives a contiguous partial classification of a published nonvanishing conjecture: every coprime numerator in each gap 7 through 17, including infinitely many n per gap and the first gap with 16 residue classes. Exact certificates settle natural missing finite-gap cases beyond the reported smaller gaps. The value is complete all-parameter coverage in these gaps, not a claim to solve arbitrary gaps or a merely selected numerical sample; the common method alone is not a new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
