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

PASS. Embedded uniform-feasible-edge chain obtained from exponential edge clocks has drift x’=-x(y+z), y’=-y(x+z), z’=-z(x+y). Exact scalar first integral u’=(1-au)(1-bu)(1-cu) gives x=a(1-bu)(1-cu) etc and u→1/a. Martingale quadratic-variation+Gronwall yields finite-time fluid LLN; post-T edge count dominated by small parts when a>b or total residual when a=b, establishing terminal convergence. Integrating each edge-type intensity under u gives AB=b(1-c/(2a)), AC=c(1-b/(2a)), BC=bc/(2a), and unmatched (a-b)(a-c)/a. With s=(b+c)/a, xy≤s²/4 establishes sharp R>=7/8 and equality only a:b:c=2:1:1. This is an asymptotic-in-probability/expectation theorem for positive linear part fractions only; no finite-order universal ratio.

## originality

PASS

PASS best-of-knowledge. Dyer--Frieze introduced the random feasible-edge greedy algorithm; Hertz et al explicitly discuss that algorithm but analyze the UNIFORM average over maximal matchings, a distinct distribution. Arnosti treats random bipartite graphs and random edge sets. No inspected source supplied dense deterministic complete-tripartite type limits or sharp within-class 7/8 ratio; Dyer--Frieze full text not acquired this cycle, priority remains qualified.

## value

PASS

PASS. A sharp asymptotic performance benchmark and unique worst-shaped tripartition quantify a natural stochastic matching algorithm on a dense heterogeneous graph family; the exact edge-type fluid distribution has standalone use and exceeds routine examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
