# Sharp parameter-uniform oscillation cutoff for the fast-\(x\) Oregonator reduction

## Finding

Consider the **fast-\(x\) quasi-steady reduction**, not the full three-dimensional Oregonator and not the alternative fast-\(y\) Tyson reduction. For positive parameters \(q,f,s,\omega\), define

\[
X_q(y)=\frac{1-y+\sqrt{(1-y)^2+4qy}}{2q},\qquad
\dot y=\frac{-y(1+X_q(y))+fz}{s},\qquad
\dot z=\omega(X_q(y)-z).
\]

Let \(q_*\) be the unique positive root of

\[
10q^3+6q^2+12q-1=0,
\qquad q_*\approx0.0797323143464641.
\]

**Sharp global oscillation-cutoff theorem.** For all \(q\ge q_*\), for every \(f,s,\omega>0\), this planar system has a unique positive equilibrium, which attracts every solution starting in \(y,z\ge0\). There are no nonconstant periodic orbits. For each \(0<q<q_*\), some positive choices of \(f,s,\omega\) give a hyperbolic repelling equilibrium surrounded by at least one periodic orbit in the strictly positive quadrant. Thus \(q_*\) is exactly the threshold, uniform in the other three parameters, separating impossible from possible self-sustained planar oscillation.

## Assumptions and scope

The equation results from the Field--Noyes dimensionless kinetics \(\dot x=s(y-xy+x-qx^2)\), \(\dot y=[-y-xy+fz]/s\), \(\dot z=\omega(x-z)\) by imposing \(\dot x=0\) and using the positive root \(x=X_q(y)\). Treat the resulting two-dimensional ODE as an exact standalone model. All parameters are strictly positive; initial \(y,z\) may be zero. Neither a finite-\(s\) approximation error bound nor a three-dimensional conclusion is asserted.

For every \(y\ge0\), \(X_q(y)>0\) and

\[
m\le X_q(y)\le M,\qquad
m=\min\{1,1/q\},\quad M=\max\{1,1/q\}.
\]

The function is smooth for \(y\ge0\). Positivity of the half-axes follows from \(\dot y|_{y=0}=fz/s\ge0\) and \(\dot z|_{z=0}=\omega X_q(y)>0\). Solutions on the boundary become strictly positive for positive time.

## Proof

**1. Exact equilibrium and derivative reduction.** At equilibrium \(z=x=X_q(y)\) and \(y=fx/(1+x)\). The nullcline \(y(1-x)+x-qx^2=0\) gives

\[
q x^2+(q+f-1)x-(1+f)=0.
\]

Its constant term is negative and its quadratic coefficient positive, so exactly one positive root \(x_*=\bigl(1-q-f+\sqrt{(q+f-1)^2+4q(1+f)}\bigr)/(2q)\) exists. It lies strictly between \(m\) and \(M\) if \(q\ne1\); at \(q=1\), \(x_*=1\). The corresponding equilibrium is \((y_*,z_*)=(fx_* /(1+x_*),x_*)\).

Write \(h(y)=y(1+X_q(y))\). When \(0<q<1\), \(x=X_q(y)\) ranges from \(1/q\) down to \(1\), and implicit differentiation of \(y=x(1-qx)/(x-1)\) yields

\[
X_q'(y)=-\frac{(x-1)^2}{D},\quad
h'(y)=\frac{N(x,q)}{D},\quad
D=qx^2-2qx+1>0,
\]
\[
N(x,q)=2qx^3-2qx^2-2qx-x^2+2x+1.
\]

**2. Sharp sign transition.** For \(1<x\le(1+\sqrt5)/2\), the coefficient of \(q\) in \(N\) is nonpositive. Because the admissible range obeys \(q\le1/x\),

\[
N(x,q)\ge N(x,1/x)=x^2-1>0.
\]

For \((1+\sqrt5)/2\le x\le1+\sqrt2\), the coefficient of \(q\) is nonnegative and \(N(x,q)\ge -x^2+2x+1\ge0\); at the upper endpoint strict positivity follows from \(q>0\). For \(x>1+\sqrt2\),

\[
N(x,q)\ge0\quad\Longleftrightarrow\quad
q\ge q_0(x):=\frac{x^2-2x-1}{2x(x^2-x-1)}.
\]

Its derivative is

\[
q_0'(x)=-\frac{(x-1)(x^3-3x^2-3x-1)}{2x^2(x^2-x-1)^2}.
\]

The cubic \(P(x)=x^3-3x^2-3x-1\) increases strictly on \(x>1+\sqrt2\) and crosses zero there once, at \(c\approx3.84732210186307\). Therefore \(q_0\) has exactly one maximum on that range, at \(c\). Eliminating \(c\) from \(P(c)=0\) and \(q=q_0(c)\) gives the exact resultant \(-4(10q^3+6q^2+12q-1)\). Because \(10q^3+6q^2+12q-1\) is strictly increasing for \(q>0\), the maximum is \(q_*=q_0(c)\), its unique positive root. Thus \(h'(y)\ge0\) for all \(y\ge0\) whenever \(q_*\le q<1\). For \(q>1\), \(X_q'(y)>0\) and hence \(h'(y)=1+X_q(y)+yX_q'(y)>0\). For \(q=1\), \(X_q\equiv1\) and \(h'\equiv2\). We have proved

\[
q\ge q_*\ \Longrightarrow\ h'(y)\ge0\ \text{for all }y\ge0.
\]

**3. Compact trapping and stability.** Put \(m=\min\{1,1/q\}\) and \(M=\max\{1,1/q\}\). Every trajectory from the closed nonnegative quadrant eventually enters the strictly positive, inward-pointing rectangle

\[
\frac{fm}{4(1+M)}\le y\le1+\frac{2fM}{1+m},
\qquad \frac m2\le z\le2M.
\]

Indeed, \(z'=\omega(X_q(y)-z)\) drives \(z\) into \([m/2,2M]\); then the inequalities \(- (1+M)y+fm/2\le s\dot y\le-(1+m)y+2fM\) drive \(y\) into its indicated interval. Each boundary vector points strictly inward; comparison also proves global existence. This rectangle contains the unique positive equilibrium.

The Jacobian at any point is

\[
J(y,z)=\begin{pmatrix}-h'(y)/s&f/s\\ \omega X_q'(y)&-\omega\end{pmatrix},\quad
\mathrm{tr}J=-h'(y)/s-\omega,
\quad\det J=\frac{\omega}{s}(h'(y)-fX_q'(y)).
\]

At equilibrium, the determinant is positive for all \(q>0\). For \(q<1\), \(X_q'<0\), and since \(y_*-f=-f/(1+x_*)<0\), the expression \(h'-fX_q'=1+x_*+(y_*-f)X_q'\) is positive. If \(q>1\), set \(K(x)=(1-qx)(1+x)-f(x-1)\). Its unique positive root \(x_*\) satisfies \(K'(x_*)<0\), and \(h(y)-fX_q(y)=X_q(y)K(X_q(y))/(X_q(y)-1)\). Here \(x_*<1\) and \(X_q'(y_*)>0\), giving \((h-fX_q)'(y_*)>0\). At \(q=1\), \(h'-fX_q'=2\). Therefore for \(q\ge q_*\), the unique equilibrium is a strict sink (negative trace and positive determinant).

Throughout the interior \(y,z>0\) the divergence is

\[
\frac{\partial\dot y}{\partial y}+
\frac{\partial\dot z}{\partial z}
=-\frac{h'(y)}s-\omega\le-\omega<0.
\]

Bendixson's criterion rules out every nonconstant periodic orbit. Any forward orbit has a nonempty compact omega-limit set in the positive trapping rectangle. Poincaré--Bendixson, together with the absence of periodic orbits, of saddles and of other equilibria, forces its omega-limit to be the unique sink. Hence every nonnegative trajectory converges.

**4. Sharpness and constructive oscillation below the cutoff.** For any \(0<q<q_*\), choose the same \(c>1+\sqrt2\) defined above and put

\[
s=1,\quad y_0=\frac{c(1-qc)}{c-1}>0,\quad
f=\frac{(1+c)(1-qc)}{c-1}>0,\quad
\omega=-\frac{h'(y_0)}2>0.
\]

Because \(q<q_*=q_0(c)<1/c\), we have \(X_q(y_0)=c\) and \(h'(y_0)<0\). The unique equilibrium \((y_0,c)\) then has positive trace \(-h'(y_0)/2\) and positive determinant, so it is a hyperbolic source. A sufficiently small ellipse around it has a strictly outward-pointing vector field (by the matrix Lyapunov equation for a hyperbolic source). The compact outer trapping rectangle above points inward. Their difference is a positively invariant annulus with no equilibrium. Poincaré--Bendixson guarantees a nonconstant periodic orbit in that annulus, entirely in \(y,z>0\). This proves that the universal no-cycle cutoff cannot be decreased.

## Verification

A standalone Python/SymPy checker in `verify.py` reconstructs the inverse nullcline derivative, the exact numerator for \(h'\), the derivative of \(q_0\), the elimination resultant, and the unique positive numerical root. Run `python verify.py` with a Python environment containing SymPy. It prints \(c\approx3.84732210186307\) and \(q_*\approx0.07973231434646\). The global-attraction and periodic-orbit claims are analytical consequences of the displayed inward bounds and planar theorems, not finite-experiment extrapolations.

## Relationship to prior work

The 1974 Field--Noyes article introduced the Oregonator and studied oscillatory behavior, including a dimensional reduction. The University of Arizona open textbook explicitly displays this precise fast-\(x\) algebraic reduction as equation (8.3), provides numerical phase portraits, and poses fixed-point/stability exercises. The distinguishing claim here is the **parameter-uniform, sharp if-and-only-if oscillation-possibility threshold**, including constructive cycles on the opposite side, rather than the existence of individual numerical oscillations.

Llibre--Oliveira (2019 preprint, 2022 journal) proves a periodic orbit when its **different fast-\(y\) planar model** has an unstable equilibrium. He--Zhao (2024) studies weak foci and up to two small cycles in that alternative rational fast-\(y\) family. Cai--Liu--Zhang (2018) likewise uses fast-\(y\) elimination and a delay. Their existence and bifurcation statements do not furnish the present parameter-independent threshold for the fast-\(x\) square-root model. Studies of the full three-dimensional Oregonator are not automatically statements about this exact planar reduction. Troy (1977) also discusses a **different threshold**, the size of a perturbation that triggers a transient spike returning to equilibrium, as described in its indexed abstract; that abstract does not establish the present parameter-uniform periodic-orbit criterion, while its full text remains a historical-overlap risk.

## Limitations

No assertion is made that the same sharp parameter boundary applies to the full three-dimensional Oregonator, to a nonzero fast-variable relaxation time, or to other normalizations of \(q\) without transforming parameters. For \(q<q_*\), the theorem guarantees oscillation **for some** positive auxiliary parameters, not for all such parameters; neither uniqueness nor orbital stability of the constructed periodic orbit is claimed. The historical full text of certain early papers was inaccessible, so bibliographic priority is not conclusively certified. No independent audit has been performed.

## References

1. R. J. Field and R. M. Noyes, *Oscillations in chemical systems. IV. Limit cycle behavior in a model of a real chemical reaction*, Journal of Chemical Physics **60** (1974), 1877--1884. DOI: 10.1063/1.1681288 (public issue date 1974-03-01).
2. *Introduction to Mathematical Modeling*, University of Arizona Open Textbook, chapter *Chemical Reactions*, Oregonator equations (8.2)--(8.3). https://opentextbooks.library.arizona.edu/mathematicalmodeling/chapter/chemical-reactions/
3. J. Llibre and R. Oliveira, *On the limit cycle of a Belousov--Zhabotinsky differential systems*, Mathematical Methods in the Applied Sciences **45** (2022), 579--584. DOI: 10.1002/mma.7798; full 2019 accepted preprint at https://web.icmc.usp.br/SCATUSU/RT/Serie_Matematica/Serie_Mat_444.pdf.
4. Z. He and Y. Zhao, *Hopf bifurcation and limit cycle of the two-variable Oregonator model for Belousov--Zhabotinsky reaction*, Mathematical Methods in the Applied Sciences **47** (2024), 14600--14609. DOI: 10.1002/mma.10291.
5. Y. Cai, L. Liu, and C. Zhang, *Hopf-zero bifurcation of Oregonator oscillator with delay*, Advances in Difference Equations (2018), article 438. DOI: 10.1186/s13662-018-1894-2.
6. Z. Zheng, T. Zhou, Z. Zhang, and S. Zhang, *Periodic solution and global structure of Oregonator*, Chaos, Solitons & Fractals **11** (2000), 1191--1195. DOI: 10.1016/S0960-0779(99)00025-9.
7. W. C. Troy and R. J. Field, *The Amplification Before Decay of Perturbations Around Stable States in a Model of the Zhabotinskii Reaction*, SIAM Journal on Applied Mathematics **32** (1977), 306--322. DOI: 10.1137/0132024.
8. W. C. Troy, *A threshold phenomenon in the Field--Noyes model of the Belousov--Zhabotinskii reaction*, Journal of Mathematical Analysis and Applications **58** (1977), 233--248 (indexed abstract concerns perturbation-triggered transients).
