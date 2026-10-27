# Sharp three-bloc polarization threshold and turnout discontinuity in costly spatial voting

## Finding

**Theorem (complete pure-strategy classification).** Two candidates independently choose any policy \(x,y\in[0,1]\) to maximize their own *unnormalized expected number of votes*, not their probability of winning. A continuum of voters has ideal points \(0,1/2,1\) with respective masses \(e,1-2e,e\), where \(0<e<1/2\). Every voter has independent voting cost with cumulative distribution \(K(t)=t^q\) on \([0,1]\), where \(q\ge1\), and votes for the strictly closer candidate precisely when the distance advantage exceeds that cost. Define

\[
 e_*(q)=\frac1{1+2^q},\qquad
 \mathcal H=\{(0,1/2),(1/2,0),(1/2,1),(1,1/2)\},\qquad
 \mathcal E=\{(0,1),(1,0)\}.
\]

If \(q>1\), the **entire set** of pure Nash equilibria is \(\mathcal H\) when \(e<e_*(q)\), \(\mathcal H\cup\mathcal E\) when \(e=e_*(q)\), and \(\mathcal E\) when \(e>e_*(q)\). The same classification holds at \(q=1\) off the critical value \(e=1/3\). At \(q=1,e=1/3\), the entire equilibrium set instead is

\[
 \begin{split}
 \mathcal I={}&\{(0,z),(z,0):1/2\le z\le1\}\\
 &\cup\{(1,z),(z,1):0\le z\le1/2\}.
 \end{split}
\]

For \(e<e_*(q)\), equilibrium turnout is exactly \(T=2^{-q}\). For \(e>e_*(q)\), equilibrium turnout is \(T=2e\). The one-sided equilibrium turnout jump at the threshold is strictly positive and equals

\[
 J(q)=\frac{2}{1+2^q}-2^{-q}=\frac{2^q-1}{2^q(1+2^q)}>0.
\]

At \(q>1\), the two turnout values coexist at the critical parameter. At \(q=1,e=1/3\), the continuum realizes exactly \(T\in[1/2,2/3]\). Thus, for example, \(q=2\) and any \(1/5<e<1/4\) give extreme-platform equilibria \((0,1)\) and \((1,0)\) even though a strict majority \(1-2e>1/2\) of voters are centrists.

## Assumptions and scope

There are exactly two policy-seeking candidates, and every candidate's action set is the full continuum \([0,1]\). Each candidate maximizes her own expected *vote share of all eligible voters*. A voter at \(p\) finds policy \(z\) attractive according to \(-|p-z|\); the larger of the two candidates' attractiveness values beats the other by an advantage in \([0,1]\). Voting costs are independent with CDF \(K(t)=t^q\), \(q\ge1\), and are independent of voter location. In a distance tie, voting benefit is zero and the probability of casting a vote is zero. There is no candidate tie-breaking preference, electoral majority criterion, probabilistic winning payoff, or exogenous turnout.

The electorate distribution contains precisely three point masses, not a strictly positive voter-position density. All assertions are about pure-strategy Nash equilibria in this model; no conclusion is asserted for smooth heterogeneous electorates or strategic pivotal voting.

## Proof

**Payoff reduction.** For a candidate located at \(x\), against opponent \(y\), the expected vote share is

\[
 U(x;y)=e|x-y|^q+(1-2e)\big[|1/2-y|-|1/2-x|\big]_+^q,
 \quad [t]_+=\max\{t,0\}.
\]

Indeed, if \(x<y\) the left endpoint bloc votes for \(x\), each with distance advantage \(y-x\); if \(x>y\) the right endpoint bloc votes for \(x\), each with advantage \(x-y\). The center bloc votes for \(x\) only when \(x\) is closer to \(1/2\) than \(y\). Applying the cost CDF to these advantages yields the displayed identity.

**Finite-support best-response principle.** More generally, for any finite atomic voter support \(P\subset[0,1]\), and \(q\ge1\), a candidate's vote-share objective against a fixed opponent is convex on each interval between consecutive points of \(P\cup\{0,1\}\). This holds because on such an interval every term is a nonnegative multiple of \([a+bx]_+^q\) for suitable constants \(a,b\). Consequently some best response always occurs at an element of \(P\cup\{0,1\}\). In this symmetric three-bloc model when \(q>1\), the endpoint term \(e|x-y|^q\) is strictly convex on either \([0,1/2]\) or \([1/2,1]\), while the middle term is convex there. Hence every best response belongs to \(\{0,1/2,1\}\): an interior point of either half-interval has strictly less payoff than at least one endpoint.

**The strict-power cases.** Against opponent \(0\), the payoffs for actions \(0,1/2,1\) are

\[
 0,\qquad (1-e)2^{-q},\qquad e.
\]

Against opponent \(1/2\), both endpoints yield \(e2^{-q}>0\), while the middle yields zero; opponent \(1\) is symmetric to opponent \(0\). Two candidates never share the same position in equilibrium because each then obtains zero, whereas deviation to some other position yields strictly positive support. The table therefore leaves only \(\mathcal H\) and \(\mathcal E\). The halfway profiles are equilibria exactly when \((1-e)2^{-q}\ge e\), i.e. \(e\le1/(1+2^q)\). The extreme profiles are equilibria exactly when \(e\ge(1-e)2^{-q}\). This proves the three regimes for \(q>1\).

**The linear-power boundary.** Put \(q=1\), and by symmetry consider an opponent at \(y\in[0,1/2]\). At the anchor policies \(0,1/2,1\), our payoffs are respectively \(ey,(1-e)(1/2-y),e(1-y)\). If \(0<y<1/2\), the last is strictly larger than the first, and every best response is at \(1/2\) or \(1\). In fact, on each half-interval the objective is piecewise affine, and a flat interval cannot contain a global maximum except possibly the segment \([1/2,1-y]\) when \(e=1/3\); for \(y>0\) that segment has value \((1-2y)/3\), strictly below the action-\(1\) payoff \((1-y)/3\). Consequently no interior opponent position belongs to an equilibrium unless the other candidate is at endpoint \(0\) or \(1\). Against endpoint \(0\), the best response is uniquely \(1/2\) if \(e<1/3\), uniquely \(1\) if \(e>1/3\), and the entire segment \([1/2,1]\) if \(e=1/3\); the best responses against endpoint \(1\) are reflections. Against the middle policy, the best response set is precisely \(\{0,1\}\). Combining these statements yields the same finite classifications off \(e=1/3\), and exactly the four continuum branches \(\mathcal I\) at equality.

**Turnout and the discontinuity.** In a half-center equilibrium, every voter bloc has distance advantage \(1/2\), so total turnout is \(K(1/2)=2^{-q}\). In an extreme equilibrium, the two endpoint blocs have advantage one and the center bloc is indifferent and abstains, so total turnout is \(2e\). Their threshold difference is exactly \(J(q)\), positive for \(q\ge1\). At \(q=1,e=1/3\), every equilibrium is a reflection/relabeling of \((0,z)\) for \(1/2\le z\le1\), and total turnout is \((1+z)/3\), ranging across \([1/2,2/3]\). No other equilibrium types exist by the best-response analysis.

## Verification

Run the accompanying file `verify.py` using Python 3: `python verify.py`. All calculations are self-contained, using `fractions.Fraction` and no third-party packages. It verifies the equilibrium classification on a finite rational action grid for four integer powers and several centrist weights, checks both limiting turnout regimes exactly, and verifies midpoint-convexity inequalities on multiple finite-support profiles. The reference execution passed 13,750 exact-rational grid-profile classifications and 189 midpoint-convexity inequalities. These finite tests corroborate but do not prove the claims over all real policies, weights, and \(q\); the proof above supplies the universal argument.

## Relationship to prior work

Wolf and Meir (2026, arXiv:2609.29869v1) define the underlying costly-voting payoff rule, analyze polarization for continuous electorates, and discuss power-law costs. Their main voter-position assumption is a strictly positive continuous density; their nonuniform-electorate appendix examines smooth examples. The atomic three-bloc threshold and its entire continuous-policy equilibrium and turnout classifications are not presented in those inspected sections.

Kamada and Kojima (2014) **already analyze the same three ideal-point locations and the effect of polarization on policy divergence**, but candidate policies in their model belong only to the three-point action set, voters always vote according to a probabilistic preference-shock rule, and candidate preferences include a winning/payoff refinement. Their theorem has a center-center or extreme-extreme dichotomy. They also discuss an equivalence in *winning probabilities* with an associated costly-voting formulation. Neither a winning-probability equivalence nor their particular policy-action game implies this theorem's unnormalized expected-vote-share payoffs, zero-turnout at co-location, half-center equilibria, continuous-action reduction, or the discontinuous turnout law. General qualitative divergence and the use of three concentrated voter blocs are not claimed as new.

Bhaskar and Pyne (arXiv:2412.12523v1) study spatial competition with atomic voter populations but compulsory nearest-candidate voting; their equilibrium-computation results use a different payoff. Mustillo (2026) studies costly party competition using an agent-based model, and Arzumanyan (2025) studies group-rule-utilitarian strategic turnout, neither under these exact strategic and cost rules in the material inspected.

## Limitations

The result is an exact analytic special-case statement for three atomic voter groups and a common power-law turnout-cost distribution. It establishes neither persistence under smoothing of the voter distribution nor uniqueness of mixed equilibria. The finite verifier does not establish mathematical novelty or prove universal quantifiers. An earlier equivalent derivation using another parameterization of turnout-cost spatial games remains possible. Independent scientific validation has not been performed.

## References

1. Guy Wolf and Reshef Meir, *Costly Voting in the Hotelling–Downs Model*, arXiv:2609.29869v1 (first submitted 2026-09-24), https://arxiv.org/abs/2609.29869 .
2. Yuichiro Kamada and Fuhito Kojima, *Voter Preferences, Polarization, and Electoral Policies*, *American Economic Journal: Microeconomics* **6** (2014), 203–236, https://doi.org/10.1257/mic.6.4.203 .
3. Umang Bhaskar and Soumyajit Pyne, *Equilibrium Computation in the Hotelling–Downs Model of Spatial Competition*, arXiv:2412.12523v1, https://arxiv.org/abs/2412.12523 .
4. Thomas Mustillo, *Party Competition with Costly Voting*, *Journal of Artificial Societies and Social Simulation* **29** (2026), https://doi.org/10.18564/jasss.6117 .
5. Mariam Arzumanyan, *Exploring Voter Turnout Dynamics in Polarized Elections: A Group-Rule Utilitarian Framework*, *Rationality and Society* (2025), https://doi.org/10.1177/10434631241300255 .
