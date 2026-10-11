# Exact cubic rectangular constant of the real \(\ell_3^2\) plane
## Finding
For the real plane \(X=\ell_3^2\), define
\[
\mu_3(X)
=
\sup_{\substack{x,y\in S_X\\x\perp_B y}}
\sup_{\lambda\ge0}
\frac{(1+\lambda^3)^{1/3}}{\|x+\lambda y\|_3}.
\]
Then
\[
\boxed{\mu_3(\ell_3^2)=\rho_0^{1/3}}
=1.124652845212756109\ldots,
\tag{1}
\]
where \(u_0\) is the unique root in \((16.1428,16.1429)\) of
\[
P(u)=u^{10}-12u^9-59u^8-104u^7-350u^6-368u^5-334u^4+40u^3+77u^2+60u-7,
\tag{2}
\]
\[
A(u)=8482484u^9+35056168u^8+66754285u^7+196108143u^6+203704837u^5+173520417u^4
-23602937u^3-42303003u^2-31205429u+3667499,
\tag{3}
\]
\[
B(u)=167282621u^9+692749853u^8+1317595314u^7+3874778514u^6+4024515932u^5+3430463796u^4
-466156426u^3-835826554u^2-616943313u+72501863,
\tag{4}
\]
\[
h_0=\frac{B(u_0)}{4A(u_0)}\in(4,5),
\tag{5}
\]
and
\[
\rho_0=
\frac{u_0^2(1+u_0)+h_0^3(1+u_0^2)}{(u_0+h_0)^3+u_0^2(h_0-1)^3}
=1.422510428368351774\ldots.
\tag{6}
\]
The reduced maximizing orbit is unique.

## Assumptions and scope
All scalars are real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x\|\le\|x+\alpha y\|
\ \text{for every }\alpha\in\mathbb R.
\]
In \(\ell_3^2\), smoothness gives
\[
x=(x_1,x_2)\perp_B y=(y_1,y_2)
\quad\Longleftrightarrow\quad
x_1|x_1|y_1+x_2|x_2|y_2=0.
\tag{7}
\]
Signed coordinate permutations reduce every non-axis unit Birkhoff pair to
\[
x_t=\frac{(t,1)}{(1+t^3)^{1/3}},
\qquad
y_t=\frac{(1,-t^2)}{(1+t^6)^{1/3}},
\qquad t\ge1,
\tag{8}
\]
with either orientation of \(y_t\). Axis pairs give value \(1\) and are non-extremal.

## Proof
Let the sign of the tangent orientation be absorbed into a signed parameter
\[
s=\pm\lambda\frac{(1+t^3)^{1/3}}{(1+t^6)^{1/3}}.
\]
Cubing the rectangular ratio gives
\[
F(t,s)=
\frac{1+t^3+|s|^3(1+t^6)}{|t+s|^3+|1-st^2|^3}.
\tag{9}
\]
We first remove three regions exactly. If \(0\le s\le t^{-2}\), denominator minus numerator equals
\[
s^2t\bigl(3(t^3+1)-2st^5\bigr)>0.
\tag{10}
\]
If \(-t\le s\le0\), put \(v=-s\); the same difference is
\[
v^2(3t^4+3t-2v)>0.
\tag{11}
\]
If \(s\le-t\), put \(v=-s\ge t\); the difference is
\[
t\bigl(3v^2(t^3-1)+6tv-2t^2\bigr)>0.
\tag{12}
\]
Thus every ratio larger than \(1\) lies in
\[
s\ge t^{-2}.
\]
Set
\[
u=t^3\ge1,
\qquad
h=st^2\ge1.
\]
Then (9) becomes
\[
R(u,h)=
\frac{u^2(1+u)+h^3(1+u^2)}{(u+h)^3+u^2(h-1)^3}.
\tag{13}
\]
On the finite boundary,
\[
R(1,h)-1=-\frac{3h-1}{h(h^2+3)}<0,
\tag{14}
\]
and
\[
R(u,1)-1=-\frac{u(u+3)}{(u+1)^3}<0.
\tag{15}
\]
Moreover, if \(N(u,h)\) and \(D(u,h)\) denote the numerator and denominator in (13), then
\[
D(u,h)-N(u,h)
=
-u\bigl(3h^2u-3h^2-6hu+2u\bigr).
\]
Hence \(R(u,h)\to1\) along every unbounded path in \([1,\infty)^2\). For bounded \(h\) and \(u\to\infty\), divide by \(u^3\). If \(h\to\infty\) and \(u\ge h^3\), then \(|D-N|/u^3\to0\); if \(u<h^3\), then \(D\ge u^2(h-1)^3\) and \(|D-N|/[u^2(h-1)^3]\to0\). Thus every unbounded sequence has \(R\to1\). Hence any value larger than \(1\) has an interior maximizer.

The two numerator polynomials of \(\partial R/\partial u\) and \((3u)^{-1}\partial R/\partial h\) are
\[
F_u=3h^5u^2+6h^5u-3h^5-12h^4u+4h^3u-3h^2u^4+6h^2u^3+3h^2u^2+6hu^4-2u^4,
\tag{16}
\]
\[
F_h=-h^4u^3+h^4u^2-h^4u+h^4+4h^3u^3+4h^3u-2h^2u^3-2h^2u+2hu^4-2hu^2-2u^4-2u^3.
\tag{17}
\]
Their resultant with respect to \(h\) factors as
\[
4u^{13}(u+1)^4Q(u)P(u),
\tag{18}
\]
where
\[
Q(u)=27u^6+81u^5+170u^4+270u^3+259u^2+81u+8>0
\]
for \(u>0\). A Sturm calculation shows that \(P\) has exactly one root for \(u\ge1\), namely \(u_0\) in (2).

The linear subresultant, reduced modulo \(P\), is a nonzero scalar multiple of
\[
4A(u)h-B(u).
\tag{19}
\]
Exact sign isolation on \(16.1428<u<16.1429\) gives
\[
A(u_0)>0,
\qquad
B(u_0)-16A(u_0)>0,
\qquad
20A(u_0)-B(u_0)>0,
\]
so the unique interior stationary point has \(h=h_0\in(4,5)\). Substitution of (19) into (16)--(17) leaves numerators divisible by \(P\), proving that \((u_0,h_0)\) is indeed stationary.

Because there is no other interior critical point and all boundary or escaping values are at most \(1\) in the limiting sense, while \(R(u_0,h_0)>1\), this stationary point is the unique global maximum. Equation (1) follows from (6).

Numerically,
\[
t_0=u_0^{1/3}=2.527320371009115\ldots,
\qquad
h_0=4.932369794345353\ldots.
\]
A representative maximizing Birkhoff pair is
\[
x=\frac{(t_0,1)}{(1+t_0^3)^{1/3}},
\qquad
y=\frac{(1,-t_0^2)}{(1+t_0^6)^{1/3}},
\]
and the maximizing scale is
\[
\lambda_0=1.915353174158011\ldots.
\]

## Verification
The bundled `verify.py` reconstructs (13), differentiates it symbolically, verifies the resultant factorization (18), applies an exact Sturm root count to (2), proves the isolating interval and the inequalities forcing \(4<h_0<5\), checks the divisibility certificates for the stationary point, and replays the boundary identities (14)--(15).

A numerical stress grid is included only as a supplementary check. The proof of the continuum maximum is the exact semialgebraic argument above, not the grid.

## Relationship to prior work
Baronti, Casini and Papini revisited the rectangular constant and its Gastinel--Joly generalizations \(\mu_p\). Their 2021 paper states that exact values are generally unknown and proves, for \(p\ge2\), the general estimate
\[
\mu_p(\ell_p)\le(2^{p-1}-1)^{1/p}.
\]
At \(p=3\) this gives only
\[
\mu_3(\ell_3)\le3^{1/3}=1.442\ldots,
\]
whereas (1) determines the planar value exactly.

The closest indexed exact result found is the \(p=4\) planar computation
\[
\mu_4(\ell_4^2)=\left(\frac{5+\sqrt{17}}4\right)^{1/4}.
\]
Its quartic reduction is specific to exponent \(4\) and does not imply the cubic stationary system (16)--(18). Other exact \(\ell_3^2\) records concern different Birkhoff-orthogonal objectives such as \(T_\perp\) and Dragomir symmetry.

## Limitations
The theorem computes \(\mu_3\) for the two-dimensional real space \(\ell_3^2\). It does not determine \(\mu_3(\ell_3)\) in arbitrary dimension, nor \(\mu_p(\ell_p^2)\) for a full interval of exponents.

The exact value is algebraic but is naturally represented through the isolated degree-ten root (2), rather than a short radical expression.

Bibliographic and semantic-index searches cannot prove absolute novelty. An equivalent computation may exist under a different parametrization of Birkhoff tangents or without the notation \(\mu_3\).

## References
1. M. Baronti, E. Casini and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124--133, doi:10.1017/S0004972721000253. First published online 26 April 2021. Primary MSC 46B20.
