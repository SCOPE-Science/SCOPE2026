# Unique variance-minimizing dispersal on balanced bipartite metapopulations

## Finding

Consider \(N=2m\ge4\) identical habitat patches divided into two groups of size \(m\). Every emigrant from a patch disperses uniformly among patches in the opposite group, with no within-group arrivals. At any dispersal probability \(d\in[0,1]\), each patch experiences an independent, equal-variance annual environmental innovation. For a common stable local autoregressive response \(a\in(0,1)\), there is **exactly one** dispersal rate \(d_N^*(a)\) minimizing stationary fluctuations of every local population.

For \(N=4\), this optimum is exactly \(d_4^*(a)=2/3\), independent of the autoregressive response. For each even \(N>4\), it lies strictly between \(2/3\) and \(N/(N+2)\), and decreases strictly as \(a\) increases. It approaches \(N/(N+2)\) as \(a\) decreases to zero. At fixed \(a\) and large even \(N\),
\[
d_N^*(a)=1-\frac{2}{(N-2)(1-a^2)^2}+O_a(N^{-2}).
\]
Thus the optimal migrant fraction tends toward one as the number of patches grows, although complete migration is never locally variance-optimal. The stationary variance of the overall spatial mean is independent of dispersal.

## Assumptions and scope

Let \(N=2m\) for an integer \(m\ge2\). Define the row-stochastic, symmetric \(N\times N\) matrix \(P\) by \(P_{ij}=1/m\) if patches \(i\) and \(j\) are in opposite groups, and zero otherwise. Let \(0<a<1\), \(0<\sigma^2<\infty\), and \(0\le d\le1\). The fluctuations evolve as
\[
Z_{t+1}=a\big((1-d)I+dP\big)Z_t+\eta_{t+1}.
\]
The innovations are centered, independent and identically distributed across times, independent of the past, and have covariance \(\sigma^2I\). Their components need not be normally distributed, but must have finite second moments. This is a linear population-fluctuation model, not a nonnegative count process. Stationary statements refer to its unique finite-second-moment stationary solution.

Write \(V_N(d)=\operatorname{Var}(Z_{t,i})\), which is the same for every patch in stationarity. Then
\[
V_N(d)=\frac{\sigma^2}{N}\left[\frac1{1-a^2}+\frac1{1-a^2(2d-1)^2}+\frac{N-2}{1-a^2(1-d)^2}\right].
\]
The unique optimum is the unique root in \((1/2,1)\) of
\[
\frac{2(2d-1)}{[1-a^2(2d-1)^2]^2}
=\frac{(N-2)(1-d)}{[1-a^2(1-d)^2]^2}.
\]

## Proof

**Stationary covariance.** Let \(u\) be the all-one vector and let \(s\) equal \(+1\) in the first group and \(-1\) in the second. The orthogonal projectors \(J=uu^{\mathsf T}/N\), \(H=ss^{\mathsf T}/N\), and \(R=I-J-H\) decompose \(\mathbb R^N\). Direct matrix multiplication shows \(P=J-H\). Its eigenvalues are \(1\) on \(J\), \(-1\) on \(H\), and \(0\) on \(R\), the last with multiplicity \(N-2\). Therefore \(B=a((1-d)I+dP)\) has eigenvalues \(a\), \(a(1-2d)\), and \(a(1-d)\), all of modulus strictly below one. The convergent stationary Lyapunov sum \(\Sigma=\sum_{k\ge0}B^k(\sigma^2I)(B^{\mathsf T})^k\) consequently equals
\[
\Sigma=\sigma^2\left[\frac{J}{1-a^2}+\frac{H}{1-a^2(1-2d)^2}+\frac{R}{1-a^2(1-d)^2}\right].
\]
Every diagonal of \(J,H,R\) is respectively \(1/N,1/N,(N-2)/N\), proving the variance formula. Since \(Ju=u\) and \(Hu=Ru=0\), \(\operatorname{Var}(N^{-1}\sum_iZ_{t,i})=\sigma^2/[N(1-a^2)]\), independent of \(d\).

**Unique optimum.** Put \(f(x)=1/(1-a^2x^2)\) for \(-1\le x\le1\). Direct differentiation gives
\[
f''(x)=\frac{2a^2(1+3a^2x^2)}{(1-a^2x^2)^3}>0.
\]
The two nonconstant terms \(f(2d-1)+(N-2)f(1-d)\) are thus strictly convex on \([0,1]\). Its derivative is negative at \(d=1/2\) and positive at \(d=1\). Hence the unique minimizer is interior and is precisely the stated root. For \(N=4\), at \(d=2/3\) the arguments \(2d-1\) and \(1-d\) both equal \(1/3\), and their derivative weights balance, giving the unique minimum. For even \(N>4\), the derivative at \(2/3\) is negative, since \(N-2>2\). At \(d=N/(N+2)\), the unweighted derivative numerators balance, but \(2d-1>1-d>0\), so the first (positive) term has strictly smaller squared denominator and the derivative is positive. This proves both strict bounds.

**Monotonicity in response.** For \(N>4\) write \(x=2d-1\) and \(y=1-d\). On the proved optimum interval, \(x>y>0\). The optimality equation is equivalent to
\[
\frac{2x}{(N-2)y}\left(\frac{1-a^2y^2}{1-a^2x^2}\right)^2=1.
\]
Its left side is strictly increasing in \(d\) (because \(x\) increases and \(y\) decreases) and strictly increasing in \(a\) (because \(x>y\)). Thus the unique solution decreases strictly in \(a\). In the limit \(a\downarrow0\), the equation becomes \(2(2d-1)=(N-2)(1-d)\), whose solution is \(N/(N+2)\). The four-patch case remains identically \(2/3\).

**Large-network asymptotics.** At fixed \(a\), put \(\delta=1-d_N^*(a)\). From the optimum equation, its left side is at most \(2/(1-a^2)^2\) while the right side is at least \((N-2)\delta\). Hence \(\delta=O_a(N^{-1})\). Substituting \(x=1-2\delta\), \(y=\delta\) into the exact equation and expanding at zero gives \((N-2)\delta=2/(1-a^2)^2+O_a(N^{-1})\), establishing the stated expansion. All bounds are uniform for each fixed \(a\in(0,1)\); no uniformity as \(a\uparrow1\) is claimed.

## Verification

The standalone `verify.py` uses Python standard-library exact rational arithmetic to construct the population transport matrix and the analytical covariance, and confirms the discrete Lyapunov equation and equal diagonal values. It checks \(N\in\{4,6,8\}\), \(a\in\{1/3,1/2,2/3\}\), and \(d\in\{0,1/4,1/2,2/3,3/4,1\}\): 54 full matrix checks. It also checks signs of the optimality derivative at comparison points, and checks the spatial-mean variance. Running `python verify.py` prints JSON identical to `certificate.json`. These checks validate the formulas only at the stated finite points. The all-size results follow from the above algebra and inequalities, not the enumeration.

## Relationship to prior work

Abbott (2011) analyzes how dispersal mediates synchrony and stability in stochastic metapopulations, including an AR(1) model with uniform mixing across all other populations. Its global-mixing topology and principal synchrony/stability statements differ from the present balanced bipartite network and exact variance-minimizing migrant fraction. Ripa (2000) derives linearized population-synchrony relations for spatial systems; the presently available abstract does not establish this graph-specific optimizer, but its potentially broader methods remain a bibliographic risk. The present claim is a topology-specific optimization of local stationary variance, not a claim that spectral covariance methods are new. General network Lyapunov equations alone do not state the exact minimizer, the exceptional four-patch equality, or the size-dependent monotonicity without this specialization and proof.

## Limitations

The model has a homogeneous stable response, independent and equal-variance innovations, uniform bipartite migration, no local demographic nonlinearities, and no nonnegativity constraint. The result proves minimization of stationary local variance and spatial mean-square contrasts, not extinction probabilities, nonlinear persistence, or a universal optimal dispersal level on general graphs. The approach uses established matrix spectral techniques. An older general linearized spatial model could contain an equivalent specialization not located in the inspected material; independent bibliographic review remains appropriate.

## References

1. Abbott, K. C. (2011), *A dispersal-induced paradox: synchrony and stability in stochastic metapopulations*, Ecology Letters **14**, 1158–1169. DOI: 10.1111/j.1461-0248.2011.01670.x. First online publication: 2011-08-04.
2. Ripa, J. (2000), *Analysing the Moran effect and dispersal: their significance and interaction in synchronous population dynamics*, Oikos **89**, 175–187. DOI: 10.1034/j.1600-0706.2000.890119.x.
3. Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000), *Dispersal, environmental correlation, and spatial synchrony in population dynamics*, American Naturalist **155**, 628–636. DOI: 10.1086/303350.
