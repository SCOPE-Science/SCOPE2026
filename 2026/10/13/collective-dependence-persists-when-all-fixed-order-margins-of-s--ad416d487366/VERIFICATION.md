---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Power coordinates y_i=x_i^p and slack w=1−Σy_i turn the published density into Dirichlet(α,…,α,β): the Jacobian is α^d Πy_i^(α−1), and Γ(1+α)=αΓ(α) gives the normalization because dα+β=1+α. Relative to Q_d, the log likelihood on support is −logΓ(β)−(d−1)logΓ(1+α)−t log w. The beta log moment, finite since β>0, yields the exact KL formula. Aggregation into the slack leaves β+(d−k)α=1−(k−1)α, so the marginal has the same family and exponent at dimension k. Setting m=k−1, the quadratic terms combine to ζ(2)[m(m+1)−(m²+m)/2]α², proving the stated coefficient and the O_k(α³) remainder; Pinsker gives TV convergence. At t=1/c the order-one Euler terms cancel. As a function of t the limiting KL has derivative tψ'(1−t)>0 and value zero at zero; the digamma pole dominates the log-gamma term as t tends to 1. Under Q_d the number of coordinates with x_i^p>1/2 is Binomial(d,1−2^(−1/p)), with limiting mean log(2)/c; under P at most one can occur. The zero-versus-positive probability of at least two proves a liminf lower bound, not convergence or sharpness of the full TV. Own replay: python3 /workspace/review_replay.py 5; Q_d simplex radial integration in logistic coordinates checked normalization and KL at (d,p)=(2,3),(3,7),(5,9) to 42 digits and gave 0.40939007008601165 and 0.04782868294631568 for the two c=2 quantities. The submitted diagnostics were inspected, not executed; finite quadrature does not prove the limit.

## originality

PASS

The family, density, and distributional/entropy tools are prior. The distinct finding is the quantitative comparison in the admissible dimension-growing regime p=c(d−1): a nonzero full KL profile with a separate full TV obstruction, even though every fixed-order marginal tends to the product law with the given KL asymptotic. A known finite-dimensional spherical density or a general identity for copula entropy is not, by itself, this comparison.

## value

PASS

The spherical model has a natural dimension-dependent admissibility threshold. Holding p/(d−1) fixed shows quantitatively that weak information in each bounded subset of coordinates need not make the full law approximately independent, even in TV. A finite KL profile, fixed-order decay coefficient and a concrete distinguishing event give independently usable comparisons; no claim of sharp full TV is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
