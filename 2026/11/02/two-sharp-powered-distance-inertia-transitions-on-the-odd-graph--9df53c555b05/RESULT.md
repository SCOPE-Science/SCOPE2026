# Two sharp powered-distance inertia transitions on the odd graph \(KG(9,4)\)

## Finding

Let \(X\) be the \(126\) four-element subsets of \(\{1,\ldots,9\}\), with two vertices adjacent when their sets are disjoint. Equip the resulting odd graph \(KG(9,4)\) with its unweighted shortest-path metric \(d\). For every real \(p>0\), form the real symmetric \(126\)-by-\(126\) powered-distance matrix \(D_p=(d(S,T)^p)_{S,T\in X}\). The inertia convention is \((n_+,n_0,n_-)\).

There is a unique \(p_*\in(0,1/2)\) satisfying
\[
1-4\,2^{p_*}-4\,3^{p_*}+6\,4^{p_*}=0,
\qquad p_*=0.4095761090955705\ldots .
\]
The **complete** inertia of \(D_p\), for all \(p>0\), is

| Exponent | \((n_+,n_0,n_-)\) |
| :--- | :--- |
| \(0<p<p_*\) | \((1,0,125)\) |
| \(p=p_*\) | \((1,42,83)\) |
| \(p_*<p<1\) | \((43,0,83)\) |
| \(p=1\) | \((43,8,75)\) |
| \(p>1\) | \((51,0,75)\) |

In particular, the supremal generalized-roundness (equivalently, supremal negative-type) exponent of \((X,d)\) equals \(p_*\). The metric has strict \(p\)-negative type for \(0<p<p_*\), non-strict \(p_*\)-negative type, and fails \(p\)-negative type for every \(p>p_*\). At the critical exponent the complete zero-sum equality space is the \(42\)-dimensional adjacency eigenspace \(\ker(A-I)\), where \(A\) is the disjointness adjacency matrix. Consequently the least Euclidean dimension in which the snowflaked metric \(d^{p/2}\) embeds is exactly \(125\) for \(0<p<p_*\) and exactly \(83\) at \(p=p_*\).

The second spectral transition at \(p=1\) occurs in the distinct eight-dimensional adjacency eigenspace \(\ker(A+4I)\), although negative type has already failed there. Thus the sharp negative-type boundary and the later inertia jump involve different subset-harmonic modes.

## Assumptions and scope

All graph vertices are four-element subsets of a fixed nine-element set; the graph has an edge of length one precisely between disjoint subsets. There are no weights, additional vertices, or continuum limits. Here \(p>0\) is real, and \(d(S,S)^p=0\). The \(p\)-negative-type condition means \(a^{\mathsf T}D_pa\le0\) for **every** real coefficient vector \(a\in\mathbb R^{126}\) with \(\sum_{S\in X}a_S=0\). Strictness requires strict inequality unless \(a=0\).

The notation \(A_j\) denotes the distance-\(j\) relation matrix for \(j=0,1,2,3,4\); in particular \(A_0=I\) and \(A_1=A\). The positive, zero, and negative counts in inertia include multiplicity. Euclidean embedding dimensions are the dimensions of the affine spans of exact embeddings, not ambient dimensions imposed a priori.

## Proof

**1. Exact graph and adjacency spectrum.** For two four-subsets with \(h=|S\cap T|\), the distance is
\[
d(S,T)=\min\{2(4-h),\ 2h+1\}.
\]
Thus its distance classes correspond respectively to intersection sizes \(4,0,3,1,2\) and have valencies \(1,5,20,40,60\). Directly counting neighbors of a pair, or using the intersection array \(\{5,4,4,3;1,1,2,2\}\), gives
\[
\begin{aligned}
AA_1&=5A_0+A_2,\\
AA_2&=4A_1+2A_3,\\
AA_3&=4A_2+2A_4,\\
AA_4&=3A_3+3A_4.
\end{aligned}
\]
Consequently
\[
A_2=A^2-5I,\qquad
A_3=\frac{A^3-9A}{2},\qquad
A_4=\frac{A^4-17A^2+40I}{4}.
\]
The last recurrence yields
\[
(A-5I)(A+4I)(A-3I)(A+2I)(A-I)=0.
\]
The graph has no triangles and no quadrilaterals: the neighbor counts satisfy \(a_1=0\) and \(c_2=1\). It follows that the traces of \(A^j\), for \(j=0,1,2,3,4\), are \(126,0,630,0,5670\). Solving the five-by-five exact Vandermonde system gives the following distinct eigenvalues and multiplicities:
\[
\begin{array}{c|rrrrr}
\lambda&5&-4&3&-2&1\\\hline
\mathrm{mult}(\lambda)&1&8&27&48&42.
\end{array}
\]
This confirms completeness of the spectrum; the \(5\)-eigenspace consists of constants.

**2. Powered-distance eigenvalues.** Write \(u=2^p\), \(\alpha=\log_2 3\), so that \(u>1\), \(3^p=u^\alpha\), and \(4^p=u^2\). Since \(D_p=A_1+2^pA_2+3^pA_3+4^pA_4\), its eigenvalues on the five adjacency eigenspaces, in the order above, are
\[
\begin{array}{c|l}
5&5+20u+40u^\alpha+60u^2\\
-4&F(u):=-4+11u-14u^\alpha+6u^2\\
3&H(u):=3+4u-8u^2\\
-2&J(u):=-2-u+5u^\alpha-3u^2\\
1&G(u):=1-4u-4u^\alpha+6u^2.
\end{array}
\]
The constant-sector eigenvalue is always strictly positive. We now determine the sign of every other eigenvalue for **all** \(u>1\), not merely at sampled parameters.

**3. The first and second sign changes.** Elementary integer comparisons give
\[
\frac{11}{7}<\alpha<\frac85
\]
because \(3^7>2^{11}\) and \(3^5<2^8\). One has \(G(1)=-1\) and
\[
G(\sqrt2)=13-4(\sqrt2+\sqrt3)>0
\]
(the latter follows from \(\sqrt2<3/2\) and \(\sqrt3<7/4\)). Further,
\[
G'(u)=-4-4\alpha u^{\alpha-1}+12u,
\quad G''(u)=12-4\alpha(\alpha-1)u^{\alpha-2}>12-\frac{96}{25}>0
\]
for all \(u\ge1\). Since \(G'(1)=8-4\alpha>0\), the function \(G\) is strictly increasing and has exactly one root \(u_*\in(1,\sqrt2)\). Define \(p_*=\log_2u_*\). This proves the asserted root's existence, uniqueness, location, and all-time sign switch.

For \(u\ge1\), \(H(u)\le -1<0\). To show \(J(u)<0\), first consider \(1\le u\le2\). Weighted arithmetic--geometric mean gives
\[
u^\alpha\le(2-\alpha)u+(\alpha-1)u^2.
\]
Hence
\[
J(u)\le Q(u):=-2+(9-5\alpha)u+(5\alpha-8)u^2.
\]
The affine derivative \(Q'\) is positive at both endpoints: \(Q'(1)=5\alpha-7>0\) and \(Q'(2)=15\alpha-23>0\). Thus \(Q\) increases on this interval and \(J(u)\le Q(u)\le Q(2)=10\alpha-16<0\). For \(u\ge2\), one has \(p\ge1\). Convexity of \(x\mapsto x^p\) yields \(3^p\le(2^p+4^p)/2\), and therefore
\[
J(u)\le-2+\frac32u-\frac12u^2
=-\frac12\bigl((u-\tfrac32)^2+\tfrac74\bigr)<0.
\]

Finally, \(F(2)=0\). We show that \(F\) increases strictly on \([1,\infty)\). On \(1\le u\le2\), use \(\alpha<8/5\) and the concave tangent bound at \(u=4/3\):
\[
u^{3/5}\le(4/3)^{3/5}(2/5+9u/20)<\frac65(2/5+9u/20),
\]
where \((4/3)^{3/5}<6/5\) follows by raising to the fifth power. Consequently
\[
F'(u)=11+12u-14\alpha u^{\alpha-1}
>11+12u-\frac{672}{25}(2/5+9u/20)
=\frac{31-12u}{125}\ge\frac7{125}>0.
\]
For \(u\ge2\), the same bounds imply \(u^{\alpha-2}\le2^{-2/5}<4/5\); thus
\[
F''(u)=12-14\alpha(\alpha-1)u^{\alpha-2}
>12-\frac{1344}{125}>0.
\]
Since \(F'(2)>0\), the derivative remains positive for all \(u\ge2\). It follows that \(F(u)<0\) for \(1\le u<2\), \(F(2)=0\), and \(F(u)>0\) for \(u>2\), proving the isolated second transition at \(p=1\).

**4. Inertia, equality, and Euclidean dimension.** Combining the signs with the exact multiplicities \(1,8,27,48,42\) gives every row of the inertia table. In particular, on the orthogonal complement of constants, \(D_p\) is strictly negative definite for \(0<p<p_*\). At \(p=p_*\) its unique zero eigenvalue there is \(G(u_*)\), carried by the entire \(42\)-dimensional \(\lambda=1\) adjacency eigenspace. For \(p>p_*\), that eigenvalue is strictly positive, so \(p\)-negative type fails.

The centered Schoenberg Gram matrix is \(B_p=-\tfrac12P D_p P\), where \(P=I-\tfrac1{126}\mathbf1\mathbf1^{\mathsf T}\). It is positive semidefinite precisely for \(0<p\le p_*\), and its rank is \(125\) below \(p_*\) and \(83=125-42\) at \(p_*\). The squared Euclidean distances of its canonical Gram representation equal \(d(S,T)^p\), establishing the exact minimum embedding dimensions for \(d^{p/2}\). At \(p=1\), \(\ker D_1=\ker(A+4I)\) has dimension \(8\), distinct from the critical negative-type equality space.

## Verification

Run `python3 verify_odd5.py` using the Python standard library. It constructs all \(126\) vertices; independently checks \(15{,}876\) ordered graph distances by breadth-first search; verifies all \(79{,}380\) distance-matrix recurrence entries; reproduces the integer spectral multiplicities and exact first two powered-distance trace identities at three integer exponents; and calculates the displayed root as a diagnostic. The exact all-exponent sign claims are the analytic inequalities in the proof, **not** extrapolations from the numerical checks.

## Relationship to prior work

Schoenberg's negative-type/Euclidean criterion is the embedding foundation. Li--Weston (2009) establishes strictness below an endpoint and non-strictness at finite supremal negative type. Sánchez (2011) provides general finite-distance-matrix criteria, and Murugan (2011) gives a determinant characterization for vertex-transitive metrics. Aalipour and collaborators (2015) provide the Johnson-scheme setting, Kneser distance formula, and ordinary (first-power) graph distance spectrum. The present calculation applies that general spectral framework to *all real powers* in the first diameter-four odd graph, evaluates every scalar sign globally, and obtains the two exact inertia jumps and critical affine dimension. The relevant inspected source material does not state this evaluated all-\(p\) phase diagram; equivalent unindexed work remains possible.

## Limitations

The theorem concerns exactly the unweighted vertex shortest-path metric on \(KG(9,4)\). It does not claim a formula for larger odd graphs, general Kneser parameters, weighted edges, other graph products, or all finite distance-transitive metrics. The decimal root is illustrative; the defining equation and inequalities are exact. No independent scientific audit has been performed.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, first arXiv version 2009-01-06, arXiv:0901.0695, https://arxiv.org/abs/0901.0695.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, first arXiv version 2011-08-02, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
3. M. K. Murugan, *Generalized roundness of vertex transitive graphs*, first arXiv version 2011-12-23, arXiv:1112.5657, https://arxiv.org/abs/1112.5657.
4. G. Aalipour et al., *On the distance spectra of graphs*, first arXiv version 2015-09-03, arXiv:1509.01196, https://arxiv.org/abs/1509.01196.
