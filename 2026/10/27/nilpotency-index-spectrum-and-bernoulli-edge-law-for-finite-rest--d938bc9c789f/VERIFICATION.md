---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frozen enumerator and limits are mathematically correct. In block coordinates X=(A B;0 0), X^j has upper blocks A^j and A^(j−1)B. Uniform nilpotent X gives independent uniform B and uniform nilpotent A. At maximal block size d with multiplicity r, rank(A^(d−1))=r, including zero A, and index d occurs in q^((k−r)c) fibres, with remaining fibres at d+1. Centralizer counts then give the enumerator; a single k-block gives the maximal-index event. For regularity, X=XYX with im(Y)⊆W requires im(X)⊆X(W), and conversely a right inverse to X|_W on im(X) extends to a suitable Y. Thus the frozen regular proportion bound q^(−c) is valid. At 2s<k the partition with longest part k−s is (k−s,μ), μ⊢s, so the added column-square sum is k+s and the added multiplicity factor is 1−q^(−1). Summing residual weights gives K_(q,k) q^(−2s)/φ_s. The unique longest block then contributes the claimed Bernoulli nonextension. The repaired theorem uses the exact masses at s≤h=floor((k−1)/2): they are those of the target multiplied by K_(q,k)/K_q≥1. Therefore the overlap of distributions is at least the target mass on this prefix and total variation is at most its complementary tail. Since E_c≤1, the tail is bounded by P(S_q≥h)≤q^(−2h)/[(1−q^(−1))(1−q^(−2))], which is at most the stated upper bound because 2h≥k−2. The maximum-index atom gives the lower bound (K_(q,k)−K_q)(1−q^(−c))≥K_q q^(−k−1)(1−q^(−1)), uniform for c≥1. The power series recurrence (1−z)G(z)=G(z/q) normalizes S_q and coupling the two target laws gives the growing-c bound. This verifies both inequalities for all k≥1, including the empty product case.

## originality

PASS

The frozen full finite index enumerator does not pass originality as a principal contribution: verified Hall-polynomial results give the joint count by restriction and ambient type for every codimension; projecting to the largest ambient part gives the same invariant. The affine precedent is an exact additional specialization at c=1, not the limit of known finite coverage. The replacement credits these counts and uses them only as input. Its principal finding is a Bernoulli-shifted law with upper and lower errors of order q^(−k) in total variation, uniformly over all c≥1. The bounded searches and inspected stronger finite results do not supply this sharp uniform stochastic estimate; it requires identifying the unique-block mass range, the common prefix mass ratio and an atom giving a matching lower order.

## value

PASS

The exact finite formulas are useful proof inputs but no longer offered as an independent contribution. The repaired claim quantifies the distribution of the deficit from the largest possible index in a natural restricted-range sample. Uniformity in c matters because the codimension can vary arbitrarily with k, not just be fixed or divergent in a separately analyzed limit. A quantitative approximation valid throughout this range and a matching positive lower bound tell a researcher both when the Bernoulli-convolution model is accurate and that its exponential accuracy cannot be improved in order at fixed q. The lower bound comes from the maximum-index statistic of the same ensemble, not from selecting an arbitrary test case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
