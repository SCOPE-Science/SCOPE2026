# A sharp weather-reliability threshold for three transit-observation windows

## Finding
Suppose a strictly periodic astronomical transit has known period \(P>0\) and an unknown, uniformly distributed orbital phase. Three nonoverlapping-in-time observing sessions, scheduled in distinct orbital cycles, each have length \(L\in(0,P)\), so each can contain at most one transit center. The sessions may have arbitrarily chosen residues modulo \(P\). Independently for each session containing a center, the observation succeeds with probability \(d\in(0,1]\). A successful survey requires observations of **at least two different transits**. Define \(e=L/P\).

For a phase-clustered design (all three sessions have the same residue), the success probability is
\[
C(e,d)=d^2(3-2d)e.
\]
For an evenly phased design (session residues separated by \(P/3\)), the success probability is
\[
D(e,d)=\begin{cases}
0,&0<e\le1/3,\\
d^2(3e-1),&1/3\le e\le2/3,\\
d^2\bigl(1+2(1-d)(3e-2)\bigr),&2/3\le e<1.
\end{cases}
\]
Precisely, the global maximum over all three session residues equals \(C(e,d)\) when \(d\le3/4\), or when \(d>3/4\) and \(e\le1/(2d)\). When \(d>3/4\) and \(e\ge1/(2d)\), it equals the appropriate last two lines of \(D(e,d)\). Equalities at the boundaries indicate ties. At \(d=3/4\), the clustered and evenly phased designs tie for every \(e\ge2/3\); below that length the clustered design is better. At \(d>3/4\) and \(e=1/(2d)\), the two designs tie. Thus a spreading transition is possible **exactly when \(d>3/4\)**, at the sharp session-length ratio \(e=1/(2d)\).

## Assumptions and scope
Transit centers occur at \(\phi+kP\) for all integer \(k\), with \(\phi\) uniformly distributed on \([0,P)\). The three sessions lie in disjoint orbital cycles so that observations never count the same transit twice; each lasts strictly less than a period. Their residues on the phase circle are unconstrained. If a center is inside a session, a Bernoulli success with common probability \(d\) occurs, independently across sessions conditional on the phase. Endpoint coincidences have probability zero. Timing is exact, the period is known, no transit timing variations occur, and the event-center detection approximation omits finite transit duration and signal-to-noise accumulation. This is a conditional window-function result, not a geometric probability that a planet transits.

## Proof
Normalize \(P=1\) and write \(\ell=e\). Each session corresponds to a circular arc \(A_i\) of length \(\ell\) of phase values that produce a transit center inside that session. Put \(m(x)=\sum_{i=1}^3\mathbf1_{A_i}(x)\), let \(w\) be the measure of phases with \(m\ge2\), and \(t\) the measure with \(m=3\). Conditional success is zero if \(m<2\), \(d^2\) if \(m=2\), and \(3d^2-2d^3\) if \(m=3\). Therefore the probability divided by \(d^2\) is
\[
J=w+2(1-d)t.\tag{1}
\]
If the union of the three arcs is not the whole circle, cut at an uncovered phase. We obtain three ordinary intervals of length \(\ell\), ordered by left endpoints. Every point in at least two intervals lies in the middle interval: to the left of it at most the earliest interval can occur, and to its right at most the latest. Hence \(w\le\ell\), and also \(t\le\ell\). Equation (1) implies \(J\le(3-2d)\ell\). Equality is achieved by three coincident phase arcs, with independent observations in different orbital cycles.

Now suppose the union covers the whole circle. Counting arc multiplicities gives \(3\ell=1+w+t\), hence
\[
J=3\ell-1+(1-2d)t.\tag{2}
\]
Since multiplicity is at most two off the triple intersection, \(t\ge\max(0,3\ell-2)\). We also have \(t\le\max(0,2\ell-1)\). To verify the latter, consider the complementary arcs \(B_i=A_i^c\), each length \(1-\ell\), whose **triple** intersection is empty. If their union is the full circle, its measure is \(1\). Otherwise cut at an uncovered point of that union; the three complements become line intervals. Ordering their left endpoints, empty triple intersection makes the first and last intervals disjoint up to endpoints, so their union has length at least \(2(1-\ell)\). Thus the union of the complements has length at least \(\min\{1,2(1-\ell)\}\), proving the stated upper bound for \(t=1-|\bigcup B_i|\).

If \(d\le1/2\), equation (2) and the upper bound on \(t\) imply \(J\le(3-2d)\ell\). For \(\ell\le1/2\), this follows instead directly from \(t=0\) and \(3\ell-1\le\ell\); for \(\ell>1/2\), subtracting \((3-2d)\ell\) from the upper bound gives \(2(1-d)(\ell-1)<0\). If \(d\ge1/2\), equation (2) is maximized at the **lower** bound \(t=\max(0,3\ell-2)\). That bound is achieved by the three equally spaced arcs whenever they cover the circle, namely \(\ell\ge1/3\). For \(\ell\le1/2\), their bound cannot beat the clustered design. On \(1/2\le\ell\le2/3\), compare \(J_{\rm spread}=3\ell-1\) to \(J_{\rm cluster}=(3-2d)\ell\); the former wins precisely when \(2d\ell>1\). For \(2/3\le\ell<1\), the spread design has \(w=1\), \(t=3\ell-2\), and
\[
J_{\rm spread}-J_{\rm cluster}=(4d-3)(1-\ell).
\]
These comparisons prove every claimed branch, sharp boundary and attaining schedule. Rescale by \(P\).

## Verification
The accompanying `checker.py` computes circular-arc overlaps at exact rational endpoints, enumerates independent-success probabilities, and checks the asserted optimum across 35 combinations of rational duration/reliability values and 441 discrete phase-offset pairs apiece. It passed 15,540 exact rational assertions. Finite grids corroborate the proof but cannot establish an all-real optimization theorem; the argument above supplies that proof.

## Relationship to prior work
Von Braun and Ciardi (2007, arXiv:0711.4256) model transit survey window functions, white/red noise and observing strategies. Von Braun, Kane and Ciardi (2009, arXiv:0907.1614), especially Section 3.5, explicitly require two sampled transits in some survey calculations and explore sensitivity to observing cadence and night length numerically. The present result differs by optimizing all three independent session residues exactly, with a separate independent weather-success probability, and yields a reliability transition at \(d=3/4\). Existing circle multi-coverage work, including Holst's 1980 random-arc study, addresses related overlap geometry but does not establish this particular deterministic reliability-weighted scheduling classification in the material reviewed. No priority guarantee is asserted; a broader known circular-arc extremal theorem may imply the formula.

## Limitations
The theorem is for three sessions only, fixed equal lengths, exactly periodic transit centers, independently successful visits and unrestricted phase choices; atmospheric losses in real telescope data may be correlated, and other objectives such as recovering an unknown period require different designs. The global optimum does not imply noise-optimal transit detection or realistic ephemeris recovery. At two observed transits, cycle-count aliasing can remain unresolved. The proof treats point centers, not exposure-dependent signal-to-noise or partial-transit visibility.

## References
1. K. von Braun and D. R. Ciardi, *Observational Window Functions in Planet Transit Searches*, arXiv:0711.4256, initial public submission 2007-11-27, https://arxiv.org/abs/0711.4256.
2. K. von Braun, S. R. Kane and D. R. Ciardi, *Observational Window Functions in Planet Transit Surveys*, arXiv:0907.1614, initial public submission 2009-07-09, https://arxiv.org/abs/0907.1614.
3. L. Holst, *On Multiple Covering of a Circle with Random Arcs*, Journal of Applied Probability 17 (1980), 284–290, https://doi.org/10.2307/3212948.
