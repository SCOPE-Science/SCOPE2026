# A sharp Poisson window for random zero forcing on powers of paths

## Finding
Fix an integer \(k\ge2\). On the labelled path power \(G_{n,k}=P_n^k\), choose initial blue vertices independently with probability \(p_n\), and let \(\mathsf{ZF}_{n,k}\) denote the event that the ordinary zero-forcing process colors every vertex. Then, for every fixed \(c\ge0\),
\[
 p_n=c\,n^{-1/(2k)}\quad\Longrightarrow\quad
 \lim_{n\to\infty}\Pr(\mathsf{ZF}_{n,k})
 =1-\exp\bigl(-(2k-1)c^{2k}\bigr).
\]
Consequently, if \(p_{1/2}(n,k)\) is the unique initial-blue probability at which the success probability equals one half,
\[
 p_{1/2}(n,k)\sim
 \left(\frac{\log 2}{(2k-1)n}\right)^{1/(2k)}.
\]
This is an exact critical window, not only a threshold exponent. The constant \(2k-1\) counts distinct translation types of the smallest *interior triggering configurations*; multiple possible first forces arising from the same consecutive block are counted once. In fact, for \(n\ge2k+1\), the number of distinct \(2k\)-element subsets which can be the full initially blue neighborhood of an interior forcing vertex with one omitted neighbor is exactly
\[
 (2k-1)(n-2k)+1.
\]
For every \(n\ge k+2\), a deterministic structural assertion also holds: an initial blue set in \(P_n^k\) zero forces if and only if it is all vertices or admits at least one legal force immediately.

## Assumptions and scope
The path vertices are \(1,\ldots,n\); two distinct vertices are adjacent in \(P_n^k\) exactly when their numerical distance is at most \(k\). A blue vertex can force its sole white neighbor. The exponent \(k\) is fixed as \(n\to\infty\). The Bernoulli choices are independent and have the same probability \(p_n\) at all vertices. The process is ordinary zero forcing, not skew, positive-semidefinite, or probabilistic transmission along edges. The stated critical-window formula assumes \(p_n=c n^{-1/(2k)}\), with \(c\) fixed.

## Proof
**Any initial force is sufficient.** Suppose a blue vertex \(i\) has exactly one white neighbor \(j\). After forcing \(j\), all of the closed neighborhood \(N[i]\) is blue. This is the consecutive interval \([a,b]\) with \(a=\max(1,i-k)\) and \(b=\min(n,i+k)\). If it meets neither endpoint, its length is \(2k+1\); otherwise its length is at least \(k+1\). A blue interval reaching the left endpoint can be extended one site to the right: with \(b<n\) and \(b\ge k+1\), vertex \(b-k+1\) has exactly one neighbor outside the blue prefix, namely \(b+1\). A symmetric statement extends a blue suffix toward the left endpoint. When the blue interval is interior, vertex \(a+k-1\) has exactly one white neighbor at \(a-1\), so the interval extends left. Repeating reaches the left endpoint, then the right endpoint. Other initially blue vertices only help. Conversely a non-total blue set cannot progress at all unless an initial force is legal. This establishes the equivalence.

**Minimal interior triggers.** For an interior center \(i\in\{k+1,\ldots,n-k\}\), a legal first force requires all but one of its \(2k\) neighbors blue, plus the center blue. Its blue support therefore has \(2k\) elements and is obtained from the \((2k+1)\)-term interval \([i-k,i+k]\) by omitting one site other than \(i\). Omitting either endpoint of this interval produces a block of \(2k\) consecutive sites; these two descriptions overlap by translation. An omitted internal site has one of \(2k-2\) positions other than the center, each producing a different translation type. There are therefore \(2k-1\) types. For \(n\ge2k+1\), consecutive-block supports occur at \(n-2k+1\) locations, and each internal-hole type occurs at \(n-2k\) locations, giving \((2k-1)(n-2k)+1\) distinct supports.

**Poisson limit.** Let \(\mathcal M_{n,k}\) be this family of distinct interior supports, and let \(X_n\) count members \(T\in\mathcal M_{n,k}\) that are entirely blue. Every member has \(2k\) vertices and diameter at most \(2k\). Thus
\[
 \mathbb E X_n=\bigl((2k-1)(n-2k)+1\bigr)p_n^{2k}
 \longrightarrow \lambda=(2k-1)c^{2k}.
\]
For any fixed positive integer \(r\), expand the factorial moment \(\mathbb E(X_n)_r\) into ordered, distinct \(r\)-tuples of supports. Pairwise disjoint tuples contribute \(\lambda^r+o(1)\): their number is \(((2k-1)n)^r+O_{k,r}(n^{r-1})\), and each requires \(2kr\) blue vertices. To bound overlapping tuples, group supports into components joined by nonempty intersection. A component has finitely many relative positions depending only on \(k,r\), so configurations with \(m\) components have \(O_{k,r}(n^m)\) placements. Each component requires at least \(2k\) blue sites, and a component with at least two *distinct* supports requires at least \(2k+1\). Hence any tuple having an overlap contributes in total at most \(O_{k,r}((n p_n^{2k})^m p_n)=o(1)\), summed over the finitely many overlap types. All factorial moments therefore tend to those of a Poisson random variable of mean \(\lambda\), implying \(X_n\Rightarrow\mathrm{Poisson}(\lambda)\) and \(\Pr(X_n>0)\to1-e^{-\lambda}\).

**From triggers to successful forcing.** An initial force by a noninterior center belongs to one of at most \(2k\) boundary vertices of degree at least \(k\), so the probability of some such force is \(O_k(p_n^k)\). For an interior center, every legal force yields an entirely blue member of \(\mathcal M_{n,k}\). Conversely, a fully blue member causes an immediate legal force unless its single omitted neighboring site is blue too. The probability that any such anomaly occurs is at most \(O_k(n p_n^{2k+1})\) by a union bound. By the first assertion, and accounting for the negligible all-blue initial set, we obtain
\[
 \left|\Pr(\mathsf{ZF}_{n,k})-\Pr(X_n>0)\right|
 \le O_k(p_n^k+n p_n^{2k+1}+p_n^n)=o(1).
\]
This proves the critical-window formula, including \(c=0\). The success probability is continuous and strictly increasing in \(p\in(0,1)\), so monotonic bracketing at constants above and below the unique half-success point yields the asymptotic quantile formula.

## Verification
The standalone `verify.py` independently simulates full forcing and tests the initial-force equivalence for every seed set across \(24{,}456\) instances with \(1\le k\le4\) and the listed finite path lengths. It explicitly enumerates the distinct interior trigger supports for \(20\) combinations of \(k\) and \(n\), confirming their cardinality. An independent weighted automaton computes exact finite Bernoulli success probabilities on \(P_n^2\) at \(n=500,2000,10000\) with \(p=n^{-1/4}\), obtaining \(0.8722624,0.8960899,0.9155146\), respectively, approaching the proved limit \(1-e^{-3}=0.9502129\). These finite checks are diagnostics, not the infinite proof.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker, *The Zero Forcing Number of Graph Powers* (arXiv:2610.03892, 2026-10-02), Proposition 7, establishes \(Z(P_n^k)=k\) and does not compute random-set critical laws. Curtis, Gan, Haddock, Lawrence, and Spiro, *Zero Forcing with Random Sets* (arXiv:2208.12899, 2022-08-27), defines the random-set model and proves broad threshold comparisons, including the ordinary-path scale, but does not state a path-power Poisson-window constant. Han and Liang, *Zero Forcing on Maximal Outerplanar Graphs* (arXiv:2610.31138, 2026-10-22), finds optimal seed sizes in the weak-dual-path outerplanar case; it does not provide this distributional statement. A classical rare-local-pattern Poisson mechanism supplies part of the probabilistic argument, but does not alone identify the particular \(2k-1\) forcing configurations or prove that every initial force completes the graph. Earlier explicit minimum-set classifications do not imply this rare-event law.

## Limitations
The result concerns fixed \(k\), sparse independent vertex seeding, and path powers. It makes no claim for \(k\) growing with \(n\), correlated seeds, arbitrary interval graphs, cycle powers, transmission-randomized forcing, or finite-size error constants. The novelty comparison is conditional on inspected and indexed sources; terminology-dependent earlier statements remain a priority risk. Independent audit has not been performed.

## References
1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first public 2026-10-02), https://arxiv.org/abs/2610.03892.
2. B. Curtis, L. Gan, J. Haddock, R. Lawrence, S. Spiro, *Zero Forcing with Random Sets*, arXiv:2208.12899 (2022-08-27), https://arxiv.org/abs/2208.12899.
3. Z. Han, Y. Liang, *Zero forcing on maximal outerplanar graphs: capacities and phase repair*, arXiv:2610.31138 (2026-10-22), https://arxiv.org/html/2610.31138v1.
4. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910 (2018-01-26), https://arxiv.org/abs/1801.08910.
