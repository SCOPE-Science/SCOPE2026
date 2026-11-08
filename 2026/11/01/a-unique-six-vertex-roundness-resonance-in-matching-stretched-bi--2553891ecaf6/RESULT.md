# A unique six-vertex roundness resonance in matching-stretched bipartite metrics

## Finding

Let \(n\ge3\) be an integer and \(s\in[1,3]\). On the vertex set of the balanced complete bipartite graph \(K_{n,n}\), give each matched cross edge \(a_i b_i\) length \(s\), all other cross edges length \(1\), and take the shortest-path metric \(d_{n,s}\). Write
\[
 A_p=2^p,\quad B_p=s^p,\quad F_{n,s}(p)=(n-1)(A_p-1)-B_p,\quad G_s(p)=B_p-A_p-1.
\]
For every \(p\ge0\), with the usual convention that nonzero distances to the zeroth power equal one, the metric has \(p\)-negative type if and only if
\[
\boxed{F_{n,s}(p)\le0\ \text{and}\ G_s(p)\le0.}
\]
The remaining zero-sum eigenvalue is always strictly negative. Define \(\wp(n,s)\) to be the supremal exponent of negative type.

Set \(p_{\rm hex}=\log_2 3\) and \(s_{\rm hex}=4^{1/p_{\rm hex}}\). For \(n=3\), the map \(s\mapsto\wp(3,s)\) increases strictly until \(s=s_{\rm hex}\), then decreases strictly, with its unique maximum \(\wp(3,s_{\rm hex})=p_{\rm hex}\). At the unique interior double spectral zero, the squared distances of the snowflake \(d_{3,s_{\rm hex}}^{p_{\rm hex}/2}\) are those of a unit-side regular planar hexagon. No other critical parameter in the family has a two-dimensional Euclidean realization.

For \(n=4\), the supremal exponent increases strictly from \(\log_2(4/3)\) at \(s=1\) to \(1\) at \(s=3\); two modes collide only at \((s,p)=(3,1)\). For every \(n\ge5\), \(\wp(n,s)\) is strictly increasing in \(s\), is in \((0,1)\), and is the **least positive root** of
\[
\boxed{(n-1)(2^p-1)=s^p.}
\]
Equivalently, it is the **unique root in \((0,1)\)**, and the unique root up to the first positive zero of \(G_s\) when \(s>2\). Importantly, for \(s>2\) the displayed equation can have an additional positive root beyond that first negative-type endpoint; **global uniqueness of its positive roots is not asserted**. The later root does not restore negative type, because the \(G_s\)-mode is then positive.

The minimum dimension of a Euclidean realization of \(d_{n,s}^{p/2}\) is \(2n-1\) for \(0\le p<\wp\). At \(p=\wp\) it is
\[
\boxed{\begin{cases}
4,&n=3,\ s<s_{\rm hex},\\
2,&n=3,\ s=s_{\rm hex},\\
3,&n=3,\ s>s_{\rm hex},\\
6,&n=4,\ s<3,\\
3,&n=4,\ s=3,\\
2n-2,&n\ge5.
\end{cases}}
\]
All critical endpoints have non-strict negative type. With \(N=n-1\), uniformly over \(s\in[1,3]\),
\[
\boxed{\wp(n,s)=\frac1{N\log2}+\frac{\log s/(\log2)^2-1/(2\log2)}{N^2}+O(N^{-3}).}
\]
Consequently \(\wp(n,s)-\wp(n,1)=(\log s)/(N^2(\log2)^2)+O(N^{-3})\) uniformly over the same interval.

## Assumptions and scope

A metric has \(p\)-negative type when \(\sum_{i,j}z_i z_j d(i,j)^p\le0\) for every real \(z\) whose coordinate sum vanishes. Strictness means strict inequality for every nonzero such vector. For \(n\ge3\) and \(1\le s\le3\), shortest-path distances equal \(2\) within either part, \(1\) between nonmatched opposite vertices, and \(s\) between matched opposite vertices (including the tie at \(s=3\)). The realization of \(d^{p/2}\) uses the squared-distance matrix \(D_p\); it does not claim the unsnowflaked metric is Euclidean. Equal matched lengths and balanced parts are essential assumptions.

## Proof

**Zero-sum decomposition.** In the order \((a_1,\ldots,a_n,b_1,\ldots,b_n)\), let \(J\) be the \(n\)-by-\(n\) all-ones matrix. The powered-distance matrix is
\[
D_p=\begin{pmatrix}A_p(J-I)&J+(B_p-1)I\\J+(B_p-1)I&A_p(J-I)\end{pmatrix}.
\]
For any zero-sum \(z=(x,y)\), write \(x=a\mathbf1+u\), \(y=-a\mathbf1+v\), with \(\sum u_i=\sum v_i=0\), and put \(w_\pm=(u\pm v)/\sqrt2\). Direct multiplication gives the orthogonal identity
\[
 z^{\mathsf T}D_pz=2na^2 F_{n,s}(p)+G_s(p)\|w_+\|^2+(1-A_p-B_p)\|w_-\|^2.
\]
The sector multiplicities are \(1,n-1,n-1\), and \(1-A_p-B_p<0\) for every \(p\ge0\). This proves the claimed necessary-and-sufficient criterion, including the \(p=0\) boundary and all critical equality multiplicities.

**First critical root and branch change.** For \(1\le s\le2\), \(G_s(p)<0\) for \(p>0\). The quotient \(Q_s(p)=s^p/(2^p-1)\) decreases strictly from infinity to a limit at most one, so the equation \(Q_s(p)=n-1\), \(n-1\ge2\), has exactly one positive root.

For \(2<s\le3\), \(G_s\) has a unique positive root \(g(s)\), determined by \((s/2)^p=1+2^{-p}\). The left side increases, the right decreases; \(g(3)=1\), and \(g(s)>1\) for \(s<3\). The quotient \(Q_s\) is strictly decreasing on \((0,g(s)]\). Indeed, with \(t=2^p>1\), the inequality
\[
 t\log t-(t-1)\log(t+1)>0
\]
follows by differentiation from its zero limit as \(t\downarrow1\), since its derivative is \(-\log(1+1/t)+2/(t+1)>0\). For \(p\le g(s)\), \(s^p\le2^p+1\), so
\[
 \log s\le\frac{\log(t+1)}p<\frac{t\log2}{t-1},
\]
which proves \((\log Q_s)'<0\) on this interval. The first loss of negative type is therefore the first zero of \(F_{n,s}\) or \(G_s\); it cannot be reversed after \(G_s>0\). In particular, later positive roots of \(F_{n,s}\) for \(s>2\), if present, have no bearing on the negative-type endpoint. For instance \(F_{5,3}(1)=1>0\) but \(F_{5,3}(4)=-21<0\), so the equation \(F_{5,3}=0\) has two distinct positive roots, and the endpoint is the first one.

At \(p=g(s)\), the identity \(s^p=2^p+1\) gives
\[
 F_{n,s}(g(s))=(n-2)2^{g(s)}-n.
\]
Let \(p_n=\log_2(n/(n-2))\) and \(s_n=(2(n-1)/(n-2))^{1/p_n}\). For \(n=3\), \(p_3=\log_2 3>1\) and \(s_3=s_{\rm hex}\in(2,3)\), producing one interior collision. Below \(s_{\rm hex}\) the first root is the radial \(F\)-mode; above it the first root is the \(G\)-mode. For \(n=4\), \(p_4=1\), so the only collision is at \(s=3\). For \(n\ge5\), \(p_n<1\le g(s)\), and \(F(g)>0\), so the first root is always the \(F\)-root. Furthermore \(F_{n,s}(1)=(n-1)-s\ge n-4>0\), whence this root is in \((0,1)\) and is unique there. As \(s\) rises, \(F_{n,s}(p)\) decreases strictly at fixed \(p>0\), so this first root increases strictly. The competing \(g(s)\) decreases strictly on \((2,3]\). These observations give the stated monotonicity and the unique six-point maximum.

**Hilbert embedding ranks and geometric realizations.** Centering the squared-distance matrix gives the positive semidefinite Gram matrix \(-\frac12H D_pH\), where \(H=I-(2n)^{-1}\mathbf1\mathbf1^{\mathsf T}\). Its rank equals the number of strictly negative zero-sum eigenvalues, hence \(2n-1\) before the endpoint and \(2n-1\) minus the multiplicity \(1\), \(n-1\), or \(n\) of its critical zero(s) at the endpoint. This yields every displayed dimension. At \(n=3\), simultaneous vanishing forces \(2^p=3\), \(s^p=4\); six alternating points on a unit-side regular planar hexagon have squared distances \(1\) across adjacent nonmatched vertices, \(3\) between vertices in the same part, and \(4\) across opposite matched vertices. Gram rank two makes that realization unique up to Euclidean congruence. At \(n=4,s=3,p=1\), the distance matrix is that of the three-cube; its square-root snowflake embeds in \(\mathbb R^3\).

**Uniform asymptotic.** For \(n\ge5\), put \(N=n-1\), \(\varepsilon=1/N\), and \(p=\varepsilon y\) in the *first-root* equation. It becomes
\[
 \frac{e^{\varepsilon y\log2}-1}{\varepsilon}=e^{\varepsilon y\log s}.
\]
The left-minus-right side extends analytically to \(\varepsilon=0\), with value \(y\log2-1\) and nonzero \(y\)-derivative \(\log2\). The analytic implicit-function theorem gives \(y=(\log2)^{-1}+\varepsilon[\log s/(\log2)^2-1/(2\log2)]+O(\varepsilon^2)\), uniformly because \(s\in[1,3]\) is compact. Multiplying by \(\varepsilon\) proves the stated expansions.

## Verification and boundaries

The independent exact zero-sum identity follows by block multiplication. The accompanying `verify_matching_stretch.py` checks finitely many weighted shortest paths, exact rational quadratic forms, the two doubly critical Gram ranks, finite phase-grid examples and high-precision asymptotic diagnostics. These corroborate rather than prove the universal statements. The crucial correction from the original formulation is that, when \(s>2\), only the *least* positive \(F\)-root is the critical exponent; an additional later \(F\)-root may exist (as the exact \(n=5,s=3\) counterexample shows). The negative-type criterion and its \(G\)-mode prevent any re-entry. No generality is claimed for unbalanced parts, unequal matching lengths, \(s>3\), or unsnowflaked Hilbert embeddings.

## Relationship to prior work

Sánchez, *On the supremal p-negative type of a finite metric space* (arXiv:1108.0451), determines the unweighted balanced complete bipartite case \(s=1\) and presents the general finite-metric matrix criterion. Li and Weston, *Strict p-negative type of a metric space* (arXiv:0901.0695), prove general interval/strictness inheritance. Existing crown-graph formulas address \(s=3\), and Horak–LaRose–Moore–Rooney–Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), address unweighted four-point graph roundness. None of those evaluated special cases or general tools supplies this entire continuously weighted spectral phase diagram, the unique six-point interior resonance and planar hexagon, or its critical-rank classification without additional calculation. Unindexed equivalent diagonal-defect metric analysis remains a priority risk; no historical-priority guarantee is asserted.

## References

1. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, https://arxiv.org/abs/0901.0695.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
3. M. Horak, E. LaRose, J. Moore, M. Rooney and H. Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), 67–91, doi:10.2140/involve.2010.3.67.
