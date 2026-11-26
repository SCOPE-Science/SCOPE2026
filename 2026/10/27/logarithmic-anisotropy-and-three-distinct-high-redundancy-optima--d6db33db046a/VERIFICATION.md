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

The sharp normalized a_n,b_n formulas match Faulhuber–Shafkulovska (8.1); a common density factor does not affect any optimum or the quotient. Their Theorem 2.7 and §8 cover all integer n≥2 with distinct small-n arguments. For large n, the published interval I_n=(arccosh n,4 arccosh n) contains 2 log n+c uniformly for bounded c, so the sign changes bracket the global optima using the cited strict log-concavity/log-convexity and global upper-bound convexity, not merely local Taylor series. Put x=eta/n and z=e^(−eta). Expanding x csch x, x coth x, tanh(eta/2), coth(eta/2) and eta csch eta gives the three stated remainder bounds also after differentiation: the neglected orders are bounded by a constant times x^4+(1+eta)z²+x²z in the layer. The derivative factors after extracting eta/n² are −1/3+2e^(−c), 2/3−2e^(−c), and 1−4e^(−c), with nonzero derivatives at their respective zeros. This yields all three offsets with O((log n)^3/n²) error and the two persistent gaps. Subtracting at c=0 gives the claimed limiting profiles with the correct optimizer types. Evaluating the quotient at u_n=2 log n+log 4 gives coefficient u_n²/2+u_n+1; the shift to the true optimum changes the value by less than the stated remainder since the leading derivative vanishes there and the layer curvature is O(log n/n²). At eta=sqrt n the leading quotient is cosh(1/sqrt n) up to O(sqrt n exp(−sqrt n)), yielding excess 1/(2n)+O(n^(−2)+sqrt n exp(−sqrt n)) and ratio n/[4(log n)²]. The recorded 85 finite checks were inspected in source, not rerun; the exact formulas and analytic localization justify the asymptotics.

## originality

PASS

Relative to the established Gabor theorem, the dated frozen finding provides a distinct sharp high-density refinement: three noncoalescing next-order constants, scaled objective profiles, and an explicit comparison of the best rectangular choice with the square lattice. The two identified catalogue records elsewhere state equivalent asymptotics for major parts of the claim, one with a sharper optimizer-error bound. They directly cover those mathematical statements, and this finding is not claimed to have exclusive current catalogue coverage. Both are indexed later than the frozen finding and neither attributes these exact asymptotics to a source shown to predate it. The recorded dates and lack of citation do not establish historical priority, independence, or derivation. No inspected antecedent yielded these sharp asymptotics. The square penalty is part of the useful combined refinement, not a priority claim based on a routine substitution alone.

## value

PASS

For a fixed natural window with exact sharp bounds, the finding resolves whether three practically different notions of an optimal aspect ratio merge or stay distinct at high density. The finite additive separations and scaled profiles quantify the tradeoff, and the diverging square penalty calibrates the consequence of using a natural benchmark geometry. This adds quantitative information to the qualitative optimizer order, rather than just renaming the aspect parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
