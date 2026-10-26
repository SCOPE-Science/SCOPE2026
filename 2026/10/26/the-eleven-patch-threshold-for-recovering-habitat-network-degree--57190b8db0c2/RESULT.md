# The eleven-patch threshold for recovering habitat-network degree mixing from two-patch fragments

## Finding

For a tree-shaped habitat network with independent homogeneous survival, the entire mean curve for the number of connected fragments containing **exactly two surviving patches** identifies the edge-degree mixing table whenever all patch degrees are at most three. Degree four is the first permitted maximum degree for which this need not hold, and eleven patches are the smallest tree size where failure can occur.

More precisely, let \(T=(V,E)\) be any finite simple tree with \(n=|V|\ge3\), vertex degree \(d(v)\), and maximum degree \(\Delta\le4\). Write \(n_i\) for the number of vertices of degree \(i\), and let \(m_{ij}\) be the number of unoriented edges whose endpoint degrees are \(i\le j\). For \(s\ge3\), define \(c_s=\sum_{i\le j,\ i+j=s}m_{ij}\). The random variable \(F_2(T,p)\) counts components of size exactly two in the induced subgraph of retained vertices, when each vertex is retained independently with probability \(p\in(0,1)\). Writing \(q=1-p\),

\[
\mathbb E F_2(T,p)=p^2\sum_{uv\in E}q^{d(u)+d(v)-2}=p^2\sum_{s=3}^{2\Delta}c_s q^{s-2}.
\]

The curve determines every \(c_s\) exactly, by uniqueness of polynomial coefficients. If \(\Delta\le3\), the curve and the degree census \((n_i)\) determine **all** edge-type counts \(m_{ij}\). If \(\Delta\le4\), two trees with equal degree censuses and mean curves can differ only by an integer multiple of a single edge-type exchange direction, and a nonzero exchange requires at least eleven vertices. The lower bound is attained by the explicit pair below.

## Assumptions and scope

The network is a finite connected **tree**, with \(n\ge3\), maximum degree at most four, and no isolated patches. Survival states of different patches are independent with identical parameter \(p\). The degree census is treated as known separately. Observations are the exact mathematical expectation curve for all \(p\in(0,1)\), not estimates from finitely many noisy realizations. The conclusion concerns the **joint degree mixing table**, not the full graph up to isomorphism.

## Proof

**1. Derivation of the two-patch observable.** An edge \(uv\) is a surviving component of size exactly two if and only if its endpoints survive and every other neighbor of either endpoint is absent. Because a tree has no triangles, these other neighbor sets are disjoint and have \(d(u)+d(v)-2\) vertices. The event therefore has probability \(p^2q^{d(u)+d(v)-2}\). Every surviving two-vertex component corresponds to exactly one edge. Summing event indicators and expectations proves the displayed formula. The normalized function \(\mathbb E F_2(T,1-q)/(1-q)^2\) is the polynomial \(\sum_s c_s q^{s-2}\), so its coefficients are identifiable exactly.

**2. Complete subcubic inversion.** In a tree on at least three vertices no edge joins two leaves, hence \(m_{11}=0\). At \(\Delta\le3\), the edge-sum counts and degree-incidence identity give

\[
\begin{aligned}
m_{12}&=c_3, &m_{23}&=c_5, &m_{33}&=c_6,\\
m_{22}&=\frac{2n_2-c_3-c_5}{2},
&m_{13}&=c_4-m_{22}.
\end{aligned}
\]

These are every possible edge type. They reconstruct the joint degree matrix, including cases with absent degree classes and \(\Delta\le2\).

**3. All degree-four ambiguities.** Order the possible edge types as

\[
(12),(13),(14),(22),(23),(24),(33),(34),(44).
\]

For two trees with the same \((n_i)\) and \((c_s)\), subtract their edge-type counts. The equal edge-sum counts impose

\[
\delta m_{12}=\delta m_{34}=\delta m_{44}=0,\quad
\delta m_{13}+\delta m_{22}=0,\quad
\delta m_{14}+\delta m_{23}=0,\quad
\delta m_{24}+\delta m_{33}=0.
\]

The fixed vertex census gives the endpoint-incidence constraints

\[
\begin{aligned}
 n_1&=m_{12}+m_{13}+m_{14},\\
 2n_2&=m_{12}+2m_{22}+m_{23}+m_{24},\\
 3n_3&=m_{13}+m_{23}+2m_{33}+m_{34},\\
 4n_4&=m_{14}+m_{24}+m_{34}+2m_{44}.
\end{aligned}
\]

Solving these **homogeneous difference equations** yields precisely

\[
(\delta m_{12},\delta m_{13},\delta m_{14},\delta m_{22},\delta m_{23},\delta m_{24},\delta m_{33},\delta m_{34},\delta m_{44})
=t(0,-1,1,1,-1,-1,1,0,0),\qquad t\in\mathbb Z.
\]

If \(t\ne0\), one of the two trees must contain a \((2,2)\)-edge and one must contain a \((3,3)\)-edge. Consequently \(n_2\ge2\) and \(n_3\ge2\); also \(n_4\ge1\), since the \((1,4)\) and \((2,4)\) counts differ. Every tree with degrees at most four satisfies, by the handshaking identity,

\[
n_1=n_3+2n_4+2.
\]

It follows that \(n_1\ge6\) and

\[
n=n_1+n_2+n_3+n_4\ge6+2+2+1=11.
\]

This is an analytic lower bound over **all** trees in scope, not a bounded enumeration.

**4. Sharp eleven-vertex witnesses.** Use vertex labels \(0,1,\ldots,10\) and the following unordered edge lists; for example \((0,10)\) denotes one edge, not a pair of digits:

```
T_A = [(0,1),(0,7),(0,10),(1,2),(1,6),(2,3),(2,4),(2,5),(7,8),(8,9)]
T_B = [(0,1),(0,7),(1,2),(1,5),(1,6),(2,3),(2,4),(7,8),(7,10),(8,9)]
```

Each list has ten distinct edges and spans a connected eleven-vertex graph, so both are trees. Their common degree census is \((n_1,n_2,n_3,n_4)=(6,2,2,1)\). In the above edge-type order, their tables are respectively

\[
\begin{aligned}
(m_{ij}(T_A))&=(1,2,3,1,1,0,1,1,0),\\
(m_{ij}(T_B))&=(1,3,2,0,2,1,0,1,0).
\end{aligned}
\]

Both give \((c_3,c_4,c_5,c_6,c_7,c_8)=(1,3,4,1,1,0)\), hence the *same entire* mean curve

\[
\mathbb E F_2(T_A,p)=\mathbb E F_2(T_B,p)
=p^2(q+3q^2+4q^3+q^4+q^5),\qquad q=1-p.
\]

Their joint degree matrices differ by the nonzero kernel vector in Step 3, achieving the lower bound. At \(p=1/2\), both means are \(59/128\).

## Verification

Run `python3 verify_fragment.py` using the standard Python library. It recomputes connectedness and degree statistics of both witnesses; enumerates all \(2^{11}=2048\) survival subsets of each tree and tabulates counts for each exact survival quota; compares the resulting **entire symbolic polynomial** (integer coefficients) with the edge-isolation formula; checks exact expected values at five rational probabilities; verifies the one-dimensional edge-type difference; and checks the subcubic reconstruction formulas against all 1,309 labeled subcubic trees on three through six vertices. The reproducible exact outputs are in `verification_certificate.json`. These computations verify finite instances; Steps 1–3 supply the universal proofs.

## Relationship to prior work

The polynomial \(\sum_{uv\in E}q^{d(u)+d(v)}\) is a diagonal specialization of the known \(M\)-polynomial \(M(T;x,y)=\sum_{i\le j}m_{ij}x^iy^j\). Its forward construction and the joint degree matrix are *not new*. Deutsch and Klavžar (2014) analyze the full bivariate \(M\)-polynomial and degree-based indices, whereas the present result asks whether a **single diagonal specialization together with degree counts** suffices to recover the edge-type table. This distinction is essential: the full bivariate polynomial tautologically carries all \(m_{ij}\); its diagonal generally does not.

Vukičević (2009) derives criteria for realizing prescribed edge-degree matrices by trees. Vukičević and Graovac (2004) treat realization with degrees in \(\{1,2,4\}\), and separately study simultaneous discrimination by the Randić, Zagreb and modified Zagreb indices in acyclic molecular graphs. The latter uses a much richer **triple of numerical indices**, not the single diagonal observable considered here; its results therefore do not resolve the eleven-patch failure despite supplying important close background. Czabarka and collaborators (2013) study realizations of a **given** joint degree matrix, rather than recovery from its collapsed degree-sum spectrum. Niebuhr and collaborators (2015) motivate ecological fragmentation and patch survival, without the particular inverse theorem claimed here.

These comparisons do not constitute independent proof of novelty; an unlocated equivalent in specialized chemical-graph or percolation literature remains possible.

## Limitations

The identity in Step 1 relies on the lack of triangles; for a graph with common neighbors across an edge, that exponent must be adjusted. Heterogeneous survival, noisy finite-sample estimation, and stochastic habitat dynamics are not treated. Recovery of \((m_{ij})\) does not recover an entire labeled or unlabeled tree. The eleven-vertex sharp bound concerns equal degree censuses and maximum degree **at most four**; it is not a statement about arbitrarily high degrees. No independent audit of originality or correctness has been performed.

## References

1. D. Vukičević and A. Graovac, “On Molecular Graphs with Valencies 1, 2 and 4 with Prescribed Numbers of Bonds,” *Croatica Chemica Acta* 77 (2004), 313–319; publicly dated 2004-05-31; https://hrcak.srce.hr/102721.
2. D. Vukičević and A. Graovac, “Valence Connectivity versus Randić, Zagreb and Modified Zagreb Index,” *Croatica Chemica Acta* 77 (2004), 501–508; publicly dated 2004-10-25; https://hrcak.srce.hr/102951.
3. D. Vukičević, “On the edge degrees of trees,” *Glasnik Matematički* 44 (2009), 259–266; doi:10.3336/gm.44.2.01.
4. É. Czabarka, A. Dutle, P. Erdős, and I. Miklós, “On Realizations of a Joint Degree Matrix” (2013), arXiv:1302.3548.
5. E. Deutsch and S. Klavžar, “M-Polynomial and Degree-Based Topological Indices” (2014), arXiv:1407.1592.
6. B. Niebuhr and collaborators, “Survival in patchy landscapes: interplay between dispersal, habitat loss and fragmentation,” *Scientific Reports* (2015), doi:10.1038/srep11898.
