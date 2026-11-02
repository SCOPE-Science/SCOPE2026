# A binomial obstruction to random greedy matching under a rare tripartite perturbation

## Finding

Let \(G_{n,k}=K_{n,n,k}\) be the complete tripartite graph with two parts of size \(n\) and a third part of size \(k\). Starting with all vertices unmatched, repeatedly select uniformly from the edges with both endpoints unmatched, add that edge to a matching, and remove its endpoints. Let \(U_{n,k}\) be the number of vertices left unmatched at termination. Let \(B_k\) be binomial with parameters \(k\) and \(1/2\).

**Quantitative binomial-obstruction theorem.** For all integers \(k\ge1\) and \(n\ge16k\), set \(M=\lceil\sqrt{kn}\rceil\). Then

\[
d_{\mathrm{TV}}\bigl(\mathcal L(U_{n,k}),\mathcal L(|k-2B_k|)\bigr)
\le \frac{kM}{n}+\frac{k^2}{4(M-k)}.
\]

In particular, for any integer sequence \(k=k(n)\) satisfying \(k=o(n^{1/3})\) as \(n\to\infty\), the distance tends to zero. For each fixed \(k\), the entire unmatched-vertex distribution converges to that of \(|k-2B_k|\). When \(k\to\infty\) with \(k=o(n^{1/3})\),

\[
\frac{U_{n,k}}{\sqrt{k}}\ \Longrightarrow\ |Z|,\qquad Z\sim N(0,1).
\]

For each fixed \(k\), the limiting probability that greedy matching has maximum cardinality equals

\[
p_k=\begin{cases}
2^{-k}\binom{k}{k/2},&k\text{ even},\\
2^{1-k}\binom{k}{(k-1)/2},&k\text{ odd}.
\end{cases}
\]

Thus \(p_1=1\), while \(p_2=1/2\). The limiting expected number unmatched is

\[
\lim_{n\to\infty}\mathbb E U_{n,k}
=\frac{k}{2^{k-1}}\binom{k-1}{\lfloor(k-1)/2\rfloor}.
\]

## Assumptions and scope

The graph is finite, simple, undirected, with all cross-part edges and no within-part edges. Edges are chosen uniformly **from the currently feasible edges**, not by the vertex-first greedy rule. This distribution also equals processing all graph edges in a uniformly random order and accepting an edge only if both endpoints are still unmatched. All probabilities include the matching randomness; there is no random graph input. The finite bound holds for every integer \(n\ge16k\), while the limiting claims have the indicated quantifiers. Total variation is \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\).

## Proof

**1. Exact lumped process.** Denote the parts by \(A,B,C\). Let \(j\) be the number of accepted \(A\)-\(B\) edges, and let \(x,y\) be the numbers of accepted \(A\)-\(C\) and \(B\)-\(C\) edges. At every stage put \(m=n-j\). The unmatched population counts are exactly

\[
a=m-x,\qquad b=m-y,\qquad c=k-x-y,
\qquad x,y\ge0,\quad x+y\le k.
\]

The available edge count is \(Q=ab+c(a+b)\), and the next edge has a uniformly chosen available endpoint pair. At any nonterminal state, the transition probabilities for \(AB,AC,BC\) are respectively \(ab/Q,ac/Q,bc/Q\). In particular \(a,b\in[m-k,m]\) and \(|a-b|\le k\).

**2. A marked rare vertex disappears early.** Every accepted \(AB\) edge decreases \(m\) by one; an accepted edge incident to \(C\) leaves \(m\) unchanged. Call the collection of states with a given \(m\) a *level*. For \(m\ge4k\) both dense parts are nonempty, so each level is left after a finite number of rare-part matches and exactly one \(AB\) match. Fix a particular vertex \(v\) of \(C\). If it is unmatched at the start of level \(m\), the probability that the first selected edge of that level meets \(v\) is

\[
\frac{a+b}{ab+c(a+b)}
\ge \frac{2(m-k)}{m^2+2km}
\ge \frac1m,
\]

where the final inequality is exactly \(m\ge4k\). Therefore, by conditioning successively on survival to the starts of levels \(n,n-1,\ldots,M+1\),

\[
\Pr(v\text{ is still unmatched at level }M)
\le\prod_{m=M+1}^{n}(1-1/m)=\frac Mn.
\]

The first-edge test deliberately ignores possible later removal of \(v\) at the same level; this only strengthens the bound. A union bound over the \(k\) original rare vertices gives

\[
\Pr(E^c)\le\frac{kM}{n},
\]

where \(E\) is the event that every vertex of \(C\) is already matched before the process reaches level \(M\).

**3. Each rare edge has an approximately fair dense endpoint.** Conditional on selecting an edge incident to \(C\), the probability that its other endpoint lies in \(A\), given the entire past, is exactly \(a/(a+b)\). As long as \(m>M\),

\[
\left|\frac{a}{a+b}-\frac12\right|
=\frac{|a-b|}{2(a+b)}
\le\frac{k}{4(M-k)}.
\]

Expose an independent uniform variable whenever a rare-part edge is chosen, using that uniform variable both to make the actual \(A/B\) endpoint choice and to produce a reference fair coin. By maximal coupling, each of the at most \(k\) rare-edge endpoint choices made above level \(M\) differs from its reference fair coin with conditional probability at most \(k/[4(M-k)]\). Complete the reference sequence with fresh independent fair coins if fewer than \(k\) rare matches occur above level \(M\). The resulting reference bits are independent Bernoulli\((1/2)\). Hence the probability of at least one disagreement above level \(M\) is at most \(k^2/[4(M-k)]\).

**4. The terminal invariant.** On \(E\), all \(k\) rare vertices have been matched. If \(X\) of them were matched to part \(A\), the two remaining dense parts differ by exactly \(k-2X\) vertices, because every \(AB\) match deletes one vertex from each part. Thereafter only edges between \(A\) and \(B\) remain; matching must terminate with precisely \(|k-2X|\) vertices unmatched. Thus, on the event \(E\) and the event of no coupled endpoint disagreement, the terminal count equals \(|k-2B_k|\), where the reference sum is \(B_k\). The coupling inequality proves the stated total-variation bound.

**5. Bounds, limits and optimality.** Since \(n\ge16k\), the chosen \(M\) is at least \(4k\); the error is \(O(k^{3/2}/\sqrt n+k/n)\), so it vanishes for \(k=o(n^{1/3})\). For every execution, maximality means that all terminal unmatched vertices belong to a single part. If that is \(C\), the count is at most \(k\). Otherwise \(C\) is empty, and the dense-part difference is at most \(k\). Consequently \(0\le U_{n,k}\le k\). This boundedness permits convergence of the mean for fixed \(k\). Using the elementary telescoping identity \( (k-2j)\binom{k}{j}=k[\binom{k-1}{j}-\binom{k-1}{j-1}] \), together with symmetry around the center of the binomial distribution, gives

\[
\mathbb E|k-2B_k|=
\frac{k}{2^{k-1}}\binom{k-1}{\lfloor(k-1)/2\rfloor}.
\]

For \(n\ge k\), there exists a matching leaving exactly \(k\bmod 2\) vertices: pair the \(k\) rare vertices as evenly as possible to \(A\) and \(B\), then match the remaining dense vertices across the bipartite core. Therefore greedy is maximum exactly when \(U_{n,k}=k\bmod2\). The central binomial probabilities give \(p_k\). Finally, the classical binomial central limit theorem, together with the total-variation bound, gives the stated folded-normal limit when \(k\to\infty\).

## Verification

The standalone `checker.py` uses exact rational dynamic programming with the three edge-type transition weights \(ab,ac,bc\), plus independent exhaustive enumeration of random edge permutations on four small labeled graphs. It checks terminal probabilities, parity, the binomial absolute-deviation identity, and the quantitative total-variation bound at specified finite inputs. The tested program reports 165 passing assertions. Finite enumeration does **not** prove the infinite asymptotic claim; that conclusion follows from the coupling above.

## Relationship to prior work

Random greedy maximal matching is the edge version of random greedy maximal independent set on a line graph, as discussed by Krivelevich, Mészáros, Michaeli and Shikhelman. Arnosti studies the random-edge greedy matching algorithm and comparisons against other algorithms on random bipartite graphs, including an asymptotic appendix for sparse inputs. The present result addresses a different observable and geometry: the *entire terminal defect distribution* of the dense, deterministic, nonbipartite tripartite family with a small third class. Earlier work on minimum and maximum cardinalities of maximal matchings in complete multipartite graphs determines deterministic size extrema, not this random-edge selection law. No equivalent specific theorem was located in the inspected sources; this does not establish universal historical priority.

## Limitations

The explicit coupling rate is sufficient but is not asserted to be optimal. The argument does not cover a third class comparable to the two dense classes or asymmetric dense-part sizes, and it does not give a limiting law beyond \(k=o(n^{1/3})\). The 2014 multipartite edge-domination article and the 1991 general randomized greedy matching paper were not accessible in complete text during this comparison; the possibility of unlocated stronger coverage remains. No independent mathematical validation has been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first public version 2019-07-16); https://arxiv.org/abs/1907.07216.
2. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, *Stochastic Systems* 12 (2022), 133–150; author-posted complete preprint, April 2021; https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf; https://doi.org/10.1287/stsy.2021.0082.
3. M. Dyer and A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* 2 (1991), 29–45; https://doi.org/10.1002/rsa.3240020104.
4. W. Song, L. Miao, H. Wang, Y. Zhao, *Maximal matching and edge domination in complete multipartite graphs*, *International Journal of Computer Mathematics* 91 (2014), 857–862; https://doi.org/10.1080/00207160.2013.818668.
