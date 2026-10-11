# Sharp \(\ell_p\) isotonic regression stability on every finite partial order

## Finding

Let \(G=(V,E)\) be any finite directed acyclic graph, with no restriction on branching, and let \(N\) be the greatest number of vertices in a weakly connected component. For each \(1<p<\infty\), let \(\Pi_{G,p}\) be the unique metric projection in real \(\ell_p(V)\) onto the order cone \(C_G=\{y\in\mathbb R^V:y_u\le y_v\text{ for every }(u,v)\in E\}\). Thus \(\Pi_{G,p}(x)\) minimizes \(\sum_{v\in V}|x_v-y_v|^p\) over \(y\in C_G\).

Its exact global data-to-fit Lipschitz constant, measured in the *same* \(\ell_p\) norm on the input and output, is
\[
\operatorname{Lip}_{p}(\Pi_{G,p})=
\begin{cases}
1,&N\le2\text{ or }p=2,\\
N^{1/p},&N\ge3,\ 1<p<2,\\
(N/2)^{1/p},&N\ge3,\ 2<p<\infty.
\end{cases}
\]
In particular, for every weakly connected graph with at least three vertices the optimal constant depends only on the vertex count, not on the edge set, and the constants have distinct one-sided limits at \(p=2\): \(\sqrt N\) from below and \(\sqrt{N/2}\) from above, whereas the value at \(p=2\) is \(1\).

## Assumptions and scope

All graphs are finite directed acyclic graphs; weak connectivity refers to connectivity after forgetting edge orientations. All data and fits are real. A component of size one has identity projection. The supremum in the Lipschitz constant is over all pairs of distinct data vectors in \(\mathbb R^V\). The bounds are optimal suprema: in the non-Hilbert cases the extremal ratio may only be approached, not attained at an individual differentiability point.

Write \(q=p/(p-1)\), and for any nonempty coordinate set \(B\), let \(m_{B,p}(x)\) be the unique scalar satisfying
\[
\sum_{i\in B}\operatorname{sgn}(x_i-m_{B,p}(x))
 |x_i-m_{B,p}(x)|^{p-1}=0.
\]
The map sending \(x_B\) to \(m_{B,p}(x)\mathbf1_B\) is called the block mean map.

## Proof

**1. A universal bound for each block.** Since the scalar objective is strictly convex, \(m_{B,p}\) is unique; coordinatewise monotonicity and translation covariance give \(|m_{B,p}(x)-m_{B,p}(z)|\le\|x-z\|_{\infty}\). Thus the scalar mean is locally Lipschitz. For blocks with at least two vertices, at a point where every residual \(r_i=x_i-m_{B,p}(x)\) is nonzero, implicit differentiation of the defining equation gives
\[
\frac{\partial m_{B,p}}{\partial x_i}=\alpha_i,
\qquad
\alpha_i=\frac{w_i}{\sum_{j\in B}w_j},
\qquad w_i=|r_i|^{p-2}.
\]
These points have full measure: the exceptional condition \(r_i=0\) is equivalent to the strictly monotone scalar equation \(\sum_{j\ne i}\operatorname{sgn}(x_j-x_i)|x_j-x_i|^{p-1}=0\), which defines a null set by slicing; the constant-vector line is also null for block size at least two. The derivative of the block mean map has induced \(\ell_p\) norm
\[
|B|^{1/p}\left(\sum_{i\in B}\alpha_i^q\right)^{1/q}.
\]
If \(1<p<2\), every nonnegative probability vector \(\alpha\) has \(\|\alpha\|_q\le1\), giving \(|B|^{1/p}\). If \(p=2\), all weights are equal and the derivative norm equals \(1\). For \(p>2\), select a residual of maximal modulus, say \(|r_k|\). The scalar optimality equation and subadditivity of the power \((p-2)/(p-1)\in(0,1)\) imply
\[
|r_k|^{p-2}
\le\left(\sum_{j\ne k}|r_j|^{p-1}\right)^{(p-2)/(p-1)}
\le\sum_{j\ne k}|r_j|^{p-2}.
\]
As every other weight is no larger than the maximal one, all \(\alpha_i\le 1/2\). Hence
\[
\sum_i\alpha_i^q\le(1/2)^{q-1}\sum_i\alpha_i=(1/2)^{q-1},
\]
so the derivative norm is at most \((|B|/2)^{1/p}\). Absolute continuity of the scalar mean along line segments, or the almost-everywhere derivative characterization of Lipschitz maps, converts each derivative bound to the same global bound. For blocks of cardinality two the unique scalar minimizer is the arithmetic mean, so the exact constant is \(1\); for singleton blocks it is also \(1\).

**2. Reduction of isotonic projection to finitely many block means.** By strict convexity and coercivity, \(\Pi_{G,p}\) exists uniquely and depends continuously on its input. Given its fit \(y=\Pi_{G,p}(x)\), form the undirected graph consisting only of edges \((u,v)\) for which \(y_u=y_v\). Its connected components are blocks \(B\). All inequalities across different blocks are strict. Consequently, varying the common fitted value of one block slightly in either direction is feasible, and optimality forces that fitted value to equal \(m_{B,p}(x_B)\). For every input, therefore, \(\Pi_{G,p}\) agrees with one of finitely many direct sums of block mean maps. Each such direct sum is globally \(L\)-Lipschitz with
\[
L=\max\{1,\ N^{1/p}\}\quad(1<p<2),\qquad
L=\max\{1,\ (N/2)^{1/p}\}\quad(p>2),
\]
with the improved \(L=1\) whenever \(N\le2\) and for \(p=2\).

We use the elementary finite-selection lemma: if a continuous map on a normed linear space agrees at every input with one of finitely many globally \(L\)-Lipschitz maps, then it is globally \(L\)-Lipschitz. Indeed, restrict to a line segment. At any point, a branch whose value differs there from the selected map cannot be selected at sufficiently nearby points, by continuity. Finiteness gives a neighborhood in which every potentially selected branch agrees at the center, hence \(\|f(t+h)-f(t)\|\le L|h|\) for sufficiently small \(h\) at every center \(t\). The standard upper-Dini-derivative mean-value lemma for continuous metric-valued curves then gives the global \(L\)-Lipschitz estimate on each segment. Applying this lemma proves the upper bound in the theorem.

**3. Full pooling is locally stable at strictly positive edge multipliers.** Work in a single weakly connected component of size \(n\ge3\). For each directed edge \(e=(u,v)\) put \(b_e=e_u-e_v\). The \(b_e\) span the zero-sum hyperplane \(H=\{g:\sum_i g_i=0\}\) because the underlying undirected graph is connected. Choose multipliers \(\lambda_e>0\) and set \(g=\sum_e\lambda_e b_e\). Let
\[
x_i=\operatorname{sgn}(g_i)|g_i|^{1/(p-1)}.
\]
Then \(\sum_i\operatorname{sgn}(x_i)|x_i|^{p-1}=\sum_i g_i=0\), so its scalar \(p\)-mean is zero. The Kuhn–Tucker stationarity equation at the identically zero feasible fit is exactly \(\operatorname{sgn}(x_i)|x_i|^{p-1}=g_i=\sum_e\lambda_e(b_e)_i\), with nonnegative multipliers. Convexity proves \(\Pi_{G,p}(x)=0\). Since every multiplier is positive, \(g\) lies in the relative interior of \(\operatorname{cone}\{b_e\}\) in \(H\). The map \(z\mapsto(\operatorname{sgn}(z_i-m_p(z))|z_i-m_p(z)|^{p-1})_i\) is continuous and takes values in \(H\). Thus in a neighborhood of \(x\) this vector remains in the normal cone, proving that full pooling persists: locally \(\Pi_{G,p}(z)=m_p(z)\mathbf1\). At a choice with every \(g_i\ne0\), its local derivative is therefore exactly the block mean derivative in Step 1.

**4. Every connected order realizes the upper constants.** For \(2<p<\infty\), choose any edge \(e_0\), put \(\lambda_{e_0}=1\), and assign all other edges distinct generic positive coefficients of order \(\varepsilon\). As \(\varepsilon\downarrow0\), the vector \(g\) tends to \(b_{e_0}\), and the derivative weights, up to normalization, tend to \((1,1,0,\ldots,0)\). The local Lipschitz norm tends to \((n/2)^{1/p}\). Accidental zero coordinates can be avoided by generic choices, because finitely many proper linear hyperplanes cannot exhaust the strictly positive multiplier orthant.

For \(1<p<2\), choose a vertex \(j\) that is not a cut vertex in the undirected graph. Such a vertex exists in every finite connected graph, for example an endpoint of a longest simple path. The induced graph on \(V\setminus\{j\}\) is connected, hence contains an edge \(e_0\). Assign multiplier \(1\) to \(e_0\), generic positive multipliers of order \(\varepsilon\) to all remaining edges not incident with \(j\), and generic positive multipliers of order \(\varepsilon^2\) to all edges incident with \(j\). The resulting coordinates of \(g\) are of order \(1\) at the two endpoints of \(e_0\), of order \(\varepsilon\) at all other vertices different from \(j\), and of order \(\varepsilon^2\) at \(j\); coefficients can be chosen to avoid cancellations. Since
\[
w_i=|g_i|^{(p-2)/(p-1)}
\]
and the exponent is negative, the normalized derivative weight vector converges to the single-atom vector \(e_j\). The local Lipschitz norm tends to \(n^{1/p}\). This proves sharpness for every connected order and all \(p\ne2\). The Euclidean projection is nonexpansive, while translation covariance makes its Lipschitz constant at least \(1\). For a disconnected graph, the problem decomposes into independent components and the Lipschitz norm is their maximum. The cases \(N\le2\) follow from the two-coordinate arithmetic mean calculation and the identity map. This completes the proof.

## Verification

A standalone reproducible `verify_isotonic.py` evaluates the full-pooling Kuhn–Tucker identities and derivative norms for path, star, and diamond orders, at \(p=3/2,3,4\), using only the Python standard library. For each graph and exponent, the diagnostic local derivative norms approach the asserted sharp upper bound along positive-multiplier families. These finite numerical checks are sanity tests; the continuum upper bound, arbitrary-graph sharpness, and the equality claims follow from the proof, not from sampling. To replay, run `python verify_isotonic.py`.

## Relationship to prior work

Németh and Németh (arXiv:1503.08458, first posted 29 March 2015) establish order-monotonicity properties of *Euclidean* metric projection for isotonic regression cones; their structural result does not give the best Lipschitz constant for the \(\ell_p\) metric projection for arbitrary connected orders. Kyng, Rao, and Sachdeva (arXiv:1507.00710, first posted 2 July 2015) obtain algorithms for arbitrary directed acyclic graphs and \(\ell_p\) objectives, rather than the exact perturbation modulus of the solution map. Berens–Finzel–Li–Xu (1997) and Finzel–Li (1998) establish broad qualitative Lipschitz regularity of best \(\ell_p\) approximation onto linear or polyhedral sets. The present result identifies a sharp, graph-independent constant and constructs matching graph-adapted data, which do not follow from those general existence statements alone. Yang and Barber (arXiv:1706.01852) study the **Euclidean least-squares** isotonic fit measured in alternate norms, a different operator from the non-Hilbert \(\ell_p\)-objective projection here.

## Limitations

The theorem is for unweighted, real finite-dimensional \(\ell_p\) regression on a fixed directed acyclic graph; it does not address weighted coordinates, complex-valued observations, nonconvex order constraints, or infinite graphs. The sharpness construction uses families of inputs and may not produce a single pair attaining the supremum. Numerical diagnostics cannot prove the universal assertion. The full original text of the 1998 polyhedral-projection paper was not available for direct comparison; its public abstract gives only qualitative Lipschitz regularity, so residual bibliographic overlap risk remains.

## References

1. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458v1 (29 March 2015), https://arxiv.org/abs/1503.08458.
2. R. Kyng, A. Rao and S. Sachdeva, *Fast, Provable Algorithms for Isotonic Regression in all \(\ell_p\)-norms*, arXiv:1507.00710v1 (2 July 2015), https://arxiv.org/abs/1507.00710.
3. M. Finzel and W. Li, *Uniform Lipschitz Continuity of Best \(\ell_p\)-Approximations by Polyhedral Sets*, Journal of Mathematical Analysis and Applications **228** (1998), 112–118, doi:10.1006/jmaa.1998.6120 (public abstract inspected).
4. H. Berens, M. Finzel, W. Li and Y. Xu, *Hoffman's Error Bounds and Uniform Lipschitz Continuity of Best \(\ell_p\)-Approximations*, Journal of Mathematical Analysis and Applications **213** (1997), 183–201, doi:10.1006/jmaa.1997.5521 (Theorem 1, pp. 186–187 inspected).
5. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (6 June 2017), https://arxiv.org/abs/1706.01852.
