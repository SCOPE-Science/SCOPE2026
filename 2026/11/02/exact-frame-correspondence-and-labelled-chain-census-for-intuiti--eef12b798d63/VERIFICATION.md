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

For upsets U, Diamond p is D(U)={w: all v>=w all A in N(v) meet U} and Box top is stable-world set S={s: all t>=s N(t) nonempty}. If SNDR holds, any A disjoint from U at v>=w admits B contained in down A at some stable s>=w, so implication Box top -> Diamond p fails there and I_Diamond holds at w; if SNDR fails, U=W\down A is an upset falsifying I_Diamond at witness w. This proves exact arbitrary nonempty preorder correspondence including empty families and infinite W. For labelled chains, rank(A)=-1 for empty, otherwise max A; the last empty row and least suffix rank yield exact sum over ell,m. The n=1,2 direct Kripke truth-table evaluation produced C1=4,C2=241; independently evaluated formula gives C1=4,C2=241,C3=16690673,C4=18446303034659832065. Strict 3-world counterexample N(0)={{2}}, N(1)=empty family, N(2)={{0}} satisfies SNDR but not continual support; earlier sizes cannot. Large counts are exact integer evaluation of an algebraic formula, not proof by finite search.

## originality

PASS

Necessary-and-sufficient stable-neighbourhood downset refinement replaces a prior sufficient continual-frame criterion; labelled chain count and minimal counterexample are distinguishable from canonical completeness results. Best-of-knowledge new, general correspondence may have an older different notation.

## value

PASS

It exactly characterizes the intended interaction axiom on arbitrary frames, separates a previously convenient sufficient class from actual validity, and counts all concrete labelled chain frames; this supplies a nontrivial semantic invariant and exact finite model benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
