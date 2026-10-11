# Complete Hamiltonian foliation and separatrix timing at zero damping in the Sprott J flow

## Finding
For the classical two-parameter Sprott J system
\[
\dot x=a z,\qquad \dot y=-b y+z,\qquad \dot z=-x+y+y^2,
\]
the zero-damping slice \(b=0\), with arbitrary \(a>0\), admits two global polynomial first integrals
\[
C=x-ay,\qquad H=\frac{z^2}{2}+xy-\frac{a+1}{2}y^2-\frac{y^3}{3}.
\]
Moreover, for the vector field \(F\),
\[
F=\nabla H\times\nabla C,\qquad \operatorname{div}F=0.
\]
In particular, the flow is Hamiltonian on every invariant affine plane \(C=c\). The following is a **complete classification of its bounded complete trajectories** for every \(c\in\mathbb R\), including a sharp separatrix-period asymptotic.

Set
\[
V_c(y)=-\frac{y^3}{3}+\frac{a-1}{2}y^2+cy,\quad
\Delta=(a-1)^2+4c.
\]
* If \(\Delta<0\), no bounded two-sided trajectory exists.
* If \(\Delta=0\), the only bounded two-sided trajectory is the equilibrium \((ay_0+c,y_0,0)\), with \(y_0=(a-1)/2\).
* If \(\Delta>0\), write \(L=\sqrt\Delta\), \(r_\pm=(a-1\pm L)/2\), \(E_\pm=V_c(r_\pm)\). There are exactly two equilibria on the leaf: a center at \(r_-\) and a saddle at \(r_+\); their energy gap is \(E_+-E_-=L^3/6\). All other bounded complete trajectories are the periodic orbits with \(E_-<H<E_+\), one such orbit per energy, and the single homoclinic loop to the saddle at \(H=E_+\), modulo time translation.

The homoclinic loop has the explicit parametrization
\[
y(t)=r_+-\frac{3L}{2}\operatorname{sech}^2\!\left(\frac{\sqrt L}{2}(t-t_0)\right),\quad
z(t)=\frac{3L^{3/2}}{2}\operatorname{sech}^2\!\left(\frac{\sqrt L}{2}(t-t_0)\right)
\tanh\!\left(\frac{\sqrt L}{2}(t-t_0)\right),\quad x(t)=a y(t)+c.
\]
For every periodic energy \(E\in(E_-,E_+)\), the cubic equation \(V_c(y)=E\) has precisely three real roots \(q_1<q_2<q_3\). With \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\), its least period is
\[
T(E)=\frac{4\sqrt{3/2}}{\sqrt{q_3-q_1}}K(k),\qquad
k^2=\frac{q_2-q_1}{q_3-q_1}.
\]
For fixed \(a,c\) with \(\Delta>0\), this satisfies the exact endpoint laws
\[
\lim_{E\downarrow E_-}T(E)=\frac{2\pi}{\sqrt L},\qquad
T(E)=\frac{1}{\sqrt L}\log\!\left(\frac{72L^3}{E_+-E}\right)+o(1)
\quad(E\uparrow E_+).
\]
Finally, every compactly supported invariant Borel probability measure of this flow is a mixture (in the ergodic-decomposition sense) of equilibrium Dirac measures and the normalized time measures on the above periodic orbits. Thus no invariant probability mass is carried by any nonstationary homoclinic trajectory.

## Assumptions and scope
The real state space is \(\mathbb R^3\), \(a>0\), and exactly \(b=0\). For each \(c\in\mathbb R\), a **bounded complete trajectory** means a classical solution defined for every \(t\in\mathbb R\) whose image is bounded. The flow of the cubic vector field can have non-global trajectories elsewhere; no claim of global completeness is made. The leaf parameter \(c\) ranges over all real values, and all energy statements refer to the restricted Hamiltonian \(H|_{C=c}\). A mixture of periodic-orbit measures is a possibly continuous mixture, not necessarily finite or countable.

## Proof
**1. The global Nambu and Hamiltonian reductions.** Direct differentiation gives \(\dot C=\dot x-a\dot y=0\) and \(\dot H=0\). More precisely, exact polynomial differentiation shows \(F=\nabla H\times\nabla C\). The coordinate change \((x,y,z)\mapsto(c,y,z)=(x-ay,y,z)\) is an invertible linear transformation of determinant \(1\). Its equations are
\[
\dot c=0,\qquad \dot y=z,\qquad
\dot z=y^2-(a-1)y-c=-V_c'(y),
\]
and \(H|_{C=c}=E_c=z^2/2+V_c(y)\). Hence every leaf is a one-degree-of-freedom Hamiltonian system with the standard area form \(dy\wedge dz\). The Nambu representation also implies \(\operatorname{div}F=0\).

**2. All bounded complete trajectories.** The scalar acceleration factors as
\[
\ddot y=y^2-(a-1)y-c=\left(y-\frac{a-1}{2}\right)^2-\frac\Delta4.
\]
When \(\Delta<0\), \(\ddot y\ge-\Delta/4>0\), which is incompatible with a globally bounded \(y(t)\). For \(\Delta=0\), a bounded convex function on the entire real time axis must be constant, hence the only possibility is the stated equilibrium.

For \(\Delta>0\), the only critical points of \(V_c\) are \(r_-\) and \(r_+\), with \(V_c''(r_-)=L>0\) and \(V_c''(r_+)=-L<0\). The potential decreases from \(+\infty\) on the negative \(y\) axis, has one local minimum and one local maximum, then tends to \(-\infty\). Standard connected-component analysis of \(E_c=z^2/2+V_c(y)=E\) now leaves exactly a center equilibrium, one oval for each \(E\in(E_-,E_+)\), one saddle equilibrium together with its unique left-going homoclinic component at \(E=E_+\), and no other bounded complete orbit. Explicit substitution gives \(E_+-E_-=L^3/6\). At \(E_+\), the energy polynomial has a double root at \(r_+\) and a simple root at \(r_+-3L/2\). Separation of variables, or direct differentiation, yields the displayed \(\operatorname{sech}^2\) homoclinic; its two branches form one time-translated orbit.

**3. Period formula and the sharp logarithmic constant.** On the oscillation interval \([q_1,q_2]\),
\[
2(E-V_c(y))=\frac23(y-q_1)(q_2-y)(q_3-y).
\]
The least period is twice the travel time between its turning points. Substituting \(y=q_1+(q_2-q_1)\sin^2\theta\) proves the elliptic-integral formula above. As \(E\downarrow E_-\), the first two roots coalesce at \(r_-\), the third tends to \(r_++L/2\), and \(k\to0\), giving \(2\pi/\sqrt L\).

Let \(\delta=E_+-E\downarrow0\). Taylor expansion of the cubic about its double root at \(r_+\) gives
\[
q_1=r_+-\frac{3L}{2}+O(\delta),\qquad
q_2=r_+-\sqrt{\frac{2\delta}{L}}+O(\delta),\qquad
q_3=r_++\sqrt{\frac{2\delta}{L}}+O(\delta).
\]
Consequently,
\[
1-k^2=\frac{4\sqrt2}{3}\frac{\sqrt\delta}{L^{3/2}}+O(\delta),\qquad
\frac{4\sqrt{3/2}}{\sqrt{q_3-q_1}}=\frac4{\sqrt L}+O(\sqrt\delta).
\]
The classical endpoint expansion \(K(k)=\log(4/\sqrt{1-k^2})+o(1)\) implies
\[
T(E)=\frac1{\sqrt L}\log\!\left(\frac{72L^3}{\delta}\right)+o(1).
\]
All constants are explicit; this is an analytic limit, not an extrapolation from finitely many orbits.

**4. Stationary probability measures.** Every compactly supported invariant measure has compact invariant support, so it is supported on the union of bounded complete trajectories classified above. By the Poincaré recurrence theorem, almost every point is recurrent. A nonstationary point on a homoclinic loop is not recurrent: both its forward and backward limits are the saddle, not itself. The remaining recurrent components consist of equilibria and periodic orbits. The only ergodic invariant probabilities on these components are Dirac masses and normalized time averages over one periodic orbit. Ergodic decomposition yields the stated exhaustive mixture classification.

## Verification
The accompanying `verify.py`, run under Python 3.13 with SymPy 1.14, checks exact symbolic conservation of both polynomials, equality of the Nambu cross product to the original field, zero divergence, the Hamiltonian leaf reduction, factorization of the equilibrium polynomial, the exact center-to-saddle energy gap, and direct substitution of the explicit homoclinic including its turning point and asymptote. The period integral, exhaustive topology of one-dimensional energy levels, Poincaré-recurrence step and elliptic endpoint limit are independently justified analytically above; a symbolic test alone is not their proof.

## Relationship to prior work
Sprott introduced the nineteen simple chaotic flows, including case J, in 1994; the original paper catalogs equations, equilibria and numerically observed chaotic dynamics, rather than analyzing the integrable zero-damping boundary. Sprott's 2013 parameter atlas explicitly lists the two-parameter case J equations and concentrates on observed attracting regimes. Islam, Islam and Nikolov (2015) study stability and adaptive control for strictly positive damping \(b>0\); their statements do not cover the plane \(b=0\) or imply its two polynomial first integrals. The new point is a complete, system-specific **global leafwise** classification and its exact separatrix timing, not an assertion that cubic one-degree-of-freedom Hamiltonians or elliptic-integral asymptotics are novel in general.

A broader analytical study by Panchev (2004) and the jerk-flow analysis of Letellier and Vallée (2003) are plausible historical precedents. Their accessible abstracts/bibliographic records were examined, but full text could not be verified here; equivalence with any uninspected material remains a genuine priority risk. This limitation is substantive, not an assertion of noncoverage.

## Limitations
This is a theorem only on the \(b=0\) boundary; it does not classify the positive-damping chaotic regime, persistence or splitting of the separatrix for \(b\ne0\), or trajectories which are not bounded and complete. The explicit separatrix formula is up to time translation. The phrase "one homoclinic" counts an orbit modulo time translation, not distinct starting times. Unseen historical treatments, particularly the two identified older analytical papers, could reduce or remove novelty. Independent external audit has not been performed.

## References
1. J. C. Sprott, "Some simple chaotic flows," *Physical Review E* **50**, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647 (publisher date 1994-08-01).
2. J. C. Sprott, "Dynamic Regions in Simple Chaotic Flows" (2013), https://sprott.physics.wisc.edu/technote/regions.htm (case J equations and parameter charts).
3. M. Islam, N. Islam and S. Nikolov, "Adaptive control and synchronization of Sprott J system with estimation of fully unknown parameters," *Journal of Theoretical and Applied Mechanics* **45**(2), 45–58 (2015), https://jtambg.eu/papers/2015/JTAM2015_2_045-58.pdf.
4. S. Panchev, "Analytical properties of the Sprott's chaotic flows," *Chaos, Solitons & Fractals* **21** (2004), DOI: 10.1016/j.chaos.2003.12.054 (full-text comparison unresolved).
5. C. Letellier and O. Vallée, "Analytical results and feedback circuit analysis for simple chaotic flows," *Journal of Physics A* **36**, 11229–11245 (2003), DOI: 10.1088/0305-4470/36/44/004 (full-text comparison unresolved).
