# Optimal endpoint stability of affine least squares on the first two Boolean layers

## Finding

Let \(n\ge3\). On \(\Omega_n=\{X\subseteq\{1,\ldots,n\}:|X|=1\text{ or }2\}\), give the singleton layer total probability \(1-\theta\) and the pair layer total probability \(\theta\), uniformly within each layer, where \(0<\theta<1\). Let \(P_\theta\) be the real \(L^2\)-orthogonal projection onto the restrictions of all affine coordinate functions \(a_0+\sum_i a_i\mathbf1_{\{i\in X\}}\). Define
\[
H=n-1+(n-3)\theta,\quad A=\frac{4(n-1)(n-2)}{nH},\quad r=\frac{(n-2)(n-3)}{n(n-1)}.
\]
Every singleton row of the projection has absolute mass \(R_1=1+\theta A\), and every pair row has absolute mass
\[
R_2=1+(1-\theta)A+2r\left(\frac{4(n-1)\theta}{H}-1\right)_+,
\qquad u_+=\max\{u,0\}.
\]
In particular, \(\|P_\theta\|_{\infty\to\infty}=\max\{R_1,R_2\}\). Its minimum over \(0<\theta<1\) is \(3-4/n\), attained uniquely at \(\theta_*=(n-1)/(n+1)\). Exactly the pair rows maximize for \(\theta<\theta_*\), exactly the singleton rows maximize for \(\theta>\theta_*\), and all rows maximize at \(\theta_*\). The minimizing measure is uniform over all atoms, equivalently the law of independent fair Bernoulli coordinates conditioned on having one or two successes. The fair parameter is uniquely optimal in that conditional Bernoulli family.

For \(0\le f\le1\), the largest undershoot below zero and the largest overshoot above one both equal \((\|P_\theta\|_{\infty\to\infty}-1)/2\); their minimum over mixtures is \(1-2/n\), attained only at \(\theta_*\). A signed kernel-row input taking values in \(\{-1,1\}\) attains the operator norm, whereas ordinary \(\{0,1\}\)-valued indicators attain the undershoot and overshoot.

## Assumptions and scope

Both layers have strictly positive probability on every atom. Identify \(X\) with its indicator vector in \(\mathbb R^n\). The affine range has dimension \(n+1\): vanishing on singletons gives \(a_i=-a_0\), and vanishing on any pair then gives \(a_0=0\). The norm is the supremum norm on functions over \(\Omega_n\), not the Hilbert norm. The optimization is over the relative masses of the two uniform layers, not arbitrary nonexchangeable weights or arbitrary projections onto the affine space.

## Proof

**1. Kernel.** For \(S=|X|\), write \(m=\mathbb ES=1+\theta\). The affine space is the orthogonal sum of the two-dimensional space of functions of \(S\) and the contrasts \(v(X)\cdot u\) with \(v(X)=\mathbf1_X-(S/n)\mathbf1\) and \(u\perp\mathbf1\). Orthogonality follows from the conditional mean of \(v\) being zero. On the contrasts, exchangeability makes the second-moment matrix a scalar on \(\mathbf1^\perp\); its trace is \(\mathbb E[S(n-S)]/n=H/n\). This gives
\[
K_\theta(x,y)=1+\frac{(|x|-m)(|y|-m)}{\theta(1-\theta)}+
\frac{n(n-1)}{H}\left(|x\cap y|-\frac{|x||y|}{n}\right),
\qquad (P_\theta f)(x)=\mathbb E[K_\theta(x,Y)f(Y)].
\]
The first two terms sum to \(1/(1-\theta)\) for two singletons, \(1/\theta\) for two pairs, and zero across layers. For a fixed \(x\), the contrast term has conditional mean zero on either target layer. In particular each row has signed mass one.

**2. Singleton rows.** Within the singleton layer the kernel is positive, since its least value is \(1/(1-\theta)-(n-1)/H>0\). In the pair layer the overlap \(U\) with a fixed singleton is one with probability \(2/n\) and zero otherwise. Thus \(\mathbb E|U-2/n|=4(n-2)/n^2\), giving the cross-layer absolute mass \(\theta A\) and total \(R_1\).

**3. Pair rows.** For a fixed pair and a uniform singleton, overlap again has the preceding distribution, yielding cross-layer absolute mass \((1-\theta)A\). For a uniform target pair, the kernel is
\[
\frac1\theta+\frac{n(n-1)}H\left(U-\frac4n\right).
\]
For \(U\ge1\) it is positive: for \(n=3\) it is at least \(1/\theta-1>0\), and for \(n\ge4\) the contrast term is nonnegative. The only potentially negative entries come from disjoint pairs, with conditional probability \(r\), which is zero for \(n=3\). The pair layer has signed mass one. Adding twice the disjoint-pair negative mass yields \(R_2\). By permutation symmetry these are the only row types. A maximizing row \(x\) attains the operator norm with \(f(y)=1\) for \(K_\theta(x,y)\ge0\) and \(f(y)=-1\) otherwise. No input with values only in \(\{0,1\}\) attains that operator norm: the largest absolute output among such inputs is \((\|P_\theta\|_{\infty\to\infty}+1)/2\), and \(\|P_\theta\|_{\infty\to\infty}>1\).

**4. Optimal mixture.** \(R_1' =4(n-1)^2(n-2)/(nH^2)>0\). Below \(\theta_0=(n-1)/(3n-1)\), \(R_2'=-8(n-1)(n-2)^2/(nH^2)<0\); above \(\theta_0\), \(R_2'=-8(n-1)(n-2)/(nH^2)<0\) for \(n\ge4\). For \(n=3\), the disjoint-pair term vanishes and the first derivative formula for \(R_2\) applies everywhere. Both rows are continuous. At \(\theta_*=(n-1)/(n+1)>\theta_0\), we have \(H=2(n-1)^2/(n+1)\), \(4(n-1)\theta_*/H-1=1\), and \(R_1=R_2=3-4/n\). Strict monotonicity in opposite directions gives the asserted unique minimizer and row dominance.

**5. Uniformity, conditioning, and extreme outputs.** Uniform atoms have pair-layer mass \(\binom n2/(n+\binom n2)=\theta_*\). For success probability \(p\in(0,1)\), the conditional pair-to-singleton mass ratio is \((n-1)p/[2(1-p)]\), equaling \((n-1)/2\) precisely at \(p=1/2\). If a fixed row has absolute mass \(R\) and signed mass one, its negative mass in absolute value is \((R-1)/2\) and its positive mass is \((R+1)/2\). The indicator of the negative entries attains the undershoot and its complement attains the overshoot. Maximizing over rows proves the two asserted extrema.

**6. Comparison with determinant optimization.** The eigenvalue of \(\operatorname{Cov}(X)\) in the all-ones direction is \(\theta(1-\theta)/n\), and each contrast eigenvalue is \(H/[n(n-1)]\). Hence
\[
\det\operatorname{Cov}(X)=\frac{\theta(1-\theta)}n\left(\frac{H}{n(n-1)}\right)^{n-1}.
\]
Its logarithm is strictly concave in \(\theta\) and has derivative zero at \(\theta_*\). Thus the determinant criterion has the same optimizer. This observation is a special case of the existing rank-selected design calculation and is not claimed as new.

## Verification

The accompanying `verify.py` can be run with Python 3 and SymPy. It forms and inverts the full weighted Gram matrix over exact rationals and compares every absolute row sum with the formulas above for 46 parameter profiles and 1,061 row instances with \(3\le n\le9\). It also checks the symbolic derivative and crossing identities and the determinant's stationary identity. These computations are supplementary; the proof above is for the full stated domain.

## Relationship to prior work

Filmus–Mossel, Theorem 3.10, gives exchangeable harmonic orthogonality; Filmus–Kindler–Mossel–Wimmer study a single uniform slice. These do not specify the sharp absolute row masses of the present weighted two-layer projection. The rank-selected Boolean-polytope ellipsoid calculation gives the determinant optimizer under a different criterion. At uniform weights the affine space is also the row space of the unsigned vertex–edge incidence matrix of \(K_{n+1}\): map a singleton \(\{i\}\) to \(\{0,i\}\), a pair to the same edge, and put \(c_0=a_0/2, c_i=a_0/2+a_i\), so edge values are \(c_i+c_j\). The weighted result consists of the full dependence on the relative star and nonstar weights and the unique optimum in that family; it is not a claim of novelty for the uniform incidence projector by itself. Equivalent calculations under other incidence, design or discrete least-squares terminology remain a publication-priority risk.

## Limitations

The result concerns exactly the stated two positive-weight uniform layers and affine orthogonal projection. No result is asserted for higher degrees, other ranks, nonexchangeable weights, nonorthogonal projections, or either endpoint \(\theta=0,1\). Finite checks do not replace the proof, and literature comparison does not certify worldwide priority.

## References

1. Y. Filmus, G. Kindler, E. Mossel and K. Wimmer, *Invariance principle on the slice*, arXiv:1504.01689, https://arxiv.org/abs/1504.01689.
2. Y. Filmus and E. Mossel, *Harmonicity and Invariance on Slices of the Boolean Cube*, arXiv:1507.02713, https://arxiv.org/abs/1507.02713.
3. *Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoids-of-arbitrary-rank-selected-boolean-polyt--3c04f47dc8c3.
