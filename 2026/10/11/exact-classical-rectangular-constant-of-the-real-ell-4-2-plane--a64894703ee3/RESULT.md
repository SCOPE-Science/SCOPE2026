# Exact classical rectangular constant of the real \(\ell_4^2\) plane
## Finding
Let \(X=\ell_4^2(\mathbb R)\), and let
\[
\mu(X)=\sup_{\substack{x,y\in S_X,\;x\perp_B y\\ \lambda\ge0}}
\frac{1+\lambda}{\|x+\lambda y\|_4}
\]
be Joly's classical rectangular constant. Define
\[
Q(A)=81A^8-216A^6+81A^5+162A^4-81A^3-24A^2+1
\]
and
\[
A_c=\sqrt{\frac{2-\sqrt3}{3}}.
\]
Then \(Q\) has a unique zero \(A_*\) in \((0,A_c)\). Put
\[
C_*=\sqrt{A_*(1-A_*^2)},\qquad
\lambda_*=\frac{3C_*}{1-3A_*^2}.
\]
Then
\[
\mu(\ell_4^2)=
\frac{1+\lambda_*}
{\left(1+\lambda_*^4+6A_*\lambda_*^2-4C_*\lambda_*^3\right)^{1/4}}
=
1.93365718463403520398\ldots.
\]
This gives an exact algebraic determination of the published numerical value \(1.9337\).

Moreover, every normalized maximizing triple \((x,y,\lambda)\) has
\[
\lambda=\lambda_*,
\qquad
A(x,y):=x_1^2y_1^2+x_2^2y_2^2=A_*,
\qquad
B(x,y):=x_1y_1^3+x_2y_2^3=-C_*,
\]
and conversely every unit Birkhoff--James orthogonal pair with these three invariants is maximizing. One explicit representative is obtained by setting
\[
u_*=\frac{A_*}{\sqrt{1+3A_*^2}},
\]
\[
a^4=\frac{1+\sqrt{1-4u_*^2}}2,\qquad
b^4=\frac{1-\sqrt{1-4u_*^2}}2,
\]
with \(a>b>0\), and
\[
x=(a,b),\qquad
y=\frac{(b^3,-a^3)}{(a^{12}+b^{12})^{1/4}}.
\]

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality is written \(x\perp_B y\), meaning
\[
\|x\|_4\le\|x+t y\|_4
\qquad\text{for every }t\in\mathbb R.
\]
For unit vectors in the smooth plane \(\ell_4^2\),
\[
x\perp_B y
\quad\Longleftrightarrow\quad
x_1^3y_1+x_2^3y_2=0.
\]

The result concerns the classical rectangular constant \(\mu=\mu_1\), not the generalized constant \(\mu_4\).

## Proof
Take \(x,y\in S_{\ell_4^2}\) with \(x\perp_B y\). By signed-coordinate symmetries and coordinate permutation, write
\[
x=(a,b),\qquad a\ge b\ge0,\qquad a^4+b^4=1.
\]
When both coordinates are nonzero, the unit Birkhoff--James orthogonal direction is
\[
y=\pm\frac{(b^3,-a^3)}{(a^{12}+b^{12})^{1/4}}.
\]
The boundary cases are obtained by continuity.

Define
\[
A=x_1^2y_1^2+x_2^2y_2^2,
\qquad
B=x_1y_1^3+x_2y_2^3.
\]
A direct expansion gives
\[
\|x+\lambda y\|_4^4
=
1+\lambda^4+6A\lambda^2+4B\lambda^3.
\]
For a fixed \(A\) and \(\lambda>0\), the smaller denominator is obtained from the sign with \(B\le0\). If
\[
C=-B\ge0,
\]
then the Birkhoff--James relation and the unit equations give
\[
C^2=A(1-A^2).
\]
Conversely every \(A\in[0,1]\) occurs. Indeed, with
\[
u=a^2b^2\in[0,1/2],
\]
one computes
\[
A=\frac{u}{\sqrt{1-3u^2}},
\]
which increases continuously from \(0\) to \(1\).

Thus the whole problem reduces exactly to
\[
\mu(\ell_4^2)
=
\sup_{\lambda\ge0,\;0\le A\le1}
\frac{1+\lambda}
{\left(1+\lambda^4+6A\lambda^2-4\lambda^3\sqrt{A(1-A^2)}\right)^{1/4}}.
\]
Put
\[
C(A)=\sqrt{A(1-A^2)}.
\]
For each fixed \(\lambda>0\), minimizing the fourth power of the denominator is equivalent to minimizing
\[
6A\lambda^2-4C(A)\lambda^3.
\]
On \(0<A<1\),
\[
C''(A)=
\frac{3A^4-6A^2-1}{4C(A)^3}<0.
\]
Therefore the minimizer is unique. Its first-order equation is
\[
\lambda(1-3A^2)=3C(A),
\]
so necessarily \(0<A<1/\sqrt3\) and
\[
\lambda=L(A):=
\frac{3\sqrt{A(1-A^2)}}{1-3A^2}.
\]
Since \(C'\) strictly decreases from \(+\infty\) to \(0\) on \((0,1/\sqrt3)\), the function \(L\) strictly increases from \(0\) to \(+\infty\).

Let the denominator, already minimized in \(A\), be \(F(\lambda)^{1/4}\). The envelope theorem gives the same derivative as differentiating before substituting the minimizing \(A\). The stationarity condition for
\[
\frac{1+\lambda}{F(\lambda)^{1/4}}
\]
is
\[
4F(\lambda)=(1+\lambda)F'(\lambda).
\]
Using
\[
\lambda(1-3A^2)=3C(A)
\]
reduces this condition to
\[
(3A^2-1)\lambda^4-9A^2\lambda^3+9A\lambda^2-9A\lambda+3=0.
\]
Eliminating \(\lambda^2\) with
\[
(1-3A^2)^2\lambda^2=9A(1-A^2)
\]
turns the remaining condition into
\[
\lambda=S(A):=
\frac{9A^4-12A^2+1}{3A(1-3A^2)}.
\]
The function \(S\) is positive precisely on
\[
0<A<A_c,
\qquad
A_c=\sqrt{\frac{2-\sqrt3}{3}},
\]
and
\[
S'(A)=
-\frac{(1+3A^2)(1+9A^4)}
{3A^2(1-3A^2)^2}<0.
\]
Hence \(L(A)=S(A)\) has exactly one solution \(A_*\in(0,A_c)\): \(L\) increases from \(0\), while \(S\) decreases from \(+\infty\) to \(0\).

Because both sides are positive on this interval, squaring \(L(A)=S(A)\) introduces no sign ambiguity and gives exactly
\[
81A^8-216A^6+81A^5+162A^4-81A^3-24A^2+1=0.
\]
Thus \(A_*\) is the unique zero of the displayed polynomial in \((0,A_c)\).

The reduced objective tends to \(1\) as \(\lambda\downarrow0\) and as \(\lambda\to\infty\), while at \(\lambda=1\) the coordinate pair already gives a value \(2^{3/4}>1\). Therefore its unique critical point is the global maximum. Substitution gives the stated exact formula.

The equality statement follows from uniqueness at each reduction step. A maximizing normalized triple must have
\[
A=A_*,
\qquad
B=-\sqrt{A_*(1-A_*^2)},
\qquad
\lambda=\lambda_*.
\]
Conversely these conditions make every inequality above an equality and give the exact maximum.

To obtain an explicit representative, solve
\[
A=\frac{u}{\sqrt{1-3u^2}}
\]
for
\[
u=\frac{A}{\sqrt{1+3A^2}},
\]
then recover \(a^4,b^4\) as the two roots of
\[
z^2-z+u^2=0.
\]
The displayed \(x\) and \(y\) are unit, satisfy \(x\perp_B y\), and realize the required invariants.

## Verification
The unique root and the final value are
\[
A_*=0.174177500540137295788576370582\ldots,
\]
\[
\lambda_*=1.35634457846695755421350607134\ldots,
\]
and
\[
\mu(\ell_4^2)=1.93365718463403520398276193150\ldots.
\]
The latter rounds to \(1.9337\), exactly matching the more accurate numerical entry published for \(p=4\).

The proof does not use the decimal value to establish the theorem. The polynomial arises only after two exact first-order equations have been reduced, and uniqueness is proved before squaring, so no extraneous polynomial root is accepted.

As an independent symbolic check, eliminating \(\lambda\) from
\[
(1-3A^2)^2\lambda^2-9A(1-A^2)=0
\]
and
\[
(3A^2-1)\lambda^4-9A^2\lambda^3+9A\lambda^2-9A\lambda+3=0
\]
produces the factor
\[
81A^8-216A^6+81A^5+162A^4-81A^3-24A^2+1.
\]

## Relationship to prior work
Gastinel and Joly proved that the rectangular constant of an \(L_p\) space is already determined by the two-dimensional \(\ell_p^2\) problem. In their 1970 paper they explicitly reduced the \(L_p\) computation to the two-dimensional case and reported numerical values; their table lists approximately \(1.888\) at \(p=4\).

Baronti, Casini, and Papini revisited the invariant and substantially sharpened the numerical computation. Their complete open-access paper states that exact values in \(\ell_p\) are generally unknown, proves improved upper estimates, and gives the more accurate table value
\[
\mu(\ell_4)=1.9337.
\]
The present theorem turns that numerical benchmark into an exact algebraic value and determines all normalized maximizers through the invariants \(A\), \(B\), and \(\lambda\).

Paul, Ghosh, and Sain proved general attainment and extremal-geometry results for the classical rectangular constant. Their complete preprint contains no special exact evaluation for \(\ell_4^2\).

Del Río and Benítez treat the rectangular constant in two-dimensional spaces and prove the Hilbert-characterization endpoint \(\mu=\sqrt2\). Their complete seven-page article does not provide an exact \(\ell_4^2\) value.

A published exact result for the generalized constant \(\mu_4(\ell_4^2)\) is mathematically adjacent but concerns a different functional: the numerator there is \((1+\lambda^4)^{1/4}\), whereas the classical rectangular constant here has numerator \(1+\lambda\).

## Limitations
The theorem is specific to the classical rectangular constant of the real plane \(\ell_4^2\). It does not give a closed formula for \(\mu(\ell_p)\) at arbitrary \(p\), nor does it assert that the algebraic degree displayed here is minimal.

The earliest historical papers inspected in full expose only year-level or month-level publication evidence. The exact date field therefore uses the earliest checked source with a verified day-level public date, the 2014 preprint of Paul--Ghosh--Sain.

## References
1. N. Gastinel and J. L. Joly, “Condition numbers and general projection method,” *Linear Algebra and its Applications* 3 (1970), 185--224, DOI 10.1016/0024-3795(70)90015-7.
2. M. del Río and C. Benítez, “The rectangular constant for two-dimensional spaces,” *Journal of Approximation Theory* 19 (1977), 15--21, DOI 10.1016/0021-9045(77)90025-9.
3. K. Paul, P. Ghosh, and D. Sain, “On rectangular constant in normed linear spaces,” arXiv:1407.1353v1, first submitted 2014-07-05; primary MSC 46B20.
4. M. Baronti, E. Casini, and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124--133, DOI 10.1017/S0004972721000253; first published online 2021-04-26.
