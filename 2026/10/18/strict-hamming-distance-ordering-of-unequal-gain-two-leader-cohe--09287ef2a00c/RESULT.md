# Strict Hamming-distance ordering of unequal-gain two-leader coherence on Boolean cubes

## Finding
For every integer \(d\ge2\), let \(Q_d\) be the unit-edge Boolean hypercube on \(N=2^d\) vertices, with combinatorial Laplacian \(L\). Fix **any two positive, not necessarily equal, leader feedback gains** \(a,b>0\). For distinct vertices \(u,v\), define the positive-definite grounded consensus matrix
\[
 M_{u,v}=L+a e_u e_u^{\mathsf T}+b e_v e_v^{\mathsf T},
 \qquad \mathcal T_{a,b}(u,v)=\operatorname{tr}(M_{u,v}^{-1}).
\]
Then the coherence \(\mathcal T_{a,b}(u,v)\) depends only on the Hamming distance \(k=\operatorname{dist}_{Q_d}(u,v)\), and is **strictly decreasing** at every consecutive distance:
\[
 \mathcal T_{a,b}(1)>\mathcal T_{a,b}(2)>\cdots>\mathcal T_{a,b}(d).
\]
Consequently every optimal ordered two-leader placement consists of an antipodal pair, for all unequal or equal positive gains; there are exactly \(N\) optimal ordered assignments of the specified gains to vertices (or \(N/2\) unordered pairs if the gains are equal). The complete ranking, not only the optimal pair, is independent of the gain ratio and gain scale.

The exact value at distance \(k\) is
\[
 \boxed{\mathcal T_{a,b}(k)=2N g_d+
 \frac{N(1-ab B_{d,k}^{2})-2ab C_{d,k}}
 {a+b+2ab B_{d,k}}},
\]
where
\[
 g_d=\frac1{2N}\sum_{j=1}^{d}\frac{\binom dj}{j},
\quad B_{d,k}=\frac1N\sum_{j=1}^{d}\frac1j
 \sum_{\substack{0\le r\le k\\r\ \mathrm{odd}}}
 \binom kr\binom{d-k}{j-r},
\quad C_{d,k}=\frac1{2N}\sum_{j=1}^{d}\frac1{j^2}
 \sum_{\substack{0\le r\le k\\r\ \mathrm{odd}}}
 \binom kr\binom{d-k}{j-r}.
\]
By convention \(\binom{m}{s}=0\) outside \(0\le s\le m\).

A sharp, scale-independent *near-antipodal placement penalty* also follows. Fix any \(\alpha,\beta>0\) and set \(a=\varepsilon\alpha\), \(b=\varepsilon\beta\). Then
\[
 \boxed{\lim_{\varepsilon\downarrow0}
 [\mathcal T_{\varepsilon\alpha,\varepsilon\beta}(d-1)
 -\mathcal T_{\varepsilon\alpha,\varepsilon\beta}(d)]
 =\frac{2\alpha\beta}{d(\alpha+\beta)^2}}.
\]
The exact underlying differences are
\[
 B_{d,d}-B_{d,d-1}=\frac1{Nd},\qquad
 C_{d,d}-C_{d,d-1}=\frac{H_d}{2Nd},
 \qquad H_d=\sum_{j=1}^d\frac1j.
\]
These quantify the loss incurred by locating two unequal-strength leaders one Hamming step short of maximal separation.

## Assumptions and scope
The graph is the *unweighted* undirected hypercube, with one unit conductance on each graph edge; there are no other pinning terms or edge constraints. Both leader gains are finite and strictly positive; they may differ arbitrarily. Distinct leaders are required. The noise-corrupted continuous-time consensus model \(dx=-M_{u,v}x\,dt+\sigma\,dW\), with spatially independent equal-intensity white noises, has total stationary variance \(\sigma^2\mathcal T_{a,b}(k)/2\). Thus minimizing \(\mathcal T\) exactly minimizes physical network coherence. No assertion concerns heteroscedastic forcing, directed networks, anisotropically weighted cubes, three or more leaders, or a general connected graph.

## Proof
**1. Two-pin trace identity.** Let \(G=L^+\) and \(H=(L^+)^2\), and write \(g_d=G_{u,u}\), \(B=G_{u,u}-G_{u,v}\), \(C=H_{u,u}-H_{u,v}\). Vertex transitivity makes the diagonal values independent of the vertex, and \(u\leftrightarrow v\) is an automorphism. Put \(s=a+b\) and \(p=ab\). For \(z>0\), the resolvent \(R_z=(L+zI)^{-1}\) has entries
\[
 (R_z)_{u,u}=\frac1{Nz}+g_d-zH_{u,u}+O(z^2),\qquad
 (R_z)_{u,v}=\frac1{Nz}+(g_d-B)-z(H_{u,u}-C)+O(z^2).
\]
The two-column determinant lemma gives
\[
 \det(M_{u,v}+zI)=\det(L+zI)
 \big[(1+a(R_z)_{u,u})(1+b(R_z)_{v,v})-ab(R_z)_{u,v}^2\big].
\]
Since \(\det(L+zI)=z\,D[1+z\operatorname{tr}G+O(z^2)]\) for a positive constant \(D\), differentiating its logarithm at \(z=0\) yields
\[
 \operatorname{tr}(M_{u,v}^{-1})
 =2Ng_d+\frac{N(1-pB^2)-2pC}{s+2pB}.
\]
Every denominator is positive. The Walsh characters indexed by subsets of \(\{1,\ldots,d\}\) diagonalize \(L\), with eigenvalue twice the subset size. Summing the odd-overlap characters proves the finite binomial formulas for \(g_d,B_{d,k},C_{d,k}\) in the Finding.

**2. Both spectral distances increase with Hamming distance.** The continuous-time heat kernel between vertices at Hamming distance \(k\) is
\[
 p_t(k)=2^{-d}(1+e^{-2t})^{d-k}(1-e^{-2t})^k.
\]
For every \(t>0\), \(p_t(k+1)<p_t(k)\). Since \(G=\int_0^\infty(e^{-tL}-\mathbf1\mathbf1^{\mathsf T}/N)\,dt\) and \(H=\int_0^\infty t(e^{-tL}-\mathbf1\mathbf1^{\mathsf T}/N)\,dt\),
\[
 B_{d,k}=\int_0^\infty[p_t(0)-p_t(k)]\,dt,\qquad
 C_{d,k}=\int_0^\infty t[p_t(0)-p_t(k)]\,dt.
\]
It follows, with strict inequalities, that \(B_{d,k+1}>B_{d,k}>0\) and \(C_{d,k+1}>C_{d,k}>0\) for \(1\le k<d\).

**3. A maximum-principle bound.** Let \(w=G(e_u-e_v)\). Then \(Lw=e_u-e_v\). Translation by the bitwise difference \(u\oplus v\) interchanges \(u,v\), so \(w_u=B\), \(w_v=-B\). At all remaining vertices, \(w\) is discrete harmonic. The maximum principle on the connected hypercube gives \(|w_x|\le B\) for all \(x\), strictly inside at each other vertex. Hence
\[
 2C=\|G(e_u-e_v)\|_2^2=\sum_x w_x^2<NB^2
 \qquad(d\ge2).
\]
This inequality is an all-dimensional analytic consequence, not a finite computation.

**4. Strict ordering for arbitrary gains.** At fixed \(C\), the partial derivative of the trace expression in step 1 with respect to \(B\) is
\[
 -\frac{2p\{N(1+sB+pB^2)-2pC\}}{(s+2pB)^2}.
\]
Beginning at \((B_{d,k},C_{d,k})\), this derivative is strictly negative for every larger \(B\), by \(2C_{d,k}<N B_{d,k}^2\le NB^2\). At fixed \(B\), the partial derivative with respect to \(C\) is \(-2p/(s+2pB)<0\). Increasing first \(B_{d,k}\) to \(B_{d,k+1}\) while fixing \(C_{d,k}\), then increasing \(C\) to \(C_{d,k+1}\), strictly decreases the trace. This proves every adjacent inequality for all \(a,b>0\).

**5. Exact last-bit gap and weak-gain limit.** Subtract consecutive heat kernels at \(k=d-1\):
\[
 p_t(d-1)-p_t(d)=2^{1-d}e^{-2t}(1-e^{-2t})^{d-1}.
\]
Integrating, with \(x=e^{-2t}\), gives \(B_{d,d}-B_{d,d-1}=1/(Nd)\) and \(C_{d,d}-C_{d,d-1}=H_d/(2Nd)\), using the beta-integral logarithmic moment. Substitution of \(a=\varepsilon\alpha,b=\varepsilon\beta\) into step 1 and expansion at \(\varepsilon=0^+\) gives
\[
 \mathcal T_{\varepsilon\alpha,\varepsilon\beta}(k)
 =\frac{N}{\varepsilon(\alpha+\beta)}+2Ng_d
 -\frac{2N\alpha\beta}{(\alpha+\beta)^2}B_{d,k}+O(\varepsilon).
\]
Taking the difference for \(k=d-1,d\) proves the stated finite, sharp limit; no assumption that the full divergent trace has a finite zero-gain limit is made.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The standalone program uses exact rational arithmetic, checks \(d=2,\ldots,11\) spectral formulas and positivity/ordering inequalities for four distinct gain pairs, verifies the antipodal gap and logarithmic-moment identities, and independently constructs and inverts exact grounded Laplacian matrices for \(d=2,3,4\). Expected terminal record: `VERIFY_OK 481 exact rational formula, monotonicity, endpoint and direct-matrix tests`. These finite tests corroborate the analytical proof for all integers \(d\ge2\); they do not replace it.

## Relationship to prior work
Fitch and Leonard (2014 arXiv preprint, later published in 2016) derive general joint-centrality formulas for two **equal-gain** noise-corrupted leaders, and explicitly explain maximal-resistance pair selection on graphs with equivalent information centralities. In particular, the equal-gain antipodal optimum alone is not claimed here as new. The contribution assessed here is the **complete strict ordering of all Hamming separation classes for every pair of arbitrarily unequal gains**, proved through the cube heat kernel and a grounded-potential maximum principle, together with the exact unequal-gain near-antipodal weak-feedback penalty. Their inspected manuscript does not state this all-unequal-gain graded result. Lin, Fardad and Jovanović (2013 arXiv preprint) treat general leader-selection optimization and relaxations rather than the present explicit cube ordering. Patterson, McGlohon and Dyagilev (2014 arXiv preprint) analyze weighted one-dimensional paths and rings. Patterson, Yi and Zhang (2017) develop effective-resistance analysis and solve special classes including cycles and trees; their inspected results do not give the present Boolean-hypercube statement.

## Limitations
Novelty is assessed relative to material inspected and indexed mathematical records; an equivalent deduction in specialized or unindexed literature remains possible. No theorem on nonlinear dynamics, directed graphs, heterogeneous noise, arbitrary edge weights, or arbitrary numbers of pins is established. The finite verification runs cover only limited sizes and gain pairs; the all-dimensions and all-gains quantifiers follow from the preceding analytic argument. For \(d=1\) there is only one distinct-vertex distance and no nontrivial ordering, so the theorem starts at \(d=2\).

## References
- K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public preprint 2014-07-07; IEEE Transactions on Control of Network Systems 3 (2016), 366–378. https://arxiv.org/abs/1407.1569
- F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, 2013-02-03. https://arxiv.org/abs/1302.0450
- S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, 2014-12-20. https://arxiv.org/abs/1412.6595
- S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, 2017-08-23. https://arxiv.org/abs/1708.06873
