# A unique Shapley–Banzhaf allocation reversal from parallel-path redundancy

## Finding

For every pair of integers \(2\le a<b\), an edge-connectivity cooperative game consisting of \(m\ge1\) internally disjoint source–sink paths of length \(a\) and one path of length \(b\) exhibits a unique transition in the relative aggregate reward assigned to the long path by the Shapley–Shubik and normalized Banzhaf indices as the number \(m\) of short alternatives grows. Define the two long-path shares by

\[
S_m=\prod_{k=1}^{m}\frac{ka}{ka+b},\qquad
B_m=\frac{b(2^a-1)}{ma(2^b-1)+b(2^a-1)}.
\]

Then \(S_1>B_1\), the ratio \(R_m=S_m/B_m\) is a unimodal sequence, and \(R_m\to0\). Thus there is exactly one boundary between the strictly \(S_m>B_m\) and strictly \(S_m<B_m\) regimes; at most one integer value of \(m\) can be a tie at that boundary. The tie possibility is real: when \((a,b,m)=(2,4,2)\), both long-path shares equal \(1/6\).

The smallest simple-network change flipping the comparison is the addition of one length-two alternate path to a length-two/length-three pair. Initially

\[
(S_1,B_1)=\left(\frac25,\frac9{23}\right),
\]

while after adding the second short path

\[
(S_2,B_2)=\left(\frac8{35},\frac9{37}\right).
\]

The resulting second network has exactly seven edges. The two indices agree that each short-path *individual edge* is more pivotal than a long-path edge; the finding instead concerns how the **aggregate share of an entire physical path** is divided between index conventions.

## Assumptions and scope

Let \(a,b,m\) be integers with \(2\le a<b\) and \(m\ge1\). Form an undirected simple graph from two distinguished vertices \(s,t\), \(m\) internally vertex-disjoint paths each containing exactly \(a\) edges, and one additional internally vertex-disjoint path containing exactly \(b\) edges. There are no other edges. Every edge belongs to a distinct player. A coalition wins if and only if its edges contain a complete \(s\)-to-\(t\) path. All edges are held by players; endpoints are not players.

A Shapley–Shubik index is the probability that an edge first makes a random-order coalition winning; each edge permutation is equally likely. An unnormalized Banzhaf index is the probability that an edge is pivotal when every *other* edge is included in a coalition independently with probability \(1/2\). Normalize Banzhaf indices by dividing each by their strictly positive sum over all edges. An aggregate path share sums its constituent edge indices; these sums differ from assigning one player to an entire path.

## Proof

**1. Formula for the Shapley–Shubik long-path share.** Give each edge an independent uniform \([0,1]\) arrival time. These times induce a uniformly random edge order. Fix an edge of the long path and condition on its arrival time \(x\). It is pivotal exactly when all other \(b-1\) long-path edges arrived by \(x\) and no one of the \(m\) short paths is complete by \(x\). Independence gives \(x^{b-1}(1-x^a)^m\). Summing over the \(b\) long-path edges,

\[
S_m=b\int_0^1x^{b-1}(1-x^a)^m\,dx
=\frac{\Gamma(1+b/a)\Gamma(m+1)}{\Gamma(1+b/a+m)}
=\prod_{k=1}^m\frac{ka}{ka+b}.
\]

**2. Formula for normalized Banzhaf share.** The Banzhaf pivot probability of each long-path edge is \(2^{-(b-1)}(1-2^{-a})^m\). The pivot probability of each short-path edge is \(2^{-(a-1)}(1-2^{-a})^{m-1}(1-2^{-b})\). Summing the \(b\) and \(ma\) corresponding indices and normalizing yields

\[
B_m=\frac{b(2^a-1)}{ma(2^b-1)+b(2^a-1)}.
\]

**3. Individual edge ordering.** For fixed \(x\in(0,1)\), the arrival-time pivotal integrand of a tagged short edge differs from that of a tagged long edge by

\[
x^{a-1}(1-x^a)^{m-1}(1-x^{b-a})>0.
\]

The Banzhaf short-to-long edge-pivot ratio equals \((2^b-1)/(2^a-1)>1\). Thus both indices favor every short-path edge individually, even in parameter regimes where their *aggregate* long-path shares have opposite relative comparisons.

**4. Initial strict comparison.** Put \(A=b/a>1\) and \(T=a(2^b-1)/[b(2^a-1)]>0\), so \(B_m=(1+mT)^{-1}\). Then

\[
R_m=\frac{S_m}{B_m}=(1+mT)\prod_{k=1}^{m}\frac{k}{k+A},
\qquad R_1=\frac{1+T}{1+A}.
\]

For integers \(n\ge2\), the sequence \((2^n-1)/n^2\) strictly increases: its consecutive numerator difference after clearing positive denominators is

\[
(n^2-2n-1)2^n+2n+1>0.
\]

For \(n=2\) this expression is \(1\); for \(n\ge3\) both terms are positive. Hence \(T>A\), equivalently \(a^2(2^b-1)>b^2(2^a-1)\), giving \(R_1>1\).

**5. One-crossing and asymptotics.** Direct division shows

\[
\frac{R_{m+1}}{R_m}
=\frac{m+1}{m+1+A}\frac{1+(m+1)T}{1+mT}.
\]

The ratio is greater than, equal to, or less than \(1\) exactly as \(A-T+(A-1)mT\) is negative, zero, or positive. This affine expression increases strictly with \(m\). Thus \(R_m\) can first increase (possibly with one flat step) and then must decrease strictly. Because \(R_1>1\), its possible initial increase or plateau lies entirely above \(1\). Finally, by the gamma ratio asymptotic, \(S_m=\Gamma(1+A)m^{-A}(1+o(1))\) and therefore

\[
R_m=\Gamma(1+A)T\,m^{1-A}(1+o(1))\longrightarrow0.
\]

Let \(m_*=\min\{m\ge1:R_m\le1\}\), which exists. Before \(m_*\), \(R_m>1\); after \(m_*\), \(R_m<1\). At \(m_*\) either \(R_{m_*}=1\) (one tie) or \(R_{m_*}<1\). No return crossing is possible.

**6. Smallest witness.** A reversal cannot occur with \(m=1\) alone. Among simple networks of this type after adding an alternative short path, \(m\ge2\), \(a\ge2\), and \(b\ge a+1\) imply at least \(2a+b\ge7\) edges. Equality forces \(m=2,a=2,b=3\). The displayed fractions give \(2/5>9/23\) and \(8/35<9/37\), establishing the first reversal at that edge count.

## Verification

The standalone script `verification.py` enumerates every coalition of edges for nine finite networks and computes both power indices directly from their definitions using exact rational arithmetic. It then checks each against the closed formulas, and checks \(12320\) exact ratio comparisons over \(154\) parameter pairs. The generated `verification_certificate.json` reports \(3680\) complete coalitions enumerated and records the example fractions and the exact tie \(S_2=B_2=1/6\) for \((a,b)=(2,4)\). Reproduce with `python3 verification.py` and compare its standard output with `verification_certificate.json`. The all-parameter result does not depend on finite enumeration; it follows from Parts 1–6 of the proof.

## Relationship to prior work

Bachrach and Rosenschein (2007) introduced and analyzed the Banzhaf index in edge-controlled network flow and connectivity games, including a tractability result on restricted networks. Elkind, Goldberg, Goldberg, and Wooldridge (2008), especially their Section 4.2 and Theorem 11, gave polynomial-time computation of both Shapley and Banzhaf values for connectivity games on series–parallel networks, which includes this family. These computation results are prior art and are not claimed here. Bachrach, Porat, and Rosenschein (2013) investigated a different, vertex-controlled connectivity game; this confirms the network-reliability motivation of power-index reward allocation but does not supply the edge-path comparison.

The present assertion concerns the sign and uniqueness of the **relative path-level allocation gap under adding parallel alternatives**. It does not assert a new index definition or general algorithm. A broader prior comparative-statics theorem for read-once simple games, if found, might subsume it.

## Limitations

The claim is restricted to simple two-terminal networks consisting of internally disjoint paths of exactly two distinct lengths, one long path and \(m\) equal shorter paths. It concerns a *normalized* Banzhaf index and the aggregate over edges in a path; comparison to a raw Banzhaf index or treating a path as a single player is a different claim. The sequence need not decrease from \(m=1\); unimodality, not global monotonicity, is proved. An integer tie may occur at the unique boundary. No claim of applicability to arbitrary series–parallel graphs, general flow targets, heterogeneous edge reliabilities, or independent external certification is made.

## References

1. Y. Bachrach and J. S. Rosenschein, “Computing the Banzhaf Power Index in Network Flow Games,” AAMAS 2007, DOI `10.1145/1329125.1329433` (conference beginning May 14, 2007).
2. E. Elkind, L. A. Goldberg, P. W. Goldberg, and M. Wooldridge, “A Tractable and Expressive Class of Marginal Contribution Nets and Its Applications,” AAMAS 2008, Section 4.2, full text: https://www.cs.ox.ac.uk/people/paul.goldberg/papers/AAMAS08procs.pdf .
3. Y. Bachrach, E. Porat, and J. S. Rosenschein, “Sharing Rewards in Cooperative Connectivity Games,” *Journal of Artificial Intelligence Research* 47 (2013), 281–311, lawful open text: https://arxiv.org/pdf/1402.0572 .
