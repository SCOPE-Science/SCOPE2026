# Rank-resolved stochastic ordering of minimum-key depth by leaves in uniform binary search trees

## Finding

For every integer \(n\ge3\), construct a random binary search tree by inserting the keys \(1,\ldots,n\) in a uniformly random order. Let \(D_n\) be the number of edges from the root to key \(1\), and let \(B_i\) indicate that key \(i\) has no children. Write \(L_n=\sum_{i=1}^n B_i\).

**Position-resolved stochastic ordering.** In the usual first-order stochastic order, with at least one strict integer upper-tail inequality in each comparison,
\[
 D_n\mid\{B_1=1\}\;>_{\mathrm{st}}\;D_n,
 \qquad
 D_n\mid\{B_i=1\}\;<_{\mathrm{st}}\;D_n
 \quad(2\le i\le n).
\]
Consequently the covariance of \(D_n\) with the individual leaf indicator is positive at the smallest key, but negative at every other key:
\[
\operatorname{Cov}(D_n,B_i)=
\begin{cases}
 \frac14,&i=1,\\
 -\frac19,&i=2,\\
 -\frac{2}{3i(i-1)(i+1)},&3\le i<n,\\
 -\frac{1}{2n(n-1)},&i=n.
\end{cases}
\]
Despite the negative signs at all but one key, the **total** number of leaves has strictly positive covariance with the minimum-key depth:
\[
 \operatorname{Cov}(D_n,L_n)
 =\frac{(n-2)(n+1)}{12n(n-1)}>0.
\]
In particular, \(\operatorname{Cov}(D_n,L_n)\to1/12\) as \(n\to\infty\). Its Pearson correlation tends to zero; more precisely it is asymptotic to \(\sqrt{45/2}/(12\sqrt{n\log n})\).

## Assumptions and scope

All permutations are equally likely; trees are the *insertion-order* binary search trees, not uniformly sampled unlabelled binary tree shapes. Every node with no child is a leaf. Depth counts edges, so the root has depth zero. The stochastic order compares the conditional distribution given a specified key is a leaf to the unconditional distribution of the same depth variable. A strict order means non-strict inequalities for all real upper thresholds and strict inequality at one supported threshold, not strictness at every threshold. The theorem is finite and exact for all \(n\ge3\). The correlation asymptotic uses the natural logarithm.

## Proof

**1. Independent insertion ranks.** Assign independently to the keys \(1,\dots,n\) continuous uniform priorities \(U_1,\dots,U_n\), and insert them in increasing priority. For each \(k\), let
\[
 R_k=\#\{j\le k:U_j\le U_k\}.
\]
The random variables \(R_1,\ldots,R_n\) are independent, and \(R_k\) is uniform on \(\{1,\ldots,k\}\); this is the standard sequential relative-rank bijection for permutations. Put \(A_k=\mathbf1\{R_k=1\}\) for \(k\ge2\). The ancestors of the smallest key are exactly the successive record-low priority keys as the key index advances from \(2\) to \(n\). Hence
\[
 D_n=\sum_{k=2}^n A_k,
 \qquad \Pr(A_k=1)=\frac1k,
\]
and the \(A_k\)'s are independent.

The key \(i\) has no children precisely when its priority exceeds those of both its immediate neighbours among the ordered keys; at endpoints only the existing neighbour matters. Indeed, if \(U_i\) beats (is smaller than) one neighbouring priority, its Cartesian-tree subtree contains at least that neighbour on the corresponding side; if it beats neither, it has no children. Sequential insertion ranks therefore give the identities
\[
 B_1=\mathbf1\{R_2=1\},\qquad
 B_i=\mathbf1\{R_i>R_{i-1},\ R_{i+1}\le R_i\}\ (2\le i<n),
 \qquad B_n=\mathbf1\{R_n>R_{n-1}\}.
\]
These are functions only of the indicated consecutive insertion ranks, independent of all the remaining \(A_k\)'s. The corresponding leaf probabilities are \(1/2,1/3,1/2\) for the first, interior, and last positions.

**2. Conditional stochastic domination for interior keys.** Fix \(3\le i<n\) and denote \(T=A_{i-1}+A_i+A_{i+1}\). On \(B_i=1\), the insertion-rank triple \((a,b,c)=(R_{i-1},R_i,R_{i+1})\) satisfies \(b>a\) and \(c\le b\). Each of the \((i-1)i(i+1)\) possible triples has the same probability. There are \(\sum_{b=2}^{i}b(b-1)=(i-1)i(i+1)/3\) admissible triples. Since \(b=1\) is impossible, \(A_i=0\) conditionally. Counting triples with \(a=1\), \(c=1\), or both, gives the exact conditional upper tails
\[
 \Pr(T\ge1\mid B_i=1)=\frac3{i+1},\quad
 \Pr(T\ge2\mid B_i=1)=\frac3{i(i+1)},\quad
 \Pr(T\ge3\mid B_i=1)=0.
\]
On the other hand, independence of the three record indicators yields
\[
 \Pr(T\ge1)=\frac3{i+1},\quad
 \Pr(T\ge2)=\frac{3i-2}{i(i-1)(i+1)},\quad
 \Pr(T\ge3)=\frac1{(i-1)i(i+1)}.
\]
The second unconditional tail exceeds the conditional tail by \(1/[i(i-1)(i+1)]\), and the third also exceeds it strictly. All other record indicators form an independent nonnegative integer sum, with the same law after conditioning. Convolution preserves first-order stochastic order, so \(D_n\mid\{B_i=1\}<_{\mathrm{st}}D_n\). By tail summation,
\[
 \mathbb E[D_n\mid B_i=1]-\mathbb ED_n
 =-\frac2{i(i-1)(i+1)}.
\]
Multiplication by \(\Pr(B_i=1)=1/3\) gives the stated interior covariance.

**3. Endpoints and the second key.** If \(B_1=1\), then \(A_2=1\) rather than an independent Bernoulli variable of parameter \(1/2\). Every other \(A_k\) retains its law, giving strict upward stochastic order and covariance \(1/4\).

For \(B_2=1\), one has \(R_2=2\) and \(R_3\le2\); hence \(T=A_2+A_3\) changes from a sum of independent Bernoulli variables with parameters \(1/2,1/3\) to a single Bernoulli variable with parameter \(1/2\). Its positive upper tails strictly decrease and the covariance is \((1/3)(1/2-1/2-1/3)=-1/9\).

For \(B_n=1\), the local sum \(T=A_{n-1}+A_n\) has conditional law \(\operatorname{Bernoulli}(2/n)\), whereas without conditioning its two Bernoulli parameters are \(1/(n-1),1/n\). The unconditional and conditional probabilities of \(T\ge1\) coincide at \(2/n\); the unconditional probability of \(T\ge2\) equals \(1/[n(n-1)]\) and the conditional probability is zero. Thus the last leaf has strict downward stochastic order and covariance \(-1/[2n(n-1)]\). These arguments include \(n=3\), when the second and last leaf indicators overlap in insertion ranks but each comparison is still valid.

**4. Aggregate covariance and correlation.** Sum the individual covariances by linearity. The identity
\[
 \frac2{i(i-1)(i+1)}
 =\frac1{i(i-1)}-\frac1{i(i+1)}
\]
telescopes, giving exactly \((n-2)(n+1)/[12n(n-1)]\). For correlation, \(D_n\) is a sum of independent Bernoulli variables and so \(\operatorname{Var}(D_n)=\sum_{k=2}^n(1/k-1/k^2)=\log n+O(1)\). The local-peak representation of the leaf indicators yields \(\operatorname{Var}(L_n)=2n/45+O(1)\): interior indicators have variance \(2/9\), covariance \(-1/9\) at distance one, covariance \(1/45\) at distance two (the joint two-peak probability is \(2/15\)), and independence beyond distance two; the boundary makes an \(O(1)\) contribution. Combining these facts proves the stated asymptotic correlation.

## Verification

The accompanying self-contained Python program `checker.py` enumerates all \(n!\) insertion permutations for each \(3\le n\le8\), checks the Cartesian-tree/relative-rank leaf identity, all individual covariance formulas, and all conditional upper-tail inequalities. It separately counts exact independent-rank triples for \(3\le i\le80\) and checks the aggregate formula for \(3\le n<200\). All calculations use integer or rational arithmetic. Finite checks support but do not replace the preceding all-size proof.

## Relationship to prior work

The random BST model and aggregate leaf-pattern limit theory are classical. Flajolet, Gourdon and Martínez (1996) study occurrences of fixed BST patterns; Bóna and Pittel (2014) analyze the global distribution of vertices at given distances from leaves. Ji (2023) supplies a multivariate Eulerian–Stirling generating-function framework encompassing aggregate permutation peak/valley and record statistics. Those global results are not claimed here as discoveries; the specific assertion is the **key-by-key conditional stochastic domination of the extreme-key depth** and the resulting exceptional positive first-key covariance against universal negative covariances at every other key. Published aggregate generating functions may imply the sum covariance, but do not by themselves assert the specified conditional order for each inorder key. Historical priority remains subject to further independent inspection.

## Limitations

No claim is made of independence between depth and leaf count, or of strict inequality at every upper threshold. The conditional ordering applies to the depth of the **minimum key**, not to arbitrary key depths, and to individual leaf events rather than arbitrary joint leaf-event conditioning. Asymptotic correlation does not imply a joint central limit theorem here. This argument does not establish publication priority beyond the sources inspected; an unlocated multivariate positional result could subsume the position-resolved claim.

## References

1. P. Flajolet, X. Gourdon and C. Martínez, *Patterns in Random Binary Search Trees*, research report 2997 (October 1996); seminar presentation dated 7 October 1996: https://algo.inria.fr/seminars/sem96-97/flajolet.html .
2. M. Bóna and B. Pittel, *On a random search tree: asymptotic enumeration of vertices by distance from leaves*, preprint first submitted 8 December 2014: https://arxiv.org/abs/1412.2796 .
3. K. Q. Ji, *The (α,β)-Eulerian Polynomials and Descent-Stirling Statistics on Permutations*, preprint first submitted 2 October 2023: https://arxiv.org/abs/2310.01053 .
