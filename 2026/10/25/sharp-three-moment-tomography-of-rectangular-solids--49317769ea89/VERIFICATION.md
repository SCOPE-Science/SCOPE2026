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

# Evidence and reproduction

Run `python3 verify.py` with Python 3 and its standard library; no additional files or network access are required. The checker independently evaluates raw moments by multinomial expansion and verifies 2,197 exact-rational triples of positive squared edge lengths. For each, it compares all elementary symmetric polynomial reconstructions, normalized second and third power sums, cubic discriminant, strict volume condition, and exact squared volume formula. It also verifies the unit-cube identity \((M_2,M_4,M_6)=(1/2,11/30,211/630)\) and four exact families with identical first two moments but different sixth moments.

The secondary simulation samples 260,000 independent uniform point pairs with an explicit pseudorandom seed and compares empirical and analytic moments; the recorded relative discrepancies were approximately \(0.000272, 0.000485, 0.001407\). Stochastic agreement is not a proof of the reconstruction theorem.

The all-box theorem rests instead on independent coordinate differences, exact cumulants, Newton's identities, positivity and discriminant analysis of a cubic, and Rouché root-count stability. These steps are recorded with quantifiers and endpoints in `RESULT.md`. No computational search, finite enumeration or numerical root test is used to establish universal uniqueness or the sharp stability exponent. The independent-audit channel has not been performed.
