# Independent audit — 2026/09/09/092

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

The trace discriminant of M is about −0.7667688361, so M has complex eigenvalues of modulus ρ=√0.28 and is linearly conjugate to a Euclidean similarity. Independently recomputing all 16 listed length-four centers in the conjugate metric |P⁻¹x| gives minimum squared pair distance 0.20467744730050 versus (2ρ⁴R)²=0.19407316994580, with R=2.80954952157263; the maximum center norm plus radius is 2.30930921186215<R. Thus the open balls are disjoint and the subsystem satisfies OSC. Since 16ρ⁴=1.2544>1, Moran's bound gives dimension at least log(16)/(4 log(1/ρ))≈1.08902729. The source calls this a “dominated-splitting cell”; repeated powers of a matrix conjugate to a rotation have bounded singular-value ratio, so this description is false and should not be used. Its phrase |y|_Y=|Py| making S a similarity is also reversed: the relevant metric on original x coordinates is |P⁻¹x|, as actually used in the separation calculation. The supplied certificate uses ordinary floating square roots at intermediate interval endpoints, so the assertion of fully rational interval arithmetic is overstated; the numerical margins are much wider than these rounding errors. The dimension conclusion follows from independently recomputed centers and separation.

## Originality — PASS

The overlapping-system results of Hochman–Rapaport require hypotheses such as exponential separation that were not shown for this fixed cell; the strong separation result of Bárány–Hochman–Rapaport applies to a subsystem here, not automatically to the full overlap dimension. The 16-word explicit separated subsystem is a distinct numerical certificate, though priority among computational examples is not exhaustive.

## Scientific value — PASS

The 1.089 lower bound gives a reproducible noncollapse result for this fixed attractor. It is substantially below the proposed Lyapunov-dimension equality and the record supplies no full-dimension measure.

Sources: https://arxiv.org/abs/1904.09812 ; https://arxiv.org/abs/1712.07353 . Open preprints sufficed.
