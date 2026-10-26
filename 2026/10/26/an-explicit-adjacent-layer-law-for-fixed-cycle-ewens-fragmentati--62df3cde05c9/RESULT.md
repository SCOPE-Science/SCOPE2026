# An explicit adjacent-layer law for fixed-cycle Ewens fragmentation

## Finding
Fix \(n\ge2\). Let \(c(n,k)\) denote the number of permutations of \([n]\) with \(k\) cycles. For each \(1\le k\le n\), define a law on partitions \(\pi\) of \([n]\) into exactly \(k\) blocks by
\[
\mu_{n,k}(\pi)=\frac{\prod_{B\in\pi}(|B|-1)!}{c(n,k)}.
\]
There is a *single* exact sampler for all these layers such that each successive partition is obtained by splitting exactly one block. It has the following explicit adjacent-layer joint cut law; this quantitative joint law is the claimed result, not the abstract existence statement.

Set \(w_j=1/(j-1)\) for \(2\le j\le n\). For a list \(w_{j+1},\ldots,w_n\), write \(e_s(j+1)\) for its degree-\(s\) elementary symmetric polynomial, with \(e_0=1\) and \(e_s=0\) for out-of-range indices. Define, whenever \(0\le b\le n-j+1\),
\[
p_j(b)=\frac{w_j e_{b-1}(j+1)}{e_b(j+1)+w_j e_{b-1}(j+1)}.
\]
For each \(0\le r\le n-2\), each \(r\)-subset \(S\subseteq\{2,\ldots,n\}\), and each \(h\notin S\), put \(b_j=r-|S\cap\{2,\ldots,j-1\}|\). Then the following product is the *exact* probability of the ordered pair of cut sets \((S,S\cup\{h\})\) at consecutive ranks \(r\) and \(r+1\):
\[
Q_{n,r}(S,h)=
\left[\prod_{\substack{2\le j<h\\j\in S}}p_j(b_j)\right]
\left[\prod_{\substack{2\le j<h\\j\notin S}}(1-p_j(b_j+1))\right]
(p_h(b_h+1)-p_h(b_h))
\left[\prod_{\substack{h<j\le n\\j\in S}}p_j(b_j)\right]
\left[\prod_{\substack{h<j\le n\\j\notin S}}(1-p_j(b_j))\right].
\]
All terms are rational and nonnegative. If \(Z_r=e_r(2)\), its exact marginals satisfy
\[
\sum_{h\notin S}Q_{n,r}(S,h)=\frac{\prod_{j\in S}w_j}{Z_r},\qquad
\sum_{h\in T}Q_{n,r}(T\setminus\{h\},h)=\frac{\prod_{j\in T}w_j}{Z_{r+1}}
\]
for each \(r\)-subset \(S\) and \((r+1)\)-subset \(T\).

## Assumptions and scope
Finite labeled set \([n]\), arbitrary integer \(n\ge2\), and exactly \(k\) nonempty blocks for each \(1\le k\le n\). Neither consistency across different set sizes nor time-homogeneity of the resulting partition chain is asserted. All weights are positive.

## Proof
**Weighted subsets.** Give an \(r\)-subset \(S\) of \(\{2,\ldots,n\}\) probability proportional to \(\prod_{j\in S}w_j\). Sequentially inspect \(j=2,\ldots,n\), keeping a remaining inclusion budget \(b\). Elementary-symmetric decomposition gives conditional inclusion probability \(p_j(b)\) above. Newton's inequalities imply the required log-concavity \(e_b^2\ge e_{b-1}e_{b+1}\), hence \(p_j(b)\) is nondecreasing in \(b\) including the deterministic boundary cases.

**Simultaneous construction.** Run this conditional sampler for all starting budgets \(r=0,\ldots,n-1\), using the *same* independent uniform random number at each inspection index \(j\). For adjacent budgets differing by one, the indicators are ordered; before their first difference their residual budgets remain one apart, at their first difference the budgets become equal, and thereafter their indicators coincide. Thus consecutive cut sets differ by precisely one additional point. At indices before the extra cut \(h\), the shared-uniform probabilities for common inclusions and common exclusions are respectively \(p_j(b_j)\) and \(1-p_j(b_j+1)\); at \(h\) the asymmetric inclusion probability is \(p_h(b_h+1)-p_h(b_h)\); afterwards the residual budgets agree. Multiplication of these conditional factors establishes \(Q_{n,r}(S,h)\). Summing its rows and columns gives the displayed weighted-subset marginals because each run has its prescribed conditional product law.

**From cuts to Gibbs partitions.** Take one independent uniform permutation of the labels \([n]\) and split its sequence before the positions in each nested cut set. Regard the resulting consecutive blocks as an unordered partition. Nested cuts give genuine successive refinement by a single split. To verify the exact \(k\)-block law independently, fix a partition with sizes \(b_1,\ldots,b_k\). For a particular order of these blocks there are \(\prod_i b_i!\) label permutations. The cut weight associated with that order is \(\prod_{t=1}^{k-1}(b_{\sigma(1)}+\cdots+b_{\sigma(t)})^{-1}\). The elementary identity
\[
\sum_{\sigma\in\mathfrak S_k}\prod_{t=1}^{k-1}\frac1{b_{\sigma(1)}+\cdots+b_{\sigma(t)}}=\frac{\sum_i b_i}{\prod_i b_i}
\]
follows by induction, grouping permutations by their last block (the empty product for \(k=1\) is 1). Consequently this partition's unnormalized probability is proportional to \(\prod_i b_i!\cdot n/\prod_i b_i=n\prod_i(b_i-1)!\). Normalization is \(c(n,k)\), proving the asserted Gibbs marginals. If a Markov partition process is desired, the adjacent refinement couplings may be disintegrated into Markov kernels; induction preserves each marginal and the one-split support.

## Verification
The standalone `verify.py` independently enumerates every cut set and label permutation through \(n=5\), checking each probability against the factorial Gibbs law (75 cases). It also checks 494 exact rational row and column sums of the adjacent-cut formula through \(n=8\), 2600 exact conditional-choice inequalities, and 1632 simulated adjacent refinement steps. Run `python verify.py` with the Python standard library. These finite checks support, but do not replace, the general analytic proof above.

## Relationship to prior work
Berestycki–Pitman (2005, revised 2006) studied Gibbs fragmentations and identified the factorial case as unresolved within their studied fragmentation families. Gnedin–Pitman (2006), Section 2 and end of Section 4, gave the independent binary-cut encoding of Ewens partitions and explicitly asked whether the factorial Gibbs marginals can be linked by one-split discrete fragmentation. Their continuous-parameter sampling rule does not itself retain these laws at its successive hitting times. Borcea–Brändén–Liggett's general result (as stated in Pemantle–Peres 2013, Proposition 2.3) already implies a covering coupling of consecutive fixed-cardinality conditionings of independent Bernoulli variables, so *abstract existence* of this fragmentation also follows by combining that theorem with the 2006 representation. We **do not claim** the existence consequence or the classical Gibbs/Ewens marginal formula as original. The concrete common-uniform, elementary-symmetric sampler and its exact pair-mass formula \(Q_{n,r}\) are the point asserted here.

## Limitations
This is an explicit finite-\(n\) construction, not a new characterization of all possible fragmentation kernels; Markovized kernels on unordered partitions are obtained by finite conditional sums, not reduced to a closed form depending only on block sizes. Generic conditional Poisson sampling and stochastic-covering theory are powerful prior results, and a previously published specialized algorithm or identical pair formula may exist. Such historical priority has not been independently certified. The checker is exhaustive only in stated finite ranges.

## References
1. N. Berestycki and J. Pitman, *Gibbs distributions for random partitions generated by a fragmentation process*, arXiv:math/0512378 (first publicly posted 2005-12-15), Sections 1 and 4.
2. A. Gnedin and J. Pitman, *Poisson representation of a Ewens fragmentation process*, arXiv:math/0608307 (first publicly posted 2006-08-12), Theorem 1 and Section 4.
3. R. Pemantle and Y. Peres, *Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures*, arXiv:1108.0687, Proposition 2.3 (quoting Borcea–Brändén–Liggett, Theorem 4.19).
