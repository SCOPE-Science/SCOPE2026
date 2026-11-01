# A sharp Euclidean balance boundary for complete-bipartite resistance metrics

## Finding
For every pair of integers \(m,n\ge2\), equip the vertices of the unit-conductance complete bipartite graph \(K_{m,n}\) with **effective resistance distance** \(R\), rather than shortest-path distance. Put \(N=m+n\). The supremal \(p\)-negative-type exponent \(\wp_{m,n}\) is the **unique positive** solution of
\[
\frac{m-1}{m}\left(\frac{2m}{m+n-1}\right)^p
+\frac{n-1}{n}\left(\frac{2n}{m+n-1}\right)^p=2.
\]
It is always strictly greater than \(1\). The metric has strict \(p\)-negative type for \(0<p<\wp_{m,n}\), non-strict \(p\)-negative type at \(p=\wp_{m,n}\), and fails \(p\)-negative type for every larger \(p\). At the endpoint the complete equality-coefficient space is one-dimensional, spanned by the vector constant \(1/m\) on the first part and \(-1/n\) on the second part.

The threshold has the exact *balance phase transition*
\[
\wp_{m,n}\begin{cases}
>2,&m=n,\\
=2,&|m-n|=1,\\
\in(1,2),&|m-n|\ge2.
\end{cases}
\]
Consequently, **effective resistance distance itself** (not merely its square root) embeds isometrically into a real Euclidean space exactly when \(|m-n|\le1\). If \(0<p<\wp_{m,n}\), the least dimension of a Euclidean realization of the snowflake \(R^{p/2}\) is \(N-1\); at \(p=\wp_{m,n}\), it is \(N-2\).

On balanced graphs the exponent is explicitly
\[
\wp_{q,q}=\frac{\log(q/(q-1))}{\log(2q/(2q-1))}.
\]
For any fixed nonnegative integer \(k\),
\[
\wp_{q,q+k}=2+\frac{1-k^2}{2q}+O_k(q^{-2})\quad(q\to\infty).
\]
For any sequence with \(m,n\to\infty\) and \(n/m\to\rho\in(1,\infty)\), the threshold tends to \(1\), whereas if \(m\) stays fixed and \(n\to\infty\),
\[
\wp_{m,n}=1+\frac{1}{n\log2}+o_m(n^{-1}).
\]
These statements are one connected classification of the same resistance-metric invariant.

## Assumptions and scope
The graph is finite, connected, simple, complete bipartite, and has \(m,n\ge2\) vertices in its respective parts. Every edge is a unit resistor (unit conductance). Effective resistance means \(R(i,j)=(e_i-e_j)^{\mathsf T}L^+(e_i-e_j)\), with the unnormalized graph Laplacian \(L\) and its Moore–Penrose inverse \(L^+\). We use all vertices with counting measure and the ordinary real zero-sum definition: a finite metric has \(p\)-negative type if \(\sum_{i,j}z_i z_jR(i,j)^p\le0\) for every real vector \(z\) with \(\sum_i z_i=0\). Strictness means strict inequality for every nonzero such vector. The dimension statement concerns an isometric embedding of the distance \(R^{p/2}\), not of the original graph edges with their graph-theoretic path lengths.

## Proof
**1. Independently determine the resistance metric.** The Laplacian \(L\) of \(K_{m,n}\) has eigenvalue \(n\) on the \((m-1)\)-dimensional zero-sum first-part space, eigenvalue \(m\) on the \((n-1)\)-dimensional zero-sum second-part space, eigenvalue \(m+n\) on the one-dimensional global part-contrast space, and eigenvalue zero on constants. Since the difference of two first-part coordinate vectors is entirely in the first eigenspace, its resistance is \(2/n\), and similarly the resistance between two second-part vertices is \(2/m\). For a cross-part difference vector, the squared projections onto these three nonconstant eigenspaces are respectively \((m-1)/m\), \((n-1)/n\), and \((m+n)/(mn)\). Thus the cross-part resistance is
\[
\frac{m-1}{mn}+\frac{n-1}{mn}+\frac1{mn}=\frac{m+n-1}{mn}.
\]
Put \(a=(m+n-1)/(mn)\), \(b=2/n\), \(c=2/m\). These are precisely the cross-, first-within-, and second-within-part nonzero distances.

**2. Reduce *all* negative-type inequalities, without dropping directions.** Write any real zero-total coefficient vector uniquely as
\[
z=\left(u_0+\frac{s}{m}\mathbf1_m,\ v_0-\frac{s}{n}\mathbf1_n\right),\qquad
\mathbf1_m^{\mathsf T}u_0=\mathbf1_n^{\mathsf T}v_0=0.
\]
The complete powered-distance matrix has blocks \(b^p(J_m-I_m)\), \(c^p(J_n-I_n)\), and cross blocks \(a^pJ_{m,n}\). Its quadratic form on the entire zero-sum hyperplane is exactly
\[
z^{\mathsf T}D_pz=-b^p\|u_0\|_2^2-c^p\|v_0\|_2^2+s^2F_{m,n}(p),
\quad F_{m,n}(p)=\frac{m-1}{m}b^p+\frac{n-1}{n}c^p-2a^p.
\]
Therefore negative type holds if and only if \(F_{m,n}(p)\le0\); equality at an endpoint forces \(u_0=v_0=0\), establishing the asserted one-dimensional equality space.

**3. Uniqueness and full exponent range.** Divide \(F_{m,n}\) by \(a^p\). Writing \(X=2m/(m+n-1)\), \(Y=2n/(m+n-1)\), the normalized expression is
\[
G(p)=\frac{m-1}{m}X^p+\frac{n-1}{n}Y^p-2.
\]
Relabel parts so \(m\le n\). Then \(Y>1\), \(G(0)=-1/m-1/n<0\), \(G(p)\to+\infty\), and \(G''(p)>0\) on the real line. Strict convexity makes the nonpositive sublevel set on \([0,\infty)\) an initial interval with a unique positive right endpoint. Direct substitution gives \(F_{m,n}(1)=-2/(mn)<0\), so \(\wp_{m,n}>1\). It follows that the sign is strictly negative below the unique root and strictly positive above it, completing the all-exponent classification.

**4. The exact Euclidean threshold.** A rational simplification with no limiting approximation gives
\[
F_{m,n}(2)=\frac{2((m-n)^2-1)}{m^2n^2}.
\]
The sign of this expression, together with Step 3 and Schoenberg's finite Euclidean distance criterion, shows that \(R\) itself is Euclidean precisely when the two part sizes differ by at most one, and establishes each of the three comparisons of \(\wp_{m,n}\) with \(2\). At the endpoint the centered Gram matrix \(-\frac12JD_pJ\), \(J=I_N-N^{-1}\mathbf1\mathbf1^{\mathsf T}\), is positive semidefinite and has rank \(N-2\). Below the endpoint it has rank \(N-1\), proving the sharp minimum embedding dimensions. When \(m=n=q\), the scalar root equation reduces to the displayed logarithmic formula.

**5. Size-asymptotic boundary.** Let \(n=q+k\), \(m=q\) with fixed \(k\ge0\). The normalized scalar function in Step 3 satisfies, as \(q\to\infty\),
\[
G(2)=\frac{2(k^2-1)}{(2q+k-1)^2}=\frac{k^2-1}{2q^2}+O_k(q^{-3}),
\qquad G'(2)=\frac1q+O_k(q^{-2}).
\]
Uniform expansion of \(G'\) on a fixed neighborhood of \(2\) gives \(G'(p)=q^{-1}+O_k(q^{-2})\) there. The mean-value theorem and uniqueness of the root consequently give \(\wp_{q,q+k}=2+(1-k^2)/(2q)+O_k(q^{-2})\). For \(n/m\to\rho>1\) and both sizes diverging, \(G\) converges on compact positive-\(p\) intervals to \((2/(1+\rho))^p+(2\rho/(1+\rho))^p-2\). Its unique positive root is \(1\), by strict concavity for \(0<p<1\) and strict convexity for \(p>1\); hence the finite roots tend to \(1\). Finally, if \(m\) is fixed and \(n\to\infty\), \(G(1)=-2/(m+n-1)\) and \(G'(p)\to2\log2\) uniformly near \(p=1\), yielding \(\wp_{m,n}-1=1/(n\log2)+o_m(n^{-1})\).

## Verification
The standalone `verify_resistance.py` independently forms the integer graph Laplacian and inverts a reduced Laplacian over exact rational numbers to check every resistance in thirteen small complete bipartite graphs. It then forms the *full* centered powered-distance Gram matrices (rather than the two-block reduced formula), checks their inertia below, at, and above the claimed critical root, verifies the exact \(p=2\) sign identity, and checks two asymptotic regimes. Execute with `python verify_resistance.py` in an environment with Python, SymPy, NumPy, and SciPy. The proof above is analytical for every permitted size and exponent; these finite calculations are independent consistency checks only.

## Relationship to prior work
Klein's resistance-distance framework and later published complete-bipartite resistance formulas supply the underlying metric; these are not claimed as new. Sánchez (arXiv:1108.0451v1, Theorem 3.1) evaluates maximal negative type for \(K_{m,n}\) with the *shortest-path metric*, which has cross-distance \(1\) and same-part distance \(2\), unlike the three resistance distances used here. Sánchez's result therefore does not imply the balance boundary, and indeed predicts a different exponent. Yang (2012) uses the resistance formulas to calculate Kirchhoff-index extrema, not powered-distance negative type. Liu, Pan, Jin, and Li (arXiv:2512.14195v1) study identification of complete bipartite graphs from the multiset of resistance distances, rather than the quadratic-form signs of their powers. This contribution is the resistance-metric exponent classification, equality space, Euclidean threshold, and asymptotic boundary, **not** the previously known resistance values or the general finite-metric negative-type criterion.

## Limitations
Only unit-conductance complete bipartite graphs with both parts of size at least two are covered. Stars, noncomplete bipartite graphs, arbitrary multipartite graphs, edge weights, and graph shortest-path distances are not included. No assertion of publication priority follows from database searches: unindexed equivalent results and a fully uninspected older source remain plausible. Critical finite Gram calculations do not replace the universal analytic proof.

## References
1. D. J. Klein, *Resistance-Distance Sum Rules*, Croatica Chemica Acta 75 (2002), 633–649. Public metadata dated 2002-06-03: https://hrcak.srce.hr/127542.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1 (2011-08-02), especially Theorem 3.1: https://arxiv.org/abs/1108.0451.
3. Y. Yang, *Bounds for the Kirchhoff Index of Bipartite Graphs*, Journal of Applied Mathematics (2012), 195242, DOI 10.1155/2012/195242; first online 2012-04-23: https://doi.org/10.1155/2012/195242.
4. X.-Y. Liu, X.-F. Pan, Y.-Y. Jin and L.-C. Li, *Characterization of Complete Bipartite Graphs via Resistance Spectra*, arXiv:2512.14195v1 (2025-12-16): https://arxiv.org/abs/2512.14195.
5. K. Devriendt and R. Lambiotte, *Discrete curvature on graphs from the effective resistance*, Journal of Physics: Complexity 3 (2022), 025008, DOI 10.1088/2632-072X/ac730d; resistance negative-type geometry discussed in Appendix B.3.
6. D. J. Klein and M. Randić, *Resistance distance*, Journal of Mathematical Chemistry 12 (1993), 81–95, DOI 10.1007/BF01164627. Only month/year provenance is visible in the publisher record.
