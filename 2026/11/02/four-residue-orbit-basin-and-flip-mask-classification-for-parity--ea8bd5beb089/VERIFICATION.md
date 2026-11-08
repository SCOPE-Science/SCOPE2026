---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For all n≥5, N=binom(n,2), the KG(n,2) loopless binary adjacency is exactly A=I+BᵀB+J over F2, with B the vertex-edge incidence matrix of K_n. The identities T²=(n mod 2)T, TJ=JT=0 and J²=(N mod 2)J imply A²=I for n≡0; A³=A for n≡1,2; and A²=A for n≡3 (mod4). Rank T equals n−2 for even n and n−1 for odd n, giving exact rank A and rank(A−I), so all states are either periodic or enter a period≤2 orbit after one update. Each periodic point has equally sized preimage fiber, yielding the table of fixed states, 2-cycle orbits and basin sizes. The flip map (A+I) on im A has image T+J, J, T, 0 by residue, respectively. im T is the even-cut space for even n and the all-ones mask lies outside it. Directly recomputed the adjacency matrices and F2 ranks for n=5..11 and flip-space dimensions, corroborating the symbolic all-n proof. Four residue cases and the sharp first-entry time are addressed, not spatial automorphism-orbit classes.

## originality

PASS

Best-of-knowledge original full XOR KG(n,2) dynamical census and allowable temporal flip-mask multiplicities. Real spectral properties of two-set Kneser graphs and modular incidence ranks are background and can imply parts of rank calculation, but do not alone classify periodic orbit basins and cut-mask distribution. Resultary prior parity automata records concern distance-two Boolean cubes and complete multipartite graphs, non-isomorphic graph families with differing adjacency operators.

## value

PASS

A natural synchronous F2 network on the classical KG(n,2) family has exact global dynamics and mod-four phase transition. The result identifies all attractor classes, uniform basin sizes, and spatially meaningful even-cut oscillation masks, not merely a restated matrix rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
