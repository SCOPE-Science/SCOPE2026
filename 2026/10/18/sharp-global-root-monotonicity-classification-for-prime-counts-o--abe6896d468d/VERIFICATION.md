---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

For x=nk≥17, A=π(x), B=π(x+n), c=ceil(n/2), at most c odd prime candidates give Δ=B−A≤c. Therefore (k+1)log A−k log B≥log A−kc/A. Rosser–Schoenfeld’s unconditional π(x)>x/log x and monotonicity of y log y reduce sufficient positivity to 1−(log log x)/(log x)>c/n. For n≠3, c/n≤3/5 and (log log x)/(log x)<2/5 for x≥17; for n=3 use <1/3 for x≥128. Both logarithmic comparisons follow from elementary monotonic x^2/log^5 x and x/log^3 x with checked endpoints. Independently enumerated all 71 distinct remaining (n,k) with integer powers A^(k+1),B^k, finding precisely reversed (2,1),(2,2) and tie (4,1); also corroborated a larger independent sample. Thus full n≥2,k≥1 domain follows analytically plus a genuine exhaustive finite boundary.

## originality

PASS

Sun’s published prime-count root conjecture only concerns n>4 and 1≤k≤n. The actual claim supplies all k without bound, n=3 full ray, and exact n=2,4 exceptions. A broader documented earlier proof of all unbounded rays was not found in the searched primary material; other independently known prime-count root monotonicity inequalities remain a literature risk.

## value

PASS

An exact unrestricted two-parameter completion of a published arithmetic conjecture, achieved with a general uniform analytic argument and a finite sharp boundary; resolves the natural infinite-index extension rather than merely reproducing bounded-index computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
