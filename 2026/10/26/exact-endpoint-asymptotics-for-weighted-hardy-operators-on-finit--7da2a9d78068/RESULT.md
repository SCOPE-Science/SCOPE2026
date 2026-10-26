# Exact endpoint asymptotics for weighted Hardy operators on finite metric trees

## Finding
Let \(\Gamma\) be a finite compact metric tree rooted at \(o\), equipped with arc-length measure. Let \(u,v\in C(\Gamma)\) be strictly positive. Define the path-integration operator
\[
(Tf)(x)=v(x)\int_{[o,x]}u(t)f(t)\,dt,\qquad f\in L^\infty(\Gamma).
\]
For the approximation numbers
\[
a_n(T)=\inf\{\|T-R\|: R:L^\infty(\Gamma)\to L^\infty(\Gamma),\ \operatorname{rank}R<n\},
\]
one has the exact endpoint asymptotic
\[
\lim_{n\to\infty}n a_n(T)=\frac12\int_\Gamma u(t)v(t)\,dt.
\]

## Assumptions and scope
The tree has finitely many edges of positive length; the root is a vertex (subdivide its edge if necessary). The weights are real, continuous, and bounded away from zero. The norm on both domain and range is the essential-supremum norm. The result does not assert an exact formula for each finite \(a_n(T)\), and does not cover arbitrary measurable weights or infinite trees.

## Proof
Write \(q=uv\) and \(Q=\int_\Gamma q\,dt>0\). For each original edge \(e\), put \(Q_e=\int_e q\,dt\). Given large \(N\), choose positive integers \(m_e\) with \(\sum_e m_e=N\) and \(m_e=NQ_e/Q+O(1)\). Divide edge \(e\) into \(m_e\) subintervals of equal \(q\)-mass. Since there are finitely many edges and \(q\) is continuous and positive, every resulting interval \(I\) has length \(O(N^{-1})\), and uniformly
\[
\int_I q\,dt=Q/N+O(N^{-2}),\qquad (\sup_I u)(\sup_I v)|I|=(1+o(1))\int_Iq\,dt.
\]

Set \(Gf(x)=\int_{[o,x]}u f\), and let \(I_NGf\) be its linear interpolant at the subdivision vertices. The subdivided tree has \(N\) edges and \(N+1\) vertices; since \(Gf(o)=0\), the map \(R_Nf=v I_NGf\) has rank at most \(N\). On an interval of length \(h\), linear interpolation of an \(L\)-Lipschitz function has error at most \(Lh/2\). Thus
\[
\|T-R_N\|\le\frac12\max_I(\sup_Iu)(\sup_Iv)|I|=(1+o(1))\frac{Q}{2N},
\]
so \(a_{N+1}(T)\le(1+o(1))Q/(2N)\).

For the lower bound, on each subdivision interval \(I_j\), choose its midpoint in the \(u\)-measure, namely \(c_j\) satisfying \(\int_{I_j\cap[o,c_j]}u=\frac12\int_{I_j}u\). Let \(f_j\) equal \(+1\) before \(c_j\), \(-1\) after it, and zero off \(I_j\). Then \(\|f_j\|_\infty=1\), the integral of \(u f_j\) over \(I_j\) is zero, and \(Tf_j\) is supported on \(I_j\). At \(c_j\),
\[
\|Tf_j\|_\infty\ge\frac12v(c_j)\int_{I_j}u=(1-o(1))\frac{Q}{2N},
\]
uniformly in \(j\), by uniform continuity and positivity of the weights. The functions \(f_j\) have disjoint supports, as do their images. Any operator of rank less than \(N\) has a nonzero kernel vector on their \(N\)-dimensional span; normalize its coefficients so their maximum modulus is one. The disjoint-support property then gives \(a_N(T)\ge(1-o(1))Q/(2N)\). Combining the lower bound for \(a_N\) and upper bound for \(a_{N+1}\) proves the limit.

## Verification
The upper estimate uses finite-rank nodal interpolation; the lower estimate uses disjoint, zero-integral tent witnesses and rank-nullity. The constant is therefore determined by the weighted total edge length, not by the branching pattern. No numerical computation is needed. The proof depends essentially on finitely many edges and strictly positive continuous weights.

## Relationship to prior work
Evans, Harris, and Lang establish the exact asymptotic \(n a_n(T)\) for Hardy-type operators on trees when \(1<p<\infty\); their endpoint discussion treats \(p=1\) and \(p=\infty\) by estimates rather than the same exact-limit theorem. Their earlier endpoint paper is closely related. The present statement is restricted to finite trees with strictly positive continuous weights and the \(L^\infty\)-to-\(L^\infty\) approximation numbers. The earlier endpoint paper's full text was not available for a complete comparison, so a residual overlap risk remains.

## Limitations
This is an asymptotic result, not a formula for every finite approximation number. Strict positivity excludes weights with zeros, where the effective approximation scale may require a separate analysis. No conclusion is made for infinite trees, arbitrary measurable weights, or other exponents.

## References
1. W. D. Evans, D. J. Harris, and J. Lang, “Two-sided estimates for the approximation numbers of Hardy-type operators in \(L^\infty\) and \(L^1\),” *Studia Mathematica* 130 (1998), 171–192. DOI: 10.4064/sm_1998_130_2_1_171_192.
2. W. D. Evans, D. J. Harris, and J. Lang, “The approximation numbers of Hardy-type operators on trees,” arXiv:math/0003215 (first public version 30 March 2000); *Proceedings of the London Mathematical Society* 83 (2001), 390–418. DOI: 10.1112/plms/83.2.390.
