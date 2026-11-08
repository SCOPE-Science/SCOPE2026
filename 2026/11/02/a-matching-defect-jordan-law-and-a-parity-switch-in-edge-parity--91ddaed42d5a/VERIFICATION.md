---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: The loopless line-graph adjacency is F=B^T B in characteristic two; connected root graph gives im B=W (even-sum) and ker B^T=span(1). For odd n, on W, BB^T swaps each deleted matching pair and fixes unmatched vertices, yielding rank(I+R)=k, Jordan J2(1)^k, and E-n+1 semisimple zero modes; F^3=F. For even n, BB^T on W is nilpotent pair-block map R^2=0, rank F=n-2 and rank F²=k if k<n/2, otherwise n/2-1-1_{n/2 even}; this gives J3/J2/J1 multiplicities, extinction-time distribution, and last-deletion parity reversal. Independent GF(2) rank/polynomial checks on 60 n,k instances, n<=14, corroborate proof.

## originality

PASS

Qualified: incidence Gram identity and general finite-linear-map dynamics are classical. The explicit full matching-deleted clique char-2 Jordan stratification and perfect-matching parity threshold were not found in relevant inspected sources.

## value

PASS

PASS: Matching deletions form a canonical perturbation of cliques. The exact all-parameter characteristic-two Jordan census provides complete evolution and basin counts and reveals parity-controlled oscillatory versus nilpotent dynamics and a genuine perfect-matching rank transition not visible in real line-graph adjacency ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
