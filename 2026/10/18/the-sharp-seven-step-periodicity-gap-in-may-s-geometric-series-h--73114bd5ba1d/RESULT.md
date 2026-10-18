# The sharp seven-step periodicity gap in May's geometric-series host–parasitoid map

## Finding
Consider May's host–parasitoid system at the geometric-series aggregation parameter \(k=1\). After positive coordinate rescaling, its map is
\[
F_\lambda(x,y)=\left(\frac{xy}{1+x},\frac{\lambda y}{1+x}\right),
\qquad x>0,\ y>0,\ \lambda>1.
\]
For **every** \(\lambda>1\), every positive periodic point has least period either \(1\) or at least \(7\): there are **no primitive periods \(2,3,4,5,6\)**. This period bound is sharp: at \(\lambda=5\), the map has a strictly positive orbit of least period exactly \(7\). Its unique positive fixed point is \((\lambda-1,\lambda)\).

## Assumptions and scope
The biological model has positive host abundance \(H\), parasitoid abundance \(P\), attack coefficient \(a>0\), host reproduction \(\lambda>1\), and geometric-series escape probability \((1+aP)^{-1}\). It obeys
\[
H'=\frac{\lambda H}{1+aP},\qquad P'=H-\frac{H'}{\lambda}=\frac{aHP}{1+aP}.
\]
With \(x=aP\) and \(y=aH\) these equations become \(F_\lambda\). All periodicity claims concern the **strictly positive quadrant**, not boundary trajectories or other aggregation exponents. A periodic orbit's least period means the smallest positive integer \(q\) with \(F_\lambda^q(x,y)=(x,y)\).

## Proof
**1. Scalar recurrence and reconstruction.** For a positive trajectory write the first coordinates as \(x_n\). Eliminating \(y_n\) gives
\[
x_{n+1}=\frac{x_ny_n}{1+x_n},\quad y_{n+1}=\frac{\lambda y_n}{1+x_n},\quad
x_{n+2}x_n=\frac{\lambda x_{n+1}^2}{1+x_{n+1}}.\tag{1}
\]
Conversely, any positive bi-infinite solution of (1) lifts uniquely to a positive trajectory of the planar map using
\[
y_n=\frac{x_{n+1}(1+x_n)}{x_n};
\]
the second component then follows from (1). If \((x_n)\) is \(q\)-periodic, so is the lifted planar trajectory, with the same least period (the lift determines \(y_n\) uniquely).

**2. The sharp obstruction for short periods.** Set \(u_n=\log x_n\) and \(g(u)=\log\lambda-\log(1+e^u)\). Equation (1) is precisely
\[
u_{n+1}-2u_n+u_{n-1}=g(u_n),\qquad
-1<g'(u)=-\frac{e^u}{1+e^u}<0.\tag{2}
\]
Let \(u_0,\ldots,u_{q-1}\) be a nonconstant real periodic sequence satisfying (2), with cyclic subscripts and mean \(\bar u=q^{-1}\sum_{j=0}^{q-1}u_j\). Multiplying (2) by \(u_j-\bar u\) and summing by parts gives exactly
\[
\sum_{j=0}^{q-1}(u_{j+1}-u_j)^2
=-\sum_{j=0}^{q-1}(u_j-\bar u)\,[g(u_j)-g(\bar u)]
<\sum_{j=0}^{q-1}(u_j-\bar u)^2.\tag{3}
\]
The last inequality is **strict**: \(g\) is strictly decreasing with absolute slope strictly less than \(1\) on every finite interval, and at least one \(u_j\ne\bar u\). The cyclic discrete Wirtinger inequality, obtained by diagonalizing the circulant first-difference operator in the discrete Fourier basis, states
\[
\sum_{j=0}^{q-1}(u_{j+1}-u_j)^2
\ge 4\sin^2(\pi/q)\sum_{j=0}^{q-1}(u_j-\bar u)^2.\tag{4}
\]
For each integer \(2\le q\le6\), \(4\sin^2(\pi/q)\ge1\), contradicting (3). Hence no nonconstant periodic sequence has any of these periods. A constant positive sequence in (1) must have \(x=\lambda-1\), and the lifted fixed point has \(y=\lambda\). This also rules out all primitive periods \(2\) through \(6\), including the equality case \(q=6\).

**3. A certified period-seven orbit.** Fix \(\lambda=5\) and seek a palindromic positive period-seven scalar sequence
\[
(X,Y,Z,W,W,Z,Y).\tag{5}
\]
Equation (1) at the first three distinct positions forces the positive functions
\[
Y(X)=X\sqrt{\frac5{1+X}},\qquad
Z(X)=\frac{5Y(X)^2}{X(1+Y(X))},\qquad
W(X)=\frac{5Z(X)^2}{Y(X)(1+Z(X))}.\tag{6}
\]
The remaining independent cyclic equation at the midpoint \(W\) is
\[
Z(X)(1+W(X))=5W(X),
\]
equivalently \(R(X)=0\), where
\[
R(X)=5Z(X)(5-Z(X))-Y(X)(1+Z(X)).\tag{7}
\]
These functions are continuous and positive as appropriate for all \(X>0\). At two **exact rational endpoint evaluations**,
\[
\begin{aligned}
X=41/4:&\quad Y=41/6,\ Z=410/141,\ R=49241/13254>0,\\
X=19:&\quad Y=19/2,\ Z=95/42,\ R=-19/882<0.
\end{aligned}\tag{8}
\]
The intermediate value theorem supplies \(X_*\in(41/4,19)\) with \(R(X_*)=0\). Equations (6)–(7) make every cyclic occurrence of (1) hold for (5). Its positive planar lift is therefore genuinely period-seven. Because \(X_*>41/4\ne4\), this orbit is not the fixed point at \(\lambda=5\). Since \(7\) is prime, a nonfixed orbit of period dividing \(7\) has least period exactly \(7\). This proves sharpness.

## Verification
Run `python check.py` using Python's standard library. Its exact rational arithmetic independently checks both endpoint triples and the two strict signs in (8), along with the algebraic midpoint closure identity. It also checks a numerically approximated period-seven planar orbit as a diagnostic. Output is `VERIFY_OK`. The infinite, all-parameter nonexistence theorem is proved by (2)–(4), **not** by finite computation or numerical convergence. The source files contain the checker in full.

## Relationship to prior work
May's 1978 negative-binomial host–parasitoid model introduces the underlying family, identifies \(k=1\) with the geometric series, and treats equilibrium/local stability rather than prime-period exclusion. Camouzis and Kotsios (2021) analyze boundedness and nonautonomous variation of precisely the geometric-series model; their period-six limit occurs in a coefficient regime allowing zero coefficients, outside the constant strictly positive regime considered here. Bula (2016) found an analogous first admissible period seven for the **different** recurrence \(z_{n+1}=\alpha/((1+z_n)z_{n-1})\), whose numerator has no quadratic current-state factor. Neither that equation nor its period-seven classification algebraically implies (1) as stated. Chatzarakis et al. (2019) investigate a generalized rational recurrence encompassing (1) at a boundary parameter; their indexed two-cycle result is consistent with the present exclusion, but an available full-text comparison was not completed.

## Limitations
The theorem says nothing about global boundedness, stability of the period-seven orbit, occurrence of period seven at every \(\lambda>1\), or the set of admissible periods above seven. No exhaustive uniqueness claim is made regarding the research literature. The 2019 generalized-recurrence article could not be inspected in full; it remains a real potential overlap risk. Independent scientific validation has not been performed. The earliest relevant primary source is May's October 1978 publication; the cited metadata service indexes its date as 1978-10-01, whereas the printed journal issue specifies only October 1978.

## References
1. Robert M. May, *Host-Parasitoid Systems in Patchy Environments: A Phenomenological Model*, Journal of Animal Ecology **47** (1978), 833–844. DOI: 10.2307/3674. Full author-accessible scan: https://sites.ifi.unicamp.br/aguiar/files/2014/10/RobertMay-1978.pdf.
2. E. Camouzis and S. Kotsios, *May's Host–Parasitoid geometric series model with a variable coefficient*, Results in Applied Mathematics **11** (2021), 100160. DOI: 10.1016/j.rinam.2021.100160. Full open-access text: https://www.researchgate.net/publication/351228226.
3. Inese Bula, *Periodic Solutions of the Second Order Quadratic Rational Difference Equation*, in *Difference Equations, Discrete Dynamical Systems and Applications* (2016), pp. 29–47. DOI: 10.1007/978-3-662-52927-0_3.
4. G. E. Chatzarakis, E. M. Elabbasy, O. Moaaz and H. Mahjoub, *Global Analysis and the Periodic Character of a Class of Difference Equations*, Axioms **8** (2019), 131. DOI: 10.3390/axioms8040131 (partial material only inspected).
