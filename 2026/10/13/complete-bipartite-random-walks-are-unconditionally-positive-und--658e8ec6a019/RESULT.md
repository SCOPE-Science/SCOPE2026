# Complete bipartite random walks are unconditionally positive under fourth-order diagonal Padé stepping
## Finding
Let \(K_{p,q}\) be the complete bipartite graph with integers \(p,q\ge1\), let \(n=p+q\), and let \(L\) be the unit-edge combinatorial Laplacian. For the fourth-order diagonal Padé, equivalently two-stage Gauss--Legendre, end-step
\[
\Phi_h=\bigl(I-\tfrac h2L+\tfrac{h^2}{12}L^2\bigr)\bigl(I+\tfrac h2L+\tfrac{h^2}{12}L^2\bigr)^{-1},
\]
\(\Phi_h\) is row-stochastic and entrywise nonnegative for every \(h\ge0\), and it is entrywise strictly positive for every \(h>0\).

This graph-structured unconditional preservation is already sharp at four vertices. For the unit-edge path \(P_4\), the same map is entrywise nonnegative exactly for
\[
0\le h\le h_*,
\]
where \(h_*\) is the unique positive root of
\[
h^4-6h^3-60h^2-108h-72=0,
\]
so \(h_*=11.8663785439\ldots\). At \(h=12\), the endpoint-neighbor entry is exactly \(-60/84973\). Since the only connected simple bipartite graphs with at most three vertices are complete bipartite graphs, four vertices are minimal for failure of all-step positivity in that graph class.

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and use unit edge rates. The continuous-time random walk is written in column-generator form as \(u'(t)=-Lu(t)\); because \(L\mathbf 1=0\) and \(L=L^{\mathsf T}\), the same matrix is also stochastic in the row convention. The claim concerns the one-step end map only. It does not assert positivity of internal Runge--Kutta stages, nonlinear positivity, weighted-graph analogues, or corresponding statements for other Padé orders.

## Proof
Put
\[
\varphi(x)=\frac{x^2-6x+12}{x^2+6x+12}\qquad(x\ge0).
\]
The scalar denominator is positive for \(x\ge0\), the numerator has negative discriminant and is positive, and \(0<\varphi(x)\le1\). Therefore \(\Phi_h=\varphi(hL)\) is defined for every \(h\ge0\). Also \(\Phi_h\mathbf 1=\mathbf 1\), so entrywise nonnegativity is enough for stochasticity.

For \(K_{p,q}\), the Laplacian spectrum consists of \(0\), \(q\) on the sum-zero subspace of the \(p\)-vertex part, \(p\) on the sum-zero subspace of the \(q\)-vertex part, and \(n=p+q\) on the one-dimensional contrast subspace. Write
\[
a=\varphi(qh),\qquad b=\varphi(ph),\qquad c=\varphi(nh).
\]
The spectral projectors give the following entries. Cross-part entries are
\[
\frac{1-c}{n}=\frac{12h}{n^2h^2+6nh+12},
\]
which are positive for \(h>0\). Distinct vertices in the \(p\)-part have entry
\[
\frac{p+qc-na}{pn},
\]
and direct simplification yields
\[
p+qc-na=
\frac{12h^2pqn\,(hp+2hq+6)}{(h^2q^2+6hq+12)(h^2n^2+6hn+12)}>0
\]
for \(h>0\). Distinct vertices in the \(q\)-part similarly have entry \((q+pc-nb)/(qn)\), with
\[
q+pc-nb=
\frac{12h^2pqn\,(2hp+hq+6)}{(h^2p^2+6hp+12)(h^2n^2+6hn+12)}>0.
\]
Each diagonal entry is its same-part off-diagonal value plus \(a\) or \(b\), respectively, so every diagonal is also positive. At \(h=0\), \(\Phi_0=I\). This proves unconditional nonnegativity, and strict positivity for \(h>0\), on every complete bipartite graph.

For \(P_4\), exact inversion gives a common positive denominator
\[
\Delta(h)=2(h^2+3h+3)(h^4+12h^3+54h^2+72h+36).
\]
The endpoint-neighbor entry is
\[
(\Phi_h)_{12}=
\frac{-3h\,(h^4-6h^3-60h^2-108h-72)}{\Delta(h)}.
\]
Every other inequivalent entry has a numerator that is manifestly nonnegative for \(h\ge0\):
\[
9h^2(h^3+6h^2+16h+12),\quad
3h^3(5h^2+18h+12),
\]
\[
3h(h^4+6h^3+24h^2+72h+72),
\]
and the two diagonal numerator polynomials have only positive coefficients. The quartic
\[
g(h)=h^4-6h^3-60h^2-108h-72
\]
has exactly one positive root by Descartes' rule of signs; since \(g(0)<0\) and \(g(h)\to\infty\), this root is \(h_*\). Hence \(P_4\) is positivity preserving exactly for \(0\le h\le h_*\). Substituting \(h=12\) gives
\[
\Phi_{12}=
\frac1{84973}
\begin{pmatrix}
45505&-60&16776&22752\\
-60&62341&5916&16776\\
16776&5916&62341&-60\\
22752&16776&-60&45505
\end{pmatrix},
\]
which is still row-stochastic but is not entrywise nonnegative.

Finally, every connected simple bipartite graph on two vertices is \(K_{1,1}\), and on three vertices is \(K_{1,2}\). Both lie in the unconditional family above, while \(P_4\) fails. Thus four vertices are minimal.

## Verification
The accompanying `artifacts/verify_pade_bipartite.py` uses exact rational arithmetic. It reconstructs the \(P_4\) Padé step at \(h=12\), checks the displayed matrix and row sums exactly, verifies the endpoint-neighbor numerator formula at several exact rational steps, and checks the complete-bipartite projector formulas against direct matrix inversion for a finite exact test suite. These finite checks support the algebra; the universal statements are proved by the factorizations above rather than by enumeration.

## Relationship to prior work
Higueras develops Runge--Kutta monotonicity through absolute monotonicity and shows how method-wide monotonicity restrictions arise from the Runge--Kutta representation. Zappavigna, Colaneri, Kirkland, and Shorten study diagonal Padé discretization of positive linear systems and prove that higher-order diagonal Padé maps need not preserve positivity, even for arbitrarily small steps. Their sufficient positivity theorem is expressed through the support relation between a Metzler matrix and its square; for an irreducible sparse graph generator its stated positive-step sufficient bound can collapse to zero. Their paper does not contain `bipartite`, `Laplacian`, or `complete bipartite` in the inspected full text.

A published database finding, “Eight-state barrier for Markov positivity of the [2/2] Padé map,” sharpens the general negative result for conservative CTMC generators: it proves that eight states are minimal for arbitrarily-small failure and gives an exact window for an eight-state pure-birth chain. That result concerns directed nonsymmetric generators and local small-step failure. It neither implies unconditional positivity on the symmetric complete-bipartite family nor the exact large-step \(P_4\) threshold here.

A separate prior result for Crank--Nicolson on \(K_{p,q}\) gives a finite graph-dependent positivity threshold for the \([1/1]\) Padé map. The present \([2/2]\) theorem is not a corollary: its scalar rational function, spectral values, and sign factorizations differ, and the conclusion is qualitatively stronger on \(K_{p,q}\) while failing on \(P_4\).

## Limitations
The graph family has unit edge weights. Arbitrary positive edge weights can destroy the unconditional statement even on three vertices, so no weighted-graph extension is claimed. The theorem concerns the exact rational map in exact arithmetic, not floating-point sign preservation. It also does not classify every unweighted graph on four or more vertices, every complete multipartite graph, or higher diagonal Padé orders.

## References
1. I. Higueras, “Representations of Runge--Kutta Methods and Strong Stability Preserving Methods,” *SIAM Journal on Numerical Analysis* 43 (2005), 924--948, DOI `10.1137/S0036142903427068`.
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, “Essentially Negative News About Positive Systems,” *Linear Algebra and its Applications* 436 (2012), 3425--3442, DOI `10.1016/j.laa.2011.12.021`.
3. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” public database record `2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab`.
