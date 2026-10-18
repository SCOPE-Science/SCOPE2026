# A sharp subcritical Hopf threshold in the Wang–Dong–Li hidden-attractor flow

## Finding
Consider the quadratic flow of Wang, Dong and Li,
\[
\dot x=a(y-x),\qquad \dot y=-cy-xz,\qquad \dot z=y^2-b+kxy,
\]
and fix the source's reference damping parameters \(a=12\) and \(c=10\). For **every** \(b>0\) and \(k>0\), both equilibria
\[
E_\pm(k)=\left(\pm\sqrt{\frac b{k+1}},\;\pm\sqrt{\frac b{k+1}},\;-10\right)
\]
are asymptotically stable exactly when \(k<10\). At \(k=10\), both undergo simultaneous, transverse, **subcritical Hopf bifurcations**. For \(k>10\), each equilibrium has one stable real eigenvalue and two eigenvalues with positive real part. Consequently, for each fixed \(b>0\) and for \(k<10\) sufficiently close to ten there are two distinct, symmetry-related, small saddle-type periodic orbits shrinking to \(E_\pm(10)\) as \(k\uparrow10\). The two cycles each have one nontrivial unstable Floquet direction and one contracting direction.

Set \(s=\sqrt{b/11}>0\) and use the Hopf eigenvector normalization \(q_z=1\) with the conventional first Lyapunov coefficient \(\ell_1=\operatorname{Re}G_{21}/(2\omega)\). Its exact value at either equilibrium is
\[
\boxed{\ell_1(b)=\frac{\sqrt3\,s(61s^2+23364)}{96(3s^2+121)^2(12s^2+121)}>0.}
\]
The critical frequency is \(\omega=2\sqrt3\,s\), and the real-part crossing speed is
\[
\boxed{\left.\frac{d}{dk}\operatorname{Re}\lambda_+(k)\right|_{k=10}=\frac{b}{5324+12b}>0.}
\]
These statements concern the *local* dynamics near the equilibria, not global attraction or the existence of chaos.

## Assumptions and scope
The vector field is smooth and polynomial on \(\mathbb R^3\); \(b\) is an arbitrary fixed strictly positive real parameter. The bifurcation parameter is \(k>0\), with \(a=12,c=10\) fixed. A Hopf coefficient depends on eigenvector and time conventions: here \(q_z=1\), the adjoint vector is normalized by \(\langle p,q\rangle=1\) in the Hermitian pairing, and the formula of the standard quadratic Hopf normal form is used. The sign of \(\ell_1\) is invariant under nonzero eigenvector rescaling.

## Proof
The equilibria follow from \(y=x\), \(z=-10\), and \((k+1)x^2=b\). They are exchanged by \((x,y,z)\mapsto(-x,-y,z)\). At \(E_+(k)\), putting \(t=\sqrt{b/(k+1)}\), the Jacobian is
\[
A_k=\begin{pmatrix}-12&12&0\\10&-10&-t\\kt&(k+2)t&0\end{pmatrix},\qquad
\det(\lambda I-A_k)=\lambda^3+22\lambda^2+\frac{b(k+2)}{k+1}\lambda+24b.
\]
The Routh–Hurwitz determinant is exactly
\[
22\frac{b(k+2)}{k+1}-24b=\frac{2b(10-k)}{k+1}.
\]
All characteristic coefficients are strictly positive. Thus all eigenvalues have negative real parts for \(0<k<10\). At \(k=10\) the characteristic polynomial factors as
\[
(\lambda+22)(\lambda^2+12b/11),
\]
so the two critical eigenvalues are simple and imaginary. For \(k>10\), the Routh criterion gives an unstable conjugate pair; positivity of all coefficients excludes a positive real root, and the third eigenvalue is negative. Differentiating the characteristic equation at \(\lambda=i\omega\) gives the positive real-part crossing speed displayed above.

It remains to determine Hopf criticality rather than infer it from a plot. At \(k=10\), put \(D=121+3s^2\). The quadratic part at \(E_+(10)\) has the symmetric Hessian bilinear map
\[
B(u,v)=\begin{pmatrix}0\\-(u_xv_z+u_zv_x)\\2u_yv_y+10(u_xv_y+u_yv_x)\end{pmatrix}.
\]
The critical Jacobian is
\[
A=\begin{pmatrix}-12&12&0\\10&-10&-s\\10s&12s&0\end{pmatrix}.
\]
Explicit complex right/left eigenvectors are
\[
q=\begin{pmatrix}(3s+11\sqrt3 i)/D\\(-5s+\sqrt3 i(s^2+22))/(2D)\\1\end{pmatrix},\qquad
p_0=\begin{pmatrix}5\sqrt3 i/3\\2\sqrt3 i\\1\end{pmatrix}.
\]
Direct multiplication gives \(Aq=i\omega q\), \(A^Tp_0=-i\omega p_0\), and \(\overline{p_0}^{\,T}q=2\). Thus set \(p=p_0/2\). Since there is no cubic term in the vector field, the standard formula specializes to
\[
G_{21}=\overline p^{\,T}\left[B\bigl(\overline q,(2i\omega I-A)^{-1}B(q,q)\bigr)-2B\bigl(q,A^{-1}B(q,\overline q)\bigr)\right].
\]
Both inverses exist because the three eigenvalues of \(A\) are \(-22\) and \(\pm i\omega\), with \(\omega>0\). In particular, one obtains exactly
\[
A^{-1}B(q,\overline q)=\begin{pmatrix}(s^2+132)/(44sD)\\(s^2+132)/(44sD)\\6/D\end{pmatrix}.
\]
Substitution of the displayed vectors and bilinear form, followed by clearing nonzero denominators, gives
\[
\operatorname{Re}G_{21}=\frac{s^2(61s^2+23364)}{8D^2(12s^2+121)}
\]
and hence the displayed factorization for \(\ell_1=\operatorname{Re}G_{21}/(2\omega)\). Every factor is positive for \(s>0\). The positive crossing and positive cubic Lyapunov coefficient satisfy the nondegenerate subcritical Hopf hypotheses. Hence small saddle periodic orbits exist on the stable-equilibrium side \(k<10\), with nontrivial radial Floquet expansion, and vanish at \(k=10\). Reflection symmetry gives the identical result at the other equilibrium. \(\square\)

## Verification
The accompanying standalone program `check.py` reconstructs the equilibria, characteristic polynomial, Routh determinant and crossing identity; it then verifies both eigenvector equations and the quadratic-normal-form coefficient *symbolically*, including the exact positive factorization. Run it with `python3 check.py` after installing SymPy. The positivity for every \(s>0\) comes from the displayed analytic factorization rather than from its sampled values.

## Relationship to prior work
Wang, Dong and Li (2022) introduced the displayed flow, studied hidden/coexisting attractors, and numerically varied \(k\) over a range containing ten. That numerical parameter survey is acknowledged as prior work. The finding here is the exact Hopf threshold and the sign and closed form of the cubic Hopf coefficient **uniformly in the source's other varied parameter** \(b>0\), together with its local saddle-cycle consequence. Published work on a recurrence shell for this *same* flow proves invariant-measure bounds, but these do not imply a local eigenvalue crossing or the cubic normal form. Other known local Hopf calculations for *different* quadratic systems employ similar general methods but cannot imply this flow-specific coefficient.

## Limitations
No global basin structure, global continuation of either small periodic orbit, stability of a chaotic attractor, or existence of any particular global chaotic orbit is established. A general Hopf bifurcation theorem supplies the local existence conclusion; the novel content asserted is the exact verification of its nondegeneracy and direction for this flow. The publisher's complete article and any supplementary files could not be accessed during comparison; the relevant publicly indexed sections were examined, and uncatalogued equivalent previous calculations remain a priority risk. Independent verification has not been performed.

## References
1. J. Wang, C. Dong, and H. Li, “A New Variable-Boostable 3D Chaotic System with Hidden and Coexisting Attractors: Dynamical Analysis, Periodic Orbit Coding, Circuit Simulation, and Synchronization,” *Fractal and Fractional* **6** (2022), 740. DOI: 10.3390/fractalfract6120740. First verified public date: 2022-12-14.
2. “Exact recurrence shell in the Wang–Dong–Li variable-boostable flow,” publicly indexed published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-recurrence-shell-in-the-wang-dong-li-variable-boostable-fl--0eb4288eae95.
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer (2004), Hopf normal-form conventions.
