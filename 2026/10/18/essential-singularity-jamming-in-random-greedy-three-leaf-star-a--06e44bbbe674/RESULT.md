# Essential-singularity jamming in random greedy three-leaf-star adsorption

## Finding

For each integer \(N\), take the complete bipartite graph \(K_{a_N,b_N}\), where \(a_N+b_N=N\), \(a_N/N\to(1+\delta)/2\), \(b_N/N\to(1-\delta)/2\), and \(-1<\delta<1\). Independently assign each distinct labeled copy of the three-leaf star \(K_{1,3}\) a continuous uniform priority. Process copies in increasing priority, accepting a copy if all four of its vertices remain vacant. Let \(U_N\) be the number of vacant vertices at termination. Then

\[
\frac{U_N}{N}\xrightarrow{\mathbb P}F(\delta),\qquad
F(\delta)=\begin{cases}0,&\delta=0,\\ |\delta|\exp\!\left(\frac{1-\delta^{-2}}2\right),&\delta\ne0.\end{cases}
\]

The same convergence holds in mean. The function \(F\) is positive at every nonzero imbalance and is flat at balance: it extends to a smooth function at \(\delta=0\) with every derivative zero there, although it is not identically zero in any neighborhood. This is an essential-singularity, rather than a power-law, imbalance response.

There are balanced-feasibility examples with extensive random jamming: for \(N=40m\), \(a_N=28m\) and \(b_N=12m\), a perfect covering by \(K_{1,3}\) copies exists, yet
\[
U_N/N\xrightarrow{\mathbb P}(2/5)e^{-21/8}=0.0289759\ldots.
\]

## Assumptions and scope

Each star is a four-vertex *subgraph* with its specified center and three specified leaves; there are \(a\binom b3\) centers in the first part and \(b\binom a3\) centers in the second. A star is accepted only if all four vertices are vacant, without replacement. Equal continuous random priorities generate a uniformly random permutation of all candidate stars. Only fixed limiting \(\delta\) is considered; no critical finite-size scaling at \(\delta_N\to0\) is asserted. The theorem covers all sequences of integer class sizes with the stated limits, without arithmetic divisibility conditions.

## Proof

**1. Exact reduced chain.** As every still-eligible star has survived all earlier priorities, conditional on the accepted history the next accepted star is uniform among the eligible stars. At remaining counts \((a,b)\), let
\[
W_A=a\binom b3,\qquad W_B=b\binom a3.
\]
The next accepted star changes counts by \((-1,-3)\) with probability \(W_A/(W_A+W_B)\), or by \((-3,-1)\) with probability \(W_B/(W_A+W_B)\). This identity is exact even though the underlying priority list is sampled only once. The chain stops if there are no eligible stars, which requires either one part empty or both parts of size at most two. In the latter case at most four vertices remain.

**2. Deterministic limit away from the boundary.** In accelerated time \(t=k/N\), write \(s=(a+b)/N\), \(d=(a-b)/N\). Each accepted copy consumes four vertices, so \(s(t)=1-4t\) exactly at discrete time points. As long as both normalized class counts are bounded away from zero, the transition probabilities converge uniformly to \(p_A=b^2/(a^2+b^2)\), \(p_B=a^2/(a^2+b^2)\), with the right-hand counts interpreted as normalized quantities. The limiting equations are
\[
\dot s=-4,\qquad \dot d=-\frac{4sd}{s^2+d^2},\qquad (s(0),d(0))=(1,\delta).
\]
Their right-hand side is locally Lipschitz where \(s>0\). Bounded chain increments, Azuma's inequality for the martingale of centered steps, and discrete Gronwall therefore give convergence uniformly on every time interval staying a positive distance from either class-count boundary. Explicitly, the martingale fluctuations are \(O_{\mathbb P}(N^{-1/2})\) on fixed intervals, and the drift approximation is \(O(N^{-1})\) when both classes are bounded below by a positive multiple of \(N\).

**3. First integral and the terminal value.** When \(\delta\ne0\), the sign of \(d\) is preserved by the deterministic equations. Direct differentiation shows
\[
\frac{d}{dt}\left[|d|\exp\left(-\frac{s^2}{2d^2}\right)\right]=0.
\]
Its initial value is \(|\delta|\exp(-1/(2\delta^2))\). The continuous solution reaches the first class-count boundary at \(|d|=s\), at which the invariant equals \(s e^{-1/2}\); hence the terminal total fraction is exactly \(F(\delta)\). It is positive for \(\delta\ne0\) and smaller than one. To justify transfer of this boundary value to the discrete process, fix a small \(\varepsilon>0\) and stop the fluid approximation when the minority count first reaches \(\varepsilon N\). From that point each accepted copy removes at least one minority vertex; hence at most \(\varepsilon N+O(1)\) additional copies can be accepted before termination, and the residual total fraction changes by at most \(4\varepsilon+o(1)\). The continuous terminal total is approached as \(\varepsilon\downarrow0\). For \(\delta=0\), uniqueness gives \(d(t)=0\) for \(t<1/4\); for any fixed \(\varepsilon>0\), convergence up to \(t=(1-\varepsilon)/4\) leaves only \(\varepsilon N+o_{\mathbb P}(N)\) vertices, and the final count cannot increase. Thus the terminal fraction converges to zero.

**4. Mean convergence and flatness.** Since \(0\le U_N/N\le1\), convergence in probability implies convergence in expectation. For nonzero \(\delta\), \(F(\delta)=e^{1/2}|\delta|e^{-1/(2\delta^2)}\); standard repeated differentiation shows that every derivative tends to zero as \(\delta\to0\), yielding the smooth flat extension.

**5. Packing feasibility witness.** For \(a=28m,b=12m\), choose \(m\) disjoint stars centered in the first part and \(9m\) centered in the second. Their demands are \((m+27m,3m+9m)=(28m,12m)\), so a perfect star factor exists. Nevertheless \(\delta=(28-12)/40=2/5\), producing the positive limit above. The physical vertex labels can be partitioned into disjoint groups of these sizes, so this is an actual covering, not a merely fractional demand calculation.

## Verification

The accompanying standalone `verify.py` independently evaluates exact rational terminal distributions using both labeled-vertex physical stars and the two-count chain, for all \(1\le a,b\le5\). It also runs reproducible finite-size simulations at three sizes and checks the perfect-factor witness. These finite checks independently test the rates and numerics; they are not substitutes for the asymptotic martingale argument. Run with `python3 verify.py` (Python standard library only).

## Relationship to prior work

Random sequential adsorption has a substantial literature. De Oliveira and Tomé (1994) study inhomogeneous particle adsorption on *spatial bipartite lattices*, not uniform four-vertex-star packings on complete bipartite substrates. Bennett and Bohman (arXiv:1210.3581, first posted 2012) prove bounds for *regular* uniform hypergraphs; the present four-uniform star hypergraph has nonuniform vertex degrees on unequal parts, and their results neither give this exact density nor cover its positive imbalance-jamming branch. Hell and Kirkpatrick (1986) concern existence and optimization of star factors, not the terminal probability law of random greedy packing. In particular, feasible perfect packing does not imply high stochastic coverage. The length-two-path adsorption model has a power-law imbalance response; the present three-leaf-star process has a flat essential-singularity response and is not a corollary of that case.

## Limitations

No law of terminal fluctuations, quantitative convergence rate, or joint limit with vanishing imbalance is proved. Positive vacancy density for fixed nonzero imbalance is asymptotic and can be numerically tiny when the imbalance is small. General regular-hypergraph results do not automatically apply to this nonregular model. A complete bibliographic uniqueness claim is not made: a related older star-factor article was accessible only at abstract level.

## References

- M. J. de Oliveira and T. Tomé, *Inhomogeneous random sequential adsorption on bipartite lattices*, Physical Review E 50 (1994), 4523. DOI: 10.1103/PhysRevE.50.4523. Published 1994-12-01.
- P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581, first public version 2012-10-12; later Combinatorics, Probability and Computing 28 (2019), 816–825. Full arXiv preprint inspected.
- P. Hell and D. G. Kirkpatrick, *Packings by Complete Bipartite Graphs*, SIAM Journal on Algebraic Discrete Methods 7 (1986), 199–209. DOI: 10.1137/0607024. Abstract inspected; complete text not accessible in this review.
