# Sharp Hilbert-snowflake thresholds for one-edge-deleted bicliques

## Finding
Let \(m,n\ge2\) be integers with \(m+n\ge5\). Delete one cross-part edge from the unweighted complete bipartite graph \(K_{m,n}\), and use the shortest-path metric \(d\) on all \(m+n\) vertices. Put \(M=m-1\), \(N=n-1\), \(a=2^p\), and \(h=3^p-1\). For \(0\le p\le1\) define
\[
F_{m,n}(p)=a\left(\frac1M+\frac1N\right)-2(a-1)-\frac{a^2\left(\frac{an}{M}+\frac{am}{N}-2h\right)}{a^2mn-h^2MN}.
\]
There is exactly one \(p_{m,n}\in(0,1]\) with \(F_{m,n}(p_{m,n})=0\). It equals \(1\) exactly for \(\{m,n\}=\{2,3\}\); in all other stated cases it lies strictly between \(0\) and \(1\). The supremal negative-type exponent of \((V,d)\) is precisely \(p_{m,n}\). Negative type is strict for \(0\le p<p_{m,n}\), nonstrict at the endpoint with one-dimensional zero-sum equality space, and fails for all \(p>p_{m,n}\). The least affine dimension of an isometric Hilbert realization of the snowflake \(d^{p/2}\) is \(m+n-1\) below the endpoint and \(m+n-2\) at the endpoint.

For the balanced family \(m=n=r\ge3\), the exponent \(p_r\) is equivalently the unique root in \((0,1)\) of
\[
\bigl[r-1-(r-2)2^p\bigr]\bigl[r2^p+(r-1)(3^p-1)\bigr]=2^{2p}.
\]
It strictly exceeds the corresponding exponent of the undeleted \(K_{r,r}\), namely \(q_r=\log_2(r/(r-1))\), and satisfies
\[
p_r-q_r=\frac{\log3}{(\log2)^2}\,r^{-3}+O(r^{-4})\quad (r\longrightarrow\infty).
\]
Moreover \(p_{r+1}<p_r\) for all \(r\ge3\). Thus the gain from deleting one edge is strictly positive but asymptotically cubic in the balanced part size.

## Assumptions and scope
All graphs are finite, simple, connected and unweighted. The distinguished deleted edge joins the first vertex in each bipartition part. All remaining cross-part distances are \(1\), every distinct within-part distance is \(2\), and the two endpoints of the deleted edge have distance \(3\). For \(p\ge0\), a metric has \(p\)-negative type when \(\sum_{u,v}d(u,v)^p z_uz_v\le0\) for every real family \((z_u)\) with \(\sum_u z_u=0\), with diagonal contributions understood as zero. Strict negative type requires strict inequality for every nonzero zero-sum family. Logarithms without subscript are natural logarithms. The four-vertex path case \(m=n=2\), whose supremal exponent is \(2\), is excluded from the one-dimensional endpoint claim.

## Proof
**1. Exact quadratic reduction.** Write \(z=(x_0,\ldots,x_{m-1};y_0,\ldots,y_{n-1})\), \(\sum z=0\), and \(S=\sum_i x_i=-\sum_jy_j\). With \(a=2^p\) and \(h=3^p-1\), the complete powered-distance quadratic form is exactly
\[
Q_p(z)=-a\sum_u z_u^2+2(a-1)S^2+2h x_0y_0.
\]
The first two terms are those of the original biclique; only the deleted endpoint pair changes from distance one to distance three. Fixing \((S,x_0,y_0)=(S,x,y)\), the form is maximized when the other coordinates in each part are equal, by the equality case of Cauchy--Schwarz. Put \(M=m-1\) and \(N=n-1\). The resulting maximal value is
\[
\begin{aligned}
\widehat Q_p(S,x,y)={}&-a\left[x^2+y^2+\frac{(S-x)^2}{M}+\frac{(S+y)^2}{N}\right]\\
&+2(a-1)S^2+2hxy.
\end{aligned}
\]
Every omitted within-part contrast contributes exactly a negative square multiplied by \(-a\). Hence negative type for the full metric is equivalent to \(-\widehat Q_p\) being positive semidefinite as a form on the three independent real variables \((S,x,y)\); strictness and the kernel can be recovered from this decomposition.

**2. Schur complement.** The symmetric matrix of \(-\widehat Q_p\) is
\[
B=\begin{pmatrix}
a(1/M+1/N)-2(a-1)&-a/M&a/N\\
-a/M&am/M&-h\\
a/N&-h&an/N
\end{pmatrix}.
\]
For \(0\le p\le1\), subadditivity gives \(0\le h=3^p-1\le 2^p=a\). Consequently the lower-right two-by-two block \(C\) is positive definite, since its diagonal entries are positive and
\[
\det C=\frac{a^2mn-h^2MN}{MN}>0
\]
for \(m,n\ge2\). Its scalar Schur complement equals exactly \(F_{m,n}(p)\). The preceding reduction therefore proves the equivalence
\[
(V,d)\text{ has }p\text{-negative type}\quad\Longleftrightarrow\quad F_{m,n}(p)\ge0
\qquad(0\le p\le1).
\]
Moreover, if \(F_{m,n}(p)=0\), then \(C\) is invertible and the whole zero-sum quadratic form has a precisely one-dimensional kernel.

**3. Existence, uniqueness and maximality.** Substitution and elementary simplification give
\[
F_{m,n}(0)=\frac1m+\frac1n>0,\qquad
F_{m,n}(1)=-\frac{2(m+n-5)}{m+n-1}.
\]
Continuity gives at least one zero in \((0,1)\) when \(m+n\ge6\), or at the endpoint \(p=1\) when \(m+n=5\). The finite-metric strict-negative-type interval principle states that whenever a metric has \(p\)-negative type, it has strict \(q\)-negative type for each \(0\le q<p\). If the scalar Schur complement vanished at some smaller exponent and the metric had negative type at a larger exponent, its earlier nontrivial equality would contradict this principle. Thus the zero is unique, all smaller exponents have strict negative type, and no larger exponent (including any \(p>1\)) has negative type. At the critical exponent, the kernel dimension proved in step 2 and the centered Euclidean Gram representation imply the asserted affine Hilbert dimensions.

**4. Balanced family.** Let \(m=n=r\ge3\). The reduced form splits under exchange of the two parts: the mode \(x=y,S=0\) is strictly negative, since its coefficient is \(-2ar/(r-1)+2h<0\) for \(0\le p\le1\). On the remaining mode \(y=-x\), its two-by-two determinant is nonnegative precisely when
\[
T_r(p):=\bigl[r-1-(r-2)a\bigr]\bigl[ra+(r-1)h\bigr]-a^2\ge0.
\]
The critical root is therefore the unique zero of \(T_r\) in \((0,1)\). For the original \(K_{r,r}\), the threshold is \(q_r=\log_2(r/(r-1))\) by the same zero-sum quadratic form with \(h=0\). At \(p=q_r\), one has the exact identity \(T_r(q_r)=3^{q_r}-1>0\), so \(p_r>q_r\).

At the balanced critical exponent, choose \(S=1\); the equality vector has \(x=-y=a/(ra+(r-1)h)\). Every other vertex in the first part has coefficient \((1-x)/(r-1)>0\), and those in the second have its negative. Thus the unique equality vector is nonzero on every undistinguished vertex. The metric for size \(r\) is an isometric submetric of the size \(r+1\) metric, and its equality vector extended by zeros cannot be an equality vector for the larger metric if that larger metric has negative type (its own equality vectors are nonzero at all undistinguished vertices). Hence \(p_{r+1}<p_r\).

For the asymptotic, \(q_r=O(r^{-1})\) and \(T_r(q_r)=3^{q_r}-1=(\log3/\log2)r^{-1}+O(r^{-2})\). The critical root also obeys \(p_r=O(r^{-1})\): for sufficiently large \(r\), evaluating \(T_r\) at \(p=2/(r\log2)\) gives a negative value, while the value at \(q_r\) is positive. Uniformly throughout the interval between these two points,
\[
T_r'(p)=-(\log2)r^2+O(r).
\]
The mean value theorem therefore yields
\[
p_r-q_r=\frac{\log3}{(\log2)^2}r^{-3}+O(r^{-4}),
\]
with the stated coefficient and error.

## Verification
The accompanying standalone standard-library checker `verify.py` independently constructs the graph distances by breadth-first search, evaluates complete centered powered-distance Gram spectra, compares the reduced quadratic form with direct pairwise sums, tests the endpoint formulas, and checks balanced roots and the asymptotic coefficient. In the packaged check, 5,414 finite comparisons and assertions passed. These are auxiliary tests; the proof above supplies the all-integer and all-real-exponent assertions. Run with `python3 verify.py`. No external numerical library is required.

## Relationship to prior work
Młotkowski, Skrzypczyk and Wojtylak (arXiv:2409.17662, first posted September 26, 2024), Section 2, give the ordinary quadratic embedding constant at exponent one for complete bipartite graphs with matching edges removed, including one removed edge. Their calculation identifies the exponent-one boundary but does not give the powered-distance threshold at all real exponents or the balanced cubic excess. Robertson (arXiv:2004.10923) supplies a general determinant characterization of maximal generalized roundness, but not this symmetry-reduced all-parameter formula or asymptotic. The finite-metric strictness interval is due to Li and Weston (arXiv:0901.0695), with a later related formulation by Doust and Weston (arXiv:2404.06658). These general tools are used and are not claimed as new. The novelty claim is limited to the exact two-parameter threshold, its kernel and the sharp balanced stability law.

## Limitations
This statement is for deleting a single cross-part edge, not a matching of arbitrary size or a weighted edge. The explicit scalar formula is asserted in the parameter range \(0\le p\le1\), and the interval principle is needed to exclude all larger exponents. No uniform asymptotic is claimed when both parts grow at unrelated rates. Scientific priority requires independent assessment against potentially unindexed or historical equivalent powered-distance calculations; finite tests are not a proof of the theorem.

## References
1. W. Młotkowski, M. Skrzypczyk and M. Wojtylak, *On quadratic embeddability of bipartite graphs and theta graphs*, arXiv:2409.17662 (initial public version September 26, 2024), https://arxiv.org/abs/2409.17662.
2. G. Robertson, *The Maximal Generalised Roundness of Finite Metric Spaces*, arXiv:2004.10923 (April 23, 2020), https://arxiv.org/abs/2004.10923.
3. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (January 6, 2009), https://arxiv.org/abs/0901.0695.
4. I. Doust and A. Weston, *Polygonal equalities and p-negative type*, arXiv:2404.06658 (April 9, 2024), https://arxiv.org/abs/2404.06658.
