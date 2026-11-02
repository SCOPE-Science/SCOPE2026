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

The proof reduces the original quadratic operator identity to a projective nondegenerate quadric equipped with rank-\((n-1)\) fibers. The additive-character formulas for the number of zeros and unit values of a nondegenerate quadratic form are standard, and supply the general infinite-family count independently of any finite computation.

Run `python3 check.py` with Python 3 and no external dependencies. The standalone checker computes spin-factor multiplication over prime fields and over the genuine quadratic extension \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). It evaluates the original weight-zero identity on every ordered pair of standard basis vectors, which is sufficient by bilinearity. For \(n=4,q=3\), it checks all \(29{,}282\) nonzero rank-one linear operators, finding exactly \(1{,}040\) solutions. It also performs two smaller exhaustive boundary tests at \(n=3,q=3\) (outside the claimed domain), and seven additional complete candidate-parameter enumerations with sampled direct identity checks. Both determinant types are tested where applicable. Exact output and marker appear in `check_output.txt`: `SPIN_FACTOR_RANK_ONE_RB_OK 10_CASES`.

The finite checks do not certify all field orders or dimensions. The geometry refers only to the reduced rank-one variety; the full equation scheme has not been examined for nilpotent structure. Independent mathematical review has not been performed.
