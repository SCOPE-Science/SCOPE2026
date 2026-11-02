# Exact transient Wasserstein amplification on two-level regular trees

## Finding
For integers \(b,k\ge 2\), let \(T_{b,k}\) be the unit-edge tree with a root, \(b\) children, and exactly \(k\) leaves at each child. Its continuous-time random walk jumps across every edge in each direction at rate one. Write \(P_t=e^{-tL}\) for the Markov semigroup, where \(L\) is the unnormalized combinatorial Laplacian. Distances in \(W_1\) are shortest-path distances with every edge of length one.

For every real \(t\ge0\), define
\[
S(t)=\exp\!\left(-t\begin{pmatrix}1&-\sqrt{k}\\-\sqrt{k}&k+1\end{pmatrix}\right),\qquad
G(t)=\exp\!\left(-t\begin{pmatrix}b+1&-\sqrt{k}\\-\sqrt{k}&k+1\end{pmatrix}\right),
\]
and write their entries as \(S_{ij}\) and \(G_{ij}\). Put \(z=e^{-t}\) and \(U=((b-1)S_{22}+G_{22})/b\). Define
\[
\begin{aligned}
I_{b,k}(t)={}&\frac{|(b-1)S_{11}+G_{11}|+(b-1)|S_{11}-G_{11}|}{b}\\
&+\frac{\sqrt{k}}{b}\bigl(|(b-1)S_{12}+G_{12}|+(b-1)|S_{12}-G_{12}|\bigr),\\[3pt]
O_{b,k}(t)={}&\frac{|(b-1)S_{12}+G_{12}|+(b-1)|S_{12}-G_{12}|}{b\sqrt{k}}\\
&+\frac{|U+(k-1)z|+(k-1)|U-z|}{k}+\frac{b-1}{b}|S_{22}-G_{22}|.
\end{aligned}
\]
Then the exact optimal Wasserstein-one amplification coefficient is
\[
\boxed{\ \mathcal C_{b,k}(t):=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)}=\max\{I_{b,k}(t),O_{b,k}(t)\}.\ }
\]
An edge from the root to a child attains the value \(I_{b,k}(t)\); a child-to-leaf edge attains \(O_{b,k}(t)\). In each case the witnesses are the two Dirac probabilities at that edge's endpoints. The formulas hold without piecewise restrictions on time, and evaluating them requires only two \(2\)-by-\(2\) exponentials, regardless of the size of the tree.

There is a sharp branching asymptotic. On the diagonal family \(b=k=N\), as integers \(N\to\infty\),
\[
\boxed{\ \max_{t\ge0}\mathcal C_{N,N}(t)
=4-\frac{10}{N}+O\!\left(\frac{\log N}{N^2}\right).\ }
\]
The diameter bound \(4\) is never attained by any finite member of the family, but the amplification tends to \(4\) already at the vanishing times \(t_N=3\log N/N\).

## Assumptions and scope
All probabilities are on the finite vertex set; \(W_1\) uses the unweighted graph-path metric, even though the Markov process is defined by its jump rates. Every undirected edge carries jump rate one in each direction, not a degree-normalized transition rate. No self-loops are added. The two integers satisfy \(b,k\ge2\), and the time satisfies \(t\ge0\). The graph has \(1+b+bk\) vertices and \(b+bk\) edges. Its diameter is four. The assertion concerns the induced norm on probabilities in the transportation distance, equivalently the Lipschitz seminorm operator norm of \(P_t\).

## Proof
**1. Reduce the transport norm to edge columns.** Give every edge its outward orientation from the root, and write \(B\) for the vertex-by-edge incidence matrix with \(-1\) at an edge's tail and \(+1\) at its head. For this finite tree, \(B\) has full column rank and \(L=BB^{\mathsf T}\). A signed measure \(\sigma\) of total mass zero has a unique edge flow \(h\) satisfying \(Bh=\sigma\); the exact tree-transport identity is \(\|\sigma\|_{W_1}=\sum_e|h_e|\). This follows either by transporting the signed mass through the unique connecting paths or by the dual \(1\)-Lipschitz potential whose increments have the signs of the flows.

The intertwining identity \(e^{-tBB^{\mathsf T}}B=B e^{-tB^{\mathsf T}B}\) follows term by term from the exponential series. Consequently the transport norm between the semigroup images of any adjacent vertices is exactly the absolute column sum of \(E(t)=e^{-tB^{\mathsf T}B}\). For an arbitrary pair, decompose its shortest path into edges and use the triangle inequality. For an arbitrary pair of probabilities, apply the same bound to an optimal transport coupling and linearity of \(P_t\). Hence
\[
\mathcal C_{b,k}(t)=\max_{\text{edges }e}\sum_f|E(t)_{f,e}|.
\]
The matrix \(E(t)\) is symmetric, so columns can be replaced with rows.

**2. Decompose the edge Laplacian.** Index root-to-child edges by \(i=1,\ldots,b\), and edges from child \(i\) to its leaves by \((i,j)\), with \(j=1,\ldots,k\). Direct incidence multiplication gives \(B^{\mathsf T}B\) with inner-inner block \(I_b+J_b\), inner-outer block \(-I_b\otimes\mathbf1_k^{\mathsf T}\), and outer-outer block \(I_b\otimes(I_k+J_k)\). Here \(J_d\) denotes the all-ones matrix of order \(d\).

Split the leaf-edge coordinates into their branchwise means and the sum-zero contrasts inside each branch. The latter have eigenvalue one. In the normalized means, the remaining operator is
\[
\begin{pmatrix}I_b+J_b&-\sqrt{k}I_b\\-\sqrt{k}I_b&(k+1)I_b\end{pmatrix}.
\]
The constant vector on the \(b\) branches yields the matrix defining \(G(t)\); its orthogonal complement yields \(b-1\) copies of the matrix defining \(S(t)\). The contrast semigroup contributes \(z=e^{-t}\).

**3. Evaluate the two edge orbits.** For a root-to-child edge with branch index \(i\), the entries in its row of \(E(t)\) are: \(((b-1)S_{11}+G_{11})/b\) in its own inner column; \((G_{11}-S_{11})/b\) in each of the other \(b-1\) inner columns; \(((b-1)S_{12}+G_{12})/(b\sqrt k)\) in each of its \(k\) outer columns; and \((G_{12}-S_{12})/(b\sqrt k)\) in each of the remaining \(k(b-1)\) outer columns. Their absolute sum is exactly \(I_{b,k}(t)\).

For a child-to-leaf edge, the inner entries are \(((b-1)S_{12}+G_{12})/(b\sqrt k)\) on its parent branch and \((G_{12}-S_{12})/(b\sqrt k)\) on each other branch. Its outer entries are \((U+(k-1)z)/k\) on itself, \((U-z)/k\) on its \(k-1\) siblings, and \((G_{22}-S_{22})/(bk)\) on each of the \(k(b-1)\) outer edges in the other branches. Their absolute sum is exactly \(O_{b,k}(t)\). These are the only two edge orbits, proving the all-time formula.

Both \(2\)-by-\(2\) exponentials above can, if desired, be evaluated using elementary exponentials and hyperbolic functions: for either displayed symmetric matrix \(H\), let \(\tau=\operatorname{tr}H\) and \(\delta=\sqrt{(H_{11}-H_{22})^2+4k}\). Then
\[
e^{-tH}=e^{-\tau t/2}\left[\cosh(\delta t/2)I_2-\frac{2\sinh(\delta t/2)}{\delta}\left(H-\frac\tau2I_2\right)\right].
\]

**4. Sharp large-branching behavior.** For \(b=k=N\), the matrices \(-H_S\) and \(-H_G\) are Metzler, with \(-H_G\le-H_S\) entrywise. Positivity and matrix comparison therefore give \(0\le G_{ij}(t)\le S_{ij}(t)\). In particular the absolute values in the inner-edge formula simplify to
\[
I_{N,N}(t)=2\left(1-\frac1N\right)X_N(t)-\left(1-\frac2N\right)Y_N(t),
\quad X_N=S_{11}+\sqrt N S_{12},\quad Y_N=G_{11}+\sqrt N G_{12}.
\]
Write \(\Delta_N=\sqrt{N(N+4)}\), \(\lambda_\pm=(N+2\pm\Delta_N)/2\), and \(A_N=(N-1+\lambda_+)/\Delta_N\). The spectral decomposition of \(H_S\) gives
\[
X_N(t)=A_N e^{-\lambda_-t}-(A_N-1)e^{-\lambda_+t},\qquad A_N=2-\frac3N+O(N^{-2}),\quad A_N>1.
\]
Therefore \(X_N(t)\le A_N\) for all \(t\ge0\), and \(Y_N\ge0\), giving the uniform upper bound
\[
I_{N,N}(t)\le2(1-N^{-1})A_N=4-\frac{10}{N}+O(N^{-2}).
\]
At \(t_N=3\log N/N\), the fast eigenmode of \(H_S\) contributes \(O(N^{-3})\), while its slow mode differs from its zero-time coefficient by \(O((\log N)/N^2)\). The smaller eigenvalue of \(H_G\) is exactly \(N+1-\sqrt N\), and hence \(0\le Y_N(t_N)\le\sqrt{N+1}\,e^{-(N+1-\sqrt N)t_N}=O(N^{-5/2+o(1)})\). Thus
\[
I_{N,N}(t_N)=4-\frac{10}{N}+O\!\left(\frac{\log N}{N^2}\right).
\]
For the outer-edge formula, positivity and \(0\le G_{ij}\le S_{ij}\le1\) show that its inner-column term is at most \(2/\sqrt N\), its other-branch outer-column term is at most one, and its same-branch outer-column term is at most two: the latter follows by splitting into \(U\ge z\) and \(U<z\). Consequently \(O_{N,N}(t)\le3+2/\sqrt N\) uniformly in \(t\). For all sufficiently large \(N\), this is smaller than \(I_{N,N}(t_N)\). Combining this with the upper bound for \(I_{N,N}\) proves the claimed exact first-order asymptotic of the global maximum.

Finally, every heat kernel on a finite connected graph is strictly positive at each positive time. Two such probability measures admit a coupling that matches a positive common mass at zero cost, so their \(W_1\) distance is strictly below the diameter \(4\). At \(t=0\) the norm is one and as \(t\to\infty\) it tends to zero; by continuity its maximum is attained and strictly below four for every fixed finite \(b,k\).

## Verification
Run `python CHECKER.py` with Python 3, NumPy, and SciPy. The script constructs the full vertex-edge incidence matrix independently of the displayed two-block decomposition. It compares the exact formula against complete exponential-matrix absolute row sums for \(b,k=2,\ldots,6\) at nine times, reconstructs unique tree flows from evolved vertex probabilities, independently solves five finite optimal-transport linear programs, and checks the large-branching trend. The successful replay recorded 783 matrix/flow comparisons, 5 primal transport linear programs, and 8 large-branching tests. These are finite supplementary checks; the all-parameter statement and asymptotic are proved above.

## Relationship to prior work
Ollivier's Markov-chain coarse-curvature work develops the relation between transportation contraction and local pairs in geodesic graphs. Münch and Wojciechowski, especially Theorem 3.8, establish a heat-semigroup formulation of graph Lipschitz contraction estimates. Cheng, Li, and Wu treat general coupling criteria and exponential convergence for jump processes. Those general frameworks motivate the exact coefficient considered here; none of the inspected relevant statements furnishes the two-block all-time formula for \(T_{b,k}\) or its sharp asymptotic factor-four saturation. The 2019 source was only accessible for abstract-level comparison, leaving an explicit historical-coverage risk. Exact closed results for a one-level star, a clique-barbell, or a bipartite graph concern distinct geometries and do not imply the displayed two-level tree calculation.

## Limitations
The graph is finite, has exactly two generations below its root, and has uniform branching within each generation. The generator is unnormalized and all jump rates and geometric edge lengths equal one. The formula is an exact maximum of two elementary expressions; it does not assert that one edge orbit dominates for every pair of parameters and all times. The asymptotic sharp coefficient \(10\) is proved only along the equal-branching diagonal. No independent external validation is claimed; equivalently formulated older results not found by the stated searches remain possible.

## References
1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, Journal of Functional Analysis 256 (2009), 810–864. Full-text access: https://paperzz.com/doc/6992413/ricci-curvature-of-markov-chains-on-metric-spaces.
2. Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first public version December 4, 2017), especially Theorem 3.8. https://arxiv.org/abs/1712.00875.
3. Lingyan Cheng, Ruinan Li, and Liming Wu, *Ricci curvature and \(W_1\)-exponential convergence of Markov processes on graphs*, arXiv:1907.11036 (first public version July 25, 2019). https://arxiv.org/abs/1907.11036.
