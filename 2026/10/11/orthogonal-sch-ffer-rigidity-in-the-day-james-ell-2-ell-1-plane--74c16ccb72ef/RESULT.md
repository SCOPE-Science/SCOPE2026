# Orthogonal Schäffer rigidity in the Day--James ell_2--ell_1 plane
## Finding
Let \(X=\ell_2-\ell_1\) be the real Day--James plane
\[
\|(s,t)\|=
\begin{cases}
\sqrt{s^2+t^2},&st\ge0,\\
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
g_\perp(X)=\sqrt{\frac32}.
\]
Moreover, equality occurs exactly, up to global sign change, coordinate interchange, and reversing the ordered pair, for the balanced pair
\[
\left\{
\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\left(-\frac12,\frac12\right)
\right\}.
\]
Thus the orthogonality restriction leaves the Schäffer constant unchanged on this plane, even though the same plane has \(J_\perp(X)<J(X)\).

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\lambda y\|\ge\|x\|
\qquad(\lambda\in\mathbb R).
\]
The norm is invariant under global sign change and coordinate interchange.

## Proof
Every unit-sphere point is either on a smooth Euclidean arc, on a smooth opposite-sign taxicab facet, or at a coordinate-axis junction.

For a smooth Euclidean-arc point, symmetry gives
\[
x=(c,s),\qquad c^2+s^2=1,\qquad0<s\le c.
\]
Put \(r=s/c\in(0,1]\), so \(c=(1+r^2)^{-1/2}\). The unique norming functional is \((c,s)\), hence the unique unit Birkhoff direction, up to sign, is
\[
y=\frac{(-s,c)}{s+c}
=
\left(-\frac r{1+r},\frac1{1+r}\right).
\]
Both coordinates of \(x+y\) are positive, and
\[
\|x+y\|^2
=
1+\frac{1+r^2}{(1+r)^2}
\ge
\frac32.
\]
Equality holds exactly at \(r=1\). At that point
\[
x=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right),
\qquad
y=\left(-\frac12,\frac12\right),
\]
and both \(\|x-y\|\) and \(\|x+y\|\) equal \(\sqrt{3/2}\).

For a smooth taxicab-facet point, symmetry gives
\[
x=(a,-b),\qquad a+b=1,\qquad a\ge b>0.
\]
Write
\[
a=\frac12+u,\qquad b=\frac12-u,\qquad0\le u<\frac12.
\]
The unique norming functional is \((1,-1)\), so the unit Birkhoff direction is
\[
y=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right).
\]
Again \(x+y\) has positive coordinates, and
\[
\|x+y\|^2
=
\frac32+2\sqrt2\,u+2u^2
\ge\frac32,
\]
with equality exactly at \(u=0\). This is the same balanced pair with the order reversed, up to sign.

At the junction \(x=(1,0)\), the complete norming-functional segment is
\[
f_\tau(s,t)=s-\tau t,\qquad0\le\tau\le1.
\]
Thus every unit Birkhoff direction is, up to sign,
\[
y=\frac{(\tau,1)}{\sqrt{1+\tau^2}},
\qquad0\le\tau\le1.
\]
Here
\[
\|x+y\|^2
=
2+\frac{2\tau}{\sqrt{1+\tau^2}}
\ge2,
\]
so no axis pair is extremal.

The three strata are exhaustive. Hence the global minimum is \(\sqrt{3/2}\), and the equality analysis gives the stated complete minimizer classification.

## Verification
The proof uses every norming functional at nonsmooth points and the unique norming functional at smooth points. The two nontrivial estimates reduce to
\[
\frac{1+r^2}{(1+r)^2}\ge\frac12
\]
and
\[
\frac32+2\sqrt2\,u+2u^2\ge\frac32.
\]
No finite sampling or numerical optimization is used as proof.

## Relationship to prior work
Kato, Maligranda, and Takahashi studied this Day--James plane in the context of classical Banach-space constants; public bibliographic metadata records publication on 17 June 2001.

Baronti and Papini introduced \(J_\perp\) and \(g_\perp\). Their full text treats exactly this mixed Euclidean--taxicab plane in Example 5.4, records
\[
J(X)=\sqrt{\frac83},
\qquad
g(X)=\sqrt{\frac32},
\]
and states only a numerical value for \(J_\perp(X)\). A full-text search of the article's \(g_\perp\) occurrences gives values for neighboring examples but no \(g_\perp\) value for Example 5.4.

The present result supplies the missing orthogonal Schäffer value and classifies every minimizing Birkhoff pair.

## Limitations
The theorem concerns only the real two-dimensional \(\ell_2-\ell_1\) Day--James plane. It does not determine \(g_\perp\) for the full \(\ell_p-\ell_1\) family. A differently notated later classification outside the checked indexes remains a bibliographic risk.

## References
1. M. Kato, L. Maligranda, and Y. Takahashi, “On James and Jordan--von Neumann constants and the normal structure coefficient of Banach spaces,” *Studia Mathematica* 144 (2001), 275--295, DOI 10.4064/sm144-3-5.
2. M. Baronti and P. L. Papini, “Parameters in Banach spaces and orthogonality,” *Constructive Mathematical Analysis* 5 (2022), 37--45, DOI 10.33205/cma.1067323.
