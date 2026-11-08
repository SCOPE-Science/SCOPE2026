---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Weyl integration constant-term identity and Clebsch–Gordan yield μ2=1, μ3=1 even (0 odd), μ4=n+1, μ5=T=(5n²+10n+8)/8 even (0 odd), μ6=S=(n+1)(n²+2n+2)/2. Independent coefficient-array Laurent constant-term calculation n2..19 verified all μ2..μ6, independent of package script. Since tensor multiplicities μj are nonnegative, aligned nonnegative coefficients maximize each fixed-magnitude complex pair; even μ3>0 enforces phase alignment when mixed. Odd n>=3 use cubic Bernstein control values 1,5,5(n+1),S, all strictly less than S except final => pure chi_n uniquely optimizes. For even n, Q=P_n(x)/(1+x²)^3, derivative 6H_n/(1+x²)^4; H(0)>0, remaining coefficients nonpositive with strictly negative high terms, so exactly one positive root and K>S. Asymptotics H(c/n)/n²→5/8-c/2 yield x_n=5/(4n)+O(n^-2) and gain 75n/32+O(1). This supports all n analytically; finite moment checks do not establish full maximizer quantifier.

## originality

PASS

Closest published same-SU2 result found was a moving high-weight packet sharp fourth-moment theorem; it differs both exponent and inclusion of trivial character. Older compact Lie group character-norm studies determine individual-character growth, but accessible evidence does not establish the exact two-character sixth-moment parity optimizer. Best-of-knowledge originality, explicitly retaining inaccessible 1982 relevant primary full-text risk.

## value

PASS

Exact L2-to-L6 synthesis constant and complete extremizing lines for the natural smallest nontrivial central Fourier span containing one high-weight character. The parity threshold distinguishes odd pure-character rigidity from even strict mixing, with quantified x~5/(4n), K−S~75n/32. Such a sharp compact-group spectral concentration invariant is not a routine calculation of an individual character moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
