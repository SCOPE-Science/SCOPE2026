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

Let q=p^d be the smallest prime power exceeding r>=2. Lucas congruence gives f(n)=C(n,r) mod p with period q, so (zeros mod q, count mod p) is a complete p*q DFA. Every state is reachable by 0^r 1^t 0^(N-r). For any two states, suffix blocks 1^k 0 1^k... give affine hyperplanes with coefficient vectors f(a+j); equality of right languages requires proportional coefficient vectors. Their supports have trivial cyclic translation stabilizer because r is in support but r-q/p is not (highest Lucas digit decreases), forcing same a and then same t. Hence every reachable state is distinguishable for every acceptance residue c; sc=p^(2+floor(log_p r)). Independent partition refinement checked all residues in 15 (p,r) choices across p=2,3,5 and tested support translations; the infinite argument is Myhill-Nerode plus Lucas, not the sample.

## originality

PASS

Renard, Rigo, Whiteland give modular word-binomial permutation automata and a minimal four-state (p=2,r=1,pattern 01) example, but the inspected full Section 6.2 does not determine exact general r>=2 state numbers. Related q-Parikh representations are not minimal-DFA lower bounds. No published Resultary exact staircase matched the targeted search; historical unindexed case remains possible.

## value

PASS

Exact minimal complete automaton size for a simple natural modular subsequence language exhibits a sharp prime-power plateau-and-jump law. The state complexity lower bound is a genuine structural rigidity argument, not a routine recognition claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
