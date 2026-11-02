# Three sharp optimal-placement regimes in a directional six-voter ring

## Finding

Two fixed, opposite opinions in a six-agent circular network can be placed one, two, or three edges apart. In a nearest-neighbor voter process with directional copying, the separation minimizing fluctuations in the total opinion-one count exhibits **three distinct regimes**, with exact algebraic transition points. In particular, there is a nonempty parameter interval on which the unique optimum is **neither** adjacent nor antipodal.

Write \(P(z)=z^6+2z^5-z^4-18z^3-38z^2-12z+8\) and \(Q(z)=2z^3-z^2-10z-4\). Each polynomial has exactly one root in \(z>2\); denote them \(z_P,z_Q\), respectively. They satisfy \(z_P>27/10>z_Q\). Define

\[
q_- = \frac{z_P-\sqrt{z_P^2-4}}2=0.4321746804683752097\ldots,
\qquad
q_+ = \frac{z_Q-\sqrt{z_Q^2-4}}2=0.4528129368129362104\ldots.
\]

For \(0<q\le1\), the unique variance-minimizing clockwise separation \(a\in\{1,2,3\}\) is \(a=1\) when \(q<q_-\), \(a=2\) when \(q_-<q<q_+\), and \(a=3\) when \(q>q_+\). At \(q=q_-\) exactly the first two separations tie; at \(q=q_+\) exactly the last two tie. For \(q>1\), the same description applies with \(q\) replaced by \(1/q\).

At the exact rational bias \(q=4/9\), the three stationary opinion-count variances are

\[
V_1=\frac{5338692}{5387041},\qquad
V_2=\frac{1553544}{1590121},\qquad
V_3=\frac{17352}{17689},
\]

with \(V_2<V_3<V_1\). This is the smallest cycle permitting a strictly intermediate geometric optimum: there is no choice \(1<a<\lfloor n/2\rfloor\) when \(n<6\).

## Assumptions and scope

Let the vertices of the simple cycle \(C_6\) be \(0,1,\dots,5\) in clockwise order. Vertex \(0\) is permanently in opinion \(0\); vertex \(a\) is permanently in opinion \(1\), with \(a\in\{1,2,3\}\). The remaining four agents have opinions in \(\{0,1\}\). Independently, each unfixed agent copies the opinion at the next clockwise vertex at rate \(1\), and the opinion at the previous counterclockwise vertex at rate \(q>0\), in continuous time. A copy from an equal-opinion neighbor has no effect. There are no spontaneous flips, long-distance edges, or rate heterogeneities other than this common directional bias. The stationary distribution is unique. Denote the total number of opinion-one agents by \(X\), including the fixed one-agent, and its stationary variance by \(V_a(q)\).

## Proof

**1. Stationary domain walls.** The two fixed agents split the cycle into independent directed-copying paths, of \(a\) and \(6-a\) edges, with opposite fixed endpoint opinions. On any such path, the number of adjacent disagreeing pairs is odd. Copying a nearest neighbor never creates new disagreeing pairs, and a suitable finite sequence of allowed copying events reduces any state to one disagreeing pair. Since all rates are positive, the one-interface states form the unique closed communicating class. Within this class, the interface performs an irreducible reflecting birth–death walk. The two paths use disjoint free agents and update clocks; their stationary laws are independent.

For a path containing \(L\ge1\) edges, its one-interface states correspond to \(L\) possible counts of opinion-one internal agents, \(0,1,\ldots,L-1\). On one path, the count rises at rate \(1\) and falls at rate \(q\); on the other, the rates reverse. Their stationary count laws are truncated geometric distributions with respective weights proportional to \(q^{-j}\) and \(q^j\). Their variances agree. For \(q\ne1\), logarithmic differentiation of the partition function \(\sum_{j=0}^{L-1}q^j=(1-q^L)/(1-q)\) gives

\[
W_L(q)=\frac{q}{(1-q)^2}-\frac{L^2q^L}{(1-q^L)^2},
\]

and \(W_L(1)=(L^2-1)/12\). In particular \(W_1=0\), \(W_L(q)=W_L(1/q)\), and by independence

\[
V_a(q)=W_a(q)+W_{6-a}(q).
\]

**2. Exact factorization.** It suffices to take \(0<q<1\). Put \(z=q+q^{-1}>2\). Direct common-denominator algebra from the preceding formula yields

\[
V_1-V_2=-\frac{q^7P(z)}{(q+1)^2(q^2+1)^2(q^4+q^3+q^2+q+1)^2},
\]

and

\[
V_2-V_3=-\frac{2q^5Q(z)}{(q+1)^2(q^2+1)^2(q^2+q+1)^2}.
\]

All denominators are positive. These identities are rational-polynomial identities, not numerical fits.

**3. Uniqueness and order of phase boundaries.** Write \(t=z-2>0\). The shifted polynomials are

\[
P(t+2)=t^6+14t^5+79t^4+214t^3+230t^2-60t-200,
\]

\[
Q(t+2)=2t^3+11t^2+10t-12.
\]

Each has exactly one sign change in descending powers, so Descartes' rule of signs allows at most one positive root. Both are negative at \(t=0\) and tend to \(+\infty\), so each has exactly one positive root. Furthermore, at \(z=27/10\),

\[
P(27/10)=-\frac{34459471}{1000000}<0,
\qquad
Q(27/10)=\frac{269}{250}>0.
\]

Hence \(z_P>27/10>z_Q\). Since \(q=(z-\sqrt{z^2-4})/2\) is strictly decreasing for \(z>2\), we have \(0<q_-<q_+<1\).

**4. Sign classification.** For \(0<q<q_-\) both \(P(z)\) and \(Q(z)\) are positive, so \(V_1<V_2<V_3\). For \(q_-<q<q_+\), \(P(z)<0<Q(z)\), giving \(V_2<V_1\) and \(V_2<V_3\). For \(q_+<q<1\), both are negative, yielding \(V_3<V_2<V_1\). At either root precisely the stated pair ties, while the third variance is strictly higher. Continuity of \(W_L\) at \(q=1\) gives the antipodal optimum there as well. The symmetry \(W_L(q)=W_L(1/q)\) gives the \(q>1\) statement. Exact substitution at \(q=4/9\) yields the rational variances displayed in the finding, showing a strict interior optimum.

## Verification

Run `python3 check_voter.py` with SymPy. The self-contained script verifies both rational-polynomial identities, the shifted-polynomial expansions, the rational root-order witness, and the strict rational witness at \(q=4/9\). Separately, it constructs the complete sixteen-state continuous-time generator on the unfixed agents, solves for stationary probabilities with exact rational arithmetic for each of three placements and each of three positive rational copying-rate ratios, and checks equality with the analytic variances. The proof above establishes the entire continuum of rates; the finite generator checks are independent finite corroboration and do not prove the continuum claim alone.

## Relationship to prior work

Mobilia, Petersen, and Redner (2007) study the voter model with fixed opposite zealots and derive the unbiased one-dimensional domain-wall picture, including the distribution on two arcs. That domain-wall mechanism is prior knowledge; it does not contain the directional-rate six-cycle phase boundaries stated here. Yildiz, Acemoglu, Ozdaglar, Saberi, and Scaglione (2011 manuscript) develop general covariance and stationary-fluctuation formulas for stubborn-agent voter networks, including directed networks, and study a distinct placement objective maximizing expected influence. Those general frameworks can evaluate finite examples but the inspected material does not state or directly imply the three-regime algebraic minimization theorem without the new parameter comparison. Their relevance limits claims of broad novelty. The contribution here is specifically the strict algebraic threshold classification for the minimum stationary **total-count variance** when opposing zealot positions vary under a common directional copying bias.

## Limitations

The model is small and idealized: exactly six vertices, one fixed agent of each opinion, independent Poisson nearest-neighbor copying, homogeneous directional rates, and stationary—not transient—opinion-count variance. The minimizer may change under spontaneous noise, additional zealots, different network geometries, heterogeneous rates, or a different objective such as the mean opinion. No general phase diagram for all ring sizes is claimed. A finite exact phase diagram is not proof of empirical political behavior. Historical-priority searches did not establish global uniqueness; more specialized literature on directed voter rings or truncated-geometric allocation may contain equivalent statements.

## References

1. M. Mobilia, A. Petersen, and S. Redner, “On the Role of Zealotry in the Voter Model,” *J. Stat. Mech.* P08029 (2007), arXiv:0706.2892 (first public posting 2007-06-20), https://arxiv.org/abs/0706.2892, DOI:10.1088/1742-5468/2007/08/P08029.
2. E. Yildiz, D. Acemoglu, A. Ozdaglar, A. Saberi, and A. Scaglione, “Discrete Opinion Dynamics with Stubborn Agents,” *Operations Research* manuscript OPRE-2011-01-026, https://web.mit.edu/Asuman/Desktop/asuman/www/documents/voter-submit.pdf.
3. M. Mobilia, “Nonlinear q-voter model with inflexible zealots,” *Physical Review E* 92, 012803 (2015), arXiv:1506.04911, DOI:10.1103/PhysRevE.92.012803 (different well-mixed nonlinear model).
