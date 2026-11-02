# A three-regime roundness transition in five-cycle cluster metrics

## Finding

Let \(m\ge 2\) be an integer, let \(0<s\le 2\), and partition \(5m\) points into five labelled clusters \(X_0,\ldots,X_4\), each of size \(m\). Distinct points in the same cluster have distance \(s\); points in clusters whose labels are adjacent in the five-cycle have distance \(1\); and points in the other pair of distinct clusters have distance \(2\). This is a metric, denoted \(X_{m,s}\). Its endpoints \(s=1\) and \(s=2\) are the shortest-path metrics of, respectively, the lexicographic clique and independent-set blow-ups of the five-cycle.

Put
\[
 a=\frac{\sqrt5-1}{2},\qquad b=\frac{\sqrt5+1}{2}=1+a,\qquad ab=1.
\]
The supremal exponent \(\wp_m(s)\) for which \(X_{m,s}\) has \(p\)-negative type is the **unique positive solution** of
\[
 \boxed{\ m a\,2^{p}+(m-1)s^{p}=m b.\ }
\]
Negative type is strict for \(0\le p<\wp_m(s)\), holds non-strictly at the endpoint, and fails for all \(p>\wp_m(s)\). The nullspace of the powered-distance form on zero-sum vectors at the endpoint has dimension exactly \(2\); hence the minimum Euclidean dimension of the snowflake \((X_{m,s},d^{p/2})\) is \(5m-1\) for \(0<p<\wp_m(s)\), and \(5m-3\) at \(p=\wp_m(s)\).

Define the critical intracluster distance
\[
 s_c=2^{-a}=\exp(-a\log 2).
\]
There are **three different asymptotic regimes** as \(m\to\infty\), with \(s\) fixed:

1. If \(0<s<s_c\), let \(p_\infty(s)>0\) be the unique positive root of \(a2^p+s^p=b\). Then
   \[
   \boxed{\ \wp_m(s)\longrightarrow p_\infty(s)>0,\quad
   m\bigl(\wp_m(s)-p_\infty(s)\bigr)\longrightarrow
   \frac{s^{p_\infty(s)}}{a(\log2)2^{p_\infty(s)}+(\log s)s^{p_\infty(s)}}.\ }
   \]
2. At \(s=s_c\), the limiting root is tangent at zero and
   \[
   \boxed{\ \sqrt m\,\wp_m(s_c)\longrightarrow\frac{\sqrt2}{\log2}.\ }
   \]
3. If \(s_c<s\le2\), then
   \[
   \boxed{\ m\,\wp_m(s)\longrightarrow\frac1{a\log2+\log s}.\ }
   \]

In particular, the graph-metric endpoints have closed forms
\[
 \wp_m(1)=\log_2\left(1+\frac1{ma}\right),\qquad
 \wp_m(2)=\log_2\left(\frac{mb}{mb-1}\right).
\]
An additional exact boundary at exponent \(1\) is
\[
 \boxed{\ X_{m,s}\text{ has }1\text{-negative type}\ \Longleftrightarrow\
 s\le\frac{m}{m-1}\,a^2.\ }
\]

## Assumptions and scope

The clusters are labelled cyclically modulo \(5\), with every cluster containing \(m\) distinct points. For \(i\ne j\), distances between clusters are the ordinary five-cycle distances \(\min(|i-j|,5-|i-j|)\in\{1,2\}\). Distances between different points of the same cluster equal \(s\). The restriction \(0<s\le2\) ensures the triangle inequality, since the only new potential obstruction comes from two unit edges joining a pair of points in the same cluster via a neighbouring cluster. These distances are realized by a complete weighted graph within each cluster (edge length \(s\)), with complete unit-weight links between successive clusters, taking shortest paths.

For \(p\ge0\), the metric has \(p\)-negative type when
\[
 \sum_{x,y\in X_{m,s}}\alpha_x\alpha_y d(x,y)^p\le0
 \quad\text{for every real }(\alpha_x)\text{ with }\sum_x\alpha_x=0,
\]
where the zeroth power of each positive distance is \(1\). Strict negative type means strict inequality for every nonzero such vector. The powered metric \(d^{p/2}\) is a Euclidean metric exactly when the original metric has \(p\)-negative type; its minimum Euclidean embedding dimension is the rank of the centered Gram matrix \(-\tfrac12JD_pJ\), with \(J\) the orthogonal projection onto the zero-sum subspace.

## Proof

**1. Entire powered-distance spectrum.** Let \(D_p\) be the \(5m\)-by-\(5m\) matrix with entries \(d(x,y)^p\), and let \(B_p\) be the five-cycle powered-distance matrix: its diagonal entries are \(0\), its entries at cyclic separation \(1\) equal \(1\), and those at separation \(2\) equal \(2^p\). With \(J_m\) the all-ones matrix, the exact tensor identity is
\[
 D_p=B_p\otimes J_m+s^p I_5\otimes(J_m-I_m).
\]
Vectors that sum to zero within every cluster are eigenvectors with eigenvalue \(-s^p\), giving multiplicity \(5(m-1)\). The remaining vectors are constant on each cluster. Fourier diagonalization of the five-cycle gives their eigenvalues as follows:
\[
 \begin{aligned}
 E_0(p)&=2m(1+2^p)+(m-1)s^p &&\text{(constant vector; multiplicity 1)},\\
 E_1(p)&=m(a-b2^p)+(m-1)s^p &&\text{(frequencies }\pm1;\text{ multiplicity 2)},\\
 E_2(p)&=m(-b+a2^p)+(m-1)s^p &&\text{(frequencies }\pm2;\text{ multiplicity 2)}.
 \end{aligned}
\]
The cosine identities used here are \(2\cos(2\pi/5)=a\), \(2\cos(4\pi/5)=-b\), and \(2\cos(8\pi/5)=a\). Only \(E_0\) lies outside the zero-sum subspace, and it is strictly positive.

**2. Exactly one obstruction.** Because \(0<s\le2\),
\[
 E_1(p)\le ma-mb2^p+(m-1)2^p
 =ma-(ma+1)2^p\le-1
 \quad(p\ge0).
\]
The zero-sum spectrum is therefore negative except possibly for \(E_2\). Now
\[
 E_2(0)=-1,\qquad
 E_2''(p)=ma(\log2)^2 2^p+(m-1)(\log s)^2 s^p>0.
\]
Also \(E_2(p)\to\infty\) as \(p\to\infty\). Strict convexity, its negative value at zero, and eventual positivity imply that \(E_2\) crosses zero exactly once on \((0,\infty)\), from negative to positive. Rearranging \(E_2(p)=0\) gives the boxed equation. For any \(p\) below the unique root all eigenvalues on the zero-sum subspace are strictly negative. At the root only the two real Fourier vectors of frequencies \(\pm2\) become null; above it their eigenvalues are positive. This establishes all quantifiers in the classification without an enumeration assumption.

The centered powered-distance Gram matrix equals \(-\tfrac12JD_pJ\). It is positive definite on its \(5m-1\)-dimensional zero-sum subspace before the threshold, and at the threshold it has a two-dimensional nullspace there. This gives the claimed minimum embedding dimensions. The formula at \(p=1\) follows by substituting \(2^1=2\) into \(E_2(1)\le0\), using \(b-2a=a^2\).

**3. Why the branching transition is sharp.** Define
\[
 h_s(p)=a(2^p-1)+(s^p-1)=a2^p+s^p-b.
\]
The critical-root equation is equivalently
\[
 m h_s(\wp_m(s))=s^{\wp_m(s)}.
\]
Here \(h_s(0)=0\),
\[
 h_s'(0)=a\log2+\log s,
 \qquad h_s''(p)=a(\log2)^2 2^p+(\log s)^2s^p>0.
\]
The sign of the initial slope changes precisely at \(s=s_c\). If \(s<s_c\), strict convexity and \(h_s(p)\to\infty\) give a unique positive zero \(p_\infty(s)\) besides the zero at the origin, and \(h_s'(p_\infty(s))>0\). The finite-size root is beyond this positive zero, tends to it, and expansion of \(m h_s(p)=s^p\) at that simple root proves the displayed first-order correction.

If \(s>s_c\), strict convexity and positive initial derivative show the only nonnegative zero of \(h_s\) is \(0\). Therefore \(\wp_m(s)\to0\). The expansions \(h_s(p)=(a\log2+\log s)p+O(p^2)\) and \(s^p=1+O(p)\) yield \(m\wp_m(s)\to(a\log2+\log s)^{-1}\).

At \(s=s_c\), the linear term vanishes. Since \(a(1+a)=ab=1\),
\[
 h_{s_c}(p)=\frac{(\log2)^2}{2}p^2+O(p^3),
 \qquad s_c^p=1+O(p).
\]
Consequently \(m(\log2)^2\wp_m(s_c)^2/2\to1\), proving the inverse-square-root law. These Taylor expansions have legitimate remainder terms because all exponentials are analytic near the relevant roots. Finally \(s=1\) and \(s=2\) reduce the defining equation to elementary linear equations in \(2^p\), yielding both endpoint formulas.

## Verification

Run `python verify_five_cluster.py` with Python 3.10 or newer and NumPy 2.x; `requirements.txt` records the tested dependency. The checker constructs the full powered-distance matrix independently of the tensor formula and compares its full spectrum with the predicted multiplicities for \(210\) parameter configurations. It verifies \(725\) exact rational quadratic-form decompositions, \(48\) sharp-threshold and critical-rank configurations, both graph-metric endpoint identities, and all three asymptotic regimes. The test results are recorded in `VERIFICATION.md`. The proof of the universal statements is the algebraic Fourier decomposition and convexity/Taylor argument above; numerical sampling is only corroboration.

## Relationship to prior work

Sánchez [2], Example 2.8, already evaluates the supremal negative-type exponent of the ordinary five-cycle as \(\log_2((3+\sqrt5)/2)\), precisely the limiting collapsed-cluster value, and also establishes a general distance-matrix criterion. Murugan [3], Theorem 3.1, gives a general spectral-determinant criterion for row-permutation metric spaces such as these vertex-transitive cluster metrics. Li and Weston [1] provide a general strict-negative-type inheritance principle. Weston [4] supplies cardinality/diameter-based lower bounds. None of these inspected results evaluates this five-cluster family for all \(m,s\), the triple critical asymptotic scaling, or its two-mode critical Euclidean rank. The spectral methodology and the ordinary five-cycle endpoint are prior mathematical input, not claimed as new.

The result has particular significance because both graph-metric endpoints of the family have an exponent of order \(m^{-1}\), whereas sufficiently short but positive intracluster distances yield an exponent bounded away from zero; the unique boundary \(s_c=2^{-a}\) has a different, \(m^{-1/2}\), law. This is a stability threshold for preserving uniform Hilbert snowflake exponents when identical five-cycle clusters grow.

## Limitations

The exact result assumes five equal-sized clusters, equal positive distances within each cluster, fixed distances \(1\) and \(2\) between cyclically adjacent and nonadjacent clusters, and \(0<s\le2\). It does not classify arbitrary cycle lengths, unequal cluster sizes, or heterogeneous intracluster distances. The exponent and embedding dimension are rigorous finite-metric results; no infinite-dimensional limiting metric or general Banach-space rigidity theorem is asserted. The checked literature includes general methods that could enable other derivations, and equivalent published formulations may exist outside the inspected sources.

## References

[1] H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, initial public version January 6, 2009. Particularly Theorem 5.4. https://arxiv.org/abs/0901.0695

[2] S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, initially public August 2, 2011. Particularly Corollary 2.4 and Example 2.8. https://arxiv.org/abs/1108.0451

[3] M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, initially public December 23, 2011. Particularly Theorem 3.1. https://arxiv.org/abs/1112.5657

[4] A. Weston, *Optimal lower bounds on the maximal p-negative type of finite metric spaces*, arXiv:0807.2705, initially public July 17, 2008. Particularly Theorem 4.1. https://arxiv.org/abs/0807.2705
