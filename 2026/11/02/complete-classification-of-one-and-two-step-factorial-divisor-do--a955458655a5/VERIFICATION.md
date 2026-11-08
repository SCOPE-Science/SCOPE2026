---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=1, K(n) tests tau((n+k)!)/tau(n!). The exact local ratio R(t)=product_{p^a||t}(V_p(t-1)+a+1)/(V_p(t-1)+1) and estimate R(t)<=exp(S(t)/t) are reconstructed. If t>=2048 is composite, split by largest prime <=sqrt(t) or >sqrt(t), isolating a large prime factor with cofactor a>=2. Consecutive-composite bounds outside cofactors 2,3 are (45/34)^2, (3/2)(15/13)^2, and (9/5)(45/44)^2, all <2. Cofactors 2 and 3 with both complementary large factors prime give product >2. Independent exact integer computation for 2<=m<2048 found 60 double-composite two-step hits: 55 prime-pair and five exceptions 8,15,20,25,34, and the only composite one-step factor m=4. Thus K=1 iff n+1 prime or n=3; the stated K=2 classification exhausts all n, with no infinitude asserted for simultaneous-prime families.

## originality

PASS

Freiberg arxiv:2609.15597 studies the same K(n), bounds and sparse large values; Erdős–Graham–Ivić–Pomerance (1996) study n! divisor growth. They do not in their accessible indexed statements give the exact K=1/K=2 classification, prime-pair alternatives and five exceptional windows. The standard exponential bound is acknowledged as prior. The highly plausible Freiberg primary full text could not be retrieved despite arxiv/OA and authorized institutional attempts, so no whole-document noncoverage assertion is made.

## value

PASS

The first two exact fibers of the natural factorial-divisor doubling waiting time K(n) describe how a prime jump or pairs of composite integers can double tau(n!). The arithmetic alternative of two linear prime forms, isolated by a rigorous uniform cutoff and five exceptions, is a genuine infinite-domain classification of a specific mathematical quantity, not finite table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
