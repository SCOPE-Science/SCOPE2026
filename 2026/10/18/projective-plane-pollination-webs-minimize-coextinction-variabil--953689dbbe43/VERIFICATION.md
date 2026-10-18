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

# Verification and reproducibility

Run `python3 VERIFY.py` with Python 3.8 or later; no third-party packages or network access are required. The verification constructs point-line incidence matrices of finite projective planes over the prime fields of orders \(2,3,5,7\), checks their regular degrees and exact pair intersections, and produces degree-preserving two-edge switches as non-optimal comparators. It computes the predicted covariance variance formula and the projective-plane lower bound for every possible deletion count, and verifies all strict comparisons in the theorem's specified stage interval.

For prime orders \(2\) and \(3\), an **independent probability-space enumeration** visits every subset of pollinators at each deletion count, counts the plant extinctions for each subset, and checks the exact rational second moment against the covariance calculation. The script also verifies the discrete second-difference identity using exact binomial arithmetic for all tested cases.

For \(q=2\), after four pollinators are removed, the projective-plane web yields 7 deletion subsets causing zero plant extinctions and 28 causing one (of 35 equally likely choices), giving variance \(4/25\). A switched network yields 9, 24, and 2 subsets causing zero, one, and two extinctions respectively, giving variance \(48/175\); both have mean \(4/5\). The script verifies analogous complete distributions for \(q=3\) and checks projective-plane incidence structures at \(q=5,7\).

The computational checks are finite and do not prove the theorem for all prime powers. The general result is established analytically by the event formula, double-counting of pair intersections, Pascal convexity, and finite-field projective-plane construction in RESULT.md. The verification does not address empirical ecological data, temporal dependence, or independent scientific validation.
