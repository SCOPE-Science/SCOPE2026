# Subprincipal density asymptotics at an intermittent neutral fixed point

## Finding
For the standard Liverani--Saussol--Vaienti (LSV) interval map with \(0<\gamma<1\), the invariant probability density has a fully explicit finite constant after its neutral singularity, followed by two competing fractional-power corrections. Put \(H=h_\gamma(1/2)\) and \(H_1=h_\gamma'(1/2)\). Then, as \(x\downarrow0\),
\[
\boxed{h_\gamma(x)=\frac{H}{2^{\gamma+1}}x^{-\gamma}+\frac{\gamma+2}{4}H+\frac{H_1}{2^{\gamma+3}}x^{1-\gamma}-\frac{\gamma(\gamma+1)2^\gamma}{12}H x^\gamma+O_\gamma\!\left(x^{\min\{1,2\gamma\}}\right).}
\]
In particular, after subtracting the singular and constant terms, the first displayed correction is universally nonzero at order \(x^\gamma\) for \(0<\gamma<1/2\). The candidate leading exponent changes at \(\gamma=1/2\), where the two powers coincide; in the range \(1/2<\gamma<1\), the actual first nonzero exponent depends on whether \(H_1\) vanishes.

## Assumptions and scope
Fix \(0<\gamma<1\) and set \(b=2^\gamma\). On \((0,1]\), define
\[
T_\gamma(x)=\begin{cases}x(1+b x^\gamma),&0<x\leq1/2,\\2x-1,&1/2<x\leq1.\end{cases}
\]
Its absolutely continuous invariant probability measure has density \(h_\gamma\), normalized by \(\int_0^1h_\gamma(x)\,dx=1\). The density is positive and analytic near the right-hand half-interval; \(h_\gamma(1/2)\) and \(h_\gamma'(1/2)\) mean its analytic values from that interval. Constants implicit in the remainder may depend on fixed \(\gamma\) and its normalized density. No uniformity as \(\gamma\to0\) or \(\gamma\to1\) is asserted.

## Proof
**1. The exact inverse-branch renewal formula.** Let \(f(x)=x(1+b x^\gamma)\), let \(g=f^{-1}\), and define \(x_n=g^n(x)\). For \(0<x<1\), the Frobenius--Perron equation, iterated down the neutral branch, gives
\[
h_\gamma(x)=\sum_{n=0}^{\infty}q(x_n)(g^n)'(x),\qquad q(u)=\frac12h_\gamma\!\left(\frac{1+u}{2}\right).
\]
The sum converges because inverse-branch derivatives decay polynomially; this is also the exact formula in Section 6 of [1]. Near zero, \(q\) is analytic, with \(q_0=q(0)=H/2\), \(q_1=q'(0)=H_1/4\).

**2. Abel coordinate through the first nonlinear term.** Choose a decreasing Abel coordinate \(A\) satisfying \(A(g(x))=A(x)+1\). Its existence, analyticity and differentiable expansion follow from [1], Theorem 2.1 and equation (2.5). Matching the reciprocal, logarithmic and linear-in-\(x^\gamma\) coefficients in \(A(f(x))=A(x)-1\) gives
\[
A(x)=\frac{x^{-\gamma}}{\gamma b}-\frac{\gamma+1}{2}\log x+C_\gamma
 +\frac{(\gamma+1)(2\gamma+1)b}{12\gamma}x^\gamma+O(x^{2\gamma}).
\]
Analytic control of the remainder in the coordinate \(x^\gamma\) permits differentiation. Hence
\[
-A'(x)=\frac{x^{-\gamma-1}}{b}+\frac{\gamma+1}{2x}
-\frac{(\gamma+1)(2\gamma+1)b}{12}x^{\gamma-1}+O(x^{2\gamma-1}).\tag{1}
\]
For a separate algebra check, let \(z=x^\gamma\) and \(\widehat f(z)=z(1+bz)^\gamma\). Substitution of
\(\widehat A(z)=c_{-1}/z+c_\ell\log z+c_1z+\cdots\)
into \(\widehat A(\widehat f(z))-\widehat A(z)+1=0\) gives
\(c_{-1}=1/(\gamma b)\), \(c_\ell=-(\gamma+1)/(2\gamma)\), and
\(c_1=(\gamma+1)(2\gamma+1)b/(12\gamma)\).

**3. A controlled Euler--Maclaurin expansion of the renewal sum.** Let \(t=A(x)\), \(X(s)=A^{-1}(s)\), and \(W(s)=-q(X(s))X'(s)\). Then \(X(t+n)=g^n(x)\), and
\[
h_\gamma(x)=-A'(x)\sum_{n=0}^{\infty}W(t+n),\qquad
\int_t^\infty W(s)\,ds=\int_0^xq(u)\,du.
\]
Since \(X(s)\asymp s^{-1/\gamma}\), its differentiated asymptotics and analyticity of \(q\) imply
\(W^{(j)}(s)=O(s^{-1-1/\gamma-j})\) for \(0\leq j\leq4\). The Euler--Maclaurin formula with the first Bernoulli correction, bounding the next Bernoulli term and integral remainder using these derivative estimates, therefore yields
\[
\sum_{n=0}^{\infty}W(t+n)=\int_t^\infty W(s)\,ds+\tfrac12W(t)-\tfrac1{12}W'(t)+O(t^{-4-1/\gamma}).
\]
As \(-A'(x)\asymp t^{1+1/\gamma}\) and \(t\asymp x^{-\gamma}\), multiplication yields
\[
h_\gamma(x)=-A'(x)\int_0^xq(u)\,du+\frac{q(x)}2
+\frac{q(x)A''(x)}{12A'(x)^2}-\frac{q'(x)}{12A'(x)}+O(x^{3\gamma}).\tag{2}
\]
The sign in front of the \(A''/A'^2\) term is positive: it comes from \(-B_2W'(t)/2!\) with \(B_2=1/6\).

**4. Coefficients and remainder.** Taylor expansion gives
\(\int_0^xq(u)\,du=q_0x+q_1x^2/2+O(x^3)\), and
\[
\frac{A''(x)}{A'(x)^2}=(\gamma+1)b x^\gamma+O(x^{2\gamma}),\qquad
\frac{1}{A'(x)}=O(x^{\gamma+1}).
\]
Inserting these and (1) into (2), the constant is
\((\gamma+1)q_0/2+q_0/2=(\gamma+2)q_0/2\).
The coefficient of \(x^\gamma\) is
\[
-\frac{(\gamma+1)(2\gamma+1)b}{12}q_0
+\frac{(\gamma+1)b}{12}q_0
=-\frac{\gamma(\gamma+1)b}{6}q_0.
\]
The \(x^{1-\gamma}\) coefficient is \(q_1/(2b)\). All remaining terms are bounded by \(O(x^{\min\{1,2\gamma\}})\), since \(0<\gamma<1\) and the next Taylor term in the singular integral is \(O(x^{2-\gamma})\). Substitution of \(q_0=H/2\) and \(q_1=H_1/4\) proves the displayed identity.

For clarity, the resulting limit formulas are
\[
\lim_{x\downarrow0}\!\frac{h_\gamma(x)-Hx^{-\gamma}/2^{\gamma+1}-(\gamma+2)H/4}{x^\gamma}
=-\frac{\gamma(\gamma+1)2^\gamma}{12}H
\quad(0<\gamma<1/2),
\]
\[
\lim_{x\downarrow0}\!\frac{h_{1/2}(x)-Hx^{-1/2}/(2\sqrt2)-5H/8}{x^{1/2}}
=\frac{H_1-H}{8\sqrt2},
\]
\[
\lim_{x\downarrow0}\!\frac{h_\gamma(x)-Hx^{-\gamma}/2^{\gamma+1}-(\gamma+2)H/4}{x^{1-\gamma}}
=\frac{H_1}{2^{\gamma+3}}\quad(1/2<\gamma<1).
\]
These are exact asymptotic limits; the normalization-dependent coefficients scale linearly with any alternative normalization of the invariant density.

## Verification
The reciprocal/logarithmic/linear Abel coefficients can be independently recomputed by expanding \(1+c_{-1}z^{-1}[(1+bz)^{-\gamma}-1]+c_\ell\gamma\log(1+bz)+c_1z[(1+bz)^\gamma-1]\) through order \(z^2\); all coefficients vanish with the values above. Substitution into (2) verifies the Bernoulli coefficient and cancellation algebra. Numerical evaluation of the inverse-branch series at small positive inputs agrees with the predicted finite intercept; this is a finite numerical diagnostic, not the proof of the asymptotic statement. The proof is analytic and needs no external numerical certificate.

## Relationship to prior work
Korepanov--Wei--Wormell [1] provide the analytic Abel coordinate, convergent inverse-branch density representation, and Euler--Maclaurin framework. In Section 6, equations (6.3) and Lemma 6.5, they isolate the singular terms \(M_0x^{-\gamma}\) and \(M_1x^{1-\gamma}\) but retain a bounded and otherwise unspecified remainder \(\mathcal E(x)\). The present formula identifies its finite limiting constant and the first neutral-coordinate power correction, including their competition at \(\gamma=1/2\); it does **not** claim that the already displayed \(M_1\) term is new. Earlier LSV work [2] concerns density stability and linear response, and [3] states the leading density order in the course of a different ergodic-theoretic problem. Thaler's operator-iterate result [4] concerns infinite-measure models, rather than these explicit subprincipal coefficients in the finite-measure range.

## Limitations
The result concerns the standard two-branch LSV family and fixed \(0<\gamma<1\), not all intermittent maps, nor uniform estimates as the parameter approaches the endpoints. No numerical values for \(H\) or \(H_1\) are asserted. For \(\gamma>1/2\) a vanishing derivative would make the indicated \(x^{1-\gamma}\) coefficient zero; the theorem is an expansion, not a proof that this term is always nonzero. The method builds on published Abel-coordinate and Euler--Maclaurin machinery, and an unlocated equivalent coefficient calculation could affect priority.

## References
[1] A. Korepanov, Y. Wei, C. Wormell, *Rigorous and effective numerics for Liverani--Saussol--Vaienti maps*, arXiv:2610.01879v1 (first public 2026-10-01), https://arxiv.org/html/2610.01879v1 .

[2] D. Dragičević, C. González-Tokman, J. Sedro, *Linear response for random and sequential intermittent maps*, Journal of the London Mathematical Society **111** (2025), e70150, https://doi.org/10.1112/jlms.70150 .

[3] C. Bonanno, M. Lenci, *Pomeau--Manneville maps are global--local mixing*, Discrete and Continuous Dynamical Systems **40** (2020), arXiv:1911.02913, https://arxiv.org/abs/1911.02913 .

[4] M. Thaler, *The asymptotics of the Perron--Frobenius operator of a class of interval maps preserving infinite measures*, Studia Mathematica **143** (2000), 103--119, https://doi.org/10.4064/sm-143-2-103-119 .
