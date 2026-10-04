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
# Verification

The proof was checked in three layers.

1. **Parametric algebraic certificate.** `verify_one_mixed.py` builds the cleared numerator of \(E_1^*E_2^*-E_2^*-2E_1^*\) using a small integer multivariate-polynomial implementation. With \(A=u+2\), \(d=v+1\), and \(b=v+w+1\), the whole domain is split into the exhaustive cases \(u\ge v\) and \(v\ge u\). The substitutions \(u=v+z\) and \(v=u+z\) respectively produce 143 and 148 monomials, all with strictly positive integer coefficients. This verifies the inequality for infinitely many integer parameters by symbolic coefficient positivity; it is not a bounded enumeration.

2. **Exact-rational multiplicity checks.** The script evaluates the closed formulas for many patterns \((a,c;x_1,\ldots,x_r)\), confirms \(E_i\ge E_i^*\), and checks \(1/E_1+2/E_2\le1\) with `Fraction` arithmetic.

3. **Independent sampled-span Markov chains.** For five representative systematic one-mixed-column codes over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), the script computes the stopping expectations directly from the finite subspace Markov chain. Each exactly equals the derived closed formula.

Running `python3 verify_one_mixed.py` returns `VERIFY_OK`, with certificate term counts 143 and 148 and minimum coefficient 1 in both cases.

The computational checks do not certify literature originality and do not replace the analytic derivation of the stopping-time formulas or superadditivity. No independent external audit has been performed.
