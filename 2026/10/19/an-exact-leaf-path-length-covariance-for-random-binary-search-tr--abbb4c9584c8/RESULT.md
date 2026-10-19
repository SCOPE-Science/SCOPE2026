# An exact leaf–path-length covariance for random binary search trees

## Finding
Let \(L_n\) be the number of leaves and \(P_n\) the internal path length of the random binary search tree constructed by inserting \(n\) distinct ordered keys in uniformly random order. For every integer \(n\ge 2\),
\[
\operatorname{Cov}(L_n,P_n)=-\frac{n(n+1)-6}{9n}.
\]
The covariance is zero at \(n=2\) and strictly negative at every \(n\ge3\). The probability model is the classical random insertion tree, **not** the uniform (Catalan-distributed) binary-tree model.

For \(n\ge4\), the exact leaf variance and classical path-length variance give
\[
\operatorname{Corr}(L_n,P_n)=
-\frac{n(n+1)-6}{9n\sqrt{\frac{2(n+1)}{45}\left[n(7n+13)-2(n+1)H_n-4(n+1)^2H_n^{(2)}\right]}}.
\]
In particular,
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(L_n,P_n)
=-\sqrt{\frac5{18(7-2\pi^2/3)}}
\approx-0.81299484698.
\]
The finite covariance identity fixes the leading coefficient that is left unspecified in the earlier general quadtree joint-asymptotic result [1, Theorem 5.4, dimension one].

## Assumptions and scope
Fix an integer \(n\ge2\) and insert the distinct keys \(1,\ldots,n\) in a uniformly random permutation order into an initially empty ordinary binary search tree, with neither rebalancing nor deletion. Each vertex of outdegree zero counts as one leaf. The root has depth zero; \(P_n\) is the sum of the depths of the \(n\) inserted vertices. Define \(L_0=P_0=0\), \(L_1=1\), and \(P_1=0\). Harmonic numbers are \(H_j=\sum_{k=1}^j 1/k\), with \(H_0=0\), and \(H_j^{(2)}=\sum_{k=1}^j1/k^2\).

## Proof
**Splitting identities.** Let \(I\) be the number of keys smaller than the first inserted key and \(J=n-1-I\). The index \(I\) is uniform on \(\{0,\ldots,n-1\}\); conditional on \(I\), the two subtrees are independent, each distributed as a random binary search tree of its respective size. For \(n\ge2\), using independent subtree copies,
\[
L_n\stackrel d=L_I^{(1)}+L_J^{(2)},\qquad
P_n\stackrel d=P_I^{(1)}+P_J^{(2)}+(n-1).
\]
Put \(a_n=\mathbb E L_n\), \(b_n=\mathbb E P_n\), and \(C_n=\operatorname{Cov}(L_n,P_n)\). Taking expectations in the splitting recurrences gives the elementary exact formulas
\[
a_n=\frac{n+1}{3}\quad(n\ge2),\qquad
b_n=2(n+1)H_n-4n\quad(n\ge0).
\]
The exceptional initial values may be written uniformly as
\[
a_k=\frac{k+1}{3}+\delta_k,
\quad\delta_0=-\frac13,\quad\delta_1=\frac13,
\quad\delta_k=0\ (k\ge2).
\]

**The root-split covariance.** Conditional independence and the law of total covariance show that, for \(n\ge2\),
\[
C_n=\frac2n\sum_{k=0}^{n-1}C_k+Q_n,\qquad
Q_n=\operatorname{Cov}_I(a_I+a_J,b_I+b_J).
\]
Here \(a_I+a_J=(n+1)/3+\delta_I+\delta_J\). Since the deviations sum to zero in expectation and \(b_0=b_1=0\), direct averaging over the uniform root rank yields
\[
Q_n=\frac2{3n}(b_{n-2}-b_{n-1}).
\]
The difference \(b_{n-1}-b_{n-2}=2(H_{n-1}-1)\) therefore gives the explicit negative source
\[
Q_n=-\frac4{3n}(H_{n-1}-1).
\]
This vanishes at \(n=2\) and is strictly negative for \(n\ge3\). It is **only** the root-rank contribution; the first term in the covariance recurrence retains all within-subtree dependence.

**Solving the recurrence.** We have \(C_0=C_1=C_2=0\). We prove by induction that
\[
C_n=-\frac{n(n+1)-6}{9n}\quad(n\ge2).
\]
Indeed, for \(n\ge3\), substitute the induction hypothesis into the recurrence, using
\[
\sum_{k=2}^{n-1}\frac{k(k+1)-6}{k}
=\sum_{k=2}^{n-1}\left(k+1-\frac6k\right)
=\frac{(n-1)n}{2}+n-3-6(H_{n-1}-1).
\]
Consequently
\[
\begin{aligned}
C_n
&=-\frac2{9n}\left[\frac{(n-1)n}{2}+n-3-6(H_{n-1}-1)\right]
-\frac4{3n}(H_{n-1}-1)\\
&=-\frac{n(n+1)-6}{9n},
\end{aligned}
\]
as required. The harmonic terms cancel exactly, producing a rational function of sample size. The same recurrence makes every \(C_n\) nonpositive: for \(n\ge3\) the root-rank term is strictly negative, while the accumulated subtree terms are nonpositive.

**Leaf variance and correlation.** Give key \(j\) an independent continuous insertion-time label \(U_j\). For an interior key \(2\le j\le n-1\), its node is a leaf exactly when \(U_j>\max\{U_{j-1},U_{j+1}\}\); at an endpoint there is only one neighbor. Thus the leaf indicators form a two-dependent sequence. Interior indicators have variance \(2/9\), the two boundary indicators each have variance \(1/4\), adjacent interior pairs have covariance \(-1/9\), and adjacent boundary–interior pairs have covariance \(-1/6\). At distance two, interior pairs have covariance \(1/45\) and the two boundary–interior pairs have covariance \(1/24\). All more separated pairs are independent. Summing for \(n\ge4\) gives
\[
\operatorname{Var}(L_n)=\frac12+\frac{2(n-2)}9
+2\left[-\frac{n-3}9-\frac13+\frac{n-4}{45}+\frac1{12}\right]
=\frac{2(n+1)}{45}.
\]
The classical Quicksort/path-length second-moment recurrence yields
\[
\operatorname{Var}(P_n)
=n(7n+13)-2(n+1)H_n-4(n+1)^2H_n^{(2)}.
\]
This identity also follows by squaring the displayed splitting recurrence for \(P_n\) and inducting, and is verified by an independent rational-moment recurrence in the accompanying code. Since \(\operatorname{Var}(P_n)/n^2\to7-2\pi^2/3>0\), combination with the exact covariance and leaf variance proves the stated correlation limit.

## Verification
The attached standard-library Python script `check_bst.py` independently constructs recurrences for the first and second moments of both statistics and their mixed moment using exact rational arithmetic. It verifies the covariance formula, both variance formulas (for their stated ranges), and the means through \(n=80\). Separately, it enumerates every permutation for each \(2\le n\le8\) and independently computes leaves and path lengths recursively, checking the covariance. All checks pass. The proof, not the finite computations, establishes the infinite family.

Run: `python3 check_bst.py`.

## Relationship to prior work
Chern, Fuchs, Hwang, and Neininger [1, Section 5.2, especially Theorems 5.4 and 5.6] already analyzed **this same pair** of statistics for dimension-one quadtrees, equivalently binary search trees, and proved covariance of linear order and asymptotic decorrelation/independence. Their displayed covariance result involves a suitable general constant rather than the finite-sample formula above; this note supplies the exact dimension-one constant, \(-1/9\), all finite-size corrections, and the leading correlation coefficient. Its claim is a quantitative refinement, **not** first discovery of dependence or decorrelation.

Devroye [2] gives the leaf local-counter representation and marginal leaf central limit theorem with limiting variance \(2/45\). Sedgewick and Flajolet's accessible analysis [3] gives the classical leaf expectation and path-length mean/variance asymptotics. The present calculation couples these two statistics rather than deriving their separate marginal behavior. Closely related published calculations for squared root imbalance versus path length, and for degree/path-length statistics in different random-tree models, do not imply the displayed leaf/path-length identity.

## Limitations
This result assumes uniform insertion permutations and the ordinary binary search tree; it makes no assertion for uniform Catalan trees, nonuniform keys, balancing rules, higher-dimensional quadtrees, or the full joint distribution. For \(n=2\), the leaf count is deterministic, so correlation is undefined even though covariance is zero. Correlation formulas are stated for \(n\ge4\); the covariance statement applies for every \(n\ge2\). The closest earlier joint paper proves an asymptotic statement for these observables, so the advance is specifically quantitative and exact. Some related fringe-tree literature was accessible only in abstract form; implicit earlier equivalent calculations cannot be excluded without further bibliographic review.

## References
[1] H.-H. Chern, M. Fuchs, H.-K. Hwang, R. Neininger, *Dependence and phase changes in random \(m\)-ary search trees*, arXiv:1501.05135, first posted 21 January 2015. Lawful full text: https://web.math.nccu.edu.tw/mfuchs/dep-m-ary-st-r1-w-app.pdf (Section 5.2).

[2] L. Devroye, *Limit Laws for Local Counters in Random Binary Search Trees*, Random Structures & Algorithms 2 (1991), 303–315. Full text: https://luc.devroye.org/devroye_1991_limit_law_counter_random_binary_search_tree.pdf.

[3] R. Sedgewick and P. Flajolet, *An Introduction to the Analysis of Algorithms*, random-tree chapter, accessible exposition: https://aofa.cs.princeton.edu/60trees/.

[4] C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Random Recursive Trees*, arXiv:1406.6883 (2014); abstract and bibliographic description consulted, full text not verified.
