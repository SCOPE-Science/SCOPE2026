# Scientific review

## Correctness — PASS

A single final claim has been evaluated: uniqueness of the optimal exponential incubation progression rate for every nonconstant nondecreasing final-size payoff on a finite star with one positive transmission window, plus convergence of all optima to a payoff-independent short-window limit. The exact conditional binomial formula uses the common random infectious lifetime; its derivative is derived without any independent-leaf marginalization error. Conditioning on root progression produces the piecewise continuous reward kernel. A Laplace-transform integration by parts gives the derivative as a difference of two positive kernels supported strictly to opposite sides of the transmission start. Their ratio is strictly monotone, with analytically verified opposite endpoint signs. The short-window argument is a probability-kernel convergence and a unique limiting crossing. No finite simulation is used to deduce an infinite-parameter conclusion. An independent forward-state Markov ODE implementation in `verify.py` reproduces selected probabilities and sign patterns, with explicitly stated numerical tolerances.

## Originality — PASS (provisional priority)

Hall and Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation* (arXiv:2108.07128v1, 2021-08-16; doi:10.1007/s00285-022-01854-9), supply exact rooted-tree SIR/SEIR marginal equations for fixed rates, not one-pulse all-payoff unimodality or its universal short-window optimal rate. Their primary MSC is 92D30. Cocomello and Ramanan (arXiv:2309.08829v1) address locally tree-like large-graph limits with time-dependent rates, not this finite star optimization. Ma and Ma (doi:10.3934/mbe.2006.3.161) study seasonally forced deterministic SEIR invasion thresholds. A general exact solver for a model does not make the one-crossing theorem an immediately stated special case; neither cited inspected paper states it. Related publications outside inspected material may still contain an equivalent optimization, so publication priority remains provisional.

## Value — PASS

A finite epidemic-contact season competes with latent-stage timing: progressing too slowly misses the season, while progressing too quickly risks recovery before it begins. The theorem proves exactly one optimal delay scale rather than just observing it numerically, for *every* monotone outbreak-size preference including multiple tail risks. More importantly, it explains the nonobvious universality of the short-contact-season optimum across number of contacts, per-contact intensity, and reward profile. This establishes a structural benchmark for seasonal activity planning or contact pulses, rather than a textbook probability calculation in a single parameter case.

## Limits

The pulse must begin at a strictly positive time, waiting times must be exponential, and leaves are terminal transmissions. Only one pulse and monotone utility of final leaf infections are covered. Publication priority is not exhaustively certified; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
