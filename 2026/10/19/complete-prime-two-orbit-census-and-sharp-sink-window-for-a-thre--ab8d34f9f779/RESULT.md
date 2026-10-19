# Complete prime-two orbit census and sharp sink window for a three-dimensional parabolic map

## Finding

For the real map
\[
F(x,y,z)=\bigl(a y^2,\;b y(1-z),\;c(1-x)\bigr),\qquad a,b,c>0,
\]
put \(B=b(c-1)\) and \(v=abc\). The number of distinct primitive two-cycles in the **entire real phase space**, counting cyclic interchange as the same orbit, is
\[
N_2=\begin{cases}0,&B\leq1,\\1,&1<B\leq2,\\3,&B>2.\end{cases}
\]
For \(B>1\), the sole symmetric cycle has successive \(y\)-coordinates \(r,-r\), where \(r=\sqrt{(B-1)/v}\). Its two-step Floquet characteristic polynomial is
\[
P_{\rm sym}(\lambda)=\lambda^3-\lambda^2+4(B-1)\lambda-4(B-1)^2.
\]
It is a locally exponentially attracting two-cycle if and only if
\[
1<B<\frac{3+\sqrt5}{4}.
\]
At the upper endpoint a nonreal conjugate pair of Floquet multipliers lies on the unit circle, while the third lies strictly inside. For \(B>2\), two additional nonsymmetric primitive two-cycles exist. For **each** additional cycle,
\[
P_{\rm asym}(\lambda)=\lambda^3-\lambda^2+2(B^2-2)\lambda-4,
\]
with exactly one real multiplier in \((0,1)\) and a nonreal pair of modulus greater than \(2\). Thus neither additional cycle is locally attracting.

## Assumptions and scope

The parameters \(a,b,c\) are strictly positive. No boundedness, positivity, or initial-condition restriction is imposed on the state \((x,y,z)\in\mathbb R^3\). A primitive two-cycle comprises two distinct points interchanged by \(F\). Its two-step multipliers are the eigenvalues of \(DF\) at the second point times \(DF\) at the first point. An exponentially attracting cycle means all these multipliers have modulus strictly less than one.

For \(B>1\), define \(r^2=(B-1)/v\). The symmetric cycle is
\[
(a r^2,r,c(1-a r^2))\longleftrightarrow
(a r^2,-r,c(1-a r^2)).
\]
When \(B>2\), let, independently for \(\varepsilon\in\{-1,1\}\),
\[
S_\varepsilon=\varepsilon\sqrt{(B-2)/v},\quad
D=\sqrt{(B+2)/v},\quad
s_\varepsilon=(S_\varepsilon+D)/2,\quad
 t_\varepsilon=(S_\varepsilon-D)/2.
\]
The two extra cycles are
\[
(a t_\varepsilon^2,s_\varepsilon,c(1-a s_\varepsilon^2))
\longleftrightarrow
(a s_\varepsilon^2,t_\varepsilon,c(1-a t_\varepsilon^2)),
\qquad\varepsilon\in\{-1,1\}.
\]

## Proof

**Exact reduction.** Write \(s=y_0\), \(t=y_1\) on a two-periodic trajectory. The other coordinates are forced by the update equations:
\[
x_0=a t^2,\quad x_1=a s^2,\quad
z_0=c(1-a s^2),\quad z_1=c(1-a t^2).
\]
The two remaining equations are exactly \(t=g(s)\) and \(s=g(t)\), where
\[
g(u)=-B u+v u^3.
\]
Conversely, any solution of these two scalar equations lifts uniquely to a two-periodic point of \(F\) by the displayed coordinates. If \(s=t\), all three coordinates are fixed, so primitive two-cycles require \(s\ne t\).

**Complete count.** Subtracting the equations \(g(s)=t\) and \(g(t)=s\), then factoring by \(s-t\), gives
\[
v(s^2+st+t^2)=B-1.
\]
The left side is positive for distinct real \(s,t\), proving impossibility when \(B\leq1\). If \(s+t=0\), the equation becomes \(v s^2=B-1\), yielding exactly one symmetric orbit for each \(B>1\). If \(s+t\ne0\), adding the two equations and factoring by \(s+t\) yields
\[
v(s^2-st+t^2)=B+1.
\]
Subtracting the two quadratic relations gives \(st=-1/v\), and therefore
\[
(s+t)^2=(B-2)/v,\qquad (s-t)^2=(B+2)/v.
\]
Nonsymmetric real solutions exist precisely when \(B>2\). For each of the two possible signs of \(s+t\), the sign of \(s-t\) merely interchanges the two points. Thus there are exactly two extra cycles, proving the count at all parameter values, including \(B=2\).

**Floquet spectra.** At a state \((x,y,z)\), the Jacobian is
\[
J(y,z)=\begin{pmatrix}0&2ay&0\\0&b(1-z)&-by\\-c&0&0\end{pmatrix}.
\]
Substitution of the forced periodic coordinates into \(J(t,z_1)J(s,z_0)\) gives, using \(v s^2=B-1\) and \(t=-s\), the symmetric polynomial stated above. For nonsymmetric cycles use \(v st=-1\) and \(v(s^2+t^2)=B\) to obtain the second stated polynomial. These are identities in the original three-dimensional Jacobian, not merely the derivative of the one-dimensional cubic factor. In either case the trace of the two-step Jacobian is \(1\).

**Sharp attraction boundary.** Set \(d=B-1>0\). For the symmetric characteristic polynomial \(\lambda^3+a_1\lambda^2+a_2\lambda+a_3\), the coefficients are \(a_1=-1\), \(a_2=4d\), \(a_3=-4d^2\). The strict degree-three Schur/Jury conditions are
\[
|a_3|<1,\qquad 1+a_1+a_2+a_3>0,\qquad
1-a_1+a_2-a_3>0,\qquad
1-a_2+a_1a_3-a_3^2>0.
\]
The first gives \(d<1/2\); on this interval the second is \(4d(1-d)>0\) and the third is \(2+4d+4d^2>0\). The fourth is
\[
1-4d+4d^2-16d^4
=-(4d^2-2d+1)(4d^2+2d-1),
\]
strictly positive exactly when \(0<d<(\sqrt5-1)/4\). The intersection is precisely \(1<B<(3+\sqrt5)/4\). Smoothness of \(F\) and strict spectral contraction imply local exponential attraction. At the endpoint \(4d^2+2d=1\), factorization gives
\[
P_{\rm sym}(\lambda)=(\lambda-4d^2)(\lambda^2-2d\lambda+1).
\]
The quadratic has a nonreal unit-modulus pair because \(0<d<1\), and \(0<4d^2<1\). No nonlinear attraction claim is made at equality.

For \(B>2\), the derivative of \(P_{\rm asym}\) is \(3\lambda^2-2\lambda+2(B^2-2)>0\) on the entire real line. Since \(P_{\rm asym}(0)=-4\) and \(P_{\rm asym}(1)=2(B^2-4)>0\), there is a unique real root \(\rho\in(0,1)\). The other two roots are nonreal conjugates whose product is \(4/\rho>4\); each consequently has modulus \(2/\sqrt\rho>2\). The additional cycles are unstable.

## Verification

The accompanying `verify.py` independently recomputes both difference/sum factorizations, the symbolic \(3\times3\) Floquet polynomials modulo the respective cycle equations, the Schur-factor identity, and exact state-update and Jacobian identities at five rational choices \(B=6/5,3/2,2,5/2,4\). Run `python verify.py` with SymPy installed. Finite checks are corroboration, not a substitute for the complete symbolic argument above.

## Relationship to prior work

Wang, Tong, Li, Zhang, Iu and Li introduce the three-dimensional polynomial map as a precursor to a four-dimensional memristive extension. Their 2023 article gives fixed-point analysis and numerical parameter-dependent Lyapunov/bifurcation plots; the inspected article sections do not present the exact primitive-two census and three-dimensional Floquet stability boundary here. General one-dimensional odd-cubic period-two algebra contributes the scalar reduction, while the additional three-dimensional Floquet and Schur analysis is necessary to determine attraction. Published descriptions of complete two-cycle classifications for the Duffing and Bogdanov maps concern different planar systems and do not imply the present three-dimensional spectrum.

## Limitations

The classification covers primitive period two only, not higher periods, global basins, or the four-dimensional memristive extension. The characteristic polynomials determine linear stability; the possible nonlinear bifurcation type precisely at the unit-circle threshold is not established. The source-comparison claim is limited to the accessible full-text HTML representation, targeted searches and mathematical-record summaries; it does not certify absolute historical priority. The normalized threshold does not depend separately on \(a\), but individual orbit coordinates do.

## References

- M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu and Z. Li, “A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor,” *Symmetry* **15** (2023), 1879; first published 2023-10-06. DOI: https://doi.org/10.3390/sym15101879.
- E. Iqbal, “Stability of Sampled-Data Systems,” *Introduction to Control Systems*, §7.4 (Jury stability test), https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Introduction_to_Control_Systems_%28Iqbal%29/07%3A_Design_of_Sampled-Data_Systems/7.03%3A_Stability_of_Sampled-Data_Systems.
