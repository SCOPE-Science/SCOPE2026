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

For sorted absolute magnitudes a_k, the signed top-k indicators give x=sum_k (a_k−a_{k+1})s_k, with the same nonnegative coefficients giving the norm as sum_k (a_k−a_{k+1})W_k. Triangle inequality reduces the supremum exactly to these indicators (ties and zero coefficients are harmless). On a proper support of k coordinates with q runs, b internal sign changes give b twos and 2q ones, so the numerator is W_b+W_{b+2q}; b<=k−q and k+q<=n. Increasing q in W_{k−q}+W_{k+q} changes it by w_{k+q+1}−w_{k−q}<=0 wherever both spreads are feasible. A single alternating run attains the q=1 value. Full supports have even sign-flip count and attain n for even n or n−1 for odd n. This covers n=2, where the two directed differences count the same pair in opposite directions. In odd dimensions each proper-support gap from 2 is (w_k−w_{k+1})/W_k and the full-support gap is 2w_n/W_n. For alpha=1/p, derivative of (1−t)^alpha+(1+t)^alpha is negative on (0,1); k=n−1 therefore maximizes the proper branch. AM–GM beats the full branch since the difference 1−1/(n−1)^2−((n−1)/n)^2 has numerator 2n²(n−3)+4n−1 over n²(n−1)^2, positive for n>=3. Its even Taylor expansion gives defect alpha(1−alpha)/(n−1)^2 plus order (n−1)^−4. Inspected checker.py and its recorded stdout (check_output.txt line 40); the 39 finite cases are not a proof, and the submitted script was not executed.

## originality

PASS

The exact finite real cyclic norm and strictness law for arbitrary decreasing positive Lorentz weights, and the resulting closed power-weight specialization, are distinct from the retrieved exact neighboring claims. Standard rearrangement and signed-layer methods are not new contributions. This is a bounded assessment, not a priority certification.

## value

PASS

This computes a natural discrete differentiation norm for a whole class of symmetric norms, identifying precisely when parity produces a strict gain over the triangle bound and giving a sharp asymptotic in a standard power family. The reduction to a single active run or a near-alternating odd cycle is structural, not a numeric coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
