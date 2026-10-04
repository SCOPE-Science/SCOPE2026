# Exact transverse-type partition of the cloud-shaped equilibrium curve
## Finding
Consider the autonomous system
\[
\dot x=z,\qquad
\dot y=-z\left(ay+by^2+xz\right),\qquad
\dot z=x^2-|xy|+y^2-1.
\]
For the parameter values \(a=4\) and \(b=5/2\) used in the introducing article's displayed hidden-chaos example, the equilibrium set is the closed curve
\[
\mathcal E=\left\{(x,y,0):x^2-|xy|+y^2=1\right\}.
\]
At every smooth equilibrium with \(xy\ne0\), put \(s=\operatorname{sign}(xy)\) and
\[
T(x,y)=2x-sy-\left(4y+\frac52y^2\right)(2y-sx).
\]
The Jacobian has characteristic polynomial
\[
\lambda\left(\lambda^2-T(x,y)\right).
\]
Hence \(T>0\) gives one positive and one negative transverse eigenvalue, while \(T<0\) gives a pure imaginary transverse pair. The zero eigenvalue is tangent to the equilibrium curve.

The first-quadrant smooth arc has exactly one transition point
\[
E_+=(x_+,y_+,0)\approx(1.1367844797,0.7438652721,0),
\]
where \(y_+\) is the unique root in \((0.7438,0.7439)\) of
\[
75y^6+240y^5+197y^4-32y^3-92y^2-64y-16=0,
\]
and
\[
x_+=\frac{10y_+^3+16y_+^2+2y_+}{5y_+^2+8y_++4}.
\]
The component from \((1,0,0)\) to \(E_+\) is saddle-normal; the remainder of that arc, from \(E_+\) to \((0,1,0)\), is center-normal.

The fourth-quadrant smooth arc has exactly one transition point
\[
E_-=(x_-,y_-,0)\approx(1.0648057445,-0.9192381665,0),
\]
where \(y_-\) is the unique root in \((-0.9193,-0.9192)\) of
\[
75y^6+240y^5+137y^4-128y^3-12y^2+64y-16=0,
\]
and
\[
x_-=\frac{-10y_-^3-16y_-^2+2y_-}{5y_-^2+8y_--4}.
\]
The component from \((1,0,0)\) to \(E_-\) is saddle-normal; the remainder from \(E_-\) to \((0,-1,0)\) is center-normal. Every smooth equilibrium in the second and third quadrants is center-normal. At \(E_+\) and \(E_-\), all three eigenvalues are zero.

## Assumptions and scope
The statement concerns only the source parameter slice \(a=4\), \(b=5/2\) and only equilibria with \(xy\ne0\), where the vector field is differentiable. The four axis equilibria \((\pm1,0,0)\) and \((0,\pm1,0)\) are not assigned a Jacobian type because \(|xy|\) is not differentiable there.

"Center-normal" is a spectral statement: it means one tangent zero eigenvalue and a nonzero pure imaginary transverse pair. It does not assert nonlinear Lyapunov stability, existence of a center manifold filled with periodic orbits, or attraction. "Saddle-normal" means one tangent zero eigenvalue together with one positive and one negative real transverse eigenvalue.

## Proof
On a smooth quadrant of the equilibrium curve, write \(|xy|=sxy\), where \(s\in\{-1,1\}\). At an equilibrium \((x,y,0)\), define
\[
h(y)=4y+\frac52y^2,
\qquad
g_s(x,y)=x^2-sxy+y^2-1.
\]
The Jacobian is
\[
J=\begin{pmatrix}
0&0&1\\
0&0&-h(y)\\
2x-sy&2y-sx&0
\end{pmatrix}.
\]
Direct expansion gives
\[
\det(\lambda I-J)
=\lambda\left[\lambda^2-\bigl(2x-sy-h(y)(2y-sx)\bigr)\right]
=\lambda(\lambda^2-T).
\]
This proves the local spectral alternatives.

It remains to locate the zeros of \(T\) on \(g_s=0\). For \(s=1\), the equation \(2T=0\) is linear in \(x\):
\[
(5y^2+8y+4)x-(10y^3+16y^2+2y)=0.
\]
Eliminating \(x\) with \(x^2-xy+y^2=1\) yields exactly
\[
P_+(y)=75y^6+240y^5+197y^4-32y^3-92y^2-64y-16.
\]
A Sturm sequence shows that \(P_+\) has exactly two real roots, one in \((-0.4060,-0.4059)\) and one in \((0.7438,0.7439)\). The negative root gives \(x>0\), hence \(xy<0\), and therefore belongs to the wrong sign branch. The positive root gives \(x>0\), so it is the unique transition on the first-quadrant arc. The one-sided value of \(T\) at \((1,0)\) is \(2>0\), while \(T(1,1)=-11/2<0\); uniqueness of the zero fixes the stated sign partition. On the third-quadrant arc there is no valid zero, and \(T(-1,-1)=-5/2<0\), so the whole smooth arc is center-normal.

For \(s=-1\), the linear equation for a transition can be written
\[
(5y^2+8y-4)x+(10y^3+16y^2-2y)=0.
\]
Elimination with \(x^2+xy+y^2=1\) gives
\[
P_-(y)=75y^6+240y^5+137y^4-128y^3-12y^2+64y-16.
\]
A Sturm sequence shows that \(P_-\) has exactly two real roots, one in \((-0.9193,-0.9192)\) and one in \((0.2913,0.2914)\). Both yield \(x>0\); therefore only the negative root has \(xy<0\) and is valid for this branch. It is the unique fourth-quadrant transition. Again the one-sided value near \((1,0)\) is \(2>0\), while \(T(1,-1)=-1/2<0\). The second-quadrant arc has no valid zero and \(T(-1,1)=-15/2<0\), so it is center-normal throughout.

## Verification
The included `verify.py` uses exact rational arithmetic only. It reconstructs both elimination sextics from the equilibrium and transition equations, builds their Sturm sequences, proves that each sextic has exactly two real roots, proves the stated rational isolating intervals contain one root each, and checks the sign information that selects the two physically valid quadrant roots. It also checks exact signs of \(T\) at representative equilibria. Running `python3 verify.py` prints `VERIFY_OK`; the captured output is included as `VERIFY_OUTPUT.txt`.

The numerical coordinates of \(E_+\) and \(E_-\) are only decimal displays of the algebraically defined roots. The proof itself uses the exact sextics, rational root-isolating intervals, and sign arguments.

## Relationship to prior work
Wang, Pham, and Volos introduce the cloud-shaped equilibrium curve, display the defining vector field, and numerically study hidden chaotic dynamics, bifurcation behavior, Lyapunov exponents, circuit realization, and antisynchronization. Their equilibrium discussion identifies the curve \(x^2-|xy|+y^2=1\) but does not compute a Jacobian spectrum along the curve or partition its smooth arcs by transverse type.

Searches using the exact DOI, title, defining equations, the phrases "cloud-shaped equilibrium" and "normal stability", and the two transition-polynomial structures did not locate a prior statement of this two-transition classification. Related literature on infinite-equilibrium chaotic systems discusses other vector fields, other curve shapes, or stability intervals for different models and does not imply the present sextic boundaries by specialization.

## Limitations
The four nondifferentiable axis equilibria require a nonsmooth analysis and are intentionally left unclassified. Purely imaginary transverse eigenvalues do not prove nonlinear center behavior or stability. The result does not determine basins of attraction, does not reassess whether any numerically displayed attractor is hidden, and does not prove existence or persistence of the paper's chaotic attractor. The classification is exact only for \(a=4\) and \(b=5/2\); other parameter values require a fresh sign analysis.

## References
1. X. Wang, V.-T. Pham, and C. Volos, “Dynamics, Circuit Design, and Synchronization of a New Chaotic System with Closed Curve Equilibrium,” *Complexity* 2017, Article 7138971. DOI: 10.1155/2017/7138971. Published 16 February 2017.
2. MSC2020, 37C10: Dynamics induced by flows and semiflows.
