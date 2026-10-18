---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The optimal K-g-frame lower bound is A=sup{lambda: lambda KK*<=S}, so the Douglas least domination factor is inf{mu:KK*<=mu S}=1/A. Any K-dual factorization K=T_Lambda*T_Gamma^* forces KK*<=||T_Gamma||^2 S; the reduced solution attains 1/A. In dimension one Lambda=2I,K=I gives A=4 and unique dual squared norm 1/4, refuting the printed inequality. A separate exact frame (e1,e1,2e2) has A=2 and dual family (e1/2+t e2,e1/2-t e2,e2/2); its synthesis frame operator is diag(1/2,1/4+2t^2), so all |t|<=1/(2sqrt2) attain norm^2=1/2. Direct symbolic multiplication independently verified both identities. The unique reduced solution has an additional range normalization and is not the unique norm minimizer.

## originality

PASS

PASS, best-of-knowledge for exact source-specific correction. The 2018 Li–Leng–Huang full institutional primary pages 4–7 explicitly equate the maximal lower bound A to the minimum Douglas domination coefficient, and assert uniqueness among all duals attaining squared norm A; both assertions are false as exact operators. Labrigui–Touri–Kabbaj arXiv:1901.03703v1 Theorem 3.2 repeats the same incorrect equation, not its correction. Douglas unique reduced factor and general nonuniqueness of other frame-dual objectives are established antecedents; the contribution is pinpointing this cited theorem and proving both counterexamples and the precise correct claim. Unindexed errata remain risk.

## value

PASS

PASS. The published theorem uses the sharp dual synthesis norm to define its canonical dual. Its incorrect bound differs by an arbitrarily large factor under frame rescaling, and a whole interval of exact nonunique minimizers invalidates the claimed characterization. Distinguishing reduced-factor uniqueness from mere operator-norm minimization changes a foundational canonical construction, not merely a harmless notational typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
