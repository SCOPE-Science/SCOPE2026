# Independent mathematical audit

## correctness

PASS

At (e_j,−e_j), the scores are ±α, so attention messages equal ±t e_j with t=tanh α. If η s_j t>1, the residual is ∓R e_j for R=η s_j t−1>0 and the normalized map interchanges the two states exactly. Tangent variations have zero first-order score derivatives because they are perpendicular to e_j; on every transverse eigenmode k≠j the exact one-step Jacobian block is [[1−ηs_k p,−ηs_k(1−p)], [−ηs_k(1−p),1−ηs_k p]]/R with p=(1+t)/2. Common/difference eigenvalues are q_com=(1−ηs_k)/R, q_dif=(1−ηs_k t)/R, and the second-step Floquet multipliers are their squares by global sign equivariance. Solving both strict unit-circle inequalities gives s_k/s_j<t and η s_j>2/[t(1+s_k/s_j)]; combining k forces j=1, t>s2/s1 and η>2/[t(s1+sd)]. Equality gives a multiplier +1, precluding exponential attraction without asserting nonlinear boundary instability. Independent exact Fraction evaluation with s=(8,2,1),t=1/2,η=1/2 gives {0,1/4,1/4,9/16} and η*=4/9. Exact scalar rational-grid comparisons also corroborate iff. The argument is local and excludes points where normalization denominator vanishes.

## originality

PASS

The most relevant discrete work treats positive-leading value eigenvalue fixed points (Altafini) or masked isotropic repulsive cycles (Gao–Yang–Chen). The closest negative-definite spectral selection work is continuous time with QᵀK=V, a different vector field. None logically implies the derived self-inclusive discrete two-edge anisotropic iff Floquet criterion. Known existence of repulsive attention flips is explicitly credited.

## value

PASS

The theorem gives a complete local bifurcation phase diagram for a minimal discrete attention system with distinct physical controls: the second strongest negative eigenmode decides if stabilization by gain is possible, but the weakest decides the sharp gain onset. This is an independently meaningful nonlinear dynamics classification, with a rational three-dimensional witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
