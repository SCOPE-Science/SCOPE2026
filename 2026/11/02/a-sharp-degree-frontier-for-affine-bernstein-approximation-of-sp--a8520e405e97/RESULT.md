# A sharp degree frontier for affine Bernstein approximation of spherical positive-definite kernels

## Finding

For every integer \(n\ge1\), define the ordinary affine Bernstein operator on \([-1,1]\) by
\[
(\mathcal B_n f)(t)=\sum_{j=0}^{n}\binom nj
f\!\left(-1+\frac{2j}{n}\right)
\left(\frac{1+t}{2}\right)^j
\left(\frac{1-t}{2}\right)^{n-j}.
\]
Let \(\mathcal P_d\) be the cone of continuous real-valued functions \(f:[-1,1]\to\mathbb R\) for which \((x,y)\mapsto f(x\cdot y)\) is positive semidefinite on the unit sphere \(S^d\subset\mathbb R^{d+1}\).

**Exact two-sphere frontier.** On \(S^2\), the operator \(\mathcal B_n\) maps every member of \(\mathcal P_2\) into \(\mathcal P_2\) if and only if \(n\in\{1,2,3\}\). Every degree \(n\ge4\) fails: the normalized Legendre polynomial \(P_{n+2}\) has a positive-semidefinite zonal kernel, while its Bernstein image has a strictly negative coefficient of \(P_n\). More precisely,
\[
\boxed{\ [P_n]\,\mathcal B_n[P_{n+2}]
=\frac{n!}{n^n}\,\frac{(2n+1)(3-n)}{6n}\ . }
\]
Here \([P_n]h\) denotes the coefficient multiplying \(P_n\) in the finite Legendre expansion of the polynomial \(h\).

**All-dimensional obstruction.** For any integer \(d\ge2\), put \(\lambda=(d-1)/2\) and \(Q_m^{(d)}(t)=C_m^{\lambda}(t)/C_m^{\lambda}(1)\), where \(C_m^\lambda\) is the Gegenbauer polynomial. Then
\[
\boxed{\ [Q_n^{(d)}]\,\mathcal B_n[Q_{n+2}^{(d)}]
=\frac{n!}{n^n}\frac{(n+\lambda)(d+1-n)}{3n}
\frac{(n+1)(n+2)}{(n+d-1)(n+d)}\ . }
\]
Consequently, **for every** \(d\ge2\) and \(n\ge d+2\), the operator \(\mathcal B_n\) does not preserve \(\mathcal P_d\). The statement does *not* assert that all lower degrees preserve the cone for \(d>2\).

## Assumptions and scope

All dimensions and Bernstein degrees are positive integers as specified. Spherical positive definiteness means nonnegative quadratic forms for every finite set of sphere points and complex coefficients; strict positive definiteness is not assumed. The dot-product variable is \(t\in[-1,1]\), **not** the geodesic-distance variable of the circle Bernstein operator. Gegenbauer polynomials have the conventional normalization \(C_m^\lambda(1)>0\); Legendre polynomials satisfy \(P_m(1)=1\). The bracket coefficient is a basis coefficient, not a pointwise function value.

By Schoenberg's spherical characterization, \(f\in\mathcal P_d\) exactly when it has a uniformly convergent expansion \(f=\sum_{m\ge0}a_mQ_m^{(d)}\) with \(a_m\ge0\) and \(\sum_m a_m<\infty\). This standard theorem is used as a premise, not claimed as new. For \(d=2\), \(Q_m^{(2)}=P_m\).

## Proof

### 1. An exact top Gegenbauer coefficient

Write \(x_j=-1+2j/n\) and introduce the centered difference
\[
\Delta_n F=\sum_{j=0}^n(-1)^{n-j}\binom nj F(x_j).
\]
Expanding the Bernstein basis in powers of \(t\) gives \([t^n]\mathcal B_nF=2^{-n}\Delta_nF\). Its exponential generating function is
\[
\sum_{j=0}^n(-1)^{n-j}\binom nj e^{zx_j}
=e^{-z}(e^{2z/n}-1)^n=(2\sinh(z/n))^n.
\]
Comparison of the coefficients of \(z^n\) and \(z^{n+2}\) proves the *exact* identities
\[
[t^n]\mathcal B_n[t^n]=\frac{n!}{n^n},\qquad
\frac{\Delta_n(t^{n+2})}{\Delta_n(t^n)}
=\frac{(n+1)(n+2)}{6n}.
\]
The two leading monomials of \(C_{n+2}^\lambda\) are
\[
C_{n+2}^\lambda(t)=A_{n+2}\left(
 t^{n+2}-\frac{(n+1)(n+2)}{4(n+\lambda+1)}t^n
\right)+R(t),\quad \deg R\le n-2,
\]
where \(A_m=2^m(\lambda)_m/m!\) is the leading coefficient. Lower-degree terms of the input cannot contribute to \([t^n]\mathcal B_n F\). Consequently,
\[
[t^n]\mathcal B_n C_{n+2}^\lambda
=A_{n+2}\frac{n!}{n^n}(n+1)(n+2)
\left(\frac1{6n}-\frac1{4(n+\lambda+1)}\right).
\]
The coefficient of the highest Gegenbauer basis element is the leading monomial coefficient divided by \(A_n\). Substituting
\[
\frac{A_{n+2}}{A_n}=
\frac{4(n+\lambda)(n+\lambda+1)}{(n+1)(n+2)}
\]
gives \([C_n^\lambda]\mathcal B_n[C_{n+2}^\lambda]
=(n!/n^n)(n+\lambda)(2\lambda+2-n)/(3n)\). The normalization ratio
\[
\frac{C_n^\lambda(1)}{C_{n+2}^\lambda(1)}
=\frac{(n+1)(n+2)}{(n+2\lambda)(n+2\lambda+1)}
\]
now gives the boxed all-dimensional formula because \(2\lambda+2=d+1\). Its sign is strictly negative when \(n\ge d+2\). Schoenberg's theorem then proves the all-dimensional failure statement: an input with a single positive Gegenbauer coefficient has an output with a negative one. Setting \(d=2\) yields the boxed Legendre identity.

### 2. Preservation in the three lowest degrees on \(S^2\)

It suffices, by positivity, linearity and uniform convergence of the Schoenberg expansion, to verify that \(\mathcal B_n[P_m]\) is a nonnegative linear combination of Legendre polynomials for every integer \(m\ge0\) and \(n=1,2,3\). The parity and endpoint identities \(P_m(-t)=(-1)^mP_m(t)\), \(P_m(1)=1\) give the following **exact** expansions.

For \(n=1\), even \(m\) gives \(P_0\), and odd \(m\) gives \(P_1\).

For \(n=2\), if \(m\) is even and \(v=P_m(0)\), then
\[
\mathcal B_2P_m=\frac{2+v}{3}P_0+\frac{1-v}{3}P_2.
\]
For odd \(m\), \(\mathcal B_2P_m=P_1\). Both coefficients in the even case are nonnegative since \(|P_m(t)|\le1\) on \([-1,1]\).

For \(n=3\), if \(m\) is even and \(v=P_m(1/3)\), then
\[
\mathcal B_3P_m=\frac{1+v}{2}P_0+\frac{1-v}{2}P_2,
\]
which is positive in the Legendre basis. For odd \(m\), instead,
\[
\mathcal B_3P_m=\frac{9+3v}{10}P_1+\frac{1-3v}{10}P_3.
\]
The first coefficient is nonnegative because \(v\ge-1\). To verify the second for **every** odd degree, observe the exact values
\[
P_1(1/3)=1/3,\quad P_3(1/3)=-11/27,\quad P_5(1/3)=1/3.
\]
For every odd \(m\ge7\), the classical Bernstein bound for Legendre polynomials states that, if \(t=\cos\theta\in(-1,1)\), then
\[
(\sin\theta)^{1/2}|P_m(\cos\theta)|<\sqrt{2/(\pi m)}.
\]
Since \(\sin(\arccos(1/3))=2\sqrt2/3\), it follows that
\[
|P_m(1/3)|<\sqrt{\frac{3}{\pi m\sqrt2}}
\le\sqrt{\frac{3}{7\pi\sqrt2}}<\frac13.
\]
The last strict comparison is equivalent to \(27<7\pi\sqrt2\). Therefore \(1-3v\ge0\) in every odd case, so \(\mathcal B_3\) preserves the full cone. This completes the sharp classification on \(S^2\).

## Verification

The standalone `CHECK.py` uses only Python standard-library exact rational arithmetic. It checks the boxed Gegenbauer formula for all \(2\le d\le9\) and \(1\le n\le12\), the specific \(n=4\), \(d=2\) coefficient \(-9/256\), and nonnegativity of every coefficient of \(\mathcal B_nP_m\) for \(n\in\{1,2,3\}\) and \(0\le m\le64\). The final checker replay passed 292 exact assertions. These are supplementary finite checks; the proof above establishes the unrestricted degree and dimension quantifiers. The sole external inequality required for the positive direction was verified in Gautschi–Giordano's printed Eq. (56).

To reproduce, run `python3 CHECK.py` from a directory containing this result and the checker.

## Relationship to prior work

Otten, Nguyen and Watts (2026) prove that the degree-\(n\) Bernstein operator in the **geodesic-distance variable on the circle** preserves positive definiteness for all \(n\). In their Section 4, they also explicitly evaluate the **affine** operator on \(S^2\) at \(n=4\), obtaining \([P_4]\mathcal B_4[P_6]=-9/256\). Their stated result does not give a classification of all affine degrees on \(S^2\), nor the dimension-dependent formula for all \(d,n\). The present result recovers their counterexample as its first negative case but does not conflate their successful circle operator with this unsuccessful affine one.

Schoenberg's Gegenbauer coefficient theorem supplies the kernel-positivity criterion, and the classical Bernstein pointwise inequality for Legendre polynomials supplies the only nonalgebraic estimate in the safe-degree proof. Dimension-walk constructions for spherical kernels use different operators and do not imply these formulas for ordinary Bernstein interpolation.

## Limitations

For \(d>2\), the result gives a necessary degree restriction \(n\le d+1\) for preservation, not a sufficiency theorem: the status of intermediate low degrees in higher sphere dimensions is not claimed. The result applies to ordinary equally spaced affine Bernstein sampling on \([-1,1]\), not arbitrary Bernstein-type or Gegenbauer-adapted operators, nor the geodesic-distance operator on \(S^1\). It is about positive semidefiniteness, not strict positive definiteness or quantitative errors in covariance approximation.

## References

1. M. Otten, N. Nguyen and T. W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836, first public version 2026-08-05, especially Theorem 1.2 and Section 4. https://arxiv.org/abs/2608.04836
2. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108. https://doi.org/10.1215/S0012-7094-42-00908-6
3. W. Gautschi and C. Giordano, *Luigi Gatteschi's work on asymptotics of special functions and their zeros*, Numerical Algorithms 49 (2008), 11–31, Section 5.3, Eq. (56). https://doi.org/10.1007/s11075-008-9208-5
4. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975, Theorem 7.3.3 (classical Legendre Bernstein inequality).
5. R. K. Beatson and W. zu Castell, *One-Step Recurrences for Stationary Random Fields on the Sphere*, SIGMA 12 (2016), 043, on distinct positivity-preserving dimension-walk operators. https://doi.org/10.3842/SIGMA.2016.043
