---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Start edge 2 vertices, each attachment samples uniform vertex then uniform neighbor; stars have probability s_n=2/(n-1). For n>=4 diameter<=3 precisely J_n<=2 with all nonleaf vertices adjacent. Mark second internal vertex and b of its leaf neighbors. The exact surviving-double-star recurrence is q_{n+1}(b)=[n-2-b+1/(b+1)]q_n(b)/n+[b-1+1/(n-b)]q_n(b-1)/n+2*1_{b=1}/[n(n-1)]. It has correct star-to-two-hub birth and kills trajectories producing a third internal vertex. Stable n*q_n(b) limit yields c_1=4/3, c_b=4/[b(b+2)] at each fixed b. Fractional moment F_n=sum b^(1/8)q_n(b) has drift bound F_{n+1}<=(1-17/(16n))F_n+2/[n(n-1)], leading F_n<=64/n, so no mass escapes to b→infinity, and summation gives total 3. Star contribution 2 yields nP(diam<=3)→5, with conditional mass 4/[3b(b+2)]. Independent rational history enumeration through n=8 is encoded in checker, and an independent n=1800 recurrence calculation gave nP(J=2)~3.01543 and nP(diam<=3)~5.01654. Infinite asymptotics rely on tightness and stable-recursion proof.

## originality

PASS

Best-of-knowledge PASS: exact result and mathematical object are not established by accessible identified prior statements; reviewed aliases, reductions, stronger coverage and checked data. Distinct original ingredient: correction of omitted predecessor factor and summably tight fixed-hub asymptotics. Residual priority and access risks retained.

## value

PASS

Corrects published rare-event two-hub asymptotic constants in a natural preferential redirection/random friend-tree model and determines the full fixed-secondary-hub limiting distribution. The identified omitted b−1 term changes not merely a normalization but individual coefficients from b=3 onward, and the no-mass-escape argument is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
