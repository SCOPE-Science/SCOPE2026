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
# Finite exact verification

Run `python3 verify.py` from the extracted package. The checker uses the Python standard library alone and exhaustively evaluates every loopless directed graph with \(n=2,3,4\) vertices at probabilities \(p=1/3,1/2,2/3\). It calculates the full covariance of the \(n^2\) bidegree histogram cells from graph weights as `Fraction` objects and checks every entry against the rank-three correction formula. It also verifies all four eigenvector equations, binomial identities, and dimension counts, including the \(n=2\) eigenvalue coincidence.

These finite enumerations test exactly 12,492 graph/probability instances in nine cases. They do not verify the infinite parameter domain by exhaustion. The proof in `RESULT.md` supplies the all-parameter argument through conditional arc independence and a four-direction orthogonal diagonalization. There is no use of numerical eigendecomposition, random sampling, or external packages in the checker.

External historical priority, statistical calibration beyond second moments, and independent mathematical audit have not been performed.
