# One-quarter oscillation basins and a parity fracture in complete split-graph majority dynamics

## Finding

Let \(G_n=K_n\vee\overline{K}_n\), with \(n\ge 1\), be the labelled complete split graph formed from an \(n\)-vertex clique \(C\), an \(n\)-vertex independent set \(I\), and every edge between them. Under synchronous binary strict-neighbor majority with tie retention, write \(F_n\) for the global update. Then, for every \(n\ge1\),

\[
F_n^4=F_n^2.
\]

There are exactly two fixed configurations. The number \(N_2(n)\) of **distinct primitive two-cycle orbits**, not individual periodic configurations, is

\[
N_2(n)=\begin{cases}
1+\frac12\binom{n}{n/2}^{\!2},& n\text{ even},\\[2mm]
1,&n\text{ odd}.
\end{cases}
\]

Let \(B_n\) be the number of labelled initial configurations eventually entering a primitive two-cycle, whether or not already periodic. Put

\[
A_n=\sum_{0\le c<n/2}\binom nc,\qquad
Q_n=\sum_{0\le c<n/2}\binom nc^2.
\]

Then the exact attraction-basin count is

\[
B_n=\binom{2n}{n}+A_n^2-Q_n.
\]

Equivalently, if \(n\) is odd,

\[
B_n=4^{n-1}+\frac12\binom{2n}{n},
\]

whereas if \(n\) is even, with \(H_n=\binom{n}{n/2}\),

\[
B_n=4^{n-1}-2^{n-1}H_n+\frac34H_n^2+\frac12\binom{2n}{n}.
\]

For independent unbiased initial vertex states, the probability \(p_n=B_n/4^n\) of eventual primitive oscillation satisfies

\[
p_n=\begin{cases}
\displaystyle \frac14+\frac1{2\sqrt{\pi n}}+O(n^{-3/2}),&n\text{ odd},\\[3mm]
\displaystyle \frac14+\frac{1-\sqrt 2}{2\sqrt{\pi n}}+\frac{3}{2\pi n}+O(n^{-3/2}),&n\text{ even}.
\end{cases}
\]

Thus the two parities have the **same limiting one-quarter oscillation basin** but approach it from opposite sides for all sufficiently large sizes; the number of primitive oscillatory orbits is one at odd sizes and asymptotic to \(4^n/(\pi n)\) at even sizes.

The sharp maximum first-periodic-entry time is \(0\) for \(n=1\), \(1\) for \(n=2\), and \(2\) for every \(n\ge3\).

## Assumptions and scope

All graphs are undirected, simple, labelled and loopless. Each vertex state belongs to \(\{0,1\}\). At each simultaneous update a vertex adopts the strict majority state among its open neighbors; on an exact tie it retains its state. The clique \(C\) and independent side \(I\) each contain exactly \(n\) vertices. Primitive period means the least period of the full labelled configuration, not the period of a population-count summary. A first-periodic-entry time of \(t\) means the state at update \(t\) is on a periodic orbit and no earlier state is periodic.

## Proof

**Exact vertex rule.** Let \(c\) and \(s\) be the numbers of vertices with state \(1\) on \(C\) and \(I\), respectively. A clique vertex with current state \(x\) sees exactly \(c+s-x\) ones among its \(2n-1\) neighbors. Thus its new value is

\[
x'=\begin{cases}
0,&c+s<n,\\
1-x,&c+s=n,\\
1,&c+s>n.
\end{cases}
\]

An independent-side vertex with state \(y\) sees all \(n\) clique vertices, so

\[
y'=\begin{cases}
0,&2c<n,\\
y,&2c=n,\\
1,&2c>n.
\end{cases}
\]

These formulas are exact at the microscopic level, including ties and the cases \(c=0\) and \(c=n\).

**Uniform transient bound and periodic structure.** If \(c+s>n\), the clique becomes all ones immediately. If \(2c>n\), the independent side also becomes all ones (consensus). If \(2c<n\), the update is the alternating pair (all clique ones, all independent zeros). If \(2c=n\), the independent side initially retains its states; the condition \(s>n/2\) forces consensus on the next update. The case \(c+s<n\) is its zero-one complement: immediate consensus when \(2c<n\), immediate entry to the opposite unanimous-shore pair when \(2c>n\), and consensus one update later when \(2c=n\).

If \(c+s=n\), the clique complements every bit. At \(c=0\) or \(c=n\), the state is already one of the two unanimous-opposition configurations, which exchange with each other at every update. If \(0<c<n\) and \(2c<n\), the next state has \(n-c\) clique ones and zero independent ones; because \(0<n-c<n\) and \(2(n-c)>n\), one further update reaches the unanimous-opposition pair. The complementary conclusion holds when \(0<c<n\) and \(2c>n\). Finally, \(2c=n\) is possible only for even \(n\); now \(s=n/2\), the independent bits remain fixed, and all clique bits complement at each update. This is genuinely primitive period two because the clique contains both colors.

These cases exhaust every initial state and prove \(F_n^4=F_n^2\). They show that precisely two states are fixed (the two global consensuses), that the unanimous-opposition configurations form one primitive two-cycle, and that for even \(n\) all configurations with \(c=s=n/2\) form primitive two-cycles. No other periodic states exist. There are \(\binom{n}{n/2}^2\) balanced labelled configurations, paired by a fixed-point-free clique complementation. This proves the formula for \(N_2(n)\).

The uniform bound \(2\) is attained for \(n\ge3\) by a configuration with \(c=1\), \(s=n-1\), which first reaches the unanimous-opposition orbit after exactly two updates. For \(n=2\), one clique one and no independent ones first reaches global consensus after one update. For \(n=1\), all four states are initially periodic. This gives the sharp entry-time claims.

**Complete two-cycle attraction basin.** The case analysis gives the exact if-and-only-if condition

\[
(c+s=n)\quad\text{or}\quad(c+s>n\ \text{and}\ 2c<n)
\quad\text{or}\quad(c+s<n\ \text{and}\ 2c>n).
\]

Each population pair \((c,s)\) represents \(\binom nc\binom ns\) labelled states. The middle and final regions contribute equally by complementing all states. In the middle region substitute \(j=n-s\), so \(0\le j<c<n/2\). Vandermonde's identity and the identity

\[
2\sum_{0\le j<c<n/2}\binom nc\binom nj
=\left(\sum_{0\le c<n/2}\binom nc\right)^2
-\sum_{0\le c<n/2}\binom nc^2
\]

prove \(B_n=\binom{2n}{n}+A_n^2-Q_n\). For odd \(n\), binomial symmetry yields \(A_n=2^{n-1}\) and \(Q_n=\tfrac12\binom{2n}{n}\). For even \(n\), the central term contributes \(H_n\), giving \(A_n=(2^n-H_n)/2\) and \(Q_n=(\binom{2n}{n}-H_n^2)/2\). Substitution gives the two closed formulas.

**Asymptotic parity fracture.** Stirling's formula supplies

\[
\frac{\binom{2n}{n}}{4^n}=\frac1{\sqrt{\pi n}}+O(n^{-3/2}),\qquad
\frac{\binom{n}{n/2}}{2^n}=\sqrt{\frac{2}{\pi n}}+O(n^{-3/2})
\quad(n\text{ even}).
\]

Substitution yields both probability expansions, including the order \(n^{-1}\) term for even \(n\). For even \(n\), \(N_2(n)=1+\tfrac12H_n^2\sim4^n/(\pi n)\); for odd \(n\), \(N_2(n)=1\) identically.

## Verification

The standalone standard-library script `verify_split_majority.py` uses explicit neighbor lists rather than the proof's population rules for all \(349{,}524\) labelled configurations with \(1\le n\le9\). It checks the global iterate identity, primitive two-cycle counts, complete attraction basins and sharp transient bounds. A second count-level implementation independently checks the combinatorial formulas for every \(1\le n\le150\). Run `python3 verify_split_majority.py`; the expected final marker is `SPLIT_MAJORITY_VERIFY_OK`. The file `verification_output.txt` contains the recorded output. The infinite-size conclusion follows from the proof above, not from exhaustive tests at finite sizes.

## Relationship to prior work

The classical Goles--Olivos finite-graph threshold result establishes eventual period at most two but does not, in its accessible summary, furnish the present exact graph-family orbit and basin enumerations. Tamuz--Tessler (first publicly posted 15 July 2013) develops general synchronous-majority structural results and information-retention criteria; Benjamini et al. (first publicly posted 11 May 2014) investigates period-two behavior on infinite graphs and consensus on random graphs. Their examined full texts address different graph families and conclusions. Existing parity-update automata have a different linear XOR rule rather than strict majority. The present assertion concerns the new parity-dependent exact counts and limiting one-quarter basin, not the previously known general period-at-most-two fact.

## Limitations

The theorem concerns balanced complete split graphs, synchronous binary opinions and deterministic tie retention; it does not address unequal clique/independent sizes, asynchronous updates or noisy tie breaking. It does not assert uniqueness across unindexed historical literature. Full text of the short 1980 Goles--Olivos primary article was not accessible through the sources available for this comparison; its abstract supports only the general period-two statement, so the historical overlap risk is retained. The computational evidence is finite and is not offered as proof of infinite-size classification.

## References

1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first submitted 2013-07-15. https://arxiv.org/abs/1307.4035
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486, first submitted 2014-05-11. https://arxiv.org/abs/1405.2486
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187--189. https://doi.org/10.1016/0012-365X(80)90121-1
