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

For rank-one idempotent E=uv^T with v^Tu=1, quotient by scalar rescaling gives projective lines [u]. Rank-one determinant lemma and adj(XI−C_f)=X²I+X(C_f−I)+(C_f²−C_f+c1I) force v^Tu=1, v^TC_fu=1−c1, v^TC_f²u=1−2c1−c0. For a vector with minimal annihilator h|f of degree d, these equations have q^(3−d) solutions iff moments obey the h-recurrence. Companion module F_q[X]/(f) gives Φ_q(h)/(q−1) projective lines per h. d=3 contributes Φ_q(f)/(q−1); d=2 writing f=h(X)(X−s) leaves consistency s³=0, hence c0=0 and h=f/X with q solutions per line; d=1 imposes λ=1−c1, c0=−c1² and f(λ)=−c1³=0, forcing c1=c0=0, λ=1 and q² choices. Independent exhaustive rank-one idempotent/matrix-cube enumeration over F_2,F_3,F_5 for every c0,c1 matched the formula (R5_NILCLEAN_CUBIC_ALL_COEFFS_OK). Polynomial totients computed by direct gcd; uniform extension-field result rests on module proof.

## originality

PASS

Breaz–Modoi establish qualitative nil-clean existence and construction of companion-matrix decompositions, and their Remark 6 expressly notes nonuniqueness. The exact Φ_q(f) + correction term fiber count is not in the materially read paper. Nil-clean index papers study ring/global extremal fiber sizes, not the trace-one cubic per-polynomial rank-one fiber. Searches of Resultary nearest finite-matrix factorization results give distinct products/decompositions. A similarly phrased future general polynomial fiber theorem remains possible.

## value

PASS

Rank-one nil-clean decomposition multiplicity refines the basic existence/nonuniqueness theorem in the smallest nontrivial companion dimension. The answer varies with irreducible factorization and singular constant-term strata and gives a universal finite-field formula. That is a motivated, potentially reusable exact invariant for cyclic matrix modules, not a routine relabeling or one-number table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
