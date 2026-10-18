# Scientific review

## Correctness — PASS

The theorem is a statement about the full-real-line heat operator coupled to the SIR balance. The explicit characteristic formula for the moment generating function yields an exact variance split into an initial-data tilted variance and \(Dt\), so no Gaussian closure is assumed. Since initial infectivity support is nonnegative, the conditional mean stays nonnegative and nondecreasing. Boundedness of the compact initial support and the finite-time quadratic bound on mean infectivity rule out finite-time blowup. Total removed mass bounds the time integral of infection; if the susceptible limit were positive, the conditional mean would grow at least quadratically and force positive log-prevalence growth, contradicting bounded prevalence. With zero diffusion or a fixed cap, integrated force of infection has a finite upper bound. This establishes every stated quantifier and equality limit. The included standalone arithmetic checker verifies the characteristic identity and non-Gaussian variance formula but is not a substitute for the infinite-time proof.

## Originality — PASS (specific theorem; residual risk acknowledged)

Lamata-Otín et al. [1] analyze early-time and cutoff-dependent outbreaks, approximate diffusion-induced variance, and investigate the effect of finite interventions on attack rate. Their paper's no-cutoff active phase is not a theorem about exact terminal attack rate for arbitrary compact initial trait measures. The exact full-line moment transformation and sharp comparison with both \(D=0\) and capped trait mutation are the narrow new scope. Berestycki et al. [2, Proposition 4] proved a qualitatively similar complete-attack phenomenon for a different model in which *susceptibles*, not infectives, carry a diffusing exposure-risk trait; this result is explicitly acknowledged as established precedent, rather than claimed anew. Almeida et al. [3] assume bounded contact kernels for their general heterogeneous final-size treatment. Classical Gaussian trait propagators are also not novel. The remaining possibility of specialized subsumption is a genuine originality risk.

## Value — PASS

The source calls infectivity a probability while using an unbounded continuous diffusion approximation. The exact all-time jump in final size at zero mutation, and its elimination under every genuine hard cap, exposes a substantive long-time distinction between that approximation and a physically admissible infection-probability state space. The result helps separate source-supported early-time evolutionary effects from universal, but mathematically artificial, infinite-time full-attack predictions. The result is not merely a finite numerical counterexample, and it holds for every compactly supported initial infected-trait measure. It deliberately makes no claims about finite populations, biological certainty, or nonlinear interventions.

## Closest literature and scientific limitations

The closest conceptual precedent is Berestycki et al. [2, Proposition 4], with susceptible-risk diffusion; the closest identical differential equation is Lamata-Otín et al. [1], whose supplementary material treats approximations and finite-horizon behavior. The strict limitation is full-line mutation with Gaussian tails outside the probability interval. Any bounded physical trait law has the opposite survivor lower bound. Existing results in broader mutator and epidemic literature may yet imply this special conclusion. All assumptions and remaining risks appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
