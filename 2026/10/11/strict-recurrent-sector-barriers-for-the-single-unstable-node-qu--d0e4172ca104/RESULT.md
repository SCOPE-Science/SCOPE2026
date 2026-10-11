# Strict recurrent-sector barriers for the single-unstable-node quadratic flow

## Finding
Let \(a\in\mathbb R\) and \(b>0\), and consider the quadratic system
\[
\dot x=y,\qquad \dot y=-x+yz,\qquad \dot z=z+a x^2-y^2-b.\tag{1}
\]
Its unique equilibrium is \(e=(0,0,b)\). Every bounded solution defined for all \(t\geq0\) other than the stationary equilibrium obeys
\[
\liminf_{t\to\infty} z(t)<0,\qquad
\limsup_{t\to\infty}\bigl(a x(t)^2-y(t)^2\bigr)>b.\tag{2}
\]
Consequently such a solution requires \(a>0\) and
\(\limsup_{t\to\infty}|x(t)|>\sqrt{b/a}\). For \(a\leq0\), the equilibrium is the **only** bounded forward solution, the only nonempty compact two-sided invariant set is \(\{e\}\), and the only compactly supported invariant probability measure is \(\delta_e\).

## Assumptions and scope
Parameters are real with \(b>0\); no condition on \(a\) is implicit. A bounded forward solution means a classical trajectory of (1) defined for every \(t\geq0\), with relatively compact range in \(\mathbb R^3\). Such solutions have compact, nonempty \(\omega\)-limit sets consisting of complete bounded trajectories. A compact invariant set means invariance under the two-sided flow restricted to that set. No assertion is made about existence of bounded orbits in the region \(a>0\) or about the rate at which other solutions escape.

## Proof
**Exact energy and unstable-filter identities.** Put \(E=(x^2+y^2)/2\) and \(Q=b+y^2-a x^2\). Direct differentiation of (1) gives
\[
\dot E=y^2z,\qquad \dot z=z-Q.\tag{3}
\]
On a bounded forward orbit, solve the scalar second equation between \(t\) and \(t+s\), multiply by \(e^{-s}\), and let \(s\to\infty\). Since \(z(t+s)\) is bounded,
\[
z(t)=\int_0^\infty e^{-s}Q(t+s)\,ds.\tag{4}
\]

**Rigidity of an eventually nonnegative height.** Suppose a bounded forward solution has \(z(t)\geq0\) for every \(t\geq T\). Equation (3) makes \(E\) nondecreasing there and bounded, hence \(E\to E_\infty\). On its compact invariant \(\omega\)-limit set, \(E\equiv E_\infty\), so \(y^2z=0\) along every complete trajectory lying in that set. Such a trajectory cannot have \(y\ne0\) on any open time interval: if it did, \(z=0\) throughout that interval, where (1) would give \(\dot x=y\), \(\dot y=-x\) and \(a x^2-y^2-b=0\). Differentiating the last identity forces \(2(a+1)xy=0\). If \(a=-1\), the identity reads \(-x^2-y^2-b=0\), impossible because \(b>0\). If \(a\ne-1\), one has \(x=0\) throughout the interval since \(y\ne0\), contradicting \(\dot x=y\). Thus \(y\equiv0\), and \(\dot y=-x\) implies \(x\equiv0\). Then \(\dot z=z-b\); boundedness for both positive and negative times forces \(z\equiv b\). Accordingly the whole \(\omega\)-limit set equals \(\{e\}\), so \(E_\infty=0\). As \(E\geq0\) and is nondecreasing on the tail, \(E\equiv0\) there. The solution has \(x=y=0\), and bounded forward continuation of \(\dot z=z-b\) makes \(z=b\) there. Uniqueness makes the original solution stationary. Therefore **every bounded forward nonstationary orbit has \(z(t)<0\) arbitrarily late**. 

**Necessity of nonlinear pumping.** If the same solution had \(a x(t)^2-y(t)^2\leq b\) throughout a tail, then \(Q\geq0\) on that tail and equation (4) would imply \(z\geq0\) there, contrary to the preceding paragraph. Hence \(a x(t)^2-y(t)^2>b\) also occurs arbitrarily late.

**Strict asymptotic gaps.** Let \(\omega\) be the compact \(\omega\)-limit set of a bounded nonstationary orbit. It cannot be \(\{e\}\): that would imply \(z(t)\to b>0\), contradicting the arbitrarily late visits to \(z<0\). Choose a non-equilibrium point of \(\omega\). Its complete orbit in \(\omega\) is bounded, and the preceding two paragraphs applied to that orbit produce one point of \(\omega\) having \(z<0\) and (possibly another) point having \(a x^2-y^2>b\). Every point of \(\omega\) is approached by the original solution along times tending to infinity. Thus the strict limits in (2) follow. If \(a\leq0\), the second strict inequality is impossible, proving the no-bounded-forward-orbit assertion. If \(a>0\), it implies \(a x(t)^2>b\) at some \(\omega\)-limit point, proving the asserted strict amplitude lower bound. Every orbit in a compact invariant set is bounded forward, so when \(a\leq0\) that set is \(\{e\}\); any invariant probability supported on a compact set must then be \(\delta_e\). This completes the proof.

## Verification
A standalone symbolic checker (`verify.py`) uses SymPy to recompute both identities (3), the equilibrium linearization, and the algebraic derivative on a putative interval with \(z=0\) and \(y\ne0\). Run `python verify.py` in an environment with Python 3 and SymPy. The passage from identities to the infinite-time claims above is analytic, not an inference from numerical experiments. The source ODE is equation (9) of Sprott et al. [1].

## Relationship to prior work
Sprott, Jafari, Pham and Hosseini [1] introduced (1) and mapped extremely small, mostly positive-\(a\) regions of bounded behavior through parameter scans, with a local equilibrium analysis and numeric examples of chaos, periodic orbits and tori. The present result instead proves a global obstruction for **every** bounded forward orbit throughout \(a\leq0\) and two strict necessary sectors for **every** nonstationary bounded forward orbit at arbitrary \(a\). Their volume-contraction observation, which concerns an attracting regime's *average* height, does not itself supply this all-orbit statement or the nonlinear-pumping sector. Chen et al. [2] study equilibrium types, compactification at infinity and small periodic solutions for a related quadratic flow, not an identified theorem implying (2). Their mathematical displays did not all survive the available HTML extraction, so an unrecognized stronger comparison remains a residual literature risk.

## Limitations
The theorem is one-sided: the necessary condition \(a>0\) does not show that any nonstationary bounded orbit exists at a given positive \(a\). Unbounded forward behavior is not identified with finite-time escape; the proof requires only ordinary continuation of bounded ODE solutions. The strict constants in (2) may depend on the orbit. The literature comparison is not a guarantee of worldwide priority, and no independent audit has been performed.

## References
1. J. C. Sprott, S. Jafari, V.-T. Pham and Z. S. Hosseini, “A chaotic system with a single unstable node,” *Physics Letters A* **379** (2015), 2030–2036, DOI: `10.1016/j.physleta.2015.06.039`. Public author PDF: `https://sprott.physics.wisc.edu/pubs/paper430.pdf`; article first listed available online 2015-06-19.
2. M. Chen et al., “Dynamical Analysis and Periodic Solution of a Chaotic System with Coexisting Attractors,” *Complexity* (2021), article 9948488, DOI: `10.1155/2021/9948488`.
