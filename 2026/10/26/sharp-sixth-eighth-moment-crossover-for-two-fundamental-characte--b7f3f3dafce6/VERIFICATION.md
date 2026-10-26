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

# Verification instructions and limits

Run \(\texttt{python3 check.py}\) using the Python standard library. The checker:

1. Builds the \(C_2\) Weyl kernel as an explicit two-dimensional Laurent-polynomial dictionary, confirms constant term \(8\), and evaluates every mixed coefficient at total degrees \(0,2,4,6,8\) with exact integers.
2. Reconstructs the two sharp scalar norm polynomials at 1001 test parameters and checks the unique critical-point signs, algebraic sixth-root expression, and eighth-root bisection value.
3. Separately integrates eight complex-coefficient examples using a \(64\times64\) Weyl-weighted torus grid and compares them to the exact symbolic moment expansions. The integration comparison is a numerical cross-check, not the proof of sharpness.

The continuum inequalities and all-extremizer classification are proved analytically in RESULT.md by positivity of the full mixed-moment expansion and exact monotonicity of derivatives on \([0,1]\). The test output recorded in \(\texttt{check_output.txt}\) is an execution record, not independent validation. No external certification or independent audit has been performed. Priority assessment remains provisional because searching cannot establish the absence of unindexed equivalent proofs.
