# Exact clustered-ultrametric Lipschitz-ball volumes and a strict balancing law

## Finding
Let a finite metric space be partitioned into \(k\ge2\) nonempty classes of sizes \(n_1,\ldots,n_k\), with total cardinality \(N\). Distinct points of class \(i\) have distance \(t_i\in(0,1]\), while points in different classes have distance \(1\). In anchored potential coordinates, the real Lipschitz-dual unit ball \(Q\) has dimension \(N-1\) and exact Lebesgue volume
\[
\boxed{\operatorname{vol}_{N-1}(Q)=
\left(\prod_{i=1}^{k}t_i^{n_i-1}\right)
\sum_{j=1}^{k}n_j\prod_{i\ne j}\bigl[n_i-(n_i-1)t_i\bigr].}
\]
The formula permits different positive within-class distances, as well as singleton classes.

When all \(t_i=t\), define \(r=(1-t)/t\) and let \(e_j(n_1,\ldots,n_k)\) be the degree-\(j\) elementary symmetric polynomial. The same volume is
\[
\boxed{V_t(n_1,\ldots,n_k)
=t^{N-1}\sum_{j=1}^{k}j r^{j-1}e_j(n_1,\ldots,n_k).}
\]
For fixed integers \(N\ge k\ge2\) and fixed \(0<t<1\), this volume is strictly Schur-concave in the class-size partition: every nontrivial Robin Hood transfer strictly increases volume. Therefore balanced class sizes uniquely maximize, and \((N-k+1,1,\ldots,1)\) uniquely minimize, up to permutation. At \(t=1\), every profile has volume exactly \(N\); the strict comparison does not extend to that endpoint.

For fixed \(k\ge2\) and \(t\in(0,1)\), along multiples of \(k\) as \(N\to\infty\), the maximal-to-minimal ratio obeys
\[
\boxed{\frac{V_t(N/k,\ldots,N/k)}{V_t(N-k+1,1,\ldots,1)}
\sim \frac{(1-t)^{k-1}}{k^{k-1}[k-(k-1)t]}N^{k-1}.}
\]
These are coordinate volumes of dual balls, not invariantly normalized volumes of the primal Lipschitz-free balls.

## Assumptions and scope
All spaces and potentials are real. The points of the finite space \(M\) are labeled, and \(o\in M\) is any chosen basepoint. Let
\[
Q=\{f:M\to\mathbb R:f(o)=0,\ |f(x)-f(y)|\le d(x,y)\ \text{for all }x,y\in M\}.
\]
The displayed inequalities are exactly the unit ball of \(\operatorname{Lip}_0(M)\), the finite-dimensional dual of the Lipschitz-free space \(\mathcal F(M)\). The coordinate Lebesgue measure takes the \(N-1\) values \(f(x)\), \(x\ne o\), as standard coordinates. Changing the basepoint changes these coordinates by an integer-unimodular linear map and preserves volume.

All \(n_i\) are positive integers, \(N=\sum_i n_i\), and \(0<t_i\le1\). Because within-class distances do not exceed cross-class distance, the metric satisfies the triangle inequality (indeed it is an ultrametric). For singleton classes the value of \(t_i\) is immaterial, and the formula is independent of it. The Schur comparison requires a *common* \(t\) strictly between zero and one, and compares integer profiles of the same \(N,k\). The asymptotic statement additionally fixes \(k,t\) and assumes \(k\mid N\).

## Proof
**1. An anchored-coordinate translation identity.** Define \(F(L)\), for real \(L\ge1\), to be the \(N\)-dimensional Lebesgue volume of the vectors \(x\in[0,L]^M\) with within-class ranges at most \(t_i\) and total range at most \(1\). Since the cross-class distance is \(1\) and each within-class distance is at most \(1\), these are precisely the Lipschitz inequalities before choosing an additive constant. The change of variables \(x=(f+s\mathbf1)\), \(f(o)=0\), is unimodular. For each \(f\in Q\), the allowed interval for \(s\) has length \(L-(\max f-\min f)\), since \(\max f-\min f\le1\). Hence
\[
F(L)=\int_Q\bigl[L-(\max f-\min f)\bigr]df,
\qquad F'(1+)=\operatorname{vol}_{N-1}(Q).
\]
The derivative is exact because the right-hand side is affine in \(L\) for \(L\ge1\).

**2. Remove the global-range condition only to first order.** Let \(H(L)\) be the volume of the same cube with only the within-class range constraints. It separates as \(H(L)=\prod_{i=1}^k h_i(L)\), where \(h_i(L)\) is the \(n_i\)-coordinate volume of an interval cube of length \(L\) restricted to range at most \(t_i\). For \(L\ge t_i\), integrating according to the unique minimum coordinate gives
\[
 h_i(L)=n_i\int_0^L\min\{t_i,L-u\}^{n_i-1}\,du
=n_iLt_i^{n_i-1}-(n_i-1)t_i^{n_i}.
\]
For \(n_i=1\), this is simply \(L\), as required. The possible nonuniqueness of a minimum is confined to a measure-zero set for \(n_i\ge2\).

For \(L=1+\varepsilon\) with \(0<\varepsilon\le1\), any point counted by \(H(L)\) but not \(F(L)\) has one coordinate below \(\varepsilon\) and a *different* coordinate above \(1\). A union bound over ordered pairs therefore yields the fully explicit estimate
\[
0\le H(1+\varepsilon)-F(1+\varepsilon)
\le N(N-1)\varepsilon^2(1+\varepsilon)^{N-2}.
\]
At \(L=1\) the total-range restriction is automatic, so \(H(1)=F(1)\). The estimate proves \(F'(1+)=H'(1+)\), with no interchange of unproved limits. Differentiating the product yields
\[
 H'(1)=\left(\prod_i t_i^{n_i-1}\right)
\sum_j n_j\prod_{i\ne j}[n_i-(n_i-1)t_i],
\]
which is the claimed exact volume.

**3. Symmetric-polynomial representation and strict comparison.** For a common \(t\), set \(r=(1-t)/t\). Then \(n_i-(n_i-1)t=t(1+rn_i)\), and the product-rule expression in step 2 is
\[
 V_t(\boldsymbol n)=t^{N-1}\frac{d}{dr}\prod_{i=1}^k(1+rn_i)
 =t^{N-1}\sum_{j=1}^k j r^{j-1}e_j(\boldsymbol n).
\]
Here the derivative is a formal derivative in \(r\), with the outside factor of \(t\) held fixed. Let two sizes be \(a\ge b+2\), and let \(\boldsymbol z\) denote the other \(k-2\) sizes. The transfer to \((a-1,b+1,\boldsymbol z)\) preserves their sum and increases their product by \(a-b-1\). Expanding the elementary symmetric polynomials in these two variables gives
\[
 e_j(a-1,b+1,\boldsymbol z)-e_j(a,b,\boldsymbol z)
 =(a-b-1)e_{j-2}(\boldsymbol z),
\]
with \(e_0(\boldsymbol z)=1\) and out-of-range indices interpreted as zero. Consequently
\[
\boxed{V_t(a-1,b+1,\boldsymbol z)-V_t(a,b,\boldsymbol z)
 =t^{N-1}(a-b-1)\sum_{j=2}^k j r^{j-1}e_{j-2}(\boldsymbol z)>0.}
\]
The \(j=2\) term alone is strictly positive for \(0<t<1\), including \(k=2\). Repeated integer transfers lead to the unique balanced profile; reversing permissible transfers leads to the unique one-large-part profile. This proves the strict Schur order and both extremal classifications. At \(t=1\), only the \(j=1\) term survives, giving \(V_1=N\).

**4. Sharp comparison as dimension grows.** Write \(N=kn\). Direct substitution into the volume formula gives the two exact expressions
\[
V_t(n,\ldots,n)=t^{N-k}N\bigl[t+(1-t)N/k\bigr]^{k-1},
\]
\[
V_t(N-k+1,1,\ldots,1)
=t^{N-k}\bigl[(N-k+1)(k-(k-1)t)+(k-1)t\bigr].
\]
Taking their ratio and sending \(N\to\infty\) with \(k,t\) fixed gives the stated positive coefficient of \(N^{k-1}\). This completes all asserted quantifiers and endpoints.

## Verification
The analytic proof supplies a complete all-dimensional argument. As separate finite evidence, `verify_ultrametric.py` counts integer lattice points in integral dilates of the anchored Lipschitz polytope, extracts exact volume from the top Ehrhart finite difference, and compares against the claimed rational formula. The anchored difference-constraint matrix is a network-incidence matrix, so after scaling rational edge lengths to integers its vertices are integral. The script reports `EXACT_EHRHART_VOLUME_PASS 20 configurations (including 6 nonuniform radii)` and `STRICT_BALANCING_CHECK_PASS 5350 transfers`. All arithmetic is exact rational or integer arithmetic; no floating-point tolerance is used. Execute `python3 verify_ultrametric.py` using the Python standard library. The finite checks are corroboration, not an infinite proof.

## Relationship to prior work
Aliaga and Guirao establish the preserved-extreme-molecule structure of Lipschitz-free spaces and supply the foundational functional-analytic setting [1]. Alexander, Fradelizi, García-Lirola, and Zvavitch investigate general finite-metric Lipschitz-free convex bodies and volume products, including the equilateral benchmark [2]. Their inspected results do not state the heterogeneous within-cluster volume formula or its strict size-majorization law. Cúth and Doucha show that separable ultrametric Lipschitz-free spaces are isomorphic to \(\ell_1\) [3], and Dilworth, Kutzarova, and Ostrovskii give finite-ultrametric isomorphic estimates [4]; those estimates do not determine these coordinate volumes.

Two particularly close results on *the same clustered metric family* have also been compared: one determines the optimal projection constant onto within-cluster fluctuations, and another determines the exact Euclidean Banach–Mazur distance in a balanced four-point case. Their optimized operator/ellipsoid invariants do not imply the entire interior-volume formula by stated identities. A related complete-multipartite volume formula for within-class distances at least one applies on the other side of the equilateral metric; it is not being reused as a claim of novelty at its shared equilateral endpoint. The strict comparison here concerns distances strictly below one, for which the governing global-range constraint changes form.

## Limitations
The metric is two-level and cross-class distances are uniformly one. General hierarchical ultrametrics with three or more genuine distance levels are not classified. Arbitrarily distinct within-class distances are permitted in the exact volume formula, but strict Schur monotonicity is established only with a common within-class distance. The result does not claim affine-invariant primal volume products or characterize isotropic constants. Independent literature may contain an equivalent formula under a different representation; novelty is supported by specific statement comparisons, not guaranteed by unsuccessful searches.

## References
1. R. J. Aliaga and A. J. Guirao, *On the preserved extremal structure of Lipschitz-free spaces*, arXiv:1705.09579 (first public 2017-05-26), https://arxiv.org/abs/1705.09579. Primary MSC 46B20.
2. M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11-24), https://arxiv.org/abs/1911.10642.
3. M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434 (first public 2014-11-10), https://arxiv.org/abs/1411.2434.
4. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public 2018-07-10), https://arxiv.org/abs/1807.03814.
5. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, Arnold Mathematical Journal 3 (2017), 205–218, https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/17-63/index.html.
