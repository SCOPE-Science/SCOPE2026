# A three-quarters rare-jamming constant for dimers on cocktail-party graphs

## Finding

Let \(G_n=K_{2n}\setminus M_n\), where \(M_n\) is a perfect matching, so \(G_n\) is the complete \(n\)-partite graph with all parts of size two (the cocktail-party graph). Process its edges in a uniformly random permutation, accepting an edge exactly when neither endpoint has previously been covered by an accepted edge. Let \(P_n\) be the probability of imperfect final vertex coverage. Then, for every integer \(n\ge2\), the final number of uncovered vertices is either zero or two, and

\[
P_n=\frac{3}{4n}+O(n^{-6/5})\qquad(n\to\infty).
\]

In particular \(\lim_{n\to\infty}nP_n=3/4\), while the expected fraction of uncovered vertices is \(P_n/n\sim3/(4n^2)\). The exact probabilities satisfy the rational finite-state recurrence below; initial examples are \(P_2=0\), \(P_3=1/5\), \(P_4=8/65\), and \(P_5=1231/11375\). The event of failure means that the only two remaining vertices are one of the deleted pairs.

## Assumptions and scope

Every allowed edge has an independent identical continuous priority (or equivalently an independent rate-one exponential deposition clock); priorities are considered in increasing order and accepted edges cannot share endpoints. This is **uniform random-order edge-dimer adsorption**, not an algorithm selecting a random vertex followed by a random neighbor. The graph has labeled vertices arranged into \(n\) specified forbidden pairs; all other unordered vertex pairs are allowed. The theorem holds for all \(n\ge2\). No assumptions about a thermodynamic spatial embedding or lattice distance are made.

## Proof

**1. Exact Markov state.** Among the currently uncovered vertices, let \(p\) be the number of intact forbidden pairs and \(s\) the number of singleton vertices whose forbidden partners have already been covered. There are \(m=2p+s\) uncovered vertices and \(\binom m2-p\) eligible edges. Conditional on a new accepted edge, the state transitions with the following multiplicities:

\[
\begin{array}{c|c|c}
\text{edge endpoints}&\text{multiplicity}&\text{new state}\\
\text{two singletons}&\binom s2&(p,s-2)\\
\text{one intact-pair vertex and one singleton}&2ps&(p-1,s)\\
\text{vertices from two different intact pairs}&2p(p-1)&(p-2,s+2).
\end{array}
\]

The multiplicities sum to \(\binom m2-p\). With \(F(p,s)\) the probability of ending with exactly one forbidden pair uncovered, this gives, for \(m\ge4\),

\[
F(p,s)=\frac{\binom s2F(p,s-2)+2psF(p-1,s)+2p(p-1)F(p-2,s+2)}{\binom{2p+s}{2}-p},
\]

omitting any term with zero multiplier. Boundary states are \(F(1,0)=1\), \(F(0,2)=0\), and \(F(0,0)=0\); \(P_n=F(n,0)\). A nonterminal uncovered set with at least four vertices always contains an allowed edge (every forbidden part contains at most two vertices), so the only possible jammed remnant is an intact pair.

**2. One intact pair at an intermediate scale.** Stop the chain when \(2k\) uncovered vertices remain, for any integers \(n>k\ge2\), and let \(Q_k\) be the number of intact forbidden pairs among them. Track one originally forbidden pair. If it is intact while \(m\) vertices remain, with \(q\) intact pairs in total, the probability it survives the next dimer is

\[
1-\frac{2(m-2)}{\binom m2-q}.
\]

Since \(1\le q\le m/2\), for every even \(m\ge6\) this conditional probability lies between \((m-4)/m\) and \((m-3)/(m+1)\). Multiplying over \(m=2n,2n-2,\ldots,2k+2\) telescopes. By exchangeability of the original \(n\) forbidden pairs,

\[
\frac{k(k-1)}{n-1}\ \le\ \mathbb E Q_k\ \le\ \frac{n(4k^2-1)}{4n^2-1}.
\tag{1}
\]

Both bounds are \((k^2/n)(1+O(1/k+1/n))\) when \(k\to\infty\), \(k=o(n)\).

**3. Two intact pairs are negligible.** For two specified forbidden pairs still intact when \(m\ge6\) vertices remain, precisely \(4m-12\) allowed edges touch at least one of their four vertices. Thus their conditional survival probability to the next step is at most

\[
1-\frac{4m-12}{\binom m2}
=1-\frac8m+\frac{16}{m(m-1)}.
\]

Using \(1-x\le e^{-x}\) and summing over even sizes gives

\[
\Pr(\text{both specified pairs survive to }2k)
\le e^{8/k}\left(\frac{k+1}{n+1}\right)^4.
\]

Indeed the sum of the \(8/m\) terms is \(4(H_n-H_k)\ge4\log((n+1)/(k+1))\), and the sum of the correction terms is at most \(8/k\). Consequently

\[
\mathbb E[Q_k(Q_k-1)]
\le n(n-1)e^{8/k}\left(\frac{k+1}{n+1}\right)^4
=O(k^4/n^2).
\tag{2}
\]

**4. Exact survival from a single rare pair.** If \(Q_k=1\), the remaining \(2k-2\) vertices are singletons, and the unique intact forbidden pair survives a step with \(m\) uncovered vertices exactly when the selected edge avoids its two endpoints. This happens with probability \((m-3)/(m+1)\). The product down to two vertices telescopes to

\[
t_k=\prod_{j=2}^{k}\frac{2j-3}{2j+1}
=\frac3{(2k-1)(2k+1)}=\frac3{4k^2-1}.
\]

If \(Q_k=0\), failure is impossible because intact forbidden pairs can never be created. If \(Q_k\ge2\), bound its conditional failure probability by one. In particular, writing \(V_k=\mathbb E[Q_k(Q_k-1)]\),

\[
t_k(\mathbb E Q_k-V_k)\le P_n\le t_k\mathbb E Q_k+V_k/2.
\tag{3}
\]

The left inequality follows from \(\Pr(Q_k=1)\ge\mathbb E Q_k-V_k\); the right uses \(\Pr(Q_k\ge2)\le V_k/2\). Substitute (1) and (2), and take \(k=\lfloor n^{1/5}\rfloor\) for sufficiently large \(n\). The main contribution is \(3/(4n)\), the relative error from (1) is \(O(1/k+1/n)\), and the absolute error from (2) is \(O(k^4/n^2)\). Hence \(P_n=3/(4n)+O(n^{-6/5})\), as claimed.

## Verification

Run `python verify.py` from the directory containing the accompanying script. It compares the \((p,s)\) recurrence with an independently implemented labeled-vertex-subset recurrence for every \(1\le n\le7\), using exact rational arithmetic. It also verifies the finite intermediate moment bounds for \(5\le n\le18\) and performs a floating-point recurrence study through \(n=1000\), for which \(nP_n\) approaches \(0.745026425\). The numerical observation supports but **does not prove** the limiting constant; the proof above establishes it for every asymptotically large \(n\).

## Relationship to prior work

Random-order dimer deposition is the edge form of the random sequential adsorption studied by Pippenger (1989), while Dyer and Frieze (1991) analyze uniform-edge randomized greedy matching on general graphs. Their reported principal results address graph families such as high-girth regular graphs and forests; those results do not imply a first-order failure probability for the dense complete multipartite family with parts of size two. Gamarnik and Goldberg (arXiv:0807.1277, 2008), in particular Theorem 5 and Corollary 5, establish average matching-size bounds in **fixed-degree, high-girth** regimes, not the present degree-growing, triangle-rich, near-perfect-coverage event. Related exact results for bipartite crown graphs use a different graph and do not determine the cocktail-party constant. The same cocktail-party graph occurs in other combinatorial invariants, but their numerical values do not determine a random greedy matching probability.

## Limitations

The adsorption order must be uniformly random among eligible edges; a random-vertex-first matching algorithm is different. Only the binary probability of imperfect coverage and its exact finite-state recurrence are analyzed, not the full random deposition time distribution. The error exponent \(6/5\) is a proved bound, not asserted optimal. Some older source full texts were inaccessible; bibliographic uniqueness is not an independent certification and an unlocated equivalent result remains possible.

## References

1. N. Pippenger, "Random Sequential Adsorption on Graphs," *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: `10.1137/0402034`.
2. M. E. Dyer and A. M. Frieze, "Randomized Greedy Matching," *Random Structures & Algorithms* **2** (1991), 29–45. DOI: `10.1002/rsa.3240020104`.
3. D. Gamarnik and D. A. Goldberg, "Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections," arXiv:`0807.1277` (first posted 2008-07-08), *Combinatorics, Probability and Computing* **19** (2010), 61–81.
4. J. W. Evans, "Random and cooperative sequential adsorption," *Reviews of Modern Physics* **65** (1993), 1281–1329. DOI: `10.1103/RevModPhys.65.1281`.
