---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The count includes the root; the mixed marked derivative consequently includes the direct term kzT^k. The stated bivariate generating functions, their derivatives, and the Lagrange extraction give the displayed mixed moment, with k=0 contributing no direct term and k=n−1 handled by zero out-of-range coefficients. An independent derivation uses the cycle lemma: given multiplicities a_j, the number of trees is (1/n)n!/∏a_j!, and for root degree d it is d/(n−1) times the multinomial for the residual profile of the ordered d-forest obtained by removing the root. Their ratio is d a_d/(n−1), so the conditional root mean is Σ_j j²a_j/(n−1). The profile itself has the distribution of that of a uniform weak composition (X_i) of n−1 into n coordinates. By exchangeability the mixed moment equals E N_(n,k) times E[Σ_i X_i² | X_1=k]/(n−1). With m=n−1−k the latter sum in the numerator has mean k²+m+2m(m−1)/n by stars-and-bars factorial moments. Subtracting E R_n=3(n−1)/(n+1) times E N_(n,k) yields P_n(k) over the stated denominator. The binomial factor is positive at every feasible k. Direct evaluation at k=0,1,2,3,4 gives the claimed signs and the last positive sizes 3,7,24 for k=2,3,4; the convex polynomial is already positive and increasing at k=5. At n=2 the tree is deterministic. The binomial ratio tends to 2^(−k−1) for fixed k, and the polynomial prefactor scales as stated. The two balancing equations follow from deterministic total vertex and child counts. A fresh enumeration recursively combined nested child-tuples over ordered positive compositions of n−1, verifying 72 exact covariance and balance checks on 6,917 shapes for 2≤n≤10. Frozen VERIFICATION.md and verify_plane_root_degree.py were inspected, not executed; their separate preorder-word replay through n=11 is documented there, and neither bounded test proves the general identities.

## originality

PASS

Do not credit the separate root and profile marginals, the cycle-lemma representation, or the k=0 covariance as uncovered content: the last is exactly reproduced by a distinct leaf-count record and dominated there by conditional leaf ordering. The supported distinct claim is the full finite root-versus-children-count profile law, especially the evaluated non-leaf coefficients and complete finite sign thresholds. Neither the matched leaf, depth or recursive-tree records nor the primary passages give a stronger evaluated result covering it.

## value

PASS

Root degree is a canonical distinguished local statistic and the outdegree counts are the natural global profile, with two deterministic constraints. The theorem quantifies signed dependence which their separate laws and uniform proportions cannot predict. The strict finite sign reversals for degrees 2, 3 and 4, and strict positivity above that range, give meaningful precise cutoffs beyond an isolated leaf formula or a single small computation. The fixed-degree limit does not claim anything uniform in k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
