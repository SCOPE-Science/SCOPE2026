# The antipodal threshold for rooted colour refinement on even-cycle powers

## Finding

Let \(r\ge2\) and \(d\ge1\) be integers, and let \(G=C_{2r}^{\square d}\) be the Cartesian power of the simple undirected cycle on \(2r\) vertices. Initially give the origin \(o=(0,\ldots,0)\) one singleton colour and every other vertex a second common colour. Run **synchronous one-dimensional counting colour refinement**: at each round retain the old colour and append the multiset of neighbours' old colours, including multiplicities. Let \(\mathcal P_k\) be its partition after exactly \(k\) rounds, starting at \(k=0\).

For a vertex \(x=(x_1,\ldots,x_d)\), put \(\delta_i(x)=\min(x_i,2r-x_i)\in\{0,\ldots,r\}\), and let \(m_j(x)=|\{i:\delta_i(x)=j\}|\) for \(0\le j\le r\). Write \(m(x)=(m_0,\ldots,m_r)\), and \(\ell(x)=\sum_{j=0}^r j m_j(x)=\operatorname{dist}(o,x)\). The diameter from \(o\) is \(D=rd\).

**Complete round-by-round theorem for \(r\ge3\).** For every integer \(0\le k\le D-1\), vertices \(x,y\) have the same colour after round \(k\) precisely when either both have \(\ell>k\), or they have exactly the same distance histogram \(m(x)=m(y)\) with \(\ell\le k\). In particular, the least stable round is exactly \(D-1\). The stable partition is the orbit partition of the automorphisms fixing \(o\); its \(\binom{d+r}{r}\) classes have cardinalities
\[
|\mathcal O_m|=\frac{d!}{m_0!\cdots m_r!}\,2^{m_1+\cdots+m_{r-1}},\qquad m_0+\cdots+m_r=d.
\]
Let \(p_{d,r}(j)\) be the coefficient of \(q^j\) in the Gaussian polynomial
\[
\begin{bmatrix}d+r\\d\end{bmatrix}_q=\prod_{i=1}^d\frac{1-q^{r+i}}{1-q^i}.
\]
The number of colours after round \(k\), for \(0\le k<D\), is exactly
\[
1+\sum_{j=0}^{k}p_{d,r}(j).
\]

**Exceptional four-cycle boundary.** When \(r=2\), the graph \(C_4^{\square d}\) is the hypercube \(Q_{2d}\). At round \(k\), \(0\le k\le2d-1\), its colour classes are the fibres of the **truncated total distance** \(\min\{\ell(x),k+1\}\), rather than the finer coordinate histograms. Its least stable round remains \(2d-1\), but there are only \(2d+1\) final classes. For \(d\ge2\), this is strictly less than \(\binom{d+2}{2}\). Thus the exceptional multiplicity-two antipode in \(C_4\) causes a genuine loss of coordinate-profile information, while antipodal multiplicity does **not** cause that loss for any longer even cycle.

## Assumptions and scope

All graphs are finite, simple and undirected. Cycle lengths \(2r\) are at least four; \(C_2\) is not included as a simple cycle. Cartesian adjacency means that two tuples differ in exactly one coordinate, by one cyclic step in that coordinate. A refinement round uses all neighbour multiplicities, with the old colour retained; ``stabilized'' means the colour partition no longer splits on the next round. The claim concerns the partition **within the marked graph**, not identification of the graph among all nonisomorphic graphs. The general mathematical statements do not depend on finite experiments.

## Proof

**1. Homogeneity of the unseen region.** The underlying product is vertex-transitive and \(2d\)-regular. If \(\ell(x)>k\), then no initial marker lies in the graph-distance-\(k\) neighbourhood of \(x\). Induction on the colour-refinement rounds therefore shows that all such vertices have the same round-\(k\) colour. At round zero, the assertion is immediate. An automorphism obtained by independently reflecting each coordinate around zero and permuting the \(d\) coordinates shows that every histogram fibre is monochromatic at every round.

**2. The weighted predecessor multiset.** For \(r\ge3\), fix a histogram \(m=(m_0,\ldots,m_r)\) whose total distance \(s=\sum j m_j\) is positive. Neighbours one step closer to \(o\) arise by replacing a coordinate distance \(j\ge1\) by \(j-1\). There are \(w_jm_j\) such neighbours with resulting histogram \(m-e_j+e_{j-1}\), where \(w_j=1\) for \(1\le j<r\) and \(w_r=2\). Denote this weighted multiset of predecessor histograms by \(P(m)\); it has cardinality \(N=\sum_{j=1}^r w_jm_j\). We prove that, **for fixed \(s,d,r\)**, the map \(m\mapsto P(m)\) is injective.

For \(1\le j\le r\), sum the coordinate count at distance \(j\) over this predecessor multiset, with multiplicity, obtaining \(B_j\). Directly from the coordinate changes,
\[
B_r=(N-2)m_r,\qquad
B_j=(N-1)m_j+w_{j+1}m_{j+1}\quad(1\le j<r).
\]
If \(N\ge3\), these identities recover \(m_r\) first and then \(m_{r-1},\ldots,m_1\) backwards; \(m_0=d-\sum_{j=1}^r m_j\) follows. If \(N=1\), there is a single positive coordinate distance \(s<r\), and \(m\) is determined by \(s,d\). If \(N=2\), either (i) exactly one coordinate has distance \(r\), or (ii) exactly two coordinates have positive distances strictly below \(r\). In case (ii), the displayed triangular formulas with \(m_r=0\) recover all histogram entries. If cases (i) and (ii) had the same fixed \(s\), it would be \(s=r\). Case (i) has only one predecessor histogram, consisting of a single positive coordinate at distance \(r-1\), with multiplicity two. In case (ii), because \(r\ge3\), at least one positive coordinate has distance at least two; decreasing it leaves **two** positive coordinates. Hence its predecessor multiset contains a different histogram, distinguishing the cases. This proves injectivity for every \(N\).

**3. Induction through the distance shells.** We prove the roundwise partition statement by induction on \(k\). At round zero only the origin is singled out. Suppose the individual histogram fibres of distances below \(k\) are already separate at round \(k-1\), and all vertices at distances at least \(k\) have one common colour. For a vertex at distance \(k\), every neighbour at distance \(k-1\) has a known distinct colour for its histogram; the multiset of these colours is exactly \(P(m)\). By Step 2, different histograms on the new shell produce different round-\(k\) colours. They also split from the farther vertices, which have no neighbour in a distance-\(k-1\) colour. Existing classes remain separate because old colours are retained. By Step 1, all vertices farther than \(k\) remain together. This establishes the exact stated partition at every round through \(D-1\).

**4. Sharpness, orbits and enumerators.** The final shell at distance \(D\) has exactly one histogram, consisting of \(d\) coordinates at distance \(r\). Thus at round \(D-1\), every histogram has its own colour and the partition is stable: each histogram fibre is an orbit under coordinate permutations and reflections. At round \(D-2\), the nonempty shells at distances \(D-1\) and \(D\) remain in the common unseen class, so stabilization cannot have occurred earlier. (The shells exist since \(D\ge3\).) The orbit-size formula follows by choosing positions of each distance and then choosing one of the two signs for every distance strictly between zero and \(r\). The distance enumerator of histograms is the generating polynomial of partitions fitting in a \(d\)-by-\(r\) rectangle, namely the Gaussian polynomial displayed above. Counting the histograms already reached plus the unseen class gives the roundwise colour-count formula.

**5. The exceptional \(C_4\) case.** As graphs, \(C_4=K_2\square K_2\), so \(C_4^{\square d}=Q_{2d}\). The hypercube is distance-regular relative to the origin: a vertex at distance \(j\) has exactly \(j\) neighbours in shell \(j-1\) and \(2d-j\) in shell \(j+1\). Inductively the refinement colours are exactly the truncated total distances. The unique outermost shell enters at round \(2d-1\), proving the asserted least stable round and \(2d+1\) classes. For \(d\ge2\), the strict inequality \(2d+1<\binom{d+2}{2}\) holds because their difference is \(d(d-1)/2\).

## Verification

A standalone standard-library Python program `verify_even_cycles.py` independently implements both (a) full-graph synchronous refinement from the actual adjacency lists and (b) an aggregated weighted-histogram quotient. It compares every computed round to the asserted partition. A separate direct enumeration tests injectivity of the predecessor multiset over finite parameters. The recorded output in `verification_output.txt` states 21 full-graph parameter configurations, 43 weighted-quotient configurations, and 58 predecessor-injectivity configurations passed. Run `python verify_even_cycles.py` from the directory containing this file. These checks cover finite parameters only and are not the proof of the unrestricted theorem.

## Relationship to prior work

General colour refinement, its orbit/automorphism relationship, and its iteration-depth significance are standard foundations (Grohe–Kersting–Mladenov–Selman; Arvind–Köbler–Rattan–Verbitsky; Kiefer–McKay). Prior special-family analyses include marked square toroidal grids, odd-cycle Cartesian powers and hypercubes. The present theorem contributes **the precise all-round profile for arbitrary Cartesian powers of even cycles of length at least six and the unique four-cycle exception**. It does not claim as new the generic refinement algorithm, the hypercube's distance-regularity, the classical Gaussian polynomial, the general Cartesian-product construction, or the existing stable orbit description of two-dimensional marked tori. Compared with the odd-cycle proof, the double predecessor at an even-cycle antipode requires a new injection argument and exposes a genuine boundary failure at length four. Full equivalence coverage by other specialized publications remains a residual literature risk.

## Limitations

The graph is required to have *equal-length* even-cycle factors. The theorem does not characterize mixed Cartesian products of distinct cycle lengths, multiple marked vertices, directed variants, higher-dimensional Weisfeiler–Leman refinement, or identification among arbitrary graphs. The cited primary papers are broad in scope and do not exclude equivalent results in unindexed specialized literature.

## References

1. M. Grohe, K. Kersting, M. Mladenov, E. Selman, *Dimension Reduction via Colour Refinement*, arXiv:1307.5697 (first version 22 July 2013), https://arxiv.org/abs/1307.5697.
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first version 4 February 2015), https://arxiv.org/abs/1502.01255.
3. S. Kiefer, B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182 (20 May 2020), https://arxiv.org/abs/2005.10182.
