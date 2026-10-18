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

The entire derivation space is D(a,b,c) with diagonal entries (a,2a,3a) and subdiagonal entries (b,b,c); the automorphisms are G(h,t,u)=[[h,0,0],[t,h²,0],[u,ht,h³]], h!=0. Matrix conjugation yields a fixed, b→hb−at/h, c→h²c+a(t/h)^2−2au/h. For a!=0 and odd q, t kills b and u kills c; in char 2, after killing b the invariant Δ=ac+b² is zero or nonzero, all nonzero squares being equivalent in F_{2^s}. For a=0,b!=0, c/b² classifies, giving q orbits size q−1. For a=b=0, square-class quotient of c gives two odd-characteristic or one even-characteristic orbit; zero singleton. Sums reproduce q³, including q=2 and3. Source matrix finite-field verifier enumerates q={2,3,4,5,7,8,9}; all-field proof uses no invalid division by 2 in characteristic 2.

## originality

PASS

Best-of-knowledge non-coverage after primary statement and implication comparisons. The claim is not made new merely because a text query lacked an identical title.

## value

PASS

The finite-field conjugacy quotient of infinitesimal symmetries is a natural classification invariant, and characteristic-two splitting into Δ=0/nonzero produces genuinely different moduli and orbit statistics not supplied merely by the two standard matrix tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
