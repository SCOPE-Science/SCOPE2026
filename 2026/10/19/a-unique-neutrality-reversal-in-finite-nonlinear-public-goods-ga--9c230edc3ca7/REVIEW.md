# Independent mathematical audit

## correctness

PASS

PASS is for the corrected summary and slogan with the exact finite and strict-regime limit theorems unchanged. The frozen opening's unqualified fixed-group-size 1/N scaling is false if applied to all finite reversal regimes, even keeping the cost and multipliers fixed. For n=3, r1=3, rn=6, c=1, K>3 and K<5 for N>6, so strict finite reversal holds. Yet the limiting G(t)=t² gives I(τ)<1 for every fixed τ>0; by convergence and the unique finite crossing this gives Nw_c→∞, not a finite constant. The frozen slogan's 'only at intermediate selection strengths' is also misleading: advantage holds at all sufficiently small positive w. Both are corrected in repairs/5. For the proof, use E[H]=sM/L and E[H(H−1)]=s(s−1)M(M−1)/(L(L−1)) in the two focal samples, where s=n−1 and L=N−1. Their differences give the stated affine Δ_X with its doubled slope; summing from state 1 to j gives the quadratic prefixes, and summing those gives cN(N−1)/2 times [(r1+2rn)/(3K)−1]. The absorbing birth–death increment recurrence gives the reciprocal exponential sum for either update ratio. Jensen handles nonpositive prefix sum, with strictness unless all prefixes are zero; they are all zero exactly when both multipliers equal K. For positive prefix sum, if all prefixes are nonnegative the denominator decreases strictly below N; otherwise it is strictly convex with initial negative derivative and grows to infinity, so it has one minimum and crosses N exactly once at positive w. Affinity of P_j/(cj) makes its two endpoints decisive. The opposite-mutant ratio depends only on the terminal prefix, and is strictly above one in the synergistic reversal regime. For strict straddling of n and r1+2rn>3n the finite signs persist for large N, P_j/N converges uniformly to cG(j/N), and the Riemann-sum integrals converge locally uniformly in τ. G has positive mean and is negative on a nonempty interval, giving the strict convexity and sign bracket for the unique positive limiting root. Independent exact enumeration of the individual groups with and without cooperators confirmed the payoff gap for tested populations and verified the two numerical crossings 5.5922885957873975 and 1.1554760747212843 (/tmp/opencode/scope-review-analytic.py 5). Frozen verifier was inspected, not executed.

## originality

PASS

The repaired contribution is not the affine game, weak-selection condition, exponential fixation identity, or relative fixation ranking. It is the complete all-positive-strength neutral comparison with an exact endpoint inequality for reversal, its unique crossing and maximum, and the strict-regime scaling with the explicit integral. The inspected highly relevant sources give antecedents and different kinds of fixation reversals, not the conjunction of those claims or an equivalent stronger classification.

## value

PASS

Weak advantage does not tell which finite games retain advantage at high intensity. In this benchmark multiplayer game the exact criterion distinguishes two nonempty biological regimes of reversal, and shows how relative advantage over defectors can persist while the neutral advantage disappears. Uniqueness and an explicit population-size law locate this effect and are useful beyond isolated examples. The restricted scaling formulation avoids claiming the same law at the excluded parameter boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
