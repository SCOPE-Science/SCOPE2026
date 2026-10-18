# Exact negative covariance of right-spine length and total path length in random binary search trees

## Finding
For every integer \(n\ge 1\), insert a uniformly random permutation of \(\{1,\ldots,n\}\) into an initially empty binary search tree. Let \(P_n\) be the sum of all root-to-node edge depths, with root depth zero, and let \(R_n\) be the number of nodes along the all-right branch starting at the root, including the root. Write \(H_n=\sum_{j=1}^{n}1/j\) and \(H_n^{(2)}=\sum_{j=1}^{n}1/j^2\). Then
\[
\operatorname{Cov}(P_n,R_n)=3n+H_n-2(n+1)H_n^{(2)}.
\]
The covariance is zero at \(n=1,2\), strictly negative for every \(n\ge3\), and decreases strictly as a function of \(n\) from that point onward. Moreover,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(P_n,R_n)}{n}=3-\frac{\pi^2}{3}<0,
\quad
\operatorname{Corr}(P_n,R_n)\sim
\frac{3-\pi^2/3}{\sqrt{7-2\pi^2/3}}\,\frac1{\sqrt{\log n}}.
\]
Thus the unscaled covariance has a nonzero negative linear-order limit, although the standardized correlation vanishes. As a local model-sensitivity interpretation, weighting insertion permutations by \(\theta^{R_n}\) yields
\[
\left.\frac{\partial}{\partial\log\theta}\,\mathbb E_\theta P_n\right|_{\theta=1}
=3n+H_n-2(n+1)H_n^{(2)}.
\]
In particular a small positive record bias strictly *decreases* the mean path length to first order whenever \(n\ge3\).

## Assumptions and scope
The insertion order is uniformly distributed over all permutations of distinct keys. There are \(n\) internal nodes; only root-to-internal-node edge depths are summed. The right spine is the path obtained by repeatedly following a right-child pointer until none remains. This spine has the same length as the number of strict left-to-right upper records of the insertion permutation. It is **not** the maximum tree height, nor the number of all right children. The convention is \(P_0=R_0=0\). Every identity except the limiting statements is finite-sample and exact. The usual first-pivot Quicksort comparison count on the same ordered input coincides with \(P_n\) with the corresponding recursive partition convention.

## Proof
**Root decomposition.** The first inserted key has rank \(K\), uniformly distributed on \(\{1,\ldots,n\}\). Given \(K=k\), the left and right subtrees, of sizes \(k-1\) and \(n-k\), have independent uniform random-binary-search-tree laws. Writing \(L=k-1\) and \(Q=n-k\),
\[
P_n=P_L+P'_Q+n-1,\qquad R_n=1+R'_Q.
\]
Indeed a left-subtree entry cannot exceed the root and so cannot become a record; every upper record after the first belongs to, and is an upper record within, the subsequence of keys exceeding the root.

**First moments.** Set \(a_n=\mathbb EP_n\), \(b_n=\mathbb ER_n\), and \(e_n=\mathbb E(P_nR_n)\), all zero when \(n=0\). Root splitting gives
\[
a_n=n-1+\frac2n\sum_{j=0}^{n-1}a_j,
\quad b_n=1+\frac1n\sum_{j=0}^{n-1}b_j.
\]
These recurrences, with their initial conditions, yield the exact identities
\[
a_n=2(n+1)H_n-4n,\qquad b_n=H_n.
\]

**Mixed moment.** Multiplying the two root decompositions and conditioning on the split, including the left subtree contribution, gives
\[
e_n=a_n+\frac1n\sum_{r=0}^{n-1}
\left[e_r+(a_{n-1-r}+n-1)b_r\right]\qquad(n\ge1).
\]
This identity is the essential joint-moment step; a covariance obtained by treating the two subtrees or the two statistics as independent would be wrong.

Introduce ordinary generating functions \(A(z)=\sum_{n\ge0}a_nz^n\), \(B(z)=\sum_{n\ge0}b_nz^n\), and \(E(z)=\sum_{n\ge0}e_nz^n\). They are absolutely convergent for \(|z|<1\) and can alternatively be treated as formal power series. Writing \(\ell(z)=\log(1-z)\), the first-moment formulas imply
\[
B(z)=-\frac{\ell(z)}{1-z},\qquad
A(z)=-\frac{2(z+\ell(z))}{(1-z)^2}.
\]
Summing the mixed recurrence after multiplying by \(z^{n-1}\) gives the first-order differential equation
\[
E'(z)-\frac{E(z)}{1-z}=A'(z)+A(z)B(z)+z\left(\frac{B(z)}{1-z}\right)'.
\]
The uniquely determined formal solution with \(E(0)=0\) is
\[
E(z)=\frac{1-\ell(z)}{1-z}+\frac{2\ell(z)^2-1}{(1-z)^2}.
\]
Differentiating the displayed formula verifies the equation directly, so this generating-function step requires no unjustified convergence exchange.

The standard harmonic coefficient identity, obtained by twice differentiating \((1-z)^{-\alpha}\) at \(\alpha=2\), is
\[
[z^n]\frac{\ell(z)^2}{(1-z)^2}
=(n+1)\left((H_{n+1}-1)^2-(H_{n+1}^{(2)}-1)\right).
\]
Taking coefficients of \(E(z)\) and substituting \(H_{n+1}=H_n+1/(n+1)\) and \(H_{n+1}^{(2)}=H_n^{(2)}+1/(n+1)^2\) yields
\[
e_n=2(n+1)H_n^2+(1-4n)H_n+3n-2(n+1)H_n^{(2)}.
\]
Subtracting \(a_nb_n\) cancels the squared harmonic term and proves the claimed exact covariance.

**Strict sign and sharp asymptotics.** Denote the covariance by \(c_n\). Direct subtraction gives, for \(n\ge2\),
\[
c_{n+1}-c_n=3-2H_n^{(2)}-\frac{n+3}{(n+1)^2}.
\]
Let \(u_n=2H_n^{(2)}+(n+3)/(n+1)^2\). Then \(u_2=55/18>3\) and \(u_{n+1}-u_n=n/((n+1)(n+2)^2)>0\). Hence \(c_n\) strictly decreases from \(c_2=0\), proving strict negativity for \(n\ge3\). Since \(H_n=O(\log n)\) and \(H_n^{(2)}\to\pi^2/6\), division by \(n\) yields the first limit.

For the correlation, the independent-record-indicator representation gives \(\operatorname{Var}(R_n)=H_n-H_n^{(2)}\sim\log n\). The classical random-BST internal-path-length variance identity is
\[
\operatorname{Var}(P_n)=7n^2+13n-2(n+1)H_n-4(n+1)^2H_n^{(2)}
\sim\left(7-\frac{2\pi^2}{3}\right)n^2.
\]
It is also obtainable by squaring the same root recursion; its leading-order value is recorded by Aguech, Amri and Sulzbach. Both variance coefficients are positive for \(n\ge3\); combining them with \(c_n\) yields the claimed correlation equivalent.

**Local record-bias derivative.** For \(\theta>0\), define \(\mathbb P_\theta(\pi)=\theta^{R(\pi)}/\sum_{\sigma\in S_n}\theta^{R(\sigma)}\). Differentiating this finite partition function shows, for any statistic \(X\), that \(\partial_{\log\theta}\mathbb E_\theta X=\operatorname{Cov}_\theta(X,R)\); insert \(X=P_n\) and \(\theta=1\).

## Verification
The standalone file `verify.py` independently computes \(P_n\) from the depth traversed during each insertion and \(R_n\) from strict record maxima, exhaustively enumerates every insertion permutation for \(1\le n\le8\), and compares exact rational mixed moments with the closed formula. Independently it evaluates the root-decomposition recurrence for \(1\le n\le100\), verifies the first-moment formulas and the exact covariance at each size, and checks the strict-sign step algebraically in rational arithmetic for a finite diagnostic range. This is a check of small instances and recurrences; the proof above supplies the infinite-sample derivation.

## Relationship to prior work
Corsini, *The height of record-biased trees* (initial arXiv release on 10 December 2021, arXiv:2112.05732) studies the model obtained by weighting permutations by their record count; its key objectives are the height and subtree-size bounds, not a finite-sample mixed moment between the total internal path length and the rightmost branch. The full author-hosted manuscript was inspected, including the model decomposition, main height theorems and concluding discussion.

Aguech, Amri and Sulzbach, *On Weighted Depths in Random Binary Search Trees* (publicly available 11 July 2017, DOI 10.1007/s10959-017-0773-1) prove weighted depth/path-length/Wiener results. Their full open article explicitly recalls the ordinary internal-path-length variance and gives mixed moments involving weighted path length and the Wiener index; it does not state the right-spine/path-length covariance above. These prior results supply essential background, but do not imply the exact joint law without additional computation.

Bouvel, Nicaud and Pivoteau, *Record-biased permutations and their permuton limit* (arXiv:2409.01692, first posted 3 September 2024), studies record-biased permutation statistics and permuton limits. Accessible abstracts and scholarly metadata were inspected; their complete preprint text was not conclusively compared, leaving a residual historical-priority risk. Earlier work on record-biased permutations and classical random-BST path lengths supplies the two separate ingredients, but a marginal formula for either does not determine their covariance. Published mathematical results on root split imbalance versus total path length and random recursive tree attachment indicators describe distinct statistics and do not imply this finite two-statistic identity.

## Limitations
The result concerns uniform random distinct-key insertion and the local derivative at the unbiased parameter. It does not assert monotonicity of mean path length for all positive record-bias parameters, a distributional limit for the pair, or a new formula for ordinary path-length variance. The originality assessment is based on accessible inspected primary texts, mathematical research searches and comparison to documented related results, not an exhaustive mathematical-priority guarantee. No independent audit has been performed.

## References
1. B. Corsini, *The height of record-biased trees*, arXiv:2112.05732, first posted 2021-12-10. Author-hosted full text: https://benoitcorsini.com/files/articles/corsini_2021_rbt.pdf.
2. R. Aguech, A. Amri and H. Sulzbach, *On Weighted Depths in Random Binary Search Trees*, *Journal of Theoretical Probability* 31 (2018), 1929–1951. Online first 2017-07-11. DOI: https://doi.org/10.1007/s10959-017-0773-1.
3. M. Bouvel, C. Nicaud and C. Pivoteau, *Record-biased permutations and their permuton limit*, arXiv:2409.01692, first posted 2024-09-03.
4. N. Auger, M. Bouvel, C. Nicaud and C. Pivoteau, *Analysis of Algorithms for Permutations Biased by Their Number of Records*, arXiv:1605.02905, 2016 (background; does not treat random-BST internal-path-length covariance).
