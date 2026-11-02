---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

In the specified symmetric payoff game with a-favoring ties, sample-k response is binomial tail m_k=ceil(k/(1+u)). For k≤4, divide F_{k,m}−p by p(1−p): h_1=0,h_2=1,h_3,2=2p−1,h_3,1=2−p,h_4,2=−3p²+5p−1,h_4,1=3−3p+p². The u<3 mixture is concave with h(1)=1−θ_1≥0, hence no positive-to-negative crossing at an interior zero when θ_1<1; θ_1=1 yields a zero field, not asymptotic attraction. When u≥3 all nontrivial terms strictly positive. Endpoints u=2,3 obey the stated threshold changes. For 1<u<3/2 and θ_2=α,θ_5=1−α, drift is p(1−p)[2α−1−(1−α)(6p³−9p²+p)]. The cubic has positive maximum M=7√7/18−1 at p_-=(3−√7)/6; two simple roots with +,−,+ drift precisely for 1/2<α<7√7/(18+7√7), with lower attracting, upper repelling, p=1 attracting, and a non-attracting fold at α_c. At α≤1/2 only a repelling interior crossing can occur. Independent exact rational calculations verified all binomial factorizations, α=0.503 root-sign brackets and both parameter-boundaries; infinite quantifiers rest on polynomial shape analysis.

## originality

PASS

Arigapudi, Heller and Schreiber 2025 AEJ Microeconomics, arxiv:2305.10301v2, Theorem 1 rules out stable interior miscoordination under homogeneous samples and Theorem 2 gives heterogeneous stable interior examples for sufficiently disparate/larger samples; the published theorem does not specify the sharp universal budget five or that all k≤4 mixtures fail. Its formulas provide the model but do not directly give the algebraic first threshold and exact 2/5 interval. Oyama, Sandholm, Tercieux 2015 establish sample-best-response selection/dominance sufficient conditions, not this two-sided interior-stability minimality. Izquierdo & Izquierdo focus on pure equilibrium stability and different statistical inference; no same cutoff established in inspected primary. Resultary sampling-best-response semantic search returned other finite game/sample problems but not this theorem. An earlier derivation based on their published general response function is a residual priority risk.

## value

PASS

A universal minimum observation budget for persistent mixed behavior is a natural structural threshold in heterogeneous best-response population dynamics. The surprising necessity of five draws (not just sufficiency) and exact bifurcation window distinguish a persistent mixed attracting state from mere diversity of response rules, with an explicitly competing pure-state basin. This is more than a low-order expansion of a known simple game.

The dated certificate retains the supplied scientific assessment, sources and limitations.
