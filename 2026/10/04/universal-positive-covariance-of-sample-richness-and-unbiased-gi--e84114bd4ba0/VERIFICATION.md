---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Exchangeability reduces covariance with the pair-collision U-statistic to covariance with one selected collision indicator. Conditioning on the collision category gives the stated exact formula \(2s_2A_n-(1+s_2)B_n\). Under the size-biased category variable \(P\), \(A_n=E f(P)\) and \(B_n=E[P f(P)]\) with \(f(x)=(1-x)^{n-2}\) antitone. The two-copy covariance identity therefore gives \(B_n\le s_2A_n\), yielding the positive lower bound. For \(n>2\), strict monotonicity of \(f\) gives equality exactly for a constant size-biased mass, hence a uniform parent law; for \(n=2\), equality is automatic. The exact-rational verifier exhausts several complete sample spaces and independently matches the formula.

## originality

PASS

The closest occupancy source studies the number of occupied boxes and frequency counts under arbitrary box probabilities, while the closest coincidence-statistic source treats pair coincidences as U-statistics for Rényi functionals. Neither inspected source states their exact finite-sample covariance, its universal sign, or the equality classification. Fresh Resultary search also surfaced related species-discovery and occupancy covariance findings but no implication-equivalent richness versus Gini--Simpson theorem. Best-of-knowledge originality remains exposed to older ecological/occupancy literature using different notation.

## value

PASS

Observed richness and Gini--Simpson diversity are two foundational finite-sample diversity summaries. A universal exact sign, quantitative lower bound and complete equality classification for arbitrary category weights give a natural robustness relation between them, beyond a textbook expectation calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
