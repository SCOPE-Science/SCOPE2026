---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The mathematics is unchanged in the repaired RESULT.md. After fixing trace the determinant condition is bc=-f(a). For valuation j<e there are j+1 possible valuations k of b, each with phi(p^{e-k}) choices and p^k compatible c, hence (j+1)phi(p^e). For product zero b=0 contributes p^e in addition to e phi(p^e). The sum of truncated valuations is sum_r p^{e-r}R_r, proving the finite formula exactly. The normalized correction p^{-e-1}R_e goes to zero by continuity of Haar measure on the decreasing root neighborhoods; the intersection consists of at most two points. Split roots are integral, each with mean distance valuation 1/(p-1), including a repeated root. In the nonsplit case distances to the two roots are equal by conjugacy. For a nearest center a0 of valuation distance t, ultrametricity gives v(x-alpha)=min(v(x-a0),t) everywhere. The cumulative tail integral gives H_p(t)=sum_{j=1}^{floor(t)}p^{-j}+(t-floor(t))p^{-floor(t)-1}, strictly smaller than 1/(p-1) for finite t and zero iff t=0. A root modulo p exists iff v(f(x))>=1 at some x; in the nonsplit case 2t is the maximum integer valuation of f. This proves both equality criteria and convergence. For odd p the nonsplit unit residue has t=s if the discriminant valuation is 2s, and odd valuation forces t=s+1/2. At 2 odd trace has two simple roots or no roots according to determinant parity. For even trace translate to y^2-c: odd v gives t=s+1/2, and for v=2s odd squares are 1 mod 8 so the nonsquare units 3,7 give t=s+1/2 and 5 gives t=s+1. Together with the square and zero cases this yields exactly the stated densities. Independent replay /workspace/replay_matrix_mass.py used smooth lifts and a two-level rescale of each singular scalar class, verifying 5400 exact finite counts and 900 level-26 normalized comparisons. Those tests corroborate, not replace, the proof. The uploaded verifier was inspected, not run.

## originality

PASS

Repaired comparison explicitly credits the same-day coverage of every odd-prime finite fiber and the numerical data for the odd-prime limits. The prior attempt with the same valuation decomposition, including dyadic parameters, is now cited and its missing correct counts distinguished by a concrete counterexample. Pass only the supported distinct all-prime root-count formulation with a correct complete classification including exceptional dyadic values and both sharp equality criteria, not priority for the odd-prime finite counts or the valuation method. The theorem remains an exact local statement.

## value

PASS

Precise fixed-polynomial local factors are natural input to trace/determinant counting. After crediting the odd finite counts, the remaining exact formula works at all levels with no assumption of invertibility, simple roots, or odd p, and gives the correct limiting mass for all dyadic and repeated-root parameters. The distinct dyadic corrections and equality cases matter because field-level counts cannot predict their local mass; they expose how much the density changes among indistinguishable nonsmooth reductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
