# Dependence and birth-label limits for direct leaf children in recursive trees

## Finding

In a uniform recursive tree on birth labels \(1,\ldots,n\), write \(Y_j\) for the number of final leaves directly attached to vertex \(j\). For \(n\ge3\) and \(1\le j<k\le n\),
\[
\operatorname{Cov}(Y_j,Y_k)=-\frac{(n-k)(n+j-2)}{(n-1)^2(n-2)}.
\]
The covariance is strictly negative if \(k<n\); \(Y_n=0\). In contrast, distinct possible leaf-child indicators of the same parent have positive covariance \(1/((n-1)^2(n-2))\).

For every fixed \(d\), if \(j_{1,n},\ldots,j_{d,n}\) are distinct and \(j_{s,n}/n\to u_s\in[0,1]\), then
\[
(Y_{j_{1,n}},\ldots,Y_{j_{d,n}})\Rightarrow (Z_1,\ldots,Z_d),\qquad
Z_s\text{ independent},\quad Z_s\sim\operatorname{Poisson}(1-u_s).
\]

A protected vertex is nonleaf and has no direct leaf child. Its probability at label \(j\) is
\[
p_{n,j}=\sum_{r=0}^{n-j}(-1)^r\binom{n-j}{r}\frac{1}{(n-1)_{\underline r}}-\frac{j-1}{n-1},
\qquad (n-1)_{\underline r}=\frac{(n-1)!}{(n-1-r)!}.
\]
For \(n\ge3\), \(p_{n,1}>\cdots>p_{n,n-1}=p_{n,n}=0\), and if \(j/n\to u\), then \(p_{n,j}\to e^{u-1}-u\). The root and aggregate protection formulas, and the leaf-parent cylinder identity used in the proof, are not claimed as new.

## Assumptions and scope

At each time \(i=2,\ldots,n\), \(P_i\) is the parent of \(i\), chosen independently and uniformly from \(\{1,\ldots,i-1\}\). A leaf has no children. The protection formula is for \(n\ge2\), including the boundary labels; the Poisson law is only for a fixed number of distinct parents, not a vector of growing dimension. The direct-child statistic is different from counting leaves among all descendants of a vertex.

## Proof

**Cylinder computation.** Put \(E_{j,i}=\mathbf 1\{P_i=j,\ i\text{ is a leaf}\}\) for \(j<i\). For proposed marked child labels \(S=\{i_1<\cdots<i_r\}\subseteq\{2,\ldots,n\}\), the earlier leaf-set identity [1, Eq. (1)] is
\[
\mathbb P(S\text{ consists of leaves})=\prod_{s=1}^r\frac{i_s-s}{n-s}.
\]
Indeed the leaf event restricts each parent choice to exclude the earlier members of \(S\); the uniform choices remain independent on the allowed sets. Conditional on this event, the allowed set for \(P_{i_s}\) has size \(i_s-s\). If all proposed parents \(j_s<i_s\) lie outside \(S\), their conditional joint probability is \(\prod_s(i_s-s)^{-1}\); otherwise it is zero. Multiplication gives the cylinder probability \(1/(n-1)_{\underline r}\) for compatible prescriptions and zero otherwise. A child assigned two distinct parents is also impossible. The root-only marked identity is explicit in [2].

**Fixed-point representation for one parent.** With parent \(j\) fixed, every collection of distinct proposed children \(i>j\) is compatible. For a uniform permutation of size \(n-1\), the probability of fixing \(r\) prescribed coordinates is also \(1/(n-1)_{\underline r}\). Inclusion-exclusion therefore identifies the whole indicator vector \((E_{j,i}:i>j)\) with the fixed-point indicators on the coordinates \(j,\ldots,n-1\) of that permutation. In particular \(\mathbb E Y_j=(n-j)/(n-1)\).

**Cross-parent dependence.** For \(j<k\), a possible mark \((j,i)\) pairs with a mark \((k,h)\), \(h>k\), precisely when \(i\ne k,h\). Thus for each of the \(n-k\) choices of \(h\) there are \(n-j-2\) compatible choices of \(i\). Applying the two-mark identity and subtracting the product of the means gives the covariance above. For two different children of one parent the two-mark event is always compatible, and the difference \(1/((n-1)(n-2))-1/(n-1)^2\) is positive.

**Joint limit.** For fixed factorial orders \(r_s\ge0\), let \(r=\sum_s r_s\). For \(r>0\), the candidate assignments in the expansion of \(\mathbb E\prod_s(Y_{j_{s,n}})_{\underline{r_s}}\) have count \(\prod_s(n-j_{s,n})^{r_s}+O_{r,d}(n^{r-1})\) after incompatible assignments are removed. A repeated child or a child equal to one of the participating parents fixes at least one otherwise free label, so these exclusions cost at most \(O_{r,d}(n^{r-1})\) uniformly in the parent indices. Each surviving tuple has probability \(1/(n-1)_{\underline r}\), for all sufficiently large \(n\). This gives convergence to \(\prod_s(1-u_s)^{r_s}\), including vanishing means. The zeroth moment is one. Ordinary mixed moments follow by expressing powers as linear combinations of falling factorials. The product-Poisson law is moment determinate by its moment generating function, giving the stated weak limit.

**Protection.** Inclusion-exclusion in the fixed-point representation gives the alternating sum for the probability of no direct leaf child. The event that \(j\) itself is a leaf is a subset of that event and has probability \((j-1)/(n-1)\), so subtracting gives \(p_{n,j}\). Going from \(j\) to \(j+1\) removes coordinate \(j\) from the constrained set. The increase in the no-fixed-point probability equals the probability that coordinate \(j\) alone among the previously constrained coordinates is fixed. The leaf-probability increment is \(1/(n-1)\), the probability that coordinate \(j\) is fixed at all. Hence \(p_{n,j}-p_{n,j+1}\) is the probability that coordinate \(j\) and at least one other constrained coordinate are fixed. This is positive for \(j\le n-2\) and zero for \(j=n-1\). Finally \(\binom{n-j}{r}/(n-1)_{\underline r}\) is at most \(1/r!\) and tends to \((1-u)^r/r!\) for fixed \(r\); dominated convergence gives the stated limit after subtracting the leaf probability.

## Verification

The accompanying standard-library script `verification/verify_leaf_parents.py` enumerates recursive trees through order eight. It checks cylinders through three marks, single-parent indicator vectors, cross-parent covariances, and label-specific protection probabilities. The recorded output is `TOTAL_EXACT_ASSERTIONS 6196`. These checks are finite; the counting, moment and inclusion-exclusion arguments establish the general statements.

## Relationship to prior work and limitations

The use of the conditional parent choices in [1] makes the arbitrary-parent cylinder law a direct consequence of the earlier leaf-set law, and the restricted fixed-point representation follows by inclusion-exclusion. The focus here is the finite sign contrast between direct-child dependence within and across parents, the simultaneous fixed-dimensional Poisson limit as a function of deterministic birth labels, and the birth-label resolution of protection. Devroye and Janson [3, §7] derive a Poisson direct-leaf-child count for the root of a continuous-time Yule tree at deterministic age, a precursor to the scalar mean profile, and use random fringe-tree age for protected proportions. That setup does not give the simultaneous deterministic-label finite-tree law. Mahmoud and Ward [4, Theorem 2.1 and Eq. (2.4)] give the exact aggregate mean and the root probability; those cases are not contributions here. Mahmoud and Smythe [5] is a related historical source on leaves in rooted subtrees, for which full-text comparison remains incomplete.

## References

1. *The oldest leaves of random recursive trees form a Poisson point process*, Resultary record `0a1a1c4bbf35`, Eq. (1) and Proof §1 (2026-10-18).
2. *Exact joint leaf law at the root of a uniform recursive tree*, Resultary record `4490954b5d10`, Proof §1 (2026-10-13).
3. L. Devroye and S. Janson, *Protected nodes and fringe subtrees in some random trees*, Electron. Commun. Probab. 19 (2014), article 6, doi:10.1214/ECP.v19-3048; arXiv:1310.0665, §7.
4. H. M. Mahmoud and M. D. Ward, *Asymptotic properties of protected nodes in random recursive trees*, J. Appl. Probab. 52 (2015), 290–297, doi:10.1239/jap/1429282623.
5. H. M. Mahmoud and R. T. Smythe, *On the distribution of leaves in rooted subtrees of recursive trees*, Ann. Appl. Probab. 1 (1991), 406–418, doi:10.1214/aoap/1177005874.
