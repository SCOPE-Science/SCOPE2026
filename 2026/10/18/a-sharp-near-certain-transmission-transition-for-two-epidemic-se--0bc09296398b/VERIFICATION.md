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

Exact source conditioning gives nD=2+sum_{r<=a}p^r+sum_{r<=c}p^r+sum_{r=1}^{b-1}(p^r+p^{b-r}-p^b), where a+b+c=n-1, a,c>=0, b>=1. Difference on moving a>0 one step outward equals p^b(1+b(1-p))-p^a; H(a,b)=p^{b-a}(1+b(1-p)) grows strictly with a and decreases with b, so its least permissible value is g_n=p^{n-3}(1+(n-2)(1-p)). For g_n>1 every outward move improves; at equality only the final one-step moves tie; for g_n<1 moving endpoint inward improves. g_n has unique interior peak at p=1-(n-2)^(-2) above one and hence unique interior root, with p=1 also a boundary root. Taylor expansion at p=1-y/(n-2)^2 proves the constant 2 limit. Separately exhaustively enumerated percolated edges, every source and every sentinel pair for n=4..8 and p=1/4,1/2,3/4,9/10 with rational arithmetic: all formulas matched. The finite test does not prove arbitrary n.

## originality

PASS

Newman establishes percolation representation and Holme studies epidemic sensor importance using discovery time; neither gives this exact unconditional detection probability placement threshold for all n. The exchange argument isolates a new sharp near-certain-transmission crossover and scaling.

## value

PASS

The non-obvious fact that endpoint placement becomes uniquely optimal only in a sharply quantified near-certain-transmission window is a natural finite-network sensor-placement phase boundary. The exact exchange law and 2/(n-2)^2 scale are useful beyond a small numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
