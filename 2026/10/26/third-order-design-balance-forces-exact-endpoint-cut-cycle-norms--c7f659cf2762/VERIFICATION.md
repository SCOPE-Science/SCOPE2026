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

For a source incidence (i,S), eliminating block potentials leaves the scalar lambda*v/k on mean-zero point potentials. This gives x_i=(k-1)/(lambda*v), x_j=-1/(lambda*v) on S minus i, and zero elsewhere; each block potential is its average x minus 1/k on S alone. Thus the block S contributes 1, since lambda*v>k. On every other block T through i only the edge from i is positive, with absolute block sum 2[(k-1)^2+b_T]/(k*lambda*v); on a block missing i the negative and positive parts are separated by membership in S, giving 2b_T(k-b_T)/(k*lambda*v), including the zero cases. Here b_T=|T intersect (S minus i)|. The sums of b_T on the first class and b_T(k-b_T) on the second are (k-1)(lambda-1) and (k-1)(v-k)(lambda-tau) respectively. The latter count excludes exactly tau blocks through i for each cross pair. Substitution of (k-1)r=lambda(v-1) gives the claimed Q formula for every column. Q_ee=1/k+(k-1)/(lambda*v) is strictly between 0 and 1, so replacing Q by I-Q adds 1-2Q_ee to each absolute column sum. Symmetry gives the same infinity norms. The inverse-incidence and Steiner quadruple simplifications agree (e.g. Q=11/4 and P=3 at v=8,k=4,tau=1); no transitivity is used.

## originality

PASS

The exact norms for general strength-three incidence graphs, determined by third-order overlap rather than a symmetry hypothesis, pass the scoped comparison. Electrical-current representations, weaker universal bounds, and exact norms for other graph families or design regimes are prior work, not contributions of this record.

## value

PASS

Exact endpoint norms are natural measures of worst-case absolute electrical transfer and of the canonical cycle projection. A formula for every edge across a family defined by incidence balance rather than group symmetry is informative beyond general bounds. In particular designs with the same (v,k) can have different constants, quantified by the inverse pair-incidence dependence; the strength-three calculation explains the difference and provides exact benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
