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

Applied finite Heyting duality: G_{m,n} is the upset algebra of m disjoint n-element chains and endomorphisms correspond to isotone open p-morphisms f with f[↑x]=↑f(x). Each source component maps to a single target component and surjects onto a final segment; onto a final segment of length j it has C(n-1,j-1) monotone block maps. If f²=f, every active target final segment S must be fixed pointwise, forcing its source-chain map uniquely. Every inactive chain independently maps onto a final subsegment of one of r active components, with b_n(k_i)=∑_{j<=k_i}C(n-1,j-1) choices for target i. Labeling active chains of each multiplicity c_t gives m!/[(m-r)!∏ c_t!] and the displayed product. The algebra image is exactly Upsets(S), so its factors are C_{k_i+1}; different length multisets give nonisomorphic dual posets. Counting all nonempty multisets gives C(m+n,m)-1. Independent brute-force finite p-morphism enumeration matched closed ranks for (m,n)=(1,3),(2,2),(3,1),(2,3),(3,2), including I_2,2=2z²+4z³+z⁴+2z⁶+z⁹ and 59 idempotents at m3,n2. Arbitrary powers follow from p-morphism reasoning, not finite tests.

## originality

PASS

Finite Heyting duality and unrestricted Gödel algebra hom-set counts are published antecedents. The natural exact idempotent-retraction image-type spectrum and its labeled multiplicities are not stated in primary Yamamoto text or accessible Aguzzoli–Mordonini abstract. The latter full 2025 chapter was inaccessible through lawful OA and authorized institutional access (VPN disconnected), creating explicit overlap risk but not alone requiring rejection.

## value

PASS

Finite powers of Gödel chains are a natural family in finite Heyting algebra theory, and retraction-image isomorphism types/ranks refine unrestricted hom-set and automorphism counts. The full multiset-resolved formula, C(m+n,m)-1 count, and image-rank polynomial supply precise invariants for all powers, distinguishing images with equal cardinality but nonisomorphic factors. This independently motivated complete classification uses an accessible dual structural proof, not an arbitrary small-parameter census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
