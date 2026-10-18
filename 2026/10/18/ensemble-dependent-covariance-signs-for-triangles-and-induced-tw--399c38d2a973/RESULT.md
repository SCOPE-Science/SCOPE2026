# Ensemble-dependent covariance signs for triangles and induced two-paths

## Finding
Let \(n\ge4\). For a simple graph on \(n\) labeled vertices, let \(T\) count three-vertex induced triangles and let \(P\) count three-vertex induced open two-paths (exactly two of the three possible edges present). There is an exact sign reversal between the independent-edge and fixed-edge Erdős–Rényi ensembles.

In \(G(n,p)\), for \(0<p<1\),
\[
\operatorname{Cov}(T,P)=3\binom n3 p^4(1-p)\{2(n-3)-(3n-8)p\}.
\]
In particular, the covariance is positive below the sharp threshold \(p_c(n)=2(n-3)/(3n-8)\), zero at that threshold, and negative above it; \(p_c(n)\to2/3\).

In \(G(n,m)\), with \(N=\binom n2\) possible edges and \(0\le m\le N\), put
\[
B(n,m)=m(n^2-3n-8)+n^3-2n^2-3n+4.
\]
Then
\[
\operatorname{Cov}(T,P)=-\frac{64m(m-1)(m-2)(N-m)(N-m-1)B(n,m)}{(n+1)^2(n+2)(n^2-n-10)(n^2-n-8)(n^2-n-4)^2}.
\]
The fixed-edge covariance is strictly negative **if and only if** \(3\le m\le N-2\), and is zero for all remaining permitted edge counts. Moreover, if \(m/\binom n2\to p\in(0,1)\), then
\[
n^{-3}\operatorname{Cov}_{G(n,m)}(T,P)\longrightarrow-p^4(1-p)^2.
\]
The independent-edge covariance is generically of order \(n^4\) when \(p\) is fixed away from the threshold, whereas the fixed-edge covariance is of order \(n^3\).

## Assumptions and scope
All graphs are simple, undirected, and labeled. The ensemble \(G(n,p)\) includes each possible edge independently with common probability \(p\). The ensemble \(G(n,m)\) chooses uniformly one \(m\)-element subset of its \(N\) possible edges. Counts \(T,P\) count unordered vertex triples, not ordered paths or noninduced subgraphs. Exact formulas include boundary probabilities and edge counts by continuity or direct evaluation; the sign classification concerns \(0<p<1\). The asymptotic statement is along integer sequences \(m=m_n\).

## Proof
Define the noninduced wedge count \(W=\sum_v\binom{d_v}{2}\). Each induced open two-path contributes one wedge and each triangle contributes three, so \(P=W-3T\) identically.

For either ensemble define \(q_j\) as the probability that any prescribed \(j\) distinct edges are present. In \(G(n,p)\), \(q_j=p^j\). In \(G(n,m)\), \(q_j=(m)_j/(N)_j\), interpreted as zero when \(m<j\), with \((x)_j=x(x-1)\cdots(x-j+1)\). Let \(H=\binom n3\) and \(W_0=n\binom{n-1}{2}\) be the numbers of potential triangles and potential wedges.

For a fixed triangle, exactly three potential wedges use two of its edges, exactly \(6(n-3)\) use one, and the remaining \(W_0-3-6(n-3)\) use none. Thus
\[
\operatorname{Cov}(T,W)=H\{(W_0-3-6(n-3))(q_5-q_3q_2)+6(n-3)(q_4-q_3q_2)+3(q_3-q_3q_2)\}.
\]
For a fixed triangle, exactly \(3(n-3)\) distinct potential triangles have one edge in common; one is identical, and the other \(H-1-3(n-3)\) have no edges in common. Therefore
\[
\operatorname{Var}(T)=H\{(H-1-3(n-3))(q_6-q_3^2)+3(n-3)(q_5-q_3^2)+(q_3-q_3^2)\}.
\]
Consequently \(\operatorname{Cov}(T,P)=\operatorname{Cov}(T,W)-3\operatorname{Var}(T)\). Substitution of \(q_j=p^j\) cancels the disjoint contributions and gives the claimed cubic sign factor.

For \(G(n,m)\), substitute the falling-factorial probabilities, put all terms over a common denominator and cancel factors to obtain the stated rational product; the cancellation is an algebraic identity for every integer \(n\ge4\), \(0\le m\le N\), including cases where \(m<6\) by the zero convention. All denominator factors are positive for \(n\ge4\). For \(n\ge5\), both coefficients of \(B(n,m)\) are positive. For \(n=4\), \(B(4,m)=24-4m\), which is positive throughout \(3\le m\le N-2=4\). Hence the strict sign is precisely the claimed range; outside that range at least one numerator falling-factorial factor vanishes. Finally, divide the rational product by \(n^3\) and use \(m\sim pn^2/2\) and \(N-m\sim(1-p)n^2/2\) to obtain \(-p^4(1-p)^2\).

## Verification
Run \(\texttt{python3 verify.py}\) with a standard Python 3 interpreter. The script computes the joint statistics for every labeled simple graph on \(n=4,5,6\), groups them by edge count, and checks both the overlap identity and factored covariance against exact-rational enumeration. It also checks four exact rational values of \(p\) and many additional \((n,m)\) values through \(n=60\). The recorded run passed 775 exact assertions while exhaustively enumerating 33,856 graphs. Exhaustive verification is finite corroboration; the unrestricted statement is proved above using overlap classification and algebraic identities.

## Relationship to prior work
Ginoza and Mugler (arXiv:0907.4680, 2009) study correlated small network motifs under degree-preserving directed edge swaps and provide an explicit motivation for considering joint motif statistics, but their model and comparisons do not state the two ensemble formulas here. Fretter, Müller-Hannemann and Hütt (2012) discuss subgraph fluctuations under edge-density perturbations; available abstract evidence does not determine whether their complete text contains related formulas. Fodor et al. (2020) analyze dependence of motif counts in biological null models and identify deterministic constraints on motif statistics, not the exact present uniform-graph covariance. Goldschmidt, Griffiths and Scott (arXiv:1902.06830, 2019) investigate joint subgraph fluctuations and may imply related asymptotic behavior, but the available literature comparison does not establish coverage of the finite \(G(n,m)\) sign law. The formula is not asserted to be a historically certified first discovery.

## Limitations
The claim is restricted to the two induced three-vertex motifs (triangle and open two-path) in homogeneous labeled simple-graph ensembles. It does not extend without proof to degree-preserving randomization, directed networks, or arbitrary graphons. Some plausible primary texts were not available in full; implicit earlier coverage and historical priority remain unresolved. No independent scientific audit has been performed.

## References
- R. Ginoza and A. Mugler, *Network motifs come in sets: correlations in the randomization process*, arXiv:0907.4680 (first posted 2009-07-27), https://arxiv.org/abs/0907.4680.
- C. Fretter, M. Müller-Hannemann, and M.-T. Hütt, *Subgraph fluctuations in random graphs*, Physical Review E 85 (2012), 056119, https://doi.org/10.1103/PhysRevE.85.056119.
- C. Goldschmidt, S. Griffiths, and A. Scott, *Moderate deviations of subgraph counts in G(n,m) and G(n,p)*, arXiv:1902.06830 (2019), https://arxiv.org/abs/1902.06830.
- J. Fodor, M. Brand, R. J. Stones, and A. Buckle, *Intrinsic limitations in mainstream methods of identifying network motifs in biology*, BMC Bioinformatics 21 (2020), https://doi.org/10.1186/s12859-020-3441-x.
