# A sharp birth-time sign transition for leaf dependence in random recursive trees

## Finding

In a standard uniform random recursive tree, the covariance between the outdegree of a specified **nonroot** vertex and the total number of leaves has a sharp birth-time sign transition. Write \(D_{n,i}\) for the number of children of vertex \(i\ge2\), and \(L_n\) for the number of outdegree-zero vertices. For \(n\ge3\), \(2\le i\le n\), put \(N=n-1\), \(t=i-1\), and \(H_k=\sum_{r=1}^k 1/r\). Then

\[
\operatorname{Cov}(D_{n,i},L_n)
=\frac{(N-t)(N-2)}{2N^2}-\frac{t}{N}(H_N-H_t).
\tag{1}
\]

For \(4\le n\le6\) every nonterminal nonroot label has negative covariance. For every \(n\ge7\), the covariance at \(i=2\) is positive and at \(i=n-1\) is negative; as \(i\) increases over \(2,\ldots,n-1\), the sign can cross **only once**, from positive to negative (possibly via one zero). At \(i=n\), \(D_{n,n}=0\), so the covariance is zero.

If \(i/n\to x\in(0,1)\), then
\[
\operatorname{Cov}(D_{n,i},L_n)\longrightarrow f(x)
=\frac{1-x}{2}-x\log(1/x).
\]
The function \(f\) changes sign exactly once, at the unique \(x_*\in(0,1)\) solving \(2x_*\log(1/x_*)=1-x_*\), namely \(x_*=0.284668137040838\ldots\). Thus asymptotically the early positive regime occupies about \(28.47\%\) of birth labels; the rest are negative, apart from the terminal zero. No distributional stochastic ordering is claimed.

## Assumptions and scope

The labeled recursive tree is built by independently choosing, for every \(j\in\{2,\ldots,n\}\), a parent \(P_j\) uniformly from \(\{1,\ldots,j-1\}\). Leaves are **outdegree-zero** vertices. Since \(n\ge2\), the root is never a leaf. For nonroot vertices, graph degree differs from outdegree by the deterministic constant one, so the covariance statement also applies to ordinary graph degree at such a vertex. All finite-size statements refer to this uniform independent-parent model.

## Proof

Set \(Y_j=\mathbf1\{j\text{ has no children at time }n\}\), for \(j\ge2\). The independent-parent construction gives, by telescoping,
\[
\Pr(Y_j=1)=\prod_{k=j+1}^n\left(1-\frac1{k-1}\right)=\frac{j-1}{n-1}.
\tag{2}
\]
For a fixed nonroot \(i\), set \(A_{k,i}=\mathbf1\{P_k=i\}\), \(k>i\), so \(D_{n,i}=\sum_{k=i+1}^n A_{k,i}\). If \(j\ne i\) and \(k>\max\{i,j\}\), conditioning on \(A_{k,i}=1\) removes the possibility that \(k\) chooses \(j\), and independent parent choices give
\[
\operatorname{Cov}(A_{k,i},Y_j)
=\frac{j-1}{(n-1)(k-1)(k-2)}.
\tag{3}
\]
When \(k\le j\), the covariance is zero. In the self-label case, \(D_{n,i}Y_i=0\): a vertex with a child cannot be a leaf. Consequently
\[
\operatorname{Cov}(D_{n,i},Y_i)
=-\frac{i-1}{n-1}\sum_{k=i+1}^n\frac1{k-1}
=-\frac{t}{N}(H_N-H_t).
\tag{4}
\]
For \(j<i\), summing (3) over arrivals \(k>i\) gives
\[
\operatorname{Cov}(D_{n,i},Y_j)
=\frac{j-1}{N}\left(\frac1{i-1}-\frac1{n-1}\right)
=\frac{(j-1)(N-t)}{NtN}.
\]
Summing this over \(2\le j<i\) contributes \((t-1)(N-t)/(2N^2)\). For \(j>i\), summing (3) over \(k>j\) gives \((N-j+1)/N^2\), and summing over \(i<j\le n\) contributes \((N-t-1)(N-t)/(2N^2)\). The two off-diagonal contributions total \((N-t)(N-2)/(2N^2)\). Combining with (4) proves (1), including \(i=n\) by empty sums.

For \(1\le t<N\), factor the right side of (1) as
\[
\frac{N-t}{N}\left[\frac{N-2}{2N}-a_N(t)\right],\quad
 a_N(t)=\frac{t}{N-t}\sum_{r=t+1}^{N}\frac1r.
\tag{5}
\]
For \(t<N-1\), algebra yields
\[
a_N(t+1)-a_N(t)=\frac{N\sum_{r=t+1}^N1/r-(N-t)}{(N-t)(N-t-1)}>0,
\tag{6}
\]
since \(r\le N\) in every summand and at least one index is strictly less than \(N\). Thus the bracket in (5) is strictly decreasing and its sign crosses at most once. At \(t=N-1\), (1) equals \(-1/(2N)\). For the earliest nonroot vertex \(t=1\), positivity is equivalent to
\[
b_N=\frac{(N-1)(N-2)}{2N}-(H_N-1)>0.
\]
We have \(b_5<0\), \(b_6>0\), and \(b_{N+1}-b_N=1/2-1/N>0\) for \(N\ge3\). Direct substitution for \(N=3,4,5\) shows nonpositivity, in fact negativity. Hence positive covariance at \(i=2\) first appears at \(N=6\), or \(n=7\), and strictly negative covariance at the penultimate vertex persists. The terminal vertex is deterministically childless.

For \(i/n\to x\in(0,1)\), the harmonic difference converges to \(\log(1/x)\), proving the asserted scaling limit. To show its root is unique, observe \(x\log(1/x)/(1-x)\) is strictly increasing from \(0\) to \(1\) on \((0,1)\): writing \(y=1/x>1\), the reciprocal expression is \(\log y/(y-1)\), strictly decreasing in \(y\). Hence the equation \(x\log(1/x)/(1-x)=1/2\) has one solution. Convergence and monotonicity (5) give convergence of finite-size sign boundaries divided by \(n\) to \(x_*\).

## Verification

The accompanying standalone Python program `verify_recursive_leaf_age.py` uses exact rational arithmetic and independently enumerates **every** parent-choice array for \(2\le n\le9\). It reconstructs every degree, total leaf count, and mixed moment and compares each covariance with (1). It also verifies sign monotonicity and the first positive early label for every \(4\le n\le300\). These finite computations supplement, but do not replace, the infinite proof by (2)–(6).

## Relationship to prior work

The classical recursive-tree degree literature analyzes distributions and degree frequencies; the tagged nonroot birth-label/total-leaf covariance and its sharp sign transition require a distinct self-leaf exclusion term. Bryc–Minda–Sethuraman analyze marginal numbers of leaves via a Markov-chain framework, not this tagged joint covariance. A closely related published root-degree result gives \(\operatorname{Cov}(D_{n,1},L_n)=(n-2)/(2(n-1))\) and an equal-share decomposition of root attachment events; it neither states (1) for nonroot vertices nor the birth-time sign transition. The root case cannot simply be substituted for a nonroot vertex because the latter contributes a negative self-leaf covariance, (4).

## Limitations

The result applies to uniform recursive trees, not arbitrary growing trees, preferential attachment, or uniform Cayley trees. It establishes covariance signs, not positive or negative association of full joint laws. Historical priority is subject to residual uncertainty from older tagged-degree literature, including the inaccessible complete text of Janson's degree article and related older degree-count work; no claim that all literature has been exhausted is made.

## References

1. S. Janson, “Asymptotic degree distribution in random recursive trees,” *Random Structures & Algorithms* 26 (2005), 69–83, DOI 10.1002/rsa.20046 (online published 2004-11-16).
2. W. Bryc, D. Minda, and S. Sethuraman, “Large deviations for the leaves in some random trees,” arXiv:0809.4741, first submitted 2008-09-27.
3. “Equal-share covariance of root degree and leaves in a random recursive tree,” published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f.
