# Hidden ambient periodicity and positive Bessel period shear near a reversible quadratic cylinder

## Finding
Fix \(a>0\), any \(b_3,b_5,b_6,c\in\mathbb R\), and the quadratic differential system
\[
\dot x=2az,\qquad \dot y=z(b_3+b_5x+b_6y),\qquad
\dot z=c(x^2+z^2-1)-2ax.
\]
This is the constant-angular-coefficient subfamily of the reversible invariant-cylinder normal form described in the first reference. Although the algebraic cylinder \(x^2+z^2=1\) has cofactor \(2cz\) (nonzero for \(c\ne0\)), an entire open three-dimensional neighborhood of that cylinder is foliated by periodic trajectories. Two exact smooth first integrals there (indeed, globally defined) are
\[
H=e^{-(c/a)x}(x^2+z^2-1),\qquad
J=e^{-Bx}y-\frac1{2a}\int_0^x e^{-Bs}(b_3+b_5s)\,ds,
\quad B=\frac{b_6}{2a}.
\]
The minimal physical-time period depends only on \(h=H\). In a neighborhood of \(h=0\), it is smooth and obeys
\[
T(0)=\frac\pi a,\qquad
T'(0)=\frac{\pi c}{2a^2}I_1(c/a)\ge0,
\]
with equality if and only if \(c=0\). Here the modified Bessel function is normalized by
\[
I_1(s)=\frac1{2\pi}\int_0^{2\pi} e^{s\cos u}\cos u\,du.
\]
In particular, for each fixed nonzero \(c\), \(T(h)\) increases strictly with \(h\) sufficiently near zero. The shear coefficient does not depend on the three coefficients governing the axial coordinate. Every periodic orbit in this neighborhood has all three Floquet multipliers equal to one, even though its original-time period is not constant when \(c\ne0\).

## Assumptions and scope
All parameters are fixed real numbers, with \(a>0\); no smallness of \(c\) or of the axial coefficients is assumed. By a tubular neighborhood of the cylinder we mean \(U=\{(x,y,z):(x,z)\in A\}\), where \(A\) is a sufficiently thin annulus about the unit circle; \(y\) is unrestricted. All periodicity and monotonicity assertions concern this neighborhood and \(h\) sufficiently near zero, not the entire phase space. Solutions are understood in original (unrescaled) time. In the \(c=0\) case the local periods are exactly \(\pi/a\).

## Proof
**First integrals.** Set \(F=x^2+z^2-1\). Direct differentiation along the polynomial vector field yields
\[
\dot F=2x(2az)+2z(cF-2ax)=2czF.
\]
Because \(\dot x=2az\), differentiation of \(e^{-cx/a}F\) gives zero. Likewise, with \(B=b_6/(2a)\),
\[
\frac d{dt}(e^{-Bx}y)=ze^{-Bx}(b_3+b_5x)
=\frac d{dt}\left(\frac1{2a}\int_0^x e^{-Bs}(b_3+b_5s)\,ds\right),
\]
so \(\dot J=0\). Their differentials are independent on a neighborhood of the unit cylinder: \(\partial_yJ=e^{-Bx}\ne0\), and \(dH\) has a nonzero component in the \((x,z)\)-plane because \(dH\) restricts to \(e^{-(c/a)x}dF\) along the unit circle.

**Periodic foliation.** Write \(\lambda=c/a\). On \(H=h\),
\[
z^2=Q_h(x):=1-x^2+h e^{\lambda x}.
\]
At \(h=0\), the zeros \(-1,1\) of \(Q_0\) are simple, and \(Q_0>0\) between them. Consequently for some \(\epsilon>0\), the component of \(\{H=h\}\) close to the unit circle in the \((x,z)\)-plane is a smooth oval for every \(|h|<\epsilon\). It has two simple turning points \(x_-(h)<x_+(h)\), close to \(-1,1\), with upper and lower arcs \(z=\pm\sqrt{Q_h(x)}\). Since \(\dot x=2az\), each oval is traversed without equilibrium and its minimal original-time period is
\[
T(h)=\frac1a\int_{x_-(h)}^{x_+(h)}\frac{dx}{\sqrt{Q_h(x)}}.
\]
The integration endpoints are smooth in \(h\). Factoring the two simple endpoint zeros and substituting a cosine coordinate regularizes the integral, making \(T\) smooth (indeed real analytic) near \(h=0\). On a given oval, \(J\) determines \(y\) uniquely by
\[
y=e^{Bx}\left(J+\frac1{2a}\int_0^x e^{-Bs}(b_3+b_5s)\,ds\right).
\]
Thus \(y\) returns whenever \(x\) does, giving a complete periodic orbit at every point in the corresponding three-dimensional tubular neighborhood. The \(J\) coordinate cannot change the period. At \(h=0\), \(x(t)=\cos(2at+\phi)\) and \(z(t)=-\sin(2at+\phi)\), so \(T(0)=\pi/a\).

**The exact period derivative.** Differentiating \(\dot x=2az\) once and eliminating \(z\) and \(F\) with \(H=h\) gives
\[
\ddot x+4a^2x=2ac h e^{\lambda x}.
\]
Use the smooth small-\(h\) family of periodic solutions with its positive turning point as phase origin. With \(u=\omega(h)t\), set
\[
x(t,h)=\cos u+hX_1(u)+O(h^2),\qquad
\omega(h)=2a+h\omega_1+O(h^2),
\]
where \(X_1\) is \(2\pi\)-periodic. Equating the first powers of \(h\) produces
\[
4a^2(X_1''+X_1)=2ac e^{\lambda\cos u}+4a\omega_1\cos u.
\]
The left-hand side has zero first cosine Fourier coefficient. Taking that coefficient on the right, using \(\pi^{-1}\int_0^{2\pi}e^{\lambda\cos u}\cos u\,du=2I_1(\lambda)\), yields \(4ac I_1(\lambda)+4a\omega_1=0\), hence \(\omega_1=-cI_1(c/a)\). Since \(T(h)=2\pi/\omega(h)\),
\[
T'(0)=\frac{\pi c I_1(c/a)}{2a^2}.
\]
For real \(s\), the defining integral or its positive-coefficient power series shows that \(I_1(s)\) has the sign of \(s\) and vanishes only at zero. Therefore \(cI_1(c/a)>0\) for \(c\ne0\), proving strict local period monotonicity. If \(c=0\), the projected oscillator is exactly harmonic for every nearby level and its period is constant.

**Floquet interpretation.** The two independent first integrals form transverse coordinates to each periodic trajectory. A local transverse first-return map preserves both coordinates and is therefore the identity. Its two multipliers are one; the tangential multiplier is also one. In the full fixed-time variational flow, the nonzero derivative \(T'(0)\) produces a nontrivial phase shear for \(c\ne0\), compatible with this completely neutral multiplier spectrum.

## Verification
The accompanying `verify_period.py` tests both exact first-integral identities numerically along a full orbit, checks the return of all three coordinates, compares centered finite differences of the regularized period integral with the closed-form Bessel coefficient for five positive and negative parameter combinations, and checks sample monotonicity near zero. The script uses Python 3 with NumPy and SciPy. It is a diagnostic, not a proof of the infinite or parameter-uniform statements; the proof above establishes those statements.

## Relationship to prior work
Messias, Reinol and Rodrigues de Lima give the encompassing reversible quadratic normal form and establish local period annuli *on* invariant cylinders. In their discussion with nonzero cofactor they explicitly distinguish the dynamics off the distinguished cylinder, for which the circular-cylinder polynomial first integral is unavailable. The present result identifies a genuinely different, nonpolynomial pair of ambient integrals in the constant-angular-coefficient subfamily, proves that nearby *off-cylinder* dynamics is also periodic, and calculates its original-time Bessel period derivative. Thus it is not the already established on-cylinder annulus statement. Llibre and Serantola classify simpler invariant-cylinder polynomial flows with a genuine circular-radius first integral; their corresponding planar circular rotations are isochronous and do not give the nonzero-cofactor exponential foliation or its period shear. Standard perturbative Fourier solvability supplies a proof technique, but does not itself specify this coefficient or its strictly positive sign for this dynamical family.

## Limitations
The integrability and periodic foliation require the precise equalities that set the two extra angular couplings to zero; generic members of the seven-parameter normal form need not share them. Nothing here classifies the full phase portrait away from the stated tubular neighborhood or proves global period monotonicity. Only local nonisochrony at \(h=0\) is shown for nonzero \(c\). The exact formulas are reproducible analytically, but comparison with all possibly uncatalogued integrability and period-function literature remains a bibliographic limitation. No independent audit is claimed.

## References
1. M. Messias, A. C. Reinol, and C. A. B. Rodrigues de Lima, *Time-reversal symmetric quadratic differential systems having an invariant cylinder: global dynamics and mechanical application*, International Journal of Dynamics and Control 14, article 353 (first public version verified 2026-09-02), https://doi.org/10.1007/s40435-026-02300-0.
2. J. Llibre and L. P. Serantola, *The easiest polynomial differential systems in R3 having an invariant cylinder*, Extracta Mathematicae 40 (2025), 121–141, https://doi.org/10.17398/2605-5686.40.1.121.
