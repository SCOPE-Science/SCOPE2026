# A logarithmic collapse law for negative type of weighted complete-graph coronas

## Finding
For every integer \(m\ge3\) and real \(t>0\), let \(X_{m,t}\) consist of \(m\) core vertices \(a_1,\ldots,a_m\) forming a unit-edge complete graph and one private pendant vertex \(b_i\) joined to each \(a_i\) by an edge of length \(t\). All \(2m\) vertices are included and \(d\) is the shortest-path metric. Define
\[
F_{m,t}(p)=(m-1)\bigl[1+(1+2t)^p-2(1+t)^p\bigr]-2t^p.
\]
There is a unique \(\wp_m(t)\in(1,2)\) with \(F_{m,t}(\wp_m(t))=0\). This is exactly the supremal \(p\)-negative-type exponent of \((X_{m,t},d)\): the space has strict \(p\)-negative type for every \(0\le p<\wp_m(t)\), has nonstrict \(\wp_m(t)\)-negative type, and fails \(p\)-negative type for every \(p>\wp_m(t)\). At the endpoint, the complete real zero-sum equality space is the line with coefficient \(+1\) at every core vertex and \(-1\) at every pendant vertex. Therefore the least Euclidean embedding dimension of the metric \(d^{p/2}\) is \(2m-1\) below the endpoint and \(2m-2\) at it.

The exponent decreases strictly with \(m\) and, for fixed \(m\), decreases strictly as the pendant length \(t\) increases. Let
\[
p_m^*=\log_2\!\left(\frac{2m}{m-1}\right),\quad
u=1/t,\quad
h(\nu)=(\nu+2)\log(\nu+2)+\nu\log\nu-2(\nu+1)\log(\nu+1).
\]
Then \(h(\nu)>0\), and the sharp limiting laws are
\[
\lim_{t\downarrow0}(2-\wp_m(t))\log(1/t)=\log(m-1),
\]
\[
\wp_m(t)=p_m^*+\frac{p_m^*(m-2)}{2m\log2}\,\frac1t+o(t^{-1})\qquad(t\to\infty),
\]
\[
\wp_m(t)=1+\frac{2}{(m-1)h(1/t)}+O_t(m^{-2})\qquad(m\to\infty).
\]
Thus shortening private leaves drives the exponent logarithmically slowly toward \(2\), while lengthening them drives it toward the ordinary \(m\)-leaf star exponent \(p_m^*\). The collapsed \(t=0\) quotient is an equilateral \(m\)-point space with infinite supremal negative type, so the first limit is singular. For the unit-length six-vertex member, \(m=3,t=1\), the exponent is exactly \(\log2/\log(3/2)\).

## Assumptions and scope
For real \(p\ge0\), \(p\)-negative type means
\[
Q_p(\alpha)=\sum_{u,v\in X_{m,t}}\alpha_u\alpha_v d(u,v)^p\le0
\quad\text{whenever }\sum_{u\in X_{m,t}}\alpha_u=0,
\]
with \(d(u,u)^p:=0\), including at \(p=0\). Strict negative type requires strict inequality for every nonzero zero-sum vector. Equivalently, the centered Gram matrix \(B_p=-\tfrac12 JD_pJ\), where \(D_p=(d(u,v)^p)\) and \(J=I-\mathbf1\mathbf1^T/(2m)\), is positive semidefinite, and strictness corresponds to positive definiteness on \(\mathbf1^\perp\). The exponent \(p\) refers to the distance power, not an \(L_p\)-space parameter. Pendant lengths are common and positive; clique-edge lengths are exactly one. The formulas cover all integer \(m\ge3\) and all real \(t>0\).

The nonzero distances are \(d(a_i,a_j)=1\) for \(i\ne j\), \(d(a_i,b_i)=t\), \(d(a_i,b_j)=1+t\) for \(i\ne j\), and \(d(b_i,b_j)=1+2t\) for \(i\ne j\). These are shortest-path distances because each pendant vertex is a leaf and the core is complete.

## Proof
**Exact quadratic decomposition.** Write \(\alpha_{a_i}=x_i\), \(\alpha_{b_i}=y_i\), \(\sum_i(x_i+y_i)=0\). Set \(s=m^{-1}\sum_i x_i\), \(\xi_i=x_i-s\), and \(\eta_i=y_i+s\); then \(\sum_i\xi_i=\sum_i\eta_i=0\). Directly summing all pairs gives the identity
\[
\begin{aligned}
Q_p(\alpha)={}&-\sum_i\xi_i^2-(1+2t)^p\sum_i\eta_i^2\\
&+2\bigl[t^p-(1+t)^p\bigr]\sum_i\xi_i\eta_i
+m s^2F_{m,t}(p).
\end{aligned}
\]
Thus the \(2(m-1)\) fluctuation directions are controlled by a repeated symmetric \(2\times2\) matrix with diagonal entries \(-1\) and \(-(1+2t)^p\), and off-diagonal entry \(t^p-(1+t)^p\). The remaining zero-sum radial direction is controlled by \(F_{m,t}(p)\).

**No earlier fluctuation obstruction.** For \(0<p<2\), concavity of \(z\mapsto z^{p/2}\) on positive numbers and \((1+t)^2=t^2+(1+2t)\) yield
\[
(1+t)^p<t^p+(1+2t)^{p/2}.
\]
Therefore the fluctuation determinant satisfies
\[
(1+2t)^p-\bigl((1+t)^p-t^p\bigr)^2>0.
\]
Its diagonal entries are negative, so the entire fluctuation form is strictly negative definite. At \(p=2\) this determinant is zero, but the radial coefficient is already positive for \(m\ge3\).

**A unique radial threshold.** The radial coefficient obeys \(F_{m,t}(1)=-2t<0\) and \(F_{m,t}(2)=2(m-2)t^2>0\); hence a root exists in \((1,2)\). At every such root the decomposition shows negative type but not strict negative type, with the equality vector \(x_i=1,y_i=-1\). There cannot be two distinct roots in \((1,2)\): otherwise the metric would have negative type at the larger root while failing to have strict negative type at the smaller, contradicting the strict downward propagation theorem for negative type (Li--Weston, Theorem 5.4). Consequently the root is unique, \(F_{m,t}(p)<0\) for \(1\le p<\wp_m(t)\), and \(F_{m,t}(p)>0\) for \(\wp_m(t)<p\le2\). Strictness at \(p=1\) and downward propagation establish strict negative type for all \(0\le p<\wp_m(t)\). Any \(p>\wp_m(t)\) is impossible by the same propagation theorem: it would force strict negative type at the nonstrict endpoint. This proves the exact exponent and the one-dimensional equality space. Schoenberg's squared-distance embedding criterion then gives the stated minimal ranks \(2m-1\) and \(2m-2\).

**Strict parameter monotonicity.** Put \(u=1/t\) and
\[
G_p(u)=(u+2)^p+u^p-2(u+1)^p.
\]
Dividing the radial equation by \(t^p\) yields \((m-1)G_p(u)=2\). For every \(1<p<2\), strict concavity of \(z^{p-1}\) implies
\[
\frac{\partial G_p(u)}{\partial u}=p\bigl((u+2)^{p-1}+u^{p-1}-2(u+1)^{p-1}\bigr)<0.
\]
Increasing \(t\) decreases \(u\), so at fixed \(p\) the left side strictly increases. Increasing \(m\) also increases the left side because \(G_p(u)>0\) for \(p>1\) by strict convexity of \(z^p\). The unique-root sign classification therefore forces strict decrease of \(\wp_m(t)\) in either parameter.

**Limits.** As \(t\to\infty\), \(u\to0\) and \(G_p(u)\to2^p-2\), so \(\wp_m(t)\to p_m^*\). Uniformly for \(p\) near this value,
\[
G_p(u)=2^p-2+p(2^{p-1}-2)u+o(u),
\]
which gives the displayed \(1/t\) correction by implicit differentiation. As \(t\downarrow0\), for each fixed \(p<2\) the integral second-difference identity gives \(G_p(u)\to0\) as \(u\to\infty\); since \(G_2(u)=2\), the root tends to \(2\). Uniformly for \(p\in[3/2,2]\),
\[
G_p(u)=p(p-1)u^{p-2}\bigl(1+O(u^{-1})\bigr)
\quad(u\to\infty).
\]
Taking logarithms of the root equation yields \((2-\wp_m(t))\log(1/t)\to\log(m-1)\). Finally, for fixed \(u>0\), the strict convexity of \(z\log z\) proves \(h(u)=\partial_pG_p(u)|_{p=1}>0\). The implicit expansion of \(G_p(u)\) at \(p=1\) yields the stated \(O_t(m^{-2})\) inverse-branching law.

## Verification
The standalone standard-library checker `verify_weighted_corona_roundness.py` constructs the weighted graph and computes shortest paths independently. It checks 576 exact rational zero-sum quadratic identities at powers \(1,2,3\), 105 real-power full zero-sum inertia profiles below/at/above the threshold, parameter monotonicity, and numerical asymptotic diagnostics. Its successful terminal line is `ALL_WEIGHTED_CORONA_ROUNDNESS_CHECKS_OK`. All-order correctness rests on the analytic proof and the cited downward-propagation theorem, not the finite checks. Run with `python3 verify_weighted_corona_roundness.py`.

## Relationship to prior work
Li and Weston prove strict downward propagation of negative type, used above to establish root uniqueness. Sánchez gives a general finite-metric distance-matrix criterion and evaluates complete bipartite shortest-path metrics, not the weighted complete-corona threshold. Ferdi, Baskoro and Santika study quadratic embedding constants for corona graphs, but their distance form uses the first power \(d\) and does not determine the variable-power threshold or the singular pendant-length law. An independently accessible classification of general-position sets for unweighted complete-graph coronas counts geodesically noncollinear vertex sets, a distinct invariant; it does not imply negative-type assertions. The present calculation determines the full positive-\(p\) interval, equality space, Euclidean ranks and sharp length-asymptotic behavior for this specific family.

## Limitations
The result assumes a complete core, exactly one private leaf per core vertex, a common positive pendant length, and shortest-path (not electrical-resistance) distance. It does not classify arbitrary core graphs, different pendant lengths on different vertices, or full powered-distance inertia beyond the endpoint. Matching statements in unindexed literature remain a publication-priority risk. The \(t=0\) comparison refers to the metric quotient after identified zero-distance pairs; the model with \(2m\) distinct vertices is only defined for \(t>0\).

## References
1. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first posted 2009-01-06), Theorem 5.4. https://arxiv.org/abs/0901.0695
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first posted 2011-08-02), Sections 2--3. https://arxiv.org/abs/1108.0451
3. Ferdi, E. T. Baskoro and A. P. Santika, *Further Results on the Quadratic Embedding Constants of Corona Graphs*, arXiv:2603.14962 (posted 2026-03-16), Sections 1 and 4. https://arxiv.org/abs/2603.14962
