# Exact orthogonal Schäffer constant of the cubic Day--James plane
## Finding
Let \(X=\ell_3-\ell_1\) be the real Day--James plane with
\[
\|(s,t)\|=
\begin{cases}
\bigl(|s|^3+|t|^3\bigr)^{1/3},&st\ge0,\\
|s|+|t|,&st<0.
\end{cases}
\]
For Birkhoff--James orthogonality \(x\perp_B y\), define
\[
g_\perp(X)=
\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\max\{\|x-y\|,\|x+y\|\}.
\]
Then
\[
g_\perp(X)=
\left(1+\frac{3}{2^{4/3}}\right)^{1/3}
=
1.298726719564592\ldots .
\]
Equality is attained by
\[
x=(2^{-1/3},2^{-1/3}),
\qquad
y=(1/2,-1/2),
\]
and by their images under the norm symmetries.

This gives an exact form for the value reported numerically as \(g_\perp(X)\approx1.2987\) in Baronti--Papini's Example 5.7.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality means
\[
x\perp_B y\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge\|x\|\qquad(\lambda\in\mathbb R).
\]
Only the cubic Day--James plane and the orthogonal Schäffer constant above are treated.

## Proof
Put
\[
C=\left(1+\frac{3}{2^{4/3}}\right)^{1/3}.
\]
The unit sphere consists of smooth same-sign cubic arcs, smooth opposite-sign taxicab segments, and four nonsmooth axis points.

For a same-sign cubic point, symmetry gives
\[
x=(A,tA),\qquad
A=(1+t^3)^{-1/3},\qquad0<t\le1.
\]
The unique norming functional is proportional to \((A^2,t^2A^2)\), so the unique unit Birkhoff direction, up to sign, is
\[
y=\left(\frac{t^2}{1+t^2},-\frac1{1+t^2}\right).
\]
If \(0<t\le1/2\), then \(x+y\) has opposite signs and
\[
\|x+y\|=1+A(1-t)>\frac43>C.
\]
Here \(A\ge(8/9)^{1/3}>2/3\), while \(C<4/3\) follows from \(2^{4/3}>5/2\).

For \(1/2\le t\le1\), the coordinates of \(x-y\) are positive and
\[
\|x-y\|^3=1+F(t),
\]
where
\[
F(t)=
\frac{3t(1+t^3)^{2/3}}{(1+t^2)^2}
+
\frac{1-t^6}{(1+t^2)^3}.
\]
Exact differentiation gives
\[
F'(t)=
-\frac{3H(t)}
{(t+1)^{1/3}(1+t^2)^4(t^2-t+1)^{1/3}},
\]
where
\[
H(t)=
t^7+2t^5(1+t^3)^{1/3}-2t^5+3t^4-3t^3
+2t^2+2t(1+t^3)^{1/3}-1.
\]
Since \((1+t^3)^{1/3}\ge1\),
\[
H(t)\ge P(t):=t^7+3t^4-3t^3+2t^2+2t-1.
\]
Now \(P(1/2)=41/128>0\), and
\[
P'(t)=7t^6+12t^3-9t^2+4t+2>0
\qquad(1/2\le t\le1).
\]
For \(1/2\le t\le3/4\), use \(12t^3-9t^2\ge-3/4\); for \(t\ge3/4\) that term is nonnegative. Hence \(F\) decreases and
\[
\|x-y\|^3\ge1+F(1)=1+\frac{3}{2^{4/3}}=C^3.
\]

Next take an interior point of an opposite-sign taxicab segment:
\[
x=(a,-b),\qquad a+b=1,\qquad a\ge b>0.
\]
Its unique norming functional is \((1,-1)\), so the unit Birkhoff direction is
\[
y=(\alpha,\alpha),\qquad \alpha=2^{-1/3}.
\]
Because \(b\le1/2<\alpha\),
\[
\|x+y\|^3=(a+\alpha)^3+(a+\alpha-1)^3.
\]
This is increasing for \(a\ge1/2\), so its minimum occurs at \(a=b=1/2\), where
\[
\|x+y\|^3
=(\alpha+1/2)^3+(\alpha-1/2)^3
=1+\frac{3}{2^{4/3}}
=C^3.
\]

Finally let \(x=(1,0)\). Its norming functionals are
\[
(1,-\theta),\qquad0\le\theta\le1.
\]
Thus every unit Birkhoff direction is, up to the norm symmetries,
\[
y=(u,v),\qquad0\le u\le v,\qquad u^3+v^3=1.
\]
If \(u\ge1/2\), then
\[
\|x+y\|^3=(1+u)^3+v^3=2+3u+3u^2\ge17/4,
\]
so \(\|x+y\|>4/3>C\). If \(u\le1/2\), then \(v^3\ge7/8\), hence \(v>5/6\), and
\[
\|x-y\|=1-u+v>\frac43>C.
\]
Thus axes cannot minimize.

At
\[
x=(2^{-1/3},2^{-1/3}),\qquad
y=(1/2,-1/2),
\]
both vectors are unit, the norming functional of \(x\) annihilates \(y\), and
\[
\|x+y\|^3=\|x-y\|^3=1+\frac{3}{2^{4/3}}.
\]
Therefore \(g_\perp(X)=C\).

## Verification
The sphere-stratum split is exhaustive, and every Birkhoff direction is obtained from the full norming-functional set. The nontrivial cubic expansion and derivative factorization are independently reproduced by the included `algebra_check.py` using exact symbolic arithmetic. The script checks algebra only; the global sign and monotonicity arguments are given in the proof.

## Relationship to prior work
Yang and Li determined the exact classical James constant of the same \(\ell_3-\ell_1\) plane; Springer records publication on 15 August 2016.

Baronti and Papini define
\[
J_\perp(X)
\quad\text{and}\quad
g_\perp(X),
\]
and their Example 5.7 treats exactly this cubic Day--James norm. Their full text states
\[
J_\perp(X)=J(X),
\qquad
g_\perp(X)\approx1.2987>g(X),
\]
and remarks that the calculations are not simple. The inspected source does not display an exact closed form for \(g_\perp\).

Targeted searches using the Day--James and \(\ell_3-\ell_1\) names, orthogonal Schäffer and \(g_\perp\) notation, the decimal \(1.2987\), and the exact radical above did not locate an equivalent exact formula.

## Limitations
The theorem determines only \(g_\perp\) for the real cubic Day--James plane. It does not give a full \(p\)-profile for \(\ell_p-\ell_1\).

The Yang--Li full text was not open through the inspected publisher route, but only its role as a classical-James source is used. The decisive same-invariant comparison is the fully inspected Baronti--Papini article.

## References
1. C. S. Yang and H. Y. Li, “The James constant for the \(\ell_3-\ell_1\) space,” *Acta Mathematica Sinica, English Series* 32 (2016), 1075--1079, DOI 10.1007/s10114-016-5423-5; published 2016-08-15.
2. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” *Constructive Mathematical Analysis* 5 (2022), 37--45, DOI 10.33205/cma.1067323.
