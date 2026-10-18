---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For integers m≥1, N≥1 and fixed p∈(0,2], the sharp radius in Hamada--Honda--Kohr Theorem 2.1 is the unique root in (0,1) of p(1−r^m)/(1+r^m)=2r^N/(1−r). The left-hand side strictly decreases and the right strictly increases in r; replacing N by N+1 decreases the right for each fixed r, hence unique roots increase to 1. Put ε=1−R and x=Nε. A root cannot satisfy bounded x as N→∞, because the 2r^N/ε term would blow up; comparison at r=1−C log N/N forces x=O(log N). Consequently Nε²=o(1), log R^N=−x+o(1) and (1−R^m)/(1+R^m)=mε/2(1+o(1)). The exact equation gives x²e^x=4N²/(pm)(1+o(1)), so x=2W(N/sqrt(pm))+o(1); large-W expansion yields x=2logN−2loglogN−log(pm)+o(1). The asymptotic is N→∞ at fixed m,p, not a joint scaling. Independent high-precision bisection: for (m,p,N)=(1,1,10000), x=14.4538717182126408, 2W(...)=14.4636920761867454; for (5,2,100000) x=16.5012445295687707 vs 16.5025324911803368; the error shrinks, but numerical checking is not an asymptotic proof.

## originality

PASS

The 2025 primary paper was inspected across its 19 pages; it establishes the exact equation and optimality, and discusses m→∞ for N=1, not the fixed-(m,p), N→∞ Lambert-W boundary layer. Literature searches, including related powered and high-order radius records, found no prior equivalent log-log constant for this same family. Passing best-of-knowledge is bounded; the input equation and uniqueness are credited.

## value

PASS

The sharp high-tail rate with both a log-log correction and exact pm-dependent constant quantifies how the naturally defined optimal radius approaches 1, a genuine endpoint asymptotic absent from the source. It is a modest exact consequence of a previously published implicit equation, not a new general Bohr theorem; the logarithmic error control is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
