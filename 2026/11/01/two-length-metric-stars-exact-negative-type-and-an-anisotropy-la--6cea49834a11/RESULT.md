# Two-length metric stars: exact negative type and an anisotropy law

## Finding

Let \(m,n\ge 2\) be integers. Let \(T_{m,n}(a,b)\) be the finite metric tree consisting of a hub, \(m\) leaves at edge length \(a>0\), and \(n\) other leaves at edge length \(b>0\), equipped with the unique-path metric \(d\). Thus the nonzero distances are \(a,b,2a,2b,a+b\) according to the vertex types. For \(p>0\), define

\[
 F_k(p)=2k-(k-1)2^p,\qquad
 \Delta_p(a,b)=\frac{(a+b)^p-a^p-b^p}{(ab)^{p/2}},\qquad
 P_k=\log_2\frac{2k}{k-1}.
\]

The supremal \(p\)-negative-type exponent \(\wp=\wp(T_{m,n}(a,b))\) is the **unique** root in \((1,\min\{P_m,P_n\})\) of

\[
 F_m(\wp)F_n(\wp)=mn\,\Delta_{\wp}(a,b)^2. \tag{1}
\]

The metric has strict \(p\)-negative type for every \(0<p<\wp\), has non-strict \(\wp\)-negative type with exactly one zero-sum equality direction, and fails \(p\)-negative type for every \(p>\wp\). The Euclidean embedding of the snowflake \(d^{p/2}\) has minimum affine dimension \(m+n\) for \(0<p<\wp\), and exactly \(m+n-1\) at \(p=\wp\).

At fixed \(m,n\), the critical exponent depends on the lengths only through the absolute log-ratio \(|\log(a/b)|\). It is strictly increasing in that quantity, with

\[
 \wp\bigl(T_{m,n}(a,a)\bigr)
 =\log_2\frac{2(m+n)}{m+n-1},\qquad
 \lim_{a/b\to0\ \mathrm{or}\ \infty}\wp(T_{m,n}(a,b))
 =\min\{P_m,P_n\}=P_{\max\{m,n\}}.
 \tag{2}
\]

In particular, exchanging the two arm lengths while **keeping each group's leaf count fixed** does not change the exponent, although the two resulting weighted trees need not be isometric. For \(m=n=2\), every finite positive ratio has \(\wp<2\), but \(\wp\to2\) in the extreme length-ratio limit.

## Assumptions and scope

The metric space consists of all \(N=m+n+1\) vertices, **including the hub**; edge lengths are path lengths, not conductances or vertex masses. We require \(m,n\ge2\) and finite positive \(a,b\). For \(p>0\), \(p\)-negative type means that every real vector \(z\) indexed by vertices with \(\sum_v z_v=0\) obeys

\[
 Q_p(z)=\sum_{v,w}z_vz_wd(v,w)^p\le0.
\]

It is strict when equality requires \(z=0\). Generalized roundness has the same supremum. No claim is made here for arbitrary independent arm lengths or additional internal vertices.

## Proof

**Exact quadratic decomposition.** Write the coefficients on the two leaf classes as \(\alpha_i=x+u_i\) and \(\beta_j=y+v_j\), where \(\sum_i u_i=\sum_j v_j=0\). The hub coefficient is forced to equal \(-mx-ny\). Summing all within-class, cross-class and hub pairs gives the exact identity

\[
\begin{aligned}
Q_p(z)={}&-(2a)^p\sum_{i=1}^m u_i^2-(2b)^p\sum_{j=1}^n v_j^2\\
&-m a^pF_m(p)x^2-n b^pF_n(p)y^2\\
&+2mn\bigl((a+b)^p-a^p-b^p\bigr)xy. \tag{3}
\end{aligned}
\]

Thus the two internal leaf-fluctuation sectors are always strictly negative. In the remaining two-dimensional sector the quadratic matrix is

\[
 M_p=\begin{pmatrix}
 -m a^pF_m(p)&mn((a+b)^p-a^p-b^p)\\
 mn((a+b)^p-a^p-b^p)&-n b^pF_n(p)
 \end{pmatrix}.
\]

For \(1<p<\min\{P_m,P_n\}\), both diagonal entries are strictly negative. The determinant of \(M_p\) is

\[
 mn(ab)^p\left[F_m(p)F_n(p)-mn\Delta_p(a,b)^2\right]. \tag{4}
\]

**Unique first crossing.** Both \(F_m\) and \(F_n\) decrease strictly with \(p\) and are positive up to their first zeros \(P_m,P_n\). Write \(u=a/(a+b)\). For \(p>1\),

\[
 \Delta_p(a,b)=\frac{1-u^p-(1-u)^p}{[u(1-u)]^{p/2}}.
\]

The numerator is strictly positive and increases with \(p\), while the denominator strictly decreases. Hence \(\Delta_p\) strictly increases on \((1,\infty)\). At \(p=1\), the determinant bracket in (4) equals \(4\); at \(p=\min(P_m,P_n)\) it is negative. There is therefore one and only one zero \(\wp\) in the stated interval. Formula (3) gives strict negative type below this crossing in the interval \(p>1\). At the crossing, \(M_{\wp}\) is negative semidefinite of rank one, while both internal sectors remain strictly negative. Its kernel is one-dimensional; explicitly, after taking \(y=1\), the leaf-class means in an equality vector obey

\[
 x=\frac{n((a+b)^\wp-a^\wp-b^\wp)}{a^\wp F_m(\wp)},\qquad
 z_{\mathrm{hub}}=-mx-n.
\]

Above the crossing but below \(\min(P_m,P_n)\), the determinant is negative and \(M_p\) has a positive direction. At and beyond the first diagonal zero, there is likewise a positive direction (the nonzero off-diagonal term handles equality at the diagonal zero). Thus no \(p>\wp\) has negative type.

For \(p=1\), every zero-sum vector obeys the stronger identity

\[
 Q_1(z)=-2a\sum_i\alpha_i^2-2b\sum_j\beta_j^2<0
\]

unless all coefficients vanish. The standard exponent-inheritance theorem for negative type then gives strict \(p\)-negative type also for \(0<p<1\). Alternatively this follows from Schoenberg's integral representation of fractional powers of strict negative-type kernels. This completes the claimed exponent classification.

**Monotonicity under length contrast.** Scaling both lengths together does not change \(\wp\). Put \(a=e^s,b=e^{-s}\) with \(s\ge0\). The length-dependent term becomes

\[
 \Delta_p(e^s,e^{-s})=(2\cosh s)^p-2\cosh(ps).
\]

For \(s>0\) and \(1<p<2\), strict concavity of \(t\mapsto\log\sinh(ts)\) on \([1,2]\) implies

\[
 \sinh(ps)>(2\cosh s)^{p-1}\sinh s.
\]

Differentiating the preceding expression for \(\Delta_p\), we obtain

\[
 \frac{d}{ds}\Delta_p(e^s,e^{-s})
 =2p\bigl[(2\cosh s)^{p-1}\sinh s-\sinh(ps)\bigr]<0. \tag{5}
\]

Since \(1<\wp<\min(P_m,P_n)\le2\), decreasing the cross term \(\Delta_p\) forces its unique equality point in (1) strictly upward as \(s\) grows. At \(s=0\), direct specialization to an equal-arm star of \(m+n\) leaves yields the first value in (2). For any fixed \(1<p<\min(P_m,P_n)\), the binomial expansion gives \(\Delta_p(e^s,e^{-s})\to0\) as \(s\to\infty\) (because \(p<2\)). The determinant bracket is eventually positive at that \(p\), proving the limit in (2). Symmetry of \(\Delta_p(a,b)\) proves invariance under inverting the ratio.

**Embedding ranks.** On the \((N-1)\)-dimensional zero-sum subspace, the negative of half of \(Q_p\) is the centered Euclidean Gram form associated with squared distances \(d^p\). Its rank is \(N-1=m+n\) below \(\wp\), and \(N-2=m+n-1\) at the unique rank-one crossing. Schoenberg's criterion therefore gives exactly the claimed minimum Euclidean dimensions.

## Verification

The standalone file `verify_two_level_star.py` recomputes all pairwise metric distances rather than using (3) to generate the input matrix. It tests (3) against direct quadratic forms in 168 exact rational trials, including powers \(1,2,3\); independently checks the strict/critical/indefinite spectra with a Jacobi eigensolver for 20 combinations of leaf counts and length ratios; and checks uniform-length roots, length-exchange symmetry, and ratio monotonicity numerically. Execute `python3 verify_two_level_star.py`. These tests support, but do not substitute for, the all-real-exponent proof above.

## Relationship to prior work

Doust and Weston, *Enhanced negative type for finite metric trees* (first public arXiv posting 2007-05-03), prove enhanced strict \(1\)-negative type on all weighted finite trees and explicitly evaluate the supremal exponent for **unweighted equal-arm stars** (Theorem 38). Their evaluated star formula is recovered when \(a=b\) above; neither the two-length threshold (1) nor its contrast monotonicity (2) is stated in the inspected text. Li and Weston, *Strict \(p\)-negative type of a metric space* (2009), prove the exponent-inheritance principle used here. Sánchez, *On the supremal \(p\)-negative type of a finite metric space* (2011), gives a general matrix criterion and evaluates unweighted complete bipartite graph metrics; that method does not itself evaluate the present weighted family or imply the contrast law without the new two-sector reduction and inequality (5).

Doust and Weston, *Beyond trees: the metric geometry of subsets of weighted Hamming cubes* (arXiv:2404.06684, 2024), establish a family of exact \(1\)-negative-type and distance-matrix theorems for subsets of weighted Hamming cubes. The weighted star embeds in that setting, but their inspected Theorem 1.1 and Sections 2 and 6 do not evaluate the supremal exponent above \(1\) for two arm-length classes or prove the present anisotropy law. Their Example 6.10 studies non-linear zero-form loci at \(p=2\) for an ordinary three-leaf star rather than this sharp threshold.

A broader metric-transform paper of Deza and Maehara (1990) was identified through subsequent citations and its accessible abstract. Its full text was not accessible in this review, so an equivalent special-case computation there remains a publication-priority risk. The result is therefore a best-knowledge literature distinction, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The statement is for finite positive lengths, two arm-length classes, and at least two leaves in each class. The limit in (2) is a limit of exponents, not an attained exponent for any finite nonzero ratio; in particular the limiting value \(2\) for four leaves is not attained. No exact exponent formula is claimed for stars with three or more distinct arm lengths, and no independent mathematical validation has been performed.

## References

1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411 (first version 2007-05-03), especially Theorem 38, https://arxiv.org/abs/0705.0411.
2. H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first version 2009-01-06), https://arxiv.org/abs/0901.0695.
3. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first version 2011-08-02), https://arxiv.org/abs/1108.0451.
4. I. Doust and A. Weston, *Beyond trees: the metric geometry of subsets of weighted Hamming cubes*, arXiv:2404.06684 (2024), particularly Theorem 1.1 and Section 6, https://arxiv.org/abs/2404.06684.
5. M. Deza and H. Maehara, *Metric transforms and Euclidean embeddings*, Transactions of the American Mathematical Society **317** (1990), 661–671, doi:10.1090/S0002-9947-1990-0974513-6 (abstract and citations inspected; full text not obtained).
