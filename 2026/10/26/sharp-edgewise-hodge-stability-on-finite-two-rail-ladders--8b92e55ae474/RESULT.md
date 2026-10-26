# Sharp edgewise Hodge stability on finite two-rail ladders

## Finding

Let \(n\ge2\) and let \(L_n=P_2\square P_n\) be the unweighted ladder graph with \(n\) rungs, \(2n\) vertices and \(3n-2\) edges. Orient all rungs from the lower to upper rail and the rail edges from column \(h\) to column \(h+1\). Let \(P_n\) be Euclidean orthogonal projection of real edge flows onto gradient flows, with the maximum absolute edge value as norm. Put
\[
\alpha=2-\sqrt3,\qquad \rho=\frac{1-\alpha}{1+\alpha}=\frac1{\sqrt3}.
\]
For any \(n\), set \(m=\lfloor(n+1)/2\rfloor\) and
\[
 t_n=\alpha^{m-1}+\alpha^{n-m}.
\]
Then the **sharp** operator norm, attained at a central rung, is
\[
\boxed{\|P_n\|_{\infty\to\infty}=
1+\rho\left[\frac{2(1-\alpha^n)}{1+\alpha^n}
+\frac{2\alpha t_n^2}{1-\alpha^{2n}}
-\frac{(1+\alpha)t_n}{1-\alpha^n}\right].}
\]
The first values, in order \(n=2,3,4,5,6\), are
\[
 \frac32,\quad \frac95,\quad \frac{27}{14},\quad \frac{39}{19},\quad \frac{163}{78}.
\]
The only maximizing rows are the middle rung row (odd \(n\ge3\)) or the two middle rung rows (even \(n\ge4\)); when \(n=2\), all four rows tie. **Exactly at five rungs**, the norm first exceeds \(2\). Every rail-edge row has absolute sum strictly below \(2\), for every finite \(n\).

The finite-ladder norm stays strictly below \(1+2/\sqrt3\). Its asymptotic deficit has sharp, parity-dependent leading terms: for \(m\to\infty\),
\[
\begin{aligned}
1+\tfrac2{\sqrt3}-\|P_{2m+1}\|_{\infty\to\infty}
&\sim 2(1-\alpha)\alpha^m,\\
1+\tfrac2{\sqrt3}-\|P_{2m}\|_{\infty\to\infty}
&\sim (1-\alpha^2)\alpha^{m-1}.
\end{aligned}
\]
In particular, the root convergence rate is \(\sqrt{2-\sqrt3}\). A sign-valued finite edge-flow input attains the norm for every \(n\).

## Assumptions and scope

The graph is the ordinary *open-ended* unweighted ladder, not a periodic prism, and no edge conductances are varied. The projection minimizes the sum of squared errors in all \(3n-2\) edge coordinates. The domain and codomain both have the ordinary coordinatewise maximum norm; no normalization by vertex count or edge degree is used. The conclusions apply to the linear projection on the complete edge-data space, not to probabilistic spanning-tree samples. The main formula holds for all integers \(n\ge2\).

## Proof

**1. Exact operator decomposition.** Index the \(n\) rungs first, then the \(n-1\) top-rail edges, then the \(n-1\) bottom-rail edges. Define \(D\in\mathbb R^{(n-1)\times n}\) by \((Dz)_h=z_{h+1}-z_h\). Set
\[
 B=2I+D^{\mathsf T}D,\quad G=B^{-1},\quad K=2G,\quad Q=DGD^{\mathsf T}.
\]
Decompose vertex potentials into symmetric and antisymmetric rail components. The symmetric component projects rail flows onto the identical-rail subspace, with no effect on rungs; the antisymmetric component has positive-definite Gram matrix \(B/2\). Direct multiplication yields the full orthogonal projection
\[
P_n=\begin{pmatrix}
K&GD^{\mathsf T}&-GD^{\mathsf T}\\
DG&(I+Q)/2&(I-Q)/2\\
-DG&(I-Q)/2&(I+Q)/2
\end{pmatrix}.\tag{1}
\]
This proves symmetry, idempotence and projection onto the required \((2n-1)\)-dimensional gradient subspace. The matrix \(B\) has diagonal \(3,4,\ldots,4,3\) and super/subdiagonal \(-1\).

**2. Green kernel and rung signs.** The root \(\alpha\in(0,1)\) satisfies \(\alpha+\alpha^{-1}=4\). Solving the tridiagonal recurrence with the two endpoint equations gives, for \(1\le i\le j\le n\),
\[
K_{ij}=\rho\,\alpha^{j-i}
\frac{(1+\alpha^{2i-1})(1+\alpha^{2(n-j)+1})}{1-\alpha^{2n}},
\quad K_{ji}=K_{ij}.\tag{2}
\]
The formula may also be verified by substitution into \(BK=2I\), with the specified endpoint diagonal entries. Every entry is strictly positive, and \(K\mathbf1=\mathbf1\) because \(B\mathbf1=2\mathbf1\). A column of \(K\) increases strictly toward its diagonal and decreases strictly after it. Therefore, by (1), the absolute sum in rung row \(j\) is
\[
R_j=\sum_iK_{ji}+\sum_{h=1}^{n-1}|K_{h+1,j}-K_{h,j}|
=1+2K_{jj}-K_{1j}-K_{nj}.\tag{3}
\]
All equalities are exact and hold for the edge orientations stated above.

**3. Rail rows are always sub-two.** For a rail location \(h\), define \(r_j=G_{h+1,j}-G_{h,j}\). The kernel product structure (2) shows \(r_j<0\) for \(j\le h\), \(r_j>0\) for \(j\ge h+1\), and each side of this split is strictly decreasing as \(j\) increases. Hence \(Q_{hk}=r_{k+1}-r_k<0\) whenever \(k\ne h\). Because \(B r=e_{h+1}-e_h\), summing over \(j\ge h+1\) gives
\[
2\sum_{j=h+1}^n r_j+Q_{hh}=1.
\]
Also \(\sum_jr_j=0\) and \(\sum_kQ_{hk}=r_n-r_1\). The absolute sum of either rail-edge row of (1) consequently simplifies to
\[
H_h=1+\sum_{k\ne h}|Q_{hk}|+\sum_j|r_j|
=2-(r_n-r_1)<2.\tag{4}
\]
Strictness follows from \(r_1<0<r_n\); no numerical comparison is involved.

**4. Locate the maximizing rung.** Put \(a=\alpha^n\), \(t_j=\alpha^{j-1}+\alpha^{n-j}\). Expansion of (2) in (3) gives
\[
R_j=1+\rho\left[\frac{2(1-a)}{1+a}+\frac{2\alpha t_j^2}{1-a^2}-\frac{(1+\alpha)t_j}{1-a}\right].\tag{5}
\]
The quantities \(t_j\) strictly decrease from either end toward the middle, apart from the symmetry tie at two middle positions. The bracket in (5) decreases as a function of \(t\) on the relevant range \(0<t\le1+\alpha^{n-1}\): its derivative is nonpositive because
\[
(1+\alpha)(1+\alpha^n)-4\alpha(1+\alpha^{n-1})
=(3-\alpha)(\alpha^2-\alpha^n)\ge0.
\]
The inequality is strict for \(n>2\). Thus the central rung rows alone maximize among rungs when \(n>2\). The explicit comparisons for \(n=2,3,4\) give central rung maxima \(3/2,9/5,27/14\), while the corresponding maximal rail row sums are \(3/2,5/3,13/7\).

For \(n\ge5\), the central position obeys \(t_n\le 2\alpha^2\) and \(\alpha^n\le\alpha^5\). Discarding the positive quadratic term in (5), and bounding its other terms in their unfavorable directions, gives the exact strict estimate
\[
R_m-2\ge \rho\left[
\frac{2(1-\alpha^5)}{1+\alpha^5}
-\frac{2\alpha^2(1+\alpha)}{1-\alpha^5}\right]-1
=\frac{29}{627}>0.\tag{6}
\]
Therefore (4) rules out every rail row for \(n\ge5\), and the direct comparisons rule them out (apart from \(n=2\) equality) at the smaller sizes. Formula (5) at \(j=m\) proves the claimed sharp norm and location.

**5. Exact attainment.** Fix a central rung \(m\). Give every rung input value \(+1\). On top rail edge \(h\), set input \(+1\) if \(h<m\) and \(-1\) otherwise; on the corresponding bottom rail use the opposite sign. By the strictly increasing/decreasing sign pattern of column \(m\) in (2), this sign vector agrees with the sign of every coefficient in row \(m\) of (1). Hence its maximum input norm is \(1\), while its projected rung \(m\) value is exactly \(R_m=\|P_n\|_{\infty\to\infty}\). The pair consisting of zero edge data and this finite sign vector attains the claimed Lipschitz ratio.

**6. Strict finite-volume deficit and rate.** Subtract (5) at the center from \(1+2\rho\):
\[
1+2\rho-R_m=\rho\left[
\frac{t_n\{(1+\alpha)(1+\alpha^n)-2\alpha t_n\}}{1-\alpha^{2n}}
+\frac{4\alpha^n}{1+\alpha^n}\right].\tag{7}
\]
This is strictly positive: \(t_n\le1+\alpha^{n-1}\) implies
\((1+\alpha)(1+\alpha^n)-2\alpha t_n\ge(1-\alpha)(1-\alpha^n)>0\).
For odd \(n=2m+1\), \(t_n=2\alpha^m\); for even \(n=2m\), \(t_n=(1+\alpha)\alpha^{m-1}\). Substitution in (7) and division by the respective leading powers gives the stated two positive limits, because all the remaining terms have strictly higher powers of \(\alpha\). This also proves the asserted root rate.

## Verification

The accompanying `verify_ladder_hodge.py` implements rational Gaussian elimination without external libraries. It constructs the stated block projector from \(B\) and, independently for \(2\le n\le11\), builds the graph's signed incidence matrix and its ordinary least-squares projection by fixing one vertex potential. It compares every matrix entry exactly, checks symmetry and idempotence, reconstructs row sums for \(2\le n\le22\), verifies central-rung extremality and the strict sub-two rail bound, and tests the explicit norm-attaining sign vector. The program outputs `ALL EXACT CHECKS PASSED: 67101` when run with Python 3. These finite checks are independent computational corroboration; the universal result follows from the analytical proof above.

## Relationship to prior work

The graph-gradient least-squares projection and Hodge decomposition are foundational in Jiang, Lim, Yao and Ye (2008), while transfer-current representations appear in Kassel and Wu (2013). Klenke (2017) gives the stationary infinite-ladder rung kernel. A published finite-volume weighted-ladder result gives the full rung-to-rung kernel (2), including endpoint corrections, in a spanning-tree context. **That rung block is prior information, not claimed as a discovery here.** The present theorem additionally reconstructs all rung–rail and rail–rail entries of the *gradient* projector, proves their competing row-sum signs, identifies the central-rung maximizer over *all* edges for each finite size, isolates the five-rung threshold, and determines both parity-dependent sharp defect constants. Those conclusions are not stated in the inspected source.

Schild, Rao and Srivastava (2017) study the absolute transfer-current matrix and prove a general logarithmic spectral bound. Their theorem is compatible with, but does not numerically determine, the sharp ladder \(\ell^\infty\) norm or its extremizing edge.

## Limitations

The claimed contribution is the sharp all-edge operator norm, its extremizers and its finite-size transition; the underlying finite rung Green kernel is previously recorded. The argument is specific to unweighted two-rail open ladders; it establishes neither weighted sharp constants nor strip widths greater than two nor corresponding circular-ladder norms. Published priority remains provisional because another source could have already optimized the absolute transfer-current row sums. No independent external verification has been performed.

## References

1. X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067 (first version 7 November 2008); *Mathematical Programming* 127 (2011), 203–244.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (first version 10 December 2013).
3. A. Klenke, *The Random Spanning Tree on Ladder-like Graphs*, arXiv:1704.00182 (first version 1 April 2017).
4. A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632 (first version 4 August 2017), SODA 2018.
5. *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees*, public mathematical research record (4 October 2026), published-finding corpus repository, record identifier `647fc3f7ee8c`.
