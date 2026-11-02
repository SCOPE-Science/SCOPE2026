# A sharp two-contact intervention reversal on epidemic paths

## Finding

Consider a path \(P_n\) with edges \(1,\ldots,n-1\). An outbreak starts at a uniformly chosen vertex and independently transmits across each edge that is open. All edges open with probability \(p\), except precisely two designated edges which instead open with probability \(q\), where \(0<q<p\le1\). The eventual infected set is the open component of the initial vertex. Choose the two designated edges to minimize the mean final infection count.

**Sharp minimum-size result.** On \(P_6\), all global minimizers are exactly

\[
\begin{cases}
\{(2,4)\},&0<q<p/(1+p),\\
\{(2,4),(2,3),(3,4)\},&q=p/(1+p),\\
\{(2,3),(3,4)\},&p/(1+p)<q<p.
\end{cases}
\]

Here \((i,j)\) denotes the weakened edges, not infected vertices. This is the first path size exhibiting a switch from **separated** to **adjacent** optimal interventions: the unique optima on \(P_3\), \(P_4\) and \(P_5\) are, respectively, \((1,2)\); \((1,2),(2,3)\); and \((2,3)\), with every optimal pair adjacent. The exact difference is

\[
\mathbb E X_{6;2,4}-\mathbb E X_{6;2,3}
=\frac{(p-q)((1+p)q-p)}3.
\]

**Arbitrary-size structural extension.** For every fixed integer \(n\ge6\) and each fixed \(0<p\le1\), there are positive \(\epsilon_0,\epsilon_1\) such that every minimizing pair is nonadjacent when \(0<q<\epsilon_0\), while every minimizing pair is adjacent when \(p-\epsilon_1<q<p\). No universal single-crossover assertion is made for \(n>6\).

## Assumptions and scope

All edge-open trials are independent. The initial infected vertex is uniform among \(n\) sites, independent of those trials. Transmission follows the independent-cascade (bond-percolation) mechanism and only the first infected connected component is counted, including its seed. The two attenuations have the same efficacy, and exactly two distinct edges must be attenuated. All comparisons are for \(n\ge3\), \(0<q<p\le1\), with the sharp switch proved for \(n=6\). The model does not assert equivalence to an arbitrary continuous-time SIR process with random shared infectious periods.

Index path vertices \(1,\ldots,n\) and edges \(i=1,\ldots,n-1\), with edge \(i\) joining vertices \(i,i+1\). Write \(X_{n;i,j}\) for the final infected size when edges \(i<j\) have probability \(q\) and the others probability \(p\). For \(m\ge1\), let \(A_m(p)=\sum_{k=0}^{m-1}p^k\). Let \(K_n(p)=n+2\sum_{d=1}^{n-1}(n-d)p^d\).

## Proof

**1. Mean component-size identity.** For a particular bond configuration with components of sizes \(s_1,\ldots,s_t\), averaging over the uniform seed gives \(\mathbb E[X\mid\text{bonds}]=n^{-1}\sum_k s_k^2\). Equivalently, if \(w_t\) is the open probability of edge \(t\),

\[
n\mathbb E X=n+2\sum_{1\le a<b\le n}\prod_{t=a}^{b-1}w_t.
\tag{1}
\]

Indeed the \(a,b\) vertices lie in one component exactly when every intervening edge is open. Since there is one path between them, independence gives the product. This establishes (1) for all \(n\).

**2. Exact two-edge attenuation formula.** Put \(r=p-q\). Expanding each interval-path product in (1) in its two possible weakened-edge factors \((p-r)\) gives, for \(1\le i<j\le n-1\),

\[
 n\mathbb E X_{n;i,j} = K_n(p)
 -2r\bigl[D_i(p)+D_j(p)\bigr]
 +2r^2 A_i(p)p^{j-i-1}A_{n-j}(p),
 \quad D_i(p)=A_i(p)A_{n-i}(p).
\tag{2}
\]

For example, the coefficient of \(-2r\) from paths using edge \(i\) is \(\sum_{a\le i<b}p^{b-a-1}=A_i A_{n-i}\). Paths using both edges give precisely the positive \(r^2\) term. Thus (2) is exact, with no asymptotic truncation.

**3. Classification for \(n\le6\).** Let \(F_{i,j}=n\mathbb E X_{n;i,j}\), and compare to the proposed base pair. For \(n=3\), there is one choice. For \(n=4\), relative to \((1,2)\), pair \((2,3)\) ties and \((1,3)\) has excess \(2q(p-q)>0\). For \(n=5\), relative to \((2,3)\), the exact positive excesses for the remaining pairs, grouped by reflection symmetry, are

\[
\begin{array}{c|c}
\text{Pairs}&F_{i,j}-F_{2,3}\\ \hline
(1,2),(3,4)&2p(p-q)(1+q)\\
(1,3),(2,4)&2q(p-q)(1+p)\\
(1,4)&2(p-q)(2pq+p+q).
\end{array}
\tag{3}
\]

For \(n=6\), relative to the separated pair \((2,4)\), the complete ten-pair comparison (again grouped by reflection) is

\[
\begin{array}{c|c}
\text{Pairs}&F_{i,j}-F_{2,4}\\ \hline
(2,4)&0\\
(2,3),(3,4)&-2(p-q)((1+p)q-p)\\
(1,2),(4,5)&2(p-q)(p^2q+p^2+2p-q)\\
(1,3),(3,5)&2p(p-q)(1+pq)\\
(1,4),(2,5)&2p(p-q)(1+q+pq)\\
(1,5)&2p(p-q)(2+q+p+2pq).
\end{array}
\tag{4}
\]

Every entry in (4) except the first two classes is strictly positive under \(0<q<p\le1\). In particular \(p^2q+p^2+2p-q>0\) because \(2p-q>p>0\). Thus the only candidates are \((2,4)\) and the reflected adjacent pairs, and the sign of \((1+p)q-p\) gives precisely the three regimes in the finding. Dividing their difference in (4) by six yields the displayed expectation difference.

**4. Weak-link limit on every longer path.** At \(q=0\), two disabled edges divide the path into three nonempty blocks of lengths \(a,b,c\), with \(a+b+c=n\). Formula (1) becomes \(n\mathbb E X=g_p(a)+g_p(b)+g_p(c)\), where

\[
g_p(m)=m+2\sum_{d=1}^{m-1}(m-d)p^d,
\quad g_p(m+2)-2g_p(m+1)+g_p(m)=2p^{m+1}>0.
\tag{5}
\]

The strict discrete-convexity exchange \((a,c)\mapsto(a+1,c-1)\) when \(c-a\ge2\) strictly decreases the objective. Therefore *exactly* the minimizing three-block partitions have sizes differing by at most one. For \(n\ge6\), each such block has length at least two. Thus both disabled edges are nonadjacent. Since the finite set of placements has a positive objective gap between these minimizers and every adjacent pair at \(q=0\), continuity of (1) gives \(\epsilon_0>0\) for which every minimizer remains nonadjacent when \(0<q<\epsilon_0\).

**5. Weak-attenuation limit on every longer path.** For \(0<p<1\), the central-edge sensitivities in (2) satisfy

\[
D_{i+1}(p)-D_i(p)=\frac{p^i-p^{n-i-1}}{1-p};
\]

at \(p=1\) the continuous limit is \(n-2i-1\). Therefore \(D_i\) increases strictly toward the central edge(s), is symmetric about the center, and the only pairs maximizing \(D_i+D_j\) are the two central-adjacent choices (two reflected pairs for even \(n\), one for odd \(n\)). In (2), their advantage in the linear \(-2r(D_i+D_j)\) term is strictly positive compared with every noncentral pair. The quadratic terms are bounded over the finite placement set, so for all sufficiently small \(r=p-q>0\), *every* minimizing pair is central-adjacent, proving the \(\epsilon_1\) assertion. This is not a claim that every optimal arrangement at every intermediate \(q\) has been classified for arbitrary \(n\).

## Verification

Run `python3 verify.py` from this directory. The standalone standard-library checker verifies the coefficientwise polynomial identities (2)–(4) for all relevant placements; independently reconstructs mean infections by enumerating every bond state and seed for rational probability samples including the exact tie curve; and checks (2) symbolically for all pairs on \(3\le n\le12\). Its current replay reports 794 passing exact symbolic and rational assertions. This finite computation checks the algebra and boundary examples but is **not** the proof of the unbounded-\(n\), continuum-parameter statements; steps 1–5 provide that proof.

For illustration, with \(p=3/4\), the separated pair wins at \(q=1/4\) because its expected size is \(7091/3072\) versus \(2417/1024\) for either adjacent central pair. At \(q=1/2\), the adjacent choice wins: \(2267/768\) versus \(2275/768\). At \(q=3/7\), the two classes tie.

## Relationship to prior work

Newman (public preprint April 30, 2002) develops epidemic spreading through percolation on networks, including transmissibility. Kenah and Robins (public preprint October 30, 2006) clarify that independent bond occupation is not generally equivalent to SIR dynamics with shared random infectious periods; our model assumes independent bonds explicitly. Yi, Shan, Paré and Johansson (public preprint November 22, 2020) study edge deletion algorithms for expected SIR spread and independent-cascade models, but their inspected algorithmic bounds and graph interventions do not state the present two-partial-edge exact path phase diagram. Demange and colleagues (public preprint March 18, 2021) formulate probabilistic firebreak placement via edge *removal*, including tree algorithms; their complete-edge interventions do not supply the \(q>0\) exact threshold classification. Russo and colleagues (public preprint September 2015) study firebreak placement via structural/network heuristics rather than the present all-pairs analytical optimum. Youssef and Scoglio (2013) optimize time-varying weighted contacts in a continuous-time epidemic system by optimal control, which is a different objective and does not yield the static exact \(P_6\) bond intervention threshold. Prakash and colleagues (2013) treat fractional *node* immunization and infection-rate reduction, but its full text was inaccessible; comparison with its public abstract leaves a limited historical-priority risk. None of those inspected formulations directly proves the sharp \(P_6\) switch or the all-size two-limit theorem; this is an inspected-evidence statement, not a proof of historical uniqueness.

## Limitations

The result is exact only for a homogeneous undirected path, independent edge trials, uniform single-seed location, and precisely two equally attenuated links. It does not optimize costs or location-specific seeds, account for directional contacts or correlated edge risks, predict real epidemic incidence, or classify all intermediate attenuation levels for \(n>6\). Some earlier literature on probabilistic network interdiction or series-system reliability may give equivalent extremal results in other notation. No independent validation or definitive historical-priority assessment has been performed.

## References

1. M. E. J. Newman, *The spread of epidemic disease on networks*, first public arXiv submission 2002-04-30, https://arxiv.org/abs/cond-mat/0205009.
2. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first public arXiv submission 2006-10-30, https://arxiv.org/abs/q-bio/0610057.
3. Y. Yi, L. Shan, P. E. Paré and K. H. Johansson, *Edge Deletion Algorithms for Minimizing Spread in SIR Epidemic Models*, first public arXiv submission 2020-11-22, https://arxiv.org/abs/2011.11087.
4. M. Demange, A. Di Fonso, G. Di Stefano and P. Vittorini, *A graph theoretical approach to the firebreak locating problem*, first public arXiv submission 2021-03-18, https://arxiv.org/abs/2103.10115.
5. F. Russo and colleagues, *A complex network theory approach for the spatial distribution of fire breaks in heterogeneous forest landscapes for the control of wildland fires*, preprint first publicly posted 2015-09-14, https://arxiv.org/abs/1509.04065.

6. M. Youssef and C. Scoglio, *Mitigation of epidemics in contact networks through optimal contact adaptation*, Mathematical Biosciences and Engineering 10 (2013), 1227–1251, freely accessible full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3857636/.
7. B. A. Prakash, L. Adamic, T. Iwashyna, H. Tong and C. Faloutsos, *Fractional Immunization in Networks*, SDM (2013), 659–667, DOI https://doi.org/10.1137/1.9781611972832.73; public abstract inspected; full text unavailable.
