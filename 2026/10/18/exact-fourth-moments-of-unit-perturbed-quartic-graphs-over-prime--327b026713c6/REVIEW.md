# Scientific review: unit-perturbed quartic fourth moments

## Correctness — PASS
The exact claim concerns ordered additive energy of \((x,x^4+cx^2)\) over \(\mathbb Z/p^2\mathbb Z\) for all primes \(p\ge5\) and unit \(c\). The change to sum and two differences is bijective, and the collision polynomial factors into two independent linear factors and a quadric whose gradient never vanishes on its modulo-prime zero set. A one-factor zero has exactly \(p^2\) lifts; any multiple-component intersection has \(p^3\) lifts. The intersection cardinalities use standard binary quadratic-character sums, and inclusion–exclusion establishes the formula. Every coefficient and normalization was rechecked against independent direct pair-fiber counts, not just against the factorized equation. The phase reversal follows by character substitution, not extrapolation. The proof is valid uniformly in \(p\) and \(c\); finite checks are supplementary.

## Originality — PASS, subject to bibliographic risk
Hickman and Wright's 2018 prime-power Fourier restriction work provides polynomial-graph and congruence-estimate context but not this explicit quartic-plus-quadratic constant-input fourth moment. Mockenhaupt and Tao address the finite-field collision mechanism rather than the singular-lift prime-square calculation. Published notes on the unperturbed quartic over finite fields and on the prime-square parabola concern different objects and do not imply the formula for unit quadratic perturbations. Statement, parameter, equivalence, and broader-coverage searches found no directly covering published result. This is a best-knowledge comparison rather than a proof that no older equivalent identity exists; unindexed elementary arithmetic counts remain a residual risk.

## Mathematical value — PASS
The additive energy is the exact fourth Fourier moment of constant input on a natural degree-four deformation over the first nonfield local ring. The result covers every prime and every unit coefficient, not a selected numerical slice. It isolates how transverse and singular intersection lifts contribute and exhibits two genuinely distinct quadratic-residue branches with a mod-four reversal of their ordering, together with invariance under changing the higher base-prime digit of the perturbation. These are structural invariants that provide precise test data for local-ring Fourier restriction beyond the known pure-graph and parabolic examples. No sharp unrestricted operator norm is claimed.

## Closest literature and limits
References in `RESULT.md` identify the principal finite-ring restriction source and finite-field additive-collision source. An older hidden equivalent energy computation cannot be excluded. The proof does not determine the full two-sum fiber spectrum, the nonunit perturbation regime, or the unrestricted sharp extension constant.

Self-review: passed. Independent audit: not yet performed.
