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

Independently reconstructed RESULT.md §§Character reduction–Strict sign. Subtracting exterior-square trace from unordered-pair trace gives 2Q=1+χ_W−χ_U. Tensoring with the permutation character is Ind Res: W and U both contribute V and (n−3,2,1), which cancel in their difference; the remaining difference is χ_W−χ_U+χ_X−χ_Y. The five dimensions and ratios follow from the hook and content formulas, valid also at n=6. In the centered moment only X, Y and the products of the V ratio with W and U remain, with ρ_Vρ_W=a. For n≥7, a−c=12/[n(n−1)] and b is the strict convex combination of a,c with the stated weights; Jensen gives the strict sign including c=0 at n=7. For n=6, b/a=3/5 and c/a=−1: the even and odd brackets are respectively −15a^t+15b^t and −9a^t+15b^t. Time 0 and 1 have deterministic counts. Independent n=5 replay by cycle type: after two transpositions the path counts for identity, 3-cycle, and two 2-cycles are (10,60,30). From these types the transitions to a lone 2-cycle, a 4-cycle, and a (3,2) are respectively (10,0,0), (3,6,1), (2,4,4), by splitting or joining cycles. Thus the third-step path counts are (340,480,180) out of 1000; E[F]=3/2, E[Q]=13/25, E[FQ]=51/50, giving 6/25. The supplied Python and its stored finite output were inspected, not executed; neither substitutes for the proof.

## originality

PASS

Pass for the exact non-lazy discrete covariance and uniform strict sign with the n=5 boundary, not for the central-character machinery or individual cycle-count moments. The strongest indexed overlap shares the mixed-character identity but treats a different transition operator and a different sign law.

## value

PASS

The fixed-point and two-cycle counts are the first two canonical cycle statistics. A sign rule at every nontrivial time, with an explicit minimal-size counterexample and a qualitatively different published holding-kernel behavior, is an exact structural statement rather than a single-time recomputation or marginal law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
