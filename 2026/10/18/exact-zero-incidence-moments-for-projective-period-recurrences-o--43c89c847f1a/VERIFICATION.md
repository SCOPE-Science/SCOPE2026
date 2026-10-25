---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

PASS: Irreducibility identifies F_p^d and the order-L element; gcd(L,p-1)=1 makes any nontrivial mod-p power non-scalar, hence distinct lag rows independent. A^L=I+pB and centralizer F_p^d with non-scalar B guarantees B is nonzero/invertible and the rows ell,ell B independent. Odd-p binomial lifting gives exact period T_k=Lp^(k-1) for every primitive state; N_k=(p-1)p^((d-1)(k-1)). For lag divisible by L with valuation j, the pair constraints row-reduce to x1=0,p^j x2=0; primitive solutions count (p^(d-2)-1)p^((d-2)(k-1)+j). Other lag counts and the diagonal give mean (p^(d-1)-1)/(p-1) and variance (p^(d-2)-1)(k-1). Independently enumerated all primitive cubic p=3,k=1,2,3 cycles and moments. Hypotheses d≥3, odd p, gcd(d,p-1)=1, nonscalar lift all used, k=1 checked.

## originality

PASS

Best-of-knowledge claim-versus-prior assessment with direct source comparisons; see four named checks, source inspections and retained risks.

## value

PASS

PASS: General exact prime-power zero-hit covariance is a natural quantitative invariant of projective Singer-period recurrences over finite local rings. It extends fixed-seed period methods to any nonzero linear observable and separates projective orbit geometry from depth-dependent fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
