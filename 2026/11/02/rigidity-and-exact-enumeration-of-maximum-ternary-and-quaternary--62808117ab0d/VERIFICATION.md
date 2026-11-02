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

# Reproducibility and evidence limits

The theorem's infinite-range statement rests on a mathematical implication from the explicit structural bounds in Lin–Djaljapayan–Yu, arXiv:2610.30615v1, Theorem 7.1 and Lemma 6.1. The no-weight-four branch uses their Eq. (5) plus one-coordinate synchronization. Its published cardinality theorem supplies the matching optimal upper bound.

Run `python3 check_bound_gaps.py` to reproduce the six exact gap calculations at \(n=17\), plus finite arithmetic spot checks. The elementary expression \(g(n+1)-g(n)=n-b\), where each excluded upper bound is \(bn+a\) with \(b\le7\), proves positivity for every subsequent length without computational extrapolation; the program is a diagnostic only.

Run `python3 check_extremizers.py` to check that all parameter choices produce different labeled valid shell codes in the four reported small regimes, verify the unique center in each example, and test specific constructions at lengths 17 and 24. Read `bound_gaps_output.txt` and `verification_output.txt` for the exact outputs obtained when these checks were run. These scripts do not search over all admissible codebooks at large lengths, and do not independently certify the published structural lemmas; the mathematical proof provides the all-length classification.

Boundary: nothing here establishes uniqueness for \(n\le16\), codes over alphabets larger than four, or other prescribed distance sets. Mathematical independent audit has not been performed.
