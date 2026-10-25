---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For positive probability polynomial P and unilateral Hardy shift S, T=M_P; reproducing-kernel norm equality makes D_{n,h}=max_t |P(e^{it})|^n |1-P(e^{it})^h|. Triangle equality gives contacts at t_j=2πj/d, d=gcd(k-k0); their peripheral values traverse q=d/gcd(d,k0)-th roots, and after lag h all Q_h=q/gcd(q,h)-th roots. Exponential suppression holds away from contacts. Near any contact log P(e^{is})=iμs-(v/2)s²+O(s³) with log|P|=-(v/2)s²+O(s⁴). If Q=1, optimizing |s|e^{-nvs²/2} yields hμ/sqrt(e v)n^-1/2 and O(n^-3/2). If Q even, a peripheral contact P^h=-1 gives exact norm2 for every n≥0, matched by universal upper bound2. For odd Q≥3, the maximal roots ζ=e^{±i(π-π/Q)} give B=2cos(π/(2Q)), derivative a=hμ Im(ζ)/B², an optimizer s=a/(nv)+O(n^-2), and positive correction h²μ²sin²(π/Q)/(2B³v)n^-1+O(n^-2). Strong convergence follows boundary dominated convergence away from finitely many contacts; ||T^n||=1; for each r use h=r to rule out Ritt of T^r. Independent norm optimization checks P=(1+z)/2 (Gaussian), P=(z+z³)/2 (exact2), P=(z+z⁴)/2 (odd Q3 + coefficient) at large finite n; not a proof of asymptotic generality.

## originality

PASS

Best-of-knowledge originality is for the precisely new contribution, excluding acknowledged prior-covered premises/corollaries. The four structured implication comparisons and genuine source inspections support noncoverage within a bounded search, not an absolute proof of novelty.

## value

PASS

A natural exact operator-theoretic problem for positive averages of shifts: it determines all possible lagged norm behaviors, including exact even-order extremality, Gaussian decay and a sign-definite n^-1 correction at odd peripheral roots. The arithmetic quantity Q_h and sharp constants quantify strong-stability versus operator-norm regularity and provide counterexamples to automatic Ritt behavior. This structural classification is mathematically motivated rather than a selected numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
