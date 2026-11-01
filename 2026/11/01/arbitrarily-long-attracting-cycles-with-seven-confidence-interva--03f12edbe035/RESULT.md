# Arbitrarily long attracting cycles with seven confidence intervals and three opinion agents

## Finding

**Theorem (unbounded attracting periods at fixed complexity).** For every integer \(p\geq 2\), there exists a synchronous scalar set-based confidence opinion dynamics (SCOD) system consisting of precisely three agents, two with distinct, permanently fixed opinions and one ordinary averaging agent, whose **common** compact, symmetric confidence set has \(0\) in its interior and at most seven connected components, such that the ordinary agent has an exponentially attracting periodic orbit of **least period exactly \(p\)**. The three-agent bound is minimal for nonconstant periodic trajectories in scalar SCOD with symmetric confidence sets and any designated stubborn agents. In particular, neither three agents nor seven intervals impose any finite upper bound on the least period of an attracting orbit.

More precisely, two stubborn opinions are fixed at \(0\) and \(1\). For \(p\ge3\), the construction uses exactly seven disjoint closed intervals; for \(p=2\), exactly three. The orbit has return multiplier \(2^{-p}\), and an explicitly described nonempty open interval is in its basin of attraction.

## Assumptions and scope

Time \(t\in\mathbb Z_{\ge0}\) is synchronous. The two stubborn agents keep opinions \(0\) and \(1\) at every time. The only ordinary agent has real opinion \(x(t)\). All agents are assigned the same confidence set \(\mathcal O_p\subset\mathbb R\), with \(\mathcal O_p=-\mathcal O_p\). An ordinary agent includes itself and precisely the agents with opinion difference in \(\mathcal O_p\), and replaces its own opinion by the arithmetic mean of those trusted opinions; stubborn agents remain fixed. Self-confidence follows from \(0\in\mathcal O_p\).

When only the stubborn opinion \(0\) is trusted, the ordinary agent updates by \(L(x)=x/2\); when only the stubborn opinion \(1\) is trusted, it updates by \(R(x)=(x+1)/2\). No claim is made that these formulas hold away from the indicated neighborhoods, or that every initial condition reaches the constructed orbit.

Fix \(p\ge2\) and define
\[
Q=2^p-1,\quad c=\frac1{4Q},\quad x_0=\frac1Q,\quad x_j=\frac{2^{p-j}}Q\quad(1\le j\le p-1).
\]
Define a set of nonnegative discrepancies \(P_p\) to consist of \([0,c]\) and the following intervals:
\[
I_2=\left[\frac{2^{p-1}}Q-c,\frac{2^{p-1}}Q+c\right],\quad
I_3=\left[\frac{Q-1}Q-c,\frac{Q-1}Q+c\right].
\]
For \(p\ge3\), additionally include the **continuous interval**
\[
I_1=\left[\frac2Q-c,\frac{2^{p-2}}Q+c\right].
\]
For \(p=2\), omit \(I_1\); then \(I_2=I_3\). Finally put \(\mathcal O_p=P_p\cup(-P_p)\). Thus \(\mathcal O_p\) is compact and symmetric with a neighborhood \([-c,c]\) of zero. The definition uses a fixed number of intervals as \(p\) grows, although their endpoints depend on \(p\).

## Proof

**1. Exact itinerary.** Write \(Q=2^p-1\). For \(p\ge3\), the positive set \(P_p\) consists of the central component plus \(I_1,I_2,I_3\). These intervals are disjoint: their centers or nearest endpoints have unscaled gaps of at least \(1\), whereas each endpoint padding is only \(cQ=1/4\). The analogous claim for \(p=2\) follows by merging \(I_2=I_3\). Hence the full symmetric set has seven components for \(p\ge3\) and three for \(p=2\).

At \(x_0=1/Q\), the distance to stubborn opinion \(1\) is \((Q-1)/Q\in I_3\), whereas the distance to stubborn opinion \(0\), namely \(1/Q\), lies outside \(P_p\). For \(1\le j\le p-1\), the numerator \(Qx_j=2^{p-j}\) is one of \(2,4,\ldots,2^{p-2}\) (hence inside \(I_1\)) or \(2^{p-1}\) (inside \(I_2\)); thus opinion \(0\) is trusted.

The distance from \(x_j\) to stubborn opinion \(1\) has numerator \(Q-2^{p-j}\). For \(p\ge3\), these numerators lie between \(2^{p-1}-1\) and \(Q-2\), so are above the top of \(I_1\) by at least one integer unit; they are not in \(I_2\), whose center \(2^{p-1}\) differs by at least one unit, nor in \(I_3\), centered at \(Q-1\), again by at least one unit. They are not in \([0,c]\). At \(p=2\), the sole excluded distance is \(1/3\), whereas the trusted distance is \(2/3\), with the same separation. Thus \(1\) is never trusted at \(x_j\) for \(j\ge1\).

Every included distance is at least \(c\) from the relevant confidence-boundary (for the long \(I_1\), its endpoints have padding \(c\)); every excluded distance is at least \(3c\) from the whole confidence set. This is because all orbit and stubborn differences have numerator integral in units of \(1/Q\), while every interval endpoint is displaced by exactly \(1/(4Q)\) from an integral numerator. Consequently the same trust pattern holds whenever the ordinary opinion is within \(c/2\) of the corresponding orbit point.

It follows that the orbit has the exact transitions
\[
x_0\stackrel{R}\longmapsto x_1\stackrel{L}\longmapsto x_2\stackrel{L}\longmapsto\cdots\stackrel{L}\longmapsto x_{p-1}\stackrel{L}\longmapsto x_0.
\]
Indeed \(R(1/Q)=(Q+1)/(2Q)=2^{p-1}/Q\), and \(L(x_j)=x_{j+1}\) until the final halving \(L(2/Q)=1/Q\). Every orbit value is distinct (its numerator is one of \(1,2,4,\dots,2^{p-1}\)), so its least period is exactly \(p\).

**2. Open-basin attraction.** Take any initial opinion \(y_0\) with \(\lvert y_0-x_0\rvert<c/2\). By induction, the same unique stubborn agent is trusted at every step as on the orbit. The difference from the reference state at time \(t\) obeys the exact identity
\[
y_t-x_{t\bmod p}=2^{-t}(y_0-x_0).
\]
Its absolute magnitude is always smaller than \(c/2\), closing the induction. The basin therefore contains the open interval \((x_0-c/2,x_0+c/2)\); the period return map has slope \(2^{-p}\). This is genuine asymptotic attraction to an orbit, not merely a single exactly periodic initial condition.

**3. Minimality of three agents.** With a single agent every opinion is fixed, whether or not it is stubborn. With two regular agents and a symmetric confidence set, trust is reciprocal: either neither trusts the other (both opinions fixed), or both trust one another and average to consensus in one update (then fixed). With one regular and one stubborn agent of opinion \(a\), either the ordinary agent ignores the stubborn agent and remains fixed forever, or it averages with \(a\), in which case its distance to \(a\) strictly halves. A nonconstant periodic orbit is impossible because such a cycle would require the distance to \(a\) to return after at least one strict decrease and no increase. With two stubborn agents the state is fixed. Hence fewer than three agents never yield a nonconstant periodic trajectory.

## Verification

The standalone `verify.py` uses exact rational arithmetic (Python standard-library `fractions.Fraction`). It reconstructs \(\mathcal O_p\), tests the inclusion/exclusion pattern and every orbit transition for \(2\le p\le120\), then tests four perturbations inside the asserted attracting neighborhood over four full periods each. It also checks the absence of repeated reference orbit values. These finite checks independently exercise the explicit formulas but are **not** used as a substitute for the proof of the all-integer theorem.

Run: `python3 verify.py`. The expected first line is `PASS: exact rational itinerary and open-basin checks for periods 2..120`.

## Relationship to prior work

Zabarianska and Proskurnikov introduced SCOD and demonstrated a period-three orbit with three agents and two stubborn opinions for a symmetric nonconvex confidence set (their Example 4, arXiv:2408.01753v1, Section II-B). Their principal convergence theorem assumes *homogeneous stubborn opinions*; that theorem does not cover the present two distinct fixed opinions. The new statement is an **all-period construction with an explicit uniform bound of seven confidence intervals and a robust attracting neighborhood**, not the previously reported existence of some oscillations. In scalar HK dynamics with a confidence interval rather than a disconnected confidence set, the relevant finite-termination statements are inapplicable to the constructed sets.

Gaivão and Nogueira's analysis of piecewise increasing contractions (arXiv:2007.08014) bounds the **number of periodic orbits** by the number of discontinuities plus one, not the least period of one orbit. Results on contracted rotations and piecewise affine maps illuminate the mechanism, but do not by themselves supply its realization by reciprocal trust decisions and fixed agents in SCOD. The construction here verifies that extra geometry directly.

## Limitations

The confidence set depends on the requested period; the theorem does not establish unbounded coexistence of distinct periods for one fixed confidence set, nor global attraction from all initial opinions. The model is deterministic, scalar, synchronous and allows a disconnected symmetric confidence set and two different fixed external opinions. It does not assert that analogous cycles exist with convex confidence sets or in models without stubborn agents. Specialized or unindexed prior results may give alternative formulations of its constructive mechanism.

## References

1. I. Zabarianska and A. V. Proskurnikov, *Opinion Dynamics with Set-Based Confidence: Convergence Criteria and Periodic Solutions*, first public arXiv:2408.01753v1, 2024-08-03, https://arxiv.org/abs/2408.01753 (especially Section II-B, Example 4, and Section III, Theorem 1).
2. J. P. Gaivão and A. Nogueira, *Dynamics of piecewise increasing contractions*, arXiv:2007.08014v1, 2020-07-15, https://arxiv.org/abs/2007.08014 (Theorem 1 and introduction).
3. M. A. Bernardo, C. Altafini, A. V. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, https://doi.org/10.1016/j.automatica.2023.111302.
