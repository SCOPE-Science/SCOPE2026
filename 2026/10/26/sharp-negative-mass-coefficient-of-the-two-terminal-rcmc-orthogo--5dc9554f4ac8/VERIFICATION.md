---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The proof uses: (1) positive-definite Dirichlet extension and reversible harmonic measure; (2) exact two-by-two inverse identity; (3) weighted Cauchy–Schwarz with its equality case; (4) the unique positive stationary point of a rational one-variable quotient; (5) explicit bipartite conductance graphs attaining equality; and (6) the strong graph maximum principle for the support criterion. All quantifiers and endpoint conditions are specified in RESULT.md.

The included \(\texttt{verify.py}\) is standalone Python 3 code with no third-party packages. Run \(\texttt{python3 verify.py}\) after extracting all embedded files. It performs exact \(\texttt{fractions.Fraction}\) checks of Type A and B matrices, reversibility-aware harmonic moments, projector conservation/idempotence, sign criteria, and the proposed bound on a deterministic suite of small connected weighted graphs; it also checks exact extremizing uniform-star networks. These finite tests do not prove the theorem's universal cases, establish coverage of all papers, or constitute an independent audit.

The source paper arXiv:2312.05470v1 (first public 2023-12-09) provides the existing algorithm's definitions and qualitative positivity limitation. The theorem's quantitative maximum and asymptotic have been derived directly and are confined to the raw two-terminal Type B projection. Independent audit status remains unperformed.
