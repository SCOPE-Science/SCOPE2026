# Polynomial universality and disconnected optimal viscosity in two-guru delegation forests

## Finding

**Theorem (two-guru realization and sharp consequences).** Consider a finite, fixed, acyclic delegation graph consisting of exactly two rooted trees, one rooted at each direct voter (guru). Each non-guru delegates to its parent. A vote at delegation distance \(d\) contributes weight \(\alpha^d\) to its root, for \(0\le\alpha\le1\). Both gurus cast independent binary votes; the first is correct with probability \(4/5\) and the second with probability \(3/5\). The larger total weighted vote wins, with an independent fair coin deciding any exact tie. Let \(A_D(\alpha)\) be the probability of a correct group decision.

1. **Universality.** For every integer polynomial \(P(t)\in\mathbb Z[t]\) with \(P(0)=P(1)=0\), there exists such a delegation forest with *equally many voters in its two trees* whose guru-weight difference is exactly \(P(\alpha)\). For this forest,
   \[
   A_D(\alpha)=\begin{cases}
   4/5,&P(\alpha)>0,\\
   7/10,&P(\alpha)=0,\\
   3/5,&P(\alpha)<0.
   \end{cases}
   \]
2. **Arbitrarily disconnected optima.** For every integer \(m\ge1\), a two-guru, equal-component-size forest has exactly \(m\) connected components in its set of globally accuracy-maximizing viscosity parameters. In particular, that optimal set can be precisely
   \[
   \bigcup_{r=1}^{m}\left(\frac{2r-1}{2m},\frac{2r}{2m}\right).
   \]
3. **No fixed-grid safeguard.** For every nonempty finite set \(S\subset[0,1]\), some two-guru, equal-component-size forest satisfies
   \[
   \max_{\alpha\in[0,1]}A_D(\alpha)=4/5,
   \qquad\max_{\alpha\in S}A_D(\alpha)\le7/10.
   \]
   Thus every predetermined finite viscosity grid can miss the optimal regime by at least \(1/10\) in group accuracy, even with just two independent guru votes.
4. **Sharp small example.** A six-voter forest consisting of a two-leaf star and a three-vertex path has \(A_D(\alpha)=4/5\) for every \(0<\alpha<1\), but \(A_D(0)=A_D(1)=7/10\). No acyclic delegation forest on at most five voters, with any number of gurus and any independent guru competencies, can have accuracy strictly greater at an interior viscosity than at both endpoints, under the same fair-tie rule. Six voters are therefore the sharp first size exhibiting strict interior advantage over both endpoint choices.

## Assumptions and scope

Every finite rooted tree has one distinguished root (guru); every other vertex chooses exactly its unique parent, so delegation paths are acyclic. The two-guru constructions use exactly two components, with one independently cast ballot per component; delegators do not cast independent ballots. The weight of each guru is the sum of \(\alpha^{d(v)}\) over vertices in its component, including the guru at distance zero. The ground truth is fixed and the independent guru votes have the specified correctness probabilities. In a tie of *total weighted votes*, not just a tie of guru weights, a fair independent coin is used. The theorem concerns a fixed delegation graph, not optimization over the graph, strategic responses, stochastic changes of delegation, or alternative tie rules. The small-size minimality result permits arbitrary independent guru correctness probabilities in \([0,1]\).

## Proof

**Depth polynomials and realization.** Let \(h_{i,d}\) be the number of vertices at distance \(d\) from guru \(i\). Then
\[
w_i(t)=\sum_{d\ge0}h_{i,d}t^d,\qquad h_{i,0}=1.
\]
Conversely any finite integer sequence \(h_0=1\) and \(h_d\ge1\) for every \(1\le d\le L\) is realized by a rooted tree: put \(h_d\) vertices at level \(d\) and assign each the first vertex of level \(d-1\) as parent. The result is connected and has a unique route to its root, with precisely the required depths.

Write \(P(t)=\sum_{d=1}^L c_dt^d\), where \(c_d\in\mathbb Z\), and define
\[
h_{1,0}=h_{2,0}=1,\quad h_{1,d}=1+\max(c_d,0),\quad h_{2,d}=1+\max(-c_d,0)
\quad(1\le d\le L).
\]
All level populations are positive and hence realizable. Their weight difference is \(w_1(t)-w_2(t)=P(t)\). The two component sizes are equal because their difference is \(\sum_{d=1}^L c_d=P(1)=0\). The zero polynomial can be realized by two singleton gurus, for which both weights agree identically.

If the gurus' weights differ, the heavier guru alone determines the correct outcome probability. If the weights coincide, identical guru votes give the common decision and opposed votes are tied. For independent correctness probabilities \(q_1,q_2\), a fair tie has success probability
\[
q_1q_2+\tfrac12\bigl(q_1(1-q_2)+(1-q_1)q_2\bigr)=\frac{q_1+q_2}{2}.
\]
Substituting \(q_1=4/5\) and \(q_2=3/5\) proves the displayed accuracy formula.

**Any number of accuracy islands.** Take
\[
P_m(t)=t(1-t)\prod_{j=1}^{2m-1}(2mt-j)\in\mathbb Z[t].
\]
Its roots in \([0,1]\) are exactly \(0,1\) and \(j/(2m)\) for \(1\le j\le2m-1\). Each internal root is simple, and the sign on the final open subinterval before \(1\) is positive. Therefore signs alternate on consecutive open subintervals, with \(P_m>0\) precisely on the \(m\) intervals displayed in the statement. The realization lemma turns this polynomial into two equally sized rooted trees; the accuracy formula then makes these intervals exactly the disconnected global maximum set. At all boundary roots the accuracy is only \(7/10\), so the components are genuinely separated.

**An invisible optimum window for any grid.** Given nonempty finite \(S\subset[0,1]\), choose rational \(0<r<s<1\) such that the closed interval \([r,s]\) is disjoint from \(S\). Writing \(r=a/b\) and \(s=c/d\) in positive integers, set
\[
P(t)=t(1-t)(bt-a)(c-dt).
\]
This integer polynomial vanishes at \(0,1,r,s\), is strictly positive exactly when \(r<t<s\), and is strictly negative at all other interior points. The two-tree realization has global accuracy \(4/5\) within the interval, but each grid point has accuracy at most \(7/10\). The claimed gap follows.

**Sharp six-voter boundary.** With two guru trees of depth populations \((1,2)\) and \((1,1,1)\), the weight difference is
\[
(1+2t)-(1+t+t^2)=t(1-t),
\]
which is positive for every \(0<t<1\) and zero at \(0,1\). The two components each have three vertices, so the six-voter construction meets all hypotheses.

For the lower bound, let a forest on at most five vertices have \(g\ge1\) gurus. If \(g=1\), accuracy is viscosity-independent. If \(g=2\), there are at most three delegators; either only one guru receives any delegators, or both do, in which case the components have sizes at most three and two. In the latter case the two guru weights are, up to exchanging gurus, \(1+t\) and either \(1+t+t^2\) or \(1+2t\). The sign of the difference is constant throughout \(0<t\le1\) (or is zero throughout); hence the accuracy on the interior equals that at the endpoint \(t=1\). If \(g=3\), at most two delegators exist. When both feed one guru, its weight is \(1+2t\) or \(1+t+t^2\), while the others each have weight one; weighted majority changes at most once, from ordinary three-guru majority to dictatorship by that guru. When they feed distinct gurus, the weights are \(1+t,1+t,1\) and three-guru simple majority is unchanged. The accuracy at the sole possible threshold is the average of the values immediately to either side, as the only newly tied vote configurations receive a fair tie-breaking coin. For \(g=4\), at most one delegator exists, the only weight change is from \((1,1,1,1)\) at zero to \((1+t,1,1,1)\) for positive \(t\), and the winner for every voting profile is constant over \(0<t\le1\). For \(g=5\), no voter delegates. Thus in every case the maximum accuracy over \([0,1]\) is attained at \(0\) or \(1\), proving minimality. The argument applies for arbitrary independent guru competencies because it only compares the voting rules, not numerical competence values.

## Verification

The standalone `verify.py` reconstructs positive integer level populations from the coefficients of the prescribed polynomials, realizes the first two examples as actual finite parent-pointer forests, checks independent root distances and polynomial weight identities exactly using rational arithmetic, and verifies 75 exact rational test cases. It also enumerates all 1,441 labeled acyclic parent-choice forests on at most five vertices, finding 55 level-profile signatures; exact Sturm root counting detects the sole possible interior majority threshold in 90 of those forests, in agreement with the case proof. Running `python verify.py` should print a single `PASS` line. Neither finite enumeration nor these sample checks replace the all-degree realization proof or the all-size sign argument.

For an explicit two-island example, distinct from the canonical \(P_m\) family above,
\[
Q(t)=-18t^5+45t^4-40t^3+15t^2-2t,
\]
whose two maximizing intervals are \((1/3,1/2)\) and \((2/3,1)\). Applying the construction yields level sizes \((1,1,16,1,46,1)\) and \((1,3,1,41,1,19)\), each with 66 voters; their guru-weight difference is exactly \(Q\).

## Relationship to prior work

Boldi, Bonchi, Castillo and Vigna introduced damped transitive proxy scores (Katz-style attenuated path sums); their 2011 account provides illustrative parameter-dependent score rankings but does not establish polynomial realization or arbitrarily many optimal accuracy windows. Armstrong, Alouf-Heffetz and Talmon (arXiv:2405.06698, first public 2024-05-08) define the binary epistemic viscous-democracy setting, show that interior viscosity can be optimal using a Stars-and-Chains example, and explicitly discuss a piecewise-constant accuracy objective and finite-grid numerical estimation. These already-known observations are not claimed here. The new assertion is unrestricted realization of differences of **two** guru depth polynomials, its unboundedly disconnected accuracy-optimum consequence, the predetermined-grid failure with constant gap, and the sharp six-voter witness. Results on general Katz scores and parametric voting weights are structurally related but are not being asserted to prove these same voting-accuracy statements.

## Limitations

The construction may use many voters and high branching to encode an arbitrarily oscillating polynomial; it does not claim typical or empirical graphs exhibit such oscillations. It uses only two fixed gurus and equal-sized rooted components; unrestricted network evolution, more alternatives, strategic delegation, bounded-degree constraints, and different tie conventions are not covered. Fair tie-breaking is essential at exact score crossings and at the two endpoints of the six-voter example. The grid result concerns a finite sampling grid fixed **before** observing the delegation forest; an adaptive polynomial-root algorithm with access to the graph is not ruled out. No assertion of absolute publication priority or external independent validation is made.

## References

1. B. Armstrong, S. Alouf-Heffetz, and N. Talmon, *Optimizing Viscous Democracy*, arXiv:2405.06698, first publicly posted 2024-05-08. https://arxiv.org/abs/2405.06698 ; IJCAI 2024, https://doi.org/10.24963/ijcai.2024/292 .
2. P. Boldi, F. Bonchi, C. Castillo, and S. Vigna, *Viscous Democracy for Social Networks*, Communications of the ACM 54(6) (2011), 129–137. Author-posted version: https://chato.cl/papers/boldi_bonchi_castillo_vigna_2011_viscous_democracy_social_networks.pdf ; https://doi.org/10.1145/1953122.1953154 .
3. E. W. Weisstein, *Katz Centrality*, MathWorld, https://mathworld.wolfram.com/KatzCentrality.html (background on attenuated-path scoring; no claim of equivalent optimal-parameter results).
