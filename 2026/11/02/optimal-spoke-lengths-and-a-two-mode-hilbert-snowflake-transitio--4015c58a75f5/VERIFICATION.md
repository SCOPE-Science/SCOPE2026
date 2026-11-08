---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n>=4 and 1/2<=r<=1, shortest-path distance between nonadjacent rim points is 2r, adjacent 1, hub-rim r. The zero-sum powered-distance form decomposes exactly into the hub-vs-mean scalar g=(n−3)(2r)^p+2−2nr^p and the orthogonal nonconstant cycle modes -a||u||²+(1−a)<u,Au>, a=(2r)^p. Since min cycle eigenvalue is -2c_n, nonpositivity is precisely a<=a_n=2c_n/(2c_n−1) and g<=0. Both constraints are monotone in p, yielding min{p_g,p_s}, strictness, nullities and embedding dimensions by Schoenberg. Substituting the contrast threshold into g yields unique crossover r*=b_n^{1/p*}, p*=log2(a_n/b_n), b_n=((n−3)a_n+2)/(2n). Implicit g_r at its root =-2p/r<0, hence p_g strictly rises while p_s falls; yields unique maximum. Independent shortest-path and projected-matrix eigenspectra for n4..13, multiple r and p on both sides, agree including n4 center-of-square p=2. Taylor formulas correctly separate fixed r<1 from r=1 and odd/even parity.

## originality

PASS

Obata 2017 Theorem 1.1 and Lou–Obata–Huang 2020 Example 3.6 provide unweighted p=1 wheel QEC and parity baseline. These do not imply an exact variable-spoke, variable-exponent threshold, unique optimal radial weight, competing global/oscillatory critical modes or boundary-layer asymptotics. Robertson supplies Hilbert/negative-type criteria rather than computed weighted wheel invariants. Resultary wheel polytope ellipsoid deals with a different invariant. Residual risk: an older radial two-distance metric negative-type theorem might specialize to this family.

## value

PASS

The weighted wheel is a canonical center-plus-cycle shortest-path family; its Hilbert snowflake threshold and optimum spoke length are natural metrics in embedding geometry. The full two-parameter classification, parity-dependent equality dimension, and sharp n^{-1} transition window provide a useful precise invariant beyond the previously known unit-spoke parity case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
