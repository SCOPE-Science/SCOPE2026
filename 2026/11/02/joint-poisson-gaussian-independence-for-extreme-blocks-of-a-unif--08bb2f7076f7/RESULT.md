# Joint Poisson–Gaussian independence for extreme blocks of a uniform noncrossing partition

## Finding
Let \(\mathcal P_n\) be uniform among the noncrossing partitions of \(\{1,\ldots,n\}\). Write \(K_n\) for its total block count and \(X_{n,r}\) for the count of blocks of size \(r\). Put \(b_n=\lfloor\log_2 n\rfloor\), \(\alpha_n=n2^{-b_n}\), and
\[
Z_n=\frac{K_n-(n+1)/2}{\sqrt{n/8}}.
\]
Along **every** integer subsequence for which \(\alpha_n\to\alpha\in[1,2]\), for any fixed finite set \(J\subset\mathbb Z\),
\[
\left(Z_n,(X_{n,b_n+j})_{j\in J}\right)
\ \xrightarrow{d}\
\left(Z,(P_j)_{j\in J}\right),
\qquad P_j\sim\operatorname{Poisson}(\alpha 2^{-j-1}),
\]
where all \(P_j\) are mutually independent and independent of \(Z\sim N(0,1)\).
In particular, writing \(L_n\) for the largest block size, jointly with \(Z_n\), for each fixed integer \(x\),
\[
\Pr(L_n-b_n\le x)\longrightarrow
\exp\bigl(-\alpha2^{-x-1}\bigr),
\]
and the centered maximum is asymptotically independent of the Gaussian block-count fluctuation. The maximum's marginal limit is previously known; the joint independence and rare-block vector are the focus here.

## Assumptions and scope
The partition law is exactly uniform on type-A noncrossing partitions, with no additional block-size conditioning. The index \(j\) is fixed while \(n\) varies; for sufficiently large \(n\), every \(b_n+j\) is positive. Since \(\alpha_n\) need not converge along the full sequence, the statement is explicitly subsequential. The Gaussian normalization is \(\sqrt{n/8}\), not the exact finite-sample standard deviation; the two are asymptotically equal. All limits concern \(n\to\infty\) along the specified subsequences.

## Proof
**1. Uniform weak-composition representation.** A block-size-preserving bijection sends a noncrossing partition of \([n]\) to a rooted ordered tree with \(n+1\) vertices, such that every size-\(r\) block corresponds to an outdegree-\(r\) vertex; see Kortchemski–Marzouk. The outdegrees \((d_1,\ldots,d_{n+1})\) in preorder satisfy \(d_i\ge0\) and \(\sum_i d_i=n\). The cycle lemma for increments \(d_i-1\) (total sum \(-1\)) says that exactly one of the \(n+1\) cyclic rotations of any weak composition of \(n\) produces the valid tree depth-first excursion. The rotations are distinct since a nontrivial period would require its length to divide both \(n\) and \(n+1\). Thus every statistic invariant under rotation, including the full degree-count profile, has the distribution of the corresponding profile of a **uniform weak composition of \(n\) into \(n+1\) slots**. In this representation \(X_{n,r}\) counts entries equal to \(r\) and \(K_n\) counts positive entries.

**2. Exact rare-block factorial moments.** Fix a finite \(J\) and nonnegative integers \((a_j)_{j\in J}\). Set \(a=\sum a_j\), \(r_j=b_n+j\), and \(R=\sum_j a_jr_j\). Selecting \(a\) ordered distinct specified slots, prescribing their sizes, and distributing the remaining \(n-R\) units among \(n+1-a\) slots yields, whenever \(R\le n\),
\[
\mathbb E\prod_{j\in J}(X_{n,r_j})_{\underline{a_j}}
=(n+1)_{\underline a}
\frac{\binom{2n-R-a}{n-a}}{\binom{2n}{n}}
=\frac{(n+1)_{\underline a}(n)_{\underline a}(n)_{\underline R}}
{(2n)_{\underline{R+a}}}.
\]
Here \((u)_{\underline q}=u(u-1)\cdots(u-q+1)\) and \((u)_{\underline0}=1\). Since \(a\) is fixed and \(R=O(\log n)\), a product expansion of each falling factorial gives
\[
\mathbb E\prod_{j\in J}(X_{n,r_j})_{\underline{a_j}}
=\left(1+O\left(\frac{(\log n)^2}{n}\right)\right)
\prod_{j\in J}(\alpha_n2^{-j-1})^{a_j}.
\]
Convergence of all multivariate factorial moments identifies independent Poisson limiting counts with the stated parameters.

**3. Gaussian block-count law under *every fixed factorial Palm marking*.** In the expectation weighted by \(\prod_j(X_{n,r_j})_{\underline{a_j}}\), the \(a\) marked entries have fixed sizes and the other \(m=n+1-a\) slots form a uniform weak composition of \(t=n-R\). Hence the total number of positive entries has exactly the law of \(a+Y_{m,t}\), where, for \(t\ge1\),
\[
\Pr(Y_{m,t}=k)
=\frac{\binom{m}{k}\binom{t-1}{k-1}}
{\binom{m+t-1}{m-1}}.
\]
This is the elementary hypergeometric representation
\[
Y_{m,t}\ \overset d=\ 1+H_{m,t},\qquad
H_{m,t}\sim\operatorname{Hypergeom}(m+t-1,m-1,t-1),
\]
where \(\operatorname{Hypergeom}(N,M,d)\) counts marked objects in \(d\) draws without replacement from \(N\) objects of which \(M\) are marked. Indeed, its mass function reduces to the preceding binomial coefficient ratio. Its exact first two moments are
\[
\mathbb E Y_{m,t}=\frac{mt}{m+t-1},\qquad
\operatorname{Var}(Y_{m,t})
=\frac{mt(m-1)(t-1)}{(m+t-1)^2(m+t-2)}.
\]
For the Palm parameters \(m=n+O(1)\), \(t=n-O(\log n)\), the expectation equals \(n/2+O(\log n)\) and the variance is \(n/8+o(n)\). The classical hypergeometric central limit theorem applies because the population success fraction and sample fraction both converge to \(1/2\), with all four contingency counts proportional to \(n\). It can alternatively be proved directly by Stirling's formula applied to the displayed exact mass function, with Gaussian central window and exponentially controlled tails. Consequently, for every fixed marking multi-index,
\[
\frac{a+Y_{m,t}-(n+1)/2}{\sqrt{n/8}}\xrightarrow{d}N(0,1).
\]
Taking a bounded continuous function \(g\), the exact Palm identity and the moment limit in Step 2 imply
\[
\mathbb E\left[g(Z_n)\prod_j(X_{n,r_j})_{\underline{a_j}}\right]
\longrightarrow \mathbb E[g(Z)]\prod_j(\alpha2^{-j-1})^{a_j}.
\]
The positive-count marginal itself has the same hypergeometric CLT by setting \(a=R=0\).

**4. Independence.** Fix \(J\) and any bounded continuous \(g\). The preceding mixed factorial-moment identities characterize the limiting tilted laws: their generating functions agree, coefficient by coefficient, with those of the product of the Gaussian law and the specified independent Poisson laws. Tightness of the count vector follows from its first factorial moments. Uniform integrability of any fixed polynomial in these counts follows from the next-order factorial-moment bounds, so no mass is lost on passing to subsequences. The multivariate Poisson law has an everywhere finite moment-generating function and is moment-determinate. Hence every joint subsequential limit has exactly the claimed independent product law, proving the first assertion.

**5. Maximum.** From the one-block expectation formula,
\[
\mathbb E X_{n,r}
=(n+1)\frac{\binom{2n-r-1}{n-1}}{\binom{2n}{n}},
\qquad
\frac{\mathbb EX_{n,r+1}}{\mathbb EX_{n,r}}
=\frac{n-r}{2n-r-1}\le\frac12
\]
for \(1\le r<n\). Also \(\mathbb EX_{n,1}\le n/2\) for \(n\ge2\), hence \(\mathbb EX_{n,r}\le n2^{-r}\). Therefore, for every fixed positive integer \(M\),
\[
\Pr\left(\exists r>b_n+M:X_{n,r}>0\right)
\le\sum_{r>b_n+M}n2^{-r}
=n2^{-(b_n+M)}\le2^{1-M}.
\]
The finite-vector joint limit in Step 4, applied to levels \(b_n+x+1,\ldots,b_n+M\), is independent of \(Z\), and the error caused by larger levels is bounded by \(2^{1-M}\). Letting \(M\to\infty\) gives the joint maximum/Gaussian independence and
\(\Pr(L_n-b_n\le x)\to\exp(-\sum_{j>x}\alpha2^{-j-1})=\exp(-\alpha2^{-x-1})\), as required.

## Verification
The standalone script `verify.py` uses exact integer and rational arithmetic to enumerate every noncrossing partition through \(n=8\), independently tests Catalan/Narayana counts, one- and two-block factorial-moment formulas, and checks the conditional positive-slot-count distribution using weak-composition enumeration. It reports **824 successful exact finite assertions** and six numerical scale comparisons; these do not substitute for the analytic subsequential limit and independence proof.

## Relationship to prior work
Arizmendi (2012) derived expected numbers of blocks of fixed sizes and conditional formulas. Kortchemski and Marzouk (2015) established the noncrossing-partition/plane-tree bijection and fixed-degree count limit theorems. Janson (2011) developed the random-allocation framework and extreme-degree marginal laws in plane trees (especially Example 18.17). Kargin (2019) established the block-count Gaussian marginal, fixed-size block-count Gaussian marginals, and the largest-block marginal limit for uniform noncrossing partitions. The new statement here is a **single joint limit** identifying independence of a global Gaussian fluctuation from *multiple logarithmic-size rare block counts*, with independence of the maximum as a corollary. No priority is claimed for the marginal limit laws, the plane-tree bijection, or the classical hypergeometric CLT.

## Limitations
The finding is restricted to the uniform type-A model and fixed finite sets of shifts \(J\). It does not assert process convergence in an infinite-dimensional topology, quantitative convergence rates, or joint independence for nonuniform simply generated weights. The lattice effect prevents a single unqualified full-sequence extreme-size limit. Although relevant primary work was inspected, a general rare-event/random-allocation theorem elsewhere could give an equivalent consequence; independent historical-priority assessment has not been performed.

## References
- O. Arizmendi, *Statistics of blocks in k-divisible non-crossing partitions*, arXiv:1201.6576 (first posted January 31, 2012), https://arxiv.org/abs/1201.6576.
- S. Janson, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510 (December 2, 2011), https://arxiv.org/abs/1112.0510; particularly §18 and Example 18.17.
- I. Kortchemski and C. Marzouk, *Simply generated non-crossing partitions*, arXiv:1503.09174 (March 31, 2015), https://arxiv.org/abs/1503.09174.
- V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632 (July 1, 2019), https://arxiv.org/abs/1907.00632.
