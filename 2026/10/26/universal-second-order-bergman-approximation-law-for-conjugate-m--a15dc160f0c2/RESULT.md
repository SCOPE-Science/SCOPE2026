# Universal second-order Bergman approximation law for conjugate monomials

## Finding
Fix an integer \(m\ge3\). In the standard weighted Bergman space \(A^2_\alpha(\mathbb D)\), define the optimal squared best-analytic-approximation constant
\[
C_{\alpha,m}^2=\sup_{0\ne f\in A^2_\alpha}\frac{\inf_{h\in A^2_\alpha}\|\overline z^{\,m}f-h\|_{L^2(d\mu_\alpha)}^2}{\|f\|_{A^2_\alpha}^2}.
\]
As \(\alpha\to+\infty\), with \(m\) fixed, set
\[
K_m=\frac{4m^2(m-1)^{m-1}}{(m+1)^{m+1}},\qquad t_m=\frac{m-1}{2}.
\]
Then
\[
\boxed{C_{\alpha,m}^2=\frac{K_m}{\alpha+1}+O_m(\alpha^{-3}).}
\]
Every norm-attaining monomial index \(n_{\alpha,m}\) satisfies \(n_{\alpha,m}=t_m\alpha+O_m(1)\). More precisely, the exact squared Hankel singular value associated to \(z^n\), denoted \(\lambda_{\alpha,m}(n)\), has the locally uniform two-term profile, for \(n/\alpha\to t\in(0,\infty)\):
\[
\alpha\lambda_{\alpha,m}(n)
=F_m(n/\alpha)+\alpha^{-1}G_m(n/\alpha)+O_m(\alpha^{-2}),
\]
where, for \(t>0\),
\[
F_m(t)=\frac{m^2t^{m-1}}{(1+t)^{m+1}},\qquad
G_m(t)=\frac{m^2t^{m-2}\bigl(2t^2-2(m+1)t+m-1\bigr)}{2(1+t)^{m+2}}.
\]
The peak \(F_m(t_m)=K_m\) is unique and nondegenerate, and \(G_m(t_m)=-K_m\). The cancellation of the order-\(\alpha^{-1}\) correction after multiplying by \(\alpha+1\) holds for **every fixed monomial order \(m\ge3\)**, rather than for one prescribed order.

## Assumptions and scope
Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), \(\alpha>-1\), and \(d\mu_\alpha=(\alpha+1)(1-|z|^2)^\alpha\,dx\,dy/\pi\). Analytic approximation is by the whole closed Hilbert subspace \(A^2_\alpha\), not by a bounded-degree polynomial space. Every asymptotic constant in an \(O_m\) term may depend on the **fixed integer** \(m\), but not on \(\alpha\) or the index being optimized. No uniformity in \(m\to\infty\) is asserted. A maximizing index always exists for fixed \(\alpha\). The result does not assert finite-weight uniqueness.

## Proof
**1. Exact diagonalization.** Let \(M_k=\int_{\mathbb D}|z|^{2k}\,d\mu_\alpha=k!\,\Gamma(\alpha+2)/\Gamma(k+\alpha+2)\). Orthogonality of angular frequencies shows that the anti-holomorphic Hankel residuals \((I-P_\alpha)(\overline z^{\,m}z^n)\) are mutually orthogonal for different \(n\). The corresponding squared diagonal values are
\[
\lambda_{\alpha,m}(n)=\frac{M_{n+m}}{M_n}
-\mathbf 1_{\{n\ge m\}}\frac{M_n}{M_{n-m}}.
\]
Therefore \(C_{\alpha,m}^2=\max_{n\ge0}\lambda_{\alpha,m}(n)\). If \(n\ge m\), write
\[
\lambda_{\alpha,m}(n)=
\prod_{j=1}^{m}\frac{n+j}{n+\alpha+1+j}
-\prod_{j=1}^{m}\frac{n+1-j}{n+\alpha+2-j}.
\]
If \(n<m\), retain only the first product. Each diagonal value is nonnegative because it is a squared norm, and the products show that it tends to zero as \(n\to\infty\) for fixed \(\alpha\).

**2. Uniform two-term expansion.** Put \(A=\alpha\) and \(t=n/A\). On any compact subinterval of \((0,\infty)\), expand the two products as analytic functions of \(A^{-1}\). Writing their first-order logarithmic coefficients as \(p_1\) and \(q_1\), respectively, gives
\[
p_1-q_1=\frac{m^2}{t(1+t)},\qquad
p_1+q_1=m\left(\frac1t-\frac3{1+t}\right).
\]
The difference of the second-order logarithmic coefficients is
\[
-\frac{m^2}{2t^2}+\frac{3m^2}{2(1+t)^2}.
\]
Multiplication by \((t/(1+t))^m\) and re-expansion gives
\[
\lambda_{A,m}(n)=A^{-1}F_m(t)+A^{-2}G_m(t)+O_m(A^{-3}).
\]
The same asymptotic holds after differentiating with respect to the continuous interpolation variable \(t\) on each fixed compact subinterval.

**3. Exclusion of both index tails.** For \(n\ge m\) put \(f(k)=(n+k)/(n+A+1+k)\). Since \(f\) increases and takes values in \([0,1]\) for the indices used, telescoping the difference of products yields, for \(A\ge2m\),
\[
0\le\lambda_{A,m}(n)\le
\frac{m^2(A+1)}{(n+A+2-m)^2}
\left(\frac{n+m}{n+A+2-m}\right)^{m-1}.
\]
Indeed, \(f(j)-f(1-j)=(2j-1)(A+1)/[(n+A+1+j)(n+A+2-j)]\), and \(\sum_{j=1}^m(2j-1)=m^2\). For \(n<m\), the single product is \(O_m(A^{-m})\). Thus \(A\lambda_{A,m}(n)\to0\) whenever \(n/A\to0\) or \(n/A\to\infty\), for fixed \(m\ge3\). In contrast, \(A\lambda_{A,m}(\lfloor At_m\rfloor)\to F_m(t_m)>0\). Hence every maximizing sequence satisfies \(n/A\to t_m\), once uniqueness of the limiting maximum is used.

**4. Sharp localization and correction.** The logarithmic derivative of \(F_m\) is \((m-1)/t-(m+1)/(1+t)\), so \(F_m\) has a unique strict maximum at \(t_m=(m-1)/2\), with \(F_m''(t_m)<0\). Uniform differentiated expansions show that, for a sufficiently large constant \(B_m\), the discrete sequence is strictly increasing for \(n/A\) between a fixed neighborhood's left endpoint and \(t_m-B_m/A\), and strictly decreasing between \(t_m+B_m/A\) and its right endpoint. Combined with global index localization, this gives \(n_{A,m}=At_m+O_m(1)\). Consequently
\[
A C_{A,m}^2=F_m(t_m)+A^{-1}G_m(t_m)+O_m(A^{-2}).
\]
Direct substitution yields \(F_m(t_m)=K_m\) and \(G_m(t_m)=-K_m\), proving
\(C_{A,m}^2=K_m/(A+1)+O_m(A^{-3})\).

## Verification
The accompanying standalone `verify_asymptotic.py` uses exact rational arithmetic. It checks the two Taylor coefficients and cancellation identity for \(m=2,\dots,16\) at six positive rational values of \(t\), and independently cross-checks the diagonal product formula against exact Beta moments for \(m=3,\dots,9\) and three integer weights. It reports 2,175 exact assertions. These finite checks support the algebra but do not prove the uniform limit or index localization, which follow from the displayed bounds and differentiable expansion. Reproduce with `python verify_asymptotic.py` (Python standard library only).

## Relationship to prior work
The weighted Bergman/Hankel literature determines boundedness, Schatten membership and fixed-weight high-index singular-value behavior; see Bourass–El-Fallah–Marrhich–Naqos (2021). Those results address \(n\to\infty\) with the weight fixed, not the double scale \(n\asymp\alpha\to\infty\), where the operator norm is attained. General analytic Bergman semiclassical expansions of Rouby–Sjöstrand–Vũ Ngọc (2018) motivate such asymptotics but do not present these conjugate-monomial sharp constants, peak indices, or the cancellation at order \(\alpha^{-2}\). The present theorem treats all fixed orders \(m\ge3\) and states both the full scaled diagonal profile and the common second-order correction.

## Limitations
The result is asymptotic for fixed integer \(m\), not an exact finite-weight classification or an estimate uniform as \(m\) grows. The method uses the standard radial power weight and the symbol \(\overline z^{\,m}\). The full 1988 Arazy–Fisher–Peetre article was not accessible for a definitive priority comparison; an equivalent older formulation remains possible. The algebraic assertions do not constitute an independent audit.

## References
1. M. Bourass, O. El-Fallah, I. Marrhich and H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743, first posted 2021-02-02, https://arxiv.org/abs/2102.01743.
2. O. Rouby, J. Sjöstrand and S. Vũ Ngọc, *Analytic Bergman operators in the semiclassical limit*, arXiv:1808.00199, first posted 2018-08-01, https://arxiv.org/abs/1808.00199.
3. J. Arazy, S. D. Fisher and J. Peetre, *Hankel operators on weighted Bergman spaces*, American Journal of Mathematics 110 (1988), 989–1053, https://doi.org/10.2307/2374685.
