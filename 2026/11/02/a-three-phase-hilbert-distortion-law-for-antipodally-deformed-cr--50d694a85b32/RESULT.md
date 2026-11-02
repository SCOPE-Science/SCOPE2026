# A three-phase Hilbert distortion law for antipodally deformed crown metrics

## Finding
For each integer \(n\ge3\), let \(X_{n,t}=\{u_1,\ldots,u_n,v_1,\ldots,v_n\}\), where \(1\le t\le3\), be the real finite metric space with
\[
d(u_i,u_j)=d(v_i,v_j)=2\quad(i\ne j),\qquad
d(u_i,v_j)=\begin{cases}t&i=j,\\1&i\ne j.\end{cases}
\]
The metric is well-defined: the only potentially restrictive triangle conditions are \(2\le1+t\) and \(t\le2+1\). At \(t=1\), it is the shortest-path metric of \(K_{n,n}\); at \(t=3\), it is the shortest-path metric of the crown graph \(K_{n,n}\setminus M\).

Let \(c_2(X)\) denote the least possible bilipschitz distortion of \(X\) into a real Hilbert space, over arbitrary target dimensions. Put \(q=t^2\). Then
\[
\boxed{\ c_2(X_{n,t})^2=
\max\left\{\frac{4(n-1)}{n-1+q},\ \frac{4(n-2)}{n},\ \frac{(n-2)q}{2(n-1)}\right\}.\ }
\]
All three branches are necessary. More precisely, writing
\[
q_- = \frac{2(n-1)}{n-2},\qquad q_+=\frac{8(n-1)}n,
\]
the maximum is the first term for \(1\le q\le q_-\), the second for \(q_-\le q\le q_+\), and the third for \(q_+\le q\le9\). Thus the exact distortion has a **nondegenerate constant plateau** for every \(n\ge3\), even while the matched distances vary. Each sharp upper bound is realized by two correlated copies of a regular simplex, in dimension at most \(2n-2\); throughout the plateau and the large-\(q\) regime the copies can be chosen antipodal, in dimension \(n-1\).

## Assumptions and scope
The integer \(n\) is at least \(3\), and \(t\) is any real number in the closed interval \([1,3]\). There are \(2n\) labeled points with exactly the distances displayed above. The target is an arbitrary real Hilbert space. Distortion means the product of the optimal Lipschitz and inverse-Lipschitz constants; equivalently, after global rescaling, an embedding \(f\) has distortion at most \(D\) precisely when
\[
d(x,y)\le\|f(x)-f(y)\|\le Dd(x,y)\qquad(x\ne y).
\]
No symmetry is imposed on competing embeddings. Any such finite embedding can be considered in a finite-dimensional Hilbert subspace.

## Proof
### 1. Reduction to three squared distances
Given any noncontracting embedding with upper distortion \(D\), compose it with every simultaneous permutation of the indices and with the involution interchanging the \(u\)- and \(v\)-parts. Take their orthogonal direct sum, divided by the square root of the group order. All squared-distance ratios remain between \(1\) and \(D^2\); the new squared distances take just three values: \(a\) for pairs in a single part, \(b\) for unmatched cross-part pairs, and \(c\) for matched cross-part pairs. Writing \(T=D^2\), we have
\[
4\le a\le4T,\qquad1\le b\le T,\qquad q\le c\le qT.\tag{1}
\]

Any such symmetric Hilbert squared-distance array necessarily satisfies
\[
|b-c|\le a,\qquad (n-1)a\le(n-1)b+c.\tag{2}
\]
Indeed let \(\mu_u,\mu_v\) be the two part centroids and \(U_i=u_i-\mu_u\), \(V_i=v_i-\mu_v\) the centered vectors. Their common mean squared norm is \(R^2=a(n-1)/(2n)\). Put \(m=n^{-1}\sum_i\langle U_i,V_i\rangle\). Centering gives mean cross inner product \(-m/(n-1)\) for \(i\ne j\). Consequently, with \(\delta^2=\|\mu_u-\mu_v\|^2\),
\[
\begin{aligned}
c&=2R^2+\delta^2-2m,\\
b&=2R^2+\delta^2+\frac{2m}{n-1},\\
\frac{(n-1)b+c}{n}&=\frac{(n-1)a}{n}+\delta^2.
\end{aligned}
\]
Cauchy--Schwarz yields \(|m|\le R^2\), and both inequalities in (2) follow. This argument uses *any* embedding, with no assumed equivariance.

### 2. Three universal lower certificates
Combining (1)--(2) in three different ways gives
\[
4\le a\le b+\frac{c}{n-1}\le T\left(1+\frac{q}{n-1}\right),
\]
and hence
\[
T\ge\frac{4(n-1)}{n-1+q}.\tag{3}
\]
Next \(c\le a+b\) and \((n-1)a\le(n-1)b+c\) imply
\[
(n-2)c\le2(n-1)b.
\]
Since \(c\ge q\) and \(b\le T\),
\[
T\ge\frac{(n-2)q}{2(n-1)}.\tag{4}
\]
Finally, substituting \(c\le a+b\) into the second inequality of (2) yields
\[
(n-2)a\le nb,
\]
so \(a\ge4\) and \(b\le T\) give
\[
T\ge\frac{4(n-2)}n.\tag{5}
\]
Together (3)--(5) prove the claimed lower bound for every real Hilbert embedding. Their crossover points satisfy \(1<q_-<q_+<9\), for every integer \(n\ge3\).

### 3. Exact upper certificates
Write \(e_i\) for the standard basis of \(\mathbb R^n\), and put \(w_i=e_i-n^{-1}\sum_j e_j\), so \(\|w_i-w_j\|^2=2\). In orthogonal copies of the zero-sum hyperplane, write \(w_i'\) for a second copy. For any \(a>0\) and \(-1\le\rho\le1\), let
\[
\begin{aligned}
f(u_i)&=\sqrt{a/2}\ w_i,\\
f(v_i)&=\sqrt{a/2}\bigl(\rho w_i+\sqrt{1-\rho^2}\ w_i'\bigr).
\end{aligned}\tag{6}
\]
These two centered regular simplices have squared within-part distance \(a\), matched cross distance \(c=a(n-1)(1-\rho)/n\), and unmatched cross distance \(b=a(n-1+\rho)/n\). Thus \(\rho=(b-c)/a\), provided \(a=(n-1)b/n+c/n\); this last equality is precisely the centroid inequality (2) at equality.

Three explicit choices attain the three lower certificates:

* If \(1\le q\le q_-\), choose \(T=4(n-1)/(n-1+q)\), \(a=4\), \(b=T\), \(c=qT\), and \(\rho=(1-q)T/4\). Then \(-1\le\rho\le0\), all squared distances lie in the intervals (1), and their maximal normalized value is \(T\).
* If \(q_-\le q\le q_+\), choose \(T=4(n-2)/n\), \(a=4\), \(b=T\), \(c=8(n-1)/n\), and \(\rho=-1\). The matched normalized squared distance \(c/q\) decreases from \(T\) to \(1\) across this interval, while the other two types have normalized values \(1\) and \(T\).
* If \(q_+\le q\le9\), choose \(T=(n-2)q/[2(n-1)]\), \(a=nq/[2(n-1)]\), \(b=T\), \(c=q\), and \(\rho=-1\). The assumptions \(n\ge3\) and \(q\ge q_+\) ensure \(a\ge4\), \(a\le4T\), and \(T\ge1\).

In every case formula (6) realizes the specified distances, with no contraction and squared expansion at most \(T\). Hence the lower and upper bounds coincide, proving the theorem.

### 4. Consequences
The function \(t\mapsto c_2(X_{n,t})\) strictly decreases to its minimum \(\sqrt{4(n-2)/n}\) on \([1,\sqrt{q_-}]\), stays constant on the entire closed interval \([\sqrt{q_-},\sqrt{q_+}]\), and then strictly increases on \([\sqrt{q_+},3]\). Both transition points are interior to \([1,3]\). At \(t=3\), the expression gives \(c_2^2=9(n-2)/[2(n-1)]\), consistent with the unweighted crown-graph specialization of the known diameter-three distance-regular result. At \(t=1\), it gives \(c_2^2=4(n-1)/n\) for the complete-bipartite graph metric.

## Verification
Run `python3 check_deformed_crown.py` with Python 3 and no third-party dependencies. It checks the piecewise optimum, all exact squared-distance constraints, and explicit positive-semidefinite Gram-factor conditions using rational arithmetic for \(n=3,\ldots,100\) and multiple rational \(q\) values, including phase boundaries. A separate exact rational vertex enumeration of the reduced four-variable linear program verifies optimum equality on 104 cases for \(n=3,\ldots,10\). It reports:

`CHECK_OK exact_rational_phase_cases= 1756 independent_exact_LP_cases= 104 orders=3..100 phases=3`

The exhaustive proof for **all real parameters** is the algebraic argument above, not this finite program. The code gives independent checks of the three-phase formulas but no infinite formal certificate.

## Relationship to prior work
Vallentin's work (2005, revised 2007) develops exact and lower-bound methods for Euclidean distortion of unweighted distance-regular graph metrics, including a general semidefinite-programming reduction. Cioabă, Gupta, Ihringer and Kurihara (public preprint September 20, 2021) prove an exact formula for diameter-three distance-regular **graph shortest-path metrics**; their Theorem 4.3, particularly its antipodal specialization, already covers the unweighted crown graph at \(t=3\). That endpoint is a benchmark, **not a novelty claim**. The present result instead determines a continuous metric deformation with both non-graph-metric intermediate distances and two sharp phase boundaries; neither inspected paper states these three-regime parameter laws. A priority search under crown graphs, bipartite-minus-matching graphs, weighted antipodal metrics, and finite-dimensional Hilbert distortion did not identify a direct earlier formula. This negative search is not proof of global uniqueness.

## Limitations
Only the explicitly defined \(2n\)-point metrics with \(n\ge3\) and \(1\le t\le3\) are treated. No assertion is made for arbitrary weighted edges, complex nonlinear targets, \(\ell_p\) distortions for \(p\ne2\), or embeddings in a prescribed lower dimension. The construction bounds the needed Hilbert dimension by \(2n-2\) but does not classify all optimal embeddings or their minimal dimensions. Earlier equivalent formulations in the literature may still exist, and no independent mathematical audit has been performed.

## References
1. F. Vallentin, *Optimal Distortion Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716 (first public version September 30, 2005; revised 2007). https://arxiv.org/abs/math/0509716 . Relevant material: Theorem 2.4, semidefinite bounds, and the graph families explicitly evaluated.
2. S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The Least Euclidean Distortion Constant of a Distance-Regular Graph*, arXiv:2109.09708 (first public version September 20, 2021). https://arxiv.org/abs/2109.09708 . Relevant material: Theorem 4.3 and Section 4.2, which treat diameter-three **unweighted** graph distances.
