# A sharp one-edge influence optimum on a path with competing leaders

## Finding

Fix an integer \(L\ge3\). On the undirected unit-weight path with vertices \(0,1,\ldots,L\), fix two opposing leaders at opinions \(0\) and \(1\) on vertices \(0\) and \(L\), respectively. All other vertices hold the unique equilibrium opinions obtained by averaging neighbors. Permit exactly one extra unit-weight undirected edge between *any* two initially nonadjacent vertices; neither endpoint is required a priori to be a leader. The objective is the sum (equivalently, mean) of the \(L-1\) followers' equilibrium opinions.

For any edge \(\{a,b\}\), \(0\le a<b\le L\), with \(d=b-a\ge2\), put \(F=L(d+1)-d^2>0\). The exact increase over the original path is

\[
\Delta_L(a,b)=\frac{d^2(a+b-L)}{2\,[L(d+1)-d^2]}.
\]

**Global endpoint theorem.** Every edge maximizing this objective has its right endpoint at the opinion-one leader, \(b=L\), and its left endpoint is a follower \(a\in\{1,\ldots,L-2\}\). In particular, restricting candidates to leader-follower edges is not an assumption: it follows from optimality among **all** missing edges.

The optimal edges are exactly \(\{a,L\}\), where \(a\) maximizes

\[
f_L(a)=\frac{a(L-a)^2}{2[L+a(L-a)]},\qquad 1\le a\le L-2.
\]

Let \(\alpha_L\in(0,L)\) be the unique zero of

\[
P_L(u)=L^2-3Lu-Lu^2+u^3.
\]

Then the complete integer maximizer set consists of whichever of the integers \(\lfloor\alpha_L\rfloor\), \(\lceil\alpha_L\rceil\), clipped to the allowed interval \([1,L-2]\), give the larger value of \(f_L\); retain both if tied. These candidates and the exact rational function provide a complete formula for every finite \(L\).

Moreover, all maximizing positions obey \(a_L=\sqrt L+O(1)\), the optimal **total** opinion increase is

\[
\Delta_L^*=\frac L2-\sqrt L+O(1),
\]

and the optimal mean follower opinion tends to one:

\[
\bar h_L^*=\frac12+\frac{\Delta_L^*}{L-1}
=1-\frac1{\sqrt L}+O(L^{-1}).
\]

Thus one additional link can shift the average follower opinion arbitrarily close to the promoting leader's opinion even though the original path has perfectly balanced mean opinion \(1/2\).

## Assumptions and scope

The graph is finite, simple, connected, undirected, and all original and newly added edges have equal conductance one. Leaders have fixed opinions exactly zero and one. Every other vertex's equilibrium opinion is the arithmetic average of its neighbors' values. This equilibrium is the unique solution to the two-boundary discrete Dirichlet problem. For example, it is the limit of lazy neighbor-averaging updates \(x_j(t+1)=(1-\varepsilon)x_j(t)+\varepsilon\deg(j)^{-1}\sum_{k\sim j}x_k(t)\), at nonleaders, for any \(0<\varepsilon<1\) and arbitrary initial follower opinions in \([0,1]\). Only one previously absent edge of fixed unit conductance may be added. The objective includes the \(L-1\) followers and excludes the two fixed leaders; including both leaders instead would give the same maximizers because their sum is constant.

The theorem is *not* about arbitrary network topologies, heterogeneous edge weights, strategic choice of multiple edges, stochastic time-varying opinion formation, or transient manipulation. It concerns exact equilibrium **average**, not a majority-vote threshold.

## Proof

**1. Existence and uniqueness.** Every follower has a path to the fixed boundary. The grounded graph Laplacian is positive definite: its quadratic form is the sum of edge squares with the two boundary coordinates fixed to zero. The corresponding discrete harmonic extension is therefore unique. The lazy update above has an absorbing random-walk substochastic follower transition with spectral radius below one, so it converges to that extension.

**2. Every chord has an explicit voltage profile.** Regard each edge as a unit resistor and fix boundary voltages \(0\) and \(1\). For a chord from \(a\) to \(b\), the original \(d=b-a\) edge segment is in parallel with a unit resistor. Their equivalent resistance is \(d/(d+1)\), while the outer path lengths are \(a\) and \(L-b\) in series. The total unit-voltage current is \((d+1)/F\), because

\[
a+\frac d{d+1}+(L-b)=\frac{F}{d+1}.
\]

The potential step along the two outer segments is consequently \((d+1)/F\); along each of the \(d\) internal path edges it is \(1/F\). Thus for *all* \(0\le j\le L\), including the endpoints,

\[
h_j^{(a,b)}=\begin{cases}
(d+1)j/F,&0\le j\le a,\\
(da+j)/F,&a\le j\le b,\\
((d+1)j-d^2)/F,&b\le j\le L.
\end{cases}
\]

The formulas agree at \(a,b\) and yield \(h_0=0\), \(h_L=1\), so by uniqueness they are the equilibrium opinions. The original path has \(h_j^{(0)}=j/L\).

**3. Exact gain.** Subtracting \(j/L\) from the three linear pieces and summing over \(j=1,\ldots,L-1\) yields

\[
\sum_{j=1}^{L-1}\!\left(h_j^{(a,b)}-\frac jL\right)
=\frac{d^2(a+b-L)}{2F}.
\]

In particular \(d=L\), the chord between the two fixed leaders, has zero influence; the expression also correctly allows some added edges to *harm* the opinion-one leader's aggregate influence.

**4. Global unrestricted optimum touches the promoting leader.** At fixed integer length \(d\ge2\), we have \(b=a+d\) and

\[
\Delta_L(a,a+d)=\frac{d^2(2a+d-L)}{2[L(d+1)-d^2]}.
\]

Its denominator depends only on \(d\) and is strictly positive. It is strictly increasing in \(a\in\{0,1,\ldots,L-d\}\). Therefore its unique maximum for this length is the edge \(\{L-d,L\}\). This eliminates *every* chord not incident to the leader at \(L\) from global optimality. When \(d=L\) the candidate \(\{0,L\}\) has gain zero, whereas all admissible \(\{a,L\}\), \(1\le a\le L-2\), have positive gain. The cases \(d=1\) are already present path edges. Hence every global maximizer is of the stated form.

**5. Complete finite maximizer classification.** Substitute \(a=L-d\) to obtain \(f_L(a)\). Direct differentiation gives

\[
f_L'(u)=\frac{(L-u)[L^2-3Lu-Lu^2+u^3]}{2[L+u(L-u)]^2}.
\]

Write \(P_L(u)=L^2-3Lu-Lu^2+u^3\). On \([0,L]\), \(P_L(0)=L^2>0\) and \(P_L(L)=-2L^2<0\). Its derivative \(P_L'(u)=3u^2-2Lu-3L\) is initially negative and has at most one positive zero; if that zero lies in \([0,L]\), \(P_L\) first decreases and then increases, but its terminal value is still strictly negative. It follows that \(P_L\) crosses zero exactly once on \((0,L)\). Consequently \(f_L\) increases strictly up to \(\alpha_L\) and decreases strictly afterward. A maximizing admissible integer must be one of the two adjacent integers bracketing \(\alpha_L\), after clipping to the admissible interval; direct exact comparison resolves ties. This proves both necessity and sufficiency of the stated finite algorithm.

**6. Sharp scale.** Set \(u=\sqrt L+c\) for bounded \(c\). The root polynomial satisfies

\[
\frac{P_L(\sqrt L+c)}{L^{3/2}}=-2(c+1)+O(L^{-1/2}).
\]

Thus \(\alpha_L=\sqrt L-1+O(L^{-1/2})\). A maximizing integer differs from \(\alpha_L\) by at most one, so \(a_L=\sqrt L+O(1)\). Substitution into the rational formula (or an expansion uniformly for bounded \(c\)) gives \(f_L(a_L)=L/2-\sqrt L+O(1)\). Division by \(L-1\), added to the original mean \(1/2\), completes the asymptotic mean claim.

## Verification

A standalone exact-rational script, `verify.py`, independently solves the grounded Laplacian via Gaussian elimination, compares every follower potential with the voltage formula, sums the gain, and exhaustively checks all chords for \(3\le L\le11\). It separately checks the cubic root/bracketing characterization against exact integer maximization for \(3\le L\le159\). The extracted checker reports **989 passed assertions**. These finite checks support and test, but do not replace, the all-\(L\) analytical proof above.

For \(L=10\), the unique optimal new edge is \(\{2,10\}\). The exact aggregate gain is \(32/13\), and the new mean follower opinion is \(181/234\) versus the original \(1/2\). For \(L=100\), \(\{9,100\}\) is optimal and yields mean \(9195/10109\).

## Relationship to prior work

Zhao, Liu and Wang (2014) establish the competitive fixed-leader, averaging-agent network model, and show that network changes influence competition; their illustrative edge addition is not an unrestricted exact optimization theorem for paths. Yildiz and colleagues study stochastic binary opinion dynamics with stubborn agents, including stationary absorption interpretations and optimal *leader placement*, which is not the one-extra-edge problem with fixed leaders.

Zhou and Zhang (2021) study essentially the same DeGroot equilibrium objective with an edge-addition budget, but **restrict all candidate edges at the outset** to pairs involving an opinion-one leader and a follower, and develop general algorithms and approximation guarantees. That restriction does not establish the path-specific fact that the optimum over *all* nonedges is necessarily leader-incident. Their general rank-one gain formula also does not state the closed two-parameter chord identity, complete finite path optimum, or square-root placement and near-unanimity asymptotics proved here. These distinctions concern mathematical implication, not merely a mismatch in titles or variables.

The comparisons establish a plausible new result within inspected primary materials and known mathematical records, not an independently certified historical priority claim.

## Limitations

The exact numerical effect presumes unit-weight undirected edges, two perfectly committed endpoint leaders, harmonic neighbor averaging, and a single costless new link of the same weight. Different placements, nonlinear updates, more than one link, partial stubbornness or heterogeneous edge strengths require separate analysis. The fact that equilibrium average approaches one does not imply a corresponding speed of convergence, transient persuasion, or an empirical vote share. Broader historical literature may contain an unlocated equivalent derivation; no independent audit has been performed.

## References

1. Zhao, J., Liu, Q., and Wang, X. (2014). *Competitive Dynamics on Complex Networks*. Scientific Reports **4**, article 5858. Published 2014-07-28. https://doi.org/10.1038/srep05858
2. Zhou, X., and Zhang, Z. (2021). *Maximizing Influence of Leaders in Social Networks*. arXiv:2106.06128, first submitted 2021-06-11. https://arxiv.org/abs/2106.06128
3. Yildiz, E., Acemoglu, D., Ozdaglar, A., Saberi, A., and Scaglione, A. (2011). *Discrete Opinion Dynamics with Stubborn Agents*. SSRN working paper, first publicly posted 2011-01-21. https://doi.org/10.2139/ssrn.1744113. Accessible manuscript text: https://paperzz.com/doc/8057777/discrete-opinion-dynamics-with-stubborn-agents
