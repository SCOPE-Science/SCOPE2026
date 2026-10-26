# Scientific self-review

## Correctness — PASS

The claim concerns the mean of the **realized** reduced-coin purity, not the purity of the averaged density operator. The exact state after two steps is a sum over the ordered coin labels \(a,b\) at vertex \(e_a\oplus e_b\). Diagonal contributions are computed using the Haar-row Dirichlet second moment. For different final coin labels, the hypercube has exactly two matching path pairs, and independent Haar phases remove their cross term. The disjoint-entry unitary fourth moment \(1/(d^2-1)\) gives the off-diagonal contribution. The components sum to the stated rational function, with no uncontrolled limit or finite-enumeration inference. The attached code reconstructs two-step vertex amplitudes and checks 40 deterministic and stochastic assertions across eight dimensions, including 36,000 independent sampled coin pairs. The all-dimensional proof is symbolic and does not rely on the samples. The theorem explicitly excludes \(d=1\).

## Originality — PASS (self-review)

The primary 2026 source derives the averaged quantum channel and the hypercube walk, but its fully accessible 15-page version does not develop nonlinear single-realization reduced-coin purity. Vieira–Amorim–Rigolin (2013) and Fang *et al.* (2023) concern different random-coin ensembles or deterministic entangling protocols for one-dimensional walks. The exact dimension-three first-interference crossover does not follow from their statements without changing the object and calculating a nontrivial fourth-moment contraction. Targeted searches did not identify identical formulas; failure to find one is not proof of global novelty. Standard Haar–Weingarten moment theory can be used to derive the result, so unexamined general random-walk or random-circuit purity theorems remain a priority risk.

## Value — PASS

Coin–position purity is a physically motivated entanglement diagnostic for the model: an averaged depolarizing quantum channel erases the relevant nonlinear trajectory statistic. The two-step time is natural because it is the **first time two different coordinate-flip histories can reach the same vertex**, introducing coherent off-diagonal coin terms. The exact formula reveals a sharp dimension-dependent *direction reversal* of the mean entanglement change, plus its distance from maximally mixed coin purity. The crossover is not a parameter renaming or a routine inference from averaged transport; it separates two physically distinct finite-time regimes while making no broad later-time claims.

## Closest literature and risks

A. C. Quillen, Physical Review A 114, 042410 (2026), establishes the walk and its averaged channel; exact coincidence with this model is deliberate, and the new nonlinear observable is different. Vieira–Amorim–Rigolin (2013) and Fang *et al.* (2023) develop random-coin and optimal-coin entanglement phenomena under different protocols. Standard unitary-design moment calculus is a plausible general route to the formula; uninspected broader random-circuit literature might imply it implicitly. The evidence justifies a limited self-review originality judgment, not priority certification. Additional limits: no later-time monotonicity, no samplewise sign, no von Neumann entropy claim.

Self-review: passed. Independent audit: not yet performed.
