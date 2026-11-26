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

An independent backward check tracks the initial ancestors of one strategy and one game label sampled at time t from independently uniform individuals. Write a=p_s/2, b=p_g/2. When the two current ancestral carriers coincide, going one step backward separates them if that carrier was focal, its model was distinct and exactly one trait copied; the probability is s=(N−1)(a+b−2ab)/N². For distinct carriers, the probability of joining is j=(a+b)/N²: either carrier was focal, had the other as model and copied the tracked trait. The two-state chain starts with coincident probability 1/N; after t steps that probability is π+(1/N−π)(1−s−j)^t with π=j/(s+j). Exchangeability gives a uniform individual conditional on coincidence and a uniform ordered distinct pair otherwise. Their initial joint label probabilities are h_sg and (N r_s q_g−h_sg)/(N−1). Substituting these gives the stated transient formula with λ=s+j and θ=(Nπ−1)/(N−1)=2ab/[N(a+b−2ab)+2ab], exactly the coefficient in the original propensities. A prescribed block where all other individuals in turn copy both traits from individual 1 has uniformly positive probability, yielding almost-sure joint consensus. Bounded convergence turns the transient limit into the fixation law for each arbitrary pair of labels. Excluding self multiplies both nonzero ancestry transition probabilities by N/(N−1), giving the same terminal law and the faster discrete-time rate. Finally, θ is strictly increasing in a and b; differentiating in a gives 2Nb²/[N(a+b−2ab)+2ab]². The maximum at a=b=1/2 is exactly 1/(N+1).

## originality

PASS

The supported distinct result is the explicit terminal joint table for arbitrary fixed initial paired labels and the discrete-step rate for the same neutral co-imitation mechanism. Ancestor separation/coincidence is standard, and the inspected two-locus Moran process even gives an analogous two-state calculation after rate matching. Its stated sampling theorems have different initialization and dynamics, however, and do not give the fixed-initial-data co-imitation law by substitution into their hypotheses. The model source supplies the exact update mechanism but not the neutral law.

## value

PASS

The exact joint table separates association caused solely by shared neutral copying from association that would require selection. The coefficient quantifies the effect at any N and propensity pair, with a sharp maximum, while the transient identity measures how long that dependence takes to build up under either pair-sampling convention. This supplies a useful comparison for the already studied coevolving game/strategy model, not merely a proof that consensus occurs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
