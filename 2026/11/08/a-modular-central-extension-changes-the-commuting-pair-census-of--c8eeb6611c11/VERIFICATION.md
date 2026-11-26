---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For truncation x^(p+2), differentiating the relation forces f(0)=0 because 2 is a unit. The coefficient of degree j+s−1 in fg'−gf' has diagonal (s−j)a_j multiplying b_s. For 2≤j≤p the only allowed resonance is s=j, which is in range precisely when j≤(p+1)/2. Subtracting a multiple of f at that entry leaves only the free tail s>p+2−j, of dimension j−1. At j=1 the last diagonal coefficient is p=0, and f and x^(p+1) account for both degrees of freedom; order p+1 is central. The x^(p+1) quotient truncates the same triangular system one step earlier and removes only the j=1 top resonance from that range; its cutoff for the s=j resonance stays the same because p is odd. Counting zero and each order with its q^dim centralizer gives both polynomials and the fixed-p limiting ratio. The classes of e_2 and e_p commute downstairs but all lifts have the same bracket (p−2)e_(p+1)≠0, including p=3. A fresh exhaustive calculation gives (C(L), C(L'))=(945,153), (589761,13041), (540625,45625) for (p,q)=(3,3),(3,9),(5,5), and direct ordered-pair enumeration independently gives 945 for L over F_3. Replay with Python 3: /workspace/branches/636bdfe2-4000-4b40-8423-fc87000f8064/independent_reproduction.py. The proof, not exhaustion in these fields, covers all extension degrees and odd primes; the uploaded verifier was read only.

## originality

PASS

The elementary triangular method is closely related to known Witt-algebra centralizer calculations, but the compared theorem does not give centralizers at the two higher truncations, their finite-field censuses, or the effect of this specific nonsplit extension. Qualified to this canonical pair of truncations and the modular resonance, not to Witt centralizers in general.

## value

PASS

This is a complete centralizer and commuting-pair census for a natural modular truncation, not selected small fields. The quantitative comparison distinguishes the actual central extension from a split stabilization: their leading commuting counts differ by a factor tending to 2/(p+1), and the deficient lift is explained by the surviving degree-p+1 commutator. The exact order strata make the result reusable for finite fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
