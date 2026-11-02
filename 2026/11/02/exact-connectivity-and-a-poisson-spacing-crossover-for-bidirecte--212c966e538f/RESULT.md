# Exact connectivity and a Poisson-spacing crossover for bidirected cycle percolation

## Finding
For each integer \(n\ge3\), independently retain each of the \(2n\) oppositely directed arcs of the bidirected cycle \(C_n\) with probability \(p\in[0,1]\). Let \(\mathcal C_v\) be the strongly connected component (SCC) of vertex \(v\), let \(K_n\) be the SCC count, and write the ranked SCC sizes as \(L_{n,1}\ge L_{n,2}\ge\cdots\), padded by zeros.

The model has the **exact finite-size identities**, for every \(j\in\{0,\ldots,n-1\}\),
\[
\Pr(0\rightleftarrows j)=\left(p^j+p^{n-j}-p^n\right)^2,
\qquad
\mathbb E|\mathcal C_0|=\sum_{j=0}^{n-1}\left(p^j+p^{n-j}-p^n\right)^2,
\]
and
\[
\Pr(K_n=1)=2p^n-p^{2n}+n(1-p)^2p^{2n-2}.
\]

The complete **near-perfect-window ranked-component law** is as follows. Suppose \(p=p_n\) and \(n(1-p_n)\to\lambda\in[0,\infty)\). Let \(B_+\) and \(B_-\) be independent Poisson random variables with mean \(\lambda\). If \(B_+=0\) or \(B_-=0\), set \(\boldsymbol P_\lambda=(1,0,\ldots)\). Otherwise, conditionally on \(B_++B_-=k\ge2\), let \(\boldsymbol P_\lambda\) be the decreasing rearrangement of a \(\operatorname{Dirichlet}(1,\ldots,1)\) vector of length \(k\), padded with zeros. Then
\[
\left(\frac{L_{n,1}}n,\frac{L_{n,2}}n,\ldots\right)
\ \Rightarrow\ \boldsymbol P_\lambda
\qquad\text{in }\ell^1.
\]
In particular, for \(\lambda>0\),
\[
\Pr(K_\infty=1)=2e^{-\lambda}-e^{-2\lambda},\qquad
\Pr(K_\infty=k)=e^{-2\lambda}\frac{(2\lambda)^k-2\lambda^k}{k!}\quad(k\ge2),
\]
where \(K_\infty\) denotes the number of nonzero entries of \(\boldsymbol P_\lambda\), and
\[
\lim_{n\to\infty}\frac{\mathbb E|\mathcal C_0|}{n}
=2e^{-\lambda}+e^{-2\lambda}
+\frac{1-4e^{-\lambda}+3e^{-2\lambda}}{\lambda}.
\]
The continuous extension of this last expression at \(\lambda=0\) equals one.

Finally, if \(p_n\to1\) while \(n(1-p_n)\to\infty\), put \(r_n=1-p_n^2\) and \(a_n=-\log(p_n^2)\). Then
\[
 a_n L_{n,1}-\log(nr_n)\ \Rightarrow\ G,
 \qquad \Pr(G\le x)=\exp(-e^{-x})\quad (x\in\mathbb R).
\]
If instead \(n(1-p_n)\to0\), the full vertex set is strongly connected with probability tending to one. Together, these give a complete crossover from one macroscopic SCC, through a mixed Poisson/Dirichlet ranked partition, to a Gumbel extreme of microscopic components.

## Assumptions and scope
Edges of \(C_n\) join consecutive residues modulo \(n\). The clockwise arc along edge \(i\) and its reverse counterclockwise arc are two distinct, independent Bernoulli variables, each of parameter \(p_n\). SCC means mutual **directed** reachability, not undirected adjacency; zero-size padding makes ranked component vectors elements of \(\ell^1\). The cycle has \(n\ge3\) vertices and no extra chords, loops, or long-range arcs. All limits are along integers \(n\to\infty\). The Gumbel regime requires both \(p_n\to1\) and \(n(1-p_n)\to\infty\). The exact identities also hold at the endpoints \(p=0\) and \(p=1\).

## Proof
**1. Deterministic reduction.** Every simple directed cycle in a directed subgraph of \(C_n\) is either a two-arc backtrack across a single bidirectional edge or a Hamiltonian tour in one of the two orientations. Indeed, after entering a new vertex, avoiding an immediate return forces continued travel in the same cyclic direction until the tour is completed. Every edge in a finite strongly connected digraph belongs to a directed cycle when it lies on some closed directed walk, and every edge used in a simple directed path joining two vertices of the same SCC lies on a closed directed walk. Consequently, in the absence of a complete clockwise or counterclockwise Hamiltonian tour, every SCC is exactly a connected component of the undirected subgraph comprising edges whose **both** arcs are present. If a complete tour survives, every vertex is in one SCC.

**2. Finite laws.** For vertices \(0\) and \(j\), a clockwise path and a counterclockwise path are the only possible simple directed routes from \(0\) to \(j\), using respectively \(j\) and \(n-j\) arcs, and their arc sets are disjoint. Inclusion–exclusion gives \(\Pr(0\leadsto j)=p^j+p^{n-j}-p^n\). The routes from \(j\) back to \(0\) use precisely the *other* orientation of every underlying edge, so the forward and backward reachability events are independent. Squaring proves the first identity, and summation over \(j\) proves the expectation identity.

Write \(A\) and \(B\) for survival of every clockwise and every counterclockwise arc respectively. Their union has probability \(2p^n-p^{2n}\). If neither occurs, the deterministic reduction permits exactly one SCC only if the bidirectional undirected graph is connected; on a cycle this requires at most one edge without both arcs. If there is exactly one such edge and neither full oriented tour survives, both arcs on that edge must be absent, while all other edges must have both arcs. These \(n\) disjoint events have total probability \(n(1-p)^2p^{2n-2}\), proving the claimed complete-connectivity formula.

**3. Critical Poisson window.** Mark each edge with its missing clockwise and counterclockwise arcs. In the regime \(n(1-p_n)\to\lambda\), each marked orientation converges to an independent homogeneous rate-\(\lambda\) Poisson point process on the unit circle: this follows from independent Bernoulli counts on disjoint arcs. The probability that any underlying edge loses both arcs is at most \(n(1-p_n)^2\to0\). Thus distinct limiting marks are almost surely at distinct circle positions. If either orientation has zero marks, its complete Hamiltonian tour survives, giving the single-block outcome. Otherwise each marked edge cuts the connected bidirectional subgraph; its component sizes are precisely the cyclic spacings between the \(k\) marked positions, expressed in vertex units. Conditional on \(k\), these positions are iid uniform on the circle. Choose one of the \(k\) positions uniformly as the cyclic origin: the successive gaps have \(\operatorname{Dirichlet}(1,\ldots,1)\) law. This choice does not change their decreasing rearrangement. Since the Poisson mark count is tight, collisions vanish, and the normalized spacings converge jointly, the ranked component vector converges in \(\ell^1\). Independence of the two Poisson counts immediately yields the displayed \(K_\infty\) probabilities.

For the mean component fraction, divide the finite exact mean formula by \(n\) and take a bounded Riemann-sum limit:
\[
\int_0^1\left(e^{-\lambda t}+e^{-\lambda(1-t)}-e^{-\lambda}\right)^2\,dt
=2e^{-\lambda}+e^{-2\lambda}+\frac{1-4e^{-\lambda}+3e^{-2\lambda}}{\lambda}.
\]
At \(\lambda=0\), the integrand is one.

**4. Diverging-cuts Gumbel regime.** Denote by \(D_i\) the indicator that edge \(i\) is not bidirectional. These indicators are independent Bernoulli variables with mean \(r_n=1-p_n^2\), and \(a_n=-\log(1-r_n)\). With \(x\in\mathbb R\) fixed, set
\[
 k_n=\left\lfloor\frac{\log(nr_n)+x}{a_n}\right\rfloor,
 \qquad I_i=D_i\prod_{h=1}^{k_n}(1-D_{i+h}),
\]
where indices are cyclic. Because \(nr_n\to\infty\) and \(r_n\to0\), we have \(k_n/n\to0\) and \(n\mathbb EI_i=nr_n(1-r_n)^{k_n}\to e^{-x}\). An \(I_i\) records a deficient edge followed by a run of at least \(k_n\) fully bidirectional edges. Two such events whose starting indices are within cyclic distance at most \(k_n\) are mutually exclusive; whenever all pairwise cyclic distances exceed \(k_n\), their underlying Bernoulli variables are disjoint and the events independent. For each fixed factorial order \(m\), the number of allowed distinct ordered \(m\)-tuples is \(n^m(1+O_m(k_n/n))\). Hence for \(Z_n=\sum I_i\),
\[
\mathbb E(Z_n)_m=\left(nr_n(1-r_n)^{k_n}\right)^m(1+O_m(k_n/n))\to e^{-mx},
\]
so \(Z_n\Rightarrow\operatorname{Poisson}(e^{-x})\) by the factorial-moment criterion. The event of no deficient edge has probability \((1-r_n)^n\to0\), and the probability that at least one complete oriented Hamiltonian cycle survives is at most \(2p_n^n\to0\). Outside these vanishing events, the maximum SCC size is the longest bidirectional run of edges plus one. Therefore \(\Pr(L_{n,1}\le k_n)\to e^{-e^{-x}}\) with a possible one-vertex shift, which vanishes under multiplication by \(a_n\to0\). This establishes the stated Gumbel limit.

**5. Supercritical near-perfect regime.** If \(n(1-p_n)\to0\), a union bound shows that all \(2n\) arcs are present with probability tending to one, whence the entire cycle is one SCC.

## Verification
The accompanying standalone `verify.py` reconstructs all strongly connected components by transitive-closure reachability and independently compares them against the bidirectional-cut reduction for **every** one of the \(64+256+1024+4096=5440\) possible arc configurations for \(n=3,4,5,6\). It also computes exact rational probabilities under \(p=1/3\) and \(p=3/5\) for \(n=3,4,5\), confirming the complete-connectivity, pairwise-connectivity, and expected-size identities. The executed program passed 5,482 exact assertions. Four continuous-window parameter instances were numerically checked for consistent probability bounds; these are not certificates for general infinite-limit claims. The critical-window and Gumbel limits are proved analytically above.

## Relationship to prior work
Liu, Rolla and Shi introduce and investigate independently retained bidirected arcs, concentrating on existence, uniqueness, and thresholds for **infinite** strongly connected clusters on transitive graphs. Their Lemma 1.2 also uses the fully bidirectional subgraph as a general lower bound, but does not supply the exact finite-cycle SCC reduction, finite probabilities, ranked component-limit law or Gumbel crossover here. Newman and Grassberger investigate strongly connected percolation on planar directed lattices. Van der Hofstad and Pandey establish general local-to-global criteria for giant strong components of random digraphs, rather than this finite-circle partition formula. Existing undirected one-dimensional run and spacing facts are essential, classical ingredients; the nontrivial directed effect is the surviving single-orientation Hamiltonian tour, which produces an additional macroscopic atom in the Poisson window. This comparison is a best-knowledge literature assessment, not a certificate of historical priority.

## Limitations
The theorem applies only to a simple cycle with independent equally likely arcs in both directions. The Gumbel statement additionally assumes the explicit near-perfect and diverging-cut regime; it says nothing about fixed \(p<1\), non-independent arcs, random long-range edges, or general graph sequences. The Poisson–Dirichlet phrase here refers to a **Poisson mixture of ranked finite-dimensional Dirichlet spacings**, not the classical infinite-dimensional Poisson–Dirichlet distribution. General results about runs in Bernoulli sequences and circle spacings may imply pieces of the result, and unlocated earlier work specifically on directed rings remains a historical-priority risk. No independent review has been performed.

## References
1. Yucheng Liu, Leonardo T. Rolla and Yuliang Shi, *Percolation on Bidirected Graphs*, arXiv:2610.28762v1 (first public 2026-10-20), https://arxiv.org/html/2610.28762v1 .
2. Newman and Grassberger, *Strongly-connected percolation on directed lattices*, arXiv:2607.24975v1, https://arxiv.org/html/2607.24975v1 .
3. Remco van der Hofstad and Manish Pandey, *Are giants in random digraphs 'almost' local?*, arXiv:2403.02137v1, https://arxiv.org/html/2403.02137v1 .
4. Femke van Ieperen and Ivan Kryven, *Percolation of a strongly connected component in simple directed random graphs with a given degree distribution*, arXiv:2012.06415v1, https://arxiv.org/abs/2012.06415 .
5. Christina Goldschmidt and Robin Stephenson, *The scaling limit of a critical random directed graph*, arXiv:1905.05397v1, https://arxiv.org/abs/1905.05397 .
