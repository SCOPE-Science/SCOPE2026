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
# Verification and limitations

The mathematical proof in `RESULT.md` is an all-integer matching/inclusion-exclusion argument. The standalone script `verify_oi2rd_triangular.py` checks its fixed-domain instances using the original neighborhood definition, not just the transformed matching criterion. Run with `python verify_oi2rd_triangular.py` using a standard Python 3 installation; no third-party modules or network access are needed.

In detail, the script checks all \(4^{\binom n2}\) assignments for \(n=3,4,5\), compares the entire resulting weight profiles with the symbolic coefficient formula, and independently counts the two-singleton-color assignments for every maximum matching at \(n=3,4,5,6\). Its deterministic observed output is recorded in `verification_output.txt`. This is exhaustive only for these finite orders. It is not a proof that the formulas hold at all larger orders, and it is not independent mathematical validation.

The result's exact scope is ordinary outer-independent two-rainbow domination with named colors on \(T_n=L(K_n)\) for \(n\ge5\). The \(n=3,4\) checks are boundary tests. General literature precedence remains subject to additional human verification. No external audit has been performed.
