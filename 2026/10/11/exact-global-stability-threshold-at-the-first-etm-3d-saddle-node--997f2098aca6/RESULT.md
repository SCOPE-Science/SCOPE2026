# Exact global-stability threshold at the first ETM-3D saddle-node
## Finding
For the ETM-3D system
\[
\dot x=-2x-\rho y+yz,\qquad
\dot y=x-y+\rho z-2xz,\qquad
\dot z=\rho y-5z+xy,
\]
with \(\rho\ge0\), define
\[
P(\rho)=594\rho^8-2076\rho^7-5948\rho^6+20050\rho^5+25505\rho^4-66100\rho^3-63325\rho^2+77500\rho+75000.
\]
Let \(\rho_*\) be the smallest positive zero of \(P\). Exact Sturm isolation gives
\[
2.188758<\rho_*<2.188759,
\]
and numerical evaluation gives \(\rho_*=2.188758626951725\ldots\).

The origin is globally exponentially stable for every \(0\le\rho<\rho_*\). At \(\rho=\rho_*\), a nonzero double equilibrium appears, so the origin is no longer globally attractive. Thus \(\rho_*\) is the exact endpoint of the initial global-stability regime and exactly the first saddle-node parameter that arXiv:2610.04768v1 reports numerically as \(2.18875863\).

There is also a sharp certificate statement: a centered quadratic strict Lyapunov function exists exactly for \(0\le\rho<\rho_*\). Every such certificate is, after positive scaling,
\[
V_a(x,y,z)=\frac12\left(a x^2+y^2+(2-a)z^2\right),\qquad 0<a<2.
\]

## Assumptions and scope
The claim concerns the vector field printed in arXiv:2610.04768v1 on its benchmark domain \(\rho\ge0\). “Centered quadratic” means a positive-definite quadratic form with no translation or linear term. Global exponential stability is asserted only for \(0\le\rho<\rho_*\); at the endpoint a second equilibrium prevents global attraction. No claim is made about translated quadratic functions or about stability of other equilibrium branches after the first saddle-node.

The exact algebraic threshold uses the source's equilibrium reduction. The special singular equilibrium case occurs at \(\rho=\sqrt5\), which is strictly larger than \(\rho_*\), so it does not interfere with the first saddle-node.

## Proof
Write the system as \(\dot u=A(\rho)u+N(u)\), where
\[
A(\rho)=\begin{pmatrix}-2&-\rho&0\\1&-1&\rho\\0&\rho&-5\end{pmatrix},\qquad
N(x,y,z)=\begin{pmatrix}yz\\-2xz\\xy\end{pmatrix}.
\]
Let \(W\) be symmetric positive definite and consider \(V(u)=\frac12u^T W u\). Its derivative is the sum of a homogeneous quadratic term and the cubic term \(C_W(u)=u^TWN(u)\). If \(C_W\) were not identically zero, choose \(u\) with \(C_W(u)\ne0\) and replace \(u\) by \(-u\) if necessary so that \(C_W(u)>0\). Along \(tu\), the positive cubic term dominates the quadratic term for large \(t\), contradicting strict global decrease. Hence any centered quadratic strict Lyapunov function must satisfy \(C_W\equiv0\).

For
\[
W=\begin{pmatrix}w_{11}&w_{12}&w_{13}\\w_{12}&w_{22}&w_{23}\\w_{13}&w_{23}&w_{33}\end{pmatrix},
\]
coefficient comparison gives
\[
w_{12}=w_{13}=w_{23}=0,\qquad w_{11}-2w_{22}+w_{33}=0.
\]
After positive scaling, therefore,
\[
W=\operatorname{diag}(a,1,2-a),\qquad 0<a<2.
\]
For this family, \(C_W\equiv0\) and
\[
\dot V_a=u^T M(a,\rho)u,
\]
where
\[
M(a,\rho)=\begin{pmatrix}
-2a&\frac{1-a\rho}2&0\\
\frac{1-a\rho}2&-1&\frac{\rho(3-a)}2\\
0&\frac{\rho(3-a)}2&5a-10
\end{pmatrix}.
\]
After permuting coordinates to \((z,x,y)\), the first two Sylvester minors have signs \(5a-10<0\) and \((-2a)(5a-10)>0\). Thus \(M(a,\rho)\prec0\) is equivalent to \(\det M(a,\rho)<0\). Direct expansion gives
\[
\det M(a,\rho)=-\frac14F(a,\rho),
\]
with
\[
F(a,\rho)=3a^3\rho^2+2a^2\rho^2-10a^2\rho-40a^2-18a\rho^2+20a\rho+85a-10.
\]
The endpoint values are \(F(0,\rho)=-10\) and \(F(2,\rho)=-4\rho^2\) for \(\rho>0\). Its discriminant as a cubic in \(a\) is
\[
\operatorname{disc}_a F=120P(\rho).
\]
Exact Sturm counting shows that \(P\) has precisely two positive roots, one in \((2.188758,2.188759)\) and one in \((3.355161,3.355162)\). At \(\rho=1\), the cubic \(F(\cdot,\rho)\) has two roots in \((0,2)\), hence is positive between them. At \(\rho=5/2\) and at \(\rho=4\), it has no root in \((0,2)\). Since a root can enter or leave \((0,2)\) only through an endpoint or a multiple-root event, and neither endpoint vanishes for \(\rho>0\), it follows that \(F(a,\rho)>0\) for some \(a\in(0,2)\) exactly when \(0<\rho<\rho_*\). At \(\rho=0\), \(a=1\) gives \(F(1,0)=35>0\).

Therefore for every \(0\le\rho<\rho_*\) there is \(a\in(0,2)\) with \(M(a,\rho)\prec0\). The positive-definite quadratic \(V_a\) then satisfies \(\dot V_a\le-c\|u\|^2\) for some \(c>0\), which yields global exponential stability of the origin.

Finally, the source reduces nonzero equilibria to the quartic
\[
Q(x,\rho)=8x^4+8\rho x^3+(-6\rho^2+10\rho+35)x^2+(-4\rho^3+5\rho^2+15\rho)x+2\rho^4-5\rho^3-20\rho^2+25\rho+50.
\]
Its discriminant is
\[
\operatorname{disc}_x Q=12000P(\rho).
\]
Exact root counting gives no real root at \(\rho=1\) and two real roots at \(\rho=5/2\). Hence the first positive discriminant zero \(\rho_*\) is the first collision at which a real pair of nonzero equilibria is born. Since \(Q(0,\rho)=(\rho^2-5)(2\rho^2-5\rho-10)\) is coprime to \(P\), the multiple root at \(\rho_*\) is nonzero. This identifies \(\rho_*\) exactly with the source's first numerically continued saddle-node.

## Verification
The exact symbolic identities and Sturm counts are reproduced by `artifacts/verify_threshold.py`. Its saved output is `artifacts/verification_output.txt`. The script checks the determinant identity, both discriminant identities, the positive-root isolating intervals for \(P\), the relevant root counts of \(F\) and \(Q\), and the coefficient formula forcing the one-parameter Lyapunov family.

The proof does not infer an infinite statement from finite sampling: finite sample parameters are used only after exact discriminant and endpoint calculations reduce changes in real-root topology to the isolated discriminant values. The Sturm counts are exact rational computations.

## Relationship to prior work
Khalili-Amirabadi and Jalaeian-Farimani, arXiv:2610.04768v1, prove global ultimate boundedness using a translated quadratic function and report the first two saddle-node values numerically. They also exhibit the energy-preserving quadratic triad and the equilibrium quartic used here. They do not state the exact discriminant polynomial \(P\), a global-stability interval for the origin, or the coincidence between the first saddle-node and the endpoint of centered quadratic certification.

Goyal, Pontes Duff, and Benner, arXiv:2308.13819v2, give the general criterion that a quadratic form is a global strict Lyapunov function when the quadratic nonlinearity is generalized energy-preserving with respect to its weight and the weighted symmetric linear part is negative definite. That framework supports the Lyapunov step but does not specialize to ETM-3D, derive the forced weight family, compute the exact threshold, or connect it to the equilibrium discriminant.

## Limitations
The result concerns centered quadratic strict Lyapunov functions. It does not rule out other Lyapunov functions outside that class, and it does not classify the stability of every nonzero equilibrium branch. At \(\rho=\rho_*\) the origin cannot be globally attractive because a distinct equilibrium exists; the result does not claim loss of local stability there. The first saddle-node identification is for the vector field and equilibrium reduction of arXiv:2610.04768v1.

## References
1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, “ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos,” arXiv:2610.04768v1, 2026.
2. P. Goyal, I. Pontes Duff, and P. Benner, “Guaranteed Stable Quadratic Models and their Applications in SINDy and Operator Inference,” arXiv:2308.13819v2, 2024.
