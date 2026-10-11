# Sharp recurrence exclusion and oscillator realizability in six-parameter quadratic jerk flows

## Finding
Consider the six-parameter quadratic jerk system introduced in the 2015 study of nine nonhyperbolic-equilibrium flows:
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=b_2y+b_3z+b_4x^2+b_5y^2+b_7xy+b_8xz,
\]
with real coefficients, \(b_4\ne0\), and \(\beta=b_5-b_8\). There is a sharp dichotomy *for the existence of nontrivial compact dynamics somewhere in each coefficient fiber*:

1. If \(b_4\beta\ge0\), every bounded forward solution converges to the unique equilibrium \((0,0,0)\). The only nonempty compact **two-sided invariant** set is \(\{(0,0,0)\}\), and the only compactly supported invariant Borel probability measure is the point mass there. In particular, no nonconstant periodic orbit or bounded complete non-equilibrium trajectory exists.
2. If \(b_4\beta<0\), every compactly supported invariant probability measure \(\mu\) instead satisfies the exact stationary moment constraint
\[
\int y^2\,d\mu=-\frac{b_4}{\beta}\int x^2\,d\mu.
\]
The opposite-sign condition is not sufficient for recurrence at every individual parameter choice, but it is *sharp as a uniform exclusion criterion*: for every prescribed pair \((b_4,\beta)\) with \(b_4\beta<0\), there are choices of the remaining coefficients for which a continuum of nonconstant periodic orbits exists. More precisely, with \(\omega=\sqrt{-b_4/\beta}>0\), choose
\[
b_2=-\omega^2,\quad b_3=b_5=b_7=0,\quad b_8=-\beta.
\]
Then every \(R>0\) and phase \(\theta\in\mathbb R\) yields the periodic orbit
\[
(x,y,z)(t)=\bigl(R\cos(\omega t+\theta),\ -R\omega\sin(\omega t+\theta),\ -R\omega^2\cos(\omega t+\theta)\bigr)
\]
of least period \(2\pi/\omega\).

In the original study's nine examples A--I, all printed coefficients have \(b_4(b_5-b_8)<0\), in agreement with this necessary condition for any nontrivial compact recurrent regime.

## Assumptions and scope
The phase space is all of \(\mathbb R^3\). All six coefficients are arbitrary real constants, subject only to \(b_4\ne0\). This ensures that \((0,0,0)\) is the unique equilibrium: an equilibrium requires \(y=z=0\) and \(b_4x^2=0\). A *bounded forward solution* has a trajectory contained in some compact subset of phase space for all positive time on its maximal interval; local smoothness and boundedness then imply forward completeness. A compact two-sided invariant set means a compact set on which the restricted flow exists for all real times and maps the set onto itself. It should not be confused with a merely positively invariant compact set, which can contain trajectories converging to the origin. Invariant measures are invariant under the flow on their compact support.

## Proof
Define the globally polynomial observable
\[
P(x,y,z)=z-b_3y-b_2x-\frac{b_7}{2}x^2-b_8xy.
\]
Direct differentiation, using \(\frac{d}{dt}(xy)=y^2+xz\) and \(\frac{d}{dt}(x^2/2)=xy\), gives the exact coboundary
\[
\boxed{\dot P=b_4x^2+(b_5-b_8)y^2=b_4x^2+\beta y^2.}
\]

Suppose \(b_4\beta\ge0\). Multiplication by \(s=\operatorname{sgn}(b_4)\) yields \(\frac{d}{dt}(sP)=|b_4|x^2+s\beta y^2\ge0\). Along any bounded forward orbit, \(sP\) is monotone and bounded, and therefore tends to a finite limit. Its nonempty compact omega-limit set is invariant. On that set the continuous observable \(sP\) is constant at its limiting value, hence its derivative vanishes on every entire orbit in the omega-limit set. Since \(|b_4|>0\), this forces \(x=0\) there. Any complete trajectory entirely contained in \(\{x=0\}\) must have \(y=\dot x=0\) and \(z=\dot y=0\). Thus the omega-limit set consists solely of the origin, proving convergence of every bounded forward orbit. This reasoning remains valid when \(\beta=0\).

For a bounded complete trajectory, apply the same argument in reversed time using the monotone function \(-sP\). Both the positive and negative limit sets are the origin, so \(P(t)\) has identical zero limits at both ends. Monotonicity makes \(P\) constant for all time, whence \(x\equiv0\), and consequently \(y\equiv z\equiv0\). Every orbit in any compact two-sided invariant set is bounded and complete, so the set is just the origin.

Let \(\mu\) be a compactly supported invariant probability measure. Invariance and boundedness of \(P\) on the support give \(\int \mathcal L_FP\,d\mu=0\), hence
\[
 b_4\int x^2\,d\mu+\beta\int y^2\,d\mu=0.
\]
If \(b_4\beta\ge0\), multiplying by \(s\) forces \(\int x^2\,d\mu=0\), so \(x=0\) almost everywhere. Invariance implies that almost every corresponding full orbit has \(x(t)=0\) at every rational time, and by continuity at every real time; differentiation then gives \(y=z=0\). Thus \(\mu=\delta_{(0,0,0)}\). If \(b_4\beta<0\), rearrangement yields the claimed stationary second-moment identity.

Finally suppose \(b_4\beta<0\). With the explicit coefficient choices in the finding, \(z=-\omega^2x\) defines an invariant plane because there \(\dot z=-\omega^2y\); the quadratic residual \((b_4+\beta\omega^2)x^2\) vanishes identically. The planar equations are \(\dot x=y\), \(\dot y=-\omega^2x\), hence the stated harmonic periodic trajectories exist for every \(R>0\). They show no uniform nonrecurrence conclusion can extend to the opposite-sign sector. The nine sign checks follow by substituting the published Table 1 coefficients; they are independently reproduced by the attached exact checker.

## Verification
Run `python CHECK.py` with SymPy installed. The script checks the polynomial Lie derivative, each harmonic solution and cancellation condition, the period-average second moments, and the signs of all nine coefficient triples in the 2015 table. Its symbolic assertions pass. These calculations verify algebraic steps; the infinite-time assertions rely separately on the compactness, invariance, and monotonicity proof above, not on numerical integration.

## Relationship to prior work
Wei, Sprott and Chen [1] introduce exactly this six-coefficient family (their Eq. (4)) and list nine numerical chaotic models (their Table 1). Their four-page article examines equilibrium spectra and reported bifurcation simulations, rather than a coefficient-uniform monotone polynomial, global bounded-orbit convergence, invariant-measure rigidity, or the sharp oscillator construction. Liu, Sang, Wang and Ahmad [2] use a polynomial monotonicity argument to exclude bounded chaos in a different quadratic jerk equation containing a linear position term and a quadratic acceleration term; that equation does not have the unique nonhyperbolic-equilibrium family studied here. The related 2015 study [3] analyzes periodic-orbit bifurcation for a particular nonhyperbolic jerk equation; only its abstract was accessible, so it remains a historical-priority risk rather than proof of noncoverage. The proposed theorem makes no claim of general novelty independent of available sources.

## Limitations
This result does not assert that arbitrary initial conditions produce bounded trajectories, that every system in the opposite-sign cone has a periodic orbit, or that a chaotic attractor exists at any chosen parameter values. The conclusion for all bounded forward trajectories is conditional on boundedness. The compact-set claim concerns two-sided invariant sets, not arbitrary compact forward-invariant sets. Earlier or unindexed work proving an equivalent parameter-uniform result cannot be ruled out. Independent verification has not been performed.

## References
[1] Z. Wei, J. C. Sprott, H. Chen, “Elementary quadratic chaotic flows with a single non-hyperbolic equilibrium,” *Physics Letters A* **379** (2015), 2184–2187. DOI: 10.1016/j.physleta.2015.06.040. Public author archive: https://sprott.physics.wisc.edu/pubs/paper437.pdf. First verified availability: 2015-06-22.

[2] M. Liu, B. Sang, N. Wang, I. Ahmad, “Chaotic Dynamics by Some Quadratic Jerk Systems,” *Axioms* **10** (2021), 227. DOI: 10.3390/axioms10030227.

[3] Z. Wei, W. Zhang, M. Yao, “On the periodic orbit bifurcating from one single non-hyperbolic equilibrium in a chaotic jerk system,” *Nonlinear Dynamics* **82** (2015), 1251–1258. DOI: 10.1007/s11071-015-2230-y. The available comparison is limited to the public abstract.
