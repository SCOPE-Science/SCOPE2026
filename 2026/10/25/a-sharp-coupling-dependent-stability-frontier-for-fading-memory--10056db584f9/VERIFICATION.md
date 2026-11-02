---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Two full-buffer coordinate refresh/update steps directly yield the reported 3x3 monodromy T on (x,y,stored second gradient). Its exact cubic coefficients satisfy all four strict Schur–Jury inequalities iff 0<t<tau*. The key final Schur factor t(1+gamma)(1+c²gamma t)F(t) with F=2-(1+gamma)t+c²gamma(1-gamma)t² has a smaller positive root tau* preceding |c|gamma t=1 for 0<|c|,gamma<1; endpoints c=0,gamma=0,1 are direct substitutions. The zero-buffer plane E together with T E spans R³, so a non-Schur eigenmode cannot be hidden by buffer initialization. Algebraic comparison of tau* with 2 yields gamma<1/2 and c²>1/[2(1-gamma)], and strict sqrt discriminant bound gives unattained supremum 3. Independently recreated symbolic monodromy/cubic/Jury factorization and 96 spectral classification examples. No implication beyond the stated quadratic family.

## originality

PASS

Best-of-knowledge originality: On two-coordinate equal-curvature coupled quadratic, full-buffer fading-memory cyclic CoCD is globally stable exactly when 0<alpha lambda<4/[1+gamma+sqrt((1+gamma)^2-8c² gamma(1-gamma))], with coupling-induced t>2 window and sharp unattained supremum 3. The materially compared earlier results cover only credited subclaims or different mathematical objects; no decisive prior implication was found. Priority is not exhaustively certified. Full 2026 CoCD original paper and its appendices were inaccessible (Oxford download capacity issue); it may contain specialized exact quadratic calculations not visible in the primary abstract.

## value

PASS

The source algorithm has general conservative sufficient bounds; identifying its exact necessary/sufficient stability region for the first coupled quadratic case is a natural sharp stability problem. Counterintuitive increase past ordinary no-memory step 2 and the unattained bound 3 are meaningful structural parameter effects, not merely an arbitrary substitution. Small dimensional specialization remains valuable for algorithm design and counterexamples to overly broad memory intuition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
