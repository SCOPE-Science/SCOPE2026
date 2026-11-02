# An exact occupancy staircase for prey aggregation under crowding and predator satiation

## Finding
Fix a finite set of \(n\ge2\) identical habitats and a total prey biomass \(B>0\). The prey experiences logistic self-crowding in each habitat and a saturating, Holling-II loss in the presence of a fixed local predation pressure. In this model, the *exact* optimizer of total instantaneous net growth undergoes a staircase: as predation pressure increases, its number of populated habitats drops one at a time from \(n\) to \(1\). No optimum has unequal positive habitat biomasses, and no intermediate support size is skipped.

For \(k=1,\ldots,n-1\) set
\[
 c_k=\frac{r}{Kh}\left(1+\frac{hB}{k}\right)\left(1+\frac{hB}{k+1}\right),\quad c_0=+\infty,\quad c_n=0.
\]
Then \(c_1>c_2>\cdots>c_{n-1}>0\). For \(1\le k\le n\), if \(c_k<c<c_{k-1}\), the maximizers are **exactly** the permutations of the vector consisting of \(k\) copies of \(B/k\) and \(n-k\) zeros. At \(c=c_k\), precisely those equal-support vectors with support sizes \(k\) and \(k+1\) tie, and there are no other maximizers.

## Assumptions and scope
Let \(n\in\{2,3,\ldots\}\) and \(B,r,K,c,h\in(0,\infty)\). An admissible allocation is \(x=(x_1,\ldots,x_n)\in[0,\infty)^n\) with \(\sum_i x_i=B\). Define the instantaneous, additive net-growth functional
\[
 \mathcal G(x)=\sum_{i=1}^{n} f(x_i),\qquad
 f(t)=rt-\frac rK t^2-\frac{ct}{1+ht}.
\]
Here \(r\) is the intrinsic prey-growth coefficient, \(K\) the per-habitat crowding scale, \(h\) the predation handling/saturation coefficient, and \(c\) the fixed per-habitat pressure coefficient. All habitats have identical parameters. The analysis is conditional on a fixed current total biomass \(B\), not on an equilibrium, an evolving dispersal process, or a predator population responding endogenously to the allocation. Predation losses are local and additive across patches.

## Proof
**Step 1: a global maximizer cannot have two distinct positive coordinates.** Compactness of the simplex and continuity of \(f\) give existence. Write \(\alpha=r/K>0\). Direct differentiation gives
\[
 f'(t)=r-2\alpha t-\frac{c}{(1+ht)^2},\qquad
 f''(t)=-2\alpha+\frac{2ch}{(1+ht)^3},
 \qquad (f'')''(t)=\frac{24ch^3}{(1+ht)^5}>0.
\]
Thus \(f''\) is strictly convex on \([0,\infty)\). Suppose a global maximum has two unequal positive coordinates \(a<b\). Varying those two coordinates by opposite sufficiently small amounts preserves admissibility. First-order stationarity on this line requires \(f'(a)=f'(b)\), or equivalently
\[
 \frac1{b-a}\int_a^b f''(t)\,dt=0.
\]
The strict upper Hermite–Hadamard inequality for the strictly convex continuous function \(f''\) gives
\[
 0=\frac1{b-a}\int_a^b f''(t)\,dt
 <\frac{f''(a)+f''(b)}2.
\]
The second derivative along the feasible opposite-coordinate transfer is consequently \(f''(a)+f''(b)>0\), incompatible with a local maximum. Therefore all strictly positive coordinates of any global maximizer are equal. As their sum is \(B\), a maximizer has exactly \(k\) positive coordinates, each \(B/k\), for some integer \(1\le k\le n\).

**Step 2: exact competition between support sizes.** Such an allocation has value
\[
 G_k=k f(B/k)=rB-\frac{rB^2}{Kk}-\frac{cB}{1+hB/k}.
\]
For every \(1\le k<n\), elementary cancellation yields the identity
\[
 G_k-G_{k+1}
 =\frac{B^2}{k(k+1)}\left[\frac{ch}{(1+hB/k)(1+hB/(k+1))}-\frac rK\right].
\]
Hence \(G_k>G_{k+1}\) exactly when \(c>c_k\), they are equal exactly when \(c=c_k\), and the inequality reverses below \(c_k\). Because both factors \(1+hB/k\) and \(1+hB/(k+1)\) strictly decrease as \(k\) increases, the critical numbers satisfy \(c_1>\cdots>c_{n-1}\).

**Step 3: exhaust all global optima, including boundaries.** If \(c_k<c<c_{k-1}\), then for each \(j<k\), \(c<c_j\) and hence \(G_j<G_{j+1}\); for each \(j\ge k\), \(c>c_j\) and hence \(G_j>G_{j+1}\). Thus \(G_k\) is the unique largest among \(G_1,\ldots,G_n\). At \(c=c_k\), the preceding comparisons are strict except for \(G_k=G_{k+1}\); these two, and only these two, are largest. Step 1 rules out all other types of maximizer. Every listed equal-support vector is feasible and has the corresponding largest value, completing necessity and sufficiency. No assumption about the sign of the maximum net growth is needed.

## Verification
All derivatives and the adjacent-support difference were independently rechecked using exact rational computations. The standalone `checker.py` evaluates every support interval and every threshold for \(2\le n\le9\) under three rational parameter sets, tests all adjacent-value identities, and exhaustively checks rational biomass-allocation grids for \(n=2,3,4\). On the retained package it reports **PASS 4963 exact rational assertions**. These finite calculations corroborate the algebra and examples but are not used to replace the universal convexity-and-comparison proof.

For a fully rational five-habitat illustration, take \(B=6\), \(r=1\), \(K=20\), and \(h=1/2\). The four thresholds are exactly \(c_1=1\), \(c_2=1/2\), \(c_3=7/20\), and \(c_4=7/25\). Accordingly \(c=1/5,3/10,2/5,3/5,6/5\) yield unique optimal support sizes \(5,4,3,2,1\), respectively, up to habitat permutation. To replay, extract `checker.py` into the same directory as this document and run `python3 checker.py` using standard Python 3; no third-party dependencies are required.

## Relationship to prior work
Schreiber and Vejdani (2005, publicly accessible November 1) analyze coevolutionary patch preference in predator–prey systems with handling time and demonstrate the relevance of aggregation. Their patch-preference and ecological-stability conditions are not the fixed-total-biomass, additive Holling-II/logistic instantaneous-growth optimization proved here; in particular, their results do not supply this \(n\)-habitat sequence of exact critical pressures and the exhaustive equal-support optimizer classification.

Barraquand and Murrell (2013) analyze how nonlinear predator–prey interactions change under spatial aggregation and spatial averaging, providing direct motivation for the competition between saturation and crowding. Their analysis of spatial moment equations does not furnish the present finite-dimensional constrained-optimization theorem or its no-skipping transition law. Holt's earlier two-patch models address habitat selection and dynamical consequences, but the inspected material does not imply the precise general \(n\)-patch statement. Generic results in nonlinear resource allocation may yet furnish a more abstract route to the same classification; historical priority is therefore not independently established.

## Limitations
The claim is only about instantaneous net growth for a given \(B\), with fixed predation pressure, homogeneous habitat qualities, local density-dependent crowding, and additive Holling-II losses. It does not show that prey behavior achieves the mathematical optimum; it does not characterize predator feedback, long-run abundance, extinction, migration costs, predator redistribution, stochastic environmental noise, or landscape heterogeneity. Because each optimal support size is an integer, near-threshold changes may be small in objective value even when habitat occupancy changes discretely. No empirical field validation or independent audit has been performed.

## References
1. S. J. Schreiber and M. Vejdani, “Handling time promotes the coevolution of aggregation in predator–prey systems,” *Proceedings of the Royal Society B* **273** (2006), 185–191. First public version recorded November 1, 2005. DOI: https://doi.org/10.1098/rspb.2005.3236. Open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1560034/.
2. F. Barraquand and D. J. Murrell, “Scaling up predator–prey dynamics using spatial moment equations,” *Methods in Ecology and Evolution* (2013). DOI: https://doi.org/10.1111/2041-210X.12014.
3. R. D. Holt, “Population dynamics in two-patch environments: Some anomalous consequences of an optimal habitat distribution,” *Theoretical Population Biology* (1985). DOI: https://doi.org/10.1016/0040-5809(85)90027-9. Author-hosted manuscript: https://people.clas.ufl.edu/rdholt/files/012.pdf.
