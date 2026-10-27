# An exact locally driven exclusion steady state on true-twin graphs and hidden dissipation

## Finding

Let \(G=(V,E)\) be a connected finite simple undirected graph with \(N=|V|\ge3\), select an edge \(\{u,v\}\), and fix a number of exclusion particles \(1\le K\le N-1\). Every allowed particle exchange across an edge has rate one, except \(u\to v\) has rate \(p>0\) and \(v\to u\) has rate \(q>0\), where \(p\ne q\). Call \(u,v\) *adjacent true twins* if
\[
N_G(u)\setminus\{v\}=N_G(v)\setminus\{u\}=W.
\]
Write \(k=|W|\), \(B=K(N-K)/[N(N-1)]\), \(h(\eta)=\eta_v-\eta_u\), and \(\mu\) for the uniform law on the \(\binom NK\) configurations containing \(K\) particles.

**Exact state and converse.** The unique stationary law equals
\[
\boxed{\ \pi(\eta)=\binom NK^{-1}\left(1+\frac{p-q}{k+p+q}(\eta_v-\eta_u)\right)\ }
\]
if \(u,v\) are adjacent true twins. Conversely, with \(p\ne q\), a stationary density of the form \(1+c(\eta_v-\eta_u)\) relative to \(\mu\) exists for any nontrivial particle sector if and only if \(u,v\) are adjacent true twins; then necessarily \(c=(p-q)/(k+p+q)\).

**Exact localization.** Orient the driven edge \(u\to v\). For each \(w\in W\), the three edges \(u\to v\to w\to u\) carry a circulation \(B(p-q)/(k+p+q)\), while every other edge carries zero stationary mean current. In particular
\[
\boxed{\ J_{u\to v}=\frac{kB(p-q)}{k+p+q},\qquad
\operatorname{EPR}=\frac{kB(p-q)}{k+p+q}\log\frac pq>0.\ }
\]
All observables symmetric under swapping \(u,v\), including the joint occupancy law of all other vertices, retain their uniform-equilibrium expectations, and
\[
\boxed{\ d_{\mathrm{TV}}(\pi,\mu)=\frac{K(N-K)}{N(N-1)}\frac{|p-q|}{k+p+q}.\ }
\]

**Dense-graph hidden dissipation.** In the complete graph \(G=K_N\), suppose \(K/N\to\rho\in(0,1)\) with fixed \(p\ne q\). Although \(d_{\mathrm{TV}}(\pi,\mu)\to0\),
\[
\boxed{\ J_{u\to v}\to\rho(1-\rho)(p-q),\qquad
\operatorname{EPR}\to\rho(1-\rho)(p-q)\log(p/q)>0.\ }
\]
Thus asymptotically equilibrium-looking configuration laws coexist with nonvanishing irreversible dissipation.

## Assumptions and scope

Configurations are binary vectors \(\eta\in\{0,1\}^V\) with \(\sum_x\eta_x=K\). A directed jump \(x\to y\) changes \(\eta\) only when \(\eta_x=1,\eta_y=0\), by exchanging the occupations. On undirected edges other than \(\{u,v\}\), both directed rates are one. The distinguished edge has the two indicated rates. All rates are strictly positive; this and connectedness ensure irreducibility in each particle-number sector. The entropy production rate is the usual stationary continuous-time Markov-chain relative-entropy production, with the convention of summing each pair of reverse transitions once. No reservoir or particle creation is present.

## Proof

**1. Adjoint and the exact state.** Let \(L_0\) be the fully symmetric-exclusion generator. It is self-adjoint in \(L^2(\mu)\). For the occupation difference \(h=\eta_v-\eta_u\), its action is
\[
L_0h=\sum_{x\sim v}(\eta_x-\eta_v)-\sum_{x\sim u}(\eta_x-\eta_u).
\]
With \(L\) the biased generator, a direct inspection of the two configurations with unequal occupations on \(\{u,v\}\) gives the exact density-adjoint identity
\[
\boxed{\ L^*(1+ch)=cL_0h+[(p-q)-c(p+q-2)]h.\ }
\]
Here \(L^*\) denotes the adjoint relative to \(\mu\), so this equality holds pointwise on the complete finite configuration space, not only in expectation.

When the distinguished endpoints are adjacent true twins, cancellation of their identical exterior-neighbor contributions yields \(L_0h=-(k+2)h\). The adjoint identity consequently vanishes for \(c=(p-q)/(k+p+q)\). The density is positive because \(|p-q|<p+q+k\), and it is normalized since \(\mu(h)=0\). Irreducibility supplies uniqueness.

**2. Necessity of the twin condition.** Assume \(p\ne q\) and \(1+ch\) is stationary. The adjoint formula forces \(c\ne0\) and forces \(L_0h\) to be proportional to \(h\). Each side is a linear function of \(\eta\) on the fixed-\(K\) sector. For \(1\le K<N\), if the sum of coefficients of one such linear function vanishes on every \(K\)-subset, comparing subsets that differ by one element proves all its coefficients are equal. Since the coefficient sums in \(L_0h\) and \(h\) are both zero, that common coefficient must vanish. Thus the graph Laplacian sends the vector \(e_v-e_u\) to a scalar multiple of itself. At every vertex \(w\notin\{u,v\}\), its Laplacian coefficient is the difference between the indicators \(\mathbf1_{w\sim v}\) and \(\mathbf1_{w\sim u}\). They must agree, yielding exactly the adjacent true-twin condition. The eigenvalue is then \(k+2\), which forces the same \(c\) as above. The fixed-particle-sector linear-function argument also covers \(K=1\) and \(K=N-1\).

**3. Currents and unaffected marginals.** Under the uniform \(K\)-particle law,
\[
\mu(\eta_u=1,\eta_v=0)=\mu(\eta_u=0,\eta_v=1)=B.
\]
Under \(\pi\) the two probabilities are \(B(1-c)\) and \(B(1+c)\). Consequently the net driven-bond current is \(pB(1-c)-qB(1+c)=kBc\). The one-site means are
\[
\mathbb E_\pi\eta_u=K/N-Bc,\quad
\mathbb E_\pi\eta_v=K/N+Bc,\quad
\mathbb E_\pi\eta_w=K/N\quad(w\notin\{u,v\}).
\]
For each ordinary edge, the current from \(x\) to \(y\) equals \(\mathbb E_\pi(\eta_x-\eta_y)\). Hence \(v\to w\) and \(w\to u\) each carry \(Bc\) for \(w\in W\) and every other edge zero; adding the \(k\) triangle currents gives \(kBc\) across \(u\to v\). Conditional on the other vertex occupancies, the possible completions with \(\eta_u\ne\eta_v\) occur as a swapping pair and their linear-density corrections cancel. This proves unchanged outside marginal and, more generally, unchanged expectations for every swap-invariant observable. Finally, \(\mu(|h|)=2B\) gives \(d_{\rm TV}(\pi,\mu)=B|c|\).

**4. Entropy production.** For every pair of reverse configuration transitions, split the stationary logarithmic affinity into the log ratio of transition rates and the difference of log stationary probabilities. In the global sum the latter telescopes to zero by stationarity: it is \(\mathbb E_\pi[L\log\pi]=0\). The symmetric edges contribute no rate affinity, while the distinguished edge contributes \(\log(p/q)\) per net \(u\to v\) jump. Therefore the entropy production is \(J_{u\to v}\log(p/q)\), strictly positive since \(k\ge1\) and \((p-q)\log(p/q)>0\).

**5. Dense limit.** For \(G=K_N\), all other \(N-2\) vertices are common neighbors, so \(k=N-2\). With \(K/N\to\rho\), the factor \(B\to\rho(1-\rho)\), the density tilt \(c=(p-q)/(N-2+p+q)\to0\), and \(kc\to p-q\). The total-variation, current, and entropy-production limits follow from the exact finite-graph formulas.

## Verification

Run the self-contained Python 3 file `verify.py` by `python3 verify.py` (only the Python standard library). It enumerates all connected labeled simple graphs of orders 3, 4, and 5, all distinguished edges and all nontrivial particle sectors, with exact `Fraction` transition generators and unequal jump rates. It checks the full stationary residual vanishes exactly if the oriented endpoints are adjacent true twins; further irregular-graph checks test exact currents, marginal-independent total variation and entropy production. The executable reports `PASS 17040 exact/non-twin and limiting checks across 770 connected graphs`. Those finite checks corroborate but do not replace the proof covering all finite graph sizes and all positive rates.

## Relationship to prior work

The single-battery symmetric exclusion literature studies localized biases on rings and lattices, especially hydrodynamic density profiles and long-range correlations. Bodineau, Derrida and Lebowitz (2010) discuss a locally driven ring and the difficulty of its stationary measure. Sadhu, Majumdar and Mukamel (2011, 2014) derive field-induced density and correlation effects on extended lattices. Ayyer (2020) gives an exact steady state for a moving *asymmetric tracer particle*, not for one spatially fixed biased edge. Those source results are not the present graph-theoretic true-twin if-and-only-if law, its exact finite-state weight, or its localized triangle currents. Their lattice-scale coverage does not imply the statements here by restriction: a one-dimensional ring normally lacks adjacent true-twin edge endpoints. The ordinary reversible canonical exclusion measure and graph Laplacian identities are standard premises, not claimed as discoveries.

## Limitations

The classification concerns stationary measures that are *linear in the distinguished endpoint occupancy difference*. It does not assert that no other exact formulas exist on graphs without true twins; every finite irreducible chain has some stationary law. The statement assumes one oriented anomalous edge, equal symmetric background rates, constant positive rates, connected simple finite graphs and conserved particle number. Its current-localization assertion is specifically for the adjacent-true-twin class. No mixing-time, large-deviation, hydrodynamic limit, or multi-defect result is claimed. A general previously unknown stationary-measure theorem for driven finite-graph exclusions could imply the result; the literature comparison is not a proof of global priority.

## References

1. T. Bodineau, B. Derrida and J. L. Lebowitz, *A diffusive system driven by a battery or by a smoothly varying field*, arXiv:1003.5838v1 (2010), https://arxiv.org/abs/1003.5838.
2. T. Sadhu, S. N. Majumdar and D. Mukamel, *Long-range steady-state density profiles induced by localized drive*, arXiv:1106.1838v1 (2011), https://arxiv.org/abs/1106.1838.
3. T. Sadhu, S. N. Majumdar and D. Mukamel, *Long-range correlations in a locally driven exclusion process*, arXiv:1402.6669v1 (2014), https://arxiv.org/abs/1402.6669.
4. A. Ayyer, *A simple symmetric exclusion process driven by an asymmetric tracer particle*, arXiv:2001.02425v1 (2020), https://arxiv.org/abs/2001.02425.
