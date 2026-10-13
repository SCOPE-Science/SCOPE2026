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

The universal congruence is proved symbolically in `RESULT.md`; enumeration is not used to infer the infinite statement.

`verify.py` performs exact integer checks. It compares Campbell’s double-binomial formula to the published recurrence through \(n=40\), checks the residue classification through \(n=500\), checks \(13{,}880\) instances of the exact summand involution, checks \(28{,}431\) positive-\(a\) summands through \(n=80\), and checks \(12{,}285\) bounded instances of the two-carry lemma.

Observed command:

`python3 verify.py`

Observed output:

`VERIFY_OK formula_recurrence=0..40 residue_pattern=1..500 symmetry_cases=13880 a_positive_terms=28431 carry_lemma_cases=12285 fixed_exceptions=5`

The checks use only Python’s exact integers and `math.comb`. Their finite ranges are corroborative. The proof’s unbounded steps are Lucas’ theorem, Kummer’s theorem, the explicit valuation identity for the \(a=0\) slice, and the exact involution on the summation region.
