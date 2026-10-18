---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For Cr_n=K_{n,n} minus diagonal matching, every vertex on side A has an occupied neighbor in B iff |J|≥2, and symmetrically |I|≥2. If an outside A-vertex a_k is inserted in exchange for adjacent b_j, the new B-count falls to |J|−1; the exchange remains total dominating iff |J|≥3. Thus only I=[n] avoids that requirement; symmetrically J=[n] or |I|≥3. The two pairwise exclusive regimes are |I|,|J|≥3 and |I|=2,J=[n] or reverse. The polynomial is [sum_{k=3}^n C(n,k)x^k]^2+2C(n,2)x^{n+2} for n≥3. The first nonzero coefficient yields γ_st(Cr3)=5 (6 sets), γ_st(Cr_n)=6 for n≥4 (28 n=4, C(n,3)² n≥5). Direct independent swap-by-swap enumeration on every subset of Cr3..Cr6 agrees with the criteria and polynomial. No inference beyond enumerated range is needed because the swap criterion proves all n.

## originality

PASS

Best-of-knowledge priority judgment based on direct statement/implication comparisons with specified inspected sources, published semantic search and alias checks; neither the source names nor negative searches by themselves demonstrate novelty. Aliases crown, K_n,n minus a perfect matching/1-factor, and bipartite Kneser H(n,1) were searched as equivalent graphs; none of the retrieved entries supplies the all-set crown polynomial or stated swap-index criterion.

## value

PASS

Deleting a perfect matching is the defining crown graph operation and it changes defender choices in a non-monotone domination parameter. The full set-size generating polynomial (not only the minimum) and exceptional endpoint layers are natural graph invariants useful for enumerative secure domination, giving a genuinely structured difference from the complete multipartite formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
