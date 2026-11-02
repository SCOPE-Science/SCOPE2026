---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the explicit convention c(a)=#{b:b◃a=b}, r(a)=#{b:a◃b=a}, qp_record(s,t)=sum s^{c(a)}t^{r(a)}, the action-quandle relations give c(x,g)=|C_G(g)| o_g by Burnside, and r(x,g)=|X||C_G(g)∩G_x|. For g of cycle type lambda in S_n, centralizer order z_lambda, orbits indexed by distinct cycle sizes with cardinality d m_d, so the displayed partition polynomial follows. Summing fixed-pair counts gives n*n!*sum_{j=0}^{n-1}p(j), with the partition asymptotic yielding the stated limit. The s^n t^n coefficient n! for n>=3 follows since c>=n, with equality only when the centralizer acts freely and transitively on n points, i.e. an n-cycle for n>=3. Independent complete quandle-operation enumeration checked n=1,...,5. IMPORTANT CONVENTION: Nelson originally defines the standard polynomial using s^{r(a)} t^{c(a)}, the variable reverse of this record; the formula here is correct for its self-contained declared definition but qp_Nelson(s,t)=qp_record(t,s), so references to the ordinary convention without this caveat are imprecise.

## originality

PASS

Best-of-knowledge originality of the precisely delimited final claim after comparing exact object/parameter theorem implications; known tools and antecedents are credited. Primary full-text coverage where available and access exceptions are disclosed. Kai component-classification theorem does not by itself imply the fixed pair density or s/t exponents, and Nelson invariant is a generic definition rather than a computed Q_n instance.

## value

PASS

For the natural universal embedding object Q_n, the exact full bivariate first-iterate fixed-point profile, distinguished-cycle statistics, and asymptotic fixed-pair probability are useful algebraic invariants. A general Burnside lemma alone does not tabulate the partition cycle-type distribution and its asymptotic. Not a claim about higher-iterate polynomials or link-coloring improvements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
