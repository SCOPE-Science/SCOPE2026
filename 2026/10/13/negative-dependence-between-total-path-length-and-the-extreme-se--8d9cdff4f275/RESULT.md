# Negative dependence between total path length and the extreme search path in random binary search trees

## Finding

Let a binary search tree be constructed by inserting a uniformly random permutation of the distinct keys \(1,\ldots,n\), with \(n\geq1\). Let \(P_n\) be the *internal path length*: the sum of the edge depths of all keys, with the root at depth zero. Let \(R_n\) be the number of nodes inspected in a successful search for the maximum key (the number of nodes on the rightmost path, including the root). Write
\[
H_n=\sum_{j=1}^n\frac1j,\qquad H_n^{(2)}=\sum_{j=1}^n\frac1{j^2},\qquad H_0=H_0^{(2)}=0.
\]
Then for every integer \(n\geq1\),
\[
\boxed{\operatorname{Cov}(P_n,R_n)=3n+H_n-2(n+1)H_n^{(2)}.}
\]
The covariance vanishes exactly at \(n=1,2\) and is **strictly negative for every \(n\geq3\)**. In particular,
\[
\operatorname{Cov}(P_n,R_n)
 =\left(3-\frac{\pi^2}{3}\right)n+\log n
 +\gamma+2-\frac{\pi^2}{3}+O(n^{-1}),
\]
and its Pearson correlation, well-defined for \(n\geq3\), obeys
\[
\boxed{\operatorname{Corr}(P_n,R_n)\sim
\frac{3-\pi^2/3}{\sqrt{7-2\pi^2/3}}\,
\frac1{\sqrt{\log n}}\approx
-\frac{0.4471358767}{\sqrt{\log n}}.}
\]
Thus total construction cost and maximum-key successful-search cost are negatively dependent in covariance at every nondegenerate finite size, their covariance is of linear magnitude, but their correlation tends to zero.

## Assumptions and scope

All \(n!\) insertion orders are equiprobable; no rebalancing, duplicates, deletions, weighted keys, or alternative pivot selection are assumed. The tree is the ordinary random binary search tree. The total internal path length is also the number of key comparisons of first-pivot Quicksort on the same insertion permutation. The maximum-key search path is the number of strict upper records of that permutation: a key is on the rightmost spine exactly when it exceeds all previously inserted keys. The empty-subtree conventions used in recurrences are \(P_0=R_0=0\), without treating an empty tree as an instance of a successful search. These definitions specify exactly which search and cost conventions the covariance uses.

## Proof

**1. Recursive decomposition.** The root rank is uniform, and its right-subtree size \(J\) is uniform on \(\{0,\ldots,n-1\}\). Conditional on \(J=j\), the right and left subtrees are independent random binary search trees of sizes \(j\) and \(n-1-j\), respectively. Writing superscripts to distinguish independent subtree copies,
\[
P_n\overset d=(n-1)+P_j^{(r)}+P_{n-1-j}^{(l)},\qquad
R_n\overset d=1+R_j^{(r)}.
\]
The marginal means are the familiar identities
\[
p_j:=\mathbb E P_j=2(j+1)H_j-4j,\qquad
r_j:=\mathbb E R_j=H_j.
\]
The first follows by summing the path-length recurrence; the second follows either by the right-path recurrence or by independent upper-record indicators. Let \(K_n=\operatorname{Cov}(P_n,R_n)\), \(K_0=0\), and define
\[
a_j=p_j+p_{n-1-j},\qquad b_j=H_j,\qquad
 g_n=\operatorname{Cov}_{J}(a_J,b_J),
\]
where \(J\) is uniform on its \(n\) possible values. The law of total covariance, together with conditional subtree independence, gives the exact recurrence
\[
K_n=\frac1n\sum_{j=0}^{n-1}K_j+g_n.
\tag{1}
\]

**2. Exact mixed root term.** Direct finite harmonic summation gives
\[
\boxed{g_n=(n+1)\left(\frac32-H_n^{(2)}\right)-\frac{H_n}{n}.}
\tag{2}
\]
Here are explicit identities that verify the nonstandard finite-sum step, for \(n\geq2\):
\[
\sum_{j=0}^{n-1}H_j=n(H_n-1),
\]
\[
\sum_{j=0}^{n-1}H_jH_{n-1-j}
=n\left((H_n-1)^2+1-H_n^{(2)}\right),
\]
\[
\begin{aligned}
\sum_{j=0}^{n-1}(j+1)H_j^2
={}&\frac{n(n+1)}2H_{n-1}^2
-\frac{(n-1)(n+2)}2H_{n-2}\\
&+\frac{(n-2)(n+5)}4-\frac{n-1+H_{n-1}}2.
\end{aligned}
\]
For the convolution identity, \(\sum_{j\geq0}H_jz^j=-\log(1-z)/(1-z)\). Extract the coefficient of \(z^{n-1}\) from its square by differentiating the generalized binomial coefficient \([z^{n-1}](1-z)^{-\alpha}=(\alpha)_{n-1}/(n-1)!\) twice at \(\alpha=2\). The resulting logarithmic derivatives are \(H_n-1\) and \(-[H_n^{(2)}-1]\). For the weighted square identity, substitute \(H_j^2=\sum_{i=1}^j(2H_{i-1}/i+1/i^2)\), reverse the two finite sums, and use \(\sum_{j=i}^{n-1}(j+1)=[n(n+1)-i(i+1)]/2\), together with the elementary reversed sums for \(\sum H_j\) and \(\sum jH_j\). Finally, using symmetry under \(j\leftrightarrow n-1-j\),
\[
\sum_{j=0}^{n-1}a_jH_j
=2\sum_{j=0}^{n-1}(j+1)H_j^2
+(n+1)\sum_{j=0}^{n-1}H_jH_{n-1-j}
-4(n-1)\sum_{j=0}^{n-1}H_j.
\]
Also \(\frac1n\sum a_j=2(n+1)H_n-5n+1\) and \(\frac1n\sum H_j=H_n-1\). Substituting these finite identities into \(g_n=\frac1n\sum a_jH_j-(\frac1n\sum a_j)(\frac1n\sum H_j)\) proves (2). At \(n=1\), both sides of (2) equal zero.

**3. Solve the covariance recurrence.** If \(S_n=\sum_{j=0}^nK_j\), (1) implies \(S_n/(n+1)=S_{n-1}/n+g_n/(n+1)\). Therefore
\[
K_n=g_n+\sum_{j=1}^{n-1}\frac{g_j}{j+1}.
\]
Use (2) and the two finite telescoping identities
\[
\sum_{j=1}^{n-1}H_j^{(2)}=nH_{n-1}^{(2)}-H_{n-1},
\qquad
\sum_{j=1}^{n-1}\frac{H_j}{j(j+1)}
=H_{n-1}^{(2)}-\frac{H_{n-1}}n.
\]
An immediate simplification yields \(K_n=3n+H_n-2(n+1)H_n^{(2)}\), with no asymptotic approximation.

**4. Strict sign and structural explanation.** The sequence \(p_j\) is strictly discretely convex because \(p_{j+1}-p_j=2H_{j+1}-2\), increasing in \(j\). Hence the symmetric sequence \(a_j=p_j+p_{n-1-j}\) decreases strictly from an outer position toward the midpoint, up to its possible central tie. On the other hand the symmetric sequence \(b_j^*=(H_j+H_{n-1-j})/2\) increases strictly toward the midpoint: its successive difference on the left half is \((1/(j+1)-1/(n-1-j))/2>0\). Symmetry gives \(\operatorname{Cov}(a_J,H_J)=\operatorname{Cov}(a_J,b_J^*)\). The reversed rearrangement inequality shows \(g_n<0\) whenever \(n\geq3\), while \(g_1=g_2=0\). The recurrence (1) then gives \(K_n<0\) for every \(n\geq3\); \(K_1=K_2=0\) is immediate. At the root, a more extreme split raises expected total path length, whereas the average of right-path means across reflected splits is largest near balanced splits. Their opposition explains the negative mixed term at each recursive level.

**5. Asymptotic covariance and correlation.** Harmonic expansions imply \(H_n=\log n+\gamma+1/(2n)+O(n^{-2})\) and \(H_n^{(2)}=\pi^2/6-1/n+O(n^{-2})\), proving the stated covariance expansion with its constant term. The upper-record indicators are mutually independent, with success probabilities \(1/j\), so \(\operatorname{Var}(R_n)=H_n-H_n^{(2)}\sim\log n\). The classical Quicksort/path-length variance, independently available in the cited literature, is
\[
\operatorname{Var}(P_n)=7n^2+13n-2(n+1)H_n-4(n+1)^2H_n^{(2)}
\sim\left(7-\frac{2\pi^2}{3}\right)n^2.
\]
Both variances are positive for \(n\geq3\). Dividing the covariance by their geometric-mean standard deviation proves the correlation asymptotic.

## Verification

The companion standalone `verify.py` uses Python's standard library. Run `python verify.py`. It computes first-pivot comparison counts and independently inserts the same permutations into pointer-based search trees, enumerates all \(46{,}233\) permutations of sizes \(1\) through \(8\), and checks rational means, both marginal variances, and the mixed covariance against the formula. Separately, it recomputes the root-conditional covariance and recurrence in exact rational arithmetic for every size through \(120\), and checks a floating-point illustration of the asymptotic laws at size \(200{,}000\). Finite enumeration is not used to prove the all-size sign, the exact formula, or the limit; those follow from the displayed analytic argument.

## Relationship to prior work

The Quicksort expectation and variance are classical; Iliopoulos and Penman provide a self-contained calculation. Grübel gives limit laws and a strong-limit description for internal path length. Chern, Fuchs, Hwang and Neininger analyze mixed path-length and space-requirement fluctuations in multiway search trees, rather than the extreme-node search path in an ordinary binary search tree. Auger, Bouvel, Nicaud and Pivoteau study permutation records and record-weighted distributions, with applications to inversions, InsertionSort and Min/Max procedures. Corsini studies the height of record-biased trees, identifying records with their rightmost paths. Aguech, Amri and Sulzbach study weighted depths of selected nodes, including extreme keys, and weighted whole-tree path length, rather than their present unweighted mixed covariance. These works motivate, but do not state in the inspected materials, the exact mixed covariance here. The novelty claim is specifically the identity, its all-size negative sign, and its resulting decay of correlation—not the marginal record law, marginal Quicksort moments, or the BST–Quicksort equivalence.

## Limitations

This is a statement about the standard uniform-permutation binary search tree and the search for its **maximum** key. A random selected key, unsuccessful search, or balancing algorithm is not covered. The covariance does not determine the full joint distribution. Vanishing Pearson correlation does not by itself establish independence or any joint limit theorem. No assertion of exhaustive historical priority or independent certification is made; specialized older mixed-moment or record-weighted generating-function work could imply the identity. The exact signs and asymptotic limits are proved, while any stronger joint independence claim remains unproved here.

## References

1. V. Iliopoulos and D. Penman, *Variance of the number of Comparisons of Randomized Quicksort*, arXiv:1006.4063 (first posted 2010-06-21), https://arxiv.org/abs/1006.4063.
2. R. Grübel, *Search trees: Metric aspects and strong limit theorems*, arXiv:1209.2546 (first posted 2012-09-12), https://arxiv.org/abs/1209.2546.
3. H.-H. Chern, M. Fuchs, H.-K. Hwang and R. Neininger, *Dependence and phase changes in random \(m\)-ary search trees*, arXiv:1501.05135 (first posted 2015-01-21), https://arxiv.org/abs/1501.05135.
4. N. Auger, M. Bouvel, C. Nicaud and C. Pivoteau, *Analysis of Algorithms for Permutations Biased by Their Number of Records*, arXiv:1605.02905 (first posted 2016-05-10), https://arxiv.org/abs/1605.02905.
5. B. Corsini, *The height of record-biased trees*, Random Structures & Algorithms 62 (2023), 623–644; DOI: 10.1002/rsa.21110, https://doi.org/10.1002/rsa.21110.
6. R. Aguech, A. Amri and H. Sulzbach, *On Weighted Depths in Random Binary Search Trees*, Journal of Theoretical Probability 31 (2018), 1929–1951; DOI: 10.1007/s10959-017-0773-1, https://doi.org/10.1007/s10959-017-0773-1.
