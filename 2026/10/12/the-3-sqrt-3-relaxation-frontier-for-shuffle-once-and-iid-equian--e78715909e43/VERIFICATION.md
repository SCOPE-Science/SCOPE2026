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
# Reproduction and scope

The analytic proof is in `RESULT.md`. With SymPy 1.14 or a compatible version installed, execute `python verify.py` from the directory containing this file. Its successful output is `VERIFY_OK exact polynomial, six-order invariance, and two-epoch witness`.

The script checks exact identities in the indeterminate \(\eta\), the two-variable quartic decomposition used in the positivity proof, six orderings at rational relaxation \(\eta=3/2\) for four finite epoch counts, and exact values \(S_2=586697/8388608\), \(I_2=15625/262144\). All checker operations use exact symbolic algebra, not floating-point tolerances. Symbolic arithmetic alone does not establish source novelty; the spectral-radius theorem and sign arguments require the human-readable proof. No external audit has been performed.
