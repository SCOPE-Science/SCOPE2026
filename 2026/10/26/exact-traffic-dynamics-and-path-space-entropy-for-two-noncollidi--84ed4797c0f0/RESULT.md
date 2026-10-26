# Exact traffic dynamics and path-space entropy for two noncolliding walkers on balanced bicliques

## Finding
Let \(m\ge2\) be an integer. Two labelled particles perform independent continuous-time nearest-neighbour walks on \(K_{m,m}\), with rate \(1\) along every directed graph edge. Compare suppression of collision-making jumps (exclusion, \(\mathrm{Ex}\)) with conditioning the independent walks never to collide (the ground-state Doob transform, \(\mathrm{NC}\)). Put \(I_t=1\) when the particles occupy opposite bipartition classes and \(I_t=0\) otherwise. Their attempted collision rate is \(\kappa_t=2I_t\).

Under \(\mathrm{NC}\), \(I\) is a symmetric two-state chain with both transition rates \(r_m=2\sqrt{m(m-1)}\). Thus its stationary opposite-class probability equals \(1/2\), independent of the graph order; in stationarity,
\[
\mathbb E\kappa_t=1,\qquad \operatorname{Cov}(\kappa_0,\kappa_t)=e^{-2r_m t},\qquad
\operatorname{Var}\left(\int_0^t\kappa_s\,ds\right)=\frac{2t}{2r_m}-\frac{2(1-e^{-2r_mt})}{(2r_m)^2}.
\]
Under \(\mathrm{Ex}\), \(I\) has transition rates \(2m\) from \(0\) to \(1\) and \(2(m-1)\) from \(1\) to \(0\), so its stationary opposite-class probability is \(m/(2m-1)\) and its stationary mean collision hazard is \(2m/(2m-1)\).

The survival exponent for the independent walkers is
\[\lambda_m=2m-2\sqrt{m(m-1)}.\]
With identical initial distributions for both path laws (using the stationary distribution of the numerator process), their exact relative entropies on \([0,t]\) are
\[
D\!\left(\mathsf P^{\mathrm{NC}}_{\pi_{\mathrm{NC}}}\middle\|\mathsf P^{\mathrm{Ex}}_{\pi_{\mathrm{NC}}}\right)=t(\lambda_m-1),\qquad
D\!\left(\mathsf P^{\mathrm{Ex}}_{\pi_{\mathrm{Ex}}}\middle\|\mathsf P^{\mathrm{NC}}_{\pi_{\mathrm{Ex}}}\right)=t\left(\frac{2m}{2m-1}-\lambda_m\right).
\]
Both rates are strictly positive for all finite \(m\ge2\) and asymptotic to \(1/(4m)\).

## Assumptions and scope
The graph is complete bipartite with \(m\) vertices on each side, \(m\in\{2,3,\dots\}\); each particle jumps independently at rate \(1\) to each adjacent vertex. They are labelled and start at distinct vertices. Exclusion suppresses only jumps to the occupied vertex. Noncolliding means the infinite-horizon survival-conditioned Doob transform, not conditioning on a fixed finite time interval. The entropy identities compare trajectory laws with *matching* initial distributions; subscripts distinguish which stationary law provides that common initial distribution. The stated covariance and integrated-hazard variance assume the noncolliding stationary initial law.

## Proof
Write \(S\) for particles in the same graph side and \(D\) for particles in different sides. The ordinary two-particle exclusion generator projected to \((S,D)\) is
\[
Q_{\mathrm{Ex}}=\begin{pmatrix}-2m&2m\\2(m-1)&-2(m-1)\end{pmatrix}.
\]
A \(D\) configuration has two possible collision-making attempted moves, each of rate one, whereas an \(S\) configuration has none. Hence the killed independent-particle generator on these two classes is
\[
Q_{\mathrm{kill}}=\begin{pmatrix}-2m&2m\\2(m-1)&-2m\end{pmatrix}.
\]
Let \(s_m=\sqrt{m(m-1)}\). Direct multiplication gives
\[
Q_{\mathrm{kill}}\begin{pmatrix}\sqrt{m/(m-1)}\\1\end{pmatrix}
=-(2m-2s_m)\begin{pmatrix}\sqrt{m/(m-1)}\\1\end{pmatrix}.
\]
The displayed eigenvector is strictly positive and the finite killed configuration chain is irreducible. Symmetry under automorphisms of the biclique and particle exchange ensures that its Perron ground state takes exactly the displayed values on the two configuration classes. Consequently \(\lambda_m=2m-2s_m\) is its principal killing rate. The ground-state transformed transition rates are the old nonkilling rates multiplied by the ratio of destination and source ground-state values: \(2m\sqrt{(m-1)/m}=2s_m\) and \(2(m-1)\sqrt{m/(m-1)}=2s_m\). This proves the exact symmetric two-state \(\mathrm{NC}\) law.

The symmetric telegraph chain has stationary law \((1/2,1/2)\) and centered autocorrelation \(e^{-2r_m t}\). Because \(\kappa=2I\), its stationary variance is \(1\), establishing the covariance. Integrating twice by stationarity yields \(2\int_0^t(t-u)e^{-2r_m u}\,du=t/r_m-(1-e^{-2r_m t})/(2r_m^2)\), as displayed. For exclusion, two-state detailed balance gives \(\pi_{\mathrm{Ex}}(D)=m/(2m-1)\).

For an arbitrary distinct configuration, the general noncollision/exclusion change of measure for a killed finite chain gives
\[
\frac{d\mathsf P^{\mathrm{NC}}_x}{d\mathsf P^{\mathrm{Ex}}_x}\Big|_{\mathcal F_t}
=\frac{h(X_t)}{h(X_0)}\exp\left(\lambda_m t-\int_0^t\kappa_s\,ds\right).
\]
In each stationary initial regime, the expected logarithm of the endpoint ratio is zero. Taking logarithms and expectations under the numerator process yields respectively \(t(\lambda_m-\mathbb E_{\mathrm{NC}}\kappa)=t(\lambda_m-1)\) and \(t(\mathbb E_{\mathrm{Ex}}\kappa-\lambda_m)=t(2m/(2m-1)-\lambda_m)\). The first is positive because \(\sqrt{m(m-1)}<m-1/2\); the second is positive by \(\sqrt{u^2-1}>u-1/u\) with \(u=2m-1>1\). Elementary expansion \(2m-2\sqrt{m(m-1)}=1+1/(4m)+O(m^{-2})\), together with \(2m/(2m-1)=1+1/(2m)+O(m^{-2})\), proves both rate asymptotics.

## Verification
`verify.py` independently constructs the full labelled configuration-space killed and transformed matrices for \(2\le m\le6\). It checks the positive eigenvector, transformed row sums, invariant weights, and two-state aggregation. It also checks the formulas algebraically and numerically for \(2\le m\le30\). The recorded execution passed 601 checks. The infinite family is proved by the uniform two-class generator calculations above; no finite sampling is treated as an infinite proof.

## Relationship to prior work
Shiatis (2026) proves a general change of measure between noncolliding and exclusion walks; this is used, not reproved as an original principle. Mendonça (2013) determines spectral data for exclusion on complete bipartite graphs, but does not treat the ground-state-conditioned killed walk, the exact stationary half-traffic identity, or the two path-space entropy rates here. Earlier general criteria distinguishing exclusion and noncollision when the collision hazard is not constant establish inequivalence but do not specify the complete conditioned two-class process and its exact quantitative entropy separation. The calculations here supply these graph-specific missing observables.

## Limitations
The identity \(\pi_{\mathrm{NC}}(D)=1/2\) is for balanced bicliques with exactly two particles and unit per-edge jump rates. It need not hold for unequal part sizes, nonuniform rates, or more particles. The result is a finite-graph explicit classification, not an asymptotic theorem for general graphs. Classical spectral diagonalization might implicitly yield equivalent special formulas; exhaustive historical priority and independent mathematical validation are not claimed.

## References
1. Rohan Shiatis, *Exclusion vs Noncolliding dynamics in Markov processes*, arXiv:2610.00741v1, first submitted 30 September 2026, https://arxiv.org/abs/2610.00741.
2. J. Ricardo G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106v4, 2013, https://arxiv.org/abs/1207.4106.
