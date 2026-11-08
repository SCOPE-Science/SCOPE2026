---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Militaru 2026 Theorem 2.12, Corollary 2.13 and Proposition 2.15 give the exact orbit model and stabilizer interpretation for nonsplit bipartite solutions. With m=|Z| and k=n-m, m! choices in each tuple position, orbit counts lie between T/m! and T, T=binom(m!+k-1,k). Stirling then gives F_n=m(n-m)(log m-1)+O(n log n) on m in [n/3,2n/3]; strict saddle concavity yields x=m/n=1/2+1/(4log n)+O((log n)^-2) and maximal log term n²/(16log n). For typical m,k~n/2, Burnside fixed-point sum over S_m×S_k is asymptotically identity-only: permutations with f fixed tuple coordinates contribute at most |C_beta|^f (m!)^((k-f)/2), and every nontrivial S_m conjugacy class has size ≥m(m-1)/2. The resulting error tends to zero, so typical orbit stabilizers are trivial and o(m,k)~(m!)^(k-1)/k!, producing the asymptotic weighted sum. Independently computed finite saddle displacement for n=400,2000,10000 and checked prior enumeration; finite tests are not the proof of Burnside asymptotics.

## originality

PASS

Militaru 2026 supplies the exact isomorphism-class formula and automorphism descriptions, not a large-size saddle, the +n/(4log n) canonical block shift, or asymptotic class-weighted rigidity. Prior simultaneous conjugacy theory for fixed G and ordered tuples and general asymptotically free multisets do not immediately imply this jointly growing S_m×S_k orbit count.

## value

PASS

The asymptotics quantify how a newly classified natural combinatorial-algebraic family is distributed among isomorphism types: the 1/16 second-order entropy term, shifted typical canonical block size and rarity of automorphisms are meaningful independent invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
