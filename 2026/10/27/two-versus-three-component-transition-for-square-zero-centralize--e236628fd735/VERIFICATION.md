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

Multiplication of the four k[t]-module blocks gives a²+t^(n−2)bc=0 in R_n, b(a+d)=c(a+d)=0 in R_2, and d²=0 in R_2 because n≥4. In particular d_0=0; the lowest nonzero coefficient of a² cannot be cancelled below t^(n−2), even in characteristic two. For n=2h this leaves the equations x²+BC=2xy+BV+CU=δB=δC=0 and h−1 free coefficients, with δ=d_1+x when n=4 and δ=d_1 otherwise. The component B=C=x=0 is affine; the branch δ=0 is a dimension-four complete intersection whose B≠0 open is irreducible (solve for C,V) and whose B=0 complement has dimension at most three (x=0, CU=0). For n=2h+1 one has BC=0, x²+BV+CU=0 and δB=δC=0, with h free coefficients; the three branches are the affine B=C=x=0 branch and the two geometrically irreducible quadratic cones with a free coordinate. The quadratic cone equations are primitive linear polynomials in one of B,C,U,V over the polynomial ring in the remaining variables, so this holds in characteristic two. The stated intersections follow as reduced varieties; this makes no scheme-theoretic assertion about the sum of the odd cone ideals. Partitioning field points by B=C=0 versus its complement gives q^(h−1)[q^4+(q²−1)q²] or q^h[q³+2(q−1)q²] as stated. A separate binary commutator-kernel calculation (python3 /workspace/branches/independent_checks.py) gave 56,64,112,128 for n=4,5,6,7, respectively. The proof, not that finite check or the reported original runs, supplies every-field and every-q validity.

## originality

PASS

The strongest inspected related results give Jordan-type existence, simultaneous normal forms, adjacent square-zero rank strata, or other fixed centralizer counts. None settles the reduced components and the unrestricted labeled point count for this fixed block pair. The assessment is bounded, not a publication-priority guarantee.

## value

PASS

For the first short block beyond the hook, the square-zero constraint results in a parity change in the number of components, not merely their coordinates. The common intersection and uniform dimensions and labeled point counts are natural exact invariants of this fixed-centralizer fiber, including in characteristic two. They answer different questions from knowing which similarity types occur.

The dated certificate retains the supplied scientific assessment, sources and limitations.
