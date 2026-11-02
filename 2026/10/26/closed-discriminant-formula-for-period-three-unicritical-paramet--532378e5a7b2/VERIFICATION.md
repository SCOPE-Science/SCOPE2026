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

Write m=d-1, h(t)=t(t+1)^d+1 and G(c)=h(c^m). Its derivative h'=(t+1)^(d-1)((d+1)t+1), and h(-1)=1, h(-1/(d+1))=1-d^d/(d+1)^(d+1). Evaluating resultants at these derivative factors gives Res(h,h')=R=(d+1)^(d+1)-d^d. Composition product over m-th roots gives Res(G,h'(c^m))=R^m and Res(G,m c^(m-1))=m^N(-1)^(N(m-1)) for N=d^2-1; multiplying and the discriminant sign (-1)^(N(N-1)/2) simplify to (-1)^(d+1). R positive for d>=2, so polynomial discriminant nonzero and exact v_p formula follows. Independent exact small-d discriminants confirm sign and powers. This is not a number-field discriminant or a higher-period result.

## originality

PASS

Hutz–Towsley establish the same exact period-three parameter polynomial family and characterize bad characteristic through discriminants, with explicit d5/d7 factorizations. Buff studies the equivalent transformed polynomial t(t+1)^d+1 and irreducibility, and Goksel related Misiurewicz arithmetic. Inspected full source mathematical statements do not state the boxed all-d closed discriminant; nonetheless the classical resultant calculation is short and earlier specialist implicit derivations are a material risk.

## value

PASS

Dynatomic critical-orbit discriminants control bad-reduction/transversality primes in a well-motivated arithmetic dynamical family. Exact all-degree prime support and valuations extend previously displayed isolated d5/d7 cases and provide a natural unknown invariant, even though the resultant method is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
