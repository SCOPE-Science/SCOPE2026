---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For the reversed left brace the lambda action is \(\lambda_g(f)=f(x+g)\) modulo \(x^{N+1}\). If the least nonzero term of \(g\) has degree \(e<N\), testing \(f=x^2\) gives leading change \(2b_ex^{e+1}\), nonzero when the characteristic is not two; every multiple of \(x^N\) acts trivially. Hence the socle is exactly \(Kx^N\). Reduction modulo \(x^N\) is a brace quotient isomorphic to the next truncation, so induction removes one highest-degree coefficient at each step and gives level \(N-1\). For odd prime fields, every strict factor in a finite socle series has additive order at least \(p\), proving the order-based upper bound. An independent direct substitution enumeration reproduced the predicted socle for \((p,N)=(3,2),(3,3),(5,4)\).

## originality

PASS

The exact Nottingham-brace source was materially read through its general construction and Section 4. It constructs the topological right brace on \(x^2D[[x]]\), its filtration, and the Nottingham multiplicative group, but does not compute the finite-truncation socle series or Yang--Baxter multipermutation level in the inspected material. The closest truncated-substitution literature is group-theoretic. A targeted Resultary search returned the audited theorem as the only direct exact result.

## value

PASS

The socle filtration is a natural structural invariant of the newly exhibited Nottingham brace and exactly controls the associated multipermutation level. Over every odd prime field the family saturates the general order bound, giving a sharp structural extremum rather than an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
