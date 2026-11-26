---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The potential change for a flip from 0 to 1 is exactly the payoff change; on an update of a single uniformly chosen vertex, the forward/reverse probability ratio is the ratio of the two Gibbs weights. At finite β the chain is irreducible with self-loops. Conditioning on the anchors makes each incident leaf contribute A or B. Since the two unanimous numerators depend only on the fixed edge count, their respective probabilities and their sum all have the same optimizer. For unequal A,B the discordant-anchor terms combine into a positive multiple of cosh(log(A/B)(s−s_*)); minimization means nearest feasible integer, including endpoint clamping, with a two-way tie only at a feasible half-integer. Equal A,B gives a constant partition function. Independent enumeration of the 16 paw-core profiles gives C01=t³+t²+2t, C10=t⁶+2t²+t, C00=t C01, C11=t² C10. Expanding C10 A²−C01 B² and C10 A⁴−C01 B⁴ gives the positive and negative factorizations in RESULT.md:58–66 for t>1; hence 0<s_*<1. Directly Z0−Z1=(B−A)(C01 B³−C10 A³)=−t²(t−1)²Q(t). Q has two sign changes and brackets of opposite signs on (0,1) and (2,3), so exactly one root is feasible; its sign gives the stated switch and tie. Bisection gives t≈2.005236660909933, β≈2.08728626747837. The degree-square sums from the stated degree sequences are 44 and 46. The frozen check.py was inspected, not executed; its advertised 88 comparisons count 84 direct-versus-pinned partition checks plus four adjacent-allocation comparisons. The analytic argument covers all β>0 within this design family, not every graph or a mixing-time optimum.

## originality

PASS

The Gibbs representation, conditional factorization and convexity are established techniques, not originality claims. The checked literature and catalogue do not supply the exact nearest-feasible-integer rule for the pinned-core allocation problem together with the unique finite-rationality paw switch. A low-rationality regularity theorem on a larger graph family does not solve the constrained problem on this nonregular family, much less at all rationalities.

## value

PASS

The closed-form rule is usable for any finite core once the pinned partition sums are known; it avoids enumerating or comparing the whole leaf-budget family. The paw then gives a minimal-complexity explicit witness to a genuine phenomenon, not a claim of smallest among all graphs: the topology maximizing a fixed stationary objective can change at a provably unique positive rationality and favor a larger degree-square sum. This quantifies the limits of using a low-rationality regularity heuristic throughout the finite-rationality range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
