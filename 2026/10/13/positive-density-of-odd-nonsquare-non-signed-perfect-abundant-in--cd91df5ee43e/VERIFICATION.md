---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a fixed odd abundant square a with C=σ(a), C−2a=2h+1 and an odd nonsquare cofactor m coprime to a with b=C(σ(m)−m)<m, the signed-perfect subset target H=(σ(am)−2am)/2 lies strictly in (hm+b,(h+1)m). Every sum of eligible proper divisors has shape Am+B with 0≤B≤b, hence cannot equal H. The cofactor sift R_Y (no prime divisor ≤Y) has density ρ_Y; G_Y(m)=sum_{p|m>Y}(p−1)^(−1) controls log(σ(m)/m), with normalized mean at most ρ_Y/Y +o(1) from exact coprime residue counts. Markov bounds bad cofactors by ρ_Y(C+1)/Y; removing O(√X) squares and scaling by a establishes the stated positive lower density, not an exact density. Independently checked σ(11025)=22971>2*11025 and 4459 finite sample cofactors; sampling is not the proof.

## originality

PASS

Ross Conjecture 17 proposed universal signed perfection; Campbell 2026 Theorem 3.1 disproves it with an infinite prime-cofactor odd nonsquare family and Theorem 2.4 constructs positive-density EVEN counterexamples. Neither checked result establishes positive LOWER density in the odd nonsquare subfamily. The present cofactor sieve upgrades the latter qualitative question with explicit positive bound. This is a best-of-knowledge implication comparison, not uniqueness certification.

## value

PASS

The arithmetic motivation is directly Ross's odd nonsquare abundant signed-perfect conjecture and Campbell's sparse counterexamples. Positive lower density distinguishes a substantial proportion of failures from mere infinitude; the bound is explicit and uniform across any chosen odd abundant square, supplying a reusable fixed-anchor sieve theorem. This is not a mechanical substitution into the previously reported even density statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
