# Exact no-loss meshes for the full Carathéodory–Fejér interval problem
## Finding
For integers \(n\ge3\) and \(N\ge3\), define
\[
M_N^{[n]}=\sup\left\{\lambda\in\mathbb R:\exists c_2,\ldots,c_n\in\mathbb R,\ 1+\lambda\cos(2\pi r/N)+\sum_{k=2}^n c_k\cos(2\pi kr/N)\ge0\ \text{for every }r\in\mathbb Z_N\right\}.
\]
Then
\[
M_N^{[n]}\ge 2\cos\!\left(\frac{\pi}{n+2}\right),
\]
and equality holds if and only if
\[
2(n+2)\mid N.
\]
If \(2(n+2)\nmid N\), the inequality is strict; in aliased cases the left-hand side may be \(+\infty\).

This gives an exact no-loss sampling criterion for the classical full degree-\(n\) Carathéodory–Fejér extremal problem: sampling only on the cyclic \(N\)-grid preserves the continuous optimum exactly on the divisibility meshes \(2(n+2)\mid N\).

## Assumptions and scope
The coefficients \(c_2,\ldots,c_n\) are real, and the sampled polynomial is even. The harmonic set is the full interval \(\{2,3,\ldots,n}\); the theorem does not concern singleton-harmonic restrictions. The restriction \(n\ge3\) deliberately excludes the already separately treated quadratic case.

Put \(R=n+2\), \(\alpha=\pi/R\), and \(c=\cos\alpha\). The continuous Carathéodory–Fejér constant for degree at most \(n\) is \(2c\).

## Proof
First reconstruct the continuous extremal. By the Fejér–Riesz factorization, any nonnegative trigonometric polynomial of degree at most \(n\), normalized to have constant term \(1\), can be written
\[
T(t)=\left|\sum_{j=0}^n b_j e^{ijt}\right|^2,
\qquad
\sum_{j=0}^n |b_j|^2=1.
\]
Its first cosine coefficient is
\[
\lambda=2\operatorname{Re}\sum_{j=0}^{n-1} b_{j+1}\overline{b_j}.
\]
This is the Rayleigh quotient of the adjacency matrix of the path on \(n+1\) vertices. Its largest eigenvalue is \(2\cos(\pi/(n+2))=2c\), with eigenvector proportional to
\[
\bigl(\sin\alpha,\sin(2\alpha),\ldots,\sin((n+1)\alpha)\bigr).
\]
Hence the continuous optimum is exactly \(2c\).

Let
\[
B(z)=\sum_{j=0}^n \sin((j+1)\alpha)z^j,
\qquad
F(t)=\frac{2}R\left|B(e^{it})\right|^2.
\]
The elementary identity
\[
(1-2cz+z^2)B(z)=\sin\alpha\,(1+z^R)
\]
shows that the zeros of \(F\) are exactly
\[
t_j=(2j+1)\alpha,\qquad 1\le j\le n.
\]
They are the odd \(2R\)-th-root angles except the two cancelled angles \(\pm\alpha\). Since \(F\ge0\) on the whole circle, it is feasible on every cyclic grid, proving
\[
M_N^{[n]}\ge2c.
\]

Now define positive contact weights
\[
y_j=\frac{2}R\bigl(c-\cos t_j\bigr),\qquad 1\le j\le n.
\]
Summing over the full set of odd \(2R\)-th-root angles and removing \(\pm\alpha\) gives
\[
\sum_{j=1}^n y_j=2c,
\qquad
\sum_{j=1}^n y_j\cos t_j=-1,
\qquad
\sum_{j=1}^n y_j\cos(kt_j)=0\quad(2\le k\le n).
\]
If \(2R\mid N\), every \(t_j\) is an \(N\)-grid angle. Multiplying the sampled nonnegativity inequalities by \(y_j\) and summing eliminates every coefficient except the first one and yields
\[
0\le 2c-\lambda.
\]
Thus \(M_N^{[n]}=2c\) whenever \(2R\mid N\).

It remains to prove strictness on every other grid. If the sampled linear program is unbounded, strictness is immediate. Otherwise suppose its optimum equals \(2c\). Finite-dimensional linear-programming duality supplies nonnegative grid weights \(w_r\) satisfying
\[
\sum_r w_r=2c,
\qquad
\sum_r w_r\cos(2\pi r/N)=-1,
\qquad
\sum_r w_r\cos(2\pi kr/N)=0\quad(2\le k\le n).
\]
Evaluating these dual weights on the continuous extremizer \(F\) gives
\[
\sum_r w_r F(2\pi r/N)=0.
\]
Every summand is nonnegative, so positive dual mass can occur only at sampled contact zeros \(t_j\).

Symmetrize the dual weights under \(t\mapsto-t\), and aggregate them over the distinct contact cosine values \(x_a=\cos t_j\). There are \(m=\lceil n/2\rceil\) such values. The difference between these aggregate weights and the aggregate weights coming from the explicit positive \(y_j\) has zero Chebyshev moments
\[
\sum_a \delta_a T_k(x_a)=0\qquad(0\le k\le n).
\]
Since \(T_0,\ldots,T_{m-1}\) form a basis of the polynomials of degree less than \(m\), the Vandermonde matrix at the distinct \(x_a\) is invertible. Therefore every aggregate weight equals its explicit positive counterpart. Consequently every contact cosine value, and by grid symmetry every contact angle, must occur on the grid.

In particular the contact fractions \(3/(2R)\) and \(5/(2R)\) of a full turn both occur. Hence
\[
\frac{2R}{\gcd(2R,3)}\mid N
\qquad\text{and}\qquad
\frac{2R}{\gcd(2R,5)}\mid N.
\]
Their least common multiple is \(2R\), so \(2R\mid N\), contradicting the assumed off-mesh case. This proves the claimed if-and-only-if criterion.

## Verification
The proof is all-parameter and does not rely on finite enumeration. The included `verify.py` independently checks the explicit extremizer identity, the positive contact-weight moment identities, and the exact equivalence between inclusion of all contact roots in the cyclic grid and \(2(n+2)\mid N\), for \(3\le n\le80\) and \(3\le N\le500\). It reports `VERIFY_OK`.

The checker is corroborative only. In particular, its finite ranges are not used to infer the infinite theorem; the strict off-mesh assertion is supplied by the dual-support and Chebyshev–Vandermonde argument above.

## Relationship to prior work
Kolountzakis and Révész introduced the discretized Carathéodory–Fejér quantity \(M_m(H)\), observed the general relaxation inequality \(M_m(H)\ge M(H)\), and connected these problems to positive-definite functions. Their full text also records the classical continuous Carathéodory–Fejér value and the relevant continuous duality. The inspected material does not state the exact all-grid equality criterion for the full harmonic interval.

Krenedits and Révész later developed the same discrete problem on finite cyclic groups within a general locally compact Abelian framework. Their Proposition 3.3 proves convergence of the finite constants to the continuous constant for fixed finite support, and their Remark 7.4 records a finite duality relation. Those general results do not by themselves determine which individual grids already attain the continuous value. The present result supplies that exact arithmetic mesh classification for the full interval \(\{2,\ldots,n}\).

The degree-\(2\) full-interval case is intentionally not claimed here. Singleton-harmonic discretizations are also different feasible sets and do not imply the present full-interval theorem.

## Limitations
No closed formula is claimed for the strict excess \(M_N^{[n]}-2\cos(\pi/(n+2))\) when \(2(n+2)\nmid N\). Some off-mesh problems are unbounded because of harmonic aliasing; the theorem classifies exact equality with the continuous optimum, not the finite optimum in every off-mesh case.

The originality comparison cannot exclude an equivalent statement hidden under substantially different terminology such as circulant positive-definite sequences, Toeplitz linear programs, or graph-theoretic theta formulations. The directly matching full texts and searches inspected here did not reveal such a statement.

## References
M. N. Kolountzakis and Sz. Gy. Révész, “On pointwise estimates of positive definite functions with given support,” arXiv:math/0302193, first submitted 2003-02-17. Primary MSC 42B10.

S. Krenedits and Sz. Gy. Révész, “The Carathéodory–Fejér type extremal problem on locally compact Abelian groups,” arXiv:1304.0071, first submitted 2013-03-30. MSC 43A35, 43A70.
