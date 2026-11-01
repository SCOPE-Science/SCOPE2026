# A unique six-vertex roundness resonance in matching-stretched bipartite metrics

## Finding

Take an integer \(n\ge3\) and a length \(s\in[1,3]\). Start from the balanced complete bipartite graph \(K_{n,n}\), label its vertex classes \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), give the matched edges \(a_i b_i\) length \(s\), and give every other cross edge length \(1\). Let \(d_{n,s}\) be the **shortest-path** metric, including all \(2n\) vertices.

For \(p\ge0\), set
\[
A_p=2^p,\quad B_p=s^p,\quad
F_{n,s}(p)=(n-1)(A_p-1)-B_p,\quad
G_s(p)=B_p-A_p-1.
\]
The exact universal criterion is
\[
\boxed{d_{n,s}\text{ has }p\text{-negative type}\ \Longleftrightarrow\ F_{n,s}(p)\le0\text{ and }G_s(p)\le0.}
\]
At \(p=0\) all off-diagonal powered distances mean \(1\). The third eigenspace is always strictly negative.

Let \(\wp(n,s)\) be the supremal \(p\)-negative-type exponent. Define
\[
p_{\mathrm{hex}}=\log_2 3,\qquad s_{\mathrm{hex}}=4^{1/p_{\mathrm{hex}}}=2.398046289121215\ldots.
\]
For \(n=3\), \(s\mapsto\wp(3,s)\) is **strictly increasing** for \(1\le s\le s_{\mathrm{hex}}\) and **strictly decreasing** for \(s_{\mathrm{hex}}\le s\le3\), with unique global maximum
\[
\boxed{\wp(3,s_{\mathrm{hex}})=\log_2 3.}
\]
At this unique interior point the two critical eigenspaces collide. The snowflake \(d_{3,s_{\mathrm{hex}}}^{p_{\mathrm{hex}}/2}\) consists, up to Euclidean isometry, of the six vertices of a unit-side **regular planar hexagon**. No other parameter in this entire metric family has a two-dimensional critical Euclidean realization.

For \(n=4\), the supremal exponent increases strictly from \(\log_2(4/3)\) at \(s=1\) to \(1\) at \(s=3\); two critical modes coexist only at the endpoint \((s,p)=(3,1)\). For every \(n\ge5\), the supremal exponent is strictly increasing in \(s\) and is the unique positive root of
\[
\boxed{(n-1)(2^p-1)=s^p.}
\]
For \(n\ge5\) the root lies in \((0,1)\), including \(s=3\).

More explicitly, when the root \(F_{n,s}(p)=0\) occurs before \(G_s(p)=0\), the first zero-sum equality space has dimension \(1\); when the \(G_s\) root occurs first, its dimension is \(n-1\); at simultaneous equality it has dimension \(n\). Hence the least dimension of a Euclidean isometric embedding of \(d_{n,s}^{p/2}\) is \(2n-1\) for \(0\le p<\wp\), and **at** \(p=\wp\) it is
\[
\boxed{
\begin{cases}
4,&n=3,\ s<s_{\mathrm{hex}},\\
2,&n=3,\ s=s_{\mathrm{hex}},\\
3,&n=3,\ s>s_{\mathrm{hex}},\\
6,&n=4,\ s<3,\\
3,&n=4,\ s=3,\\
2n-2,&n\ge5.
\end{cases}}
\]
These are ranks, not approximate embedding dimensions; all critical endpoints are included in negative type.

Finally, with \(N=n-1\), uniformly over \(s\in[1,3]\),
\[
\boxed{\wp(n,s)=\frac1{N\log2}+
\frac{\log s/(\log2)^2-1/(2\log2)}{N^2}+O(N^{-3}).}
\]
Thus stretching all matching edges from length \(1\) to a fixed \(s>1\) improves the negative-type exponent by
\[\wp(n,s)-\wp(n,1)=\frac{\log s}{(\log2)^2(n-1)^2}+O((n-1)^{-3}).\]

## Assumptions and scope

A finite metric has \(p\)-negative type if \(z^{\mathsf T}D_pz\le0\) for every real vector \(z\) with \(\sum z_i=0\), where \((D_p)_{ij}=d(i,j)^p\) off the diagonal and the diagonal is zero. Strict negative type requires strict inequality for every nonzero such vector. At \(p=0\), powers are interpreted as one for distinct vertices. For \(0\le p\le\wp<2\), \(d^{p/2}\) is a metric and its Euclidean squared-distance matrix is \(D_p\).

For \(n\ge3\), any two distinct vertices in the same bipartition class have a two-edge path using an index different from both endpoints, and no shorter path; every nonmatching cross pair is adjacent with length one. A matching cross pair has a direct edge of length \(s\le3\), and any alternative route has at least three unit-length edges. Therefore distances are exactly \(2\) within a class, \(1\) across a nonmatched pair, and \(s\) across a matched pair, including the endpoint \(s=3\) where a direct matched edge may tie a three-edge route. There are no free, unquantified edge weights.

The primary MSC classification is 46B85 (negative type and Hilbert embeddings of finite metrics), not a claim about graph theory alone.

## Proof

**1. Complete zero-sum block decomposition.** Write \(J_n\) for the all-ones matrix. In the ordering \((a_1,\ldots,a_n,b_1,\ldots,b_n)\),
\[
D_p=\begin{pmatrix}
 A_p(J_n-I_n)&J_n+(B_p-1)I_n\\
 J_n+(B_p-1)I_n&A_p(J_n-I_n)
\end{pmatrix}.
\]
For a real zero-sum vector \(z=(x,y)\), put \(a=n^{-1}\sum_i x_i=-n^{-1}\sum_i y_i\), \(u=x-a\mathbf1\), \(v=y+a\mathbf1\). Both \(u\) and \(v\) have coordinate sum zero. Let \(w_+=(u+v)/\sqrt2\) and \(w_-=(u-v)/\sqrt2\). Direct multiplication, with all cross terms vanishing, gives the **identity for every** such \(z\):
\[
\boxed{
z^{\mathsf T}D_p z=2na^2 F_{n,s}(p)
+G_s(p)\|w_+\|_2^2
+H_s(p)\|w_-\|_2^2,\quad H_s(p)=1-A_p-B_p<0.}
\]
The three mutually orthogonal sectors have respective dimensions \(1,n-1,n-1\). Thus the two displayed scalar inequalities are necessary and sufficient for negative type, with exact equality multiplicities. At \(p=0\), all three eigenvalues equal \(-1\).

**2. Location and uniqueness of the first root.** If \(1\le s\le2\), then \(G_s(p)<0\) for every \(p>0\). The quotient
\[Q_s(p)=\frac{s^p}{2^p-1}\]
is strictly decreasing for all \(p>0\), diverges as \(p\downarrow0\), and tends to \(0\) if \(s<2\), or to \(1\) if \(s=2\). Since \(n-1\ge2\), the equation \(Q_s(p)=n-1\) has exactly one positive root. It is the negative-type endpoint.

Now suppose \(2<s\le3\). The equation \(G_s(p)=0\), equivalent to
\[(s/2)^p=1+2^{-p},\]
has one positive root \(g(s)\): the left side increases strictly from \(1\), the right side decreases strictly from \(2\). Moreover \(g(3)=1\), and \(g(s)>1\) for \(s<3\).

The quotient \(Q_s(p)\) is strictly decreasing on \((0,g(s)]\). Indeed, for \(t=2^p>1\), the function
\[h(t)=t\log t-(t-1)\log(t+1)\]
satisfies \(h(1)=0\) and
\[h'(t)=-\log(1+1/t)+2/(t+1)>0,\]
since \(\log(1+1/t)<1/t\le2/(t+1)\). Whenever \(p\le g(s)\), we have \(s^p\le2^p+1\), whence
\[
\log s\le\frac{\log(t+1)}p
<\frac{t\log2}{t-1}.
\]
Consequently \((\log Q_s)'=\log s-(2^p\log2)/(2^p-1)<0\). Thus \(F_{n,s}\) has at most one zero before \(g(s)\), and it has one precisely when \(F_{n,s}(g(s))>0\). Equality gives simultaneous roots. By the interval theorem for negative type, once the first strictness failure occurs, no larger exponent can restore negative type.

At \(p=g(s)\), one has \(s^p=2^p+1\), so
\[F_{n,s}(g(s))=(n-2)2^{g(s)}-n.\]
Write \(p_n=\log_2(n/(n-2))\). The sign changes exactly when \(g(s)=p_n\). The corresponding length is
\[s_n=\bigl(2(n-1)/(n-2)\bigr)^{1/p_n}.\]
For \(n=3\), \(p_3=\log_2 3>1\), so the unique crossing is the interior length \(s_3=s_{\mathrm{hex}}\in(2,3)\). Below it the \(F\) root comes first, and above it the \(G\) root comes first. For \(n=4\), \(p_4=1\), so equality occurs only at \(s=3\). For \(n\ge5\), \(p_n<1\le g(s)\), so the \(F\) root always comes first. This proves the full classification. For \(n\ge5\), \(F_{n,s}(1)=(n-1)-s\ge n-4>0\), so its first root is below one.

Because \(F_{n,s}(p)\) decreases strictly as \(s\) increases at any fixed \(p>0\), its first root increases strictly with \(s\) wherever the \(F\)-mode is first (by monotonicity of \(Q_s\)). The \(G\)-root \(g(s)\) decreases strictly with \(s\) for \(s>2\). This proves the unique strict maximum in the six-vertex family and the strict monotonicity for larger \(n\).

**3. Critical ranks and the hexagon.** The centered Euclidean Gram matrix of the snowflake \(d^{p/2}\) is \(-\tfrac12 H D_pH\), with \(H=I-\mathbf1\mathbf1^{\mathsf T}/(2n)\). Its nonzero spectrum consists of the negative zero-sum eigenvalues above, multiplied by \(-1/2\). Below the critical exponent all \(2n-1\) zero-sum eigenvalues are negative. At the endpoint the multiplicities of critical eigenvalues are exactly \(1\), \(n-1\), or \(n\), depending on which mode first vanishes. Their subtraction from \(2n-1\) gives each dimension in the finding.

For \(n=3\), simultaneous equality requires \(2^p=3\) and \(s^p=4\). Place six points in alternating \(a\)- and \(b\)-classes around a unit-side regular hexagon: the squared distances between adjacent cross-class nonmatched pairs, same-class pairs two steps apart, and matched cross-class opposite pairs are respectively \(1,3,4\). These are exactly the powered distances at \(p=p_{\mathrm{hex}}\), \(s=s_{\mathrm{hex}}\). Positive Gram rank two proves this is the unique planar case, up to Euclidean isometry.

For \(n=4,s=3,p=1\), the spectrum has a four-dimensional zero-sum equality space, so the minimum Euclidean snowflake dimension is three. Here the weighted metric coincides with the ordinary three-cube Hamming distance, and its square-root snowflake has the standard cubical realization in \(\mathbb R^3\).

**4. Uniform large-size asymptotics.** For every \(n\ge5\) the endpoint is the \(F\)-root. Put \(N=n-1\), \(\varepsilon=1/N\), and \(p=\varepsilon y\). The exact equation becomes
\[\frac{e^{\varepsilon y\log2}-1}{\varepsilon}=e^{\varepsilon y\log s}.\]
The left-minus-right expression extends analytically to \(\varepsilon=0\) and has limit \(y\log2-1\), whose derivative in \(y\) is the nonzero constant \(\log2\). The analytic implicit-function theorem applies uniformly for \(s\in[1,3]\) on this compact parameter interval. Taylor expansion gives
\[y=\frac1{\log2}+\varepsilon\left(\frac{\log s}{(\log2)^2}-\frac1{2\log2}\right)+O(\varepsilon^2).\]
Multiplication by \(\varepsilon\) proves both uniform formulas. No finite numerical census is used in this limit argument.

## Verification

The accompanying `verify_matching_stretch.py` independently computes weighted shortest paths (not just the asserted three-distance formula), checks exact zero-sum quadratic identities using rational arithmetic, and verifies centered Gram ranks at the two simultaneously singular configurations. It also diagnoses critical phases on a finite parameter grid and checks the asymptotic Taylor formula at high precision. To reproduce: `python3 verify_matching_stretch.py` with Python, NumPy, SciPy and mpmath installed. Its completed output records 528 rational shortest-path tests, 864 exact quadratic identities, 153 critical mode/rank cases, 16 high-precision asymptotic diagnostics, and both special exact Gram ranks. The mathematical proof above establishes the universal quantifiers; these finite tests do not replace it.

## Relationship to prior work

Sánchez's 2011 finite-metric negative-type paper provides the general matrix criterion and explicitly evaluates the **unperturbed** complete bipartite graph; its balanced case is \(\wp(n,1)=\log_2(n/(n-1))\). Li and Weston establish the interval and strictness inheritance results used to pass from the first zero to the precise negative-type interval. Horak–LaRose–Moore–Rooney–Rosenthal (2010) treat ordinary four-point graph roundness on unweighted graphs, not this powered zero-sum classification with a continuous matching length. The unweighted crown endpoint \(s=3\) had also been evaluated previously, including its asymptotic correction; no independent novelty is attributed here to that fixed endpoint. The contribution is the **full matching-stretch interpolation**, its unique interior resonance and planar Hilbert realization on six points, and the uniform interpolation asymptotic. General matrix criteria are methodological antecedents, not evaluated formulas for this family.

## Limitations

All nonmatching cross edges have unit weight, all matching edges share one length in the closed interval \([1,3]\), both classes have equal size \(n\ge3\), and the metric includes all graph vertices. There is no assertion for unequal class sizes, nonuniform matching lengths, longer matched edges (which become metrically truncated), or Hilbert embeddings of the **unsnowflaked** metric. The phase diagram is exact; the displayed decimals and finite checker are corroborative only. Unindexed literature may contain equivalent weighted symmetric-metric calculations; this result has not undergone independent mathematical review.

## References

1. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first public version 2009-01-06), in particular its interval and strictness results. https://arxiv.org/abs/0901.0695
2. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first public version 2011-08-02), especially Section 3 and Theorem 3.1 on complete bipartite graph metrics. https://arxiv.org/abs/1108.0451
3. M. Horak, E. LaRose, J. Moore, M. Rooney, H. Rosenthal, *Roundness properties of graphs*, Involve 3 (2010), 67–91, doi:10.2140/involve.2010.3.67. https://msp.org/involve/2010/3-1/involve-v3-n1-p05-p.pdf
