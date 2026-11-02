# Exact Hilbert distortion of complete-graph subdivisions

## Finding

For an integer \(n\geq 2\), let \(S(K_n)\) be the graph obtained by replacing every edge of the complete graph \(K_n\) by a path with two unit-length edges. Let \(d\) be its unweighted shortest-path metric, and let \(c_2(S(K_n))\) be the least bi-Lipschitz distortion of its vertex metric in a real Hilbert space, with no a priori restriction on the target dimension. Then

\[
\boxed{c_2(S(K_n))^2=\begin{cases}
1,&n=2,\\
9/4,&n=3,\\
(43-8\sqrt{19})/3,&n=4,\\
4(n-2)/(n-1),&n\geq5.
\end{cases}}
\]

Thus the genuine subdivision family \(n\geq4\) has an exceptional algebraic value at \(n=4\), while the exact squared distortion is \(4-4/(n-1)\) for every \(n\geq5\). The optimal distortion increases strictly from \(n=4\) onward and tends to \(2\). Explicit optimal embeddings lie in \(\mathbb R^{n-1}\). The \(n=2\) path and \(n=3\) six-cycle are included as familiar boundaries; the new assertion is the exact classification for \(n\geq4\).

## Assumptions and scope

The vertices of \(S(K_n)\) are indexed by singleton sets \(\{i\}\) and two-element sets \(\{i,j\}\) in \([n]\); adjacency is set inclusion between a singleton and a two-element set. For these two Boolean layers, graph distance equals Hamming distance \(d(U,V)=|U\triangle V|\). The five possible pair classes have distances: distinct singleton–singleton, \(2\); incident singleton–doubleton, \(1\); nonincident singleton–doubleton, \(3\); doubletons sharing one element, \(2\); disjoint doubletons, \(4\) (the last class occurs only for \(n\geq4\)). The lower bound follows from arbitrary, possibly nonsymmetric, real Hilbert embeddings. The graph is not assumed to be distance-regular.

We use the normalization that an embedding \(f\) with squared distortion at most \(t\) may be rescaled so that
\[
d(U,V)^2\leq\|f(U)-f(V)\|^2\leq t\,d(U,V)^2
\]
for every two distinct vertices. Optimizing such \(t\) is equivalent to computing \(c_2^2\).

## Proof

**1. Symmetry reduction.** Average the Gram matrix of any candidate embedding over the coordinate-permutation group \(S_n\). Positive semidefiniteness is preserved, as are the preceding linear distance inequalities. Therefore all squared distances in a lower-bound argument may be assumed invariant under \(S_n\).

Put \(m=\binom n2\), \(u_i=e_i-n^{-1}\mathbf 1\in\mathbb R^n\), and \(q_{ij}=u_i+u_j\). Let \(\mathcal I:\mathbb R^m\to\mathbb R^n\) be the unsigned vertex–edge incidence matrix. Its relation \(\mathcal I\mathcal I^\top=(n-2)I+\mathbf1\mathbf1^\top\) shows that the real permutation module on doubletons decomposes orthogonally into a constant space, a standard component represented by \(q_{ij}\), and an additional component represented by
\[
w_{ij}=e_{ij}-m^{-1}\mathbf1_E-(n-2)^{-1}\mathcal I^\top q_{ij}.
\]
For \(n=3\), the additional component is zero. The standard module and additional component are inequivalent irreducible real permutation representations for \(n\geq4\). Consequently every invariant squared Euclidean distance structure on these two orbits is described by \(A,B,D,T\geq0\) and \(C\in\mathbb R\), with \(C^2\leq AB\): the singleton standard covariance is \(A\langle u_i,u_j\rangle\), the doubleton standard covariance is \(B\langle q_{ij},q_{kl}\rangle\), their cross covariance is \(C\langle u_i,q_{jk}\rangle\), the additional covariance is \(D\langle w_{ij},w_{kl}\rangle\), and \(T\) is the squared distance of the two orbit centroids. One may take \(D=0\) when \(n=3\).

Writing \(\delta_I\) and \(\delta_N\) for squared distances from a singleton to an incident or nonincident doubleton, and \(\delta_{DD}\) for the squared distance of disjoint doubletons, the complete distance formulas are
\[
\begin{aligned}
\delta_{SS}&=2A,\\
\delta_I&=T+\frac{(n-1)A+2(n-2)B-2(n-2)C}{n}+\frac{n-3}{n-1}D,\\
\delta_N&=\delta_I+2C,\\
\delta_{DS}&=2B+\frac{2(n-3)}{n-2}D,\\
\delta_{DD}&=4B+\frac{2(n-4)}{n-2}D\qquad(n\geq4).
\end{aligned}
\]
Here \(\delta_{DS}\) refers to doubletons sharing one element. These follow from \(\|u_i-u_j\|^2=2\), \(\|q_{ij}-q_{kl}\|^2=2\) or \(4\), and \(\|w_{ij}-w_{kl}\|^2=2-\|q_{ij}-q_{kl}\|^2/(n-2)\).

**2. Uniform lower bound for \(n\geq5\).** Cauchy–Schwarz and \(C^2\leq AB\) yield the completed-square inequality
\[
\delta_I\geq\frac{n-2}{n-1}B+\frac{n-3}{n-1}D+T.
\]
Comparison with the disjoint-doubleton distance then gives the explicit nonnegative remainder
\[
\delta_I-\frac{n-2}{4(n-1)}\delta_{DD}
\geq\frac{n-2}{2(n-1)}D+T\geq0.
\]
For a noncontracting embedding, \(\delta_{DD}\geq4^2=16\), while \(\delta_I\leq t\cdot1^2=t\). Hence \(t\geq4(n-2)/(n-1)\).

**3. Exceptional lower bound for \(n=4\).** Here \(\delta_{DD}=4B\), so \(B\geq4\), while
\[
\delta_I=\tfrac34A+B-C+\tfrac13D+T,
\quad \delta_N=\delta_I+2C\geq9.
\]
If the squared distortion is at most \(t\), then \(\delta_I\leq t\) and \(C\geq(9-t)/2\). Since \(A\geq C^2/B\),
\[
\delta_I\geq B-C+\frac{3C^2}{4B}
\geq M(C):=\begin{cases}
4-C+3C^2/16,&0\leq C\leq8/\sqrt3,\\
(\sqrt3-1)C,&C\geq8/\sqrt3.
\end{cases}
\]
The last expression is the exact minimum over \(B\geq4\). Set \(C_*=(4\sqrt{19}-8)/3\) and \(t_*=9-2C_*=(43-8\sqrt{19})/3\). Direct substitution shows \(8/3<C_*<8/\sqrt3\) and \(M(C_*)=t_*\). The function \(M\) is strictly increasing on \([C_*,\infty)\). Assuming \(t<t_*\) would force \(C>(9-t_*)/2=C_*\), hence \(t\geq\delta_I\geq M(C)>t_*\), a contradiction.

**4. Lower bound for \(n=3\).** The additional module vanishes, so \(\delta_I=2(A+B-C)/3+T\geq2C/3\) from \(A+B\geq2C\). The nonincident inequality gives \(C\geq(9-t)/2\). Thus \(t\geq(9-t)/3\), or \(t\geq9/4\). The case \(n=2\) is a three-vertex path, isometric to three collinear points.

**5. Matching embeddings.** For \(n\geq3\), use the centered coordinate vectors \(u_i\), \(q_{ij}\) above and define \(f(\{i\})=\alpha u_i\), \(f(\{i,j\})=\beta q_{ij}\), with
\[
(\alpha,\beta)=\begin{cases}
(\sqrt{27/8},\sqrt{27/8}),&n=3,\\
((2\sqrt{19}-4)/3,2),&n=4,\\
(2(n-2)/(n-1),2),&n\geq5.
\end{cases}
\]
For \(n\geq5\), putting \(k=(n-2)/(n-1)\), the five ratios of squared Euclidean distance to squared graph distance, ordered as in the scope paragraph, are
\[
2k^2,\quad4k,\quad\frac{4k}{3},\quad2,\quad1.
\]
Their minimum is \(1\) and maximum is \(4k\) for every \(n\geq5\). At \(n=4\), put \(C_*=(4\sqrt{19}-8)/3\). The ratios are \(C_*^2/8\), \(t_*\), \(1\), \(2\), \(1\); the identity \(3C_*^2+16C_*-80=0\) proves that the incident ratio is exactly \(t_*\). Their minimum and maximum are \(1\) and \(t_*\). At \(n=3\) the four existing pair classes have ratios \(27/16\), \(9/4\), \(1\), \(27/16\). This completes the upper bounds and proves the formula in every dimension.

## Verification

The standalone Python 3 script `verify_distortion.py` uses only the standard library. It checks all pairwise squared-distance inequalities in exact rational arithmetic for \(3\leq n\leq11\), including exact arithmetic in \(\mathbb Q(\sqrt{19})\) at \(n=4\); it also checks graph shortest-path distances against Hamming distances by breadth-first search for \(3\leq n\leq10\). Successful replay returns `CHECK_OK orders=3..11 pairwise_exact_inequalities= 12006 bfs_orders=3..10 algebraic_n4=Q(sqrt(19))`. These finite checks do not establish the quantified lower bounds: those follow from the invariant Gram decomposition and inequalities proved above.

## Relationship to prior work

The 2021 work of Cioabă, Gupta, Ihringer, and Kurihara studies sharp Euclidean distortion for distance-regular graphs. The present subdivided complete graph has two different vertex degrees for \(n\geq4\), so their distance-regular theorem does not apply. Earlier results of Vallentin on Hamming and Johnson graphs determine distortions of the complete ambient graphs, not the optimal distortion of this selected two-layer submetric. Doust and Wolf's 2021 preprint studies distance matrices, negative type, and an \(M\)-constant for subsets of the Hamming cube rather than least Euclidean distortion. Beaudou, Gravier, and Meslem identified isometric Hamming embeddings of subdivided complete graphs; that is a statement about distortion into the Hamming metric, not the sharp distortion into Hilbert space. The latter paper's full text was not available for complete verification, so historical coverage beyond its stated Hamming-embedding classification remains a residual risk. The exceptional six-cycle value agrees with previously known cycle-distortion theory and is not independently novel.

## Limitations

All edges have unit length and the target is a real Hilbert space of unrestricted finite dimension. The result does not address nonuniform subdivisions, weighted graph metrics, or embeddings into other \(\ell_p\) targets. The optimal embeddings displayed above need not be unique. The study does not claim a novelty certification or an independent audit; identification of equivalent older formulations may require further historical review.

## References

1. S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708, first posted 2021-09-20, https://arxiv.org/abs/2109.09708.
2. I. Doust, R. Wolf, *A problem on distance matrices of subsets of the Hamming cube*, arXiv:2109.07052, first posted 2021-09-15, https://arxiv.org/abs/2109.07052.
3. L. Beaudou, S. Gravier, K. Meslem, *Isometric Embeddings of Subdivided Complete Graphs in the Hypercube*, SIAM Journal on Discrete Mathematics **22** (2008), 1226–1238, https://doi.org/10.1137/070681909.
