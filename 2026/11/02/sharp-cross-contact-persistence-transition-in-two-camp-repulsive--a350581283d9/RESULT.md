# Sharp cross-contact persistence transition in two-camp repulsive bounded-confidence networks

## Finding
For the synchronous signed bounded-confidence model of Kann and Feng [1], any connected signed undirected network with two internally uniform camps and constant within-camp positive and cross-camp negative degrees has an exact three-way contact-transition classification. Set \(\alpha=r_A/(1+p_A+r_A)\), \(\beta=r_B/(1+p_B+r_B)\), and \(\eta=\alpha+\beta\). From every strictly separated two-camp initial state with \(0<d_0<c\), cross-camp interactions (i) persist at every finite step and approach confidence distance \(c\) when \(\eta<1\), (ii) close exactly at the first step when \(\eta=1\), or (iii) overshoot the confidence distance and close at the first step when \(\eta>1\). The overshoot is \((\eta-1)(c-d_0)\), and its supremum normalized by \(c\) over these finite graphs and initial states is one, not attained.

## Assumptions and scope
The graph has a nonempty vertex partition \(V=A\sqcup B\) and is connected, finite, undirected and signed. A vertex in \(A\) has exactly \(p_A\geq0\) positive edges within \(A\) and \(r_A\geq1\) negative edges into \(B\); a vertex in \(B\) has exactly \(p_B\geq0\) positive edges within \(B\) and \(r_B\geq1\) negative edges into \(A\). There are no other off-diagonal edges. Each vertex also has the positive self-loop of the model. Community cardinalities and degrees obey the ordinary graph realizability conditions; they need not be equal.

At time \(t=0\), all agents in \(A\) hold \(a\), all in \(B\) hold \(b\), with \(0<b-a<c\) and \(c>0\). At a synchronous update, a pair interacts only if its opinion distance is strictly less than \(c\). A positive neighbor with signed opinion difference \(s\) contributes \(s\) to the numerator; a negative neighbor with nonzero difference \(s\) contributes \(-\operatorname{sign}(s)(c-|s|)\). The sum is divided by the number of receptive off-diagonal neighbors plus the self-loop, so the self-loop is counted in the denominator but contributes zero. This is the equal-unit-edge-weight version of equation (3) of [1]. No equality-of-opinions ambiguity arises on negative edges in the states under study.

Write \(d_t=b_t-a_t\) and \(\Delta=c-d_0>0\), and define \(\alpha,\beta,\eta\) as in the finding. Because \(r_A,r_B\geq1\), one has \(0<\eta<2\).

## Proof
Suppose first that \(0<d_t<c\). Every existing edge is receptive. A positive within-camp neighbor has the same opinion as the updating vertex and contributes zero; each negative cross-camp edge contributes \(-\!(c-d_t)\) to an \(A\) agent and \(+\!(c-d_t)\) to a \(B\) agent. Thus all agents in a camp receive the same update, proving by induction that within-camp equality is preserved as long as the cross edges are active, with
\[
a_{t+1}=a_t-\alpha(c-d_t),\qquad b_{t+1}=b_t+\beta(c-d_t),\qquad c-d_{t+1}=(1-\eta)(c-d_t).
\]
For \(\eta<1\), the last recurrence remains strictly positive and yields \(c-d_t=\Delta(1-\eta)^t\) for every integer \(t\geq0\). Summation gives the exact opinions
\[
a_t=a-\frac{\alpha\Delta}{\eta}\left[1-(1-\eta)^t\right],\qquad b_t=b+\frac{\beta\Delta}{\eta}\left[1-(1-\eta)^t\right].\]
They remain distinct and closer than \(c\) at every finite time, and their difference converges geometrically to exactly \(c\). Thus the indicator graph of receptive pairs at each finite time includes all cross-camp edges, while the indicator graph recomputed from the limiting opinion vector excludes them because the confidence inequality is strict. This is a genuine noncommutation of limit and strict-threshold evaluation, not a claim about finite-time convergence.

For \(\eta=1\), the first recurrence gives \(d_1=c\); for \(\eta>1\), it gives \(d_1=c+(\eta-1)\Delta>c\). Hence no cross-camp pair is receptive at time one. Positive intra-camp pairs have equal opinions and contribute zero; these opinions consequently freeze forever. The frozen values are \(a_1=a-\alpha\Delta\) and \(b_1=b+\beta\Delta\). The normalized excess \((d_1-c)/c=(\eta-1)(1-d_0/c)\) is strictly less than one, since \(\eta<2\). Its supremum is one: take the graph with two equal camps of size \(m\), no positive off-diagonal edges, and every cross-camp edge negative. This connected graph has \(\eta=2m/(m+1)\to2\); choosing \(d_0/c\to0^+\) gives normalized excess approaching one.

All three phases occur in connected signed graph families. For two size-\(m\) camps, positive cliques connected by a negative perfect matching have \(\eta=2/(m+1)<1\) when \(m\ge2\). Positive cliques plus all negative cross edges have \(\eta=1\). The all-negative complete bipartite graph has \(\eta=2m/(m+1)>1\). These constructions establish sharpness, including the equality phase.

## Verification
The standalone file `verify_signed.py` uses exact rational arithmetic, executes the signed synchronous update directly and checks the prediction for all three graph families at each integer time from zero through 22, for sizes \(m=2,\ldots,11\). It reports 30 passed graph cases. This finite computation is a reproducibility check, not the proof for all graph sizes; the preceding induction and exact scalar recurrence establish the general theorem.

## Relationship to prior work
Kann and Feng [1] define the signed bounded-confidence rule and study convergence or divergence mechanisms, including an all-repulsive complete-graph theorem and simulations for community graphs. Their all-repulsive complete graph has negative within-camp interactions and does not contain the positive-within/negative-cross graph class here; their results do not state the degree-ratio boundary or finite-versus-asymptotic contact closure classification. Their general conjectural bounds on opinion spread also do not imply it. Li, Luo and Porter [2] consider adaptive confidence bounds rather than this fixed-threshold signed repulsion. Continelli and Pignotti [3] analyze time-dependent attractive Hegselmann–Krause interactions in continuous time, not the synchronous repulsive mechanism.

## Limitations
The classification applies to exactly two initially homogeneous camps and sign-biregular graphs under the stated discrete synchronous rule. It does not establish behavior for arbitrary within-camp heterogeneity, mixed edge signs within communities, varying confidence bounds, asynchronous updating, or agents whose negative neighbors initially agree exactly. The formula does not assert a universal global bound on all signed networks. A literature-equivalent quotient reduction may exist beyond the examined references.

## References
[1] Claudia Kann and Michelle Feng, *A Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1 (first publicly posted 2023-01-05), https://arxiv.org/html/2301.02210v1 .
[2] Grace J. Li, Jiajie Luo and Mason A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, https://arxiv.org/html/2303.07563v3 .
[3] Elisa Continelli and Cristina Pignotti, *Convergence to consensus results for Hegselmann-Krause type models with attractive-lacking interaction*, arXiv:2306.07658, https://arxiv.org/abs/2306.07658 .
