# Exact critical omega-limit selection and recurrence simplex in the Linz–Sprott modulus jerk

## Finding

Consider the Linz–Sprott piecewise-linear jerk equation
\[
\dddot x+A\ddot x+\dot x-|x|+1=0,\qquad A\in\mathbb R,
\]
with state \((x,v,w)=(x,\dot x,\ddot x)\). Let \(E_- =(-1,0,0)\) and \(E_+=(1,0,0)\). A *compact stationary state* means a compactly supported invariant Borel probability measure for its flow.

**Critical and outer-regime classification.** For every \(|A|>1\), the complete set of compact stationary states consists exactly of the mixtures of \(\delta_{E_-}\) and \(\delta_{E_+}\); moreover, every bounded forward trajectory converges to one of these equilibria. At \(A=1\), all compact stationary states are precisely the mixtures of \(\delta_{E_+}\) and the uniform orbit measures \(\nu^-_r\) on the circles
\[
\mathcal C^-_r=\{(-1+r\cos\theta,-r\sin\theta,-r\cos\theta):0\le\theta<2\pi\},
\qquad 0\le r\le1.
\]
At \(A=-1\), the analogous complete list is the mixtures of \(\delta_{E_-}\) and the uniform measures \(\nu^+_r\) on
\[
\mathcal C^+_r=\{(1+r\cos\theta,-r\sin\theta,-r\cos\theta):0\le\theta<2\pi\},
\qquad 0\le r\le1.
\]
Here \(r=0\) is the corresponding center equilibrium. More precisely, “mixtures” at \(A=1\), for example, means every measure of the form \(p\delta_{E_+}+(1-p)\int_0^1\nu^-_r\,d\rho(r)\), where \(0\le p\le1\) and \(\rho\) is any Borel probability measure on \([0,1]\); similarly at \(A=-1\).

**Critical omega-limit selection.** At either \(A=1\) or \(A=-1\), the omega-limit set of **every bounded forward trajectory** is exactly one of the displayed circles (including the center equilibrium at \(r=0\)) or the opposite isolated equilibrium. Thus a bounded trajectory approaches a single critical cycle as a set, rather than being able to wander among cycles of different radii. This statement does not require, or assert, convergence of a phase angle along the cycle.

**Sharp global period edge (supporting consequence).** For *every* real \(A\), every nonconstant periodic solution has least period \(T\ge2\pi\). Equality holds **if and only if** \(A=1\) and the orbit is one of \(\mathcal C^-_r\) with \(0<r\le1\), or \(A=-1\) and the orbit is one of \(\mathcal C^+_r\) with \(0<r\le1\). Thus any nonconstant cycle with \(-1<A<1\) has \(T>2\pi\). The critical families form entire annuli of neutral exact cycles, not an isolated small cycle born at a generic Hopf transition.

## Assumptions and scope

The equation holds for all real initial states and all real \(A\). Its vector field is globally Lipschitz, hence has a unique complete flow. The measure classification concerns invariant Borel probability measures with compact support, not merely numerical attractors. The bounded-forward statement requires the particular forward orbit to be bounded and is not an assertion that every trajectory is bounded. The circle classification does not assert that all bounded complete, nonrecurrent connecting trajectories are circles.

## Proof

**1. Two exact coboundaries.** Write \(\dot x=v\), \(\dot v=w\), and \(\dot w=-Aw-v+|x|-1\). Introduce
\[
G=vw+\frac A2v^2-\frac12x|x|+x,
\qquad H=\frac12(v^2+w^2)-v(|x|-1).
\]
Since \(x|x|\) is continuously differentiable, ordinary differentiation gives
\[
\dot G=w^2-v^2.
\]
On either open half-space \(x>0\) or \(x<0\), differentiation also gives
\[
\dot H=-Aw^2-\operatorname{sgn}(x)v^2,
\qquad\frac{d}{dt}(H+AG)=-(A+\operatorname{sgn}(x))v^2.
\]
The second identity holds almost everywhere in time along each trajectory; the first remains valid at \(x=0\). To justify stationary integration at the switching plane without assuming smoothness, replace \(|x|\) in \(H\) by \(h_\epsilon(x)=\sqrt{x^2+\epsilon^2}\). The exact smooth-generator derivative is
\[
\dot H_\epsilon=-Aw^2+w(|x|-h_\epsilon(x))
 -\frac{x}{\sqrt{x^2+\epsilon^2}}v^2.
\]
On compact support, dominated convergence and \(\big||x|-h_\epsilon(x)\big|\le\epsilon\) yield \(\int Aw^2\,d\mu+\int\operatorname{sgn}(x)v^2\,d\mu=0\). Also, every invariant measure satisfies
\[
\int_{\{x=0\}}v^2\,d\mu=0.
\]
Indeed, along any differentiable real function \(x(t)\), its derivative vanishes for almost all times in the level set \(x(t)=0\); invariance and Fubini transfer this fact to \(\mu\). Integrating \(\dot G\) then gives the exact identities
\[
\int w^2\,d\mu=\int v^2\,d\mu=:K,
\qquad
(A+1)\int_{\{x>0\}}v^2\,d\mu
 +(A-1)\int_{\{x<0\}}v^2\,d\mu=0.
\tag{1}
\]
If \(K=0\), invariance forces \(v\equiv0\), then \(w\equiv0\), then \(|x|=1\), on \(\mu\)-almost every complete trajectory. Thus \(\mu\) is supported on \(E_-\) and \(E_+\).

**2. Outer parameters and bounded forward trajectories.** If \(|A|>1\), the two coefficients in the second identity of (1) have the same strict sign; hence \(K=0\). This proves the invariant-measure statement. Furthermore \(L=H+AG\) is strictly decreasing off \(v=0\) for \(A>1\), and strictly increasing off \(v=0\) for \(A<-1\). Along a bounded forward orbit, \(L\) is bounded, so \(\int_0^\infty v(t)^2\,dt<\infty\). Uniform continuity of \(v\), provided by bounded \(w\), yields \(v(t)\to0\). Every point in its nonempty compact omega-limit set therefore has \(v=0\), and invariance of this omega-limit set forces \(w=0\) and \(|x|=1\). That set is connected (it is an intersection of nested closures of connected trajectory tails) and contained in \(\{E_-,E_+\}\); hence it is a singleton and the trajectory converges to that equilibrium.

**3. Exhaustion at the critical parameters.** Let \(A=1\). Equation (1) implies \(\int_{x>0}v^2\,d\mu=0\). For \(\mu\)-almost every complete trajectory, \(v=0\) for almost every time at which \(x>0\), by invariance and Fubini. On any open time interval with \(x>0\), continuity thus forces \(v=w=0\), and the jerk equation forces \(x=1\). Uniqueness implies this entire trajectory is \(E_+\). Every remaining typical trajectory stays in \(x\le0\). On that closed half-space, with \(u=x+1\), the equation is exactly
\[
(D+1)(D^2+1)u=0,
\qquad u(t)=Ce^{-t}+a\cos t+b\sin t.
\]
Compact stationarity makes each typical complete trajectory bounded for all positive *and negative* times, so \(C=0\). The condition \(x(t)\le0\) for every time is equivalent to \(r=\sqrt{a^2+b^2}\le1\). The resulting trajectories are exactly \(\mathcal C^-_r\). Each nonzero circle supports only uniform angular measure, while arbitrary mixtures across radii are invariant. The same reasoning for \(A=-1\) exchanges the half-spaces and gives \((D-1)(D^2+1)(x-1)=0\), hence \(\mathcal C^+_r\). This proves both complete measure lists, including the grazing radius \(r=1\).

**4. Exact critical omega-limit selection.** At \(A=1\), \(L=H+AG\) is nonincreasing along every trajectory, and at \(A=-1\) it is nondecreasing. On any bounded forward orbit it therefore has a finite limit \(\ell\), and \(L\equiv\ell\) on the compact invariant omega-limit set. On each complete trajectory in that set, the time derivative of \(L\) vanishes almost everywhere. The half-space argument in Step 3, now applied pointwise on those complete trajectories, places the omega-limit set inside the union of the corresponding critical circles and the opposite equilibrium. Direct substitution into \(H+AG\) gives
\[
L|_{\mathcal C_r^-}=r^2-\frac12\quad(A=1),\qquad
L|_{\mathcal C_r^+}=r^2-\frac12\quad(A=-1),
\]
and \(L(E_+)=1/2\) at \(A=1\), respectively \(L(E_-)=1/2\) at \(A=-1\). Thus the limiting value \(\ell\) selects a unique circle radius; the only possible tie is between the grazing circle \(r=1\) and the spatially separated opposite equilibrium. Since the omega-limit set is connected, it cannot contain both components. Finally, an invariant nonempty subset of a nonconstant circle under its continuous-time rotation is the whole circle. Hence the omega-limit set is exactly one circle or one isolated equilibrium, as claimed.

**5. Least-period bound and complete equality classification.** For a nonconstant least-period-\(T\) solution, \(v=\dot x\) is nonzero and has zero time mean. The periodic Wirtinger inequality and the first identity in (1) give
\[
\left(\frac{2\pi}{T}\right)^2\int_0^T v^2dt
\le\int_0^T w^2dt=\int_0^T v^2dt,
\]
so \(T\ge2\pi\). Equality forces \(v\) to be a pure first Fourier harmonic and hence \(x(t)=c+r\cos(t+\phi)\) with \(r>0\) and \(T=2\pi\). Substitution into the original equation yields
\[
|c+r\cos(t+\phi)|+Ar\cos(t+\phi)=1
\quad\text{for all }t.
\]
If the interval \([c-r,c+r]\) crosses zero in its interior, the absolute-value term has a corner while the other terms are affine in \(\cos(t+\phi)\), a contradiction. If it has fixed sign \(s\in\{-1,1\}\), coefficient comparison gives \(c=s\), \(A=-s\), and \(r\le1\). Conversely both displayed critical circle families solve the equation, giving least period \(2\pi\). Equality and strictness are therefore completely characterized.

## Verification

Running `python -m pip install -r requirements.txt` followed by `python verify_symbolic.py` prints a PASS line after checking both polynomial branches of \(\dot G\), \(\dot H\), \(\dot L\), both critical characteristic factorizations, and the critical circles by exact symbolic substitution. The measure-level conclusions and the period inequality use the explicit arguments above; finite symbolic checks are not substitutes for those arguments.

## Relationship to prior work

Linz and Sprott (1999) introduced the exact modulus jerk, identified its equilibria, and observed a pair of imaginary eigenvalues at \(A=1\), describing a Hopf transition. Their analysis includes exact piecewise-linear solution matching, but does not give the above complete invariant-measure classification or the exhaustive least-period equality case. Sprott and Linz (2000) survey its chaotic parameter regions and analytic segment construction, not the critical stationary simplex.

A later general third-order-feedback identity already implies the **smooth-feedback** counterpart of the weighted-slope balance used in (1). Its specializable stationary derivative-energy law is prior mathematics; no novelty is claimed for that multiplier mechanism or for the abstract Wirtinger inequality. The distinguishing conclusion here is the model-specific *global exhaustion of all critical compact invariant measures and selection of a single omega-limit cycle for every bounded critical forward trajectory*, including the precise maximal switching-touching radius and the outer-regime convergence classification. The universal period floor and its affine equality criterion are elementary consequences of the existing derivative-energy balance and periodic Wirtinger. They are supplied here as transparent supporting context with the exact equality loci in this model, not asserted as an independently new period principle.

The original source's general discussion of negative damping describes generic unbounded behavior. The exact neutral circles at \(A=-1\) show why volume expansion alone is not a statement that every non-equilibrium orbit must diverge: these exceptional periodic solutions have no open attracting basin.

## Limitations

This theorem classifies compact stationary states for \(|A|\ge1\), not all compact stationary states in the open interval \(-1<A<1\); equation (1) gives necessary constraints inside that interval but does not prove existence or uniqueness of cycles or chaotic attractors there. It does not classify nonrecurrent bounded complete connections at the endpoints or assert that every initial condition has a bounded orbit at \(|A|=1\). The omega-limit theorem proves orbit-set convergence for bounded forward trajectories, not asymptotic phase convergence or cycle stability. A closely related 2000 paper on no-chaos criteria for general jerk equations was located only at abstract level, so unseen equivalent critical classifications in that work remain a literature risk. The work has not received independent audit.

## References

1. S. J. Linz and J. C. Sprott, *Elementary chaotic flow*, Physics Letters A **259** (1999), 240–245, first published 16 August 1999, DOI: 10.1016/S0375-9601(99)00450-8. Open text: https://sprott.physics.wisc.edu/pubs/paper240.pdf.
2. J. C. Sprott and S. J. Linz, *Algebraically Simple Chaotic Flows*, International Journal of Chaos Theory and Applications **5** (2000), 3–22. Open text: https://sprott.physics.wisc.edu/pubs/paper250.pdf.
3. S. J. Linz, *No-chaos criteria for certain jerky dynamics*, Physics Letters A **275** (2000), 204–210, DOI: 10.1016/S0375-9601(00)00576-4. Abstract checked; full text not obtained.
4. *Global Hopf-slope balance for third-order feedback cycles and the Goodwin oscillator* (2026), published mathematical record: https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-goodwin-global-hopf-slope-balance--69bab068e3f7/RESULT.md. Its smooth-feedback stationary-slope law is acknowledged as prior mathematical coverage of the multiplier ingredient.
