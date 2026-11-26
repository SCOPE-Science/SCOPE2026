# Independent mathematical audit

## correctness

PASS

The two fluctuation eigenspaces have eigenvalues δx and ε; the normalized block means give Q(x) with diagonal rx,s and squared off-diagonal mn a²x. Q is positive definite and its top eigenvalue exceeds both fluctuation levels. Any positive diagonal congruence with condition number k produces H=λ_min(DAD)D⁻² satisfying H≼A≼kH, and feasibility implies condition number at most k in the reverse direction. Averaging H under block permutations preserves feasibility. At optimal k the averaged scaling must attain both spectral bounds 1 and k. Its upper PSD slack has a strictly positive null vector w by Perron–Frobenius; every summand's PSD slack must annihilate w, forcing H equal to its average, since the difference is diagonal. Thus unrestricted optimal scalings cannot break the symmetry. Of the three competing ratios, λ+/λ− decreases then increases about x₀ by the trace divided by square root of determinant; λ+/(δx) strictly decreases and λ+/ε strictly increases by comparing positive Perron matrices Q/x and Q. For x_E≤x₀, δx≥ε throughout the candidate interval, so the competition there is between the decreasing quotient and increasing ε-branch. The sign of det(Q−εI) is the sign of λ−−ε; its affine root is the first claimed crossing if rc>ma², otherwise the quotient dominates. For x_E≥x₀, δx≤ε throughout the candidate interval, and det(Q−δxI)/x is affine decreasing with root (bs−na²)/(b(1−b)). Strict monotonicity outside each interval and the competing monotone branches inside prove both clipping and uniqueness; if x_E=x₀ the interval is a point. In the all-n example the eigenvalues are 1/2 and (n+2)/2 on the quotient and 3/4 and 1/2 on fluctuations at x=5/6; at n=3,x=1 the least eigenvalue is 1/2 and the largest is (16+√106)/10. All strict hypotheses hold in these checks.

## originality

PASS

General condition-number formulations and neighboring structured examples are known. The strongest indexed overlap 3470d222a671 independently records an algebraically equivalent clipped rule on the same domain, but does not establish that it preceded this finding and does not assert unrestricted uniqueness. The compared earlier material does not establish the full two-fluctuation classification with unrestricted rigidity and the all-size saturation example. This is a bounded originality assessment, not a priority claim or a claim that the formula appears nowhere else.

## value

PASS

Two exchangeable communities are a natural correlation model. A closed-form rule determines when each of two different within-community fluctuation levels, rather than quotient balancing, sets the optimum. It removes any entrywise optimization and establishes that a nonsymmetric diagonal cannot tie it. The fixed-ratio all-size example and the strict Jacobi gap illustrate directly why unit diagonal does not suffice. This is useful as an exact benchmark for general preconditioning, not merely a numerical improvement on one selected matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
