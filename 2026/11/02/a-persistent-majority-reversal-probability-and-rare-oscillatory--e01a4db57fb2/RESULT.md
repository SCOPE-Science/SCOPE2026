# A persistent majority-reversal probability and rare oscillatory basins on balanced tripartite graphs

## Finding
For every integer \(n\ge1\), consider synchronous binary strict-neighbor majority dynamics with tie retention on the labelled complete tripartite graph \(K_{n,n,n}\). Every trajectory enters a fixed state or a primitive two-cycle in at most two updates; this is a sharp uniform entry-time bound for \(n\ge3\). The number of fixed configurations is
\[
Q_n=2+\mathbf 1_{2\mid n}\binom{n}{n/2}^{3},
\]
where the binomial term is included only for even \(n\). The number of distinct primitive temporal two-cycle orbits is
\[
N_n=3(2^n-2).
\]
Define \(L_n(a)=\min(a,n-a)\) and \(H_n(a)=\max(a,n-a)\), and let \(B_n\) count all labelled initial configurations whose eventual orbit has primitive period two, including configurations already on those cycles. Then
\[
B_n=3\sum_{a=0}^{n}\binom na^2
        \sum_{b=L_n(a)+1}^{H_n(a)-1}\binom nb,
\]
with an empty inner sum interpreted as zero. Thus the numbers entering a primitive two-cycle at times zero and one are respectively \(6(2^n-2)\) and \(B_n-6(2^n-2)\). No state first enters a two-cycle at a later time.

Under independently uniform initial binary opinions, the probability of eventual oscillation has the exact asymptotic
\[
\Pr(\text{eventual primitive two-cycle})
=\frac{6}{\pi^{3/2}}\arctan\frac1{\sqrt2}\ n^{-1/2}+o(n^{-1/2}).
\]
Therefore unanimity occurs with probability approaching one. Nevertheless, conditional on an initial nonzero global majority and an eventual unanimous opinion, the limiting probability that **the final unanimous opinion is opposite to the initial global majority** is the positive constant
\[
\rho=1-\frac3\pi\arctan\sqrt2
      =0.08773982804591085\ldots.
\]
The same limit holds for the unconditional probability of the reversal event, declaring it false when the initial majority is tied or unanimity is not reached.

## Assumptions and scope
The graph has three disjoint labelled shores of exactly \(n\) vertices each, and every pair of vertices in distinct shores is adjacent. Every vertex has degree \(2n\). Opinions are \(0\) or \(1\). At each simultaneous update a vertex adopts the strict majority of its \(2n\) neighbors, and on an exact tie retains its own opinion. The first periodic-entry time \(T\) is the smallest nonnegative integer for which the complete labelled state at time \(T\) lies on an eventual periodic orbit. Distinct primitive two-cycles are counted once per unordered pair of phase configurations, without quotienting graph labels. Random initial opinions are independent, unbiased Bernoulli variables. A global majority means strict majority among all \(3n\) initial vertices. The statements do not apply to asynchronous updates, different tie breaking, or unbalanced shore sizes.

## Proof
**Count reduction.** Write \(q_i\in\{0,\dots,n\}\) for the number of ones on shore \(i\) and put \(s=q_1+q_2+q_3\). For every vertex of shore \(i\) the number of neighboring ones is exactly \(s-q_i\). Consequently the *exact labelled-state update* induces the count map
\[
\Phi_i(q)=\begin{cases} n,&s-q_i>n,\\0,&s-q_i<n,\\q_i,&s-q_i=n.\end{cases}
\]
In the strict cases the whole shore becomes pure; in the equality case each individual opinion on that shore is retained. Thus the count map also determines the evolution of the underlying labelled configuration, with no hidden within-shore changes.

**Two-step classification.** Call \(s-q_i=n\) a tie at shore \(i\). Without ties the first image consists entirely of pure shores. Any three pure shores become unanimous after at most one further update: zero, one, two, or three full shores become, respectively, all-zero, all-zero, all-one, or all-one. With exactly one tie, say at shore \(i\), if \(q_i\) is an endpoint then the first image is pure and the preceding argument applies. If it is interior, the other two shores become oppositely pure precisely when \(q_i\) lies strictly between their two initial counts (whose sum is \(n\)); in this case the two pure shores exchange states each update and shore \(i\) retains its entire mixed pattern, giving a primitive two-cycle at the first image. If the untied shores become identically pure they force the tied shore to their common value on the next update. Equality to an endpoint would be another tie and so cannot arise in this one-tie case. With exactly two ties, up to reordering \(q=(n-a,a,a)\); when \(a<n/2\), the next two images are \((0,a,a)\) and \((0,0,0)\), and when \(a>n/2\) they are \((n,a,a)\) and \((n,n,n)\). Three ties imply \(q_1=q_2=q_3=n/2\), possible only for even \(n\), and every labelled state with those counts is fixed. This proves the complete time bound and rules out other cycles. The bound is attained for every \(n\ge3\) by the initial count triple \(q=(n-1,1,1)\), which evolves to \(q=(0,1,1)\) and then to zero consensus.

**Periodic-state enumeration.** The only fixed labelled states are the two consensus configurations and, for even \(n\), the independently chosen half-filled patterns in all three shores. A primitive two-cycle has exactly one mixed shore; the two others are full and empty in opposite temporal phases. There are three choices of mixed shore, \(2^n-2\) choices of its nonconstant labelled pattern, and two phase states per orbit, proving the stated orbit count.

**Oscillatory basin enumeration.** By the case analysis, the initial state eventually oscillates if and only if, for some uniquely specified \(i\), the two other shore counts add to \(n\) and the count on shore \(i\) lies strictly between them. Uniqueness holds because satisfying a second such tie would force the purported interior count to equal an endpoint. For the ordered counts of the two other shores, write \((a,n-a)\). Their labelled choices are \(\binom na^2\), and the interior shore contributes the inner binomial sum. Sum over \(a\) and the three choices of the tied shore. The endpoints \(a=0,n\) give exactly the initially periodic states, yielding their separate count.

**Rare oscillations.** Let \(A,B,C\) be independent \(\operatorname{Bin}(n,1/2)\) counts. The preceding exact event gives
\[
B_n/8^n=3\Pr(A+C=n)\Pr(\min(A,C)<B<\max(A,C)\mid A+C=n).
\]
The central-binomial estimate gives \(\Pr(A+C=n)=\binom{2n}n/4^n\sim(\pi n)^{-1/2}\). Conditional on the tie, \(A\) is hypergeometric with mean \(n/2\) and variance \(n^2/[4(2n-1)]\), while \(B\) remains an independent binomial with variance \(n/4\). The conditional lattice central limit theorem gives independent centered Gaussian limits with variance ratio \(1:2\), hence the strict-between probability tends to \(\Pr(|Z_2|<|Z_1|/\sqrt2)=(2/\pi)\arctan(1/\sqrt2)\) for independent standard normals. The equality boundary has zero limiting mass. Multiplication proves the asymptotic.

**Persistent reversal.** Set \(X_i=(2q_i-n)/\sqrt n\); under uniform initial opinions the vector converges to three independent standard normal variables \((Z_1,Z_2,Z_3)\). All pairwise-sum ties and a global initial tie together have probability \(O(n^{-1/2})\). Outside these events, the one-step three shore opinions are the signs of the three pairwise sums, and the next step is consensus with the majority of those three signs. A reversal occurs when the initial total sum has sign opposite to at least two pair sums. By symmetry, its Gaussian probability is six times
\[
\Pr(U>0,V>0,W>0),\quad U=Z_1+Z_2+Z_3,\quad V=-Z_1-Z_2,\quad W=-Z_1-Z_3.
\]
The correlations are \(r_{UV}=r_{UW}=-\sqrt{2/3}\), \(r_{VW}=1/2\). For any centered nondegenerate Gaussian triple, simultaneous sign-symmetry and the elementary bivariate Gaussian sign identity imply
\[
\Pr(U,V,W>0)=\frac18+\frac1{4\pi}
(\arcsin r_{UV}+\arcsin r_{UW}+\arcsin r_{VW}).
\]
Indeed, expand \((1+\operatorname{sgn}U)(1+\operatorname{sgn}V)(1+\operatorname{sgn}W)/8\); odd sign moments vanish by simultaneous negation, while the bivariate sign correlation is \((2/\pi)\arcsin r\), obtained from rotationally symmetric planar normals. Substitution and \(\arcsin\sqrt{2/3}=\arctan\sqrt2\) give \(\rho=1-(3/\pi)\arctan\sqrt2\). The probability of consensus tends to one, so conditioning on consensus and a strict initial majority does not change the limit.

## Verification
The companion standalone checker `check_majority.py` directly iterates every binary labelled state for \(1\le n\le5\) (a total of \(2^3+2^6+2^9+2^{12}+2^{15}=37{,}448\) configurations), compares the resulting exact entry-time/period distributions against the binomial-weighted count map, and checks the closed formulas for every \(1\le n\le30\). The displayed asymptotic constants are evaluated separately. The verification output is embedded as `check_output.txt`. These finite checks do not replace the all-\(n\) case analysis or probabilistic limit arguments above.

## Relationship to prior work
The general period-at-most-two theorem for symmetric threshold networks is due to Goles and Olivos (1980); it is substantially weaker than the two-update entry cutoff here. Benjamini, Chan, O'Donnell, Tamuz and Tan (first public arXiv version, May 11, 2014) analyze majority-dynamics consensus on unimodular and random graphs; their random-graph initial-majority results do not imply this exact deterministic tripartite census or its reversal constant. Turau (2023) treats counts of fixed points and pure cycles on trees, a different graph class and a different counting target. Published results on *parity* automata on complete multipartite graphs use mod-two parity updates, not nonlinear majority thresholds. The present claim concerns the exact labelled \(K_{n,n,n}\) dynamics and its quantitative basin statistics, not the known general period-two property.

## Limitations
This is an exact result for three **equal-sized** nonempty shores under tie retention. It makes no claim for arbitrary complete multipartite graphs, biased initial opinions, stochastic neighbor sampling, or asynchronous dynamics. The constant describes an asymptotic probability under a specified probability measure, not the probability of a reversal for each finite state. The earlier literature search has finite coverage; a previously unindexed equivalent analysis remains possible. No independent research audit has been performed.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first posted 2014-05-11, https://arxiv.org/abs/1405.2486.
- V. Turau, *Counting Problems in Trees, with Applications to Fixed Points of Cellular Automata*, arXiv:2312.13769, 2023, https://arxiv.org/abs/2312.13769.
