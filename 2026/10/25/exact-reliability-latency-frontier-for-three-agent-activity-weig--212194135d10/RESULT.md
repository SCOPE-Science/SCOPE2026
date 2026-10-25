# Exact reliability–latency frontier for three-agent activity-weighted bounded-confidence averaging

## Finding

On the three-vertex path, the node-activity-weighted Deffuant–Weisbuch model with half-compromise has an exact success-probability and conditional hitting-time law. Let \(p\) be the probability of selecting edge \(12\), and \(q=1-p\) the probability of selecting edge \(23\), where \(p,q>0\). If both edges are initially receptive, define \(D_{12}=|x_3-(x_1+x_2)/2|\) and \(D_{23}=|x_1-(x_2+x_3)/2|\). Then the probability of eventual unanimous consensus is

\[
\Pr(\mathrm{consensus})=p\mathbf 1_{\{D_{12}<c\}}+q\mathbf 1_{\{D_{23}<c\}}.
\]

Conditional on initial edge \(12\), success and \(D_{12}>0\), after \(n\ge1\) updates the opinion diameter is \(D_{12}2^{-K_n}\), where \(K_n\) counts changes of selected edge between consecutive updates. The analogous formula holds for initial edge \(23\). Consequently the almost-sure logarithmic convergence exponent on each nontrivial successful branch is \(2pq\log 2\). For \(0<\delta<D_{12}<c\), set \(m=\min\{r\in\mathbb N: D_{12}2^{-r}<\delta\}\); the conditional expected number of updates, **including the initial selection**, until diameter falls strictly below \(\delta\) is

\[
1+\frac{\lceil m/2\rceil}{q}+\frac{\lfloor m/2\rfloor}{p}.
\]

On the successful initial-edge-\(23\) branch, exchange \(p\) and \(q\). For \(m\ge2\), the latter is minimized uniquely at \(p=\sqrt{\lceil m/2\rceil}/(\sqrt{\lceil m/2\rceil}+\sqrt{\lfloor m/2\rfloor})\); its minimum is \(1+(\sqrt{\lceil m/2\rceil}+\sqrt{\lfloor m/2\rfloor})^2\).

In particular, initial opinions \((0,2/5,1)\), confidence \(c=3/4\), and tolerance \(\delta=1/10\) give consensus probability \(q\), but, conditional on consensus, expected tolerance time \(1+2/p+1/q\). Its unique minimizing edge-selection probability is \(p=\sqrt2/(1+\sqrt2)\), at which the success probability is \(\sqrt2-1\) and the expected time is \(4+2\sqrt2\). Pushing success probability toward one makes conditional convergence arbitrarily slow. This is a complete exact reliability–latency tradeoff for this natural minimal path example, not a result about larger graphs.

## Assumptions and scope

Consider path \(1-2-3\), real initial opinions \(x_1,x_2,x_3\in[0,1]\), positive activity weights \(u,v,z\), and a fixed strict confidence radius \(c\in(0,1]\). First select one agent with probability proportional to its weight; then select a neighbor with probability proportional to that neighbor's weight. Selections are independent and identically distributed at successive discrete times. A selected edge whose opinion gap is strictly smaller than \(c\) is updated by replacing both endpoint opinions with their arithmetic mean; a nonreceptive selected edge leaves the configuration unchanged. Assume \(|x_1-x_2|<c\) and \(|x_2-x_3|<c\) at time zero. Consensus means all three opinions tend to one common value. The diameter is the maximum minus the minimum of the three opinions, and time zero precedes the first selected edge.

The unordered edge probabilities are
\[
p=\frac{u}{u+z},\qquad q=\frac{z}{u+z}.
\]
The cancellation of middle activity weight \(v\) is a baseline bipartite selection identity; it is not claimed to be a new theorem.

## Proof

Write \(W=u+v+z\). Edge \(12\) is selected either by choosing leaf \(1\), with probability \(u/W\), or by choosing the center and then leaf \(1\), with probability \((v/W)(u/(u+z))\). Their sum is \(u/(u+z)\); the complementary edge has probability \(z/(u+z)\). Positive weights make both edge probabilities strictly positive.

The first selected edge is receptive by assumption. If it is \(12\), the state becomes \((a,a,b)\), with \(a=(x_1+x_2)/2\) and \(b=x_3\). Its diameter is \(D_{12}=|b-a|\). If \(D_{12}\ge c\), the edge \(23\) is forever ineligible and edge \(12\) averages two already equal numbers; the state is frozen, with distinct final clusters because \(c>0\). If \(D_{12}<c\), both edge gaps are below \(c\). Every subsequent update uses only convex combinations of current opinions, so the diameter cannot increase, and both edges stay receptive. The same argument applies symmetrically when the first edge is \(23\), yielding the probability formula because each edge occurs initially with its assigned probability.

After any successful averaging event the two endpoints of the most recently selected edge have identical opinions. Repeating that edge changes nothing. Selecting the other edge replaces its differing endpoint and the common middle value with their mean, exactly halving the diameter, with the last-selected edge now the one whose endpoints agree. Induction yields \(D_n=D_j2^{-K_n}\). The indicator of an edge switch has expectation \(2pq\) and depends on at most two adjacent independent edge draws. Splitting its sequence by even and odd indices proves a strong law, \(K_n/n\to2pq\) almost surely. Thus \(K_n\to\infty\), the successful branch converges to consensus, and its nonzero-diameter logarithmic contraction exponent is exactly \(2pq\log 2\). If \(D_j=0\), consensus occurs at the first step and there is no nontrivial logarithmic exponent.

Conditional on the initial edge \(12\), each new edge switch requires an independent geometric number of selections, with success probability \(q\) for the first switch, \(p\) for the next, then alternating. Strict diameter tolerance \(\delta\) requires exactly \(m\) switches. Summing their means produces \(1+\lceil m/2\rceil/q+\lfloor m/2\rfloor/p\). The other branch interchanges \(p,q\). For \(m\ge2\), both coefficients are positive, so the Cauchy–Schwarz inequality \(A/p+B/(1-p)\ge(\sqrt A+\sqrt B)^2\), with \(A=\lceil m/2\rceil\) and \(B=\lfloor m/2\rfloor\), gives the unique optimum and exact minimum. For \(m=1\), the appropriate endpoint gives only an unattained infimum over strictly positive activities; no interior optimizer is claimed.

For \((0,2/5,1)\) and \(c=3/4\), the first \(12\) update gives \((1/5,1/5,1)\) with \(D_{12}=4/5\ge3/4\), while first \(23\) yields \((0,7/10,7/10)\) with \(D_{23}=7/10<3/4\). Thus consensus has probability \(q\). The strict tolerance \(\delta=1/10\) requires three switches because \((7/10)/4\ge1/10\) but \((7/10)/8<1/10\). Consequently the conditional expected time is \(1+2/p+1/q\), minimized as stated by the equality case of Cauchy–Schwarz.

## Verification

The included standalone `verify.py` uses Python's `fractions.Fraction`. It checks exact edge-sampling probabilities over 125 positive-weight triples and exhaustively verifies frozen or geometric-diameter behavior for all qualifying initial opinion triples from a seven-point rational grid, five rational confidence bounds, both initial edge choices, and every subsequent binary edge word of length at most eight. It also checks the geometric-wait formulas for six rational edge probabilities, two initial edges and nine target switch counts, and checks the sharp opinion/configuration witness. On execution it reports `PASS 988640 exact-rational assertions`. These finite checks are corroboration; the theorem for arbitrary real opinions, weights and tolerances follows from the analytical argument above.

## Relationship to prior work

Li and Porter introduced the specific activity-weighted agent-pair selection rule and studied consensus, fragmentation and convergence time numerically across larger networks. The edge-probability cancellation is a standard consequence of that rule on a bipartite star, rather than the new contribution. Chen, Su, Mei and Bullo established broad convergence properties for heterogeneous Deffuant–Weisbuch dynamics. Earlier convergence-rate work supplies estimates for other asynchronous bounded-confidence models. The narrower claim here is the **exact joint law of stochastic initial consensus success and conditional time-to-tolerance**, including a sharp activity-allocation optimum and an explicit nontrivial reliability–latency curve. Searches and inspected primary text did not identify a direct published equivalent, but absence from these sources does not establish publication priority.

## Limitations

This is an exact three-vertex path result, not a claim for larger social networks. It assumes synchronous pair compromise within one selected edge, compromise fraction \(1/2\), fixed strictly positive node weights, strict confidence inequalities, and two initially receptive edges. It does not assert that center-weight cancellation or the qualitative possibility of confidence fragmentation is new. Conditional convergence time diverges as an edge-selection probability tends to zero; endpoints are excluded. The result does not claim independent verification or priority against every paper in the opinion-dynamics and stochastic-gossip literature.

## References

1. Grace J. Li and Mason A. Porter, *A Bounded-Confidence Model of Opinion Dynamics with Heterogeneous Node-Activity Levels*, arXiv:2206.09490, first posted 2022-06-19, https://arxiv.org/abs/2206.09490.
2. Wei Su, Ge Chen, Wenjun Mei and Francesco Bullo, *Convergence of the Heterogeneous Deffuant–Weisbuch Model: A Complete Proof and Some Extensions*, arXiv:2409.01593, first posted 2024-09-03, https://arxiv.org/abs/2409.01593.
3. Jiangbo Zhang and Ge Chen, *Convergence Rate of the Asymmetric Deffuant–Weisbuch Dynamics*, Journal of Systems Science and Complexity 28 (2015), 773–787, https://doi.org/10.1007/s11424-015-3240-z.
