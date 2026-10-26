# A sixth-order degeneracy and an exact resonance normal form for the sharp Chang–Marshall functional

## Finding
Let \(D(f)=\sum_{n\geq1}n|a_n|^2\) for \(f(z)=\sum_{n\geq1}a_nz^n\), and let
\[
J(f)=\frac1{2\pi}\int_0^{2\pi}\exp\!\left(|f(e^{it})|^2\right)\,dt.
\]
The sharp Chang–Marshall inequality asserts \(J(f)\leq e\) when \(D(f)\leq1\); equality at energy one occurs on the phase orbit of \(z\). We determine the first nontrivial optimized normal form in the flat second-Fourier-mode direction of this extremum.

For any polynomial \(h(z)=\sum_{n=2}^N h_nz^n\), put \(H=D(h)\) and \(f_t(z)=\sqrt{1-Ht^2}\,z+th(z)\). Then, as real \(t\to0\),
\[
\log J(f_t)=1-t^2\sum_{n=2}^N(n-2)|h_n|^2+O_h(t^3).
\]
Thus the Hessian restricted to the Dirichlet-orthogonal complement of \(z\) has a unique complex flat mode, \(z^2\).

The higher-order behavior along that flat direction has an exact resonance law. For fixed real \(u,v\), and sufficiently small real \(x\), set
\[
 a(x)=\sqrt{1-2x^2-3u^2x^4-4v^2x^6},\qquad
 f_x(z)=a(x)z+xz^2+ux^2z^3+vx^3z^4.
\]
The square root is positive, \(D(f_x)=1\), and
\[
\boxed{\log J(f_x)=1-\frac{(2u-3)^2}{4}x^4
 -\frac{2}{9}(9u^2-27uv+30u+9v^2-6v-5)x^6+O_{u,v}(x^8).}
\]
In particular, cancellation of the fourth-order loss is possible precisely when \(u=3/2\). At that unique value the sixth-order loss is
\[
\boxed{\log J(f_x)=1-\left[\frac1{24}+2\left(v-\frac{31}{12}\right)^2\right]x^6+O_v(x^8).}
\]
The best sixth-order correction within this four-mode real polynomial family is uniquely \(v=31/12\), with optimal local deficit \(e-J(f_x)=ex^6/24+O(x^8)\). This gives a quantitative obstruction to stability: if \(\mathcal O=\{e^{i\theta}z:\theta\in\mathbb R\}\), no constants \(C>0\), \(\varepsilon>0\), and exponent \(p<6\) can make
\[
e-J(f)\geq C\,\operatorname{dist}_{D}(f,\mathcal O)^p\]
hold for every Dirichlet-unit polynomial within Dirichlet distance \(\varepsilon\) of \(\mathcal O\). Moreover, if the displayed inequality holds at exponent \(p=6\) near the orbit, its constant necessarily satisfies \(C\le e/192\). This is a necessary exponent and constant restriction, not a proof of a sixth-power global or local stability inequality.

## Assumptions and scope
Throughout, \(f(0)=0\), the Dirichlet norm is \(\|f\|_D=\sqrt{D(f)}\), and the circle measure is normalized. The Hessian statement is for each fixed polynomial \(h\) with vanishing constant and linear coefficients. The higher-order identity concerns real \(x,u,v\) with \(u,v\) fixed as \(x\to0\), and the principal positive square root; sufficiently small \(x\) guarantees its existence. The uniqueness assertions refer only to the stated real four-mode jet parameters, not to all possible analytic perturbations. The distance is induced by \(\|\cdot\|_D\), and phase rotations of the extremizer are allowed.

## Proof
**Second variation.** Orthogonality of monomials gives \(D(f_t)=1\). On the unit circle, write \(g(z)=\overline z h(z)=\sum_{n\ge2}h_nz^{n-1}\). Then
\[
|f_t(z)|^2=1+2t\operatorname{Re}g(z)+t^2(|h(z)|^2-H)+O_h(t^3).
\]
The circle mean of \(g\) is zero. Expanding the exponential through order two, and using Parseval,
\[
 e^{-1}J(f_t)=1+t^2\bigl(\|h\|_{L^2(\mathbb T)}^2-H+\|g\|_{L^2(\mathbb T)}^2\bigr)+O_h(t^3)
 =1-t^2\sum_{n\ge2}(n-2)|h_n|^2+O_h(t^3).
\]
Taking the logarithm gives the claim. Every term is nonpositive, and the only zero coefficient occurs at \(n=2\).

**Exact constant-term reduction.** For the four-mode path, let \(q_0\) be the constant Fourier coefficient of \(|f_x|^2\) and \(q_j\) its real coefficient of \(z^j\) for \(j=1,2,3\). Direct multiplication yields
\[
\begin{aligned}
q_0&=1-x^2-2u^2x^4-3v^2x^6,\\
q_1&=a(x)x+ux^3+uvx^5,\\
q_2&=a(x)ux^2+vx^4,\\
q_3&=a(x)vx^3.
\end{aligned}
\]
For a Laurent series, denote its constant term by \(\operatorname{CT}\). Then
\[
J(f_x)=\exp(q_0)\operatorname{CT}_z\exp\left(\sum_{j=1}^3q_j(z^j+z^{-j})\right).
\]
The following formal identity is exact through weighted order six when \(q_j=O(x^j)\):
\[
\begin{aligned}
\log\operatorname{CT}_z\exp\left(\sum_{j=1}^3q_j(z^j+z^{-j})\right)
={}&q_1^2+q_2^2+q_3^2+q_1^2q_2-\frac14q_1^4\\
&+2q_1q_2q_3+\frac13q_1^3q_3-\frac23q_1^4q_2+\frac19q_1^6+O(x^8).
\end{aligned}
\]
To verify this identity without numerical approximation, expand the outer exponential as \(\sum_{k=0}^6(\sum_jq_j(z^j+z^{-j}))^k/k!\), retain exponent-zero Laurent monomials, then apply \(\log(1+y)=\sum_{k=1}^{6}(-1)^{k+1}y^k/k\); terms of weighted order greater than six can be discarded. Negative-frequency choices pair with positive-frequency choices, and every retained term has even weighted order. Thus the discarded remainder is \(O(x^8)\).

The Taylor series
\[
a(x)=1-x^2-\left(\frac12+\frac{3u^2}{2}\right)x^4
 -\left(\frac12+\frac{3u^2}{2}+2v^2\right)x^6+O_{u,v}(x^8)
\]
inserted into the constant-term identity and the displayed formulas for \(q_j\), followed by collecting coefficients, gives exactly
\[
\begin{aligned}
[x^2]\log J(f_x)&=0,\\
[x^4]\log J(f_x)&=-\frac{(2u-3)^2}{4},\\
[x^6]\log J(f_x)&=-\frac29(9u^2-27uv+30u+9v^2-6v-5).
\end{aligned}
\]
The remainder is analytic in \(x\) near zero. Moreover \(f_{-x}(z)=-f_x(-z)\), so \(J(f_x)\) is even and the next possible term has order eight.

**Optimize and derive the obstruction.** The fourth-order coefficient vanishes if and only if \(u=3/2\). Substitution yields
\[
[x^6]\log J(f_x)=-\frac1{24}-2\left(v-\frac{31}{12}\right)^2,
\]
which is maximized only at \(v=31/12\). Along this path, exponentiation gives \(e-J(f_x)=ex^6/24+O(x^8)\). Since \(a(x)>0\) near zero,
\[
\operatorname{dist}_D(f_x,\mathcal O)^2=(1-a(x))^2+2x^2+3u^2x^4+4v^2x^6=2x^2+O(x^4).
\]
For \(p<6\), the ratio \((e-J(f_x))/\operatorname{dist}_D(f_x,\mathcal O)^p\) tends to zero, contradicting any proposed uniform positive lower bound. At \(p=6\), the same ratio tends to \(e/(24\cdot 8)=e/192\), proving the necessary upper bound on the sextic stability constant. This proves the assertions without claiming a matching sixth-power inequality.

## Verification
The companion program `verify.py` independently enumerates constant-frequency Laurent monomials using exact symbolic arithmetic, reproduces the second-, fourth-, and sixth-order coefficients, and verifies the unique coefficient choices. It also evaluates the boundary integral by high-precision periodic trapezoidal quadrature, comparing the computed deficits against the asymptotic coefficient. The algebraic argument above is the proof; numerical tests are corroboration only. Run with `python verify.py` (requires `sympy` and `mpmath`).

## Relationship to prior work
Frank and Ivanisvili proved the sharp global bound \(J(f)\le e\) and classified the equality functions in their October 11, 2026 preprint. Their result implies nonnegativity of the deficit but not any sixth-order local coefficient or stability exponent. Andreev and Matheson studied the same functional in 1994, proving local maximality along normalized lines, explicitly separating the \(z^2\) direction; that analysis gives substantial prior context for the flat Hessian mode, but does not contain the optimized four-mode sixth-order normal form above. The present contribution is the exact nested-cancellation calculation and its quantitative exponent obstruction, not the global inequality or the existence of a flat direction itself.

## Limitations
The calculated normal form is for the specific fixed-parameter real four-mode family. It does not assert uniqueness of all near-extremizers, a full Lyapunov–Schmidt classification, or a sixth-power stability lower bound. The second variation is proved for polynomial directions; no infinite-dimensional differentiability is claimed at the critical exponential endpoint. Related historical research on nonlinear Dirichlet functionals was not all accessible in full, so global historical priority is not certified. No independent scientific validation has been performed.

## References
1. R. L. Frank and P. Ivanisvili, *The sharp constant in the Chang–Marshall inequality*, arXiv:2610.15378, first public October 11, 2026; https://arxiv.org/abs/2610.15378.
2. V. V. Andreev and A. Matheson, *Extremal functions and the Chang–Marshall inequality*, Pacific J. Math. **162** (1994), 233–246; https://msp.org/pjm/1994/162-2/pjm-v162-n2-p02-s.pdf.
3. S.-Y. A. Chang and D. E. Marshall, *On a sharp inequality concerning the Dirichlet integral*, Amer. J. Math. **107** (1985), 1015–1033.
4. J. A. Cima and A. Matheson, *A nonlinear functional on the Dirichlet space*, J. Math. Anal. Appl. **191** (1995), 380–401; abstract consulted, full article not inspected.
5. A. L. Matheson and A. R. Pruss, *Properties of extremal functions for some nonlinear functionals on Dirichlet spaces*, Trans. Amer. Math. Soc. **348** (1996); abstract consulted, full article not inspected.
