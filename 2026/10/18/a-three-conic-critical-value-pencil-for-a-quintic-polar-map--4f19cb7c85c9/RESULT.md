# A three-conic critical-value pencil for a quintic polar map

## Finding
Let \(s,p\in\mathbb C\) satisfy
\[
sp(s^2-4p)(s^2-3p)(s^2+2p)(4s^4-108s^2p+243p^2)\ne0.
\]
The reduced plane quintic
\[
C_{s,p}:\quad f=x\big((xz)^2+s(xz)y^2+py^4\big)=0
\]
is the union of a line and two distinct smooth conics belonging to a bitangent pencil. Its polar map \(\nabla f:\mathbb P^2\dashrightarrow\mathbb P^2\), written in target coordinates \([U:V:W]\), has generic degree \(3\). The closure of its **divisorial critical values** (the images of critical curves not contracted to points) is the reduced degree-six curve
\[
\begin{aligned}
\mathcal B_{s,p}:\quad 0={}&(s^2-3p)V^6+(-56s^3+180sp)V^4UW\\
&+(16s^4+720s^2p-3888p^2)V^2(UW)^2-192s^3p(UW)^3.
\end{aligned}
\]
It is **exactly three distinct smooth conics in a bitangent pencil**, each with the same tangency points \([1:0:0]\) and \([0:0:1]\) and the same respective tangent lines \(W=0\) and \(U=0\). No claim is made that this is the full discriminant of any chosen resolution of the rational map, including exceptional-divisor effects.

## Assumptions and scope
Work over the algebraically closed field \(\mathbb C\); all parameters and variables are in characteristic zero. The displayed nonvanishing product defines a nonempty Zariski-open subset of \(\mathbb A^2_{s,p}\), since \((s,p)=(1,1)\) belongs to it. The quadratic \(T^2+sT+p\) has two distinct nonzero roots, so \(C_{s,p}\) has one line component and two distinct smooth conic components. A divisorial critical value means an irreducible curve that is the closure of the image of a noncontracted irreducible component of the differential-rank-drop locus on the regular domain of \(\nabla f\). Critical images of contracted curves are points, not divisorial components.

## Proof
Write \(t=xz/y^2\) on \(y\ne0\) and set
\[
\begin{gathered}
P(t)=t^2+st+p,\quad A(t)=3t^2+2st+p,\\
B(t)=st+2p,\quad C(t)=2t+s,\\
\Phi(t)=3st^3+18pt^2+(13sp-s^3)t+s^2p+2p^2.
\end{gathered}
\]
On the dense chart \(y=1\), with \(x=u\ne0\), \(z=t/u\), differentiation gives
\[
\nabla f(u,1,t/u)=[A(t):2uB(t):u^2C(t)]. \tag{1}
\]
On \(A\ne0\), the Jacobian of \((u,t)\mapsto(V/U,W/U)\) is
\[
\det\frac{\partial(V/U,W/U)}{\partial(u,t)}
=\frac{4u^2\Phi(t)}{A(t)^3}. \tag{2}
\]
The full homogeneous Hessian determinant is
\[
\begin{aligned}
\det\operatorname{Hess}(f)=-16x^3\big(&3s(xz)^3+18p(xz)^2y^2\\
&+(13sp-s^3)(xz)y^4+(s^2p+2p^2)y^6\big). \tag{3}
\end{aligned}
\]
In particular, away from the contracted line \(x=0\), the critical divisor is the union of the conics \(xz=t_i y^2\), where the \(t_i\) are the roots of \(\Phi\). These are distinct and nonzero because
\[
\operatorname{Disc}_t\Phi=3(s^2-4p)^3(4s^4-108s^2p+243p^2)\ne0
\]
and \(\Phi(0)=p(s^2+2p)\ne0\). The line \(x=0\) maps on its regular points to \([1:0:0]\) and hence contributes no divisorial critical value. Equation (3) shows there are no additional divisorial components, including on \(y=0\).

Direct polynomial resultants are
\[
\begin{aligned}
\operatorname{Res}_t(\Phi,A)&=9p(3p-s^2)(4p-s^2)^2,\\
\operatorname{Res}_t(\Phi,B)&=-3ps(4p-s^2)^2,\\
\operatorname{Res}_t(\Phi,C)&=-(4p-s^2)^2.
\end{aligned}
\]
They do not vanish under the assumptions. Thus all \(A(t_i),B(t_i),C(t_i)\) are nonzero. Formula (1) maps each critical conic birationally onto the smooth target conic
\[
A(t_i)C(t_i)V^2-4B(t_i)^2 UW=0, \tag{4}
\]
where \(u\) parametrizes its dense open subset.

For a generic target point with \(UVW\ne0\), equation (1) is equivalent to
\[
A(t)C(t)V^2-4B(t)^2UW=0, \tag{5}
\]
which is a cubic in \(t\). Conversely, each generic root determines the unique source \(u=A(t)V/(2B(t)U)\); this proves the polar map has generic degree three.

Introduce homogeneous degree-three variables \(X,Y\) and the binary cubic
\[
\begin{aligned}
F_{s,p}(X,Y)={}&(s^2-3p)X^3+(-56s^3+180sp)X^2Y\\
&+(16s^4+720s^2p-3888p^2)XY^2-192s^3pY^3.
\end{aligned}
\]
An exact elimination identity is
\[
\operatorname{Res}_t\bigl(\Phi(t),\,A(t)C(t)X-4B(t)^2Y\bigr)
=9p(s^2-4p)^4 F_{s,p}(X,Y). \tag{6}
\]
Consequently, substituting \(X=V^2\), \(Y=UW\) in \(F\) yields the union of the three curves (4), i.e. the displayed sextic \(\mathcal B_{s,p}\). Its three parameters are distinct because
\[
\operatorname{Disc}_X F_{s,p}(X,1)
=12288(s^2-4p)(4s^4-108s^2p+243p^2)^3\ne0.
\]
The leading and constant coefficients of \(F_{s,p}\) are also nonzero by assumption, so every factor is of the form \(V^2-c_i UW\) with \(c_i\in\mathbb C^*\), pairwise distinct. Each such equation defines a smooth conic, and direct gradients at its two common intersection points give the tangents claimed. This establishes the complete reduced divisorial critical-value locus.

## Verification
The included standalone `verify.py` uses characteristic-zero exact symbolic arithmetic (SymPy) to check equations (1)--(3), the two discriminants, all three nonvanishing resultants, and the critical-image resultant (6). Run `python verify.py` in the extracted package. It prints `PASS` only if every asserted identity succeeds. A concrete specialization \((s,p)=(1,1)\) has
\[
F_{1,1}(X,Y)=-2\bigl(X^3-62X^2Y+1576XY^2+96Y^3\bigr),
\]
and \(\Phi(t)=3(t^3+6t^2+4t+1)\). The proof is algebraic for every parameter pair in the open set, not an extrapolation from this specialization.

## Relationship to prior work
Beorchia and Miró-Roig, *Jacobian schemes of conic-line arrangements and eigenschemes* (arXiv:2303.04665, Example 3.2(4), Proposition 4.5), identify the conic-line family and give its polar-map coordinates. Their proposition establishes that the line component is contracted; it does not specify the remaining Hessian components, the reduced critical-value equation, or their bitangent-pencil structure. The result above computes these objects in the first nontrivial two-conic case. Dimca, *Free and nearly free curves from conic pencils* (arXiv:1704.07196), treats syzygies and topology of conic-pencil arrangements, not this branch equation. Di Gennaro, Ilardi, Miró-Roig, Schenck, and Vallès, *Free curves, Eigenschemes and Pencils of curves* (arXiv:2306.09443), develops freeness constructions via eigenschemes and pencils, without an equivalent critical-image classification in the compared sections.

## Limitations
The statement concerns the reduced closure of images of noncontracted critical curves on the regular locus of a rational map. It does not determine the full scheme-theoretic discriminant after resolving its indeterminacy, multiplicities along exceptional divisors, or the local analytic types at intersections of the three target conics. The stated open-parameter condition is sufficient and is not claimed necessary. The originality comparison is based on identified accessible literature and searches and is not an exhaustive mathematical bibliography.

## References
1. V. Beorchia and R. M. Miró-Roig, *Jacobian schemes of conic-line arrangements and eigenschemes*, arXiv:2303.04665 (first posted 8 March 2023), https://arxiv.org/html/2303.04665v2, especially Example 3.2(4) and Proposition 4.5.
2. A. Dimca, *Free and nearly free curves from conic pencils*, arXiv:1704.07196 (2017), https://arxiv.org/html/1704.07196v3.
3. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, H. Schenck, and J. Vallès, *Free curves, Eigenschemes and Pencils of curves*, arXiv:2306.09443 (first posted 2023), https://arxiv.org/html/2306.09443v4.
