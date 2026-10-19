# Review of the eight-vertex path Padé positivity result

## Correctness — PASS

The proof identifies the first nonvanishing powers of the completed Gauss–Legendre rational step on a path, and explicitly handles the vanishing sixth-order coefficient. For the eight-vertex path, the accompanying standard-library checker reconstructs all entries over exact rational arithmetic and verifies the 64 coefficient-wise matrix identities \(Q(h)P(h)=4D(h)M(h)\). Its root and coefficient-sign checks, together with Descartes’ rule and positivity of \(D\), rigorously determine the complete real-timestep nonnegativity set \(\{0\}\cup[\alpha,\beta]\). Polynomial identities are not justified by finite sampling alone: every coefficient is compared. The analytical small-step path argument covers all positive path sizes, not merely tested sizes.

## Originality — PASS, with explicit priority limitations

The first Padé small-step obstruction from a negative seventh coefficient is established mechanism, not offered as new. Zappavigna–Colaneri–Kirkland–Shorten (2012) use a directed nilpotent shift, and Lóczi–Ketcheson (2014) establish a zero uniform radius of absolute monotonicity. The close published “Eight-state barrier for Markov positivity of the [2/2] Padé map” already proves positive small-step behavior for all Markov generators with at most seven states and a disconnected window for a directed pure-birth eight-state chain. That covers a lower-dimensional part of the present context, but its generator, algebraic threshold polynomial, and upper endpoint differ substantially from the reversible eight-vertex path. The assessed distinct result is the exact path-specific interval (and its explicit F/G boundaries) under unit-rate symmetric graph diffusion. No source inspected states it or contains a stronger result implying it; an unlocated equivalent historical result remains possible. Jin–Lazarov–Thomée–Zhou (2015) discuss threshold positivity in different subdiffusion discretizations, not this rational heat-path integrator.

## Value — PASS

Preservation of nonnegative heat solutions is fundamental for physically meaningful monotone time integration. This finding gives the complete, exact sharp time-step regime on the smallest obstructed symmetric path, including an isolated intermediate nonnegative phase despite failure for every sufficiently small positive time step. These concrete algebraic endpoints and the all-path threshold are natural, reproducible benchmarks for positivity-aware integrator analysis rather than arbitrary parameter slices.

## Limitations and sources

The theorem concerns the completed two-stage Gauss–Legendre step on unweighted paths; not internal stages, irregular conductances, other graphs, nor higher-dimensional heat stencils. It makes no claim of uniform timestep bounds for all generators or an exhaustive history of related literature. Inspected materials include the 2012 full manuscript of “Essentially Negative News About Positive Systems” (https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf), Lóczi–Ketcheson (2014, arXiv:1303.6651), the complete published directed-chain Result (https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md), and initial material from Jin et al. (2015, arXiv:1510.02825). Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
