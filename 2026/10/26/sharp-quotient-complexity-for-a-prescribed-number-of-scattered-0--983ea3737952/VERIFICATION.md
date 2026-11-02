---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The concatenation identity c01(uv)=c01(u)+z(u)#1(v)+c01(v) derives from partitioning ordered 0-before-1 pairs into left, right and cross-boundary pairs. Every reachable nondead quotient for fixed k has form R(a,t)={v:a#1(v)+c01(v)=t} with a=z(u), t=k-c01(u); any a>=1,0<=t<=k is reached by u=0 1^(k-t) 0^(a-1), and a=0 yields the initial quotient. Collapses: R(a,0)=0*, and 0<t<a is empty. For a<=t<2a, quotient is uniquely 0^(t-a) 1 0*, giving ceil(k/2) distinct single-one quotients. For 1<=a<=floor(t/2), 1<=t<=k, the two successful exponent tests 0^j1 and 1 0^j1 determine j=t-a and j=t-2a, hence determine a,t; this contributes sum_{t=1}^k floor(t/2)=floor(k²/4) multi-one quotients. Initial quotient and 0* and dead are pairwise distinct, including k=0 initial 1*0*, so Myhill–Nerode gives 3+floor((k+1)²/4). Independently built the full saturated counting DFA and minimized it by fresh partition refinement for k=0..34, matching every count; that is bounded confirmation of the exact quotient proof.

## originality

PASS

Fixed scattered-subsequence frequency is classical, and recent authors study exact word counts or binary Parikh-matrix classes. The claimed invariant is the exact minimal complete automaton state count of the all-length language with c01=k, not the number of finite words, the universality index, or the existence of at least one subsequence. Four materially compared works on those adjacent parameters do not imply the stated quotient formula; a potential unindexed automata note remains a risk.

## value

PASS

The language L_k is canonical for subsequence multiplicity, and the minimum COMPLETE DFA size directly measures optimal streaming memory required for exact recognition for each fixed k. A complete Myhill–Nerode classification with a sharp quadratic law and exact floor correction is an independently useful state-complexity invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
