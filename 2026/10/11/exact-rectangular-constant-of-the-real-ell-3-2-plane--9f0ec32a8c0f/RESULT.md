# Exact rectangular constant of the real \(\ell_3^2\) plane
## Finding
For the real plane \(X=(\mathbb R^2,\|\cdot\|_3)\), Joly's rectangular constant is
\[
\mu(X)=\sup_{x\perp_B y}\frac{\|x\|_3+\|y\|_3}{\|x+y\|_3}.
\]
Let
\[
P(u)=u^{14}-36u^{13}+783u^{12}-2584u^{11}+8189u^{10}-13212u^9+20019u^8-17104u^7+15155u^6-8860u^5+4733u^4-2456u^3+143u^2-36u+1.
\]
There is exactly one zero \(u_*\) of \(P\) in \((0.0295832,0.0295833)\). Put \(t_*=\sqrt[3]{u_*}\). Define
\[
A(t)=t^{12}-4t^9-6t^6-4t^3+1,\qquad B(t)=4(t^{10}-t),\qquad C(t)=2(t^8+t^2).
\]
There is a unique \(s_*\in(1.2347,1.2348)\) satisfying the two stationary equations in the proof below; equivalently it is the root above \(t_*\) of
\[
A(t_*)s^2+B(t_*)s+C(t_*)=0
\]
that also satisfies the first stationary equation. Then
\[
\boxed{\mu(\ell_3^2)=\frac{(1+t_*^3)^{1/3}+s_*(1+t_*^6)^{1/3}}{\left((1+s_*t_*^2)^3+(s_*-t_*)^3\right)^{1/3}}}
\]
and numerically
\[
\mu(\ell_3^2)=1.7285381384820930370177966302914\ldots.
\]
The maximizing pair can be represented, up to signed-coordinate isometries and common positive scaling, by \((1,t_*)\) and \(s_*(t_*^2,-1)\).

## Assumptions and scope
The space is real and two-dimensional, with \(\|(a,b)\|_3=(|a|^3+|b|^3)^{1/3}\). Birkhoff--James orthogonality means \(x\perp_B y\) when \(\|x\|_3\le \|x+\lambda y\|_3\) for every real \(\lambda\). Since \(\ell_3^2\) is smooth, for nonzero \(x=(x_1,x_2)\) this is equivalent to
\[
|x_1|x_1y_1+|x_2|x_2y_2=0.
\]
The claim concerns the classical rectangular constant \(\mu\), not a generalized rectangular modulus.

## Proof
By signed-coordinate isometries, coordinate interchange, and common positive scaling, every nontrivial orthogonal pair can be represented using \(0\le t\le1\), \(s\ge0\), and one of the two orientations
\[
x=(1,t),\qquad y=s(t^2,-1)
\]
or
\[
x=(1,t),\qquad y=-s(t^2,-1).
\]
Write
\[
A_0=(1+t^3)^{1/3},\qquad B_0=(1+t^6)^{1/3}.
\]
For the first orientation define
\[
R_+(t,s)=\frac{A_0+sB_0}{\left((1+st^2)^3+|t-s|^3\right)^{1/3}}.
\]
For the second orientation, the Euclidean scalar product of \(x\) and \(y\) is nonnegative when \(0\le t\le1\). Using \(\|z\|_3\le\|z\|_2\le2^{1/6}\|z\|_3\) and the Euclidean parallelogram identity gives
\[
\frac{\|x\|_3+\|y\|_3}{\|x+y\|_3}\le2^{2/3}.
\]
The same estimate handles the boundary cases \(t=0\) and \(t=1\).

For the first orientation with \(0\le s\le t\), put \(k=B_0/A_0\). Since \(k\ge t\), differentiating \(R_+\) with respect to \(s\) shows that its sign is the sign of
\[
k(1+s^2t)+s^2(1-t^3)-2st.
\]
This is bounded below by
\[
t-2st+s^2(1+t^2-t^3),
\]
whose discriminant is \(-4t(1-t)(1+t^2)\le0\). Hence \(R_+(t,s)\) is nondecreasing on \([0,t]\). At \(s=t\), because \(B_0\le A_0\),
\[
R_+(t,t)\le\frac{1+t}{(1+t^3)^{2/3}}\le2^{2/3}.
\]
The last inequality follows from convexity of \(r\mapsto r^3\), which gives \((1+t)^3\le4(1+t^3)\).

The bound \(2^{2/3}\) is not global. At \(t=1/3\) and \(s=4/3\),
\[
R_+(1/3,4/3)=\frac{9\sqrt[3]{28}+4\sqrt[3]{730}}{\sqrt[3]{49474}}>
\frac{63}{37}>2^{2/3}.
\]
Thus an extremizer lies in the interior region \(0<t<1\), \(s>t\). Finite-dimensional attainment of the rectangular constant is known, and the elementary limits here also rule out escape as \(s\to\infty\).

In this interior region set
\[
D=(1+st^2)^3+(s-t)^3,
\]
\[
P_1=t^2(1+st^2)^2+(s-t)^2,\qquad Q_1=(1+st^2)^2-t(s-t)^2,
\]
and \(k=B_0/A_0\). Stationarity in \(s\) is
\[
kQ_1=P_1.\tag{1}
\]
Cubing (1), using \(k^3=(1+t^6)/(1+t^3)\), gives
\[
E_1(t,s):=P_1^3(1+t^3)-Q_1^3(1+t^6)=0.\tag{2}
\]
At a point satisfying (1), stationarity in \(t\) reduces exactly to
\[
G(t,s):=A(t)s^2+B(t)s+C(t)=0.\tag{3}
\]
Indeed, differentiating \(\log R_+\), substituting (1), and clearing the positive factors \((1+t^3)(1+t^6)\) yields (3).

Eliminating \(s\) from (2) and (3) gives the exact factorization
\[
\operatorname{Res}_s(E_1,G)=(t+1)^{18}(t^2+1)(t^2-t+1)^{18}(t^4-t^2+1)P(t^3).
\]
All prefactors are positive for \(0<t<1\). Exact Sturm isolation shows that \(P\) has exactly two zeros in \((0,1)\): one in \((0.0295832,0.0295833)\) and one in \((0.6845614,0.6845615)\). For every \(0<t<1\),
\[
G(t,t)=t^2(t+1)^2(t^2-t+1)^2(t^6-2t^3-1)<0,
\]
while \(B(t)<0\) and \(C(t)>0\). At the first isolated zero of \(P(t^3)\), \(A(t)>0\), so the quadratic \(G(t,\cdot)\) has exactly one root above \(t\); exact interval substitution into (1) isolates it in \((1.2347,1.2348)\). At the second isolated zero, \(A(t)<0\), so \(G(t,\cdot)\) is strictly decreasing for \(s\ge0\) and has no root above \(t\). Therefore there is only one possible interior maximizer, namely \((t_*,s_*)\), and the displayed exact formula follows.

## Verification
The standalone script `verification_rectangular_l3.py` reconstructs the two stationary polynomials, verifies the resultant factorization symbolically, uses exact Sturm root counts on rational intervals, checks the branch-sign classification, and evaluates the isolated algebraic solution at high precision. Its companion output records
\[
u_*=0.0295832392367274495346655604640\ldots,
\]
\[
t_*=0.309277677371202911698442825396\ldots,
\]
\[
s_*=1.234724454723104368866456649824\ldots,
\]
and the stated value of \(\mu\). The proof does not infer an infinite statement from finite sampling; the symbolic elimination and Sturm counts are the exhaustive finite algebraic step after the analytic reduction.

## Relationship to prior work
Gastinel and Joly introduced the orthogonal/rectangular constant framework and in 1970 reported a numerical table containing the \(p=3\) value only to three decimals. Baronti, Casini, and Papini revisited the constant and in 2021 reported a more accurate numerical value \(1.7285\) for \(\mu(\ell_3)\), together with improved general upper bounds; their paper also records the classical equality between the sequence-space constant and its two-dimensional counterpart. Desbiens' 1990 paper gives the standard homogeneous definition and studies the relation with asymmetry of Birkhoff--James orthogonality. The sources inspected do not state an exact algebraic value or the degree-fourteen stationary polynomial above.

## Limitations
The result is specific to the classical rectangular constant of the real \(\ell_3^2\) plane. It does not provide a closed radical expression for \(u_*\), nor does it solve the rectangular constant for arbitrary \(p\). The exact value is given by a uniquely isolated algebraic root and an explicitly isolated stationary companion. The literature comparison cannot rule out every unpublished computation; it rules out coverage in the inspected primary sources and in the searched published-result index.

## References
1. N. Gastinel and J. L. Joly, “Condition numbers and general projection method,” *Linear Algebra and its Applications* 3 (1970), 185–224. DOI: 10.1016/0024-3795(70)90015-7.
2. J. Desbiens, “Constante rectangle et biais d'un espace de Banach,” *Bulletin of the Australian Mathematical Society* 42 (1990), 465–482. DOI: 10.1017/S000497270002863X.
3. K. Paul, P. Ghosh, and D. Sain, “On Rectangular Constant in Normed Linear Spaces,” *Journal of Convex Analysis* 24 (2017), 917–925. DOI: 10.68381/jca24054.
4. M. Baronti, E. Casini, and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124–133; first published online 26 April 2021. DOI: 10.1017/S0004972721000253.
