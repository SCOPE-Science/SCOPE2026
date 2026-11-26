# Sharp three-category ceiling for pairwise-independent occupancy parities

## Finding

Let \(n\ge1\) independent trials have the same categorical distribution, with \(m\ge2\) distinguished categories of positive probabilities \(p_1,\ldots,p_m\), \(\sum_i p_i\le1\), and an untracked residual category of probability \(p_0=1-\sum_i p_i\). Write \(N_i\) for the count in category \(i\) and \(B_i=\mathbf1_{\{N_i\text{ is odd}\}}\). For distinct \(i,j\),
\[
\operatorname{Cov}(B_i,B_j)=\frac{(1-2p_i-2p_j)^n-[(1-2p_i)(1-2p_j)]^n}{4}.
\tag{1}
\]
For odd \(n\) this covariance is strictly negative. For even \(n\) its sign is the sign of \(p_i+p_j-p_ip_j-\tfrac12\); in particular, \(B_i,B_j\) are independent exactly when \((1-p_i)(1-p_j)=\tfrac12\).

A subfamily of at least three distinguished indicators is pairwise independent if and only if \(n\) is even, the subfamily has exactly three members, and each of those three categories has probability \(p_*:=1-1/\sqrt2\). The three are never jointly independent. Additional categories outside such a subfamily are allowed: their total probability, including the untracked residual, must be \(1-3p_*=3/\sqrt2-2\). In particular, if **all** distinguished indicators are pairwise independent and \(m\ge3\), then \(m=3\) and the unique probability vector is \(p_1=p_2=p_3=p_*\), \(p_0=3/\sqrt2-2\).

For \(m\ge4\), the two least probable distinguished categories have strictly negative covariance for every \(n\). The bound on the number of categories with all pairwise covariances nonnegative is sharp: \(m=3\) and \(p_i=1/3\) give three positive covariances for every positive even \(n\).

## Assumptions and scope

The probabilities are identical across trials, and the trials are independent. All distinguished probabilities are positive; the untracked probability may be zero. The indicators are parity indicators, not indicators of whether the category has ever appeared. Pairwise independence refers to all pairs **within the specified family**; it need not hold between an indicator in that family and a category outside it.

## Proof

For any subset \(S\) of distinguished labels, a single trial contributes a factor \(-1\) to \((-1)^{\sum_{i\in S}N_i}\) if its label is in \(S\), and \(+1\) otherwise. By independence,
\[
\mathbb E\left[(-1)^{\sum_{i\in S}N_i}\right]
=\left(1-2\sum_{i\in S}p_i\right)^n.
\tag{2}
\]
Apply this to singletons and pairs, using \((-1)^{N_i}=1-2B_i\), to obtain (1). Put \(a=1-2(p_i+p_j)\), \(b=(1-2p_i)(1-2p_j)=a+4p_ip_j\). Since \(a<b\), strict monotonicity of the odd power gives the odd case. For even \(n\) compare \(a^2\) with \(b^2\), since \(u\mapsto u^{n/2}\) is strictly increasing for \(u\ge0\). Factoring gives
\[
a^2-b^2=16p_ip_j\left(p_i+p_j-p_ip_j-\tfrac12\right).
\tag{3}
\]
For two Bernoulli variables zero covariance gives independence: the probability of \((1,1)\) is then the product of the marginals, which also determines the other three entries of the joint table. For even \(n\) the independence locus can equivalently be written as
\[
0<p_i<\tfrac12,\qquad p_j=\frac{1/2-p_i}{1-p_i}.
\]
These weights leave positive probability for the other labels or the residual.

For a specified pairwise-independent family of at least three labels, odd \(n\) is impossible. In even \(n\), all the products \((1-p_i)(1-p_j)\) within the family must be \(1/2\). Comparison of two products with one common index forces the other weights to agree, since all \(1-p_i>0\). Thus every weight in the family equals the unique admissible root \(p_*=1-1/\sqrt2\) of \((1-p)^2=1/2\). The inequalities \(3p_*<1<4p_*\) make a triple feasible and a larger family impossible. Conversely any three labels with those weights satisfy the pair criterion for even \(n\), regardless of how the remaining probability is split outside the triple. For example, with four distinguished categories one may set \(p_1=p_2=p_3=p_*\), \(p_4=1-3p_*\) and \(p_0=0\); the first three are pairwise independent at even \(n\), but not all four are.

To see why the triple is not jointly independent, write \(Z_i=1-2B_i\) on its three labels. The triple moment from (2) at positive even \(n\) is \((5-3\sqrt2)^n\); the product of three singleton moments is \((\sqrt2-1)^{3n}=(5\sqrt2-7)^n\). The two bases are positive and the first is strictly larger because \(3>2\sqrt2\). The moment does not factor.

Finally, order the distinguished weights increasingly. For \(m\ge4\) the sum of the first two is at most twice the mean weight, hence at most \(2/m\le1/2\). Subtracting their strictly positive product puts the pair strictly below the even-case threshold in (3), and odd \(n\) was already resolved. For a uniform triple, \(p_i+p_j-p_ip_j=5/9>1/2\), giving sharpness at every positive even \(n\).

## Verification

The arbitrary-parameter argument is the character calculation (2), the exact sign factorization (3), and the probability-budget and triple-moment comparisons. The accompanying `verify.py` provides supplementary finite checks: exact rational enumeration for several category distributions and sample sizes one through six, and symbolic checks of the three-category moment relations for positive even sizes through 200. Its finite checks do not prove any unrestricted assertion and are not needed for the subfamily quantifier.

## Relationship to prior work

Multinomial negative-association theorems and empty-bin negative dependence apply to monotone transforms of the counts, whereas parity alternates with count. Fixed-frequency occupancy bounds address different indicators or aggregate statistics. The multinomial generating function makes (2) a standard specialization; the contribution here is the explicit covariance sign and independence feasibility classification, not the transform identity itself. Equivalent earlier deductions are possible; these comparisons do not establish historical priority.

## Limitations

The conclusions require a fixed categorical law, independent trials and parity modulo two. They do not address arbitrary dependent allocations, stopping rules or other moduli.

## References

- K. Joag-Dev and F. Proschan, “Negative Association of Random Variables with Applications,” *Annals of Statistics* **11** (1983), 286–295. DOI: 10.1214/aos/1176346079.
- D. Dubhashi and D. Ranjan, “Balls and Bins: A Study in Negative Dependence,” *BRICS Report Series* **3** (1996), no. 25. DOI: 10.7146/brics.v3i25.20006.
- J. Bartroff and L. Goldstein, “A Berry-Esseen bound for the uniform multinomial occupancy model,” arXiv:1202.0909.
