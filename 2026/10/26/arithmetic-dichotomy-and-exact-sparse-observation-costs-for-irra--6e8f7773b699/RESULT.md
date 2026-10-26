# Arithmetic dichotomy and exact sparse-observation costs for irrational two-cut rotations

## Finding
Fix an irrational rotation angle \(\alpha\in(0,1)\), a cut parameter \(\lambda\in(0,1)\), and a nonnegative integer observation radius \(R\). Let \(X_{\alpha,\lambda}\) be the two-sided shift orbit closure of the binary sequences recording membership of \(\theta+n\alpha\) in \([0,\lambda)\). Define \(\beta_R\) as the minimum lower Banach density (infimum over all winning schedules) at central observation radius \(R\). The exact formula is

\[
\beta_R(X_{\alpha,\lambda})=
\begin{cases}
\dfrac{1}{2R+1},&\lambda\not\equiv k\alpha\pmod1\quad\text{for every }k\in\mathbb Z,\\[5pt]
\kappa\!\bigl([-R,R]\cup[q-R,q+R]\bigr),&\lambda\equiv k\alpha\pmod1\quad(k\ne0),\ q=|k|.
\end{cases}
\]

Here \(\kappa(F)\) is the least lower Banach density of an integer set meeting every translate of a nonempty finite pattern \(F\subset\mathbb Z\). In both cases an optimal periodic schedule exists. The same-orbit value is rational and algorithmically computable from a finite directed graph. In particular,

\[
\beta_0=\begin{cases}1,&\text{the cut orbits are distinct},\\1/2,&\text{the cut orbits agree},\end{cases}
\qquad
\beta_R=\frac1{2R+q+1}\quad\text{if }q\le2R+1.
\]

One non-interval instance is \(q=5,R=1\), where the exact cost is \(2/11\). The conclusion is independent of the continued fraction expansion of \(\alpha\); the sole arithmetic distinction is whether the two discontinuity points share a rotation orbit, and in that event their separation \(q\).

## Assumptions and scope
Work on the circle \(\mathbb T=\mathbb R/\mathbb Z\). For each \(\theta\) avoiding the countable set of orbit images of either partition endpoint, set \(x_\theta(n)=1\) precisely if \(\theta+n\alpha\in[0,\lambda)\). Define \(X_{\alpha,\lambda}\) as the closure in \(\{0,1\}^{\mathbb Z}\) of these codings. Including any of the natural one-sided coding conventions gives the same closure. A schedule \(A\subset\mathbb Z\) observes the window \(n+[-R,R]\) at time \(n\in A\); it wins when the projection of \(X_{\alpha,\lambda}\) onto \(A+[-R,R]\) is one-to-one. Its lower Banach density is

\[
\underline d_{\rm B}(A)=\lim_{N\to\infty}\inf_{t\in\mathbb Z}\frac{|A\cap[t,t+N-1]|}{N}.
\]

The limit exists by superadditivity of the minimum counting function. The covering cost \(\kappa(F)\) is the infimum of this density over all \(A\) such that \(A\cap(t+F)\ne\varnothing\) for every \(t\in\mathbb Z\). The endpoint orbit relation is independent of the choice of representative modulo one. Since \(\alpha\) is irrational, a nonzero integer \(k\) with \(\lambda\equiv k\alpha\pmod1\) is unique.

## Proof
**1. The rotation factor and the only exceptional fibers.** Because the orbit of \(\alpha\) is dense and \([0,\lambda)\) is a proper interval, distinct phases \(\theta\ne\eta\) yield distinct coding limits. More explicitly, the translate of the interval by the nonzero displacement \(\eta-\theta\) differs from the original on a nonempty open arc. Density of irrational rotations forces a coding difference at some time when neither phase is on an endpoint. Thus each symbolic point has a uniquely determined rotation phase; the continuous factor map is obtained by taking limits of phases of approximating regular codings. For a fixed phase avoiding the endpoint orbits the symbolic fiber is a singleton. At any phase on an endpoint orbit there are exactly two one-sided limiting codings, obtained by approaching from the two sides of the circle. These sequences disagree precisely at those integer coordinates at which the phase orbit meets a partition boundary. The two boundary orbits are disjoint exactly when \(\lambda\not\equiv k\alpha\pmod1\) for all integers \(k\). In that case each exceptional pair disagrees at one coordinate. If the orbits coincide, the two exceptional sequences disagree at exactly two coordinates separated by \(q=|k|\). All translates of the corresponding one- or two-point pattern occur as finite-disagreement pairs.

**2. Necessary covering.** If two symbolic points differ exactly on a coordinate set \(D\), then a radius-\(R\) observation at time \(n\) detects them if and only if \(n\in D+[-R,R]\). Since the system is shift invariant, a winning schedule must hit every translate of the witness pattern. With disjoint boundary orbits the witness pattern is just \([-R,R]\), hence every coordinate must lie within radius \(R\) of some observation; equivalently \(A+[-R,R]=\mathbb Z\). In the same-orbit case it must hit every translate of \([-R,R]\cup[q-R,q+R]\). This proves the lower bounds by the corresponding covering costs.

**3. Sufficiency of periodic covering.** If \(A\) is a nonempty periodic schedule meeting the required pattern translates, it separates every pair in a common phase fiber by the description in step 1. Now suppose \(x,y\) have distinct phases \(\theta\ne\eta\). Choose any residue \(r\in A\pmod p\), where \(p\ge1\) is a period of \(A\). Along the observed coordinates \(r+mp\), the phase \(\theta+(r+mp)\alpha\) is dense in the circle because \(p\alpha\) is irrational. The membership indicators of \([0,\lambda)\) for phases \(\theta\) and \(\eta\) differ throughout a nonempty open subinterval, so a coordinate of the progression detects \(x\ne y\) away from every partition endpoint. It is an observed coordinate because every time in the progression belongs to \(A\). Thus every nonempty periodic covering schedule is winning. The same argument treats the disjoint-boundary case. Consequently, once optimal periodic coverings are produced, the necessary lower bounds are equalities.

**4. Exact finite algorithm.** In the coincident-orbit case, translate the pattern to \(F'=[0,2R]\cup[q,q+2R]\). Put \(D=q+2R\). Construct a directed graph with binary words \(w\in\{0,1\}^{D}\) as vertices. From \(w\) an edge appending \(b\in\{0,1\}\) is allowed exactly when at least one of the positions in \(F'\) in the resulting length-\(D+1\) word is \(1\); its terminal state is the length-\(D\) suffix, and its weight is \(b\). Every bi-infinite graph path is the indicator of a covering schedule, and conversely. Let \(\mu\) be the minimum mean edge weight over all directed cycles. Every sufficiently long directed path can be decomposed into cycles plus at most \(2^D-1\) leftover edges; all edge weights are nonnegative. The minimum mean cycle therefore bounds every path's lower asymptotic one-density by \(\mu\), while repetition of a minimizing cycle realizes \(\mu\). Hence \(\kappa(F')=\mu\), a rational number achieved by a periodic schedule. A minimum-mean-cycle algorithm computes it in finite time, and a minimizing simple cycle has length at most \(2^D\). This gives an exact algorithm for all cut distances and radii.

**5. Special values and sharp example.** If \(q\le2R+1\), the two closed integer intervals constituting \(F'\) meet or are consecutive, so \(F'=[0,2R+q]\). A covering schedule needs at least one mark per \(2R+q+1\) coordinates, and the corresponding equally spaced schedule attains that density. At radius zero, \(F'=\{0,q\}\). Every pair of sites at spacing \(q\) must contain a mark, so summing these inequalities over any long interval gives density at least \(1/2\); the period-\(2q\) pattern consisting of \(q\) consecutive ones followed by \(q\) zeros realizes \(1/2\). For \(q=5,R=1\), the period-11 word \(10010000000\) meets every translate of \([0,2]\cup[5,7]\), giving density \(2/11\). For the reverse bound, the 128-state graph of step 4 has 252 allowed edges, and its integer edge costs \(11b-2\) have no negative directed cycle. The included standalone verifier constructs all edges and confirms that exact integer inequality through simultaneous Bellman–Ford relaxations. Therefore every cycle has mean weight at least \(2/11\), proving equality.

## Verification
The standalone, dependency-free Python verifier `verification_rotation.py` constructs the finite covering graph directly from its definition. It confirms the exact rational lower certificate for \(q=5,R=1\) by absence of negative directed cycles for edge cost \(11b-2\), and checks an explicit period-11 matching upper construction. It also verifies the consecutive-window cases and \(R=0\) cases across multiple finite distances. These finite verifications are exact integer computations. The all-irrational-angle statements and the lower/upper equivalence follow from the mathematical arguments above; finite experiments are not substituted for those infinite statements.

## Relationship to prior work
L. Ferrari, *Observer–hider games for expansive dynamical systems* (early online June 29, 2026), introduces the Banach-density observation cost, finite witness-pattern covering obstruction, and exact full-shift examples. The graph cycle-covering apparatus used here is closely related to its finite-pattern framework. The contribution here is the matching global upper bound for **all** irrational two-cut rotational codings, which are generally not shifts of finite type, and the sharp arithmetic dichotomy between one and two boundary orbits. The accessible introduction of Ferrari's article describes full shifts, the golden mean shift, and general SFT graph criteria, but no such irrational-rotation classification. Work on Sturmian words and indistinguishable asymptotic pairs (Peltomäki; Barbieri–Labbé–Starosta) treats the coding and exceptional-pair structure, rather than these optimal observation-density values. The full Ferrari article could not be inspected, so precedence beyond its accessible introduction is an explicit bibliographic limitation.

## Limitations
The result concerns two-sided **binary single-interval** codings of irrational circle rotations with the standard central symbolic observation metric, not arbitrary multi-interval partitions, arbitrary observation sensors, or rotations of rational angle. It asserts the minimum over all schedules; classification of *every* winning aperiodic schedule is not needed. The finite graph computes exact costs but grows exponentially with \(q+2R\). Historical priority cannot be guaranteed from search results or abstracts; the inaccessible full text of the motivating article remains a concrete limitation. No independent audit was performed.

## References
1. L. Ferrari, *Observer–hider games for expansive dynamical systems*, Journal of Dynamics and Games, early online June 29, 2026, DOI: 10.3934/jdg.2026045, https://doi.org/10.3934/jdg.2026045.
2. J. Peltomäki, *Abelian periods of factors of Sturmian words*, Journal of Number Theory **214** (2020), 251–285, DOI: 10.1016/j.jnt.2020.04.007. The section on coding of irrational rotations supplies standard Sturmian endpoint conventions.
3. S. Barbieri, S. Labbé, Š. Starosta, *A characterization of Sturmian sequences by indistinguishable asymptotic pairs*, European Journal of Combinatorics (2021), arXiv:2011.08112, DOI: 10.1016/j.ejc.2021.103318.
