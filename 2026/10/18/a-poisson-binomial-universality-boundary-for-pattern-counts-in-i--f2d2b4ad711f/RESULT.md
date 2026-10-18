# A Poisson–binomial universality boundary for pattern counts in independent words

## Finding

Consider a finite alphabet \(\mathcal A\) with at least two symbols. A word \(w=w_1\cdots w_L\) of length \(L\ge1\) is *unbordered* when none of its nonempty proper prefixes is also a suffix. Given independent alphabet-valued observations \(X_1,\ldots,X_n\), write \(N_w\) for the number of starting positions at which the consecutive length-\(L\) block equals \(w\).

**Theorem (exact universality boundary).** The following are equivalent for every fixed word \(w\):

1. \(w\) is unbordered.
2. For every \(n\ge L\) and all independent (possibly nonidentically distributed) alphabet-valued observations, \(N_w\) has the distribution of a sum of independent Bernoulli variables.
3. For every \(n\ge L\) and every *strictly positive* i.i.d. alphabet law, \(N_w\) has the distribution of a sum of independent Bernoulli variables.

The sufficiency statement extends to any *cross-bifix-free* collection \(\mathcal C\subseteq\mathcal A^L\): no proper nonempty suffix of any codeword is a prefix of any codeword (including itself). For independent, not necessarily identically distributed observations, the total number \(N_{\mathcal C}\) of length-\(L\) codeword occurrences is a Poisson–binomial variable supported on \(\{0,\ldots,\lfloor n/L\rfloor\}\).

**Sharp first-overlap criterion.** Suppose \(L\ge2\) and \(w\) is bordered. Let \(s<L\) be its smallest positive period, meaning \(w_j=w_{j+s}\) for \(1\le j\le L-s\). Under a strictly positive i.i.d. letter law \(\mu\), set \(\pi=\Pr_\mu(w)\) and \(h=\Pr_\mu(w_1\cdots w_{L-s})\). At sample length \(n=L+s\),
\[
\mathbb E[N_w]=(s+1)\pi,\qquad
\Pr(N_w=2)=\frac{\pi^2}{h},
\]
and, sharply,
\[
N_w\text{ is Poisson–binomial}\quad\Longleftrightarrow\quad h\ge\frac4{(s+1)^2}.
\]
Consequently every bordered word fails the universal property for some strictly positive i.i.d. alphabet law, already at its earliest possible self-overlap sample length.

If the observations are i.i.d. and \(\mathcal C\) is cross-bifix-free, set \(a=\sum_{v\in\mathcal C}\Pr_\mu(v)\). Then the **exact entire distribution** is encoded by
\[
\mathbb E[z^{N_{\mathcal C}}]
=\sum_{k=0}^{\lfloor n/L\rfloor}
\binom{n-(L-1)k}{k}a^k(z-1)^k.
\]
Thus the code's count law depends only on \(n,L\), and the aggregate single-window probability \(a\).

## Assumptions and scope

The observations are independent, with arbitrary marginal distributions on a fixed finite alphabet. A code is a set of distinct equal-length words. For \(n<L\), both counts vanish identically. Bernoulli parameters \(0\) and \(1\) are allowed in distributional representations. The sharp overlap criterion additionally assumes positive i.i.d. letter probabilities and a nonempty proper border. A Poisson–binomial variable means a sum of finitely many independent, not necessarily equally distributed, Bernoulli variables.

## Proof

**1. Simultaneous occurrences and the graph polynomial.** Fix a cross-bifix-free code \(\mathcal C\) and \(n\ge L\), and put \(r=n-L+1\). Write \(I_i\) for the indicator of a codeword at position \(i\), and \(a_i=\mathbb E[I_i]\ge0\). For distinct starts at separation below \(L\), simultaneous occurrences are impossible by the cross-bifix condition. At starts separated by at least \(L\), the defining coordinate blocks are disjoint and therefore their indicators are mutually independent. Expanding the product gives the exact finite identity
\[
\mathbb E[z^{N_{\mathcal C}}]=\mathbb E\prod_{i=1}^{r}\bigl(1+(z-1)I_i\bigr)
=\sum_{\substack{S\subseteq\{1,\ldots,r\}\\ |i-j|\ge L\ \forall i\ne j\in S}}
(z-1)^{|S|}\prod_{i\in S}a_i.
\]
The right side is the weighted independence polynomial \(I_G(z-1)\) of the graph \(G\) on \(\{1,\ldots,r\}\), with adjacency \(|i-j|<L\). This graph is claw-free: every neighbor of a vertex lies to its left or right, with the vertices on each side forming a clique.

**2. Real-rootedness and independent-Bernoulli representation.** The independence polynomial of any finite claw-free graph has only real negative roots (Chudnovsky–Seymour's theorem; a self-contained later proof appears in Bencs, Theorem 1.8). Its weighted version for arbitrary nonnegative vertex weights follows rigorously. For rational weights \(a_i=m_i/B\), replace vertex \(i\) by a clique of \(m_i\) interchangeable vertices, connecting two such cliques fully whenever the original vertices were adjacent. Clique substitution preserves claw-freeness, and the clone graph produces the weighted polynomial after scaling its indeterminate by \(1/B\). More explicitly, the clone-graph polynomial at \(t/B\) is \(\sum_{S\text{ independent}}t^{|S|}\prod_{i\in S}(m_i/B)\). A limit of rational weights covers all nonnegative real weights, with roots remaining real by closure of the real-rooted polynomial class. Thus \(I_G(z-1)\) has only real roots. Since it is a probability-generating polynomial with nonnegative coefficients and value one at \(z=1\), none of its roots is positive; all are nonpositive. Factorization into normalized linear factors \((1-\theta_j)+\theta_j z\), with \(0\le\theta_j\le1\), gives the Poisson–binomial representation. Its degree is no greater than \(\lfloor n/L\rfloor\). This proves sufficiency, including the cross-bifix-free extension.

**3. Earliest overlap and the exact threshold.** If \(w\) is bordered, write \(s\) for the least positive shift producing compatible overlapping copies. At length \(L+s\), there are \(s+1\) possible starts. Because no smaller shift works, the only possible pair of occurrences is the one starting at positions \(1\) and \(s+1\); three occurrences are impossible. Each single occurrence has probability \(\pi\), so \(\mathbb EN_w=(s+1)\pi\). The unique compatible pair constrains \(L+s\) independent letters; by counting the shared prefix, its probability is \(\pi^2/h\). Consequently the quadratic generating polynomial has discriminant
\[
\Delta=(\mathbb EN_w)^2-4\Pr(N_w=2)
=\pi^2\left((s+1)^2-\frac4h\right).
\]
For a nonnegative normalized quadratic probability-generating polynomial, real-rootedness, and therefore Poisson–binomial representability, is equivalent to \(\Delta\ge0\). This proves the sharp criterion. Because \(L-s\ge1\), take any letter occurring in the shared prefix and give it arbitrarily small but positive probability while keeping every alphabet probability positive. Then \(h\) tends to zero, violates the criterion and disproves the universal property. Necessity follows.

**4. Stationary exact formula.** Under i.i.d. observations, all \(a_i=a\). The number of \(k\)-subsets of the starting positions with mutual gaps at least \(L\) equals \(\binom{n-(L-1)k}{k}\): subtract \((L-1)(j-1)\) from the \(j\)-th start to obtain an ordinary \(k\)-subset of a shorter interval. Substitution in the graph expansion proves the displayed exact generating function.

## Verification

The accompanying standalone standard-library script `verify.py` checks the finite moment expansion against direct enumeration under nonidentical rational Bernoulli/ternary letter laws for singleton motifs and cross-bifix-free codes. It also checks the earliest-overlap probability, discriminant threshold, and the stationary placement formula in exact rational arithmetic. These are finite independent checks, **not proofs** of the universal real-rootedness theorem; its nonstandard input is the published claw-free independence-polynomial theorem, explicitly identified above.

Examples at first overlap: for \(w=010\) and \(\Pr(1)=p\), one has \(s=2\), \(n=5\) and \(h=1-p\); the count is Poisson–binomial exactly when \(p\le5/9\). For \(w=01010\), one has \(s=2\), \(n=7\) and \(h=p(1-p)^2\le4/27<4/9\), so no interior Bernoulli bias gives a Poisson–binomial law at that sample length.

## Relationship to prior work

Kumar and Upadhye (2017) develop distributional approximations for counts of run patterns in independent trials; their results do not state this exact Poisson–binomial universality characterization for arbitrary literal motifs. Johnson and Fu (2014) study distributional approximations for runs and patterns, with counting conventions requiring care. Mansour, Rastegar and Roitershtein (2019) study pattern-occurrence enumeration and distributional asymptotics, not the present exact border/real-rootedness boundary in the portions inspected. The real-rootedness of claw-free independence polynomials is a **known theorem**, not claimed here; the contribution is its identification with occurrence-count generating functions, plus the complete converse and sharp first-overlap criterion. Existing results for two-letter adjacent motifs and for non-overlapping code occupancy do not establish the stated general equivalence.

## Limitations

No closed-form individual Bernoulli parameters are asserted for arbitrary nonidentical letter laws, though existence follows from real-rootedness. The sharp criterion applies specifically at the *first* overlapping sample length and not to all larger lengths; a bordered motif can be Poisson–binomial at selected biases and lengths. The theorem requires independence of the source letters and equal motif length within a code. Full historical originality cannot be certified against unindexed classical pattern-count literature. In the present research comparison, sections of the 2019 pattern paper rather than the entire document were inspected.

## References

1. A. Kumar and N. S. Upadhye, *On Discrete Gibbs Measure Approximation to Runs* (2017), arXiv:1701.03294, first public version 2017-01-12; primary MSC 62E17.
2. M. Chudnovsky and P. Seymour, *The roots of the independence polynomial of a clawfree graph*, Journal of Combinatorial Theory Series B 97 (2007), 350–357.
3. F. Bencs, *Christoffel–Darboux type identities for the independence polynomial*, arXiv:1409.2527 (2014), Theorem 1.8 and its proof.
4. A. A. Johnson and J. C. Fu, *Approximating the distributions of runs and patterns*, Statistics and Computing (2014).
5. T. Mansour, R. Rastegar and A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, arXiv:1905.05646 (2019).
