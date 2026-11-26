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

For an incoming carry C_i the next conditional mean is (b_i+C_i)/2. The output-bit identity Y_i-X_i=b_i+C_i-2C_{i+1} sums to k minus the number of carries. Above the top input position a surviving carry has a geometric tail. Finite-bit cylinder frequencies agree in the limit with independent fair bits; for arbitrary prefix endpoints, an additional run of h carries above the top bit requires h specified consecutive bits all equal to one, and in the prefix starting at zero their frequency is at most 2^(-h) (the all-one block occurs at the end of each controlling binary period). This justifies passage of the quadratic moment. Conditional propagation gives Cov(C_i,C_j)=2^(-(j-i))q_i(1-q_i) and summing gives 3 times the sum of q_i(1-q_i). Each one-bit adds 1 to sum q_i; diagonal terms in sum q_i^2 add 1/3 per one-bit, and each unordered distinct pair adds (2/3)2^(-distance). The energy strictly decreases in every positive integer gap. An outside pattern compresses strictly to a single gap of length 2 unless already in that form. At cut i a gap of length 2 loses exactly (1-2^(-i))(1-2^(-(k-i))) of energy, uniquely minimized at the two edge cuts by strict convexity of 2^(-i)+2^(-(k-i)); they coincide when k=2. This proves both levels, exactly the stated equality shifts and their gap. Sparse supports approach 2k, strictly below it for finite positions when k>=2; k=1 is constant. The supplied finite checker was inspected, not run or substituted for the infinite proof.

## originality

PASS

Credit is limited chiefly to the unrestricted fixed-Hamming-weight second level, gap and rigidity. The pair formula evaluates an already published exact recurrence, and Tarłowski already yields the first minimum. His bounds also resolve some low-weight subcases and constrain the possible word-block patterns, but do not give the all-weight fixed-Hamming-weight comparison or its rigidity by substitution. The inspected bias results govern a different statistic.

## value

PASS

The variance is the natural fluctuation scale for digit-sum correlations. Knowing its first and distinct next value under a fixed Hamming-weight constraint gives a uniform rigidity margin with equality classifications independent of ambient bit length. The gap approaches 1 as the weight grows; the result is not an empirical shift table, a new sign-bias estimate, or merely an alternative computation of one already-known variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
