# A sharp bandwidth phase transition for Kneser pair-metric exponential kernels

## Finding
For every integer \(n\geq5\), let \(X_n\) consist of the two-element subsets of \(\{1,\ldots,n\}\), equipped with shortest-path distance \(d\) in the Kneser graph \(KG(n,2)\): distinct disjoint pairs have distance one, and distinct intersecting pairs have distance two. For real \(p,t>0\), form the real symmetric exponential distance-power kernel
\[
K_{n,p}(t)_{S,T}=\exp(-t\,d(S,T)^p),\qquad S,T\in X_n.
\]
Put \(N=\binom n2\), \(m=n-4\), \(x=2^p\) and \(p_*(n)=\log_2((n-3)/(n-4))\). The complete positive-definiteness phase diagram is:

1. For \(0<p\leq p_*(n)\), \(K_{n,p}(t)\) is **positive definite at every \(t>0\)**.
2. For \(p>p_*(n)\), there is exactly one \(t_c(n,p)\in(0,\log(n-3))\) satisfying
\[
1-(n-3)e^{-t_c}+(n-4)e^{-2^pt_c}=0.
\]
For \(0<t<t_c\), the matrix is indefinite with exactly \(n-1\) negative eigenvalues; at \(t=t_c\), it is positive semidefinite of rank \(N-n+1\) and kernel dimension \(n-1\); and for \(t>t_c\), it is positive definite. The threshold \(t_c(n,p)\) increases strictly with \(p\), from zero as \(p\downarrow p_*(n)\) to \(\log(n-3)\) as \(p\to\infty\). At \(t=0\), for every \(p\), the limiting matrix is the rank-one all-ones matrix; this endpoint is excluded from the positive-time classifications.

There is also a universal sharp **critical window**. Fix any real \(c>1\); for each \(n\ge5\) set \(p_n(c)=\log_2(1+c/(n-4))\) and \(t_n(c)=t_c(n,p_n(c))\). Then \(t_n(c)\) increases strictly in \(n\) and converges to the unique positive solution \(T(c)\) of
\[
e^{T(c)}=1+cT(c).
\]
The first finite-size correction is
\[
T(c)-t_n(c)=\frac{c^2T(c)^2}{2(n-4)[1+cT(c)-c]}+O_c((n-4)^{-2}).
\]
In the explicit \(c=2\) window, \(t_5(2)=\log((1+\sqrt5)/2)\), \(t_6(2)=\log2\), and \(T(2)\approx1.256431208626169\).

## Assumptions and scope
The graph is precisely \(KG(n,2)\) with \(n\ge5\), unit edge lengths and the induced unweighted vertex metric. The finite matrix is indexed by **unordered** two-element subsets; all coefficients are real. The kernel is \(\exp(-t d^p)\) without any unstated factor of two, and both \(p\) and \(t\) range over positive real numbers. Positive definite means that the quadratic form is strictly positive on every nonzero real vector; positive semidefinite allows a nontrivial kernel. The matrices considered are neither heat kernels nor graph-Laplacian semigroups.

The theorem is about the **whole** matrix for each fixed bandwidth, not merely a test of conditionally negative type or the existence of some positive bandwidth. No assertion is made for general \(KG(n,k)\) when \(k>2\), normalized graph distances, or arbitrary two-distance metric spaces.

## Proof
**The graph metric and its three invariant sectors.** Two distinct pairs are adjacent exactly when disjoint. If they intersect, their union has three elements; since \(n\ge5\), one can choose a pair disjoint from both, proving distance two. Let \(A\) be the adjacency matrix of \(KG(n,2)\), \(J\) the \(N\)-by-\(N\) all-ones matrix and \(B\) the \(n\)-by-\(N\) unoriented vertex–pair incidence matrix, \(B_{i,S}=\mathbf1_{\{i\in S\}}\). Direct counting gives
\[
BB^{\mathsf T}=(n-2)I_n+J_n,\qquad
A=J+I-B^{\mathsf T}B.
\]
The first identity is strictly positive definite, so \(B\) has row rank \(n\). We have the mutually orthogonal decomposition
\[
\mathbb R^{X_n}=\operatorname{span}\{\mathbf1\}\oplus U\oplus W,
\]
where
\[
U=\{(a_i+a_j)_{\{i,j\}}:\sum_i a_i=0\},\quad
W=\{w:\sum_{S\ni i}w_S=0\text{ for every }i\}.
\]
Its component dimensions are respectively \(1,n-1,N-n\). On these sectors the adjacency eigenvalues are respectively
\[
k=\binom{n-2}{2},\qquad -(n-3),\qquad 1.
\]
Indeed, \(B^{\mathsf T}a\in U\) for \(\sum_i a_i=0\), \(B B^{\mathsf T}a=(n-2)a\); and \(W=\ker B\), on which \(J\) vanishes. The constant vector is a regular-graph eigenvector of degree \(k\).

**Exact kernel spectrum.** Let \(a=e^{-t}\), \(b=e^{-xt}\) with \(x=2^p>1\). Every diagonal entry of \(K\) equals one; entries on adjacent pairs equal \(a\), and other off-diagonal entries equal \(b\). Consequently
\[
K=(1-b)I+(a-b)A+bJ.
\]
Its full eigenvalue table, with multiplicities, is
\[
\begin{array}{c|c|c}
\text{sector}&\text{eigenvalue}&\text{multiplicity}\\ \hline
\mathbf1&1+k e^{-t}+(N-1-k)e^{-xt}&1\\
U&F_{m,x}(t)=1-(m+1)e^{-t}+m e^{-xt}&n-1\\
W&1+e^{-t}-2e^{-xt}&N-n
\end{array}
\]
The constant-sector eigenvalue is positive since every summand is nonnegative. For \(t>0\), the \(W\)-sector eigenvalue is strictly positive because \(e^{-xt}<e^{-t}<1\) implies \(1+e^{-t}-2e^{-xt}>1-e^{-t}>0\). Thus all nonpositive directions, if any, belong exactly to \(U\).

**One and only one finite-bandwidth transition.** The remaining scalar satisfies \(F_{m,x}(0)=0\) and
\[
F'_{m,x}(t)=e^{-t}\bigl[(m+1)-mx e^{-(x-1)t}\bigr].
\]
If \(1<x<(m+1)/m\), its bracket is positive at zero and strictly increases in \(t\), so \(F>0\) for all positive \(t\). At the endpoint \(x=(m+1)/m\), the bracket vanishes at zero and is strictly positive for \(t>0\), again yielding \(F>0\). If \(x>(m+1)/m\), the bracket starts negative, crosses zero exactly once, and then stays positive. Hence \(F\) decreases strictly from zero to one negative minimum and increases strictly to its limit one, crossing zero at one and only one positive time. At \(t=\log(m+1)\), \(F=m\exp(-x\log(m+1))>0\), locating the root in the claimed interval. This also proves all inertia and rank statements and explicitly identifies the nullspace \(U\) at the transition.

At the positive root \(F_t>0\). The partial derivative \(\partial F/\partial x=-mt e^{-xt}<0\) therefore gives strict increase of the root with \(x\), hence with \(p\). The root tends to zero when \(x\downarrow(m+1)/m\), since at the critical endpoint \(F(t)>0\) for all \(t>0\). As \(x\to\infty\), \(F\) converges uniformly on every compact positive-time interval to \(1-(m+1)e^{-t}\); the sole positive root consequently converges to \(\log(m+1)\).

**Critical-window theorem and correction.** Fix \(c>1\), write \(m=n-4\) and insert \(x=1+c/m\). The root equation is equivalently
\[
e^t=1+m(1-e^{-ct/m}).
\]
For each \(t>0\), the function \(m\mapsto m(1-e^{-ct/m})\) is strictly increasing for positive real \(m\): differentiate and use \(1-(1+u)e^{-u}>0\) for \(u>0\). It increases to \(ct\). Thus the root at integer \(m\) strictly increases with \(m\); it lies below the unique positive root \(T\) of \(e^T=1+cT\), whose existence and uniqueness follow from strict convexity of \(e^t-1-ct\), its negative derivative \(1-c\) at zero, and its limit \(+\infty\). Compactness and uniform convergence on bounded intervals prove \(t_m\uparrow T\).

For the next term, Taylor's formula, uniformly for \(t\) near \(T\), gives
\[
m(1-e^{-ct/m})=ct-\frac{c^2t^2}{2m}+O_c(m^{-2}).
\]
Let \(G(t)=e^t-1-ct\). Its derivative at the positive root is \(G'(T)=e^T-c=1+cT-c>0\). Inserting the expansion into the exact root equation and applying the mean-value theorem first shows \(T-t_m=O_c(m^{-1})\); a second Taylor expansion yields
\[
T-t_m=\frac{c^2T^2}{2m(1+cT-c)}+O_c(m^{-2}),
\]
with no unproved interchange of limits. For \(c=2,m=1\), the polynomial in \(e^{-t}\) factors as \(1-2z+z^3=(1-z)(1-z-z^2)\), giving \(t_5(2)=\log((1+\sqrt5)/2)\). For \(c=2,m=2\), it factors as \(1-3z+2z^2=(1-z)(1-2z)\), giving \(t_6(2)=\log2\).

**Related negative-type boundary (not the claimed new kernel phenomenon).** The powered-distance matrix is \(D_p=(1-x)A+x(J-I)\), whose eigenvalues on the zero-sum sectors \(U\) and \(W\) are respectively \(mx-(m+1)\) and \(1-2x\). Therefore the metric has \(p\)-negative type exactly for \(p\le p_*(n)\). The centered Schoenberg Gram matrix for the Euclidean snowflake \(d^{p/2}\) has dimension \(N-1\) for \(p<p_*(n)\) and \(N-n\) at equality. This is included to make the boundary transparent; the novel target is the full finite-bandwidth positive-definiteness and critical-window analysis, not the routine recovery of a negative-type threshold from the known Johnson/Kneser eigenspaces.

## Verification
The accompanying standalone Python 3 script `VERIFY_KERNEL.py` constructs every \(KG(n,2)\) for \(5\le n\le11\). Exact integer and rational checks establish the incidence identity, the adjacency decomposition, the \(U\)- and \(W\)-sector eigenvectors, and several powered-distance identities. Independent full-matrix exponential-kernel calculations check both nonconstant spectral eigenvalues at five power parameters and four positive times per graph. Further numeric root checks cover \(5\le n\le16\), the exact golden-ratio and binary-logarithm cases, and the first-order critical-window approximation. It requires no third-party packages and was executed successfully.

The uniform claims for all integers \(n\ge5\), all real \(p,t>0\) and every \(c>1\) rest on the preceding exact identities and scalar analysis, **not** on interpolation from these finite tests. The floating-point part of the checker is diagnostic rather than a formal interval certificate.

## Relationship to prior work
Schoenberg's classical correspondence between conditionally negative distances and positive definiteness at **all** exponential scales, as presented by Meckes (2010, Theorem 3.3), accounts for the all-bandwidth half of the first statement but does not provide the exact exceptional-bandwidth interval, the unique transition, inertia, monotonicity or finite-size scaling. The complete Kneser distance spectra and common Johnson-scheme eigenspaces are already covered by Aalipour and coauthors (2015, Theorems 3.9–3.10). They supply a strong structural antecedent to the present three-sector reduction; no originality is asserted for those eigenvalues or for the immediate negative-type corollary. Sánchez (2011) supplies finite-metric negative-type criteria, and Feragen–Lauze–Hauberg (2014) explains the general role of exponential-kernel bandwidth and the all-scale distinction. The mathematical addition here is an explicitly sharp, scale-resolved kernel phase diagram and its increasing critical-window law, not an independent method of simultaneous diagonalization.

## Limitations
This is a two-distance Kneser **pair** graph result, not a theorem for general Kneser graphs, Johnson graphs, or general two-distance metrics. The sharp transition is for the full real Gram matrix; finite tests alone cannot establish indefinite behavior for an unbounded parameter range. The asymptotic expansion assumes a fixed \(c>1\); it is not claimed to be uniform as \(c\downarrow1\) or as \(c\to\infty\). Publication-priority uncertainty remains because an equivalent statement might appear in specialized association-scheme or kernel literature; the spectral ingredients are classical and the present consequence is algebraically accessible.

## References
1. M. W. Meckes, *Positive definite metric spaces*, arXiv:1012.5863 (first posted 2010-12-29), especially Theorem 3.3. https://arxiv.org/abs/1012.5863
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first posted 2011-08-02). https://arxiv.org/abs/1108.0451
3. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first posted 2015-09-03), especially Theorems 3.9–3.10. https://arxiv.org/abs/1509.01196
4. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (first posted 2014-11-02). https://arxiv.org/abs/1411.0296
5. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44** (1938), 522–536 (classical all-scale theorem).
