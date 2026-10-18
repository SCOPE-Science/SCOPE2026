---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For idempotent e,f in T_n, B=e(X), A=f(X) have sizes r,s, intersection t; restrictions alpha=f|B, beta=e|A fix intersection C and free values outside A union B contribute (rs)^{n-r-s+t}. The full products are idempotent precisely when alpha beta alpha=alpha (for fe) and beta alpha beta=beta (for ef). For Y=alpha(B) size k containing C, select its k−t extra points from A\C, choose distinct representatives beta(Y) in B\C in (r−t)!/(r−k)! ways, assign remaining B\C elements to k image points in k^{r−k} ways. The remaining s−k beta inputs take any r values, except choices wholly in the k selected representatives which would also make ef idempotent, giving r^{s−k}−k^{s−k}. Multiply by choices of A,B and sum exact nonnegative t,k ranges. Every restriction/extension is uniquely counted, establishing all-n rank-refined formula. Independent full compositions for all idempotent pairs on n<=5 reproduced every coefficient and totals 0,0,6,204,5900, plus the symbolic formula gives n=6 total 190410; analytic bijection, not finite data, proves all n.

## originality

PASS

The closest Blyth–Almeida Santos 2006 full-transformation article studies existence of four skew-pair types; public preprint abstract discusses ubiquity, and complete content was not obtainable, leaving explicit risk. Luangchaisri–Changphas 2022 examines partial transformation monoids and subtype existence; the inspected abstract does not give a full-T_n bivariate rank census. The submitted closed joint-rank enumerator for all n is stronger than mere existence and is not implied by a subtype list or thresholds. Accepted as best-of-knowledge with prominent inaccessible-prior caveat.

## value

PASS

Skew idempotent multiplication is structurally natural in finite transformation semigroups. The first exact all-n joint-image-rank enumeration and concise rank-(2,2) formula refine mere existence/type theory, with a genuine combinatorial fiber-bijection rather than an arbitrary small-n table. The count is potentially reusable for random transformation semigroups and orbit statistics without requiring a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
