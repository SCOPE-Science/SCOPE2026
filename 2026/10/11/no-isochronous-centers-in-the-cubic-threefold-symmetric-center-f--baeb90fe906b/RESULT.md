# No isochronous centers in the cubic threefold-symmetric center family

## Finding
For the entire two-real-parameter center family of the three-dimensional cubic system introduced by Huang, Gu, Ouyang and Huang (2023), the equilibrium \((1,0,0)\) is **never isochronous**. In particular, for every choice of \(A,D\in\mathbb R\), the positive minimal periods of its sufficiently small nonconstant periodic orbits are not all equal.

More precisely, let \(T(\rho)\) be the period of the orbit through \((x,y,u)=(1+\rho,0,0)\), for \(0<\rho\ll1\). Put
\[
a=-3A-D-\frac53,\qquad b=-2A-D-\frac23,\qquad c=D,
\]
so \(b=(2a-c)/3+4/9\). The quadratic Taylor coefficient of \(T\) is
\[
T_2=\frac{\pi}{12}\left(a^2-9a+8c+\frac{124}{3}\right).
\]
Whenever \(T_2=0\), the cubic coefficient also vanishes and the quartic coefficient is strictly positive:
\[
\boxed{\displaystyle T_4=\frac{\pi}{4608}
\left(3a^4-46a^3+1147a^2+6416a+69904\right)>0.}
\]
Thus canceling the first nontrivial period defect creates an unavoidable fourth-order defect, rather than an isochronous center.

## Assumptions and scope
The original real, physical-time system is
\[
\begin{aligned}
\dot x&=Ay+(A+D-\tfrac13)xy-(2A+D+\tfrac23)x^2y+xu^2+Dy^3,\\
\dot y&=-x+x^2+yu+2xy^2,\\
\dot u&=(-x+y^2)u.
\end{aligned}
\]
Here the source's coefficients satisfy \(A_{020}=B_{030}=0\), \(A=A_{010}\), \(D=A_{030}\), with no extra restriction. The primary source proves this is exactly its center-parameter locus at \((1,0,0)\), and directly supplies the invariant center manifold \(u=0\). The result concerns local *minimal periods in the original time variable*, not orbital conjugacy after a state-dependent change of time.

Because \(\dot u=(-x+y^2)u\), every sufficiently small periodic orbit lies in \(u=0\): on a sufficiently small fixed neighborhood of \((1,0,0)\), \(-x+y^2<-1/2\), so a nonzero solution of the scalar equation cannot be periodic. The local question is therefore exactly planar.

## Proof
**Reduction and center.** With \(X=x-1\), \(Y=y\), and \(u=0\), direct expansion gives
\[
\dot X=-Y+aXY+bX^2Y+cY^3,\qquad
\dot Y=X+X^2+2Y^2+2XY^2.
\]
The linear eigenvalues are \(\pm i\). This analytic planar system is reversible under \((X,Y,t)\mapsto(X,-Y,-t)\), so its nondegenerate elliptic origin is a center; equivalently this is Theorem 5 of the source restricted to its center locus. For all sufficiently small \(\rho>0\), the orbit from \((\rho,0)\) makes one positive turn and defines an analytic period \(T(\rho)\), with \(T(0)=2\pi\).

**Exact period calculation.** Define \(C=\cos\theta\), \(S=\sin\theta\), \(X=rC\), \(Y=rS\). Direct differentiation yields
\[
\dot r=r^2R_2+r^3R_3,\qquad \dot\theta=1+rH_1+r^2H_2,
\]
where
\[
\begin{aligned}
R_2&=(a+1)C^2S+2S^3,\\
R_3&=bC^3S+(c+2)CS^3,\\
H_1&=C^3+(2-a)CS^2,\\
H_2&=(2-b)C^2S^2-cS^4.
\end{aligned}
\]
For small \(\rho\), the angular speed is positive. The unique angular radial solution has the Taylor expansion
\[
r(\theta;\rho)=\rho+\rho^2u_2(\theta)+\rho^3u_3(\theta)+\rho^4u_4(\theta)+O(\rho^5),
\qquad u_j(0)=0.
\]
Let
\[
S_2=R_2,\quad S_3=R_3-R_2H_1,\quad
S_4=R_2(H_1^2-H_2)-R_3H_1.
\]
Then the coefficients are uniquely defined by elementary trigonometric primitives:
\[
\begin{aligned}
u_2'&=S_2,\\
u_3'&=2u_2S_2+S_3,\\
u_4'&=(2u_3+u_2^2)S_2+3u_2S_3+S_4.
\end{aligned}
\]
Set \(B_2=H_1^2-H_2\), \(B_3=-H_1^3+2H_1H_2\), and \(B_4=H_1^4-3H_1^2H_2+H_2^2\). Expanding the exact physical period integral
\[
T(\rho)=\int_0^{2\pi}\frac{d\theta}{1+r(\theta;\rho)H_1+r(\theta;\rho)^2H_2}
\]
shows that the coefficients of \(\rho^2\), \(\rho^3\), and \(\rho^4\) respectively are
\[
\begin{aligned}
T_2&=\int_0^{2\pi}(-u_2H_1+B_2)\,d\theta,\\
T_3&=\int_0^{2\pi}(-u_3H_1+2u_2B_2+B_3)\,d\theta,\\
T_4&=\int_0^{2\pi}\left[-u_4H_1+(2u_3+u_2^2)B_2+3u_2B_3+B_4\right]d\theta.
\end{aligned}
\]
The omitted linear coefficient is zero because the odd-integrand linear term has zero full-circle average. Exact rational trigonometric integration (reproduced by the accompanying script) gives
\[
\begin{aligned}
\frac{T_2}{\pi}&=\frac{a^2-11a+3b+9c+40}{12},\\
\frac{T_3}{\pi}&=\frac{(a+5)(a^2-11a+3b+9c+40)}{18},\\
\frac{T_4}{\pi}&=\frac1{1152}\bigl(49a^4-310a^3+198a^2b+546a^2c+537a^2\\
&\qquad+30ab+954ac+320a+153b^2+630bc+7008b+945c^2+12720c+49120\bigr).
\end{aligned}
\]
These are coefficient identities for the actual period, not for a time-rescaled normal form.

**Exclusion of all isochronous parameters.** On the source's center locus \(b=(2a-c)/3+4/9\), the condition \(T_2=0\) forces
\[
c=-\frac{a^2-9a+124/3}{8}.
\]
With this substitution \(T_3=0\), while exact simplification of \(T_4\) gives the quartic displayed above. Its numerator has the strictly positive sum-of-squares decomposition
\[
3a^4-46a^3+1147a^2+6416a+69904
=3\left(a^2-\frac{23}{3}a\right)^2
+\frac{2912}{3}\left(a+\frac{1203}{364}\right)^2
+\frac{5396458}{91}>0.
\]
An isochronous center would require every positive-degree Taylor coefficient of \(T\) to vanish. If \(T_2\ne0\) it is not isochronous; if \(T_2=0\), the strictly positive \(T_4\) precludes isochrony. These cases exhaust all \(A,D\in\mathbb R\).

## Verification
The file `check_periods.py` independently reconstructs the polar radial/angular coefficients as exact finite Fourier series with rational symbolic coefficients, integrates the radius recursions with \(u_j(0)=0\), integrates period integrands using their zero Fourier modes, verifies \(T_2,T_3,T_4\), substitutes the two-parameter center relation, and checks the explicit sum-of-squares identity. Run `python check_periods.py` with the version of SymPy specified in `requirements.txt`; success prints `CHECK_OK`. No floating-point experiment or finite enumeration is used as the infinite-parameter proof.

For example, the nonvacuous tuning \((A,D)=(7/6,-31/6)\) gives \((a,b,c)=(0,13/6,-31/6)\), hence \(T_2=T_3=0\) and \(T_4=69904\pi/4608>0\).

## Relationship to prior work
Huang, Gu, Ouyang and Huang (2023), Section 4, Eq. (15), and Theorem 5, establish the complete center locus and its invariant planar restriction; their Section 5 instead computes focus values and limit-cycle bifurcation, and their conclusion explicitly identifies isochronous centers as a further question. The present result studies the same unperturbed vector field, adds physical-time period constants, and excludes isochrony over the complete center locus. The 2023 paper by Gu, Zegeling and Huang computes isochrony conditions for a *different* cubic Kolmogorov vector field with positive-octant equilibrium and multiplicative state equations; its two isochronous families do not imply isochrony or nonisochrony of this system. General treatments of cubic reversible isochronous systems and global isochronous centers likewise do not provide the exact two-parameter local period obstruction established here.

## Limitations
The theorem is local near \((1,0,0)\), assumes the source's exact center locus, and concerns periods in unmodified physical time. It neither counts critical periods on the full period annulus nor studies parameter-perturbed limit-cycle birth, global phase portraits, or noncenter parameters. The cited literature comparison is not a certificate of global novelty; especially, a general classification of reversible cubic isochrones may encode some special cases through changes of variables, but no found result implies the whole stated two-parameter exclusion. Independent validation has not been performed.

## References
1. T. Huang, J. Gu, Y. Ouyang and W. Huang, “Bifurcation of Limit Cycles and Center in 3D Cubic Systems with \(Z_3\)-Equivariant Symmetry,” *Mathematics* 11 (2023), 2563, published 3 June 2023. DOI: 10.3390/math11112563. Full text: https://www.mdpi.com/2227-7390/11/11/2563.
2. J. Gu, A. Zegeling and W. Huang, “Bifurcation of Limit Cycles and Isochronous Centers on Center Manifolds for a Class of Cubic Kolmogorov Systems in \(\mathbb R^3\),” *Qualitative Theory of Dynamical Systems* 22 (2023), 42. DOI: 10.1007/s12346-023-00745-8. Open preprint: https://www.researchgate.net/publication/365718536_Bifurcation_of_Limit_Cycles_and_Isochronous_Centers_on_Center_Manifolds_for_a_Class_of_Cubic_Kolmogorov_Systems_in_R3.
3. L. Cairó, J. Chavarriga, J. Giné and J. Llibre, “Class of reversible cubic systems with an isochronous center,” *Computers & Mathematics with Applications* 38 (1999), 39–53.
4. Y. Li et al., “Isochronous global center of linear plus homogeneous polynomial systems and cubic systems,” *Journal of Differential Equations* 396 (2024), 147–171. DOI: 10.1016/j.jde.2024.02.054.
