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

The shift in the second coordinate reduces all distinct two-cycles to ordered abscissae u<v with cv=1-aS(u), cu=1-aS(v). Thus the two abscissae are the two inverse points at a common level of g=aS-cx, and the orbit exists exactly when H(k)=k+c(u+v)=1 above the minimum level. Since a>c>0, the vertex is c*epsilon/a strictly in the core; g decreases and increases strictly on the two respective sides. When both inverses are in the core their sum is constant. In the mixed branch the left slope has magnitude at least a-c (the right slope), and with two outer inverses its magnitude is a+c, so H increases throughout. Its lower and two interface values, divided by epsilon, are (a^2+3c^2)/(2a), (a^2-ac+2c^2)/a at the right threshold, and (a^2+c^2)/(a-c) at the left threshold. Inverting these gives the unique branch and all switch values; enforcing the ordered inverses selects the displayed roots. At the first switch the mixed polynomial has derivative -2(a-c) in u, zero epsilon derivative, and second epsilon derivative 2a^2, giving the quadratic onset. The core squared half-gap is 2*epsilon*(1-epsilon/epsilon_*)/a; at the merger the fixed point's one-step polynomial is (lambda+1)(lambda-b). The determinant of the return is b^2 and its trace is 2b+m(u)m(v) for m(x)=aS'(x). This product begins at -a^2, then increases continuously and strictly to c^2 (use the mixed square-root expression and the core 1/epsilon term). Hence the upper Schur condition holds on the whole primitive branch, and the lower condition is R>-(1+b)^2. At equality the other multiplier is -b^2; below it only one has modulus greater than one. Substitution at R=-W yields both formulas for epsilon_s; the separator is R(epsilon_2)=2ac-a^2, including agreement at equality. The double abscissa at epsilon_* is not counted as prime period two.

## originality

PASS

The supported distinct claim is the complete prime-two classification for the specified quadratic smoothing: exact outer/core switching, coordinates, endpoint laws, and stability-transition formula over the full stated parameter domain. The smoothing, the Lozi limit, prior fixed-point work, and any applicable known fixed-point flip calculation are not credited as new. The same-map 2001 article and associated reported 1999 preprint were not accessible in full after reasonable lawful attempts; the choice is based on the checked statements, not on treating missing material as noncoverage.

## value

PASS

The family was introduced to compare smoothed and piecewise-linear dynamics; the exact period-two diagram answers where smoothing has no effect, where the orbit first moves, and when it can turn a saddle into a sink. The distinct switch and stability thresholds and their ordering are usable information beyond a Lozi-limit comparison or a local fixed-point calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
