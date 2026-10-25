# Adjacent links uniquely maximize two-failure Kirchhoff loss in Boolean hypercubes

## Finding
Let \(Q_d\) be the unweighted \(d\)-dimensional Boolean hypercube, \(d\ge3\). For any distinct edges \(e,f\), let \(K_d(e,f)\) be the Kirchhoff index after deleting these two edges. Then
\[
K_d(e,f)\le K_d(e_*,f_*),
\]
where \(e_*\) and \(f_*\) are any two different edges sharing one vertex. Equality holds **if and only if** \(e\) and \(f\) share a vertex. There are exactly \(2^d\binom d2\) maximizing unordered pairs of links. All two-link deletions leave the graph connected.

The maximum increase is an exact rational function of \(d\) specified by finite binomial sums. With \(N=2^d\), define for \(k=0,\ldots,d\) and \(p=1,2\)
\[
 g_{p,d}(k)=\frac1N\sum_{s=1}^d\frac{\displaystyle\sum_{j=0}^{s}(-1)^j\binom kj\binom{d-k}{s-j}}{(2s)^p},
\]
with out-of-range binomial coefficients interpreted as zero. Set
\[
 a_k=g_{1,d}(k)-g_{1,d}(k+1),\quad b_k=g_{2,d}(k)-g_{2,d}(k+1),\quad (0\le k<d),
\]
\[
 h=1-2a_0,\quad S=2b_0,\quad x=a_0-a_1,\quad y=b_0-b_1.
\]
Then \(h^2>x^2\) and the **sharp maximal increase** is
\[
 \boxed{\ K_d(e_*,f_*)-K(Q_d)=\frac{2N(hS+xy)}{h^2-x^2}.\ }
\]
For example, the maximal increases at dimensions \(3\), \(4\), and \(5\) are \(172/15\), \(502/51\), and \(2696/245\), respectively.

## Assumptions and scope
The graph is the simple cube on binary vectors \(\{0,1\}^d\), with unit conductance on each edge whose endpoints differ in one coordinate. The Kirchhoff index \(K(G)\) is the sum of pairwise electrical effective resistances over **unordered** distinct vertex pairs; equivalently \(K(G)=|V(G)|\operatorname{tr}(L_G^+)\). The optimization chooses an unordered set of exactly two distinct existing edges, removes each completely, and keeps all remaining conductances equal to one. Dimension \(d=2\) is excluded because two-edge deletion may disconnect the cycle. The result makes no claim for arbitrary weighted or non-cubical networks or for removing three or more links.

## Proof
**Connectivity.** Every proper nonempty vertex set of \(Q_d\) has at least \(d\) boundary edges. For completeness, split a set along one coordinate into two \((d-1)\)-cube layers. If both layers are nonempty and proper, their internal boundaries total at least \(2(d-1)\ge d\); if one is empty or full, use the other layer's \(d-1\) internal boundary edges together with at least one crossing edge, or use the full layer's \(2^{d-1}\ge d\) crossing edges. Induction from dimension one proves the cut bound. Thus deleting only two edges cannot disconnect \(Q_d\) for \(d\ge3\).

**Green kernels and strict distance monotonicity.** Let \(L\) be the cube Laplacian. Translation and coordinate-permutation invariance make the \((x,z)\) entry of \((L^+)^p\) depend only on Hamming distance \(k=\operatorname{dist}(x,z)\), and diagonalizing on Walsh characters gives \(g_{p,d}(k)\) above. In the heat-kernel representation, with \(q=e^{-2t}\),
\[
 (e^{-tL})_{xz}=2^{-d}(1+q)^{d-k}(1-q)^k.
\]
Integrating the difference of entries at distances \(k\) and \(k+1\) gives
\[
 a_k=2^{-d}\int_0^1(1+q)^{d-k-1}(1-q)^k\,dq,
\]
\[
 b_k=2^{-d-1}\int_0^1(-\log q)(1+q)^{d-k-1}(1-q)^k\,dq.
\]
Both sequences and their consecutive differences are positive and strictly decreasing in \(k\). Indeed their integrands are positive multiples of \(((1-q)/(1+q))^k\), which is strictly between zero and one for \(0<q<1\).

**Reduction of every link pair.** Write \(z_e\) for an oriented edge-incidence vector, and put \(R=z_e^{\mathsf T}L^+z_e=2a_0\) and \(S=z_e^{\mathsf T}(L^+)^2z_e=2b_0\). For two distinct edges, choose their orientations so that the mixed Green quantities \(x=z_e^{\mathsf T}L^+z_f\) and \(y=z_e^{\mathsf T}(L^+)^2z_f\) are nonnegative. Cube automorphisms reduce their absolute values to exactly two families:
\[
 \begin{array}{ll}
 \text{parallel links, separation }k=1,\ldots,d-1: &(x,y)=(2a_k,2b_k),\\[2pt]
 \text{different coordinate directions, separation }k=0,\ldots,d-2: &(x,y)=(a_k-a_{k+1},b_k-b_{k+1}).
 \end{array}
\]
For parallel links, separation is the Hamming distance between their endpoints with the active coordinate fixed. For links in different directions, it is the Hamming distance in the remaining \(d-2\) coordinates after reflecting endpoints as needed. The same monotonicity of the integrands makes both \(x\) and \(y\) strictly decrease with separation in either family.

**The two-link update.** The rank-two Woodbury identity on the orthocomplement of constants yields
\[
 K_d(e,f)-K(Q_d)=\frac{2N(hS+xy)}{h^2-x^2},\qquad h=1-R.
\]
Here \(h>0\) and \(h^2>x^2\): their positivity follows from connectivity after removing both links, since \(I_2-B^{\mathsf T}L^+B\) is positive definite, where the columns of \(B\) are the two edge-incidence vectors. For \(x,y>0\), the displayed increase is strictly increasing in each variable. It therefore suffices to compare the nearest parallel pair with \((x,y)=(2a_1,2b_1)\) against the adjacent, perpendicular pair with \((x,y)=(a_0-a_1,b_0-b_1)\).

**Uniform comparison in large dimension.** For each \(d\ge2\), the ratios \(a_0/a_1\) and \(b_0/b_1\) are expectations of the strictly increasing function \((1+q)/(1-q)\) under positive measures having respective densities proportional to
\[
 (1+q)^{d-2}(1-q),\qquad (1+q)^{d-2}(1-q)(-\log q).
\]
When \(d\) increases by one, either density is tilted by the strictly increasing factor \(1+q\). Positive covariance of increasing functions gives strict monotonicity of both ratios in \(d\): for independent identically distributed \(U,V\), twice the covariance of \(f(U)\) and \(g(U)\) is \(\mathbb E[(f(U)-f(V))(g(U)-g(V))]\), which is positive when \(f\) and \(g\) are strictly increasing on a nonatomic law. At \(d=2\), \(a_0/a_1=3\), so \(a_0>3a_1\) for every \(d\ge3\). At \(d=8\), direct evaluation of the finite rational sum gives \(b_0-3b_1=1007/1204224>0\). Hence \(b_0>3b_1\) for all \(d\ge8\). For these dimensions the adjacent pair has strictly larger \(x\) and strictly larger \(y\) than the best parallel pair, proving strict superiority.

**The remaining five dimensions.** For \(d=3,4,5,6,7\), compute the rational difference between the adjacent-pair increase and the nearest-parallel-pair increase from the same finite binomial sums:
\[
\begin{array}{c|c}
 d & \Delta_{\mathrm{adjacent}}-\Delta_{\mathrm{parallel}}\!\\\hline
 3&8/35\\
 4&1196/2635\\
 5&163136/277389\\
 6&1670696/2218671\\
 7&6361472/6418395
\end{array}
\]
Every difference is strictly positive. The finite rational algorithm below independently reproduces these certificates. Thus adjacent links uniquely maximize the increase at all \(d\ge3\). Each such unordered pair has one shared vertex, and choosing two of its \(d\) incident edges gives \(2^d\binom d2\) optimizers.

## Verification
Run `python3 verify_hypercube.py` using only the Python standard library. The program evaluates the finite rational Walsh sums for dimensions \(3\) through \(12\), verifies every orbit's increase is strictly below the adjacent optimum, and checks the dimension-eight separator exactly. It also computes actual grounded Laplacian inverses over exact rational numbers for the unmodified cube and representative deletion configurations in dimensions \(3\), \(4\), and \(5\), confirming the rank-two formula independently; it enumerates all unordered link pairs of these three cubes and checks their orbit classification. These finite calculations verify the small-dimension branch and detect implementation mistakes; the statements for all dimensions follow from the integral monotonicity argument.

## Relationship to prior work
Liu, Cao, Pan, and Elaiw (2013) derive the unmodified hypercube Kirchhoff index and the indices of its line, subdivision, and total graphs, using Laplacian spectra. Their formulas do not compare two-link failures of the original hypercube. The effective graph-resistance literature supplies the metric and spectral identity, but not this extremal geometry. Hamburger, Pippert, and Weakley (1992) consider *shortest-path distance* leverage under hypercube edge removal, a different objective. The general edge-defect method of Tamura (2026) is formulated for complete graphs with deleted edges; a Boolean cube is not a complete graph, and its nonconstant Green kernel is essential here. In particular, no cited comparison establishes the maximizing pair or its complete equality classification by implication.

## Limitations
Novelty is based on the identified and inspected sources, not a proof that no equivalent unpublished or unindexed result exists. The 1992 leverage article was available here only through its publisher abstract; its full text was not inspected. No independent mathematical audit has been performed. The arbitrary-dimensional assertion is proved analytically and is not inferred from the finite verifier. This result does not address randomly failing links, vertex failures, directed edges, heterogeneous conductances, or other robustness metrics.

## References
1. J. Liu, J. Cao, X.-F. Pan, and A. Elaiw, “The Kirchhoff Index of Hypercubes and Related Complex Networks,” *Discrete Dynamics in Nature and Society*, Article 543189 (first published 12 December 2013), https://doi.org/10.1155/2013/543189.
2. W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic, and R. E. Kooij, “Effective graph resistance,” *Linear Algebra and its Applications* 435 (2011), 2491–2506, https://doi.org/10.1016/j.laa.2011.02.024.
3. P. Hamburger, R. E. Pippert, and W. D. Weakley, “On a leverage problem in the hypercube,” *Networks* 22 (1992), 435–439, https://doi.org/10.1002/net.3230220502.
4. S. Tamura, “Edge-defect matrices and stability of the Kirchhoff index for complete graphs with deleted edges,” arXiv:2608.05924v1 (6 August 2026), https://arxiv.org/abs/2608.05924.
