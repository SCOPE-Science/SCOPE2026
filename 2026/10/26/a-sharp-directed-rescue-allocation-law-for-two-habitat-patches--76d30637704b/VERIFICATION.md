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

The transient CTMC has states 10,01,11 and absorbing 00. The 3x3 backward system is (e1+u)t10-u t11=1, (e2+v)t01-vt11=1, (e1+e2)t11-e2 t10-e1 t01=1. The determinant e1 e2(e1+e2+C)>0. Solving exactly yields the three rational t values in RESULT.md; independent symbolic solution reproduced all formulas. Substituting v=C-u and weighting α,β,γ gives T'(u)=[C+α e1-β e2-2u]/[e1e2(C+e1+e2)] and T''=-2/[...]. Strict concavity proves unique projection onto [ell,C-r] including endpoints, positive initial weights, asymmetrical extinctions and singleton feasible range. Completing the square proves exact regret identity. Independently validated rational benchmark e1=1,e2=4,C=2: t11(u=v=1)=8/7, one-way 31/28, state10 optimum u=3/2 gives 121/112. Not extrapolated to n>2 patches.

## originality

PASS

Exact direction-specific fixed-total-colonization optimization for finite two-patch CTMC and arbitrary initial distribution is narrower than established stochastic-patch conservation but not directly supplied by inspected primary statements. Day–Possingham (1995) has state-space matrices and two-patch examples for discrete time rather than this continuous-time budget. Etienne–Heesterbeek (2001) reports qualitative colonization/extinction prioritization rules, which could be close but its complete text could not be accessed and Oxford VPN was disconnected. Ross–Pollett (2009/2010) optimize homogeneous Levins-style colonization/extinction budgets. This merits qualified best-of-knowledge O, not a claim of definitive priority.

## value

PASS

The natural conservation-control question is how to allocate a fixed directional rescue budget to maximize a metapopulation’s time to extinction. The exact optimizer, threshold for abandoning one direction, dependence on the initial distribution and explicit regret are mathematically interpretable, potentially useful for small-patch models, and not a mere table lookup. The four-state chain is intentionally minimal but gives a full, nontrivial quantitative policy boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
