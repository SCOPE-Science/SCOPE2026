# Independent mathematical audit

## correctness

PASS

Balanced words of length at least four avoid the four binary reducibility exceptions of Chandgotia–Marcus–Richey–Wu, and the loop at the start state for the symbol opposite to the first bit gives primitivity. The loop state also has an edge to a different state, giving λ>1 from its positive eigenvector; independent length-k blocks give λ≤(2^k−1)^(1/k)<2. Hence λ is an irrational algebraic integer. If a positive power were rational, every conjugate would have the same power and hence modulus λ, contrary to strict Perron domination since all conjugates occur in the integer matrix spectrum. The weighted overlap identity follows by splitting appended forbidden words at their first occurrence; the possible overlaps are exactly the nonempty borders. Marking ones gives ρ=λ′(1)/λ, by analytic Perron perturbation, and at x₀=1/λ the derivative combination 2H_y−x₀H_x is the sum of Δ(b)λ^|b| divided by the square of the border polynomial. The Perron pole is simple with positive residue in the (1−x/x₀)^−1 normalization, so H_x(x₀,1)<0. With the full border balanced, no one-term cancellation is possible and two terms would require a rational positive power of λ. For the family, the only possible internal occurrence of 10001 other than the terminal suffix is across the middle zero run when m=3; it disagrees at the sixth bit with the original prefix. The only proper borders are therefore 1 and 10001, and λ−λ⁵<0 gives the stated positive frequency bias. Independent bounded replay using a failure-link automaton and the stationary distribution of its Perron-normalized transition chain checked the 348 balanced words at lengths 4,6,8,10 (no mixed-sign cases there), family border lists for 0≤m≤100, and positive limiting biases numerically for m=0 through 4. It reproduced λ≈1.999514450410 and ρ≈0.500000885746 for m=0.

## originality

PASS

The generating function, implication from all borders balanced, one-sided imbalance criterion and sign for the explicit word w₀ are prior. The supported contribution is the no-cancellation result for the mixed two-border case of the uniform-avoidance density conjecture, and the infinite family with that border profile and strict bias.

## value

PASS

This is a nontrivial restricted resolution of the uniform-avoidance half of an explicit conjecture. It decides the first mixed-sign case outside the published sign criterion for all lengths and supplies an infinite family exhibiting it. The mechanism—algebraic conjugacy of the growth root excluding two-term cancellation—explains why relative signs alone do not lead to an exact tie.

The dated certificate retains the supplied scientific assessment, sources and limitations.
