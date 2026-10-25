---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

For μ_r=2^(2^(3r)), v2(μ_r)≥8, excluding all even m≤144 by comparing v2(m/2+μ_r)=v2(m)-1. For odd nonsquarefree m a prime square p²|m forces p|m/p but p∤μ_r, hence condition fails. The remaining exactly 58 odd squarefree 3≤m≤143 are exhausted by an independently recomputed orbit test: for each p|m, x1=2^8 mod p and x_{r+1}=x_r^8 mod p; if -m/p mod p is absent from the finite orbit, no r works. Fresh code confirmed a blocking prime for every candidate, 33 different blockers and maximal orbit length52. The invariant 2^8≡111 mod145 and 111^8≡111 mod145 yields μ_r≡111 mod145, and 29+111 divisible by5 and 5+111 divisible by29, so 145 satisfies all r. The finite m-bound is complete, while the orbit recurrence proves uniformity over infinitely many r.

## originality

PASS

Best-of-knowledge priority assessment distinguishes the actual joint/exact invariant and mathematical implications from stronger but non-covering frameworks; pertinent primary statements were compared and residual risks are explicit. Uniform least mu-Sondow number 145 for mu=2^(2^(3r)), r≥1

## value

PASS

An exact constant least-witness law along the natural infinite Fermat-index subsequence refines the foundational small-witness conjecture in a nontrivial way: existence of a witness for one parameter or all parameters does not imply simultaneous sharp minimality. The finite obstruction table is substantively motivated by the arithmetic dynamics x→x^8.

The dated certificate retains the supplied scientific assessment, sources and limitations.
