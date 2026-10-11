# Invariant-leaf dissipation threshold and Hamiltonian period growth in the Jafari–Sprott LE2 flow

## Finding

Consider the Jafari–Sprott LE2 family
\[
\dot x=y,\qquad \dot y=-x+yz,\qquad \dot z=-y-a x y-b xz.
\]
At the natural coupling-removal boundary \(b=0\), the polynomial
\[
C=x+z+\frac a2x^2
\]
is a global first integral. It reduces each invariant surface to
\[
\dot x=y,\qquad
\dot y=-x+\left(C-x-\frac a2x^2\right)y,
\qquad z=C-x-\frac a2x^2.
\]
For every \(a\geq0\) and \(C\leq0\), excluding \((a,C)=(0,0)\), every orbit with initial \(y>-1\) is forward complete, remains within \(y>-1\), and converges to the unique equilibrium \((0,0,C)\) on its leaf.

Exactly at \(a=0=C\), the entire region \(y>-1\), apart from the equilibrium, consists of periodic trajectories. On the periodic level \(h>0\) of
\[
H=\frac{x^2}{2}+y-\log(1+y),
\]
the least period satisfies the two sharp limits
\[
\lim_{h\downarrow0}T(h)=2\pi,
\qquad \lim_{h\to\infty}\frac{T(h)}{\sqrt h}=2\sqrt2.
\]
For \(a=b=0\), a leaf with \(C\ne0\) has no nonconstant recurrent trajectories, and its only compactly supported invariant probability measure is the mass at \((0,0,C)\). All compactly supported invariant probability measures of the three-dimensional system at \(a=b=0\) are mixtures of such equilibrium atoms and the normalized orbit measures on the \(C=0\) periodic trajectories. At \(a=b=C=0\), initial conditions \(y<-1\) instead have finite-time escape in both directions, and the invariant line \(y=-1\) is complete but unbounded.

## Assumptions and scope

The parameters \(a,b,C\) are real, while the convergence claim additionally assumes \(a\ge0\), \(C\le0\), \((a,C)\ne(0,0)\), \(b=0\), and \(y(0)>-1\). The periodic and escape statements assume \(a=b=C=0\). All invariant-measure claims concern compactly supported Borel probability measures invariant under the flow on their support; such a flow is globally defined on the support. The first integral and reduced field are exact identities, requiring no global-completeness assumption. The level surfaces are parabolic for \(a\ne0\) and affine planes for \(a=0\).

The 2013 source's numerical chaotic examples are at different parameters. The original primary paper and its 2015 erratum define the LE2 vector field; neither supplies the conclusions below.

## Proof

**Polynomial reduction.** Direct differentiation yields
\[
\frac d{dt}\left(x+z+\frac a2x^2\right)=-bxz.
\]
Thus \(C\) is constant for \(b=0\), and substitution for \(z\) gives the claimed planar field. For \(y>-1\), define \(H=x^2/2+y-\log(1+y)\). The scalar function \(y-\log(1+y)\) is nonnegative, vanishes only at \(y=0\), and tends to infinity as \(y\downarrow-1\) or \(y\to\infty\). A direct Lie derivative calculation gives the exact dissipation law
\[
\dot H=\frac{[C-(a/2)x^2]y^2}{1+y}.
\]
Under the stated signs \(H\) is nonincreasing, and its sublevel sets are compact subsets of \(\{y>-1\}\). The continuation theorem therefore gives forward existence and invariance of the region. The zero-dissipation set consists of \(y=0\), and, at \(C=0\), also \(x=0\). On \(y=0\) one has \(\dot y=-x\); on \(x=0\) one has \(\dot x=y\). Accordingly, the largest invariant subset on which \(\dot H=0\) is \((x,y)=(0,0)\) provided \((a,C)\ne(0,0)\). LaSalle's invariance principle implies convergence, with \(z\to C\).

**The Hamiltonian boundary.** For \(a=C=0\), introduce \(v=\log(1+y)\) on \(y>-1\). Then
\[
\dot x=e^v-1,\qquad \dot v=-x,
\qquad H=\frac{x^2}{2}+W(v),\quad W(v)=e^v-v-1.
\]
These are Hamilton's equations for a one-degree-of-freedom system. The potential \(W\) is smooth, strictly convex, coercive, and has unique minimum \(W(0)=0\), \(W''(0)=1\). Hence each level \(h>0\) is a regular simple closed oval and a periodic orbit, and small-energy linearization gives \(T(h)\to2\pi\). With \(v_-(h)<0<v_+(h)\) determined by \(W(v_\pm)=h\), exact quadrature gives
\[
T(h)=\sqrt2\int_{v_-(h)}^{v_+(h)}\frac{dv}{\sqrt{h-W(v)}}.
\]
As \(h\to\infty\), the turning points satisfy \(v_-=-h-1+o(1)\) and \(v_+=\log h+o(1)\). On the negative interval, \(h-W(v)=v-v_--(e^v-e^{v_-})\). The subinterval \([v_-,-1]\) contributes \(2\sqrt h(1+o(1))\) to the integral: rescaling \(s=(v-v_-)/h\), the integrand tends to \(s^{-1/2}\) and admits an integrable bound because \(1-e^v\ge1-e^{-1}\) there. The bounded interval \([-1,0]\) contributes \(O(h^{-1/2})\). On the positive interval, using monotonicity of \(W\), splitting at \(v_+-1\) and the exponentially increasing derivative of \(W\) near \(v_+\) gives an upper bound \(O((1+\log h)/\sqrt h)\). Thus the integral is \(2\sqrt h(1+o(1))\) and \(T(h)/\sqrt h\to2\sqrt2\).

**Other trajectories and invariant measures.** At \(a=0,b=0,C\ne0\), \(\dot H=C y^2/(1+y)\) on \(y>-1\), with strict sign except when \(y=0\), and only \((0,0)\) is invariant within its zero set. When \(y<-1\), \(\dot x=y<-1\), precluding recurrence. At \(y=-1\), \(\dot y=-C\), so crossings (if any) have only one orientation for the fixed \(C\ne0\). Consequently there are no nonstationary recurrent states on those leaves. For \(C=0\), \(y=-1\) is invariant and \(x(t)=x(0)-t\). In \(y<-1\), the additional conserved function \(H_-=x^2/2+y-\log(-1-y)\) implies \(y=-x^2/2+O(\log|x|)\) on every such level as \(|x|\to\infty\); because \(\dot x=y<-1\), the travel-time integrals towards both ends of the \(x\)-axis converge. Thus these trajectories reach infinity in finite positive and negative time. Nonstationary recurrent points on \(C=0\) are precisely those on the periodic ovals in \(y>-1\). Poincaré recurrence and ergodic decomposition classify all compactly supported invariant probability measures into equilibrium atoms and normalized periodic-orbit measures.

## Verification

The included `verify.py` checks the polynomial first integral, invariant-leaf reduction, exact dissipation law, crossing orientation, associated Dulac divergence, and Hamiltonian small-amplitude linearization using exact symbolic algebra. Optional numerical quadratures check representative finite-energy periods but are not proofs of either infinite-energy limit or completeness. The analytic proof above provides these global steps.

## Relationship to prior work

Jafari and Sprott (2013) introduced nine quadratic chaotic flows with a line of equilibria. Their LE2 equations, as clarified in the 2015 erratum, give the exact input ODE. The original paper focuses on example parameters, numerical attractors, and their basins; its printed analysis does not contain the zero-coupling foliation, strict Lyapunov threshold, global Hamiltonian period law, or invariant-measure classification established here.

A later article by Jalal, Amen, and Sulaiman examines Darboux integrability for the **different LE1 system**, whose third equation begins with \(-x\), whereas LE2's begins with \(-y\). Its nonintegrability conclusions therefore do not imply statements about this LE2 boundary. Another published analysis of a 2022 line-equilibrium model treats \(\dot z=x^2-by^2\), a different vector field and not a specialization of LE2. General Hamiltonian-period and Lyapunov principles underlie parts of the proof, but the first integral, parameter restrictions, and asymptotic classification are specific to LE2.

## Limitations

This theorem does not assert global forward completeness for trajectories with \(y\le-1\), for positive \(C\), or away from \(b=0\). At \(b=0\), \(a<0\) is not classified. The asymptotic period law is for \(a=C=b=0\); other parameters need not have periodic orbits. A literature search cannot exclude an earlier unindexed equivalent treatment of this oscillator. The earliest precisely dated public listing used for source provenance is the 2013 journal manifestation; an earlier online-first release cannot be excluded. None of the evidence establishes novelty beyond the compared accessible literature or independent validation.

## References

1. S. Jafari and J. C. Sprott, “Simple chaotic flows with a line equilibrium,” *Chaos, Solitons & Fractals* **57** (2013), 79–84, DOI: 10.1016/j.chaos.2013.08.018. Full primary text: https://sprott.physics.wisc.edu/pubs/paper409.pdf.
2. S. Jafari and J. C. Sprott, “Erratum to ‘Simple chaotic flows with a line equilibrium’,” *Chaos, Solitons & Fractals* (2015), DOI: 10.1016/j.chaos.2015.05.002. Full primary text: https://sprott.physics.wisc.edu/pubs/paper444.pdf.
3. A. A. Jalal, A. I. Amen, and N. A. Sulaiman, “Darboux integrability of the simple chaotic flow with a line equilibria differential system,” *Chaos, Solitons & Fractals* (2020), article 109712, DOI: 10.1016/j.chaos.2020.109712. (Different LE1 vector field; used for comparison only.)
