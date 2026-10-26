# Exact stability on the degenerate two-delay boundary

## Finding

Consider the scalar linear delay equation
\[
x'(t)=-a x(t)-b x(t-\tau)-c x(t-2\tau),\qquad \tau>0.
\]
Assume
\[
b\ne0,\qquad c>0,\qquad c<a<3c,\qquad b^2=8c(a-c).
\tag{1}
\]
Define
\[
\omega=\sqrt{(a-c)(3c-a)} >0,
\]
and let \(\theta\in(0,2\pi)\) be the unique angle satisfying
\[
\cos\theta=\frac{2(c-a)}{b},\qquad
\sin\theta=\frac{2\omega}{b}.
\tag{2}
\]
The two right-hand sides in (2) have squared sum one. For \(n=0,1,2,\ldots\), set
\[
\tau_n=\frac{\theta+2\pi n}{\omega}.
\tag{3}
\]
**Theorem.** The zero solution is asymptotically stable if and only if \(\tau\notin\{\tau_n:n\ge0\}\). At every \(\tau_n\), the characteristic equation has exactly one simple conjugate pair \(\pm i\omega\) on the imaginary axis, and no characteristic root lies in the open right half-plane. The pair is tangent to the imaginary axis from the left, with
\[
\operatorname{Re}\lambda'(\tau_n)=0,\qquad
\operatorname{Re}\lambda''(\tau_n)=
\frac{2\omega^2(a-3c)}{(1+2c\tau_n)^3}<0.
\tag{4}
\]
Hence this degenerate boundary has isolated non-asymptotic delays, but no delay interval of instability.

## Assumptions and scope

All parameters are real, \(\tau>0\), and (1) is imposed. The theorem is exactly the discriminant-zero, positive-double-frequency case of the commensurate two-delay characteristic equation. It concerns linear asymptotic stability of the zero solution only. It does not assert nonlinear Hopf bifurcation, nonlinear stability, or any criterion for the other parameter regimes. The condition (1) implies \(a+b+c>0\) for either sign of \(b\), because
\[
(a+c)^2-b^2=(a-3c)^2>0,\qquad a+c>0.
\]

## Proof

Let
\[
f(\lambda,\tau)=\lambda+a+b e^{-\lambda\tau}+c e^{-2\lambda\tau}.
\tag{5}
\]
Separating the real and imaginary parts of \(f(i\omega,\tau)=0\) and eliminating the phase gives the frequency polynomial
\[
z^2+pz+q=0,\quad
p=2(a^2-c^2)-b^2,\quad
q=(a+b+c)(a-b+c)(a-c)^2,
\tag{6}
\]
where \(z=\omega^2\). Its discriminant is
\[
D=b^2\bigl(b^2+8c(c-a)\bigr).
\tag{7}
\]
The same elimination gives the phase equations
\[
\cos(\omega\tau)=\frac{b(c-a)}{z+a^2-c^2},\qquad
\sin(\omega\tau)=\frac{b\omega}{z+a^2-c^2}
\tag{8}
\]
whenever the denominator is nonzero; on (1) it equals \(b^2/2>0\). To check that (1) is exactly the excluded positive-double-frequency case, start with \(D=0\) and \(p<0\). Then \(b^2=8c(a-c)>0\) and \(p=2(a-c)(a-3c)<0\). The frequency polynomial has double positive root \(z=-p/2\), so \(q=p^2/4>0\). Under the usual initial condition \(a+b+c>0\), this forces \(a-b+c>0\), hence \(a+c>|b|\). The alternative \(c<0,a<c\) would give \(a+c<0\), a contradiction. Therefore \(c>0\) and \(c<a<3c\). Conversely, (1) implies \(a+b+c>0\) because \((a+c)^2-b^2=(a-3c)^2>0\) and \(a+c>0\). Under (1), (6) has the unique positive frequency squared \(z=-p/2=(a-c)(3c-a)\), counted twice algebraically. No other positive imaginary frequency is possible.

For \(\lambda=i\omega\), write \(\zeta=e^{-i\theta}\). Equations (1)–(2) give \(|\zeta|=1\), and direct substitution yields
\[
b\zeta+c \zeta^2=-a-i\omega,\qquad
S:=b\zeta+2c\zeta^2=-2c,
\]
\[
T:=b\zeta+4c\zeta^2=2(a-3c+i\omega).
\tag{9}
\]
Consequently \(f(i\omega,\tau)=0\) precisely when \(\omega\tau=\theta+2\pi n\) for an integer \(n\); positivity of \(\tau\) gives exactly (3). Since \(f_\lambda(i\omega,\tau_n)=1+2c\tau_n>0\), this characteristic root is simple. Its conjugate is simple as well.

By implicit differentiation of \(f(\lambda(\tau),\tau)=0\), using (9), one obtains at \(\tau_n\), with \(F=1+2c\tau_n\),
\[
\lambda'=-\frac{2c\,i\omega}{F},\qquad
\lambda''=-\frac{T\lambda^2}{F^3}+\frac{8c^2\lambda}{F^2}.
\tag{10}
\]
Taking real parts in (10) proves (4). Since \(a<3c\), the quadratic Taylor term in \(\operatorname{Re}\lambda(\tau)\) is strictly negative on both sides of \(\tau_n\). Each pair therefore touches the imaginary axis from the left and does not cross into the right half-plane.

It remains to justify the global root count. At sufficiently small positive \(\tau\), every characteristic root has negative real part: otherwise there would be a sequence \(\tau_j\downarrow0\) and roots \(\lambda_j\) with \(\operatorname{Re}\lambda_j\ge0\). For any such root,
\[
|\lambda_j+a|=|b e^{-\lambda_j\tau_j}+c e^{-2\lambda_j\tau_j}|
\le |b|+|c|,
\]
so the sequence is bounded. A convergent subsequence would limit to the root \(-a-b-c<0\) of the zero-delay characteristic equation, contradicting \(\operatorname{Re}\lambda_j\ge0\). Also, the same bound prevents roots in the closed right half-plane from entering from infinity as \(\tau\) varies. The number of roots in the open right half-plane can therefore change only at an imaginary-axis root. Equations (6)–(7) show that the only such events are (3), and (4) proves that none changes that count. Since the count is initially zero, no root lies in the open right half-plane at any delay. At \(\tau_n\), the simple imaginary pair prevents asymptotic stability; at all other delays there is no imaginary root and every characteristic root lies strictly in the left half-plane. This proves the theorem.

## Verification

The proof is analytic and covers every real parameter tuple satisfying (1) and every \(\tau>0\). The included `verify.py` symbolically checks the implicit-differentiation identities and checks the exact rational/algebraic witness \((a,c,b)=(2,1,\pm2\sqrt2)\), for which \(\omega=1\), \(\theta=3\pi/4\) when \(b>0\), and \(\theta=7\pi/4\) when \(b<0\). The script is a reproducibility check for the algebra; it is not used as a substitute for the infinite-delay root-count argument.

## Relationship to prior work

Hata and Matsunaga derive the same characteristic frequency polynomial and explicitly identify the excluded case \(b^2+8c(c-a)=0\), \(2(a^2-c^2)-b^2<0\) as lacking an explicit stability criterion in their 2022 paper. Their imaginary-root lemmas list the critical delays but the stated stability theorems assume away this case. The present theorem resolves that boundary by computing the second derivative of the characteristic root and proving that the contact is tangential from the stable side. Mahaffy and Busken (2015) analyze the same normalized delay ratio \(R=1/2\) through D-partitioning curves and discuss tangencies; their inspected paper studies the geometry of the full stability region and reports only partial analytic results, rather than this exact necessary-and-sufficient criterion along the parameter ray generated by \((a,b,c)\). Bortz's two-lag paper develops a general root-series approximation, while Li, Ruan, and Wei study a different two-delay linearization. The 2015 geometric treatment is the strongest broader-coverage risk, so this is a focused best-knowledge gap claim, not a guarantee of global historical uniqueness.

## Limitations

No result is asserted when the frequency discriminant is nonzero, when the repeated root of (6) is not positive, or when the zero-delay coefficient condition fails. No nonlinear dynamics, bifurcation of periodic solutions, robustness under coefficient perturbations, or stability of other equations is claimed. The 2015 D-partitioning paper studies the same rational delay ratio and includes tangencies, so an equivalent implication from its global geometry remains the principal historical-priority risk even though the inspected statements do not give the exact line-wise criterion proved here.

## References

1. Y. Hata and H. Matsunaga, “Stability switches in a linear differential equation with two delays,” *Opuscula Mathematica* 42(5) (2022), 673–690. First published online 2022-09-08. DOI: 10.7494/OpMath.2022.42.5.673. Full text: https://www.opuscula.agh.edu.pl/om-vol42iss5art2
2. D. M. Bortz, “Eigenvalues for Two-Lag Linear Delay Differential Equations,” arXiv:1206.6364v1 (first posted 2012-06-27); published as “Characteristic roots for two-lag linear delay differential equations,” *Discrete and Continuous Dynamical Systems—B* 21(8) (2016), 2409–2422. DOI: 10.3934/dcdsb.2016053. Full text: https://arxiv.org/html/1206.6364v1
3. J. M. Mahaffy and T. C. Busken, “Regions of Stability for a Linear Differential Equation with Two Rationally Dependent Delays,” *Discrete and Continuous Dynamical Systems* 35(10) (2015), 4955–4986. DOI: 10.3934/dcds.2015.35.4955. Full text: https://jmahaffy.sdsu.edu/docs/two_delay_DCDS_A_14f.pdf
4. X. Li, S. Ruan, and J. Wei, “Stability and Bifurcation in Delay-Differential Equations with Two Delays,” *Journal of Mathematical Analysis and Applications* 236(2) (1999), 254–280. DOI: 10.1006/jmaa.1999.6418. Full text: https://www.math.miami.edu/~ruan/MyPapers/LiRuanWei-jmaa99.pdf
