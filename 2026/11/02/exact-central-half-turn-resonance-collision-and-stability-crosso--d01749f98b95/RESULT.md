# Exact central half-turn resonance collision and stability crossover in the biquadratic nontwist map

## Finding

The central rotation-\(1/2\) resonance of the biquadratic nontwist map admits a complete four-orbit classification, an **exact collision curve**, and an independent sharp linear-stability crossover. The collision is singular: its two-step derivative is **exactly the identity**, rather than merely having trace two. For a nonempty open parameter region, two linearly elliptic constant-height cycles coexist with two hyperbolic height-reversing cycles. The crossover at which the elliptic coexistence region disappears is given explicitly by a unique scalar equation.

## Assumptions and scope

Let \(F:\mathbb T\times\mathbb R\to\mathbb T\times\mathbb R\) be

\[
 y'=y-b\sin(2\pi x),\qquad F(x,y)=\left(x+\omega(y')\pmod1,y'\right),\qquad
 \omega(v)=a(1-v^2)(1-\varepsilon v^2).
\]

Throughout, \(1/2<a<1\), \(0<\varepsilon\le1\), and \(0<b\le1\). A *central half-turn two-cycle* means an orbit of least period two, with both heights in \((-1,1)\) and angular increment \(1/2\pmod1\) in each step. No claim is made about period-two orbits outside this naturally distinguished resonance class.

Define
\[
 t=\frac{1+\varepsilon-\sqrt{(1-\varepsilon)^2+2\varepsilon/a}}{2\varepsilon},
 \quad Y=\sqrt t,\quad
 w=\omega'(Y)=-2aY(1+\varepsilon-2\varepsilon t),
 \quad b_c=2Y,\quad b_f=\frac1{\pi|w|}.
\]
Then \(0<t<1\), \(0<Y<1\), \(w<0\), and \(\omega(Y)=1/2\).

**Theorem.** Exactly two central half-turn two-cycles exist if \(0<b<b_c\), three if \(b=b_c\), and four if \(b>b_c\) (subject always to \(b\le1\)). Two cycles always exist:
\[
 C_{\pm}:\ (0,\pm Y)\longleftrightarrow(1/2,\pm Y),
 \qquad \operatorname{tr}DF^2(C_{\pm})=2-(2\pi b w)^2.
\]
They are linearly elliptic for \(b<b_f\), have a double eigenvalue \(-1\) at \(b=b_f\), and are hyperbolic for \(b>b_f\). If \(b>b_c\), set \(\theta=\arcsin(2Y/b)/(2\pi)\in(0,1/4)\). There are exactly two additional cycles:
\[
 R_1:(\theta,Y)\longleftrightarrow(\theta+1/2,-Y),\qquad
 R_2:(1/2-\theta,Y)\longleftrightarrow(1-\theta,-Y).
\]
Their monodromy traces equal
\[
 \operatorname{tr}DF^2(R_j)=2+(2\pi w)^2(b^2-4Y^2)>2,
\]
so both are hyperbolic saddles. At \(b=b_c\) they merge into the single cycle \((1/4,Y)\leftrightarrow(3/4,-Y)\), whose **full** two-step derivative is the identity matrix.

The elliptic–hyperbolic coexistence region is nonempty precisely when \(1/2<a<a_*(\varepsilon)\), where \(t_*(\varepsilon)\in(0,1/4)\) is the unique solution of
\[
 Q_{\varepsilon}(t_*):=2\pi t_*\left(\frac1{1-t_*}+\frac{\varepsilon}{1-\varepsilon t_*}\right)=1,
 \qquad a_*(\varepsilon)=\frac1{2(1-t_*)(1-\varepsilon t_*)}.
\]
For this parameter range every \(b\) with \(b_c<b<\min\{1,b_f\}\) gives two linearly elliptic constant-height cycles and two hyperbolic reversing cycles. At \(a=a_*\), \(b_c=b_f<1\), the reversing-cycle merger has monodromy \(I\) simultaneously with the constant-height cycles having trace \(-2\). In particular,
\[
 t_*(1)=\frac1{1+4\pi},\quad
 a_*(1)=\frac{(1+4\pi)^2}{32\pi^2},\quad
 b_c(a_*(1),1)=\frac2{\sqrt{1+4\pi}}.
\]

## Proof

**1. Exhaustive two-cycle reduction.** Because \(|v|<1\), \(0<\varepsilon\le1\), and \(0<a<1\), we have \(0<\omega(v)\le a<1\). At any central half-turn two-cycle, the angular increment at each step is congruent to \(1/2\); hence \(\omega(y_0)=\omega(y_1)=1/2\), without an integer-winding ambiguity. For \(0<v<1\),
\[
 \omega'(v)=-2av(1+\varepsilon-2\varepsilon v^2)<0
\]
(the last parenthesis is at least \(1-\varepsilon>0\) for \(v<1\)). As \(\omega(0)=a>1/2\) and \(\omega(1)=0\), the equation \(\omega(v)=1/2\) has exactly two roots \(\pm Y\). Solving its quadratic equation in \(t=Y^2\) gives the stated root.

If successive heights have the same sign, they are equal. The momentum kick vanishes, forcing \(\sin(2\pi x)=0\), and the two distinct constant-height cycles are exactly \(C_+\) and \(C_-\). If successive heights have opposite signs, we can choose the first point at height \(+Y\), and the momentum equation becomes \(b\sin(2\pi x)=2Y\). This has zero, one or two solutions modulo one as \(b\) is below, equal to, or above \(b_c=2Y\). The half-turn map sends \(\sin(2\pi x)\) to its negative, so each solution closes in exactly two steps. These are precisely the displayed cycles, and no other central half-turn two-cycle remains.

**2. Exact monodromy.** With \(c=2\pi b\cos(2\pi x)\) and \(u=\omega'(y')\), the one-step Jacobian is
\[
 J(c,u)=\begin{pmatrix}1-cu&u\\-c&1\end{pmatrix},\qquad\det J(c,u)=1.
\]
On a constant-height cycle, the second step changes \(c\) to \(-c\) but keeps \(u\) fixed; direct multiplication gives \(\operatorname{tr}(J(-c,u)J(c,u))=2-c^2u^2\), with \(|c|=2\pi b\), \(|u|=|w|\). For a height-reversing cycle, the second step reverses both \(c\) and \(u\), giving \(\operatorname{tr}(J(-c,-u)J(c,u))=2+c^2u^2\). Here \(\cos^2(2\pi x)=1-(2Y/b)^2\), proving the stated trace. At \(b=b_c\), the first angle is \(1/4\), so \(c=0\) at each step; then \(J(0,w)J(0,-w)=I\). The determinant-one trace criterion proves the linear stability statements.

**3. Unique stability crossover.** The equality \(\omega(Y)=1/2\) yields \(a=[2(1-t)(1-\varepsilon t)]^{-1}\), so
\[
 \frac{b_c}{b_f}=2\pi Y|w|
 =2\pi t\left(\frac1{1-t}+\frac{\varepsilon}{1-\varepsilon t}\right)=Q_{\varepsilon}(t).
\]
For \(0<t<1/4\), each summand in \(Q_\varepsilon\) is strictly increasing; \(Q_\varepsilon(0)=0\) and \(Q_\varepsilon(1/4)\ge2\pi/3>1\). Thus exactly one \(t_*\in(0,1/4)\) has \(Q_\varepsilon(t_*)=1\). The function \(a=[2(1-t)(1-\varepsilon t)]^{-1}\) increases strictly with \(t\). Coexistence requires \(b>b_c\), \(b<b_f\), and \(b<1\); it is possible exactly when \(t<t_*\). At equality the two thresholds coincide. For \(\varepsilon=1\), \(Q_1(t)=4\pi t/(1-t)\), yielding the displayed closed forms.

## Verification

Run `python verify_halfturn.py` with Python 3 and SymPy. It symbolically checks the polynomial root relation, both monodromy trace identities, symplectic determinant, identity monodromy at collision and the closed critical formula when \(\varepsilon=1\). Direct two-step numerical iterations at four parameter triples check each predicted orbit and trace. For \((a,\varepsilon)=(0.515,0.1)\), the exact collision parameter is approximately \(0.325836900672\); the motivating numerical study places the displayed period-two collision near \(b=0.3259\). These numerical checks are corroboration only; the proof above provides the exhaustive classification.

## Relationship to prior work

Grime et al. (2022/2023) introduced this exact map, its symmetries, fixed points, and approximate primary reconnection curves. Their 2023 follow-up explicitly exhibits a numerical period-two collision (Figure 6) and searches its bifurcation curve numerically; it does not report the present central half-turn census, exact algebraic collision threshold, identity monodromy, or the stability crossover. Wurm et al. (2004/2005) give general reversing-symmetry and indicator-curve methods, including exact low-period thresholds for the **standard** nontwist map (the zero-quartic specialization). These earlier methods motivate the argument and can recover aspects of the collision mechanism but do not specify the quartic-model classification and simultaneous flip/collision boundary. Grime et al. (2024/2025) focus on effective transport barriers and odd-period resonance structures. An earlier fixed-point classification for the same biquadratic map addresses period one rather than the rotation-\(1/2\) cycles proved here.

## Limitations

The theorem is restricted to central half-turn period-two orbits whose heights stay in \((-1,1)\); it is **not** a census of arbitrary period-two dynamics on the entire unbounded cylinder. Linear ellipticity does not establish nonlinear (KAM or Lyapunov) stability. Exact coincidence of two bifurcation thresholds is not a claim about global shearless-curve breakup or transport. Standard nontwist symmetry methods may encode parts of the derivation implicitly; a further literature check could reveal an equivalent parameterized calculation not identified here.

## References

- G. C. Grime, M. Roberto, R. L. Viana, Y. Elskens, I. L. Caldas, *Biquadratic Nontwist Map: a model for shearless bifurcations*, arXiv:2209.07408 (first posted 2022-09-15), DOI: 10.1016/j.chaos.2023.113231.
- G. C. Grime et al., *Shearless curve breakup in the biquadratic nontwist map*, arXiv:2305.17538 (2023), particularly Section 4, Figure 6 and Appendix.
- G. C. Grime et al., *Effective transport barriers in the biquadratic nontwist map*, arXiv:2409.00785 (first posted 2024-09-01), especially Sections II and V.
- A. Wurm, A. Apte, K. Fuchss, P. J. Morrison, *Meanders and Reconnection-Collision Sequences in the Standard Nontwist Map*, arXiv:nlin/0411026 (2004), especially Section II.3.
