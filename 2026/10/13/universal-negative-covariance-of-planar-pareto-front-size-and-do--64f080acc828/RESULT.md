# Universal negative covariance of planar Pareto-front size and dominated hypervolume

## Finding

**Theorem (exact dependence and uniform benchmark).** Let \(n\ge2\). Take \(n\) independent observations \((X_i,Y_i)\) with a common product distribution on \([0,1]^2\): the two coordinate marginals are independent, continuous (atomless), and nondegenerate. Let \(M_n\) count upper-right Pareto maxima. Let \(V_n\) be the Lebesgue area of the union of origin-anchored rectangles \(\bigcup_{i=1}^n[0,X_i]\times[0,Y_i]\). Then
\[
\operatorname{Cov}(M_n,V_n)<0.
\]
For arbitrary such continuous product marginals the exact covariance is a finite sum of strictly negative terms given below. For independent uniform coordinates the covariance simplifies, for every \(n\ge2\), to
\[
\boxed{\operatorname{Cov}(M_n,V_n)=-\frac{(n+2)H_n-(n+1)H_n^{(2)}-n}{(n+1)^2}},
\]
where \(H_n=\sum_{j=1}^n j^{-1}\) and \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\). Consequently,
\[
\operatorname{Cov}(M_n,V_n)=-\frac{\log n+\gamma-\pi^2/6-1}{n}+O\!\left(\frac{\log n}{n^2}\right).
\]
The sign theorem does not require uniformity of the coordinate marginals: it requires their independence.

## Assumptions and scope

The observations are iid planar vectors with coordinates in \([0,1]\), independent within each vector. Each marginal distribution function is continuous, with a nondegenerate law. Coordinates may have densities, gaps in support, or singular continuous distributions. Pareto maximality means that no other sampled point is at least as large in both coordinates. Almost surely no coordinate ties occur. The dominated hypervolume uses the *fixed origin* as reference, not a random or data-dependent reference point. The theorem concerns finite \(n\ge2\); at \(n=1\), the maximal-point count is deterministic and its covariance with hypervolume is zero.

Put the first-coordinate order statistics in decreasing order: \(X_{[1]}>\cdots>X_{[n]}\), and set \(X_{[n+1]}=0\). Write \(\Delta_k=X_{[k]}-X_{[k+1]}\), and let \(Z_1,\ldots,Z_n\) denote the correspondingly reordered second coordinates. Let \(Q\) be any generalized quantile function of their common marginal distribution. Let \(U_{(k)}\sim\operatorname{Beta}(k,1)\). Define \(a_k=\mathbb E\Delta_k>0\). The precise distribution-dependent identity is
\[
\boxed{\operatorname{Cov}(M_n,V_n)=-\sum_{k=1}^{n-1}a_k\sum_{r=1}^{n-k}\frac{\operatorname{Cov}(Q(U_{(k)}),U_{(k)}^r)}{r}}.
\]
Every covariance in the double sum is strictly positive, so this formula also proves strict negativity.

## Proof

**1. Separate geometry from relative ranks.** Independence of the two coordinate marginals implies that the rearranged values \(Z_1,\ldots,Z_n\) are still iid and independent of all sorted first-coordinate values. Let \(B_k=\max_{1\le i\le k}Z_i\), and \(I_j=\mathbf1\{Z_j>B_{j-1}\}\), with \(I_1=1\). In decreasing first-coordinate order, a point is Pareto maximal precisely when its second coordinate exceeds all earlier second coordinates. Hence \(M_n=\sum_{j=1}^n I_j\). The area of the union of origin rectangles is a staircase integral:
\[
V_n=\sum_{k=1}^n\Delta_k B_k.
\]
The gaps \(\Delta_k\) are independent of \((I_j,B_k)\) for all \(j,k\), so linearity gives
\[
\operatorname{Cov}(M_n,V_n)=\sum_{k=1}^n a_k\sum_{j=1}^n\operatorname{Cov}(I_j,B_k).
\]

**2. Independent ranks cancel the early contributions.** If \(j\le k\), the indicator \(I_j\) depends solely on the relative ordering of the first \(k\) values, and the sample maximum \(B_k\) is independent of that relative ordering for iid atomless samples. Thus \(\operatorname{Cov}(I_j,B_k)=0\) when \(j\le k\). In particular the \(k=n\) term vanishes.

**3. Later records contribute strictly negatively.** Fix \(j>k\), and write \(r=j-k\). Conditional on \(B_k=h\), the record event \(I_j=1\) requires \(Z_j\) to be the largest of the \(r\) future observations and to exceed \(h\). By exchangeability and atomlessness,
\[
\Pr(I_j=1\mid B_k=h)=\frac{1-F_Y(h)^r}{r}.
\]
Therefore
\[
\operatorname{Cov}(I_j,B_k)=-\frac1r\operatorname{Cov}(B_k,F_Y(B_k)^r).
\]
The probability integral transform gives \(B_k\overset{d}=Q(U_{(k)})\) and \(F_Y(B_k)\overset{d}=U_{(k)}\), proving the double-sum identity. Both \(Q\) and \(u\mapsto u^r\) are nondecreasing; the latter is strictly increasing, and \(Q(U_{(k)})\) is nondegenerate. For an independent copy \(U_{(k)}'\),
\[
2\operatorname{Cov}(Q(U_{(k)}),U_{(k)}^r)=\mathbb E\left[(Q(U_{(k)})-Q(U_{(k)}'))(U_{(k)}^r-(U_{(k)}')^r)\right]>0.
\]
The expectation is positive because the integrand is nonnegative and strictly positive on an event of positive probability. Likewise all \(a_k>0\) for \(k<n\). Since \(n\ge2\), the \(k=1,r=1\) term occurs and is strictly negative. This proves the sign without any assumption on the shape of the continuous marginals.

**4. Uniform specialization.** For uniform coordinates, the expected ordered gaps equal \(a_k=1/(n+1)\) for all \(k\). Since \(U_{(k)}\sim\operatorname{Beta}(k,1)\),
\[
\mathbb E U_{(k)}^s=\frac{k}{k+s},\quad
\operatorname{Cov}(I_j,B_k)=-\frac{k}{(k+1)j(j+1)}\quad(j>k).
\]
Summing \(1/[j(j+1)]\) for \(j=k+1,\ldots,n\) yields
\[
\operatorname{Cov}(M_n,V_n)=-\frac1{n+1}\sum_{k=1}^{n-1}\frac{k}{k+1}\left(\frac1{k+1}-\frac1{n+1}\right).
\]
Use \(\sum_{k=1}^{n-1}k/(k+1)^2=H_n-H_n^{(2)}\) and \(\sum_{k=1}^{n-1}k/(k+1)=n-H_n\), then simplify to the boxed harmonic identity. The standard harmonic expansions \(H_n=\log n+\gamma+O(n^{-1})\) and \(H_n^{(2)}=\pi^2/6+O(n^{-1})\) give the stated asymptotic with the displayed remainder.

## Verification

The bundled self-contained `verify.py` uses exact rational arithmetic and two independent routes. First, it enumerates all permutations of the second-coordinate ranks against first-coordinate order-statistic moments and computes the joint moment of Pareto count and staircase area. Second, it evaluates the closed \(\operatorname{Beta}(k,1)\) covariance kernel. The paths agree for every \(2\le n\le7\) and coordinate power-law quantiles with integer exponents \(1,2,3\), giving 54 permutation/kernel comparisons. Another 98 exact checks confirm the harmonic identity for \(2\le n\le99\). The independent permutation enumeration is finite evidence for implementation; the preceding proof establishes the theorem for every \(n\) and every allowed marginal law. Run `python3 verify.py` to replay all arithmetic checks.

## Relationship to prior work

Bai, Hwang, Liang, and Tsai (2001) developed distributional limit results and exact moment techniques for the number of Pareto maximal points of planar samples; their primary MSC is 60D05. Hwang, Tsai, and Chen (2011/2013) studied cardinalities of generalized dominant skylines. These sources describe the maximal-point statistic and its marginal distributional behavior; their inspected main results do not state a joint law with the **dominated hypervolume**. The latter is a separate nonlinear geometric statistic measuring the union of origin-anchored rectangles. The present finding identifies its covariance with maximal-point count under product sampling, with an exact universal sign and a sharp uniform-square benchmark. This comparison is not a proof of absolute historical priority; broader record-process identities could imply the same relation.

## Limitations

Independence of the two coordinates and a fixed reference point are essential assumptions of the theorem; no claim is made for dependent coordinates, discrete margins with ties, random reference points, non-planar hypervolume, or distribution-dependent universal asymptotic constants. The strict sign and exact uniform formula do not establish stochastic monotonicity, conditional ordering, or causal effects. Only the uniform-square asymptotic is quantified; other continuous marginals have the stated exact kernel but need not share its asymptotic rate. Historical originality has a residual risk from implicit classical record-functional formulas. No independent audit has been performed.

## References

1. Z.-D. Bai, H.-K. Hwang, W.-Q. Liang, T.-H. Tsai (2001), *Limit Theorems for the Number of Maxima in Random Samples from Planar Regions*, Electronic Journal of Probability 6, Article 3, 1–41, doi:10.1214/EJP.v6-76. First verified public article date: 2001-01-22.
2. H.-K. Hwang, T.-H. Tsai, W.-M. Chen, *Threshold Phenomena in \(k\)-Dominant Skylines of Random Samples*, arXiv:1111.6224v1 (2011); SIAM Journal on Computing 42 (2013), 405–441, doi:10.1137/110856952.
3. Z.-D. Bai, L. Devroye, H.-K. Hwang, T.-H. Tsai (2005), *Maxima in Hypercubes*, Random Structures & Algorithms 27, 290–309, doi:10.1002/rsa.20053 (marginal maxima asymptotics).
