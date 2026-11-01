---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

C PASS: The actual RESULT.md fixes n>=3 and each finite field F_q, specifies counting individual matrices rather than orbits. As F_q[t]-endomorphisms of F_q[t]/t^(n+1) plus F_q[t]/t^(n-1), commuting nilpotents have precisely 4n-4 unconstrained higher coefficients after two diagonal constant terms vanish. The four first coefficients form a 2x2 H; the Britnell-Wildon filtered-module argument proves type (n,n) iff H is invertible and (H^n)11=0, leaving q^(4n-8) lifts. A nonscalar 2x2 matrix and its nonscalar power have the same 2-dimensional commutant, so powering bijects similarity classes; each nonscalar invertible class has q-1 representatives with top-left entry zero. Split semisimple, irreducible quadratic and nonscalar Jordan classes contribute (q-1)(q-1-g_-)/2, (q-1)(q+1-g_+)/2 and (q-1)1_{char not divide n} respectively. Combining recovers the exact formula and zero criterion, including characteristic 2 and extension fields. Independently enumerated 40 GL2 prime-field cases; finite enumeration is corroboration not universal proof.

## originality

PASS

O PASS qualified: the exact finite-field existence criterion and filtration reduction are explicitly old, not claimed new. The inspected 2010/2011 Britnell-Wildon Proposition 4.7 asks whether a class has a commuting witness; the final formula counts every witness of that prescribed type in one fixed centralizer and separates g_- and g_+. Hua supplies canonical pair forms rather than this fixed-element finite-field count. Published general commuting-pair generating functions could implicitly yield the same specialization, but no exact direct implication was located after targeted inspection.

## value

PASS

V PASS: A genuine, naturally defined finite-field cardinality and conditional density for a centralizer stratum, over all n and prime powers, refines the known nonexistence test and reveals arithmetic dependence on both q-1 and q+1. This quantitative information is not a routine restatement of the binary existence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
