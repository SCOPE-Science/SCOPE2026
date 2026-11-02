# Sharp third-order dependence bounds for growth in three well-mixed habitats

## Finding
Consider three identical-sized, density-independent habitat patches with binary annual environmental quality and complete dispersal/mixing after reproduction. Their one-site and pairwise environmental statistics do **not** determine the sign of long-run population growth, even when all distinct habitat environments are pairwise independent.

The sharp result below determines exactly how unmeasured simultaneous three-patch favorable conditions affect growth. Let \(0<\ell<h\) denote low and high annual per-capita productivity, and let the favorable indicators \(H_1,H_2,H_3\in\{0,1\}\) be exchangeable within a year. Write
\[
p=\Pr(H_i=1),\quad q=\Pr(H_i=H_j=1)\quad(i\ne j),\quad r=\Pr(H_1=H_2=H_3=1).
\]
Given a feasible pair \((p,q)\), all compatible exchangeable laws are parameterized by precisely the interval
\[
\boxed{r_-:=\max\{0,2q-p\}\le r\le r_+:=\min\{q,1-3p+3q\}.}
\]
Let \(X_t>0\) be total population at the beginning of environmental year \(t\). With \(K_t=H_{1,t}+H_{2,t}+H_{3,t}\), its scalar growth rule is
\[
X_{t+1}=g_{K_t}X_t,\qquad g_k=\ell+\frac{k}{3}(h-\ell).
\]
Suppose complete environmental triples are iid across years (within-year independence is **not** assumed). Almost surely,
\[
\lim_{t\to\infty}t^{-1}\log\frac{X_t}{X_0}=\lambda(r)=\sum_{k=0}^3\Pr(K=k)\log(g_k).
\]
For fixed \((p,q,\ell,h)\), the exact growth interval is \([\lambda(r_-),\lambda(r_+)]\), and
\[
\boxed{\lambda(r)=\lambda(r_-)+(r-r_-)\log\frac{h(h+2\ell)^3}{\ell(2h+\ell)^3}.}
\]
The logarithmic coefficient is **strictly positive** for every \(h>\ell>0\). If \(r_-<r_+\), the lower and upper growth bounds have unique laws, and the sign of \(\lambda\) varies across the family precisely when \(\lambda(r_-)<0<\lambda(r_+)\); the unique zero then lies at \(r_--\lambda(r_-)/\delta\), where \(\delta\) is the positive displayed slope. Equality at an endpoint is a zero-exponent boundary, not a proof of demographic persistence.

A sharp witness uses \(p=1/2\), \(q=1/4=p^2\), \(\ell=1/30\), and \(h=10/3\). Thus every patch has the *same* marginal environmental distribution and all pairs of patch indicators are independent. At \(r=0\), there are zero favorable patches with probability \(1/4\) and exactly two with probability \(3/4\); at \(r=1/4\), there is exactly one favorable patch with probability \(3/4\) and three with probability \(1/4\), with labels uniformly chosen within each count. At both endpoints an isolated patch has geometric mean productivity \(\sqrt{h\ell}=1/3<1\). Yet
\[
\boxed{e^{4\lambda(0)}=\frac{300763}{810000}<1,\qquad e^{4\lambda(1/4)}=\frac{9826}{2025}>1.}
\]
Accordingly, completely mixed abundance declines exponentially almost surely in the first law and increases exponentially almost surely in the second, despite identical first- and second-order spatial environmental statistics. Two patches cannot exhibit this ambiguity: their full binary joint law is determined by their one-site marginals and the pairwise joint success probability.

## Assumptions and scope
Every annual triple is sampled independently from the same exchangeable distribution on \(\{0,1\}^3\). Both productivity levels are finite and positive, and individual output is linear in abundance. Complete redistribution makes all three patch abundances equal at the start of each reproduction year; there are no dispersal losses, density feedbacks, finite-population fluctuations or evolutionary changes. The pair \((p,q)\) must be feasible, that is, \(0\le p\le1\) and \(r_-\le r_+\); endpoints may coincide. The growth-exponent conclusion holds for any \(X_0>0\). In the exact witness, sampling each labeled favorable configuration uniformly within its prescribed count realizes exchangeability and the claimed pairwise independence.

## Proof
For \(K=\sum_i H_i\), exchangeability and the first three factorial moments give
\[
\begin{aligned}
\Pr(K=0)&=1-3p+3q-r,\\
\Pr(K=1)&=3(p-2q+r),\\
\Pr(K=2)&=3(q-r),\\
\Pr(K=3)&=r.
\end{aligned}
\]
Every feasible exchangeable binary law has this form, and all four coefficients are nonnegative if and only if \(r\) lies in the displayed closed interval; conversely, assigning equal weight to labeled states with equal \(K\) realizes every value in it. This proves sharpness of the moment fiber, not just necessary bounds.

Complete equal mixing gives the scalar recurrence shown above. Since \(\log g_K\) is bounded and annual triples are iid, the strong law of large numbers identifies the almost-sure exponent with its expectation. Substituting the four mass formulas, the coefficient of \(r\) is
\[
-\log g_0+3\log g_1-3\log g_2+\log g_3
=\log\frac{h(h+2\ell)^3}{\ell(2h+\ell)^3}.
\]
Its positivity is exact because
\[
h(h+2\ell)^3-\ell(2h+\ell)^3=(h-\ell)^3(h+\ell)>0.
\]
Therefore the exponent is strictly increasing in the free third-order moment and its extremal values are attained at the unique endpoint laws (unless the moment fiber is a singleton). All claimed persistence-sign cases follow from continuity and strict monotonicity. For two binary patches, the four labeled cell probabilities are determined by the two marginal success probabilities and one joint-success probability, proving minimality of three patches.

For the witness, the growth factors are \((g_0,g_1,g_2,g_3)=(1/30,17/15,67/30,10/3)\). The respective fourth powers of the geometric means are \(g_0g_2^3\) and \(g_1^3g_3\), giving the two exact fractions displayed; the inequalities are immediate by integer comparison. For each site, \(\mathbb E\log(\ell+(h-\ell)H_i)=\tfrac12\log(h\ell)=-\log3<0\). In both endpoint laws \(\Pr(H_i=H_j=1)=1/4=(1/2)^2\) for each distinct pair. These establish the witness in the full stated model.

## Verification
A standalone checker in `verify_three_patch.py` enumerates rational feasible moment fibers, verifies all four masses, first and second factorial moments, the exact cubic identity, and the endpoint construction. It additionally verifies the witness's two integer-rational sign inequalities and sampled strict logarithmic orderings. Execute with `python verify_three_patch.py` using Python 3 standard-library modules only. The general conclusion is proved above; finite enumeration and floating-point logarithm spot checks are ancillary rather than proofs of all parameters.

## Relationship to prior work
Keeling's metapopulation moment-closure analysis explains why higher moments can arise beyond means and covariances, but studies different finite-population dynamics [1]. Bascompte, Possingham and Roughgarden identify the geometric mean of spatially averaged fitness as central to the well-mixed growth criterion [2]. Schreiber examines temporal correlations and dispersal, including the well-mixed log-growth formula [3]. Wang and coauthors' spatial invariability theory uses an explicitly variance/covariance-based stability metric rather than long-run multiplicative growth [4]. The present claim does **not** assert the novelty of the geometric-mean criterion, the scalar strong law, or the elementary existence of pairwise-independent non-jointly-independent variables; it gives a sharp feasible-moment interval, monotone third-order growth law, and an exact pairwise-independent reversal witness in this three-habitat model. General moment-polytope optimization could independently imply part of the bounds; that priority question remains open for independent review.

## Limitations
The leading exponent refers to a density-independent real-valued population recurrence. Positive growth does not by itself prove finite-population survival or stationary persistence under density feedback. Near zero exponent the long-term sign is neutral in the exponential-rate sense only; no extinction assertion is made at equality. The result needs complete mixing, exchangeable within-year binary environments, strictly positive multipliers and iid years. Pairwise covariance is insufficient for this specific nonlinear multiplicative criterion; it is not claimed insufficient for variance-based stability metrics. A fully accessible version of the closest 2002 primary article could not be conclusively examined, so historical priority is provisional.

## References
[1] M. J. Keeling, “Metapopulation moments: coupling, stochasticity and persistence,” *Journal of Animal Ecology* 69 (2000), 725–736; first online publication recorded 25 December 2001. https://doi.org/10.1046/j.1365-2656.2000.00430.x

[2] J. Bascompte, H. Possingham and J. Roughgarden, “Patchy populations in stochastic environments: Critical number of patches for persistence,” *The American Naturalist* 159 (2002), 128–137. https://doi.org/10.1086/324793

[3] S. J. Schreiber, “Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence,” *Proc. R. Soc. B* 277 (2010), 1907–1914. https://doi.org/10.1098/rspb.2009.2006

[4] S. Wang et al., “An invariability–area relationship sheds new light on the spatial scaling of ecological stability,” *Nature Communications* 8 (2017), 15211. https://doi.org/10.1038/ncomms15211
