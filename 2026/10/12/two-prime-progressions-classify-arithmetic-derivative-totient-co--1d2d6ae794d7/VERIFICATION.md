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

For all primes r>7 and positive a,b,c, the exact logarithmic derivative and totient identities reduce equality to (24−7a−5b)r=35c+24. Positivity leaves only (a,b)=(1,1),(1,2),(1,3),(2,1); modular 7 and 5 exclude the middle and last. The other two yield respectively r≡2 mod35 with c=(12r−24)/35, and r≡12 mod35 with c=(2r−24)/35; minimum primes 37 and 47 give c>0. Both residues coprime to 35, so Dirichlet proves infinitely many primes. Our independent integer enumeration over all 58 primes 7<r<300 obtained exactly the four predicted qualifying supports; this is corroboration, not the infinite proof.

## originality

PASS

OEIS A166374 already poses D(n)=phi(n) and lists 3788435=5·7³·47², which lies in the second branch; Dahl–Olsson–Loiko present the standard arithmetic derivative identity. The assessed addition is the complete classification in a motivated fixed first-two-prime support and two infinite prime progressions. No checked named prior result implies their precise necessary-and-sufficient pair, but an unindexed elementary derivation is a material risk.

## value

PASS

The fixed support is motivated by the explicitly recorded first three-prime numerical instance, rather than an arbitrary test of isolated parameters. It upgrades that example to an exhaustive infinite two-progression classification with necessary-and-sufficient exponent formulas. Though elementary linear congruence algebra, the exact full-support family and infinity statement supply an independently reusable answer to a natural constrained Diophantine question; no broader classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
