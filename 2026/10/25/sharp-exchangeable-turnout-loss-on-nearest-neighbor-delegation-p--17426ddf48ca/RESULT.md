# Sharp exchangeable-turnout loss on nearest-neighbor delegation paths

## Finding
Let \(n\ge 2\) voters be arranged on the labeled path \(1,2,\ldots,n\). Each voter may name herself or an immediate path neighbor as her default delegate. For each election the set \(A\) of nonvoters is distributed **exchangeably**: its law is invariant under every permutation of the voters. A voter who casts a ballot suspends her default delegation. A nonvoter's weight follows default delegations until it reaches a casting voter, or is lost if it encounters an all-nonvoting directed cycle or self-loop. There are no backup ballots or additional delegates.

For \(0\le s\le n\), define \(a_s=\Pr(S\subseteq A)\) for any fixed set \(S\) of \(s\) distinct voters. The definition is independent of the choice of \(S\) by exchangeability, and \(1=a_0\ge a_1\ge\cdots\ge a_n\ge 0\). For every exchangeable law, the **minimum expected number of lost votes** over all nearest-neighbor/self default-delegation profiles is exactly
\[
\boxed{L_n=2a_2+\sum_{s=3}^{n}a_s.}
\]
An optimizer is the terminal reciprocal delegation \(1\leftrightarrow 2\), with every voter \(i\ge3\) delegating to \(i-1\); its path reversal is also optimal. For i.i.d. abstention probability \(q\in(0,1)\), these terminal-pair profiles are the **only** minimizers (identical when \(n=2\)), and
\[
L_n(q)=2q^2+\frac{q^3(1-q^{n-2})}{1-q}.
\]
Without the neighbor restriction, the exact minimum is \(n a_n\), attained by one directed cycle through all voters. Thus the **exact locality penalty** is \(2a_2+\sum_{s=3}^{n}a_s-na_n\). Under independent abstention with fixed \(0<q<1\), this penalty converges as \(n\to\infty\) to \(q^2(2-q)/(1-q)\).

## Assumptions and scope
All weights are one; the objective is the expected total unrepresented weight, not an equilibrium utility or a power-centrality index. A default profile is a deterministic function \(d:\{1,\ldots,n\}\to\{1,\ldots,n\}\) satisfying \(|d(i)-i|\le1\). Self-nomination is allowed. The profile is fixed before the turnout set is observed. The turnout distribution can have arbitrary dependence as long as it is permutation-exchangeable; no independence, positive turnout, or continuous distribution is assumed. Each voter's own ballot, if cast, counts even if her default delegates to somebody else. A ballot that reaches a voter who cast a ballot stops there.

For a fixed-count model with exactly \(t\) uniformly selected nonvoters, the theorem applies with \(a_s=\binom{t}{s}/\binom{n}{s}\) for \(s\le t\), and \(a_s=0\) otherwise. The empty sum is zero when \(n=2\).

## Proof
**1. A path-to-cycle loss identity.** For each voter \(v\), follow \(d\) from \(v\) until the first repeated vertex. Let \(O_v\) be the set of distinct voters visited. The ballot of \(v\) is lost if and only if every member of \(O_v\) abstains: any voter in the chain who casts a ballot terminates its delegation, while no casting voter means that the terminal directed cycle remains closed. Consequently
\[
\mathbb E[\#\text{ lost votes}]=\sum_{v=1}^{n}a_{|O_v|}.
\]
Every weakly connected component of the functional delegation graph on a path is an interval. Its unique directed cycle is either a self-loop or a reciprocal pair of adjacent vertices. If the cycle contains \(k\in\{1,2\}\) vertices, a voter at graph distance \(r\) from that cycle has \(|O_v|=k+r\).

**2. Shift each component's cycle to an endpoint.** Consider a component with \(m\) vertices. For a reciprocal pair at positions \(j,j+1\) within that interval, the component loss is
\[
2a_2+\sum_{r=1}^{j-1}a_{r+2}+\sum_{r=1}^{m-j-1}a_{r+2}.
\]
For a self-loop at position \(j\), it is
\[
a_1+\sum_{r=1}^{j-1}a_{r+1}+\sum_{r=1}^{m-j}a_{r+1}.
\]
The partial sums of either decreasing sequence \((a_{r+2})\) or \((a_{r+1})\) are discrete concave functions of their length. With fixed left-plus-right length, the displayed sums attain their minimum when one side has length zero. Therefore the best component loss for a reciprocal pair is
\[
H_2(m)=2a_2+\sum_{s=3}^{m}a_s\qquad(m\ge2),
\]
and the best possible self-loop loss is
\[
H_1(m)=\sum_{s=1}^{m}a_s\qquad(m\ge1).
\]
For \(m\ge2\), \(H_1(m)-H_2(m)=a_1-a_2\ge0\); a reciprocal terminal pair is never worse than a self-loop. For a singleton, the loss is \(a_1\).

**3. Merge intervals.** Define \(h(1)=a_1\) and \(h(m)=H_2(m)\) for \(m\ge2\). This function is subadditive for positive integer arguments with total at most \(n\). For \(u,v\ge2\), compare the \(v\) summands in
\[
h(u+v)-h(u)=\sum_{s=u+1}^{u+v}a_s
\]
term by term with those in \(h(v)=a_2+a_2+a_3+\cdots+a_v\). The \(s\)-indices on the left are no smaller than the corresponding indices on the right, so \(h(u+v)\le h(u)+h(v)\). If \(u=1\), \(v\ge2\), then \(h(v+1)-h(v)=a_{v+1}\le a_1=h(1)\). Finally, \(h(2)=2a_2\le2a_1=2h(1)\).

Every delegation profile partitions the path into consecutive components with lengths summing to \(n\). Steps 1--2 lower-bound its expected loss by the sum of their \(h\)-values; subadditivity then gives \(\mathbb E[\#\mathrm{lost}]\ge h(n)=L_n\). A terminal reciprocal pair with every remaining arrow pointing toward it attains that value. This proves the exchangeable optimum.

**4. Strictness under i.i.d. turnout and unrestricted comparison.** For \(a_s=q^s\) with \(0<q<1\), every merger of two components is strictly improving in the comparison above, and \(H_1(m)>H_2(m)\). The partial-sum concavity is strict away from the endpoint minimizers, leaving only reciprocal pairs at the two ends of the full path. Without any edge restrictions, the event that all voters abstain forces the loss of all \(n\) votes under every profile, hence the expected loss is at least \(n a_n\). A directed Hamiltonian default cycle loses votes only on that event, proving the unrestricted bound. Substituting \(a_s=q^s\) and summing the geometric tail proves the stated exact formula and its limit. \(\square\)

## Verification
The standalone script `checks/verify.py` uses only the Python standard library. It enumerates every allowed neighbor/self delegation profile for \(2\le n\le9\), tests all fixed-count exchangeable turnout laws for each \(n\), and compares exact rational losses with the formula. It also explicitly enumerates turnout subsets for \(n\le6\) to check the orbit-loss identity, and enumerates all optimal profiles for i.i.d. \(q=1/2\). Run `python3 checks/verify.py` from the directory containing this file. Passing finite checks corroborates the proof; the all-\(n\) and arbitrary-exchangeable statements follow from Steps 1--4, not from enumeration.

## Relationship to prior work
Brill et al., *Cycles in Liquid Democracy: A Game-Theoretic Justification*, introduce probabilistic default delegations and show in their extended paper (Appendix B.4, Proposition 19) that an unrestricted cycle through all voters minimizes lost voting weight. That theorem permits long-distance delegation edges. The present statement concerns a fixed social **path** with only immediate-neighbor delegations, permits arbitrary exchangeable correlation in turnout, and identifies an exact irreducible locality penalty and all independent-turnout minimizers; these do not follow by substituting a parameter into the unrestricted result. Grossi and Nitsche examine exponentially decaying expected voting influence along chains and suspendible cycles, but do not establish this path-constrained loss optimum. Li and Pournaras consider a different model with ranked backup delegates and personal fallback ballots. Grossi et al. analyze centrality and representative selection rather than minimizing lost voting weight on a prescribed path.

## Limitations
The theorem optimizes expected number of votes represented, without modeling preference compatibility, strategic incentives, or voting accuracy. It does not assert a Nash equilibrium. It does not extend to arbitrary heterogeneous or adversarially correlated turnout lacking exchangeability: for independent abstention probabilities \((0.9,0.1,0.1,0.9)\) on four voters, a central pair can outperform either terminal pair. The i.i.d. uniqueness statement excludes the degenerate endpoints \(q=0\) and \(q=1\), when ties occur. The cited recent centrality paper's complete text was not accessible at the time of comparison, so an unrecognized equivalent statement remains a publication-priority risk. None of the calculations constitutes independent verification.

## References
1. M. Brill, R. Colley, A.-M. George, G. Lisowski, G. Papasotiropoulos, U. Schmidt-Kraepelin. *Cycles in Liquid Democracy: A Game-Theoretic Justification*. COMSOC 2025, workshop paper 49; expanded version arXiv:2607.12610 (2026), particularly §2 and Appendix B.4.
2. D. Grossi and A. Nitsche. *Delegations as Adaptive Representation Patterns: Rethinking Influence in Liquid Democracy*. arXiv:2506.09789 (2025), §3 and Appendix B.
3. Z. Li and E. Pournaras. *Resilient Liquid Democracy: Mitigating Voting Power Imbalances via Secure Delegation Networks*. arXiv:2607.01730 (2026).
4. D. Grossi, A. Nitsche, G. Papasotiropoulos, O. Skibski, P. Skowron, T. Wąs. *Power in Liquid Democracy: A Network Centrality Approach*. arXiv:2608.13188 (2026).
