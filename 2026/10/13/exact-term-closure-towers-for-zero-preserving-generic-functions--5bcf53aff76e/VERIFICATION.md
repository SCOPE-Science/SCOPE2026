---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: In the equational class of F_q-vector spaces with finitely many zero-preserving operations, the free algebra adjoins a fresh independent vector e_{j,v} for every previously unseen nonzero operation input tuple v∈V_n^{r_j}∖V_{n−1}^{r_j}. The recursive universal property proves these are exactly all newly created basis directions. Thus d_{n+1}−d_n=Σ_j(q^{r_jd_n}−q^{r_jd_{n−1}}) with d_{−1}=0. Telescoping gives d_{n+1}=m−s+Σ_j q^{r_jd_n}. The F2 unary m=1 tower 1,2,4,16,65536 follows. Checks at several small parameters match direct increments; neither this finite test nor the original verification log is treated as a proof.

## originality

PASS

PASS with substantial elementary-normal-form/folklore risk: Bossut gives general free-amalgam treatment for generic functions and zero-preserving unary F2 vector space motivation, but its inspected Section 5.2 does not state the all-arity generated-hull dimension recurrence. The final quantitative invariant requires an explicit stage-by-stage independent-value census. It is not asserted to be a new Fraïssé amalgamation theorem or a statement about every generated substructure of a model companion.

## value

PASS

PASS: Finite function-depth hull dimension is a natural and technically relevant invariant in generic-function Fraïssé constructions. The all-arity exact recurrence shows the transition from linear closure to a true exponent tower already for one unary zero-preserving function and can bound finite-stage generated pieces. It is simple universal-algebra counting, but the exact invariant is motivated and not identified as tabulated prior data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
