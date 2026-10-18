---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Conditional on a uniformly chosen leaf at depth d and cherry-membership J, S_next=S+d+2 and C_next=C+1-J. Introducing Q as total depths of cherry-member leaves gives E[Q_next|T]=(1-2/n)Q+2S/n+2. Multiplication before conditioning produces mixed E[S_next C_next|T]=(1-1/n)SC+(1+1/n)S+(2-4/n)C-Q/n+2. The solved marginal recurrences n>=3 imply the covariance recurrence g_(n+1)=(1-1/n)g_n-2/9 with g3=0 and the displayed exact expression; the n=2 initial exception and n=3 zero are handled. Independently implemented rational tip-splitting enumeration over the full ordered tree distribution through n=7 and checked every covariance, supplementing rather than replacing the all-n recurrence.

## originality

PASS

Cardona et al study Sackin variance and its covariance with the total cophenetic index; the C used for Colless there is not cherry count. Wu--Choi derive cherries paired with pitchfork counts rather than global depth sum. Dearlove--Frost explicitly analyze Sackin and cherries as two shape summaries and report weak correlation qualitatively; inspected Methods/Results do not state this exact negative rational covariance. No Resultary matching all-n Sackin/cherry covariance appeared, though a more general historical mixed-moment theorem might imply it.

## value

PASS

Sackin depth and cherries are standard complementary phylogenetic balance indices. Their exact all-n negative covariance and sharp sign transition calibrate joint behavior, improve on descriptive qualitative dependence, and are naturally relevant when both features are used to assess Yule-model tree balance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
