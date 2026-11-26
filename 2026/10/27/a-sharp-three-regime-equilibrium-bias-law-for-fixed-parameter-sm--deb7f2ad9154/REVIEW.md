# Independent mathematical audit

## correctness

PASS

At a joint fixed point the memory satisfies x−cᵢ=H(mᵢ), with H(m)=m+√ε m/√(φ²−m²) on |m|<φ, and primal stationarity is Σmᵢ=0. H is odd, strictly increasing, onto, and strictly convex for positive m. Its inverse h is odd, strictly increasing and strictly concave on positive arguments. Consequently 2h(x+a)+h(x−2a) has a unique zero, between −a and 0 by its endpoint signs; the two equal memories p>0 force the third to be −2p. Then H(p)+H(2p)=3a implies p<a and p<φ/2. For equal-curvature one- or two-client scalar quadratics the same inverse-score test gives the arithmetic mean by odd symmetry, even when the common curvature is not one. For φ<2a, p necessarily tends to φ/2. Writing δ=φ/2−p, the singular term in H(2p) is asymptotic to √(φε)/(2√δ), which balances 3(a−φ/2) and yields δ∼φε/[36(a−φ/2)²]. The regular contribution to H(p) is √(ε/3)+O(√ε δ), yielding the stated O(ε) remainder for x. At φ=2a the same singular term instead balances 3δ, giving δ³∼φε/36 and a negligible O(√ε) regular correction. For φ>2a the equation is regular in (p,√ε) at (a,0); differentiating gives the stated coefficient and O(ε) remainder on substitution in H(p)−a. For stability, qᵢ=(1−β)Ψ′(x−cᵢ−mᵢ)>0 and αᵢ=β−qᵢ lie in (0,1) under the sufficient hypothesis. At η=0 the simple slow eigenvalue 1 has right vector (1,(qᵢ/(1−αᵢ))ᵢ) and left vector (1,0,0,0). Differentiating the first row of the Jacobian gives its slope −Σqᵢ/[3(1−αᵢ)]<0, while all other eigenvalues start strictly inside the unit disk. This establishes local attraction for small positive η, not global convergence or a uniform choice of β as ε tends to zero. Replay via RESULT.md §§1–4; VERIFICATION.md and the attached diagnostic code were inspected, not executed.

## originality

PASS

The supported distinct claim is the exact fixed-parameter equilibrium, its three-regime asymptotics and attainable attraction for this equal-curvature SClip-EF instance. The update, and clipping bias as a general phenomenon, are established prior art.

## value

PASS

The smallest biased scalar equal-curvature instance exposes an algorithmic failure mode rather than curvature heterogeneity or stochastic noise: with feasible constant gains even a locally attracting joint fixed point can miss the exact minimizer. The explicit saturation threshold distinguishes persistent bias from two quantitative vanishing-bias regimes, helping interpret what smoothing can and cannot correct in this fixed-control model. The result neither overturns scheduled convergence theorems nor proves global behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
