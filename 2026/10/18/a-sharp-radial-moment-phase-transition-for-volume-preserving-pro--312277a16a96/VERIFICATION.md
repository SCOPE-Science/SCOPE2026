---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Rotational invariance gives S=||U_p||^2~Beta(p/2,q/2) and beta-prime Y=(1-S)/S. Splitting radial function min of two factor radii yields convergent I0,I1 and exact M_t(r)=r^{-qt/n}(I0+r^t I1)/B. Moving-boundary terms cancel on log-r differentiation, leaving sign pJ+-qJ-. The log derivative of J+/J- is -(n-t)/2 times the strictly positive difference of E[X/(1+r^2 X)] across separated x>1 and x<1 supports, hence strictly monotone sign(t-n). Verified endpoint ratios straddle q/p in opposite orientations for t<n and t>n, proving one global max/min respectively. At t=n volume makes M constant; symmetry p=q yields r*=1; t=n+2 uses inertia integral and gives r^2=(q+2)/(p+2).

## originality

PASS

Statement-and-implication comparisons including aliases/reductions, natural table searches and dominant theorem tests found no decisive prior coverage of the stated specific result; this is best-of-knowledge, with actual matching prior material credited and explicit residual risks.

## value

PASS

Natural volume-preserving aspect-ratio optimization of all radial/central-line-diameter moments on products of balls, with a dimension-critical reversal and explicit monotone integral optimizer, addressing a subcritical sufficiency problem not settled by general extremal-position existence results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
