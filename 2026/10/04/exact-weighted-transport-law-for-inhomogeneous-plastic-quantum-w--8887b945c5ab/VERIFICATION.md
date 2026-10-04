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

The proof is analytic. The key checks are:

1. With \(b_x=\cos\theta(x)\), the right maximal path from \(x\) to \(x+2\) contains the factor \(P_+C(x+1)P_+=-b_{x+1}P_+\), while the left maximal path contains \(P_-C(x-1)P_-=b_{x-1}P_-\).
2. After arrival at the same site, the two maximal-path contributions lie in the orthogonal subspaces \(\Lambda(y)^{-1}P_+\mathbb C^2\) and \(\Lambda(y)^{-1}P_-\mathbb C^2\). This removes cross-terms in the squared norm.
3. The upper bound \(\|[W,A(a)]\|\le\sup_x b_{x+1}|a_{x+2}-a_x|\) is saturated by a state localized at the left endpoint of a selected edge with coin state \(U_x^*|0\rangle\), where \(U_x=C(x)\Lambda(x)\).
4. The Connes constraint is therefore exactly \(|a_{x+2}-a_x|\le2\epsilon/b_{x+1}\). The distance function from the origin in this weighted parity graph is itself admissible and saturates the state-distance upper bound.
5. In the homogeneous specialization \(b_x=b\), the unique infinite-line path from \(0\) to \(x\in2\mathbb Z\) has \(|x|/2\) edges, each of length \(2\epsilon/b\), yielding \(d(0,x)=\epsilon|x|/b\), exactly the source formula.

The bundled checker constructs finite periodic walk matrices with position-dependent coins and \(\Lambda\), computes commutator operator norms by singular values, and verifies the predicted edge formula. It also checks the weighted-cycle distance specialization. Numerical agreement is not used to promote finite evidence to an infinite proof.
