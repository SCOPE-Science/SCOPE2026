# Strict total positivity of every order for Euclidean-distance Bergman evaluation kernels

## Finding
For real \(t>-1\), let \(K_t(z,w)\) be the weighted Bergman reproducing kernel of the unit disk under weight \((1-|z|)^t\). Put \(H(t,s)=K_t(\sqrt s,\sqrt s)\), \(0\le s<1\). Then, **for every positive integer** \(k\) and every two strictly increasing tuples
\[
-1<t_1<\cdots<t_k,\qquad 0\le s_1<\cdots<s_k<1,
\]
one has the strict all-orders sign law
\[
\boxed{\det[H(t_i,s_j)]_{i,j=1}^{k}>0.}
\]
In particular, if \(t_1<t_2\), the ratio \(H(t_2,s)/H(t_1,s)\) is strictly increasing in \(s\). More generally, for any distinct \(t_1,\ldots,t_k>-1\), every nonzero real linear combination of the \(k\) functions \(s\mapsto H(t_i,s)\) has at most \(k-1\) **distinct** zeros on \([0,1)\).

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and planar area \(dA=dx\,dy\) is **unnormalized**. The norm is
\[
\|f\|_t^2=\int_{\mathbb D}|f(z)|^2(1-|z|)^t\,dA(z),\quad t>-1.
\]
The weight uses genuine Euclidean boundary distance \(1-|z|\), **not** \(1-|z|^2\). The diagonal is sampled at squared radius \(s\). The sign law concerns the mixed matrix of evaluation values at increasing **parameters and radii**, not the Hermitian positive definiteness of the fixed-parameter reproducing kernel. All integers \(k\ge1\) are covered simultaneously. The real zero-count corollary concerns distinct zeros, not zero multiplicities or complex zeros.

## Proof
**1. Monomial expansion.** Rotational orthogonality and the beta integral give
\[
\|z^n\|_t^2=2\pi\int_0^1r^{2n+1}(1-r)^t\,dr
=\frac{2\pi\Gamma(2n+2)\Gamma(t+1)}{\Gamma(t+2n+3)}.
\]
Taylor partial sums are complete by angular Parseval and Tonelli, hence for \(0\le s<1\),
\[
H(t,s)=\sum_{n=0}^{\infty}a_n(t)s^n,\qquad
 a_n(t)=\frac{\Gamma(t+2n+3)}{2\pi\Gamma(t+1)\Gamma(2n+2)}>0.
\]
For any finite collection of \(t\) and \(s<1\), this series converges absolutely: the coefficient grows only polynomially in \(n\).

**2. All coefficient minors are positive.** For any strictly increasing positive integers-with-zero \(n_1<\cdots<n_k\), and strictly increasing \(t_1<\cdots<t_k\), multiplication by positive row and column factors reduces the sign of \(\det[a_{n_j}(t_i)]\) to that of \(\det[\Gamma(t_i+2n_j+3)]\). By the continuous Cauchy–Binet (Andreief) identity and \(\Gamma(v)=\int_0^\infty x^{v-1}e^{-x}dx\),
\[
\det[\Gamma(t_i+2n_j+3)]
=\frac1{k!}\int_{(0,\infty)^k}
\det[x_\ell^{t_i}]_{i,\ell}
\det[x_\ell^{2n_j}]_{\ell,j}
\prod_{\ell=1}^k x_\ell^2e^{-x_\ell}\,dx_\ell.
\]
On \(0<x_1<\cdots<x_k\), both generalized Vandermonde determinants are strictly positive. Indeed, write \(x=e^u\); exponentials \(e^{\lambda_i u}\) with strictly increasing real \(\lambda_i\) have strictly positive Wronskians \(\prod_i e^{\lambda_i u}\prod_{i<j}(\lambda_j-\lambda_i)\). Rolle's theorem inductively bounds the number of zeros of a nontrivial exponential polynomial by \(k-1\); the determinant therefore cannot vanish at increasing nodes, and its sign is fixed by the positive Wronskian as the nodes coalesce. The two determinants change by the same permutation sign, so their product is symmetric and nonnegative on all of \((0,\infty)^k\), and strictly positive on the ordered chamber. Gamma-integrability holds because all \(t_i>-1\) and \(n_i\ge0\). Thus every coefficient minor is strictly positive.

**3. Radial Vandermonde minors.** For \(0\le s_1<\cdots<s_k\) and \(0\le n_1<\cdots<n_k\), the generalized Vandermonde \(\det[s_j^{n_i}]_{i,j}\) is nonnegative by the same Chebyshev argument for positive nodes and continuity at zero. Crucially, for \(n_i=i-1\), it equals the strictly positive ordinary Vandermonde \(\prod_{i<j}(s_j-s_i)\), even when \(s_1=0\) (with \(s^0=1\)).

**4. Cauchy–Binet with a uniform positive term.** For \(N\ge k-1\), define \(H_N(t,s)=\sum_{n=0}^N a_n(t)s^n\). Finite Cauchy–Binet gives
\[
\det[H_N(t_i,s_j)]
=\sum_{0\le n_1<\cdots<n_k\le N}
\det[a_{n_j}(t_i)]\det[s_j^{n_i}].
\]
Every term is nonnegative. The term \(n_i=i-1\) is a fixed, strictly positive number **independent of** \(N\). Let \(N\to\infty\). Entrywise convergence of the series yields convergence of the finite determinant while the same positive lower bound survives. This proves strict positivity for all \(k\).

**5. Consequences.** For \(k=2\), the positive determinant divided by \(H(t_1,s_1)H(t_1,s_2)>0\) implies \(H(t_2,s_2)/H(t_1,s_2)>H(t_2,s_1)/H(t_1,s_1)\). If a nonzero combination of \(k\) parameter profiles vanished at \(k\) distinct radii, the corresponding invertible strict-total-positivity matrix would annihilate its nonzero coefficient vector. Thus it has at most \(k-1\) distinct radial zeros.

## Verification
The accompanying `checker.py` independently computes the gamma-moment series and minors for sample parameter/radius arrays of sizes two through five, including a sample starting at radius zero, and compares the series with the independently derived odd-binomial closed form. The script prints `CHECK_OK` if its specified finite numerical checks pass. These experiments do **not** establish the all-parameter theorem: the infinite-order proof is the generalized Vandermonde and Cauchy–Binet argument above.

## Relationship to prior work
Marinescu and Xing (2026, arXiv:2609.24258v1) study real-analytic **parameter dependence** of Euclidean-distance weighted Bergman kernels for more general smooth pseudoconvex domains. Their general parameter-regularity theorem neither states nor implies positivity of arbitrary ordered mixed evaluation minors. A contemporaneous analysis titled *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* derives the **same** monomial expansion and classifies complex off-diagonal scalar zeros of the kernel. That exact formula and zero classification are prior, not claimed here. Complex zero locations do not impose the strict sign of all mixed \((t,s)\)-minors; the present all-orders sign law, radial ratio monotonicity, and zero-crossing bound are the distinct conclusions. Generalized Vandermonde sign facts and Andreief's identity are classical; the new result is their application to every order of this natural parameter-dependent Bergman evaluation family. Searches for total-positivity, Chebyshev, gamma-moment, and radial-weight formulations identified no published identical parameter–radius determinant theorem in the inspected material.

## Limitations
Only the disk and its actual Euclidean-distance powers are covered. The theorem is **not** a statement that the complex-valued kernel is zero-free, nor that all fixed-basepoint kernel sections form a totally positive family. Parameter and squared radius must be strictly ordered for the strict determinant statement. Classical total-positivity theory might supply an alternative route or more general coverage; unindexed earlier results remain a residual priority risk. No independent mathematical audit has been conducted.

## References
1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1, first public 2026-09-21, https://arxiv.org/abs/2609.24258.
2. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels*, publicly available mathematical note, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-lu-qi-keng-transitions-for-euclidean-boundary-distance-wei--b68d363f03d0.
3. Classical Andreief (continuous Cauchy–Binet) identity and generalized Vandermonde determinant positivity, as used and proved in the argument above.
