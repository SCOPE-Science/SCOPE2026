# A five-vertex threshold for reentrant epidemic-sentinel placement on a path

## Finding

**Theorem (sharp reentrance threshold).** Let \(P_n\) be the path with vertices \(0,\ldots,n-1\), and give its vertices any strictly positive outbreak-source probabilities \(\pi_0,\ldots,\pi_{n-1}\) summing to one. Each edge independently transmits infection with the same probability \(p\in(0,1)\). A single perfect passive sentinel at vertex \(j\) succeeds if infection reaches it from the one randomly selected source. Its detection probability is
\[
 F_j(p)=\sum_{i=0}^{n-1}\pi_i p^{|i-j|}.
\]
Call a vertex *reentrant* if it is the unique maximizer of \(F_j\) at two probabilities \(p_1<p_3\), but is not a maximizer at some intermediate \(p_2\). Such a vertex exists for some strictly positive source law on \(P_n\) **if and only if \(n\ge5\)**. For all \(n\le4\), every vertex-pair detection-probability difference has at most one sign-changing zero on \((0,1)\), so reentrance is impossible.

For \(n=5\), the weights \((6,5,6,1,5)/23\) make vertex \(2\) the unique optimal sentinel for \(p\in(0,\rho_-)\cup(\rho_+,1)\), and vertex \(1\) the unique optimum for \(p\in(\rho_-,\rho_+)\), where
\[
 \rho_\pm=\frac{5\pm\sqrt5}{10}.
\]
Only vertices \(1\) and \(2\) tie at these two transition values. In particular vertex \(2\) is uniquely optimal at \(p=1/5\) and \(p=4/5\), but not at \(p=1/2\).

## Assumptions and scope

The contact network is a finite undirected path. Exactly one source is sampled according to a fixed, strictly positive, otherwise arbitrary probability vector. Edge transmission indicators are independent, and each edge is usable in either direction if open. Eventual reachability, including detection at the initial source, defines success. There are no false alarms, competing infections, recovery-time restrictions, or simultaneous sources. The optimizer ranges over all vertices for each fixed \(p\in(0,1)\). The threshold statement quantifies existentially over source laws but universally over all path sizes below five.

## Proof

**Step 1: infection probability.** The unique path from \(i\) to \(j\) has \(|i-j|\) edges; all must transmit independently for infection to reach \(j\). Conditioning on the source gives the stated \(F_j(p)\).

**Step 2: no reentry through four vertices.** Pad a path having fewer than four vertices on the right with zero-source-weight vertices, which preserves all original \(F_j\). For four vertices use arbitrary nonnegative unnormalized weights \((a,b,c,d)\). Direct expansion yields the following complete list of six pair gaps:
\[
\begin{aligned}
F_0-F_1&=(1-p)(a-b-cp-dp^2),\\
F_0-F_2&=(1-p)(1+p)(a-c-dp),\\
F_0-F_3&=(1-p)\big[(a-d)(1+p+p^2)+(b-c)p\big],\\
F_1-F_2&=(1-p)\big[b-c+(a-d)p\big],\\
F_1-F_3&=(1-p)(1+p)(ap+b-d),\\
F_2-F_3&=(1-p)(ap^2+bp+c-d).
\end{aligned}
\]
In each of the first, second, fourth, fifth and sixth equations, the signed nonpositive or nonnegative derivative of the residual polynomial, or its linearity, gives at most one interior sign reversal; an identically zero gap is harmless. For the third, if \(a=d\) the residual is \((b-c)p\) and has fixed sign or vanishes identically. Otherwise, divide the residual by \(p>0\). Its zero equation becomes
\[
 (a-d)(p^{-1}+1+p)+(b-c)=0.
\]
The function \(p^{-1}+1+p\) is strictly decreasing on \((0,1)\), so this equation has at most one solution. If a vertex were uniquely optimal at both \(p_1\) and \(p_3\) but inferior to another vertex at some \(p_2\) between them, its gap against that rival would be positive at both endpoints and negative in the middle, forcing at least two distinct roots. This contradicts the six-gap classification. (Adding zero-weight vertices was used only for this proof, not for the strictly positive source assumption.)

**Step 3: exact five-vertex construction.** Put \(w=(6,5,6,1,5)\) and \(\pi_i=w_i/23\). Write \(G_j(p)=23F_j(p)\). The four exact factorizations are
\[
\begin{aligned}
G_2-G_0&=p(1-p)(1+p)(5p+1),\\
G_2-G_3&=(1-p)(6p^2+5),\\
G_2-G_4&=(1-p)(1+p)(2p+1)(3p+1),\\
G_2-G_1&=(1-p)(5p^2-5p+1).
\end{aligned}
\]
The first three expressions are strictly positive for all \(p\in(0,1)\). Thus the global optimizer is whichever of vertices \(1\) and \(2\) has the greater score. The last quadratic has exactly two interior zeros \(\rho_-\) and \(\rho_+\); it is positive outside and negative between them. The optimizer classification and unique reentrance follow.

**Step 4: larger paths.** For \(n>5\), initially append \(n-5\) vertices with zero source mass to the right of the five original vertices. At each of the three fixed values \(p\in\{1/5,1/2,4/5\}\), every appended sentinel has detection probability \(p^{j-4}F_4(p)<F_4(p)\) for \(j\ge5\); the known winner among the first five therefore remains unique. Replacing every appended zero weight by a sufficiently small common \(\varepsilon>0\) and renormalizing all weights preserves finitely many strict optimality inequalities by continuity. All source probabilities are then strictly positive. This supplies reentry on every \(n\ge5\).

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library and exact rational arithmetic. It checks all six four-vertex symbolic gap identities coefficientwise for independent symbolic source weights; all four five-vertex factorizations coefficientwise; and the full joint distribution of outbreak source and \(2^4\) independent-edge configurations for \(p=1/5,1/2,4/5\). These are \(240\) source/edge configurations and \(1{,}200\) exact monitor contributions, giving the three claimed unique optimizers. Run \(\texttt{python verify.py}\) from the directory containing \(\texttt{verify.py}\) and compare the emitted JSON with \(\texttt{certificate.json}\). The general theorem is proved above; enumeration only corroborates the specified finite instance.

## Relationship to prior work

Independent-edge epidemic spread with a single source is motivated by Moore and Newman's percolation treatment. Leskovec and collaborators examine general outbreak-detection objectives and sensor placement; the present claim is not that the detection objective is new, but that heterogeneous source weights permit a sharp minimal reentrance phenomenon. Classical decay centrality treats sums of geometric discounts of graph distance; Tsakas studies its extremal vertices, while Hurajová, Gago and Madaras show that unweighted paths are decay-stable. Their *unweighted* path conclusion does not cover arbitrary nonuniform outbreak-source distributions. Holme studies exact node importance for temporal SIR on small graphs, using different epidemic observables. The contribution here is the sharp five-vertex weighted-source theorem and an exact two-crossover phase diagram; no general novelty is claimed for the weighted-distance formula itself.

## Limitations

The result concerns eventual detection from one source on paths, not optimal multiple-monitor sets, time-to-detection, cyclic networks, time-dependent SIR dynamics, or uncertain edge probabilities. Source probabilities must be fixed as \(p\) varies; existence for every larger path does not mean every positive distribution reenters. The transition values are derived for one explicit distribution. The general no-reentry proof is analytic; small finite checks alone cannot establish it. A possible equivalent classification under weighted decay centrality or parameterized graph-ranking terminology remains a bibliographic uncertainty. Independent expert review has not been performed.

## References

1. C. Moore and M. E. J. Newman, *Epidemics and percolation in small-world networks*, arXiv:cond-mat/9911492 (initial public version 1999-11-30), https://arxiv.org/abs/cond-mat/9911492.
2. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen and N. Glance, *Cost-effective Outbreak Detection in Networks*, technical report CMU-ML-07-111 (2007), https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf.
3. N. Tsakas, *On Decay Centrality*, arXiv:1604.05582 (2016), https://arxiv.org/abs/1604.05582.
4. J. Hurajová, S. Gago and T. Madaras, *On decay centrality in graphs*, https://journals.msp.org/mscand/article/download/263/262/291.
5. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (2017), https://arxiv.org/abs/1708.06456.
