# Cubic roundness sensitivity of a single weighted tripartite edge

## Finding

For every integer \(n\ge2\) and every real \(1<t\le2\), start with the unit-edge complete tripartite graph \(K_{n,n,n}\), change exactly one edge joining the first and second parts to length \(t\), and retain all \(3n\) vertices with their weighted shortest-path metric \(d_{n,t}\). Define for \(0<\eta\le1\) the larger quadratic root
\[
T_n(\eta)=\frac{3n^2+(3n-2)\eta+\sqrt{\bigl(3n^2+(3n-2)\eta\bigr)^2-36n^2(n-1)\eta}}{6n}.
\]
The supremal negative-type exponent \(\wp_n(t)\) is the **unique** number \(p\) in \(\bigl(0,\log_2(n/(n-1))\bigr)\) satisfying
\[
\boxed{\frac{2^p}{2^p-1}=T_n\!\left(\frac{t^p-1}{2^p-1}\right)}.
\]
Negative type is strict for \(0<p<\wp_n(t)\), holds non-strictly with a one-dimensional equality space at \(p=\wp_n(t)\), and fails for \(p>\wp_n(t)\). The minimum affine Euclidean dimension of the snowflake \(d_{n,t}^{p/2}\) is \(3n-1\) below the endpoint and \(3n-2\) at the endpoint. The intact tripartite graph has critical exponent \(p_0(n)=\log_2(n/(n-1))\) with a two-dimensional equality space and endpoint dimension \(3n-3\).

For every fixed \(1<t\le2\), the loss caused by changing a single edge has the exact cubic-scale limit
\[
\boxed{\lim_{n\to\infty}n^3\bigl(p_0(n)-\wp_n(t)\bigr)=\frac{\log t}{3(\log2)^2}}.
\]
The endpoint \(t=2\) is the deletion of that edge in the shortest-path metric. At \(t=1\) (not included in the strict-loss assertion) the metric is the original complete tripartite metric.

## Assumptions and scope

The three vertex parts have equal integer size \(n\ge2\). Exactly one cross-part edge has positive length \(t\in(1,2]\); every other edge has length one. As the replacement edge has length at most two, shortest-path distances are \(t\) for its endpoints, \(2\) for all other distinct within-part pairs, and \(1\) for all other cross-part pairs. For \(p>0\), \(p\)-negative type means \(\sum_{i,j}c_ic_jd(i,j)^p\le0\) for all real coefficients summing to zero; strictness means strict inequality for every nonzero such vector. Its supremum over admissible \(p\) is the generalized roundness exponent. Euclidean snowflake distances are \(d^{p/2}\).

## Proof

**1. The two-distance form with one weighted edge.** Let \(B_0\) be the adjacency matrix of the intact unit-edge tripartite graph, \(E\) the symmetric matrix with ones precisely at the two oriented positions of the distinguished edge, and \(J\) the all-ones matrix. For \(a=2^p\), \(b=t^p\), and \(\eta=(b-1)/(a-1)\in(0,1]\), the matrix of powered distances is exactly
\[
D_p=a(J-I)+(1-a)B_0+(b-1)E.
\]
On \(\mathbf1^\perp\) this gives
\[
 c^\mathsf TD_pc=-a\|c\|^2-(a-1)c^\mathsf T(B_0-\eta E)c.
\]
Therefore negative type at a particular exponent \(p\) holds exactly when \(a\ge(a-1)T_n(\eta)\), where \(T_n(\eta)\) is the largest negative Rayleigh quotient of \(B_0-\eta E\) restricted to \(\mathbf1^\perp\).

**2. Complete symmetry reduction.** Let the parts be \(A,B,C\), with distinguished edge endpoints \(u\in A\), \(v\in B\). For a zero-sum vector \(c\), let \(X,Y,Z\) be its part sums and \(x=c_u\), \(y=c_v\). As \(X+Y+Z=0\), the exact identity is
\[
-c^\mathsf T(B_0-\eta E)c=X^2+Y^2+Z^2+2\eta xy.
\]
The subspace of nondistinguished within-part zero-sum fluctuations has dimension \(3n-5\) and is a zero eigenspace of the compressed matrix. On the remaining four-dimensional orthogonal complement, exchange of \(A,B\) yields symmetric and antisymmetric two-dimensional invariant sectors.

In the symmetric sector, set the values at \(u,v\) equal to \(x\), the other values in each of \(A,B\) equal to \(y\), and the values in \(C\) equal to \(-2s/n\), where \(s=x+(n-1)y\). The negative adjacency Rayleigh quotient is
\[
R_+(x,y)=\frac{3s^2+\eta x^2}{x^2+(n-1)y^2+2s^2/n}.
\]
Writing \(w=(1,n-1)^\mathsf T\), the generalized eigenvalue pencil is \(3ww^\mathsf T+\operatorname{diag}(\eta,0)-T[\operatorname{diag}(1,n-1)+(2/n)ww^\mathsf T]\). Its determinant equals \((n-1)/n\) times
\[
3nT^2-[3n^2+(3n-2)\eta]T+3n(n-1)\eta.
\]
Hence its larger root is the stated \(T_n(\eta)\). Testing \(x=y=1\) gives \(R_+=n+\eta/(3n)>n\).

In the antisymmetric sector, set the endpoint values to \(x,-x\), other values in \(A,B\) to \(y,-y\), and all \(C\) values to zero. The quotient is
\[
R_-(x,y)=\frac{s^2-\eta x^2}{x^2+(n-1)y^2}.
\]
For \(\eta>0\), this is strictly less than \(n\) for every nonzero \((x,y)\), by Cauchy–Schwarz \(s^2\le n[x^2+(n-1)y^2]\), with equality only when \(x=y\ne0\), where the \(\eta x^2\) term is strictly negative. Compactness of the normalized circle makes the maximum strictly less than \(n\). Thus the smallest compressed eigenvalue is \(-T_n(\eta)<-n\), and it is simple. This proves the spectral reduction for every \(\eta>0\).

**3. Unique critical exponent and ranks.** As \(p\downarrow0\), \(D_p\) tends to \(J-I\), strictly negative on the zero-sum hyperplane. Put \(p_0(n)=\log_2(n/(n-1))\). At \(p=p_0(n)\), the intact metric has zero quadratic form on all part-constant zero-sum vectors; using values \(1,1,-2\) on the three parts, the distinguished edge changes this form by \(2(t^{p_0(n)}-1)>0\). Thus \(p_0(n)\)-negative type fails. By continuity a critical exponent occurs strictly between zero and \(p_0(n)\). The strict-negative-type inheritance principle (Li–Weston), applied to this finite metric, implies that the admissible exponents form an initial interval, strict below its supremum, so the critical exponent is unique; equivalently, there can be no second zero of the maximal compressed powered-distance eigenvalue after the first failure. Step 2 shows that at every positive \(p\) its critical eigenvalue is simple, and substitution into the form in step 1 gives exactly the boxed equation. The finite-metric Schoenberg Gram correspondence then gives affine dimensions \(3n-1\) strictly below criticality and \(3n-2\) at criticality. In the intact case the compressed least adjacency eigenvalue is \(-n\) with multiplicity two, so its critical snowflake has dimension \(3n-3\).

**4. Cubic loss.** Write \(T_n(\eta)=n+\delta_n(\eta)\). Substituting into the quadratic gives exactly
\[
3n\delta_n(\eta)^2+[3n^2-(3n-2)\eta]\delta_n(\eta)=n\eta.
\]
For \(0\le\eta\le1\) this implies \(\delta_n(\eta)=O(1/n)\) uniformly and \(n\delta_n(\eta)=\eta/3+o(1)\) uniformly. At the critical exponent \(p_n=\wp_n(t)\), the strict-loss bound \(0<p_n<p_0(n)\) and the critical equation imply \(p_n\to0\), while
\[
\eta_n=\frac{t^{p_n}-1}{2^{p_n}-1}\longrightarrow\frac{\log t}{\log2}.
\]
The critical relation is \(p_n=\log_2[(n+\delta_n(\eta_n))/(n+\delta_n(\eta_n)-1)]\). Consequently
\[
p_0(n)-p_n=\log_2\!\left(1+\frac{\delta_n(\eta_n)}{(n-1)[n+\delta_n(\eta_n)]}\right),
\]
which, after multiplication by \(n^3\), converges to \(\log t/[3(\log2)^2]\). This also includes the edge-deletion value \(1/(3\log2)\) at \(t=2\).

## Verification

The standalone `verify_weighted_tripartite_edge.py` constructs the entire weighted distance matrix directly for several integer part sizes, edge lengths and exponents; it compares the critical eigenvalue with the two-sector quadratic root, tests kernel simplicity and analytic cubic scaling, and includes exact integer evaluations at the deletion endpoint. Execute `python verify_weighted_tripartite_edge.py` after installing NumPy from `requirements.txt`. Such finite checks support but do not replace the proof above.

## Relationship to prior work

Li–Weston establish strict-negative-type inheritance; Sánchez studies supremal negative type of finite metrics, including complete bipartite examples. Obata's general complete-multipartite quadratic-embedding-constant classification concerns the original graph, with no changed edge. Choudhury–Nandi and earlier graph-join QEC methods provide broad results at the *unweighted, original-exponent* graph distance, and can cover the special endpoint \(t=2\) through the join representation, so **the deletion endpoint is not asserted as separately original**. The asserted contribution is the continuous family \(1<t<2\), its implicit sharp threshold, equality ranks and the exact \(\log t\) coefficient of cubic sensitivity. The general spectral reduction is acknowledged as standard, and equivalent literature outside inspected primary works remains possible.

## Limitations

Exactly three equal-sized parts and one stretched edge of length \(1<t\le2\) are assumed. The result does not classify simultaneous weight changes or unequal part sizes; there is no independent mathematical validation. The endpoint deletion calculation is a limiting/special case, not a stand-alone novelty assertion.

## References

- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first public version January 6, 2009).
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first public version August 2, 2011).
- N. Obata, *Complete Multipartite Graphs of Non-QE Class*, arXiv:2206.05848 (first public version June 12, 2022).
- P. N. Choudhury and R. Nandi, *Quadratic Embedding Constants of Cartesian Products and Joins of Graphs*, arXiv:2508.10834 (first public version August 14, 2025).
