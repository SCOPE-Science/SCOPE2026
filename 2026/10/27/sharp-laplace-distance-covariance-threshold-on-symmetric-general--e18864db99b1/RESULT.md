# Sharp Laplace-distance covariance threshold on symmetric generalized hexagons

## Finding
Let \(\Gamma\) be the point–line incidence graph of any finite generalized hexagon of order \((q,q)\), where \(q\ge 2\) is an integer and such a hexagon exists. Write \(d(v,w)\) for graph distance, and for each real \(a\ge 0\) put
\[
K_a(v,w)=\exp\bigl(-a\,d(v,w)\bigr).
\]
Then the matrix \(K_a\) is positive semidefinite if and only if
\[
\boxed{a=0\quad\text{or}\quad a\ge \log q.}
\]
Writing \(N=2(q+1)(q^4+q^2+1)\) for the number of point-and-line vertices, its rank is exactly \(1\) at \(a=0\), exactly \(N-1\) at \(a=\log q\), and exactly \(N\) for \(a>\log q\). In particular, the ordinary graph distance is not conditionally negative semidefinite. The result is independent of the isomorphism type or any automorphism-transitivity assumption for the generalized hexagon.

## Assumptions and scope
A finite generalized hexagon of order \((q,q)\) is a point–line incidence geometry with \(q+1\) points on every line and \(q+1\) lines through every point, whose incidence graph is bipartite with diameter six and girth twelve. The theorem applies to every such geometry, not just a selected realization. The parameter \(a\) is real and nonnegative; the definition uses unweighted shortest-path distance in the incidence graph, with values from zero through six. Positive semidefiniteness is the condition \(\sum_{v,w}\overline{c_v}c_w K_a(v,w)\ge0\) for all complex coefficients \((c_v)\).

## Proof
Let \(A=A_1\) be the adjacency matrix, and for \(0\le j\le6\) let \(A_j\) denote the zero-one distance-\(j\) matrix, so \(A_0=I\). Girth twelve forces a unique geodesic between two vertices at distance at most five: distinct geodesics of length at most five would yield a cycle of length at most ten. Every vertex at distance between one and five from a fixed vertex therefore has exactly one neighbor in the preceding distance layer, and \(q\) in the following layer. At distance six, every one of its \(q+1\) neighbors lies in layer five. The intersection array is consequently
\[
\{q+1,q,q,q,q,q;\ 1,1,1,1,1,q+1\}.
\]
It follows that \(A_j=P_j(A)\), where \(P_0(x)=1\), \(P_1(x)=x\), \(P_2(x)=x^2-q-1\),
\[
P_j(x)=xP_{j-1}(x)-qP_{j-2}(x)\quad(3\le j\le5),
\]
and
\[
P_6(x)=\frac{xP_5(x)-qP_4(x)}{q+1}.
\]
The final relation \(AA_6=qA_5\) implies
\[
xP_6(x)-qP_5(x)=\frac{x(x^2-q)(x^2-3q)(x^2-(q+1)^2)}{q+1}.
\]
Since the graph has diameter six, its seven distance matrices are linearly independent, and these seven roots are precisely the adjacency eigenvalues:
\[
q+1,\;-(q+1),\;0,\;\pm\sqrt q,\;\pm\sqrt{3q}.
\]
The distance layer sizes are \(1\), then \((q+1)q^{j-1}\) for \(1\le j\le5\), then \(q^5\) for \(j=6\). Thus \(N=2(q+1)(q^4+q^2+1)\).

Put \(z=e^{-a}\) and \(u=\sqrt q\,z\). The radial kernel matrix is \(K_a=\sum_{j=0}^6z^jA_j\). Its eigenvalue on the adjacency eigenspace with eigenvalue \(\theta\) is \(F_\theta(z)=\sum_{j=0}^6z^jP_j(\theta)\). Direct substitution and factorization give the complete simultaneous spectrum:
\[
\begin{aligned}
F_{q+1}(z)&=(1+z)(1+qz)(1-qz+q^2z^2)(1+qz+q^2z^2),\\
F_{-(q+1)}(z)&=(1-z)(1-qz)(1+q^2z^2+q^4z^4),\\
F_0(z)&=(1-z^2)(1-u^2+u^4),\\
F_{\sqrt q}(z)&=(1-z^2)(1+u)(1-u^3),\\
F_{-\sqrt q}(z)&=(1-z^2)(1-u)(1+u^3),\\
F_{\sqrt{3q}}(z)&=(1-z^2)(1+u^2)(1+u^2+\sqrt3\,u),\\
F_{-\sqrt{3q}}(z)&=(1-z^2)(1+u^2)(1+u^2-\sqrt3\,u).
\end{aligned}
\]
For \(0<z\le1/q\) we have \(0<u\le1/\sqrt q<1\). Every listed eigenvalue is then strictly positive, except \(F_{-(q+1)}(1/q)=0\). In particular, \(1-u^2+u^4>0\) and \(1+u^2-\sqrt3\,u=(u-\sqrt3/2)^2+1/4>0\); all other signs follow from their displayed factors. If \(1/q<z<1\), the eigenvalue \(F_{-(q+1)}(z)\) is strictly negative. At \(z=1\) the matrix is the all-ones matrix. This proves the positive-semidefiniteness classification.

The incidence graph is connected, regular, and bipartite, so its eigenvalue \(-(q+1)\) is simple. Hence the zero eigenvalue of \(K_{\log q}\) has multiplicity one; all remaining eigenvalues are positive. When \(a=0\), the all-ones matrix has rank one; for \(a>\log q\), every eigenvalue is positive. Finally, if \(d\) were conditionally negative semidefinite, Schoenberg's exponential theorem would make \(e^{-ad}\) positive semidefinite at every \(a>0\), contrary to the interval \(0<a<\log q\).

## Verification
A standalone file `check_hexagon.py` reconstructs the seven distance polynomials, checks the characteristic polynomial identity and all seven factorizations symbolically over an indeterminate \(q\), and verifies endpoint signs for six integer parameter values. Run `python check_hexagon.py` with Python 3 and SymPy. The symbolic identities support the universal computation, while the sign and multiplicity arguments above establish the result for every admissible \(q\); finite spot checks alone are not used as an infinite proof.

## Relationship to prior work
The spectral-excess literature develops predistance polynomials and spectral methods for distance-regular and bipartite distance-biregular graphs. In particular, Fiol's 2013 treatment and the 2014 survey of van Dam, Koolen, and Tanaka provide the general spectral framework. The claim here is not the adjacency spectrum or the general spectral technique: it is the fully factored exponential-distance spectrum and its sharp positivity/rank classification for diameter-six generalized-hexagon incidence metrics. Generalized-quadrangle and projective-plane incidence geometries have different diameters and do not imply this statement by subspace restriction. A completely equivalent unpublished or unindexed specialization of association-scheme theory cannot be excluded by the bounded literature comparison.

## Limitations
This theorem concerns equal-order generalized hexagons and the single distance exponential \(e^{-a d}\); it does not classify unequal-order generalized hexagons, arbitrary powered-distance kernels, or numerical conditioning away from the positivity threshold. No independent mathematical validation is claimed. Its novelty assessment is limited by the coverage of searchable and accessible literature.

## References
1. M. A. Fiol, *The spectral excess theorem for distance-biregular graphs*, arXiv:1304.4354, first posted 2013-04-16, https://arxiv.org/abs/1304.4354.
2. E. R. van Dam, J. H. Koolen, H. Tanaka, *Distance-regular graphs*, arXiv:1410.6294, first posted 2014-10-23, https://arxiv.org/abs/1410.6294.
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44** (1938), 522–536, for the exponential characterization of conditionally negative semidefinite kernels.
