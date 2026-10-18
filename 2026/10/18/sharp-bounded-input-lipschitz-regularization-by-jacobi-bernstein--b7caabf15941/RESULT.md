# Sharp bounded-input Lipschitz regularization by Jacobi Bernstein–Durrmeyer operators

## Finding
For every integer \(n\ge2\) and \(a,b>0\), define the Bernstein–Durrmeyer operator \(D_{n,a,b}\) as below. Its **sharp** operator norm from essentially bounded functions (with the essential supremum norm) to the output Lipschitz seminorm is
\[
\mathcal L_{n,a,b}:=\sup_{\|f\|_\infty\le1}\operatorname{Lip}(D_{n,a,b}f)
=2n\max\{V_{n,a,b}(0),V_{n,a,b}(n-1)\},
\]
where, with \(S=n+a+b\),
\[
V_{n,a,b}(k)=\frac{\Gamma(S)}{\Gamma(a+k+1)\Gamma(b+n-k)}
\left(\frac{a+k}{S-1}\right)^{a+k}
\left(\frac{b+n-k-1}{S-1}\right)^{b+n-k-1}.
\]
The sharp pointwise derivative norm is attained **only at \(x=0\) when \(a<b\)**, **only at \(x=1\) when \(a>b\)**, and **at both endpoints only when \(a=b\)**. At the maximizing endpoint, an extremizing input is the sign of the relevant adjacent beta-density difference; consequently the formula is sharp, not just a bound.

For the uniform-weight case \(a=b=1\),
\[
\mathcal L_{n,1,1}=2n\left(\frac{n}{n+1}\right)^n\sim\frac{2n}{e}.
\]
For fixed real \(a,b>0\),
\[
\lim_{n\to\infty}\frac{\mathcal L_{n,a,b}}{n}
=2\max\left\{\frac{a^ae^{-a}}{\Gamma(a+1)},\frac{b^be^{-b}}{\Gamma(b+1)}\right\}.
\]

## Assumptions and scope
Let \(q_{\alpha,\beta}(y)=y^{\alpha-1}(1-y)^{\beta-1}/B(\alpha,\beta)\) for \(0<y<1\) and \(\alpha,\beta>0\), a probability density. For \(x\in[0,1]\) set
\[
(D_{n,a,b}f)(x)=\sum_{j=0}^{n}{n\choose j}x^j(1-x)^{n-j}
\int_0^1 f(y)q_{a+j,b+n-j}(y)\,dy.
\]
The input \(f\) ranges over all real-valued essentially bounded measurable functions on \([0,1]\); the output is a polynomial. Here \(\operatorname{Lip}(g)=\sup_{0\le x<x'\le1}|g(x')-g(x)|/(x'-x)=\max_{x\in[0,1]}|g'(x)|\). All maximizer claims concern the sharp pointwise derivative *functional norm*, not a simultaneous pointwise maximizer for every input. Both endpoints count as legitimate one-sided derivative locations. Noninteger parameters are included. For continuous inputs, the same operator supremum follows by approximating the extremizing sign function in the weighted beta-density \(L^1\) norm.

## Proof
**Step 1 (adjacent-density decomposition).** Put \(p_{m,k}(x)={m\choose k}x^k(1-x)^{m-k}\), \(S=n+a+b\), \(\alpha_k=a+k\), and \(\beta_k=b+n-k\). The derivative identity for the Bernstein basis gives, for every bounded measurable \(f\),
\[
(D_{n,a,b}f)'(x)=n\int_0^1 f(y)\sum_{k=0}^{n-1}p_{n-1,k}(x)
\big(q_{\alpha_k+1,\beta_k-1}(y)-q_{\alpha_k,\beta_k}(y)\big)\,dy.
\]
Both adjacent beta parameters are positive, even when \(k=n-1\), since \(\beta_{n-1}-1=b>0\). Thus duality identifies the norm of evaluation of this derivative with \(n\) times the \(L^1\) norm of its displayed signed kernel.

**Step 2 (exact adjacent total variation).** For arbitrary \(\alpha>0\), \(\beta>1\), the ratio \(q_{\alpha+1,\beta-1}/q_{\alpha,\beta}\) equals \((\beta-1)y/[\alpha(1-y)]\). Therefore the signed difference changes sign exactly once, at \(c=\alpha/(\alpha+\beta-1)\); it is negative on \((0,c)\) and positive on \((c,1)\). Because both densities have integral one, their signed difference has \(L^1\) norm twice its integral over \((c,1)\). By direct beta-density differentiation, that positive integral is
\[
\frac{c^{\alpha}(1-c)^{\beta-1}}{\alpha B(\alpha,\beta)}
=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha+1)\Gamma(\beta)}
\left(\frac{\alpha}{\alpha+\beta-1}\right)^\alpha
\left(\frac{\beta-1}{\alpha+\beta-1}\right)^{\beta-1}.
\]
Substitution \(\alpha=\alpha_k\), \(\beta=\beta_k\) gives \(2V_{n,a,b}(k)\).

**Step 3 (strict endpoint maximization of the adjacent variation).** Write \(t=\alpha_k\) and \(u=\beta_k-1\), so \(t+u=S-1\). Define \(h(t)=t\log t-\log\Gamma(t+1)\) for \(t>0\). Apart from a constant independent of \(k\), \(\log V_{n,a,b}(k)=h(t)+h(S-1-t)\). The derivative \(h''(t)=1/t-\psi_1(t+1)\) is strictly positive: the trigamma series gives
\[
\psi_1(t+1)=\sum_{j=1}^{\infty}\frac1{(t+j)^2}<\int_0^{\infty}\frac{ds}{(t+s)^2}=\frac1t.
\]
Thus the symmetric function \(h(t)+h(S-1-t)\) is strictly convex and strictly increases with distance \(|t-(S-1)/2|\). Among \(t=a,a+1,\ldots,a+n-1\), the maximizing value must occur at an endpoint. Comparing distances shows the maximizer is \(k=0\) when \(a<b\), \(k=n-1\) when \(a>b\), and both endpoints tie when \(a=b\).

**Step 4 (global sharp norm and evaluation locations).** By positivity and partition of unity of the Bernstein weights, for any \(x\in[0,1]\),
\[
\sup_{\|f\|_\infty\le1}|(D_{n,a,b}f)'(x)|
\le 2n\sum_{k=0}^{n-1}p_{n-1,k}(x)V_{n,a,b}(k)
\le2n\max_k V_{n,a,b}(k).
\]
At \(x=0\) only \(k=0\) survives, and at \(x=1\) only \(k=n-1\) survives, so the larger endpoint gives equality; taking \(f\) equal to the sign of that endpoint's signed density realizes the norm. For \(0<x<1\), all the Bernstein weights are positive. If the endpoint variation values differ, or if \(n\ge3\), strict convexity in Step 3 makes the second bound strict. In the sole remaining case \(n=2\) and \(a=b\), the two adjacent signed densities have distinct crossing points \(c_0<c_1\); they have opposite signs on \((c_0,c_1)\), and the first triangle inequality is strict at every interior \(x\). Thus the stated endpoint locations are exhaustive.

**Step 5 (asymptotics).** For \(a=b=1\), the endpoint expression reduces algebraically to \((n/(n+1))^n\). For fixed arbitrary \(a,b>0\), the gamma ratio \(\Gamma(n+a+b)/\Gamma(n+b)\sim n^a\), together with \((1-a/(n+a+b-1))^{n+b-1}\to e^{-a}\), yields \(V_{n,a,b}(0)\to a^ae^{-a}/\Gamma(a+1)\). At the right endpoint reflection yields \(V_{n,a,b}(n-1)\to b^be^{-b}/\Gamma(b+1)\). Taking the larger limit proves the claim.

## Verification
The companion reproducible Python 3 standard-library script `checker.py` carries out exact rational adjacent-beta total variation calculations for integer Jacobi parameters, direct polynomial kernel-derivative integrations, endpoint comparisons, and independent numerical absolute integrals at interior points. It passed **3,202 finite checks**. These calculations are finite consistency tests; strict convexity, endpoint exclusivity, noninteger parameters, and all-degree asymptotics are established analytically above, not inferred from numerical sampling.

## Relationship to prior work
The general Jacobi-weighted Bernstein–Durrmeyer operator and its classical approximation properties are standard (Berdysheva–Jetter, 2010; earlier Jacobi-weighted work of Berens–Xu). Subsequent work on derivatives of positive approximation operators includes Acu–Raşa, 2018, which analyzes differences and derivative-approximation bounds for smooth inputs rather than optimizing the bounded-input Lipschitz regularization seminorm. Known endpoint-to-endpoint oscillation contraction coefficients concern total variation across all distinct input evaluation points and do **not** determine the sharp infinitesimal derivative norm computed here. The present computation uses adjacent beta laws and strict log-convexity to determine the exact coefficient, locations and rough-input extremizers.

## Limitations
The result concerns only this precisely normalized Jacobi Bernstein–Durrmeyer family, the Lebesgue-essential-supremum input norm, and the usual output Lipschitz seminorm; it does not assert the analogous formula for other positive operators or higher derivatives. Full text of some potentially relevant early Jacobi-weighted literature was unavailable; historical priority remains a genuine residual risk. The result has been checked in the self-review only; it has **not** received independent audit or independent bibliographic validation.

## References
1. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598, doi:10.1016/j.jat.2009.11.005 (first public manuscript date identified as 2009-11-22; selected indexed sections examined).
2. H. Berens and Y. Xu, *On Bernstein–Durrmeyer polynomials with Jacobi weights*, 1991 (historical reference; full text not examined).
3. A.-M. Acu and I. Raşa, *Estimates for the differences of positive linear operators and their derivatives*, arXiv:1810.08839 (2018), sections on Durrmeyer operators and derivative bounds examined.
