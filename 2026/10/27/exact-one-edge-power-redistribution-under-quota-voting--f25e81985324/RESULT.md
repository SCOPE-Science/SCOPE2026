# Exact one-edge power redistribution under quota voting

## Finding

Consider an odd electorate with \(n=2m+1\) voters and a quota that passes a proposal exactly when at least \(r=m+1+s\) final votes are affirmative, where \(s\in\{0,1,\ldots,m\}\). Each voter independently chooses uniformly among voting yes, voting no, and delegating to each out-neighbor. Begin with no delegation edges and add one edge \(a\to b\). Let \(M_i\) be voter \(i\)'s unnormalized criticality probability: the probability, over the other voters' random actions, that replacing \(i\)'s direct no vote by a direct yes vote changes the quota outcome. Define

\[
B_{n,r}=\frac{\binom{n-1}{r-1}}{2^{n-1}},\qquad
R_{n,r}=\frac{2\left[\binom{n-3}{r-1}+\binom{n-3}{r-3}\right]}{\binom{n-1}{r-1}}.
\]

Use the convention \(\binom{u}{v}=0\) when \(v<0\) or \(v>u\). The exact criticalities after the edge is added are

\[
M_a=B_{n,r},\qquad M_b=\frac43 B_{n,r},\qquad
M_c=B_{n,r}\left(\frac23+\frac{R_{n,r}}3\right)
\quad(c\notin\{a,b\}).
\]

Moreover, with \(s=r-(m+1)\),

\[
R_{n,r}=\frac{n-3}{n-2}+\frac{2s^2}{m(n-2)},
\qquad
\sum_{i=1}^{n}M_i=nB_{n,r}+\frac{2s^2}{3m}B_{n,r}.
\]

Thus a single delegation option conserves total unnormalized criticality exactly at simple majority (\(s=0\)) and strictly increases it for every stricter quota (\(s>0\)). The delegator's criticality stays at baseline; the recipient gains a fixed one-third of baseline criticality; the other voters' changes depend explicitly on the quota distance from simple majority.

## Assumptions and scope

The delegation graph has exactly one edge, from \(a\) to \(b\), so it is acyclic and no voter abstains because of a delegation cycle. All voters have unit weight. Every direct vote is independently yes or no with probability \(1/2\); when a voter has one out-neighbor, the three actions (yes, no, delegate) each have probability \(1/3\). The quota is the integer threshold \(r\), with \(m+1\le r\le n\). Criticality is evaluated by forcing the tested voter to vote directly either way, while all other voters follow the stated random-action model. The result concerns the unnormalized probability measure, not a claim that normalized power sums are conserved for all quotas.

## Proof

With no delegation edges, the tested voter is pivotal precisely when exactly \(r-1\) of the other \(n-1\) independent fair votes are affirmative. Hence every voter's baseline criticality is \(B_{n,r}\).

After adding \(a\to b\), testing voter \(a\) still forces its vote directly, and no other voter delegates to \(a\); thus \(M_a=B_{n,r}\).

For voter \(b\), with probability \(2/3\), voter \(a\) votes directly, so the usual pivotal probability is \(B_{n,r}\). With probability \(1/3\), voter \(a\) delegates to \(b\), and changing \(b\)'s vote changes two final votes together. Among the other \(n-2\) voters, the number of affirmative votes must be either \(r-2\) or \(r-1\). This event has probability

\[
\frac{\binom{n-2}{r-2}+\binom{n-2}{r-1}}{2^{n-2}}
=\frac{2\binom{n-1}{r-1}}{2^{n-1}}=2B_{n,r},
\]

by Pascal's identity. Therefore \(M_b=(2/3)B_{n,r}+(1/3)(2B_{n,r})=4B_{n,r}/3\).

Fix an outsider \(c\notin\{a,b\}\). If \(a\) votes directly (probability \(2/3\)), the other votes are independent fair votes and \(c\)'s criticality probability is \(B_{n,r}\). If \(a\) delegates to \(b\) (probability \(1/3\)), the pair \(a,b\) contributes either zero or two affirmative votes, each with probability \(1/2\). The remaining \(n-3\) voters must contribute either \(r-1\) affirmative votes or \(r-3\) affirmative votes. Thus this conditional pivotal probability is

\[
Q_{n,r}=\frac{\binom{n-3}{r-1}+\binom{n-3}{r-3}}{2^{n-2}}=B_{n,r}R_{n,r},
\]

which gives the stated formula for \(M_c\).

To simplify \(R_{n,r}\), use

\[
\frac{\binom{n-3}{r-1}}{\binom{n-1}{r-1}}=\frac{(n-r)(n-r-1)}{(n-1)(n-2)},\qquad
\frac{\binom{n-3}{r-3}}{\binom{n-1}{r-1}}=\frac{(r-1)(r-2)}{(n-1)(n-2)}.
\]

Substituting \(n=2m+1\) and \(r=m+1+s\), the numerator sum becomes \(2m(m-1)+2s^2\), which yields

\[
R_{n,r}=\frac{2(m-1)}{2m-1}+\frac{2s^2}{m(2m-1)}
=\frac{n-3}{n-2}+\frac{2s^2}{m(n-2)}.
\]

Finally,

\[
\begin{aligned}
\sum_i M_i
&=B_{n,r}+\frac43B_{n,r}+(n-2)B_{n,r}\left(\frac23+\frac{R_{n,r}}3\right)\\
&=B_{n,r}\left(n+\frac{2s^2}{3m}\right).
\end{aligned}
\]

Since \(m\ge1\), the excess over the no-edge total \(nB_{n,r}\) is zero exactly when \(s=0\), and is positive for every \(s>0\). This proves the claim.

## Verification

The accompanying standard-library script `verify.py` enumerates every action profile of the one-edge graph for odd electorate sizes \(n\in\{3,5,7,9,11\}\) and every threshold \(r>n/2\). It compares the exact rational criticality probabilities with the formulas above and checks the total-power identity. The run completed with the output:

`VERIFY_OK: 20 exact quota/electorate cases; n=3,5,7,9,11; all thresholds r>n/2; exact enumeration matches closed forms and total-power law`

The proof above is analytic; the finite enumeration is a reproducibility check, not a substitute for the proof.

## Relationship to prior work

Colley, Delemazure, and Gilbert introduce the a-priori LD Penrose–Banzhaf measure using the same uniform choice model and show how delegation options alter criticality. Their paper gives tractable formulas for complete bipartite proxy-voting graphs and complete delegation graphs, plus numerical examples, but does not state the closed-form power vector or the quota-dependent total-criticality law for a graph with exactly one allowed delegation edge. The one-edge graph here is not their complete-bipartite proxy graph: the sole delegator has only one permitted proxy, while the other voters have no outgoing edges.

Zhang and Grossi study the delegative Banzhaf index for a fixed delegation profile and power-seeking behavior; D'Angelo, Delfaraz, and Gilbert study Banzhaf and Shapley–Shubik values in delegative simple games and graph-change bribery. These use different power constructions from the a-priori random-action measure used here. Berinsky and coauthors study random delegation effects on truth-tracking accuracy and component sizes, not this quota-pivotality statistic. The exact theorem is a restricted closed-form analysis of the Colley–Delemazure–Gilbert measure; the broad model is prior art and is not claimed as new.

## Limitations

The result is limited to unit weights, an odd electorate, a deterministic integer quota, independent uniform choices, and a single acyclic delegation edge. It does not prove monotonicity for arbitrary graph edits, weighted electorates, even electorate sizes, correlated choices, abstention cycles, or strategic delegation. The measure is unnormalized; for stricter quotas the increase in its sum is not itself a statement about welfare, accuracy, fairness, or a normalized index. The general index framework is prior art, and the contribution is the explicit one-edge formula and its conservation boundary, not a new definition of voting power.

## References

1. R. Colley, T. Delemazure, and H. Gilbert, “Measuring a Priori Voting Power in Liquid Democracy,” *Proceedings of IJCAI 2023*, 2607–2615. First public preprint: 2023-01-06. arXiv:2301.02462; DOI: 10.24963/ijcai.2023/290. https://arxiv.org/abs/2301.02462
2. Y. Zhang and D. Grossi, “Power in Liquid Democracy,” *Proceedings of AAAI 2021*, 5822–5830. First public: 2021-05-18. DOI: 10.1609/aaai.v35i6.16729. https://doi.org/10.1609/aaai.v35i6.16729
3. G. D’Angelo, E. Delfaraz, and H. Gilbert, “Computation and Bribery of Voting Power in Delegative Simple Games,” arXiv:2104.03692, first public 2021-04-08. https://arxiv.org/abs/2104.03692
4. A. J. Berinsky et al., “Tracking Truth with Liquid Democracy,” arXiv:2107.11868, first public 2021-07-25. https://arxiv.org/abs/2107.11868
