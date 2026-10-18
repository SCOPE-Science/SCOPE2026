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

# Reproducibility

Run `python3 verify.py` using Python 3 and its standard library. It exhaustively processes all subsets of distinct primes through the exact-sum dynamic-programming recurrence for sums at most 2000 and checks the first finite length-versus-product discrepancy and primorial envelopes. Expected output: `VERIFY_OK finite_exact_sums=1997 first_L_minus_K=319 max_n=2000`.

The infinite result is not certified by this program. Its nonstandard mathematical input is the fully sourced uniform-residue-class construction in the proof of Matomäki–Maynard–Shao (arXiv:1610.02017, §§2–3); imposing distinctness via seven reduced residues is worked out explicitly in RESULT.md. The prime number theorem and the Deléglise–Nicolas envelope are separately used. The necessary large-integer threshold is not numerical.
