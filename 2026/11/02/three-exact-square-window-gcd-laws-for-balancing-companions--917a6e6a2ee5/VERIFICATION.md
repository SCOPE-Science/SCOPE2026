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

The three sequences B,C,c satisfy X_{n+2}=6X_{n+1}-X_n with specified initial values. Classical identities C_n^2=8B_n^2+1 and c_n^2=(C_{2n-1}-1)/2 give first-window sums, and telescoping gives window differences B_k B_{2n+k+2}, 8B_k B_{2n+k+2}, and 8B_k B_{2n+k+1}. Strong-divisibility gcd(B_a,B_b)=B_gcd(a,b) reduces the infinite gcd to explicit gcd of initial sum and a multiple of B_k. Proof then splits primes 2 (B_k and k share exact 2-adic valuation; mod16 normalization), 3 (B_2m has nu3=nu3(2m)+1 and extra 3 for odd multiple of 3 only c), and other odd primes. Thus D_C=gcd(k,B_k); D_B=h/2 for even k otherwise h; D_c=3h if k=3 mod6 otherwise h for every k>=1. Independent exact arithmetic checked all three against 20 actual windows for k=1..59; finite checks corroborate, infinite follows from valuation proof.

## originality

PASS

Mbirika–Schrader–Spilker 2023 Question 30 explicitly states the proportionality conjectures from experiments but not a proof, nor the common explicit index gcd D_C(k)=gcd(k,B_k). The adjacent 2022 generalized Fibonacci case has different recurrence and initial conditions. The three statements as proven are a partial resolution of open published question. A later unpublished/in-preparation followup is concrete priority risk.

## value

PASS

Theorem resolves three of four natural infinite-window gcd sequences requested in a named published question, reducing infinitely many start indices to one finite gcd of k and the balancing number and identifying parity/3-mod6 effects; substantive exact number-theoretic result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
