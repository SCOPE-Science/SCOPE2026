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

The fixed-point theorem holds for finite connected nonbipartite positive-edge support, including self-loops, with positive biases not all one. Any zero or one coordinate of a boundary fixed point propagates to its neighbors, giving only the two endpoints. For two interior fixed points, choose their order so the largest odds ratio R is greater than one. The odds scaling H_R is strictly concave, commutes with each response, and gives Wx<=W H_R(y)<=H_R(Wy). At a maximizing vertex both inequalities are equalities. Positivity propagates the maximizing ratio to neighbors, so every vertex maximizes and Jensen equality makes y constant on each neighborhood. Even walks join any pair in the connected nonbipartite case, making y constant everywhere and forcing all biases neutral, a contradiction. For connected loopless bipartite support the even walks instead make y constant separately on each part; the equations force one part's bias to be alpha and the other's reciprocal, and the displayed part-constant arc indeed consists of fixed points. For necessity in the nonbipartite case the positive vector z_i=1/x_i-1 satisfies Gamma^{-1} Wz>=z by convexity of the reciprocal function and the fixed-point odds equation. At least one row is strict by the even-walk argument; a positive left Perron vector then certifies rho_1>1. Complementing gives rho_0>1. For sufficiency, small perturbations of both endpoints along positive Perron vectors give ordered strict sub- and supersolutions; monotone iteration has an interior limit. For attraction, scale the equilibrium odds down and up to trap any interior start. Convexity/concavity of the respective H_r gives monotone inward barriers. For the common diminishing-step recursion, an alleged limiting nonzero barrier drift contradicts boundedness and sum a_k=infinity. Thus both barriers converge to the same unique equilibrium in both recursions. The stochastic conclusion concerns the original Tang et al. process (the record explicitly invokes it in Proof §5): use their compatible positive pseudo-counts and intended independent declaration sampling. Theorem 3 approaches the equilibrium set, not a specified point. Because this set is finite here, vanishing jumps exclude infinitely many switches among disjoint neighborhoods of its points. Theorem 4 repels each supercritical endpoint and selects the appropriate endpoint at or below one, including equality. In nonbipartite nonneutral scope the two at-most-one regimes cannot coincide, as shown in Tang et al.'s boundary analysis. This proves the stated stochastic selection for that process, not for every different Bernoulli law with the same one-coordinate marginals.

## originality

PASS

Credit the odds-rigidity theorem for arbitrary nonbipartite weights, the deterministic attraction result including diminishing steps, and the necessity direction of the bipartite exception. The original urn and its stochastic endpoint thresholds are established, and there is material later exact catalogue coverage of the nonbipartite uniqueness, Perron classification, synchronous convergence and stochastic selection, and later coverage of the reciprocal-bias equilibrium arc. The dates do not establish provenance, and those statements do not supply the full combination of diminishing-step attraction and necessity of the reciprocal-bias pattern. Tang et al. leave interior isolation open; the inspected earlier general convergence and opinion-dynamics results do not provide that additional rigidity.

## value

PASS

The interior may exist on heterogeneous networks, but convergence to an equilibrium set alone does not determine whether initial conditions or randomness select different limiting frequencies. Uniqueness on every connected nonbipartite support makes the coexistence limit determinate for this urn and gives a convergent deterministic computation. The graph-theoretic equality mechanism also explains precisely how bipartite nonuniqueness arises, rather than simply exhibiting an isolated counterexample. These contributions answer a concrete gap posed by the prior stochastic analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
