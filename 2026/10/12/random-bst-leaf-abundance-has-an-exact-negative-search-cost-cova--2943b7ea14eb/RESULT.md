# Random-BST leaf abundance has an exact negative search-cost covariance

## Finding

Let \(T_n\) be the binary search tree obtained by inserting a uniformly random permutation of
\[
[n]=\{1,\ldots,n\},
\qquad n\ge2.
\]
Let \(L_n\) be the number of key leaves, meaning nodes with no children, and let
\[
P_n=\sum_{v\in T_n}d(v)
\]
be the internal path length, where the root has depth zero.

Then
\[
\boxed{
\operatorname{Cov}(L_n,P_n)
=
-\frac{(n-2)(n+3)}{9n}.
}
\tag{1}
\]
Thus the covariance is zero only at \(n=2\) and is strictly negative for every \(n\ge3\).

The leaf variance is
\[
\operatorname{Var}(L_3)=\frac29,
\]
and, for every \(n\ge4\),
\[
\boxed{
\operatorname{Var}(L_n)=\frac{2(n+1)}{45}.
}
\tag{2}
\]
Consequently, for \(n\ge4\), the least-squares slope in the linear regression of total search cost on leaf abundance is
\[
\boxed{
\frac{\operatorname{Cov}(P_n,L_n)}{\operatorname{Var}(L_n)}
=
-\frac52\frac{(n-2)(n+3)}{n(n+1)}.
}
\tag{3}
\]
In particular,
\[
\frac{\operatorname{Cov}(P_n,L_n)}{\operatorname{Var}(L_n)}
\longrightarrow
-\frac52.
\tag{4}
\]
The identity therefore quantifies a persistent finite-size opposition between terminal branching and aggregate search depth: one additional leaf in the best linear predictor is asymptotically associated with a reduction of \(5/2\) depth units in total internal path length.

## Assumptions and scope

The probability model is the standard random-permutation binary search tree. Conditional on the rank of the first inserted key, the left and right subtrees are independent random-permutation binary search trees on their respective key sets.

Leaves count stored keys, not external null pointers. The internal path length counts one unit for each edge on each root-to-key path.

Equation (1) is an exact mixed second-moment identity. It does not assert negative association between all increasing tree statistics, nor does it transfer automatically to median-of-sample or otherwise biased pivot rules.

## Proof

Write
\[
\ell_n=\mathbb E L_n,
\qquad
p_n=\mathbb E P_n,
\qquad
c_n=\operatorname{Cov}(L_n,P_n),
\]
with
\[
L_0=P_0=0.
\]
For a random binary search tree of size \(n\), let \(K\) be the size of the root's left subtree and put
\[
R=n-1-K.
\]
The first key has uniform rank, so \(K\) is uniform on \(\{0,\ldots,n-1\}\). Conditional on \(K\), the two subtrees are independent. Hence, for \(n\ge2\),
\[
L_n=L_K+L'_R
\tag{5}
\]
and
\[
P_n=P_K+P'_R+n-1.
\tag{6}
\]
The classical means are
\[
\ell_0=0,
\qquad
\ell_1=1,
\qquad
\ell_n=\frac{n+1}{3}\quad(n\ge2),
\tag{7}
\]
and
\[
p_n=2(n+1)H_n-4n,
\tag{8}
\]
where
\[
H_n=\sum_{j=1}^n\frac1j.
\]

Define, for a split \(K=k\),
\[
A_k=\ell_k+\ell_{n-1-k}
\]
and
\[
B_k=p_k+p_{n-1-k}+n-1.
\]
Taking conditional covariance in (5)--(6) gives
\[
c_n
=
\frac2n\sum_{k=0}^{n-1}c_k
+
\operatorname{Cov}_K(A_K,B_K).
\tag{9}
\]

For \(n\ge4\), equation (7) makes the conditional leaf mean flat except at the four boundary splits. Relative to \(\ell_n=(n+1)/3\), its deviations are
\[
A_0-\ell_n=A_{n-1}-\ell_n=-\frac13,
\]
\[
A_1-\ell_n=A_{n-2}-\ell_n=\frac13,
\]
and every other deviation is zero. Therefore
\[
\operatorname{Cov}_K(A_K,B_K)
=
\frac{2}{3n}(p_{n-2}-p_{n-1}).
\tag{10}
\]
Using (8),
\[
p_{n-2}-p_{n-1}
=
-2(H_{n-1}-1),
\]
so
\[
\operatorname{Cov}_K(A_K,B_K)
=
-\frac{4}{3n}(H_{n-1}-1).
\tag{11}
\]

The cases \(n=2,3\) give
\[
c_2=0,
\qquad
c_3=-\frac29.
\]
Assume (1) holds through size \(n-1\). For \(k\ge2\), rewrite its right-hand side as
\[
c_k=-\frac{k+1}{9}+\frac{2}{3k}.
\tag{12}
\]
Thus
\[
\sum_{k=0}^{n-1}c_k
=
-\frac{(n-2)(n+3)}{18}
+
\frac23(H_{n-1}-1).
\tag{13}
\]
Substitution of (11)--(13) into (9) cancels the harmonic terms and leaves
\[
c_n=-\frac{(n-2)(n+3)}{9n},
\]
proving (1) by induction.

For completeness, the same split recursion gives the leaf variance. Let
\[
v_n=\operatorname{Var}(L_n).
\]
By total variance,
\[
v_n
=
\frac2n\sum_{k=0}^{n-1}v_k
+
\operatorname{Var}_K(A_K).
\tag{14}
\]
For \(n\ge4\), the four boundary deviations above give
\[
\operatorname{Var}_K(A_K)=\frac{4}{9n}.
\tag{15}
\]
Starting from
\[
v_2=0,
\qquad
v_3=\frac29,
\]
an induction in (14)--(15) yields (2). Dividing (1) by (2) gives (3), and (4) follows immediately.

## Verification

The accompanying checker exhaustively enumerates every insertion permutation for
\[
1\le n\le9.
\]
For each permutation it constructs the binary search tree directly and independently computes leaf count and internal path length. Exact rational arithmetic verifies the means, the covariance (1), the leaf variance (2), and the regression slope (3).

The checker also replays the split moment recurrences through size \(300\), without using the closed covariance or variance formulas inside the recurrence itself. The finite computations are supplementary; the all-size result is the induction above.

## Relationship to prior work

Flajolet, Gourdon, and Martínez study fringe patterns in random binary search trees. Their introduction places both total path length and leaves among classical shape parameters, and their main results provide detailed leaf-pattern frequency theory. The inspected paper does not state a mixed leaf-count/internal-path-length covariance.

Kapur develops a general additive-functional framework for random search trees under the random-permutation model and treats internal path length as a principal example. This framework supplies broad moment methodology, but the inspected dissertation does not state the mixed leaf/path identity (1).

Drmota and Hwang study covariance and correlation among level-profile counts in random recursive trees and binary search trees and connect profile limits to total path length. Their full paper is explicitly classified Primary \(60C05\). The inspected text contains no leaf statistic, so its profile covariance theorems do not cover (1).

The present result combines two classical marginals into an exact finite mixed law. Its content is the cancellation in (9)--(13), not a new formula for either marginal by itself.

## Limitations

The argument depends on the uniform first-rank split and recursive independence of the two subtrees. Other search-tree models require new split weights.

The linear-regression slope in (3) is a projection coefficient, not a causal effect and not a conditional-expectation identity.

The underlying recurrences are elementary and older analysis-of-algorithms literature is extensive. An equivalent mixed moment could exist in a textbook exercise or a bivariate generating-function treatment not located by the targeted searches; this is the principal originality risk.

## References

1. P. Flajolet, X. Gourdon, and C. Martínez, “Patterns in Random Binary Search Trees,” *Random Structures & Algorithms* 11 (1997), 223–244, DOI 10.1002/(SICI)1098-2418(199710)11:3<223::AID-RSA2>3.0.CO;2-2; first published online 1998-12-07.
2. N. Kapur, “Additive functionals on random search trees,” arXiv:math/0304411, first submitted 2003-04-25.
3. M. Drmota and H.-K. Hwang, “Profiles of random trees: correlation and width of random recursive trees and binary search trees,” *Advances in Applied Probability* 37 (2005), 321–341, DOI 10.1239/aap/1118858628.
