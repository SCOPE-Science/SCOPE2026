# Sharp negative type and a fifth-power decay law for generalized-hexagon incidence metrics

## Finding

Let \(G\) be the point--line incidence graph of **any** finite thick generalized hexagon of order \((q,q)\), with integer \(q\ge2\), and let \(d\) be the unweighted shortest-path distance on its vertex set. Existence is assumed and is not asserted for every integer order.

Define
\[
F_q(p)=-(q+1)+q(q+1)2^p-q^2(q+1)3^p+q^3(q+1)4^p-q^4(q+1)5^p+q^5 6^p.
\]
There exists exactly one positive root \(\alpha_q\), and \(0<\alpha_q<1\). For every real \(p\ge0\), the matrix whose off-diagonal entries are \(d(u,v)^p\) and whose diagonal entries are zero is conditionally negative semidefinite **if and only if** \(0\le p\le\alpha_q\). It is strictly conditionally negative definite for \(0\le p<\alpha_q\). At \(p=\alpha_q\), its kernel on the zero-sum subspace consists precisely of multiples of the vector equal to \(+1\) on points and \(-1\) on lines.

Consequently, the minimum dimension of an exact Euclidean realization of the powered distances as squared Euclidean distances at the endpoint is
\[
2(q^3+1)(q^2+q+1)-2.
\]
Along any unbounded sequence of orders admitting the geometry,
\[
\alpha_q=\frac{1}{q^5\log(6/5)}+O(q^{-6}).
\]
Equivalently, \(\exp(-t d(u,v)^p)\) is positive semidefinite for every \(t>0\) precisely for \(0\le p\le\alpha_q\). This last equivalence is the classical Schoenberg criterion.

## Assumptions and scope

A generalized hexagon of order \((q,q)\) is a finite point--line incidence geometry with \(q+1\) points on every line, \(q+1\) lines through every point, incidence-graph diameter six and girth twelve. Throughout, \(q\) is an integer at least two and a corresponding hexagon is assumed to exist. The incidence graph is connected, bipartite and distance regular. Its number of vertices is \(v=2(q^3+1)(q^2+q+1)\). The definition at \(p=0\) is the off-diagonal constant-one matrix (zero diagonal).

Conditional negative semidefiniteness means \(\sum_{u,v}a_u a_v d(u,v)^p\le0\) for every real vector \(a\) with \(\sum_u a_u=0\). The Euclidean realization is of the squared-distance function \(d^p\), equivalently an embedding of \((V,d^{p/2})\), and is not claimed to preserve the original distance \(d\).

## Proof

**1. Distance-spectral reduction.** The intersection array is
\[
\{q+1,q,q,q,q,q;1,1,1,1,1,q+1\}.
\]
Let \(A\) be adjacency and \(A_j\) the distance-\(j\) matrices. The identity \(A_j=P_j(A)\) follows inductively from \(P_0(x)=1\), \(P_1(x)=x\), \(P_2(x)=x^2-(q+1)\),
\[
P_{j+1}(x)=xP_j(x)-qP_{j-1}(x)\quad (j=2,3,4),
\qquad P_6(x)=\frac{xP_5(x)-qP_4(x)}{q+1}.
\]
The final recurrence \(xP_6(x)=qP_5(x)\) gives the seven distinct adjacency eigenvalues
\[
q+1,\quad -(q+1),\quad 0,\quad \pm\sqrt q,\quad \pm\sqrt{3q}.
\]
Therefore the powered-distance matrix is \(D_p=\sum_{j=1}^{6}j^pP_j(A)\). Its eigenvalue on adjacency sector \(x\) is \(\Lambda_x(p)=\sum_{j=1}^{6}j^pP_j(x)\). All sectors other than \(q+1\) lie in the orthogonal complement of constants. The eigenvalue for the one-dimensional bipartition sector \(x=-(q+1)\) is exactly \(F_q(p)\).

**2. The bipartition sector is the largest centered eigenvalue for \(0<p<1\).** Put \(G_x(z)=\sum_{j=0}^{6}P_j(x)z^j\), where \(x\ne q+1\) is an adjacency eigenvalue. A direct substitution into the distance polynomials yields
\[
\begin{aligned}
G_{-(q+1)}(z)&=(1-z)(1-qz)(1+q^2z^2+q^4z^4),\\
G_0(z)&=(1-z^2)(1-qz^2+q^2z^4),\\
G_x(z)&=(1-z^2)(1-qz^2)(1+qz^2+xz),&&x^2=q,\\
G_x(z)&=(1-z^2)(1+qz^2)(1+qz^2+xz),&&x^2=3q.
\end{aligned}
\]
We claim \(G_x(z)>G_{-(q+1)}(z)\) for every \(0<z<1\) and each other nonprincipal \(x\). For \(1/q\le z<1\), the bipartition expression is nonpositive. The other three kinds of expressions are positive, except possibly \(x^2=q\) when \(z>1/\sqrt q\). In that last range the smaller sector is \(x=+\sqrt q\). Since \(qz-1\ge qz^2-1\ge0\), it suffices to compare \(1+q^2z^2+q^4z^4\) with \((1+z)(1+qz^2+\sqrt q z)\). Writing \(y=\sqrt qz\ge1\), the former is at least \(1+2y^2+4y^4\), whereas the latter is at most \(2(1+y^2+y)\); their difference is at least \(4y^4-2y-1>0\).

For \(0<z\le1/q\), set \(a=1/\sqrt q\in(0,3/4)\) and \(t=qz\in(0,1]\). The differences divided by \(t\) between each of \(G_0\), \(G_{-\sqrt q}\), and the lower surrogate of \(G_{-\sqrt{3q}}\) obtained by replacing \(\sqrt3\) with \(7/4\), and the bipartition expression, are bivariate polynomials. On substituting \(a=3u/4\), each has bidegree at most \((8,5)\). Every one of its 54 coefficients in the tensor-product Bernstein basis of bidegree \((8,5)\), on \(0\le u,t\le1\), is **strictly positive**. The exact minimum coefficients are, respectively, \(885/2048\), \(1677/10240\), and \(381/40960\). All 162 exact rational inequalities are reconstructed from first principles by the accompanying \(\texttt{verify.py}\); no floating-point sign inference is used in this certificate. The positive sectors with \(x=+\sqrt q\) or \(+\sqrt{3q}\) dominate their corresponding negative sectors in this range. Thus the claim follows throughout \(0<z<1\).

For \(0<p<1\), use \(r^p=\frac{p}{\Gamma(1-p)}\int_0^\infty(1-e^{-rt})t^{-1-p}\,dt\). Since \(\sum_{j=0}^6P_j(x)=0\) for any nonprincipal sector, this gives
\[
\Lambda_x(p)=-\frac{p}{\Gamma(1-p)}\int_0^\infty G_x(e^{-t})t^{-1-p}\,dt.
\]
The established strict comparison therefore implies \(\Lambda_x(p)<F_q(p)\) for all other nonprincipal adjacency sectors and every \(0<p<1\).

**3. Unique crossing.** Write \(\Delta_j(p)=j^p-(j-1)^p\). Summation by parts yields
\[
F_q(p)=-1+q\Delta_2(p)+q^2\{q\Delta_4(p)-\Delta_3(p)\}
+q^4\{q\Delta_6(p)-\Delta_5(p)\}.
\]
For \(p\ge0\), \(\Delta_j'(p)=j^p\log j-(j-1)^p\log(j-1)>0\). More generally, for \(j\ge2\), comparison of the integrals over adjacent unit intervals of \(\frac{d}{ds}(s^p\log s)=s^{p-1}(1+p\log s)\) gives \(\Delta_{j+1}'(p)\ge\frac{j-1}{j}\Delta_j'(p)\). Applying this at \(j=3\) and \(j=5\) shows \(F_q'(p)>0\) for every \(p\ge0\), since \(q\ge2\). Finally \(F_q(0)=-1\) and
\[
F_q(1)=(q-1)(q^2-q+1)(q^2+q+1)>0.
\]
Hence \(F_q\) has a unique positive zero in \((0,1)\). At and below it every centered eigenvalue is nonpositive; above it the bipartition eigenvalue is positive. At the zero the bipartition eigenspace is the entire centered nullspace, because the other comparisons are strict and bipartition has multiplicity one. Double-centering \(-D_{\alpha_q}/2\) yields a positive semidefinite Euclidean Gram matrix of rank \(v-2\).

**4. Asymptotic.** Differentiating \(F_q\) at zero gives \(F_q'(0)=q^5\log(6/5)+O(q^4)\). A uniform second-derivative bound \(F_q''(p)=O(q^5)\) for \(0\le p\le1\), together with the monotone crossing, yields \(\alpha_q=[q^5\log(6/5)]^{-1}+O(q^{-6})\).

## Verification

Run \(\texttt{python3 verify.py}\) (standard library only). The exact checker constructs the three rational bivariate polynomials, converts them to a tensor Bernstein basis, and checks all 162 strictly positive coefficients and their three minimum values. It also checks the distance-polynomial recurrence and endpoint spectral signs at orders \(2\) through \(9\) numerically, printing \(\texttt{VERIFY_OK}\). The direct numerical tests are supporting evidence and do not constitute an infinite-order proof; the recurrence, comparison inequalities and exact Bernstein certificate provide that proof.

Representative critical exponents: \(\alpha_2\approx0.176477589549845\), \(\alpha_3\approx0.029330881712536\), and \(\alpha_4\approx0.006849703743053\).

## Relationship to prior work

The classical negative-type criterion and its interval property are described in Sánchez (2011), who obtains a sharp classification for complete bipartite graph metrics. Exoo and Jajcay (2008), §2.2.3, give the geometry, diameter, girth and order of generalized-hexagon incidence graphs. The present result combines the generalized-hexagon distance algebra with an explicit all-order comparison of its powered-distance sectors; the cited sources' stated results do not imply the sharp hexagon threshold or its fifth-power decay without this additional argument. Analogous calculations for lower-diameter incidence geometries are not the same claim.

## Limitations

Only symmetric orders \((q,q)\) and finite incidence-graph vertex metrics are covered. Existence for every integer \(q\) is neither needed nor claimed. The theorem does not concern geodesic metric realizations of entire edges, generalized hexagons of order \((q,q^3)\), or arbitrary edge weights. The literature search was bounded; an older equivalent theorem in specialized distance-regular or association-scheme literature cannot be ruled out solely by unsuccessful searches. Independent mathematical validation has not been performed.

## References

1. Geoffrey Exoo and Robert Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics DS16, first version published 2008-09-29, §2.2.3. https://www.combinatorics.org/files/Surveys/ds16/ds16v1-2008.pdf
2. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first submitted 2011-08-02, §§1–3. https://arxiv.org/pdf/1108.0451
3. Hanfeng Li and Anthony Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695v1, 2009-01-06 (background on interval/strictness). https://arxiv.org/abs/0901.0695
