# Sharp three-person consensus windows under activity-weighted bounded confidence

## Finding

An activity-weighted Deffuant–Weisbuch model can turn a single early interaction into an irreversible decision between consensus and fragmentation, even on a complete network. The following theorem determines the *entire terminal law*, its sharp confidence thresholds, and the opposite effects that the same activity change can produce for two mirrored initial opinion profiles.

**Theorem.** Consider three agents on the complete graph, initially at opinions \((0,b,1)\), where \(0<b<1\). At each independent discrete update, choose agent \(i\) with probability proportional to its fixed positive activity \(w_i\), then independently choose one of its two neighbors \(j\) with probability proportional to \(w_j\). If their distance is strictly less than \(c\), where \(0<c<1\), replace *both* opinions by their arithmetic mean; otherwise leave them unchanged. Write \(W=w_1+w_2+w_3\), and, for distinct indices, define the actual probability of selecting the unordered dyad
\[
q_{ij}=\frac{w_iw_j}{W}\left(\frac1{W-w_i}+\frac1{W-w_j}\right),
\qquad q_{12}+q_{13}+q_{23}=1.
\]
Set \(L=(b/2,b/2,1)\), \(R=(0,(1+b)/2,(1+b)/2)\), and \(C=((1+b)/3,(1+b)/3,(1+b)/3)\). Define the *strict* initial-bridge condition \(B=\{1-c<b<c\}\) and \(\theta=q_{12}/(q_{12}+q_{23})\). The opinion vector converges almost surely, and its terminal distribution is as follows.

1. If \(B\) fails, the terminal vector is \((0,b,1)\), \(L\), or \(R\), according as neither, only dyad \(12\), or only dyad \(23\) is initially receptive. In particular, consensus has probability zero.
2. If \(B\) holds, the terminal distribution is a mixture with weights \(\theta\) and \(1-\theta\). The first component is \(C\) if \(b>2(1-c)\), and is otherwise \(L\). The second component is \(C\) if \(b<2c-1\), and is otherwise \(R\).

Thus, for *all* \(b,c\in(0,1)\) and positive activity weights,
\[
\boxed{\Pr(\mathrm{consensus})=
\mathbf 1_{\{1-c<b<c\}}
\frac{q_{12}\mathbf 1_{\{b>2(1-c)\}}+
q_{23}\mathbf 1_{\{b<2c-1\}}}{q_{12}+q_{23}}.}
\]
In particular, the largest consensus probability attainable by varying \(b\) over the entire interval \((0,1)\), at fixed \(c\) and weights, is exactly
\[
\boxed{\max_{0<b<1}\Pr(\mathrm{consensus})=
\begin{cases}
0,&0<c\le 2/3,\\
\max\{\theta,1-\theta\},&2/3<c\le 3/4,\\
1,&3/4<c<1.
\end{cases}}
\]
At the *two equality cases*, \(c=2/3\) and \(c=3/4\), the strict-confidence rule produces the lower regime. The thresholds do not depend on the positive activity weights.

The impact of activity is conditional on initial alignment: at \(c=4/5\), with \((w_1,w_2,w_3)=(a,1,1)\), \(a>0\), the profile \((0,7/10,1)\) has consensus probability
\[
\boxed{\frac{a(a+3)}{a(a+3)+4}},
\]
whereas the mirrored profile \((0,3/10,1)\) has probability
\[
\boxed{\frac4{a(a+3)+4}}.
\]
Consequently, increasing the activity of the same leftmost agent drives consensus to probability one in the first profile but to probability zero in the second. Both have consensus probability \(1/2\) at equal activity.

## Assumptions and scope

The theorem fixes exactly three *labeled* agents on the complete, unchanging graph; equal weighted influence on the two participants (compromise fraction \(1/2\)); strictly positive fixed node weights; independently repeated pair selections using the **node-first, weight-conditioned neighbor** rule; the strict boundary test \(<c\); and initial opinions \((0,b,1)\) with \(0<b,c<1\). It is not a statement for partially updated pairs, general compromise fractions, opinion-dependent weights, multiway updates, arbitrary initial populations, random initial opinions, or larger networks. Terminal convergence rather than finite-time exact equality is asserted on the consensus branch.

The labels \(12\), \(13\), and \(23\) denote unordered edges, not ordered activation events. If an edge is inactive, its selection is a null update; it still contributes to elapsed discrete time. Receptiveness is strict, so any threshold equality is **inactive**, including at all displayed critical values.

## Proof

**1. The unordered edge law and the first effective event.** The first-then-second sampling rule gives
\[
\Pr(\{i,j\})=\frac{w_i}{W}\frac{w_j}{W-w_i}
+\frac{w_j}{W}\frac{w_i}{W-w_j}=q_{ij}.
\]
The three numbers are positive and sum to one. Initially edge \(13\) is inactive because its opinion distance is exactly \(1>c\). Edge \(12\) is active precisely if \(b<c\); edge \(23\) is active precisely if \(1-b<c\). Therefore both are active precisely on \(B\). Because every active edge has positive fixed sampling probability, some active edge is eventually sampled almost surely. Conditional on both being active, the first effective edge is \(12\) with probability \(\theta\) and \(23\) with probability \(1-\theta\); repeated null selections of \(13\) do not alter the ratio.

**2. Exactly one active edge cannot create consensus.** When just \(12\) is initially active, the first effective averaging sets the state to \(L=(b/2,b/2,1)\). The third agent was initially at distance \(1-b\ge c\) from agent \(2\), and its new distance is the larger value \(1-b/2\ge c\). Both edges from the coincident pair to agent \(3\) are hence permanently inactive. Analogously, an initially isolated agent \(1\) remains isolated after the only active edge \(23\) is averaged, leaving state \(R\). If no edge is active there is no update at all.

**3. Both initially active: exact absorbing alternatives.** If the first effective edge is \(12\), both members acquire opinion \(b/2\) while agent \(3\) keeps opinion \(1\). If \(1-b/2\ge c\), both cross-edges are inactive and state \(L\) is permanently frozen. If \(1-b/2<c\), *every* unordered pair has opinion gap \(<c\). The condition is equivalent to \(b>2(1-c)\). The mirrored computation for first effective edge \(23\) gives state \(R\) and consensus-branch condition \((1+b)/2<c\), equivalent to \(b<2c-1\).

**4. Almost-sure consensus in the all-receptive branch.** An arithmetic-mean update keeps every opinion within the preceding convex hull. Therefore if all gaps are \(<c\) immediately after the first effective update, all later gaps remain \(<c\); pair receptiveness never disappears. The arithmetic mean \(\bar x=(1+b)/3\) is conserved. Let \(V=\sum_{i=1}^3(x_i-\bar x)^2\) and \(q_{\min}=\min_{i<j}q_{ij}>0\). Averaging dyad \(ij\) decreases \(V\) by exactly \((x_i-x_j)^2/2\). As \(\sum_{i<j}(x_i-x_j)^2=3V\), conditional expectation satisfies
\[
\mathbb E[V(t+1)\mid x(t)]\le
\left(1-\frac32q_{\min}\right)V(t).
\]
The factor is in \([0,1)\) because the three probabilities sum to one and the variance reduction is nonnegative. Hence \(\mathbb EV(t)\to0\) geometrically. Since \(V(t)\) is nonincreasing and nonnegative, it converges almost surely to a random limit, whose expectation is zero by bounded convergence. Thus the limit is zero almost surely, and all three opinions converge to \(\bar x\), proving the asserted terminal vector \(C\).

**5. Sharp boundary classification.** A successful first edge \(12\) requires \(1-c<b<c\) together with \(2(1-c)<b\); this admissible interval exists precisely when \(2(1-c)<c\), or \(c>2/3\). By reflection the same threshold governs edge \(23\). The two success inequalities can hold for the same \(b\) precisely when \(2(1-c)<2c-1\), or \(c>3/4\). In that case \(b=1/2\) makes both possible, so the maximal consensus probability is one. When \(2/3<c\le3/4\), the two success ranges are disjoint; their attainable probabilities are respectively \(\theta\) and \(1-\theta\), yielding the middle maximum. When \(c\le2/3\), neither can occur. Equality cases fail because each inequality is strict.

**6. Activity reversal.** If \((w_1,w_2,w_3)=(a,1,1)\), direct substitution gives \(q_{12}/(q_{12}+q_{23})=a(a+3)/(a(a+3)+4)\). At \(c=4/5\), \(b=7/10\) satisfies only the first-edge success inequality, while \(b=3/10\) satisfies only the second-edge one. The displayed complementary probabilities follow. Their monotonicity in \(a\) is strict because \(a(a+3)\) is strictly increasing for \(a>0\).

## Verification

The attached standalone \(\texttt{check.py}\) uses exact rational arithmetic. It independently enumerates the three possible unordered first effective interactions and tests the resulting midpoint configuration against global receptiveness; it then compares the resulting probability with the claimed closed form for 23,670 rational configurations or identities, including asymmetric positive activities, the exact boundary cases, and the mirrored activity profiles. Execute from the package directory with \(\texttt{python3 check.py}\), expecting \(\texttt{PASS 23670 exact comparisons}\). These finite computations independently corroborate the algebra. The almost-sure convergence step and the sharp quantifiers are proved above and do not follow from the finite tests.

## Relationship to prior work

Li and Porter (arXiv:2206.09490, Sections II and IV–V) define precisely the fixed-node-activity dyad selection mechanism used here and report, primarily by Monte Carlo simulation, greater fragmentation under heterogeneous randomly assigned weights. Their discussion explicitly proposes exploring how weight placement relative to initial opinions affects outcomes. The theorem supplies an exact conditional three-agent case where that effect changes sign under mirrored initial opinions, without asserting that the larger-population ensemble trend is wrong. The sampling mechanism and original model are credited, not claimed as discoveries here.

Lanchier and Li (arXiv:2005.13141) prove consensus-probability bounds for multivariate Deffuant models on finite connected graphs, with different initial-law and selection assumptions; these bounds do not determine the present conditional terminal distribution or sharp rational-activity formula. Chen, Su, Mei, and Bullo (arXiv:1901.02092) study heterogeneous **confidence bounds**, not fixed heterogeneous sampling activities, and primarily prove convergence and consensus conditions. Bernardo and collaborators' 2024 survey (DOI 10.1016/j.automatica.2023.111302) chiefly addresses synchronous bounded-confidence systems, rather than an asynchronously sampled complete triad.

The first-receptive-dyad decomposition uses elementary Markov conditioning and convex averaging, both standard methods. Neither the general method nor the mere existence of a finite consensus threshold is presented as new. The proposed contribution is their exact, fully quantified combination for the smallest complete heterogeneous-activity motif, notably including both sharp confidence windows and the opposite activity effects under two aligned initial profiles.

## Limitations

The complete result is restricted to three agents, fixed positive sampling weights, maximal equal compromise, and initial endpoints normalized to \(0\) and \(1\). It does not imply average trends for random population profiles or graphs with four or more agents. No publication-priority or independent audit claim is made: broader existing stochastic-averaging results, unindexed treatments of small confidence networks, and the full history of related model variants remain residual originality risks. The boundary convention \(<c\) is essential, and changing it changes the equality cases.

## References

1. G. J. Li and M. A. Porter, *A bounded-confidence model of opinion dynamics with heterogeneous node-activity levels*, first public preprint 19 June 2022, arXiv:2206.09490, https://arxiv.org/html/2206.09490v2 ; Phys. Rev. Research 5, 023179 (2023).
2. N. Lanchier and H.-L. Li, *Probability of consensus in the multivariate Deffuant model on finite connected graphs*, arXiv:2005.13141, https://arxiv.org/abs/2005.13141 .
3. G. Chen, W. Su, W. Mei, and F. Bullo, *Convergence Properties of the Heterogeneous Deffuant-Weisbuch Model*, arXiv:1901.02092, https://arxiv.org/abs/1901.02092 .
4. C. Bernardo, C. Altafini, A. V. Proskurnikov, and F. Vasca, *Bounded confidence opinion dynamics: a survey*, Automatica 159 (2024), 111302, https://doi.org/10.1016/j.automatica.2023.111302 .
