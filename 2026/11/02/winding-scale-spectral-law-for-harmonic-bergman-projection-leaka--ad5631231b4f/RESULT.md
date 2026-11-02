# Winding-scale spectral law for harmonic Bergman projection leakage

## Finding
Let \(\alpha>-1\), let \(p=\alpha+1\), and let \(P_\alpha\) be the weighted harmonic Bergman projection on the unit disk. For each positive integer \(k\), multiply a harmonic function by the unimodular angular character \(a_k(re^{i\theta})=e^{ik\theta}\), then project back to harmonic functions. Denote the compressed multiplier by \(T_k=P_\alpha M_{a_k}|_{\mathcal H_\alpha}\) and the **lost-energy operator** by \(D_k=I-T_k^*T_k\). Thus \(\langle D_k f,f\rangle=\|(I-P_\alpha)(a_k f)\|^2\).

Set
\[
 m_s=\frac{\Gamma(p+1)\Gamma(s+1)}{\Gamma(s+p+1)}\qquad(s\ge0).
\]
Every \(D_k\) is a positive trace-class operator. Its complete diagonal, indexed by all integers \(n\), is
\[
 d_{n,k}=1-\frac{m_{(|n|+|n+k|)/2}^{\,2}}{m_{|n|}m_{|n+k|}}\in[0,1),
 \qquad d_{n,k}=d_{-k-n,k}.
\]
Its unique zero eigenvalue occurs for even \(k\), at \(n=-k/2\); otherwise all diagonal entries are strictly positive.

**Sharp winding-scale counting law.** For every fixed \(0<\tau<1\),
\[
 \boxed{\lim_{k\to\infty}\frac1k\#\{n\in\mathbb Z:d_{n,k}\ge\tau\}=
 \frac{(1-\tau)^{1/p}}{\sqrt{1-(1-\tau)^{1/p}}}.}
\]
More generally, for every Lipschitz \(F:[0,1]\to\mathbb R\) with \(F(0)=0\), the operator \(F(D_k)\) is trace class and
\[
\boxed{\begin{aligned}
\lim_{k\to\infty}\frac{\operatorname{Tr} F(D_k)}k={}&
\int_0^1 F\bigl(1-[4x(1-x)]^p\bigr)\,dx\\
&+2\int_0^\infty F\bigl(1-[1-(2x+1)^{-2}]^p\bigr)\,dx.
\end{aligned}}
\]
In particular the sharp trace coefficient is
\[
 \boxed{\lim_{k\to\infty}\frac{\operatorname{Tr}D_k}{k}
 =p\,B(p+1,\tfrac12)
 =\frac{p\sqrt\pi\,\Gamma(p+1)}{\Gamma(p+3/2)}.}
\]
For \(\alpha=0\), this coefficient equals \(4/3\). At this weight, one also has an exact finite-winding trace formula:
\[
\boxed{\operatorname{Tr}D_k=\frac{k^2}{2}\sum_{j=0}^\infty\frac1{(j+k/2+1)^2}
+\frac{k(k-1)(k-2)}{3(k+2)^2}.}
\]
Finally, the angular compression is invertible for each fixed \(k\), with exactly
\[
\boxed{\|T_k\|=1,\qquad \|T_k^{-1}\|=\frac{\sqrt{m_k}}{m_{k/2}}
\sim\frac{k^{p/2}}{2^p\sqrt{\Gamma(p+1)}}.}
\]
Thus no fixed-winding information is lost completely, yet its optimal inverse amplification grows polynomially, and the count of modes losing any fixed positive energy fraction grows linearly.

## Assumptions and scope
The underlying Hilbert space \(\mathcal H_\alpha\) is the space of complex-valued harmonic functions on \(\mathbb D\) square integrable for the probability measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),
\]
where \(dA\) is the unnormalized Euclidean area measure. The ambient \(L^2(d\mu_\alpha)\) inner product is linear in the first variable. The multiplier \(a_k\) is defined arbitrarily at the origin, which has measure zero. The harmonic basis consists of
\[
 e_n(re^{i\theta})=m_{|n|}^{-1/2}\,r^{|n|}e^{in\theta},\qquad n\in\mathbb Z.
\]
All limits are taken with fixed \(\alpha\), fixed threshold \(\tau\) or fixed test function \(F\), and \(k\to\infty\). The spectral count includes multiplicity and ranges over all integer harmonic frequencies. No claims concern multivariable harmonic spaces, nonradial weights, finite-data inverse stability, or rates uniform as \(\alpha\) varies.

## Proof
**1. Exact harmonic projection.** Polar integration and the beta-function identity give \(\|r^se^{in\theta}\|_{L^2(d\mu_\alpha)}^2=m_s\) when \(s=|n|\). The characters \(e^{in\theta}\) are mutually orthogonal. For an integer \(n\), multiplication by \(a_k\) changes its angular frequency to \(n+k\). Orthogonal projection onto the harmonic subspace at that frequency yields
\[
 T_ke_n=w_{n,k}e_{n+k},\qquad
 w_{n,k}=\frac{m_{(|n|+|n+k|)/2}}{\sqrt{m_{|n|}m_{|n+k|}}}.
\]
The constant-frequency space is counted once, not separately as an analytic and coanalytic mode. Hence \(D_ke_n=(1-w_{n,k}^2)e_n\) and the claimed exact formula follows. Since the multiplication is unitary, \(0<w_{n,k}\le1\).

**2. Strict moment curvature and a summable tail.** Put \(h(s)=\log m_s\) for \(s\ge0\). Differentiating the gamma identity gives
\[
 h''(s)=\psi_1(s+1)-\psi_1(s+p+1)
 =\int_0^\infty t e^{-(s+1)t}\frac{1-e^{-pt}}{1-e^{-t}}\,dt.
\]
This integral is strictly positive, strictly decreasing in \(s\), and bounded by \(C_p/(1+s)^2\): the ratio of exponentials is bounded above by \(\max\{1,p\}\). Consequently \(h\) is strictly convex with decreasing curvature. The midpoint convexity gap is zero precisely when \(|n|=|n+k|\), equivalent to even \(k\) and \(n=-k/2\). In the exterior range \(n\ge0\), with \(s=n\), the gap
\[
 G_{n,k}=h(n)+h(n+k)-2h(n+k/2)
\]
is nonnegative and, by the decreasing curvature, nonincreasing in \(n\). For all \(n\ge k\), midpoint Taylor bounds give \(0\le G_{n,k}\le C_p k^2/(n+1)^2\). Since \(d_{n,k}=1-e^{-G_{n,k}}\le G_{n,k}\), the same summable estimate holds for \(d_{n,k}\). Symmetry covers the second exterior tail \(n\le-k\). There are only \(k-1\) strictly interior modes. This proves trace class for each fixed \(k\). It also gives uniformly in \(k\) and \(R\ge1\):
\[
 \frac1k\sum_{n\ge Rk}d_{n,k}\le \frac{C_p'}R,
\]
with the same estimate for the opposite exterior tail, after harmless integer rounding.

**3. Exact worst-case amplification.** The strictly decreasing midpoint gap \(G_{n,k}\) shows that exterior weights are smallest at \(n=0\) and \(n=-k\). Inside the interval \(-k\le n\le0\), write \(n=-j\). Here \(w_{-j,k}^2=m_{k/2}^2/(m_jm_{k-j})\). Convexity of \(h\) makes \(h(j)+h(k-j)\) maximal at \(j=0,k\); thus the same endpoints minimize \(w^2\) among all modes. The weight limit at \(|n|\to\infty\) is \(1\), so the weighted bilateral \(k\)-shift \(T_k\) has norm \(1\), strictly positive minimum weight \(m_{k/2}/\sqrt{m_k}\), and a bounded inverse with the stated exact norm. The gamma-ratio asymptotic
\[
 m_s=\Gamma(p+1)s^{-p}(1+O_p(s^{-1}))
\]
proves the inverse amplification limit.

**4. Limiting profiles.** The same gamma ratio, uniformly when all arguments grow proportionally to \(k\), implies for every fixed \(x>0\), with \(n/k\to x\),
\[
 d_{n,k}\longrightarrow D_{\rm ext}(x)
 :=1-\left[1-(2x+1)^{-2}\right]^p.
\]
For \(n=-j\) with \(j/k\to x\in(0,1)\),
\[
 d_{-j,k}\longrightarrow D_{\rm int}(x)
 :=1-[4x(1-x)]^p.
\]
The two exterior directions have identical profiles by the exact symmetry. For a Lipschitz \(F\) vanishing at zero, \(|F(d)|\le\operatorname{Lip}(F)d\). On each truncated exterior interval and on the interior, boundedness and pointwise convergence give Riemann-sum convergence, including endpoints since those are negligible sets. Step 2 controls both discarded tails uniformly by \(O_{p,F}(R^{-1})\). Sending \(k\to\infty\) and then \(R\to\infty\) proves the asserted trace law. The same argument shows \(F(D_k)\) is trace class.

**5. Counting and trace coefficient.** For fixed \(\tau\in(0,1)\), write \(u=(1-\tau)^{1/p}\in(0,1)\). The interior condition \(D_{\rm int}(x)\ge\tau\) is \(4x(1-x)\le u\), which occupies length \(1-\sqrt{1-u}\) in \([0,1]\). Each exterior region satisfying \(D_{\rm ext}(x)\ge\tau\) has length \((1/\sqrt{1-u}-1)/2\). The combined normalized count therefore equals
\[
 (1-\sqrt{1-u})+(1/\sqrt{1-u}-1)
 =u/\sqrt{1-u}.
\]
The level sets defining these boundaries have Lebesgue measure zero. The uniform spectral-tail estimate of Step 2 ensures that, for fixed \(\tau>0\), no discarded modes can meet the threshold once \(R\) is large enough. Consequently the count converges as claimed. Integrating the threshold count in \(\tau\), equivalently taking \(F(t)=t\) in Step 4, gives
\[
 \int_0^1\frac{(1-\tau)^{1/p}}{\sqrt{1-(1-\tau)^{1/p}}}\,d\tau
 =p\int_0^1 u^p(1-u)^{-1/2}\,du
 =p B(p+1,\tfrac12).
\]
This identity may be justified directly by Tonelli on the limiting profiles, which are nonnegative and integrable, independent of any interchange of finite-rank spectral counts.

**6. Exact unweighted finite-degree identity.** For \(p=1\), \(m_s=(s+1)^{-1}\). When \(n\ge0\),
\[
 d_{n,k}=\frac{k^2}{4(n+k/2+1)^2},
\]
with the same values in the reflected negative exterior tail. On the strictly interior indices \(n=-j\), \(1\le j\le k-1\),
\[
 d_{-j,k}=\frac{(j-k/2)^2}{(k/2+1)^2}.
\]
The elementary square sum is
\[
 \sum_{j=1}^{k-1}(j-k/2)^2=\frac{k(k-1)(k-2)}{12}.
\]
Summing both exterior tails and then the interior modes proves the displayed finite-\(k\) trace formula exactly, including \(k=1,2\). Its large-\(k\) limit agrees with the general beta coefficient \(4/3\).

## Verification
The accompanying `check.py` executes with Python 3 and only its standard library. It checks moment normalization, reflection symmetry, exact endpoint inverse weight, thousands of exact-rational unweighted mode identities, the exact interior sum, and numerical approximations to the winding-scale threshold law for several weights and degrees. The finite checks verify no infinite-dimensional convergence, trace-class assertion, or novelty statement; those conclusions are argued analytically above.

## Relationship to prior work
Dong and Zhou (2013) derive the underlying quasihomogeneous Toeplitz action on the ordinary harmonic Bergman space and study Toeplitz-product algebra. The diagonalization idea is therefore known background, not claimed as new. Hagger, Liu, Taskinen and Virtanen (first posted November 9, 2020) treat weighted harmonic Bergman projections and general boundedness/compactness of Toeplitz operators. The present finding's additional claim is the **complete high-winding lost-energy distribution**, its sharp level-counting function, full Lipschitz trace law, beta trace coefficient, and condition-number growth. These are distinct from fixed-symbol algebraic product criteria and from the boundedness of a single Toeplitz operator. Existing work on ordinary *analytic* Bergman Hankel high-symbol-degree limits involves a different Hilbert space and projection; it does not directly imply the two-sided harmonic mode distribution displayed here.

## Limitations
Only a radial power weight on the disk and integer positive winding are treated. The angular character is discontinuous at one null-set point, and no phase-smooth symbol claim is made. The results are asymptotic for fixed weight; no uniform bounds are claimed near the boundary \(\alpha=-1\), and there is no noise-robust finite-spectral inversion theorem. The mode formula is not itself new, and broader general theorems on high-winding quasihomogeneous harmonic operators could conceivably imply the asymptotic statements. Historical priority is thus provisional pending independent specialist review. The finite checker is supporting evidence rather than a proof of the infinite-dimensional theorem. No independent audit or validation has been performed.

## References
1. R. Hagger, C. Liu, J. Taskinen, and J. A. Virtanen, *Toeplitz operators on the unit ball with locally integrable symbols*, arXiv:2011.04699 (first public version November 9, 2020). https://arxiv.org/abs/2011.04699
2. X.-T. Dong and Z.-H. Zhou, *Product equivalence of quasihomogeneous Toeplitz operators on the harmonic Bergman space*, Studia Math. **219** (2013), 163–175. https://doi.org/10.4064/sm219-2-6
3. X.-T. Dong, Y. Liu, and Z.-H. Zhou, *Quasihomogeneous Toeplitz operators with integrable symbols on the harmonic Bergman space*, 2014. Bibliographic/abstract comparison; complete text not inspected.
