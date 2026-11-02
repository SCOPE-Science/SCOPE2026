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

The included `verify.py` independently enumerates all distinct deck arrangements, computes actual removal counts for every arrangement, and separately constructs the coefficient polynomial via bounded subset selection with binomial multiplicities. For 16 small parameter pairs (multiplicity up to three and up to seven labels), 493231 distinct arrangements are checked; all empirical tail frequencies equal the exact count ratios. It also confirms monotonicity and boundary conditions and compares finite-n expectations with the analytical correction for 40, 80 and 160 labels.

Execution from the standalone package returned:

`VERIFY_OK multiset_parameter_cases=16 direct_decks=493231 finite_n_bias_checked=40,80,160`

Computational enumeration cannot certify all possible multiplicities, infinitely many label counts, the asymptotic coefficient, originality, or historical priority. The proof is supplied in `RESULT.md`; independent mathematical audit was not performed.
