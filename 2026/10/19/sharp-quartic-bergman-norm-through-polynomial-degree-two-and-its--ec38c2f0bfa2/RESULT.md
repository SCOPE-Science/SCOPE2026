# Sharp quartic Bergman norm through polynomial degree two and its first truncated-kernel obstruction

## Finding

Let \(\mathcal P_d\) be the complex polynomials of degree at most \(d\) on the unit disk \(\mathbb D\), equipped with the normalized area norms \(\|P\|_{A^p}^p=\pi^{-1}\int_{\mathbb D}|P(z)|^p\,dx\,dy\). Define the sharp finite-degree concentration constant
\[
\mathcal C_d=\max_{0\ne P\in\mathcal P_d}\frac{\|P\|_{A^4}^4}{\|P\|_{A^2}^4}.
\]
Then \(\mathcal C_0=1\), \(\mathcal C_1=8/5\), and
\[
\boxed{\mathcal C_2=2.679775542207615\ldots}
\]
is the **largest real root** of
\[
19070 X^3-110975 X^2+206145 X-122472=0.
\]
The unique positive root \(u_*=0.355702920110215\ldots\) of \(30u^3+35u^2-5u-4=0\) parametrizes **every** nonzero extremizer:
\[
P(z)=\lambda\left(u_*+\sqrt{u_*(3u_*+1)}e^{i\theta}z+e^{2i\theta}z^2\right),
\quad\lambda\in\mathbb C\setminus\{0\},\ \theta\in\mathbb R.
\]
For \(d=1\), the extremizers have coefficient magnitudes \(|a|^2:|b|^2/2=2:3\), and are rotations and multiples of the truncated Bergman evaluation kernel \(K_{1,w}(z)=1+2\overline w z\) with \(|w|=\sqrt3/2\). In contrast, **no** truncated evaluation kernel \(K_{2,w}(z)=1+2\overline w z+3\overline w^{\,2}z^2\), for \(w\in\mathbb D\), maximizes the degree-two quotient. Thus degree two is the first degree at which the kernel-extremizer prescription fails for this natural finite polynomial norm.

## Assumptions and scope

All polynomials have complex coefficients; area measure is normalized to mass one on \(\mathbb D\). The ratio is homogeneous of degree zero in the polynomial and invariant under rotation of its argument. The theorem is only about the finite-dimensional spaces \(\mathcal P_0,\mathcal P_1,\mathcal P_2\). No embedding of unrestricted \(A^2\) into unrestricted \(A^4\) is claimed. The exact constant is the **fourth power** of the operator norm of inclusion \((\mathcal P_2,\|\cdot\|_{A^2})\hookrightarrow (\mathcal P_2,\|\cdot\|_{A^4})\).

## Proof

**1. Exact moments and phase alignment.** For \(P(z)=a+bz+cz^2\), normalized area orthogonality of monomials gives
\[
\|P\|_{A^2}^2=|a|^2+\tfrac12|b|^2+\tfrac13|c|^2,
\]
\[
\|P\|_{A^4}^4=|a|^4+\frac{|2ab|^2}{2}+\frac{|b^2+2ac|^2}{3}+\frac{|2bc|^2}{4}+\frac{|c|^4}{5}.
\]
With \(x=|a|\), \(y=|b|/\sqrt2\), \(h=|c|/\sqrt3\), the squared \(A^2\) norm is \(x^2+y^2+h^2\) and the fourth moment is bounded above by
\[
F=x^4+4x^2y^2+\tfrac43y^4+4x^2h^2+6y^2h^2+\tfrac95h^4+\tfrac{8\sqrt3}{3}xy^2h.
\]
When all three magnitudes are positive, equality occurs precisely when \(2\arg b=\arg a+\arg c\pmod{2\pi}\). Thus optimizing \(F/(x^2+y^2+h^2)^2\) solves the complex-phase problem without loss.

**2. The boundary and reduction to one parameter.** If \(h=0\), write \(v=y^2/(x^2+y^2)\in[0,1]\). The ratio is \(1+2v-5v^2/3\), with maximum \(8/5\) at \(v=3/5\). Hence both \(\mathcal C_1\) and its equality statement follow. Suppose \(h>0\) and set \(u=x/(\sqrt3 h)\ge0\), \(q=y^2/h^2\ge0\). The phase-aligned quotient is
\[
R(u,q)=\frac{A(u)+B(u)q+\tfrac43q^2}{(D(u)+q)^2},
\]
where \(A(u)=9u^4+12u^2+9/5\), \(B(u)=12u^2+8u+6\), \(D(u)=3u^2+1\). Its derivative with respect to \(q\) has the sign of
\[
B D-2A+\left(\tfrac83D-B\right)q.
\]
For \(u\ge0\), the intercept is \(18u^4+24u^3+6u^2+8u+12/5>0\) and the slope equals \(-4u^2-8u-10/3<0\). Therefore there is exactly one maximizer \(q=q_*(u)>0\) on \(q\ge0\), with
\[
q_*(u)=\frac{3(45u^4+60u^3+15u^2+20u+6)}{5(6u^2+12u+5)}.
\]

**3. Global one-variable maximum.** Exact rational simplification yields
\[
M(u):=R(u,q_*(u))=\frac{9(40u^4+80u^3+60u^2+40u+11)}{225u^4+360u^3+150u^2+120u+43}.
\]
Direct differentiation factors as
\[
M'(u)=-\frac{180(u+1)(6u^2+12u+5)(30u^3+35u^2-5u-4)}{(225u^4+360u^3+150u^2+120u+43)^2}.
\]
The cubic factor has exactly one positive root: its coefficients have exactly one sign change, its value at zero is negative, and its leading term is positive. Thus \(M\) strictly increases to \(u_*\) and strictly decreases afterwards. This includes the boundary \(u=0\) and the limit \(u\to\infty\) (the latter equals \(8/5\)). The interior maximum is strict, so all maximizers have all three coefficients nonzero. Reducing the rational expressions modulo the cubic gives
\[
q_*(u_*)=\tfrac32u_*(3u_*+1),\qquad
\mathcal C_2=M(u_*)=\frac{9(190u_*^2+533u_*+922)}{3814}.
\]
Eliminating \(u_*\) produces the displayed cubic polynomial for \(\mathcal C_2\). It is the largest real root: \(M(u_*)\ge M(1/3)=2791/1042>13/5\), while the elimination polynomial is strictly increasing on \([13/5,\infty)\) because its first and second derivatives are positive there. The other two real roots are approximately \(1.30964\) and \(1.82993\), both smaller. Putting \(c=1\), \(a=u_*\) and using \(y^2=h^2q_*(u_*)\) gives \(b^2=u_*(3u_*+1)\). Strict magnitude optimality and the preceding phase condition yield exactly the rotation-scalar family claimed.

**4. First kernel obstruction.** Under \(K_{1,w}=1+2\overline w z\), the ratio of coefficient energies is \(|b|^2/(2|a|^2)=2|w|^2\), so \(|w|^2=3/4\) realizes degree-one equality. At degree two, for any \(w\ne0\), the invariant \(b^2/(ac)\) equals \(4/3\) for \(K_{2,w}\), whereas it equals \(3u_*+1>2\) for every extremizer. At \(w=0\), the kernel is constant and its fourth-power quotient is \(1<\mathcal C_2\). No evaluation kernel is therefore extremal at degree two.

## Verification

`verify.py` uses exact rational polynomial arithmetic to certify the derivative factorization, the unique positive algebraic root, the quotient reduction and elimination polynomial, and the equality ratio. It independently checks the complex coefficient integral by disk quadrature on 400 randomly seeded polynomials and verifies the exact extremal polynomial numerically. The observed checks all pass; numerical sampling alone is not used as a global proof. Run with `python verify.py` using SymPy and the Python standard library. `verification-output.txt` contains the recorded output. All infinite/continuous-domain assertions are covered by the displayed algebraic proof rather than by sampling.

## Relationship to prior work

Bayart, Brevig, Haimi, Ortega-Cerdà and Perfekt (arXiv:1701.06897, first posted 2017-01-24) prove contractive comparisons between **different Bergman weights or dilated arguments**. They do not give the sharp undilated, equal-weight \(A^2\)-to-\(A^4\) constant on quadratic polynomials. Gröchenig and Ortega-Cerdà (arXiv:2005.14176) study polynomial Marcinkiewicz–Zygmund sampling inequalities, not this nonlinear finite-dimensional norm. Kulikov (arXiv:2203.12349) establishes kernel extremality for convex functionals in full weighted Bergman spaces and weighted-exponent embeddings, which does not assert it for fixed-area degree-two truncations. Wang and Zhang (arXiv:2505.12760, Theorem 1.2) give a degree-based Nikolskii bound that is not sharp for the fixed degree-two disk problem. Related fourth-moment results for Hardy Fourier polynomials and degree-two spherical harmonics use different norms and underlying domains; their equality cases do not imply this one.

## Limitations

This is an exact degree-two computation, not a formula at general degree. Kernel failure is proved only for the specified truncated evaluation kernels and the ratio above, not for all other Bergman extremal problems. A mathematically equivalent but differently described historical result could have escaped bibliographic searches; independent novelty/priority confirmation is outstanding. Numerical integration has finite discretization error but is not needed for the proof.

## References

1. F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà, K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:1701.06897 (first version 2017-01-24).
2. K. Gröchenig, J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Bergman and Hardy spaces*, arXiv:2005.14176 (2020).
3. A. Kulikov, *Functionals with extrema at reproducing kernels*, arXiv:2203.12349 (2022).
4. Wang and Zhang, *Hypercontractive inequalities and Nikol’skiĭ-type inequalities on weighted Bergman spaces*, arXiv:2505.12760 (2025).
