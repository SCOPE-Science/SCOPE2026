# Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles

## Finding
For an integer \(n\ge3\) and a real parameter \(0<\lambda\le1\), let \(C_n(\lambda)\) be the weighted cycle with \(n-1\) edges of length \(1\) and one edge of length \(\lambda\), equipped with the resulting shortest-path metric. Let \(X_{n,\lambda}=\mathcal F(C_n(\lambda))\) be its **real** Lipschitz-free space. Set \(p=n-1\) and
\[
\gamma_{p,\lambda}=\frac{p(p-1)}{p^2-\lambda^2},\qquad
E_{p,\lambda}=\begin{cases}
(p-1)\left(1+\lambda^2/p\right),&p\text{ odd},\\
p-2\lambda+(1-1/p)\lambda^2,&p\text{ even}.
\end{cases}
\]
Then the **exact, unrestricted** Euclidean Banach--Mazur distance is
\[
\boxed{d_{\mathrm{BM}}\left(X_{n,\lambda},\ell_2^p\right)^2
=1+\gamma_{p,\lambda}E_{p,\lambda}.}
\]
In particular, the distance strictly **increases** as the exceptional edge length increases when \(n\) is even, and strictly **decreases** when \(n\) is odd. At the unit-edge endpoint \(\lambda=1\), its square is \(n-1\) for even \(n\), and \((n-1)^2/n\) for odd \(n\). Both cases arise from one optimal ellipsoid computation.

## Assumptions and scope
All scalars are real. A graph edge is weighted by its positive length and the vertex metric is the corresponding shortest-path distance. Since the other route between the endpoints of each edge is longer, every cycle edge is metrically essential for \(0<\lambda\le1\). The Lipschitz-free space is defined as the zero-total-mass molecule space with the optimal-transport norm; it has dimension \(n-1\). The multiplicative Banach--Mazur distance \(d_{\mathrm{BM}}(X,\ell_2^p)\) is the infimum of \(\|T\|\,\|T^{-1}\|\) over invertible real linear maps \(T:X\to\ell_2^p\).

## Proof
**1. Cycle transport quotient and dual cube section.** Give the edges a consistent cyclic orientation, and use their normalized molecules as generating vectors. The edge-coordinate presentation of graph Lipschitz-free spaces gives
\[
X_{n,\lambda}\cong\ell_1^n/\operatorname{span}\{w\},\qquad
w=(\underbrace{1,\ldots,1}_{p\text{ entries}},\lambda).
\]
Indeed, multiplying an edge's normalized molecule by its edge length gives an ordinary oriented incidence vector; their sum around the cycle vanishes, and this is the sole linear relation. Identify the quotient linearly with the Euclidean hyperplane \(H=w^\perp\) by orthogonal projection \(P\). Its norm unit ball and polar are
\[
K=\operatorname{conv}\{\pm Pe_j:1\le j\le n\},\qquad
K^\circ=H\cap[-1,1]^n.
\]
These formulas follow directly from the \(\ell_1\) quotient norm and the \(\ell_\infty\) annihilator norm.

**2. Why no nonsymmetric Euclidean structure is better.** For any positive definite quadratic form \(q\) on \(H\), put
\[
R(q)=\max_{v\in K}q(v),\qquad
S(q)=\max_{u\in K^\circ}q^*(u),
\]
where \(q^*\) denotes the quadratic form dual to \(q\) under the Euclidean pairing on \(H\). The square of the Euclidean distortion associated with \(q\) is \(R(q)S(q)\). To minimize, consider the group permuting the first \(p\) edge coordinates. It preserves \(K\). For any \(q\) there exist positive numbers \(a,b\) such that \(a\|z\|_K^2\le q(z)\le b\|z\|_K^2\) for every \(z\), with distortion \(\sqrt{b/a}\). Averaging \(q\) over this finite group preserves the inequalities and cannot increase the distortion. Every invariant quadratic form is a scalar on the zero-sum first-\(p\)-coordinate space and another scalar on the remaining one-dimensional component. Rescale the first coefficient to \(1\).

For \(z=(z_1,\ldots,z_{p+1})\in H\), write \(s=p^{-1}\sum_{j=1}^p z_j\), so that \(z_{p+1}=-ps/\lambda\). Every candidate invariant quadratic form can be written as
\[
q_c(z)=\sum_{j=1}^p(z_j-s)^2
+\frac{(p+\lambda^2)^2}{\lambda^2}c\,s^2,
\qquad c>0.
\]
Directly evaluating the projected coordinate vectors yields
\[
R(q_c)=\max\left\{c,\frac{p-1}{p}+\frac{\lambda^2}{p^2}c\right\}.
\]
The two arguments coincide at
\[
c_0=\frac{p(p-1)}{p^2-\lambda^2}=\gamma_{p,\lambda},\qquad 0<c_0<1.
\]

**3. Exhaustion of polar vertices.** For \(u\in H\), let \(\bar u=p^{-1}\sum_{j=1}^p u_j\), which equals \(-\lambda u_{p+1}/p\). Computing the dual form gives
\[
q_c^*(u)=\sum_{j=1}^p(u_j-\bar u)^2+\frac{u_{p+1}^2}{c}.
\]
Since this is strictly convex, its maximum over the cube section is attained at a vertex. Each vertex fixes at least \(p\) cube coordinates to signs. If \(p\) is odd, the only relevant vertex type has \(u_{p+1}=\pm1\), \(p-1\) of the first coordinates balanced between signs, and the remaining first coordinate equal to \(\mp\lambda\). Thus
\[
S(q_c)=(p-1)\left(1+\frac{\lambda^2}{p}\right)+\frac1c.
\]
For \(\lambda=1\), extra descriptions of cube corners give the same value. If \(p\) is even there are two vertex types: balanced signed first coordinates and \(u_{p+1}=0\), giving \(q_c^*=p\); or \(u_{p+1}=\pm1\), \(p-1\) signed first coordinates with imbalance \(\pm1\), and the final coordinate equal to \(\pm(1-\lambda)\), giving \(q_c^*=p-2\lambda+(1-1/p)\lambda^2+1/c\). Consequently
\[
S(q_c)=\begin{cases}
E_{p,\lambda}+1/c,&p\text{ odd},\\
\max\{p,E_{p,\lambda}+1/c\},&p\text{ even}.
\end{cases}
\]
These are all cube-section vertices: if a coordinate other than the distinguished one is free, the integer sum of the other first coordinates has parity \(p-1\), forcing the stated patterns; if the distinguished coordinate is free, signed first coordinates must sum to zero, which is possible only for even \(p\) (apart from duplicated endpoint cube corners). There are no unexamined maximizing types.

**4. Scalar minimization.** Write \(A=(p-1)/p\), \(k=\lambda^2/p^2\), and \(E=E_{p,\lambda}\). For \(c\le c_0=A/(1-k)\), the polar branch \(E+1/c\) is active. Indeed, for even \(p\), its crossing with the constant branch \(p\) occurs at \(c_1=1/(p-E)\), where
\[
\frac1{c_0}-(p-E)
=\frac{(1-\lambda)(p-(p-2)\lambda)}{p-1}\ge0.
\]
On \(0<c\le c_0\) the objective is
\[
R(q_c)S(q_c)=(A+kc)(E+1/c)=AE+k+A/c+kEc.
\]
Its derivative is \(-A/c^2+kE\), strictly negative here: \(E\le p\), \(k\le p^{-2}\), \(c_0<1\), and \(A\ge1/2\) imply \(kEc_0^2<A\). On \(c\ge c_0\), \(R(q_c)=c\). For odd \(p\), the objective is \(1+Ec\); for even \(p\), it is \(\max\{pc,1+Ec\}\). Both functions strictly increase. Thus the unique optimal invariant parameter is \(c_0\), with
\[
\min_{c>0}R(q_c)S(q_c)=c_0(E+1/c_0)=1+c_0E.
\]
The averaging step proves that this is also the minimum over **every** Euclidean pullback, establishing the theorem.

**5. Opposite parity derivatives.** If \(p\) is odd, differentiation of \(E/(p^2-\lambda^2)\) gives the positive numerator \(2\lambda(p-1)(p+1)\). If \(p\) is even, its derivative has numerator \(2[p^2(\lambda-1)-\lambda^2]<0\). Multiplication by \(p(p-1)>0\) preserves these signs. Substituting \(\lambda=1\) gives the stated endpoint values.

## Verification
The accompanying standalone script `verify.py` enumerates every vertex of \(H\cap[-1,1]^n\) with exact rational arithmetic, evaluates both the primal and polar quadratic forms directly, and compares their extremal products with the closed formula. It checks all \(p\in\{2,\ldots,9\}\) and seven rational values of \(\lambda\), or 56 cases. Representative exact squares are \(4/3\) at \((n,\lambda)=(3,1)\), \(3\) at \((4,1)\), \(16/5\) at \((5,1)\), and \(87/35\) at \((4,1/2)\). Run `python verify.py` with Python 3 and no third-party dependencies. The finite script checks arithmetic only; the proof above handles all integer dimensions and real parameters.

## Relationship to prior work
The weighted edge-coordinate quotient is already part of the finite-metric Lipschitz-free literature, particularly Theorem 4.1 of Alexander--Fradelizi--García-Lirola--Zvavitch. Dilworth--Kutzarova--Ostrovskii consider finite graph transportation-cost quotients and their distance to \(\ell_1\)-type spaces. Cúth--Doucha--Titkos describe linear isometries of graph Lipschitz-free spaces. These structural results motivate the model but do not give the Euclidean Banach--Mazur optimum for the weighted-cycle family. Numerical-index parity results for cycles concern a different invariant and do not imply a Banach--Mazur distance formula. The present statement is an exact finite-dimensional Euclidean distortion profile, not a new construction of the graph quotient.

## Limitations
The formula concerns real scalars, exactly one exceptional edge no longer than the others, and finite simple cycles. No claim is made for arbitrary edge-weight vectors, complex spaces, or the singular edge-collapse parameter \(\lambda=0\), where the dimension changes. The literature comparison cannot exclude every equivalent result in less accessible or unindexed sources.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (2018), Sections 1--2.
2. M. Alexander, M. Fradelizi, L. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, Theorem 4.1 and Section 4.
3. M. Cúth, M. Doucha, T. Titkos, *Isometries of Lipschitz-free Banach spaces*, arXiv:2402.08266v1 (2024), Sections 2 and 6.
