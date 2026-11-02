# Finite multistate noisy voter modes: exact equilibrium and a two-jump six-voter staircase

## Finding

For the annealed, three-or-more-opinion noisy unanimity-two voter process on a complete graph, the **finite-population stationary count law is a product weight** and the maximum probability of any *specified opinion-count vector* can be found among at most \(N-\lceil N/s\rceil+1\) one-leader, balanced-remainder profiles. As conformity increases, the largest leader size among these maximizers never decreases. In the natural six-voter, three-opinion instance, the unique modal shapes switch successively from \((2,2,2)\) to \((4,1,1)\) to \((6,0,0)\), skipping the two intermediate leader sizes entirely.

In detail, for integers \(N\ge3\), \(s\ge3\), and noise probability \(0<p<1\), set
\[
 t=\frac{s(1-p)}{p(N-1)(N-2)},\qquad
 h_t(k)=\prod_{j=0}^{k-1}\bigl(1+t j(j-1)\bigr),\qquad
 w_t(k)=\frac{h_t(k)}{k!}.
\]
The empty product at \(k=0\) is one. If \(\mathbf n=(n_1,\ldots,n_s)\) is the stationary count vector, then
\[
 \Pr(\mathbf n=\mathbf a)=
 \frac{\prod_{i=1}^s w_t(a_i)}{
 \displaystyle\sum_{\substack{b_i\ge0\\\sum_i b_i=N}}\prod_{i=1}^s w_t(b_i)},
 \quad a_i\in\mathbb Z_{\ge0},\quad\sum_i a_i=N.
\]
The probability is for one *labeled* opinion-count vector; permutation-orbit probabilities must additionally include their multiplicities.

For each integer \(\lceil N/s\rceil\le K\le N\), put
\[
 a_K=\left\lfloor\frac{N-K}{s-1}\right\rfloor,
 \qquad r_K=N-K-(s-1)a_K,
\]
and define \(\lambda_K\) as the vector containing \(K\), then \(r_K\) copies of \(a_K+1\), and \(s-1-r_K\) copies of \(a_K\). One then has the **global modal reduction**
\[
 \max_{\substack{b_i\ge0\\\sum_i b_i=N}}\prod_i w_t(b_i)
 =\max_{\lceil N/s\rceil\le K\le N}\prod_i w_t((\lambda_K)_i).
\]
If \(K_*(t)\) denotes the largest candidate value of \(K\) attaining the right-hand maximum, then \(K_*(t)\) is nondecreasing on \([0,\infty)\). The reduction asserts existence of a canonical maximizer, not that every tied maximizer is canonical.

For \(N=6\), \(s=3\), write
\[
 t_1=\frac{\sqrt{10}-2}{6},\qquad
 t_2=\frac{\sqrt{451}-4}{60},\qquad 0<t_1<t_2.
\]
The complete modal count-profile classification, up to permutations of the three opinion labels, is
\[
\begin{array}{c|c}
\text{conformity parameter}&\text{globally maximal count shapes}\\\hline
0\le t<t_1&(2,2,2)\\
t=t_1&(2,2,2),\ (4,1,1)\\
t_1<t<t_2&(4,1,1)\\
t=t_2&(4,1,1),\ (6,0,0)\\
t>t_2&(6,0,0)
\end{array}
\]
Here the finite-model relation is \(t=3(1-p)/(20p)\), so decreasing noise crosses \(p_1=3/(3+20t_1)\approx0.43641068\) and then \(p_2=3/(3+20t_2)\approx0.34303015\).

## Assumptions and scope

The graph is the loop-free complete graph on \(N\) labeled voters. Each voter has one of \(s\) labeled opinions. At each discrete update a uniformly selected voter, independently at that update, either (i) with probability \(p\) chooses a fresh opinion uniformly among the \(s\) opinions (possibly its present one), or (ii) with probability \(1-p\) chooses two **different** other voters uniformly without replacement and adopts their common opinion if they agree; otherwise it does not change. The finite Markov chain includes self-loops. Positive noise makes it irreducible and aperiodic. The use of distinct panelists, and whether a probability refers to an individual count vector rather than its permutation orbit, are essential.

The classification concerns stationary *modes of the opinion-count distribution*, not deterministic fixed points, sample-path metastable states, expected consensus time, or the phase-coexistence region in an infinite-population equation. No thermodynamic-limit statement is asserted.

## Proof

**1. Reversible finite stationary law.** For a configuration \(\sigma\) and a site of color \(a\), let \(n_b\) be the current number of sites of a different color \(b\). The exact one-step chance that this particular site changes from \(a\) to \(b\) is
\[
 P_{a\to b}(\sigma)=\frac1N\left[\frac ps+(1-p)\frac{n_b(n_b-1)}{(N-1)(N-2)}\right]
 =\frac{p}{sN}\bigl[1+t n_b(n_b-1)\bigr].
\]
After this move, the new configuration has count \(n_b+1\) of opinion \(b\) and count \(n_a-1\) of opinion \(a\). Its reverse one-site transition has probability \(\frac{p}{sN}[1+t(n_a-1)(n_a-2)]\). Define a weight on each labeled microscopic opinion configuration by \(M(\sigma)=\prod_i h_t(n_i(\sigma))\). The ratio of weights after and before the move is exactly the ratio of the forward and reverse transition probabilities, because
\[
 \frac{M(\sigma^{a\to b})}{M(\sigma)}
 =\frac{1+t n_b(n_b-1)}{1+t(n_a-1)(n_a-2)}.
\]
Therefore all one-site transitions satisfy detailed balance for \(M\). Positive noise ensures uniqueness of the stationary distribution. There are \(N!/\prod_i n_i!\) microscopic configurations with fixed labeled count vector, yielding the stated product \(w_t(k)=h_t(k)/k!\) after normalization. This also proves that every claimed finite formula uses the without-replacement dynamics, not the mean-field approximation.

**2. Single-valley adjacent ratios.** Put \(R_t(k)=w_t(k)/w_t(k-1)\) for \(k\ge1\). Direct calculation gives
\[
 R_t(k)=\frac{1+t(k-1)(k-2)}k
 =t(k-3)+\frac{1+2t}{k},
\quad
 R_t(k+1)-R_t(k)=t-\frac{1+2t}{k(k+1)}.
\]
Since \(k(k+1)\) grows strictly, these differences change sign at most once, from nonpositive to nonnegative. Thus the finite list of adjacent ratios first weakly decreases and then weakly increases. Fix a boundary index \(m\) after the decreasing stretch and before the strictly increasing stretch (allowing a flat boundary). Suppose a globally maximal vector contained two coordinates \(u\ge v\ge m+1\). Moving one unit from \(v\) to \(u\) changes the product weight by the factor \(R_t(u+1)/R_t(v)>1\), a contradiction (with endpoints chosen inside \(1,\ldots,N\); if \(u=N\) there cannot be a second positive coordinate). Hence all but at most one coordinate lie on the nonincreasing part of the ratio list.

Take any pair \(u\ge v+2\) of those latter coordinates. Moving one from \(u\) to \(v\) multiplies the product by \(R_t(v+1)/R_t(u)\ge1\). Repeating this operation balances all such coordinates without decreasing the product. The possibly exceptional larger coordinate is designated the leader. If there was no exceptional coordinate, balancing all coordinates yields the nearly equal vector, which is also a member of \(\{\lambda_K\}\). The resulting leader must be at least \(\lceil N/s\rceil\), and the other \(s-1\) counts differ by at most one. Thus some maximizing vector equals a permutation of \(\lambda_K\), proving the global modal reduction. Flat adjacent-ratio ties may produce additional noncanonical maximizers; they do not invalidate the equality of maxima.

**3. Monotonicity of modal leader size.** Put \(g_t(k)=\partial_t\log w_t(k)\). Differentiating the finite product yields
\[
 g_t(k)=\sum_{j=0}^{k-1}\frac{j(j-1)}{1+t j(j-1)}.
\]
Its first difference is \(g_t(k+1)-g_t(k)=k(k-1)/(1+t k(k-1))\), nondecreasing in \(k\). Thus \(k\mapsto g_t(k)\) is discretely convex for every \(t\ge0\). For \(L>K\), the balanced-remainder vector \(\lambda_L\) majorizes \(\lambda_K\): transferring one from a largest remainder to the leader and rebalancing produces the next vector; iterating gives all \(L\). Convexity therefore gives
\[
 \frac{d}{dt}\log\frac{\prod_i w_t((\lambda_L)_i)}{\prod_i w_t((\lambda_K)_i)}
 =\sum_i g_t((\lambda_L)_i)-\sum_i g_t((\lambda_K)_i)\ge0.
\]
Hence every comparison of a larger leader with a smaller leader has a nondecreasing weight ratio. If a larger leader is maximal at some parameter, a strictly smaller leader cannot become its unique superior at a larger parameter. Choosing the *largest* maximizer resolves exact ties and proves that \(K_*(t)\) is nondecreasing.

**4. Exact six-voter staircase.** For \(N=6,s=3\), the five candidate weights \(W_K=\prod_i w_t((\lambda_K)_i)\) simplify to
\[
\begin{aligned}
 W_2&=1/8,\\
 W_3&=(1+2t)/12,\\
 W_4&=(1+2t)(1+6t)/24,\\
 W_5&=(1+2t)(1+6t)(1+12t)/120,\\
 W_6&=(1+2t)(1+6t)(1+12t)(1+20t)/720.
\end{aligned}
\]
The candidate \(K=3\) is strictly dominated by \(K=2\) when \(t<1/4\), and by \(K=4\) when \(t>1/6\); on the overlap of these ranges it is strictly dominated by both. At \(t=1/4\) it is still strictly below \(W_4\), and at \(t=1/6\) it is still below \(W_2\). Similarly, \(W_5<W_4\) whenever \(t<1/3\), and \(W_5<W_6\) whenever \(t>1/4\), including the boundary cases by the other inequality. Therefore neither \(K=3\) nor \(K=5\) can maximize. The equalities \(W_2=W_4\) and \(W_4=W_6\) are respectively
\[
 12t^2+8t-2=0,\qquad 240t^2+32t-29=0,
\]
whose unique nonnegative roots are \(t_1\) and \(t_2\) stated above. Both polynomials are strictly increasing for \(t\ge0\), with \(t_1<t_2\). Since \(W_2\) is constant, \(W_4\) increases strictly and \(W_6/W_4\) increases strictly, the three remaining candidates exchange dominance exactly in the displayed order, including the two indicated ties. This finishes the proof.

## Verification

The dependency-free Python 3 file `check.py` independently enumerates the unordered two-voter panels and verifies microscopic detailed balance using exact fractions for \(3\) to \(6\) voters and three opinions and an additional four-opinion case. It then enumerates all opinion-count compositions in small populations and checks the canonical-mode reduction and monotonicity for eleven exact rational conformity parameters. It verifies all five six-voter weight polynomials and isolates both positive threshold roots in disjoint rational intervals. An actual run reported `PASS 16615 exact deterministic assertions`. These finite checks corroborate but do not replace the general detailed-balance, single-valley and majorization proofs above.

## Relationship to prior work

Nowak, Stoń and Sznajd-Weron (first public 2020-12-21; arXiv:2012.11725) define precisely the annealed multi-opinion unanimity-panel dynamics (their section 2) and study deterministic mean-field fixed points and phase diagrams (their section 3, equations 7–16). Their observation that the mean-field stationary concentrations have few levels is related in theme, but it is not a finite invariant measure or a finite **global count-mode** theorem: their mean-field approximation replaces the finite hypergeometric sampling factor by powers of concentrations, and their phase thresholds do not imply the exact six-voter stationary mode thresholds here.

Herrerías-Azcué and Galla (first public 2019-03-21; arXiv:1903.09198) give exact stationary **one-opinion marginals** for a homogeneous, *linear pairwise imitation* multi-opinion model. Their rate formula is linear in the target opinion count, whereas this model has a quadratic unanimity-two rate; their marginal calculations do not imply the joint nonlinear invariant measure or global modes.

Peralta, Carro, San Miguel and Toral (first public 2018-03-19; arXiv:1803.06861) solve a nonlinear noisy-voter model with two opinions, with exact all-to-all stationary behavior and finite-size phase effects. Its binary birth-death reduction does not supply the multistate finite detailed-balance measure, the general one-leader mode theorem, or the three-opinion staircase. Mobilia (first public 2015-06-16; arXiv:1506.04911) studies finite stationary fluctuations in a two-opinion q-voter system with fixed zealots, rather than annealed uniform reassignments. Standard finite-state reversibility and product-weight calculus are ingredients, not claimed methodological inventions. Searches conducted against related results did not identify a statement logically covering the finite structural and six-voter claims; a search cannot establish complete historical priority.

## Limitations

The proof requires an annealed, uniform-refresh process, an exactly two-person panel sampled **without replacement**, the loop-free complete graph, and \(N\ge3\), \(s\ge3\), \(p>0\). It concerns the probability of each particular labeled count vector; modes of permutation-aggregated orbit probabilities can differ. At \(p=0\) the chain is reducible, and the formula is not an equilibrium uniqueness statement. Other panel sizes, quenched noise, graphs with spatial structure, metastability and asymptotic thermodynamic transitions are not classified. Historical originality is based on accessible source comparisons and is not independently certified.

## References

1. B. Nowak, B. Stoń and K. Sznajd-Weron, *Discontinuous phase transitions in the multi-state noisy q-voter model: quenched vs. annealed disorder*, arXiv:2012.11725, first posted 2020-12-21, https://arxiv.org/abs/2012.11725 and full text https://arxiv.org/html/2012.11725v3 .
2. F. Herrerías-Azcué and T. Galla, *Consensus and diversity in multi-state noisy voter models*, arXiv:1903.09198, first posted 2019-03-21, https://arxiv.org/abs/1903.09198 and full text https://arxiv.org/html/1903.09198v1 .
3. A. F. Peralta, A. Carro, M. San Miguel and R. Toral, *Analytical and numerical study of the non-linear noisy voter model on complex networks*, arXiv:1803.06861, first posted 2018-03-19, https://arxiv.org/abs/1803.06861 and full text https://arxiv.org/html/1803.06861v2 .
4. M. Mobilia, *Nonlinear q-voter model with inflexible zealots*, arXiv:1506.04911, first posted 2015-06-16, https://arxiv.org/abs/1506.04911 and full text https://arxiv.org/html/1506.04911v2 .
