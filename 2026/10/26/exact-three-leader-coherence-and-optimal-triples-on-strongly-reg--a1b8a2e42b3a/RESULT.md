# Exact three-leader coherence and optimal triples on strongly regular networks

## Finding

Let \(G\) be any connected, noncomplete, finite simple unweighted strongly regular graph with parameters \((v,k,\lambda,\mu)\), where \(v\ge4\), \(\mu>0\), and graph Laplacian \(L=kI-A\). For a three-vertex **noise-free** leader set \(S\), put \(F=V(G)\setminus S\) and define the unnormalized follower-coherence criterion
\[
C(S)=\operatorname{tr}\bigl((L_{FF})^{-1}\bigr).
\]
Let \(e(S)\in\{0,1,2,3\}\) be the number of edges induced by \(S\). Define \(b=k-\lambda+\mu\), \(p=2k-\lambda+\mu\), and
\[
K_G=\frac{(v-4)p-vk}{v\mu}.
\]
Then **the exact performance of every leader triple depends only on the number of its induced edges**:
\[
C(S)=K_G+\Phi_{e(S)}(b,\mu),
\]
where
\[
\begin{aligned}
\Phi_0(b,\mu)&=\frac{b^2+6\mu}{3b\mu},\\
\Phi_1(b,\mu)&=\frac{b^3+6b\mu-b-2\mu}{\mu(b-1)(3b+1)},\\
\Phi_2(b,\mu)&=\frac{b^3+6b\mu-2b-4\mu}{b\mu(3b-4)},\\
\Phi_3(b,\mu)&=\frac{b^2+b+6\mu-2}{3\mu(b-1)}.
\end{aligned}
\]
For every such graph, \(b\ge3\), and the four formal costs satisfy the **strict hierarchy**
\[
\Phi_0(b,\mu)<\Phi_1(b,\mu)<\Phi_2(b,\mu)<\Phi_3(b,\mu).
\]
Only classes realized by actual leader triples are relevant. Thus **precisely the three-vertex sets inducing the fewest graph edges are optimal**.

This yields a parameter-only optimal-triple classification and count. Set \(d=v-k-1\) and \(t=v-2k+\mu-2\), respectively the degree and adjacent-common-neighbor parameter of the complement. Exactly one of the following holds:

1. If \(t>0\), optimal triples induce zero edges in \(G\); there are exactly \(vdt/6\) of them and the minimum cost is \(K_G+\Phi_0(b,\mu)\).
2. If \(t=0\) and \(d\ge2\), optimal triples induce exactly one edge in \(G\); there are exactly \(vd(d-1)/2\) of them and the minimum cost is \(K_G+\Phi_1(b,\mu)\).
3. If \(d=1\), optimal triples induce exactly two edges in \(G\); there are exactly \(v(v-2)/2\) of them and the minimum cost is \(K_G+\Phi_2(b,\mu)\).

In particular, nonisomorphic strongly regular graphs with identical parameters share the same possible induced-triple performance values and the same optimal value and number of optimal triples.

## Assumptions and scope

The graph is finite, undirected, connected, simple, unweighted, noncomplete, and strongly regular: every vertex has degree \(k\); every adjacent pair has exactly \(\lambda\) common neighbors; and every distinct nonadjacent pair has exactly \(\mu\) common neighbors. The connected, noncomplete condition implies \(\mu\ge1\), and there is at least one nonedge. Strong regularity does **not** require vertex transitivity. Every chosen triple consists of distinct vertices, whose states are perfectly pinned to the common target; only the remaining \(v-3\) follower states experience independent equal-intensity white noise and evolve under the grounded Laplacian \(L_{FF}\). With unit-variance noise, total steady-state follower variance is \(C(S)/2\); the displayed theorem uses \(C(S)\) to avoid that uniform factor.

## Proof

**1. Strongly regular resolvent.** Write \(J\) for the all-ones matrix and \(A\) for adjacency. The defining common-neighbor condition gives
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J,
\]
while regularity gives \(AJ=kJ\). Double-counting edges from a neighbor of a vertex to its nonneighbors yields
\[
(v-k-1)\mu=k(k-\lambda-1).
\]
It follows that
\[
\begin{aligned}
Q(z)&=z^2+pz+v\mu,\\
(zI+L)^{-1}&=\frac{(z+b)I+A+(\mu/z)J}{Q(z)}
\end{aligned}
\]
for every \(z>0\): multiply the right-hand numerator by \((z+k)I-A\), apply the two identities above, and get exactly \(Q(z)I\). The Laplacian has one zero eigenvalue and the remaining eigenvalues positive because \(G\) is connected. The coefficient \(b\) obeys \(b\ge3\): if \(\lambda=k-1\) then connectedness forces a complete graph, while otherwise \(k-\lambda\ge2\) and \(\mu\ge1\).

**2. Three-vertex complementary determinant identity.** For a chosen leader triple \(S\) let \(A_S\) be its \(3\times3\) principal adjacency matrix and \(F=V(G)\setminus S\). Jacobi's complementary-minor identity, applied to the invertible matrix \(zI+L\), yields
\[
\det(zI+L_{FF})=\det(zI+L)\det\bigl([(zI+L)^{-1}]_{SS}\bigr).
\]
Set \(r=z+b\), \(H_S(r)=rI_3+A_S\), \(D_S(r)=\det H_S(r)\) and \(U_S(r)=\boldsymbol1^T\operatorname{adj}(H_S(r))\boldsymbol1\). The rank-one determinant identity gives
\[
\det(zI+L_{FF})=\frac{\det(zI+L)}{zQ(z)^3}\bigl(zD_S(z+b)+\mu U_S(z+b)\bigr).
\]
Every \(L_{FF}\) is positive definite. Its inverse trace equals the logarithmic derivative at \(z=0\) of its shifted determinant. The first factor above is independent of \(S\) and has logarithmic derivative
\[
K_G=\operatorname{tr}(L^+)-\frac{3p}{v\mu}=\frac{(v-4)p-vk}{v\mu},
\]
because \(L^+=(p(I-J/v)-L)/(v\mu)\), as follows by taking the finite part of the resolvent at zero. The second factor contributes
\[
\frac{D_S(b)+\mu U_S'(b)}{\mu U_S(b)}.
\]

**3. Exhaust the four three-vertex types.** For \(e(S)=0,1,2,3\), respectively, the unlabeled induced adjacency matrices are uniquely determined. Computing their \(3\times3\) determinants and adjugates gives
\[
\begin{array}{c|c|c}
e&D_e(r)&U_e(r)\\\hline
0&r^3&3r^2\\
1&r(r^2-1)&(r-1)(3r+1)\\
2&r(r^2-2)&r(3r-4)\\
3&(r-1)^2(r+2)&3(r-1)^2
\end{array}
\]
Substitution into the final expression of step 2 gives the four explicit rational functions in the Finding section. Their denominators are nonzero for \(b\ge3\), \(\mu>0\).

**4. Strict ordering.** Direct common-denominator subtraction gives the three *exact* successive gaps:
\[
\begin{aligned}
\Phi_1-\Phi_0&=\frac{2[b^2(b-1)+3\mu(b+1)]}{3b\mu(b-1)(3b+1)},\\
\Phi_2-\Phi_1&=\frac{2[b^3(b-2)+b+\mu(3b^2-3b+2)]}{b\mu(b-1)(3b-4)(3b+1)},\\
\Phi_3-\Phi_2&=\frac{2[b(b-1)^2+3\mu(b-2)]}{3b\mu(b-1)(3b-4)}.
\end{aligned}
\]
Each numerator and denominator is strictly positive when \(b\ge3\), \(\mu\ge1\). Thus the cost is strictly increasing in the number of edges induced by a feasible leader triple, proving the optimality criterion.

**5. Existence, classification and enumeration of all minimizers.** The complement \(\overline G\) is \(d\)-regular; each of its adjacent pairs has exactly \(t\) common neighbors. If \(t>0\), it contains triangles, and a triangle in \(\overline G\) is precisely an edgeless triple in \(G\). Counting complement triangles by edge–common-neighbor incidences yields \(vdt/6\). If \(t=0\) and \(d\ge2\), the complement is triangle-free but has two-edge length-two paths; these are precisely the one-edge triples of \(G\), and each has a unique center, giving \(v\binom d2\). Finally, if \(d=1\), the complement is a perfect matching; each triple includes at most one of its matching edges, and triples containing one yield exactly two edges in \(G\). Their number is \((v/2)(v-2)\). These are mutually exclusive and exhaustive, completing the proof.

## Verification

Run `python verify.py` with packages from `requirements.txt`. The script independently constructs nine strongly regular graphs, checks the adjacency identity, checks an exact shifted-resolvent matrix identity, computes exact rational grounded inverses for representatives of every feasible three-vertex pattern, checks the exact symbolic rational costs and positive-gap identities, counts optimal triples by direct combinatorial enumeration, and compares the nonisomorphic Shrikhande and four-by-four rook graphs. In the Petersen graph, an optimal edgeless leader triple has \(C(S)=91/30\); for the five-cycle the one-edge and two-edge triple values are respectively \(1\) and \(4/3\). These finite calculations are corroboration; the proof above covers every admissible strongly regular graph.

## Relationship to prior work

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (first publicly posted 2014-07-07 as arXiv:1407.1569), provide a general graph-theoretic performance formulation for leader sets, including a two-leader corollary and explicit optimum placements on cycles and paths. Their framework is applicable here but does not state the exact four induced-three-vertex cost values, their strict hierarchy, or this parameter-only trichotomy and count. Patterson, Yi and Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks* (arXiv:1708.06873, 2017), derive resistance-based performance identities and solve cycles, paths and selected tree cases rather than this three-leader strongly regular classification. The characterization of strongly regular networks by two pairwise resistance classes, studied by Zhou, Wang and Bu (2016), does not by itself optimize pinned three-leader configurations. The present proof specializes general consensus theory using an exact complementary-minor calculation and establishes an all-parameter strict pattern ordering.

## Limitations

The theorem concerns exactly three perfectly noise-free leaders, equal-intensity additive follower noise and the unweighted combinatorial Laplacian on connected noncomplete strongly regular graphs. It does not address more than three leaders, finite-gain/noisy leaders, nonregular graphs, or arbitrary edge weights. The classification characterizes optimal sets but does not construct a specific graph from parameters, and different strongly regular graphs with the same parameters need not be isomorphic. Numerical checks cannot replace the all-parameter algebraic proof. Published formulas for arbitrary leader sets are relevant antecedents; a specialized equivalent result in unindexed literature remains a residual originality risk. Independent validation has not been performed.

## References

1. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public posting 2014-07-07, https://arxiv.org/abs/1407.1569 .
2. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first public posting 2017-08-23, https://arxiv.org/abs/1708.06873 .
3. J. Zhou, Z. Wang and C. Bu, *On the Resistance Matrix of a Graph*, Electronic Journal of Combinatorics 23(1), #P1.41 (2016), https://doi.org/10.37236/5295 .
