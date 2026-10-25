# A sharp tree interval for the occupancy–isolation covariance switch

## Finding

For a finite simple tree \(T\) with \(n\ge 2\) vertices, independently retain each vertex with probability \(p\in(0,1)\). Let \(S_T\) be the total number of retained vertices and \(I_T\) the number of retained vertices without any retained neighbor (singleton components in the retained induced graph). Then there is a **unique** \(\alpha_T\in(0,1)\) at which \(\operatorname{Cov}(S_T,I_T)=0\), with positive covariance below and negative covariance above it. For \(n=2\), \(\alpha_T=1/2\); for every \(n\ge3\),
\[
\frac13<\alpha_T<\frac12.
\]
Both universal constants are sharp as asymptotic bounds across trees: for paths \(P_n\), \(\alpha_{P_n}\to 1/3\), while for stars \(K_{1,n-1}\), \(\alpha_{K_{1,n-1}}\to 1/2\) as \(n\to\infty\). Equivalently, the expected number of singleton habitat components has a unique peak in the stated interval. This phenomenon does **not** extend to all connected graphs: a clique on fifteen vertices with a pendant two-edge path has at least three distinct stationary points for the expected singleton count.

## Assumptions and scope

All graphs are finite, unweighted, simple and undirected. Tree vertices are retained independently with the same probability \(p\). The random variable \(I_T\) counts retained degree-zero vertices *in the retained induced subgraph*, not vertices that were originally isolated. There are no initial isolated vertices for a tree of order at least two. The result concerns the exact first-moment curve and its covariance with \(S_T\), not the variance of \(I_T\). No assumption is made about the embedding or edge lengths.

## Proof

Write \(q=1-p\), and let \(n_d\) be the number of vertices of degree \(d\) in \(T\). By independence,
\[
F_T(p):=\mathbb E[I_T]=p\sum_{d\ge1}n_dq^d,
\qquad
F_T'(p)=\sum_{d\ge1}n_dq^{d-1}(1-(d+1)p).
\]
For any finite statistic \(H\) of independent Bernoulli-retained vertices, differentiation of its finite probability sum gives
\[
\frac{d}{dp}\mathbb E[H]=\frac{\operatorname{Cov}(S_T,H)}{pq}.
\]
Therefore \(\operatorname{Cov}(S_T,I_T)=pqF_T'(p)\), and covariance zeros and signs are precisely the zeros and signs of \(F_T'\).

For every tree of order \(n\ge2\), the degree-sum identity gives
\[
n_1=2+\sum_{d\ge3}(d-2)n_d.
\]
At \(p=1/3\),
\[
3F_T'(1/3)=n_1-\sum_{d\ge3}(d-2)n_d(2/3)^{d-1}
=2+\sum_{d\ge3}(d-2)n_d\bigl(1-(2/3)^{d-1}\bigr)>0.
\]
At \(p=1/2\), the degree-one terms vanish and each term of degree at least two is strictly negative. Thus \(F_T'(1/2)<0\) for \(n\ge3\); for \(n=2\), \(F_T'(p)=2(1-2p)\).

It remains to exclude more than one root between the endpoints. Differentiate again:
\[
F_T''(p)=\sum_{d\ge1}n_ddq^{d-2}((d+1)p-2).
\]
The contribution of each degree-one vertex to this sum is exactly \(-2\). Using the degree-sum identity, one obtains
\[
F_T''(p)=-4+2n_2(3p-2)+\sum_{d\ge3}n_d\left[-2(d-2)+d g_d(p)\right],
\quad g_d(p)=q^{d-2}((d+1)p-2).
\]
For \(1/3\le p\le1/2\), the degree-two term is nonpositive. For \(d=3\), \(g_3(p)=q(4p-2)\le0\), making the square-bracket contribution negative. For every \(d\ge4\), the function \(g_d\) on \([0,1]\) has its global maximum at \(p=3/(d+1)\), with value \(((d-2)/(d+1))^{d-2}<1\). Therefore
\[
-2(d-2)+d g_d(p)<-2(d-2)+d=4-d\le0.
\]
It follows that \(F_T''(p)<0\) throughout \([1/3,1/2]\). Together with the strict endpoint signs, this proves exactly one zero there. Below \(1/3\), the same leaf-surplus identity gives direct positivity: for \(p\le1/3\), the degree-one term \(1-2p\ge1/3\), and for \(d\ge3\), any negative term has magnitude at most \((d-2)(1-2p)\). Indeed, if \(1-(d+1)p<0\), then
\[
q^{d-1}((d+1)p-1)\le (d+1)p-1\le (d-2)(1-2p)
\]
since \(3(d-1)p\le d-1\) exactly when \(p\le1/3\). Pairing every degree-\(d\) negative contribution with its \(d-2\) surplus leaves therefore leaves at least \(2(1-2p)>0\). For \(p\ge1/2\), every degree-one term is nonpositive and all degree-at-least-two terms are negative, so \(F_T'(p)<0\) for \(n\ge3\). Thus the root is globally unique.

For paths, \(F_{P_n}'(p)=2(1-2p)+(n-2)(1-p)(1-3p)\); its unique root approaches \(1/3\). For stars, \(F_{K_{1,n-1}}'(p)=(n-1)(1-2p)+(1-p)^{n-2}(1-np)\); its unique root approaches \(1/2\) because the first term dominates at every fixed \(p<1/2\). This proves sharpness of both endpoints.

Finally, let \(G\) be \(K_{15}\) with a two-edge pendant path appended to one clique vertex. Its degree multiset is fourteen copies of \(14\), one \(15\), one \(2\), and one \(1\). The expression
\[
F_G'(p)=14q^{13}(1-15p)+q^{14}(1-16p)+q(1-3p)+(1-2p)
\]
is strictly positive, negative, positive, negative at \(p=1/20,1/5,1/3,1/2\) respectively (exact rational certificates supplied). Continuity gives at least three distinct interior roots, proving the tree hypothesis is substantive.

## Verification

Run `python verify.py` after installing `networkx>=3.0,<4.0`; the program uses rational arithmetic and exhaustively computes \(S_T\), \(I_T\), and \(S_TI_T\) over every retained-vertex subset for all 47 nonisomorphic trees of orders two through eight at three rational probabilities (141 exact comparisons). It also verifies endpoint derivative signs and the four rational signs in the connected non-tree witness. Expected output appears in `certificate.json`. Finite checks corroborate but do not replace the all-order analytical proof.

## Relationship to prior work

He and Hubbell (2003) develop independent-cell ecological percolation and hump-shaped landscape fragmentation measures, including an approximate patch-number relationship. Their four-page article treats regular grids and scaling with abundance, not the exact unique covariance switch for arbitrary finite trees, its sharp universal interval, or the connected cyclic counterexample. Diskin and Krivelevich (2023) study large pseudo-random regular graphs under site percolation and component-size concentration; their model and asymptotic claims do not yield this exact tree theorem. Standard differentiation identities and degree-sum formulas are used as known tools; novelty is claimed only for their stated structural combination and sharp graph-class boundary.

## Limitations

Correlated retention, heterogeneous survival probabilities, disconnected forests, graphs with cycles and stochastic dynamics over time are outside the positive theorem. The connected cyclic example demonstrates that the one-switch law can fail outside trees. The threshold concerns an ideal independent-retention model, not an empirically calibrated conservation recommendation. The novelty review is not an independent bibliographic audit; equivalent unpublished or differently named statements cannot be ruled out.

## References

1. F. He and S. P. Hubbell, “Percolation Theory for the Distribution and Abundance of Species,” *Physical Review Letters* 91, 198103 (first public journal publication 7 November 2003), DOI: 10.1103/PhysRevLett.91.198103. Author-hosted full text: https://sites.ualberta.ca/~fhe/He-publications/He_Hubbell.PRL03.pdf.
2. S. Diskin and M. Krivelevich, “Site percolation on pseudo-random graphs,” *Random Structures & Algorithms* 63 (2023), 406–441, DOI: 10.1002/rsa.21141; first published 17 February 2023.
