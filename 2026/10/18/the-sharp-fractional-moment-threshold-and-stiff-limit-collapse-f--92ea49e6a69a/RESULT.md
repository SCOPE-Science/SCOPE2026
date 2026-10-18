# The sharp fractional-moment threshold and stiff-limit collapse for randomized implicit RK2

## Finding
The randomized implicit two-stage Runge–Kutta schemes S1 and S2 of Bochacik and Przybyłowicz have a complete fractional-moment phase transition on the scalar negative real stability axis. For a fixed stiffness \(a>2\), the sharp transition exponent \(p_*(a)\) is the unique positive solution of
\[
\int_0^1\left|\frac{1-a+au}{1+au}\right|^{p_*(a)}du=1.
\]
Each absolute moment of order \(0<p<p_*(a)\) decays exponentially, each moment of order \(p>p_*(a)\) grows exponentially, and the critical moment is conserved. If \(0<a\le2\), all finite positive moments decay exponentially. Despite these moment instabilities, the trajectory converges exponentially almost surely for every \(a>0\). The sharp stiff limit is
\[
p_*(a)\sim\frac{12}{\pi^2}\frac{\log a}{a}\qquad(a\to\infty).
\]
Thus no fixed positive moment order retains stability uniformly over arbitrarily stiff scalar decays.

## Assumptions and scope
The test equation is \(y'(t)=-\lambda y(t)\) with \(\lambda>0\), fixed step \(h>0\), stiffness \(a=h\lambda\), deterministic nonzero initial value \(Y_0\), independent uniform stage fractions \(U_j\) on \([0,1]\), and exact arithmetic. Both schemes have the scalar multiplier (equation (11) in the cited preprint)
\[
X_a(u)=1-\frac{a}{1+au}=\frac{1-a+au}{1+au},\quad Y_n=Y_0\prod_{j=1}^nX_a(U_j).
\]
For \(p>0\), define \(F_a(p)=\int_0^1|X_a(u)|^pdu\). The moment identity \(\mathbb E|Y_n|^p=|Y_0|^pF_a(p)^n\) is exact. Equalities, critical boundaries, and limits refer to these distributions, not Monte Carlo approximations. Almost-sure exponential convergence means \(\lim_{n\to\infty}n^{-1}\log|Y_n|=\gamma(a)<0\) almost surely, interpreting the null probability of exact zero multipliers conventionally.

## Proof
**Exact moment trichotomy.** If \(0<a\le2\), then \(|X_a(u)|<1\) for almost every \(u\in[0,1]\), so \(0<F_a(p)<1\) for every \(p>0\). For \(a>2\), the set \(0<u<(a-2)/(2a)\) has positive length and satisfies \(|X_a(u)|>1\). Put \(Z_a=\log|X_a(U)|\), whose logarithmic singularity at \(U=1-1/a\) is integrable. A direct antiderivative gives
\[
\gamma(a)=\mathbb EZ_a=\frac{(a-1)\log(a-1)-(a+1)\log(a+1)}a<0\quad(a>1).
\]
Indeed, the difference \((a+1)\log(a+1)-(a-1)\log(a-1)\) is positive at \(a=1\) and has positive derivative \(\log((a+1)/(a-1))\) for every \(a>1\). Write \(K_a(p)=\log\mathbb Ee^{pZ_a}=\log F_a(p)\). For each fixed \(a>2\), \(Z_a\) is nonconstant, bounded above, and has integrable negative logarithmic tail; hence \(K_a\) is strictly convex on \([0,\infty)\), with \(K_a(0)=0\), \(K'_a(0)=\gamma(a)<0\) and \(K_a(p)\to\infty\) as \(p\to\infty\) (positive mass on \(Z_a>0\)). Strict convexity gives exactly one positive zero, with negative values before it and positive values after it. The moment identity proves the stated trichotomy. The strong law applied to the integrable independent \(Z_a(U_j)\) proves almost-sure exponential convergence for \(a>1\); direct pointwise contraction proves the same for \(0<a\le1\).

**Stiff asymptotic.** Set \(b=1/a\) and \(c=1-b\). For \(a\ge2\), write \(Z_a=\log|U-c|-\log(U+b)\). As \(a\to\infty\), it converges almost surely to \(Z_\infty=\log((1-U)/U)\), the centered logistic variable. For every fixed \(0<\delta<1\),
\[
\mathbb Ee^{\delta|Z_a|}\le\int_0^1u^{-\delta}du+(3/2)^\delta\int_0^1|u-c|^{-\delta}du\le\frac{1+2(3/2)^\delta}{1-\delta}.
\]
This is a uniform exponential-integrability bound, justifying convergence of moments and a third-order Taylor remainder for \(K_a\) uniform in large \(a\). Its limiting cumulant generating function for \(|p|<1\) is
\[
\mathbb Ee^{pZ_\infty}=\int_0^1u^{-p}(1-u)^pdu=\Gamma(1-p)\Gamma(1+p)=\frac{\pi p}{\sin(\pi p)}.
\]
Consequently \(\operatorname{Var}(Z_a)\to\pi^2/3\). Also \(\mathbb Ee^{pZ_a}\to\pi p/\sin(\pi p)>1\) for each fixed \(0<p<1\), whereas \(K'_a(0)=\gamma(a)<0\); hence the unique root \(p_*(a)\to0\). The exact log-mean expression gives
\[
\gamma(a)=-\frac{2(\log a+1)}a+O(a^{-3}).
\]
Uniform Taylor expansion at the nonzero root yields
\[
0=\gamma(a)p_*(a)+\tfrac12\operatorname{Var}(Z_a)p_*(a)^2+O(p_*(a)^3).
\]
By the uniform positive quadratic coefficient and strict convexity, this gives \(p_*(a)=-2\gamma(a)/\operatorname{Var}(Z_a)(1+o(1))\), hence the stated constant \(12/\pi^2\).

## Verification
The accompanying standalone `verify.py` independently evaluates the integral with singularity-aware quadrature, locates finite critical exponents by bisection/Brent root solving, compares the moment identity to direct products, and checks the exact logarithmic-mean antiderivative, the classical second-moment formula, and the stiff asymptotic numerically. The infinite-time moment classification and sharp constant rely on the analytic argument above rather than on sampled trajectories. Run `python verify.py` with Python 3, SciPy, and NumPy.

## Relationship to prior work
Bochacik and Przybyłowicz (arXiv:2404.19059v1, first public 29 April 2024) derive the scalar random multiplier, prove asymptotic stability in the left half-plane, and identify the negative-real-axis second-moment stability threshold \(4.03<a<4.04\) at its nontrivial endpoint. These facts, the strong-law method, and the second-moment calculation are not claimed as new. The claim here is the all-positive-order, sharp moment hierarchy and its quantitative stiff-limit collapse; the published second-moment result is its \(p=2\) specialization. The 2025 journal version, DOI 10.1007/s10543-024-01050-9, has a matching abstract but its full text was not accessible for comparison. Classical logistic distributions, strict convexity of cumulant generating functions, and random-product theory are used rather than rediscovered.

## Limitations
Only real negative scalar stiffness, iid uniform stage fractions, fixed timestep, and exact arithmetic are classified. The theorem does not give fractional-moment boundaries for complex stiffness, nonlinear systems, dependent stage sampling, or general stochastic differential equations. The numerical verifier cannot independently certify a universal asymptotic formula; the proof supplies that justification. An undiscovered equivalent moment calculation or a statement in inaccessible journal text remains an originality risk; this is not independently audited.

## References
1. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1 (29 April 2024), Section 3, equations (11), (16), (19), https://arxiv.org/html/2404.19059v1 .
2. T. Bochacik, P. Przybyłowicz, and Ł. Stępień, same title, *BIT Numerical Mathematics* 65 (2025), article 7, DOI:10.1007/s10543-024-01050-9. Full journal text not inspected.
3. Standard beta–gamma reflection identity \(\Gamma(1-p)\Gamma(1+p)=\pi p/\sin(\pi p)\), for \(|p|<1\).
