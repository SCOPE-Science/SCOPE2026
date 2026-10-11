# Cone-crossing rigidity in a reversible quadratic jerk flow

## Finding
For Sprott's quadratic time-reversible flow (equation (11) of the cited 2015 paper), the nonlinear height \(P=z+xy\) has an exact sign-definite/indefinite transition at \(a=-1\). For \(a\le -1\), every bounded forward orbit converges to the origin; for \(a>-1\), every **nonstationary bounded complete orbit** crosses both strict sectors of the quadratic cone \((a+1)x^2=y^2\). A height-conditioned equality holds for all compact invariant probability measures, not merely for individual periodic solutions.

More explicitly, let
\[
Q=(a+1)x^2-y^2,\qquad P=z+xy.
\]
Then every compactly supported invariant Borel probability measure \(\mu\) satisfies
\[
\mathbb{E}_{\mu}[y^2\mid P]=(a+1)\mathbb{E}_{\mu}[x^2\mid P]
\quad\text{almost surely}.\]
When \(a>-1\) and \(\mu\ne\delta_{(0,0,0)}\), both \(\mu(Q>0)\) and \(\mu(Q<0)\) are strictly positive. Any nonconstant periodic orbit crosses both open sectors, and its normalized time average satisfies
\[
\frac1T\int_0^T y(t)^2\,dt=(a+1)\frac1T\int_0^T x(t)^2\,dt.
\]

## Assumptions and scope
The autonomous polynomial differential equation is, for any fixed real \(a\),
\[
\dot x=z,\qquad \dot y=x,\qquad \dot z=ax^2-y^2-yz.
\]
A **forward-bounded solution** is a solution existing on \([0,\infty)\) whose image is bounded. For a polynomial vector field, any trajectory that remains bounded for its maximal forward lifetime extends indefinitely, thus no bounded maximal solution has a finite forward endpoint. A **bounded complete solution** exists for all \(t\in\mathbb R\) and has bounded image. A compact invariant set means nonempty and invariant under both time directions of the local flow, hence its trajectories are complete. Compactly supported invariant probabilities are invariant under this flow and supported on its complete compact phase-space dynamics. No assertion is made about trajectories escaping to infinity or about the existence of nonstationary recurrent solutions for \(a>-1\).

## Proof
**1. Polynomial coboundary.** Direct differentiation gives
\[
\frac d{dt}(z+xy)=ax^2-y^2-yz+yz+x^2
\]
where the last two terms are \(\dot x\,y+x\dot y=zy+x^2\), so the exact identity is
\[
\boxed{\dot P=(a+1)x^2-y^2=Q.}
\]
The origin is the only equilibrium, because \(\dot y=x=0\), \(\dot x=z=0\), and then \(\dot z=-y^2=0\).

**2. The cone has no nonstationary complete orbit.** For \(a>-1\), write \(s=\sqrt{a+1}>0\). Suppose a complete solution lies in \(Q=0\) for all time. On any open interval with \(x\ne0\), continuity forces \(y=\varepsilon sx\), with \(\varepsilon\in\{-1,1\}\). Differentiation of this equality and \(\dot y=x\) imply \(z=\varepsilon x/s\). Differentiation again yields \(\dot z=x/s^2\). The original equation on these substitutions instead gives \(\dot z=-2x^2\). Hence \(x/s^2=-2x^2\), implying \(x=-1/(2s^2)\) throughout this interval; but then \(\dot x=z=\varepsilon x/s\ne0\), a contradiction. Thus \(x\equiv0\), whence \(y\equiv z\equiv0\). When \(a\le-1\), the largest complete invariant subset of \(Q=0\) is likewise only the origin: if \(a<-1\), \(Q=0\) forces \(x=y=0\); if \(a=-1\), it forces \(y=0\), and invariance successively forces \(x=z=0\).

**3. Bounded-forward convergence when \(a\le-1\).** Here \(Q\le0\), so \(P\) is nonincreasing. Along a bounded forward solution, \(P\) is bounded below and converges. Its omega-limit set is nonempty, compact, invariant and lies in \(Q=0\): on the limit set, the limiting constant of \(P\) is fixed along every complete trajectory, so its derivative is zero. By step 2 the omega-limit set is the singleton origin. Therefore the original trajectory converges to the origin.

For any compact two-sided invariant set in this parameter range, the same monotone identity applied in both time directions, together with boundedness and uniform continuity of \(Q\), puts its alpha- and omega-limit sets in \(Q=0\), hence both are the origin. The limits of \(P\) in both directions are consequently zero. As \(P\) is nonincreasing, it must be identically zero; thus \(Q\equiv0\), and step 2 makes the entire orbit the origin. The only nonempty compact invariant set is therefore the origin. The same invariant-support argument makes its Dirac mass the sole compactly supported invariant probability measure.

**4. Both-sector crossing when \(a>-1\).** Suppose a nonstationary bounded complete orbit stays in \(Q\ge0\) for every time. Then \(P\) is nondecreasing and bounded on the entire real line. As the orbit is bounded, \(Q(t)\) is uniformly continuous (its derivative \(2(a+1)xz-2yx\) is bounded), and \(\int_{-\infty}^{\infty}Q(t)\,dt<\infty\). Thus \(Q(t)\to0\) at both ends of time. Both alpha- and omega-limit sets are compact invariant subsets of \(Q=0\), hence step 2 makes both the origin. Therefore \(P\to0\) as \(t\to\pm\infty\); monotonicity forces \(P\equiv0\), hence \(Q\equiv0\) and the orbit is stationary, contradiction. The same argument with \(-Q\) rules out staying in \(Q\le0\). Thus every nonstationary bounded complete orbit visits both \(Q>0\) and \(Q<0\).

**5. Conditional invariant-measure equality and strictness.** Let \(\mu\) be any compactly supported invariant probability measure. For each smooth function \(H:\mathbb R\to\mathbb R\), invariance and boundedness yield
\[
0=\int\frac{d}{dt}H(P)\,d\mu=\int H'(P)Q\,d\mu.
\]
Choosing smooth antiderivatives of arbitrary smooth test functions, and then using density of smooth tests on the compact range of \(P\), gives \(\mathbb E_\mu[Q\mid P]=0\) almost surely, which is precisely the stated conditional moment equality. For \(a>-1\), if such a \(\mu\) assigns zero mass to one strict sector, the integrated equality \(\int Q\,d\mu=0\) implies \(Q=0\) almost surely. Invariance means almost every entire orbit lies in \(Q=0\), and step 2 makes \(\mu=\delta_0\). Therefore any other invariant probability puts positive mass in both strict sectors. A nonconstant periodic orbit supports an invariant time measure different from \(\delta_0\), giving the crossing and time-average assertions.

## Verification
The included standalone `verify.py` differentiates \(P\) symbolically and substitutes the two possible cone branches, verifying the conflicting derivative conditions exactly. It also checks the equality of the polynomial forms of the stated critical identities for an unrestricted symbolic parameter. No finite numerical integration is used as evidence for the infinite-time assertions: the convergence, cone invariance and measure statements are proved above.

## Relationship to prior work
Sprott's 2015 paper introduces this exact system as Eq. (11), exhibits a numerical strange-attractor/repellor pair at \(a=1.3\), and reports a nilpotent origin and computed exponents. Its discussion does not state a global result over all \(a\le-1\), a two-sector crossing obstruction for bounded complete orbits, or a conditional stationary law along \(P\). Sprott's 2014 study of involutional symmetries considers other polynomial flows and their bifurcations; its statements do not imply these conditions for Eq. (11). General monotone-coboundary arguments in other differential equations motivate the approach but are not the same theorem for this vector field.

## Limitations
The vanishing-at-equilibrium assertion concerns **bounded** forward solutions, not every solution. The cone-crossing theorem requires two-sided completeness and boundedness, and does not classify all unbounded or one-sided bounded trajectories. At \(a>-1\), nontrivial compact invariant dynamics are not proved to exist, so the boundary is a rigorous exclusion/necessary-condition boundary, not an existence equivalence. Publication-priority comparison is limited to identified and accessible sources; unindexed equivalent arguments may exist. The stationary result is for compactly supported invariant probabilities, not arbitrary nonstationary ensemble distributions. Independent audit has not been performed.

## References
1. J. C. Sprott, *Symmetric Time-Reversible Flows with a Strange Attractor*, International Journal of Bifurcation and Chaos **25** (2015), 1550078, especially Eq. (11), page 5; DOI `10.1142/S0218127415500789`; openly accessible author manuscript: https://sprott.physics.wisc.edu/pubs/paper433.pdf.
2. J. C. Sprott, *Simplest Chaotic Flows with Involutional Symmetries*, International Journal of Bifurcation and Chaos **24** (2014), 1450009; DOI `10.1142/S0218127414500096`; openly accessible author manuscript: https://sprott.physics.wisc.edu/pubs/paper407.pdf.
