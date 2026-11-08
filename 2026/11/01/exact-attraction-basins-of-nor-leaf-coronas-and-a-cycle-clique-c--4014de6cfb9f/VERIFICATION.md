---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For each finite simple loopless undirected G, synchronous open-neighborhood NOR on its single-leaf corona acts on core/leaf subsets by F(A,L)=((V\L)\N_G(A),V\A). Setting B=(V\L)\N_G(A) ensures cross-nonadjacency N(A)∩B=∅ and F(A,L)=q_{B,A}; symmetry yields F(q_{A,B})=q_{B,A}, hence F³=F, all states enter a 1/2-cycle after <=1 step. The phase pairs are independent sets of the bipartite double cover, and fixing one phase q_{A,B} forces the predecessor core B while precisely |N(B)| private-leaf bits are free. This proves each basin weight and its complete partition. On K_n the fixed basin count is 1+n2^(n-1). On C_n direct cyclic 3-state transfer has characteristic t³-t²-2t-2, initial trace 13,25,61 and the stated recurrence. Exact recurrence checks through 19 and a strict induction using b_{n-1}+2b_{n-2}+2b_{n-3}-b_n=(n-9)2^(n-3)+4 for n>=9 prove the unique crossover at 17 for all sizes. These arguments address isolates and n=1, and the special cycle n>=3.

## originality

PASS

Qualified PASS for every attractor and precise individual basin weight on one-leaf open-NOR coronas and the exact cycle–clique n=17 reversal; general NOR eventual-period-two facts and independent-set transfer machinery are acknowledged prior.

## value

PASS

This is a complete, natural graph-family nonlinear-dynamics census, not a disconnected finite simulation. The arbitrary-G orbit/basin bijection and weight polynomial are exact observables; sharp cycle/clique crossover demonstrates nonmonotone topological effects with a provably different exponential fixation rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
