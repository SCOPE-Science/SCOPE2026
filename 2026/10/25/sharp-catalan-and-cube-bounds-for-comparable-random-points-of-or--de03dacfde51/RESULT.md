# Sharp Catalan and cube bounds for comparable random points of order polytopes

## Finding
For every nonempty finite poset \(P\) with \(n\) elements, define its standard order polytope
\[
\mathcal O(P)=\{x\in[0,1]^P:x_i\le x_j\text{ whenever }i\le_P j\}.
\]
For two independent points \(X,Y\) distributed uniformly by ordinary \(n\)-dimensional Lebesgue volume, define the **one-way comparability probability** \(q(P)=\Pr(X_i\le Y_i\ \forall i\in P)\). Then
\[
\boxed{2^{-n}\le q(P)\le \frac1{n+1}.}
\]
If \(n\ge2\), equality on the left holds **if and only if** \(P\) is an antichain, and equality on the right holds **if and only if** \(P\) is a chain. Because pointwise equality between two independently sampled continuous vectors has probability zero, the probability of comparability in at least one direction is \(2q(P)\).

Write \(e(P)\) for the number of linear extensions of \(P\), and let \(C_2\) be the two-element chain. There is also an exact counting identity:
\[
q(P)=\frac{e(P\times C_2)}{\binom{2n}{n}\,e(P)^2}.
\]
For the star poset \(S_p\) consisting of \(p\ge1\) mutually incomparable minima dominated by one common maximum, the exact value and asymptotic are
\[
q(S_p)=\frac{(p+1)2^{p-1}(p!)^2}{(2p+1)!}
\sim \frac{\sqrt{\pi p}}{4\,2^p},\qquad
\frac{q(S_p)}{2^{-(p+1)}}\sim\frac{\sqrt{\pi p}}2.
\]
This gives a strict, explicitly quantified intermediate regime between the two sharp universal extremal behaviors.

## Assumptions and scope
The order on \(P\) is finite and antisymmetric; all coordinates are labeled and the volume measure is normalized on the **full-dimensional standard** order polytope, not on its set of vertices. Product comparability is the coordinatewise order on the ambient cube. No random-poset hypothesis is imposed. If \(n=1\), the single poset is simultaneously a chain and an antichain, and both bounds equal \(1/2\). All factorial formulas are exact for the stated positive integers.

## Proof
**Step 1 (positive association and lower bound).** The uniform density of \(\mathcal O(P)\), extended by zero to the cube, satisfies the continuous FKG lattice condition. Indeed \(\mathcal O(P)\) is closed under coordinatewise minimum and maximum, so its indicator \(f\) satisfies \(f(x\wedge y)f(x\vee y)\ge f(x)f(y)\). Thus its uniform law is associated. Write \(F_i(t)=\Pr(X_i\le t)\). For every fixed \(y\in\mathcal O(P)\), the events \(\{X_i\le y_i\}\) are all decreasing; association (also valid for decreasing events) gives
\[
\Pr(X\le y)\ge\prod_{i\in P} F_i(y_i).
\]
Average over the independent \(Y\). The functions \(F_i(Y_i)\) are increasing coordinate functions, hence again associated, so
\[
q(P)\ge\mathbb E\prod_iF_i(Y_i)\ge\prod_i\mathbb EF_i(Y_i)=2^{-n}.
\]
The final equality uses continuity of each marginal and the probability integral transform.

To see **strictness** for a non-antichain, take two distinct elements \(i<_Pj\). Their marginals each have positive density throughout \((0,1)\), while \(Y_i\le Y_j\) holds almost surely. Consequently the two variables cannot be independent: independent marginals with full support would give positive probability to \(Y_i>3/4\) and \(Y_j<1/4\). Association ensures nonnegative covariances of all increasing-threshold events; their dependence implies a strictly positive threshold covariance on an open set. By the Hoeffding covariance identity, strictly increasing continuous distribution transforms preserve a positive covariance: \(\operatorname{Cov}(F_i(Y_i),F_j(Y_j))>0\). Applying association to the pair-product and the remaining coordinate factors produces strict inequality \(\mathbb E\prod_kF_k(Y_k)>2^{-n}\). For an antichain the coordinates are independent uniform variables, giving equality.

**Step 2 (interleavings and upper bound).** The standard order-polytope triangulation has \(e(P)\) equal-volume simplices, one per linear extension. Thus, conditional on the order \(\pi=(\pi_1,\ldots,\pi_n)\) of the coordinates of \(X\) and independently the order \(\sigma\) for \(Y\), the two lists of ascending values are independent order statistics of \(n\) iid uniform points. Each of the \(\binom{2n}{n}\) interleavings of their two ascending lists is equally likely.

Let \(\tau(k)\) be the rank of \(\pi_k\) in \(\sigma\). The condition \(X_{\pi_k}\le Y_{\pi_k}\), for all \(k\), is equivalent to requiring that before the \(j\)-th \(Y\)-symbol the interleaving contain at least \(M_j=\max\{k:\tau(k)\le j\}\) \(X\)-symbols. Every \(M_j\ge j\), since the first \(j\) entries in \(\sigma\) have distinct ranks in \(\pi\). Hence every admissible interleaving is a ballot interleaving in which the \(k\)-th \(X\) precedes the \(k\)-th \(Y\), and there are exactly \(C_n=\binom{2n}{n}/(n+1)\) such words. Therefore \(q(P)\le1/(n+1)\).

If \(\pi=\sigma\), then \(M_j=j\) for all \(j\), so all \(C_n\) ballot words are admissible. If \(\pi\ne\sigma\), some \(M_j>j\). The alternating ballot word \(XYXY\cdots XY\), which has exactly \(j\) \(X\)-symbols before the \(j\)-th \(Y\), is then excluded, so the conditional probability is **strictly** less than \(1/(n+1)\). Thus equality holds precisely when there is just one linear extension of \(P\), equivalently when \(P\) is a chain.

**Step 3 (exact linear-extension count).** In the product order polytope \(\mathcal O(P)\times\mathcal O(P)\), the subset on which \(X_i\le Y_i\) for every \(i\) is exactly the standard order polytope \(\mathcal O(P\times C_2)\). The former has volume \(e(P)^2/(n!)^2\), and the latter has volume \(e(P\times C_2)/(2n)!\); their ratio proves the counting identity.

**Step 4 (star formula).** Condition on the upper coordinates \(S=X_{\mathrm{top}}\) and \(T=Y_{\mathrm{top}}\). Each has density \((p+1)t^p\) on \((0,1)\); conditional on its top, its \(p\) lower coordinates are independent uniform variables between zero and that top. Given \(S=s\le T=t\), the chance that one corresponding lower pair obeys \(X_i\le Y_i\) is \(1-s/(2t)\). Consequently
\[
q(S_p)=(p+1)^2\int_0^1 t^p\int_0^t s^p\left(1-\frac{s}{2t}\right)^pds\,dt
=\frac{p+1}{2}\int_0^1u^p(1-u/2)^pdu.
\]
By \(z=u/2\) and symmetry of the beta integrand, this equals \((p+1)2^{p-1}\mathrm B(p+1,p+1)\), the asserted factorial expression. The central-binomial asymptotic \(\binom{2p}{p}\sim4^p/\sqrt{\pi p}\) gives the final limit.

## Verification
The included standalone `checker.py` exhaustively computes exact linear-extension ratios for every forward-oriented relation subset on up to five labeled elements (\(1099\) cases), verifying the inequalities and equality cases. It independently matches the beta-integral factorial formula against exact doubled-poset counts for seven stars. The output was `VERIFY_OK poset_instances= 1099 star_formula_cases= 7`. Enumeration establishes these finite identities only; the universal bounds and asymptotic are proved analytically above.

## Relationship to prior work
Stanley's order-polytope triangulation and linear-extension volume identity are classical prerequisites, not new. Fang–Fourier–Litza–Pegel study geometric families of marked poset polytopes and transfer maps, not the asserted universal probability envelope. Fried's 2019 theorem gives \(2/(n+1)\) for two uniform simplex points comparable under first-order stochastic dominance: under cumulative coordinates this is precisely the **chain extremal case** of the present two-direction statement, and is **not claimed new here**. Karlin–Rinott's MTP2 association theory explains the probabilistic lower-bound mechanism. The contribution assessed here is the simultaneous sharp **all-finite-poset** bounds, complete equality classification, extension-count interpretation, and star-family quantitative interpolation.

## Limitations
The claimed inequalities apply to uniform volume and coordinatewise order, not to arbitrary log-concave or weighted measures. The chain numerical case and underlying FKG/ballot tools are prior art. Although no encompassing universal statement was identified in the inspected sources and mathematical-record searches, an older equivalent inequality for linear extensions of product posets may exist. There has been no independent mathematical review.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. DOI: 10.1007/BF02187680.
2. X. Fang, G. Fourier, J.-P. Litza, C. Pegel, *A continuous family of marked poset polytopes*, arXiv:1712.01037v1 (first public 2017-12-04); SIAM J. Discrete Math. 34 (2020), 611–639, DOI: 10.1137/18M1228529.
3. S. Fried, *The probability that two random points on the n-probability simplex are comparable with respect to the first order stochastic dominance and the monotone likelihood ratio partial orders*, arXiv:1910.01752v1 (2019-10-03), Theorem 3.9.
4. S. Karlin and Y. Rinott, *Classes of orderings of measures and related correlation inequalities I: Multivariate totally positive distributions*, J. Multivariate Anal. 10 (1980), 467–498.
5. R. Jacobovic and O. Zuk, *A correlation inequality for random points in a hypercube with some implications*, arXiv:2209.00346v1 (2022-09-01).
