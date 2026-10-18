# Full symbolic entropy across the Cantor-to-interval transition of a contracting skew product

## Finding
For the piecewise-affine three-dimensional map in Example 5.1 of Catsigeras, Guiraud, Meyroneinc and Ugalde, the separated-set entropy is exactly \(\log 2\) throughout the entire open contraction-parameter region, even when its attractor is a connected interval. More precisely, put \(\delta=\min\{1-\lambda_1,1-\lambda_2\}>0\). For every \(0<\varepsilon<\delta\) and every integer \(n\ge2\), its maximal \((n,\varepsilon)\)-separated cardinality satisfies
\[
2^{n-1}\le r(n,\varepsilon)\le 2^n\big(\lfloor 1/\varepsilon\rfloor+1\big)^3.
\]
In particular, \(\lim_{n\to\infty}n^{-1}\log r(n,\varepsilon)=\log2\) for each such fixed \(\varepsilon\), and the separated-set topological entropy is \(\log 2\).

## Assumptions and scope
Let \(T=\{(x,y):x\ge0,\ y\ge0,\ x+y\le1\}\) and \(X=T\times[0,1]\). Fix \(0<\alpha<1/2\) and \(0<\lambda_1,\lambda_2<1\). For \(y<x\) define \(g_1(x,y)=\alpha(x-y,2y)\), and for \(x<y\) define \(g_2(x,y)=\alpha(2x,y-x)\). Set \(\varphi_1(z)=\lambda_1z\), \(\varphi_2(z)=1-\lambda_2+\lambda_2z\), and apply \(F(x,y,z)=(g_i(x,y),\varphi_i(z))\) on branch \(i\). Only the forward-invariant set \(\widetilde X\) of states whose orbits never meet \(x=y\) is used; how the map is defined on that dividing set is irrelevant.

Use the maximum-coordinate metric \(d_\infty\) on \(X\), and let \(r(n,\varepsilon)\) be the supremum of cardinalities of sets \(E\subset\widetilde X\) such that every two different points in \(E\) have \(d_\infty(F^t p,F^t q)>\varepsilon\) at some \(0\le t<n\). Replacing strict \(>\varepsilon\) by \(\ge\varepsilon\) does not affect the conclusion, and the entropy agrees with the equivalent Euclidean-metric definition of the cited source. The theorem concerns entropy of the full admissible system, **not entropy of a map restricted to its attractor**.

## Proof
**1. Full symbolic coding of the contracting base.** When \(u=x+y>0\), write \(q=y/u\in[0,1]\). The first branch is exactly \(q<1/2\), the second \(q>1/2\). A direct substitution into both branch formulas gives \(u'=\alpha u\) and \(q'=2q\pmod1\). Thus any nondyadic \(q\in(0,1)\) supplies an admissible infinite orbit, and its itinerary is its successive binary digits (with digit zero corresponding to branch 1).

For \(n\ge2\), let \(m=2^{n-1}\). For each integer \(k\in\{0,\ldots,m-1\}\), choose
\[
q_k=\frac{7k+1}{7m},\quad u_0=\frac12,\quad (x_0,y_0)=\left(\frac{1-q_k}{2},\frac{q_k}{2}\right),\quad z_0=\frac12.
\]
The denominator of \(q_k\), after reduction, has a factor of seven, because \(7k+1\equiv1\pmod7\). Therefore each \(q_k\) is nondyadic, so these are \(m\) points of \(\widetilde X\). Their first \(n-1\) binary digits, hence their first \(n-1\) branch symbols, run through all binary words of that length.

**2. Strict one-step fiber separation at the first differing symbol.** For every \(z\in[0,1]\),
\[
\varphi_2(z)-\varphi_1(z)=1-\lambda_2+(\lambda_2-\lambda_1)z
\ge\min\{1-\lambda_1,1-\lambda_2\}=\delta>0.
\]
Take two different constructed points and let \(t\le n-2\) be their first differing branch time. Both began with \(z_0=1/2\), so their fiber positions at time \(t\) are **identical**: their first \(t\) fiber maps coincide. After applying their respective, now different, maps at time \(t\), their fiber positions at time \(t+1<n\) differ by at least \(\delta\). Hence this family is \((n,\varepsilon)\)-separated for every \(0<\varepsilon<\delta\), proving \(r(n,\varepsilon)\ge2^{n-1}\). No hypothesis of disjoint fiber images is required.

**3. A uniform combinatorial upper bound.** Each branch extension is a contraction in \(d_\infty\) with Lipschitz constant at most
\[
\kappa=\max\{2\alpha,\lambda_1,\lambda_2\}<1.
\]
If two points have the same branch word of length \(n\), their distance at every time \(t<n\) is at most \(\kappa^t\) times their initial distance. Divide the ambient unit cube into \(M^3\) half-open cubes of side \(1/M<\varepsilon\), where \(M=\lfloor1/\varepsilon\rfloor+1\) (assign endpoints to neighboring cells). Within one initial cube and a single length-\(n\) itinerary, points cannot be \((n,\varepsilon)\)-separated. As there are at most \(2^n\) itineraries, any separated family has at most \(2^nM^3\) members. Taking the logarithm, dividing by \(n\), and sending \(n\to\infty\) establishes the claimed fixed-scale limit and entropy. The proof does not invoke compact-system factor-entropy results on the noncompact set \(\widetilde X\).

## Verification
The self-contained `verify.py` performs exact-rational calculations for four parameter choices, including the Cantor, overlapping-interval, exact-touching and asymmetric regimes, and all binary words of lengths one through eight. It checks admissible binary itineraries, the strict first-difference fiber gap and the stated branch-contraction constant. The program reports `VERIFY_OK`. These finite checks test the implementation and formulas only; the three analytic steps above establish the assertion for every admissible parameter and every \(n\ge2\).

## Relationship to prior work
Catsigeras, Guiraud, Meyroneinc and Ugalde construct precisely this map in Example 5.1 and identify its attractor as \(\{(0,0)\}\times K\), where \(K\) is a Cantor set for \(\lambda_1+\lambda_2<1\) and the full interval for \(\lambda_1+\lambda_2\ge1\). Their Proposition 5.3(3) proves only \(h_{\mathrm{top}}\ge(\log2)/k_0\), with \(k_0=\min\{k\ge1:\lambda_1^k+\lambda_2^k<1\}\). For \(\lambda_1+\lambda_2\ge1\), this yields a lower bound strictly smaller than \(\log2\). The fixed-scale synchronous-fiber argument closes this gap without requiring separation between the *sets* \(\varphi_1([0,1])\) and \(\varphi_2([0,1])\). The original paper explicitly warns that noncompact symbolic semiconjugacy by itself does not imply its desired entropy bound. General entropy-via-multiplicity estimates for piecewise-affine skew products (Kruglikov and Rypdal) do not supply this exact lower bound for this concrete three-dimensional model.

## Limitations
The result is for \(0<\alpha<1/2\) and \(0<\lambda_i<1\), a shared initial fiber value in the explicit lower-bound construction, and the forward-admissible set that avoids the discontinuity. It makes no claim about entropy of a map on the possibly non-invariant attractor, parameter endpoints, random driving, or arbitrary piecewise-affine contractions. It also does not establish absolute historical priority beyond the sources examined. The self-review is not independent validation.

## References
1. E. Catsigeras, P. Guiraud, A. Meyroneinc, E. Ugalde, *On the Asymptotic Properties of Piecewise Contracting Maps*, arXiv:1108.1501v2 (2014), Example 5.1 and Proposition 5.3, https://arxiv.org/html/1108.1501v2 .
2. B. Kruglikov and M. Rypdal, *Entropy via multiplicity*, arXiv:math/0505019v3 (2005), https://arxiv.org/abs/math/0505019 .
3. E. Catsigeras, P. Guiraud, and A. Meyroneinc, *Complexity of injective piecewise contracting interval maps*, arXiv:1702.03599 (2017), https://arxiv.org/abs/1702.03599 .
