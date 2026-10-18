# Sharp chromosome-count threshold for balanced terminal cell lineages

## Finding
Let \(m\ge1\) and \(K=K_m\ge1\) be integers. Start a synchronous complete binary genealogy from one cell carrying \(K\) distinguishable chromosomes, each with two telomere-end budgets \((m,m)\). At every internal vertex and on each chromosome independently, toss a fair coin; the left daughter loses one unit at the first end and the right daughter at the second, or vice versa. A lineage remains viable while all its budgets remain nonnegative; a daughter with a negative budget is removed. Let \(Z_m\) count viable cells at depth \(2m\).

For each fixed \(\varepsilon>0\), as \(m\to\infty\),
\[
K_m\le (4\log2-\varepsilon)\frac{m}{\log m}\quad\Longrightarrow\quad \Pr(Z_m>0)\to1,
\]
while
\[
K_m\ge (4\log2+\varepsilon)\frac{m}{\log m}\quad\Longrightarrow\quad \Pr(Z_m>0)\to0.
\]
In fact the first regime satisfies \(Z_m/\mathbb E Z_m\to1\) in \(L^2\). The threshold is sharp to first order in the joint large-budget/large-chromosome limit. The critical window and limiting distribution at the exact threshold are not determined.

## Assumptions and scope
The genealogy is deterministic binary branching in discrete generations, with independent fair segregation coins over chromosome and parent-vertex pairs. Both end budgets initially equal \(m\); each chromosome experiences exactly one shortening per division along every chosen lineage, with complementary daughter shortenings. Zero budget remains viable and a negative budget is removed. There is no telomerase, differentiation, compartment switching, death unrelated to telomeres, or random division clock. The latter mechanisms belong to richer biological models and are not covered here. The asymptotic concerns a mathematical large-\(K\), large-\(m\) family, not fixed human chromosome counts.

A depth-\(2m\) lineage is viable precisely when on each chromosome exactly \(m\) of the \(2m\) losses occur at either end. Because losses are nonnegative, the endpoint condition also ensures viability at every preceding generation. The count can therefore be computed in an unpruned complete binary tree, counting only viable leaves.

## Proof
Write \(n=2m\), \(p=2^{-n}\binom{n}{m}\), and \(Z=Z_m\). Along any fixed root-to-leaf path, all \(K\) coordinates are independent fair Bernoulli sums of length \(n\), hence
\[
\mathbb EZ=2^np^K. \tag{1}
\]
By Stirling's formula, \(p=\sqrt{2/(\pi n)}(1+O(n^{-1}))\), so
\[
\log\mathbb EZ=n\log2-\frac K2\log n+O(K).\tag{2}
\]
Thus, if \(K\ge(2\log2+\delta)n/\log n\), \(\mathbb EZ\to0\) and Markov's inequality proves the upper-threshold assertion. Conversely, \(\mathbb EZ\to\infty\) exponentially in \(n\) if \(K\le(2\log2-\delta)n/\log n\).

For the lower assertion it remains to control correlations between different leaves. Two distinct ordered leaves share exactly \(j\) initial edges for some \(0\le j\le n-1\), then take opposite daughter edges, followed by \(t=n-j-1\) edges each. There are \(2^{2n-j-1}\) such ordered pairs. For a single chromosome, conditioning on \(r\) losses at the first end along the shared prefix, the two opposite edges make the two completion requirements \(m-r-1\) and \(m-r\). Thus their joint balanced-end probability is exactly
\[
q_j=2^{-j-2t}\sum_{r=0}^j\binom jr\binom t{m-r-1}\binom t{m-r},\tag{3}
\]
with binomial coefficients zero outside their permitted range. Independence across chromosomes yields
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}=\frac1{\mathbb EZ}+\sum_{j=0}^{n-1}2^{-j-1}R_j^K,\qquad R_j=\frac{q_j}{p^2}.\tag{4}
\]
For \(j=n-1\) the two sibling endpoints cannot both be balanced, so \(q_{n-1}=0\).

Set \(M_t=2^{-t}\binom t{\lfloor t/2\rfloor}\). Condition on the first leaf being balanced: the other leaf's last \(t\) unbiased flips must hit one prescribed sum, whose probability is at most \(M_t\). Hence \(q_j\le p M_t\). For \(t\ge1\), the elementary binomial-ratio inequality
\[
\frac{M_t}{p}\le\sqrt{\frac n t}\tag{5}
\]
holds. Indeed \(M_{2r-1}=M_{2r}\), and \(M_{2r}/M_{2(r+1)}=(2r+2)/(2r+1)\le\sqrt{(r+1)/r}\). Iterating through the even indices up to \(n=2m\) gives (5) for even \(t\); the odd case follows from the next even index. Therefore \(R_j\le\sqrt{n/(n-j-1)}\) for \(j\le n-2\).

For each fixed \(j\), a uniform fixed-offset central-binomial estimate in (3) gives \(R_j=1+O_j(n^{-1})\). (Each factor \(2^{-t}\binom t{m-r-b}\), \(b\in\{0,1\}\), equals \(p(1+O_j(n^{-1}))\) for \(0\le r\le j\); summing prefix weights proves this.) Since \(K=O(n/\log n)\), it follows that \(R_j^K\to1\) at each fixed \(j\).

We now justify exchanging the weighted sum and limit. Fix \(\delta>0\) and assume \(K\le(2\log2-\delta)n/\log n\). When \(0\le j\le n/2-1\), (5) gives
\[
K\log R_j\le\frac K2\log\frac n{n-j-1}\le\frac{K(j+1)}n\le\frac{(2\log2)(j+1)}{\log n}.
\]
For sufficiently large \(n\) this is at most \((\log2)(j+1)/2\), producing a summable uniform geometric majorant for \(2^{-j-1}R_j^K\). Pointwise convergence therefore makes the sum over \(j\le n/2-1\) tend to \(\sum_{j\ge0}2^{-j-1}=1\).

For the remaining indices, choose \(0<\eta<1/2\) sufficiently small that \((1-\eta)\log2>\log2-\delta/2\). For \(n/2\le j\le(1-\eta)n\), (5) bounds \(R_j^K\le\exp(O(n/\log n))\), whereas \(2^{-j}\le2^{-n/2}\); the entire contribution tends to zero. For \((1-\eta)n<j\le n-2\), (5) bounds \(R_j^K\le\exp((\log2-\delta/2)n)\), while \(2^{-j}\le\exp(-(1-\eta)n\log2)\), so again the sum vanishes exponentially. Along with (2), (4) yields \(\mathbb EZ^2/(\mathbb EZ)^2\to1\). This is exactly \(L^2\)-convergence of \(Z/\mathbb EZ\) to one. Chebyshev's inequality proves \(\Pr(Z>0)\to1\).

Finally, \(n=2m\) and \(\log n/\log m\to1\) convert the critical coefficient \(2\log2\) for \(K\log n/n\) into \(4\log2\) for \(K\log m/m\), as claimed.

## Verification
Run the Python standard-library script `VERIFY.py` in the same directory. It checks the exact pair probability and binomial-ratio bounds for \(1\le m\le34\), and enumerates all segregation-coin assignments for the small cases \((m,K)=(1,1),(1,2),(2,1)\) to check both moment formulas. On the packaged script this produced `PASS 1196 exact identities and finite bound checks; asymptotic theorem proved analytically.` Finite verification does not substitute for the Stirling estimate or the three-range argument establishing convergence.

## Relationship to prior work
Baland, Toupance and Villemonais (2026, arXiv:2610.12660v1) specify precisely the complementary-daughter, independently random chromosome-segregation rule without telomerase. Their results concern large initial cell populations and temporal stochastic fluctuations in a multi-compartment model; the present theorem instead addresses the probability of at least one viable depth-\(2m\) descendant as the chromosome count and available end budget jointly diverge in a pure binary-division specialization. Wattis, Qi and Byrne (2019) develop telomere-length population models with continuum limits, rather than this joint-dimensional terminal viability threshold. Standard fixed-dimensional branching-random-walk first/second-moment arguments motivate the method but do not directly provide the stated high-dimensional complementary-sibling threshold. These distinctions are based on comparisons of statements and assumptions, not simply searches for a title.

## Limitations
The result does not cover the actual complete multi-compartment hematopoietic dynamics, fixed physiological chromosome counts, asymmetric inheritance, stochastic telomerase, unequal budgets, or the critical window of width smaller than \(m/\log m\). A stronger related theorem might exist under different terminology in branching random walks or senescence genealogy; absence from searched sources cannot establish absolute novelty. The constant is a first-order asymptotic, not a numerical empirical parameter for cell populations.

## References
Baland, S., Toupance, S., and Villemonais, D., *Stochastic Modelling of Telomere Length Dynamics During Hematopoiesis*, arXiv:2610.12660v1, first public 2026-10-08, https://arxiv.org/html/2610.12660v1 (notably Section 3, division rule and Sections 4–5).

Wattis, J. A. D., Qi, Q., and Byrne, H. M., *Mathematical modelling of telomere length dynamics*, Journal of Mathematical Biology 80 (2020), 1039–1076, first published 2019-11-14, https://doi.org/10.1007/s00285-019-01448-y.
