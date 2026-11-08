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

C PASS. For F_k=kx^2(1-x), 4<k<=16/3, the nonzero fixed points solve kx(1-x)=1, with lower repeller ell, upper u. Factor F_k(x)-ell to obtain remote return R. The invariant interval [ell,R] has F((ell,R)) inside (ell,R), and the exact two-cycle ratio t=y/x>1 yields k-16/3=(t-1)^2*(3t^4+12t^3+14t^2+12t+3)/(3t^2(t^2+t+1))>0. Coppel no-prime-two convergence implies all interior states tend to u; outside states tend to 0, boundary R maps to ell. Uniform probability 1+ell-R and its monotonic endpoints follow. Independently symbolically checked cycle parametrization and threshold factorization. Coppel theorem used as cited established global iteration theorem.

## originality

PASS

Best-knowledge PASS, qualified: GAL special case and fixed points are known, but no actual inspected primary result states both exact basin edges, exact initial-state extinction proportion, and sharp period-two-free window. The 2026 GAL full text and older population papers were not fully available; this residual access risk is NOT evidence of noncoverage.

## value

PASS

V PASS. Complete two-sided extinction basins on the natural entire biological state interval and a sharp bifurcation boundary give a useful, nonlocal dynamic phase classification; initial density too high can also cause extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
