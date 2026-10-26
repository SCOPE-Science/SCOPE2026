# Sharp transient Lipschitz amplification on balanced double-star trees

## Finding

Let \(D_d\) be the finite unweighted tree formed by joining two hubs by one edge and attaching \(d\) pendant vertices to each hub, with integer \(d\geq 1\). Give edges unit length, let \(L\) be the unnormalized combinatorial Laplacian, and write \(T_t=e^{-tL}\). On functions modulo constants, the sharp Lipschitz operator norm, for **every** \(t\geq0\), is
\[
\|T_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
 =A_d e^{-\lambda_{-,d}t}-(A_d-1)e^{-\lambda_{+,d}t},
\quad \lambda_{\pm,d}=\frac{d+3\pm\sqrt{d^2+6d+1}}2,
\quad A_d=\frac{\lambda_{+,d}+2d-2}{\sqrt{d^2+6d+1}}.
\]
For each positive time the unique maximizing *edge location* is the central hub-to-hub edge. A single real, unit-Lipschitz function, taking values \(-1,0,1,2\) on left leaves, left hub, right hub, right leaves respectively, attains the norm for every \(t\geq0\).

For \(d=1\), the optimal norm is one at \(t=0\) and strictly below one for \(t>0\). For every \(d\geq2\) the norm initially increases, has a **unique** positive-time maximum at
\[
 t_d=\frac{1}{\Delta_d}\log\!\left(\frac{\lambda_{+,d}(A_d-1)}{\lambda_{-,d}A_d}\right),\qquad
 \Delta_d=\sqrt{d^2+6d+1},
\]
and its sharp peak \(M_d=\|T_{t_d}\|_{\mathrm{Lip}\to\mathrm{Lip}}\) satisfies
\[
 M_d=3-\frac8d+O\!\left(\frac{\log d}{d^2}\right),\qquad
 t_d=\frac{2\log d-\log 3+o(1)}d.
\]
Thus the sharp transient amplification tends to \(3\), rather than the \(2\)-scale seen on large ordinary stars. Equivalently, for graph-distance \(W_1\), the largest distance between transition laws from adjacent vertices is always attained by the two hubs and equals the displayed norm.

## Assumptions and scope

All integers \(d\geq1\) and all real \(t\geq0\) are included; graph edges have unit conductance and length. For a real or complex vertex function \(f\), define \(\operatorname{Lip}(f)=\max_{xy\in E(D_d)}|f(x)-f(y)|\). Constants are factored out to obtain a normed space. The heat semigroup uses jump rate one **per adjacent edge**, not the degree-normalized random-walk Laplacian. The graph is the finite *combinatorial* tree, not a continuum metric graph with differential operators along its edges.

## Proof

Orient the \(d\) left leaf edges from each leaf into its hub, the central edge from left hub to right hub, and the \(d\) right leaf edges from the right hub to its leaves. Let \(B\) be the resulting edge-by-vertex incidence matrix. Then \(L=B^{\mathsf T}B\) and, by the power series for the exponential,
\[
 B e^{-tB^{\mathsf T}B}=e^{-tBB^{\mathsf T}}B.
\]
Because \(D_d\) is a tree, \(B\) sends vertex functions modulo constants bijectively to arbitrary \(2d+1\) edge differences. Consequently the desired Lipschitz operator norm equals the maximum absolute row sum of \(E(t)=e^{-tBB^{\mathsf T}}\).

Write \(M=BB^{\mathsf T}\). With the rows ordered as left leaves, central edge, right leaves, \(M\) has diagonal leaf blocks \(I_d+J_d\), central diagonal entry \(2\), coupling \(-\mathbf 1_d\) between the center and each leaf block, and zero left-to-right coupling. On the subspace of leaf-vector deviations from the group means, \(M\) has eigenvalue \(1\). The antisymmetric pair of constant leaf groups gives eigenvalue \(d+1\). In the symmetric constant-leaf and central coordinates, \(M\) is the two-by-two matrix
\[
 S_d=\begin{pmatrix}d+1&-\sqrt{2d}\\-\sqrt{2d}&2\end{pmatrix},
\]
whose two eigenvalues are \(\lambda_{-,d},\lambda_{+,d}\), both positive. Suppress the index \(d\), and put
\[
 s(t)=(e^{-tS_d})_{11},\quad c(t)=(e^{-tS_d})_{22},\quad
 k(t)=\frac{e^{-\lambda_-t}-e^{-\lambda_+t}}{\Delta_d}.
\]
The entries of the central row of \(E(t)\) are \(c(t)\) at the center and \(k(t)>0\) at each of the \(2d\) leaf edges, for \(t>0\). Thus its absolute row sum is \(X(t)=c(t)+2d k(t)\). Its common positive-sign extremizer is the oriented unit edge-gradient vector \(\mathbf 1\), integrated to the four-level function specified above.

For a fixed left or right leaf row, define
\[
 q(t)=\tfrac12\bigl(s(t)+e^{-(d+1)t}\bigr),\qquad
 r(t)=\tfrac12\bigl(s(t)-e^{-(d+1)t}\bigr).
\]
The row has diagonal entry \(e^{-t}+(q-e^{-t})/d>0\), its other \(d-1\) entries in the same leaf group equal \((q-e^{-t})/d\), its \(d\) opposite-group entries equal \(r/d\), and its central entry is \(k\). Positivity of the two-coordinate semigroup \(e^{-tS_d}\) and variation of constants give \(s(t)\geq e^{-(d+1)t}\), so \(r(t)\geq0\). The signed row sum is \(Y(t)=s(t)+k(t)\). Diagonalizing \(S_d\) gives the exact identity
\[
 X(t)-Y(t)=(3d-2)k(t).
\]
We next prove a sign-sensitive bound that rules out an unexpectedly large leaf row. Take Laplace transforms with transform variable \(z>0\). The characteristic polynomial of \(S_d\) is \(p(z)=z^2+(d+3)z+2=(z+\lambda_-)(z+\lambda_+)\), and
\[
 \mathcal L\{s\}(z)=\frac{z+2}{p(z)},\qquad
 \mathcal L\{k\}(z)=\frac1{p(z)}.
\]
A direct rational simplification yields
\[
 \mathcal L\{q+dk-e^{-t}\}(z)
 =\frac{d^2}{(z+1)(z+d+1)(z+\lambda_-)(z+\lambda_+)}.
\]
The inverse transform is \(d^2\) times the convolution of four positive exponential kernels. Therefore \(q(t)+d k(t)\geq e^{-t}\) for every \(t\geq0\). If \(q\geq e^{-t}\), the leaf absolute row sum is exactly \(Y\). Otherwise it is
\[
 Y(t)+\frac{2(d-1)}d(e^{-t}-q(t))
 \leq Y(t)+2(d-1)k(t)<X(t)
\]
for \(t>0\), using \(X-Y=(3d-2)k\). When \(q\geq e^{-t}\), the strict inequality \(Y<X\) follows directly. Hence the central edge is the unique maximum-row location for each \(t>0\), and \(\|T_t\|_{\mathrm{Lip}\to\mathrm{Lip}}=X(t)\), as asserted. At \(t=0\), every row sum is one.

Finally \(X(0)=1\), and the central row sum of \(-M\) gives \(X'(0)=2d-2\). Since \(X\) is a linear combination of \(e^{-\lambda_-t}\) and \(e^{-\lambda_+t}\), solving these initial conditions gives exactly \(X(t)=A_de^{-\lambda_-t}-(A_d-1)e^{-\lambda_+t}\). For \(d=1\) the initial derivative vanishes and the derivative is negative thereafter. For each \(d\geq2\), the initial derivative is positive, the derivative is eventually negative, and the ratio of its two exponential terms is strictly monotone; there is exactly one positive critical time, the stated \(t_d\), and it is the global maximum.

As \(d\to\infty\), direct Taylor expansions give
\[
 \Delta_d=d+3-4d^{-1}+O(d^{-2}),\quad
 \lambda_{-,d}=2d^{-1}+O(d^{-2}),\quad
 A_d=3-8d^{-1}+O(d^{-2}).
\]
Inserting these in the exact critical-time formula gives \(t_d=(2\log d-\log3+o(1))/d\). The slow exponential changes \(A_d\) by at most \(O((\log d)/d^2)\), while at the critical time the fast term equals \((\lambda_{-,d}/\lambda_{+,d})A_de^{-\lambda_{-,d}t_d}=O(d^{-2})\). This proves the claimed peak expansion.

The equivalence with adjacent-point Wasserstein distances follows from the finite-metric Kantorovich dual representation: \(\operatorname{Lip}(T_t f)=\max_{x\sim y}|T_tf(x)-T_tf(y)|\), and each edge supremum over unit-Lipschitz test functions equals the graph-distance \(W_1\) between the two transition distributions.

## Verification

The standalone `check.py` builds the vertex and edge Laplacian matrices independently, checks \(B e^{-tL}=e^{-tM}B\), evaluates every edge-row absolute sum directly, and compares its maximum with the closed formula. It tests nine degrees (\(1,2,3,4,5,7,10,15,20\)) at seven strictly positive times each. It also checks the predicted unique peak against nearby times for every tested \(d\geq2\). Executed using Python, NumPy and SciPy, the 63 time/degree cases passed with largest reported formula discrepancy below \(5\times10^{-14}\). This finite check is supplementary: the proof above establishes every degree and time analytically.

## Relationship to prior work

Haeseler, Keller, Lenz and Wojciechowski (arXiv:1103.3695, first public 18 March 2011) treat semigroup positivity and Laplacian realizations on general discrete graphs; the inspected introduction and semigroup sections do not calculate sharp Lipschitz norms on finite double stars. Keller and Lenz (arXiv:1101.2979, first public 15 January 2011) study graph heat generators, spectra and stochastic completeness rather than this all-time stability invariant. Frank and Kovařík (arXiv:1108.6145, first public 31 August 2011) analyze continuum metric-tree heat kernels and spectral estimates, a distinct generator and function space. Fan and Godsil (arXiv:1206.0082, first public 1 June 2012) work on precisely these double-star graphs, but their operator is the unitary adjacency walk \(e^{itA}\), not the positive heat operator \(e^{-tL}\). Münch and Wojciechowski (arXiv:1712.00875, first public 4 December 2017) relate graph curvature to heat-flow Lipschitz bounds; infinitesimal curvature does not by itself provide the displayed all-time sharp finite-tree formula. Existing exact graph-heat calculations for complete bipartite graphs concern graphs of diameter at most two, rather than the diameter-three double-star geometry. No implication or equivalent formula was identified in the inspected source material; this is not a proof of priority.

## Limitations

The exact formula and equality locations are proved only for balanced unweighted double stars with unit graph metric, under the unnormalized combinatorial heat generator. They are not asserted for unequal double stars, weighted edges, normalized Laplacians or continuum metric-tree heat operators. Full coverage of unindexed historical literature is not possible; an equivalent calculation may exist. The numerical experiment alone would not prove a uniform theorem, and no independent scientific audit is claimed.

## References

1. Matthias Keller and Daniel Lenz, *Unbounded Laplacians on Graphs: Basic Spectral Properties and the Heat Equation*, arXiv:1101.2979, public 15 January 2011, https://arxiv.org/abs/1101.2979.
2. Sebastian Haeseler, Matthias Keller, Daniel Lenz, and Radosław Wojciechowski, *Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions*, arXiv:1103.3695, public 18 March 2011, https://arxiv.org/abs/1103.3695.
3. Rupert L. Frank and Hynek Kovařík, *Heat kernels of metric trees and applications*, arXiv:1108.6145, public 31 August 2011, https://arxiv.org/abs/1108.6145.
4. Xiaoxia Fan and Chris Godsil, *Pretty good state transfer on double stars*, arXiv:1206.0082, public 1 June 2012, https://arxiv.org/abs/1206.0082.
5. Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians*, arXiv:1712.00875, public 4 December 2017, https://arxiv.org/abs/1712.00875.
