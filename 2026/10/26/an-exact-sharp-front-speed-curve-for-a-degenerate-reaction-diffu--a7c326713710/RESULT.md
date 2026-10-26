# An exact sharp-front speed curve for a degenerate reaction–diffusion–advection equation

## Finding

Consider the scalar equation

\[
u_t=\partial_x\!\bigl(D(u)u_x\bigr)-\partial_x h(u)+u(1-u),
\qquad D(u)=u+\beta u^2,\qquad h'(u)=u+k u^2.
\]

For every \(0<\beta<1\), define

\[
\lambda_\beta=\frac{1+\sqrt{9-8\beta}}{4(1-\beta)},
\qquad k_\beta=3\beta\lambda_\beta.
\]

At the parameter pair \((\beta,k)=(\beta,k_\beta)\), the equation has the weak sharp traveling wave

\[
u(x,t)=U_\beta(x-\lambda_\beta t),\qquad
U_\beta(\xi)=\begin{cases}1-e^{\lambda_\beta\xi},&\xi<0,\\0,&\xi\ge0.\end{cases}
\]

More precisely, within the exponential-front family \(U_\lambda(\xi)=\max\{1-e^{\lambda\xi},0\}\), this is the complete parameter classification: a positive-speed wave of this form exists for the stated model with \(\beta>0\), \(k>0\) exactly when \(0<\beta<1\), \(k=k_\beta\), and \(c=\lambda_\beta\).

## Assumptions and scope

The coefficients are fixed, \(\beta>0\), \(k>0\), and the reaction is exactly \(g(u)=u(1-u)\) on \([0,1]\). The conservative flux is \(D(u)u_x-h(u)\), with \(h(u)=u^2/2+ku^3/3\) (the additive constant is immaterial). A weak traveling wave is understood distributionally; the profile is continuous and piecewise smooth, and its flux has no jump at the front. The result classifies only profiles of the displayed exponential form. It does not by itself rule out other sharp profiles or other traveling-wave speeds.

## Proof

Write \(\xi=x-c t\) and \(U=U_\lambda\). On \(\xi<0\), one has \(U'= -\lambda(1-U)\) and

\[
D'(U)(1-U)-D(U)=1+(2\beta-2)U-3\beta U^2.
\]

Consequently

\[
(D(U)U')'=\lambda^2(1-U)\bigl[1+(2\beta-2)U-3\beta U^2\bigr].
\]

The traveling-wave equation is

\[
(D(U)U')'+(c-h'(U))U'+U(1-U)=0.
\]

After division by \(1-U\), its residual on \(0<U<1\) is the polynomial

\[
\lambda^2\bigl[1+(2\beta-2)U-3\beta U^2\bigr]
-\lambda(c-U-kU^2)+U.
\]

For this polynomial to vanish identically, its constant, linear, and quadratic coefficients must vanish. They give, respectively,

\[
c=\lambda,\qquad 2(1-\beta)\lambda^2-\lambda-1=0,
\qquad k=3\beta\lambda.
\]

For \(\beta>0\), the quadratic equation has a positive root exactly when \(0<\beta<1\); its unique positive root is \(\lambda_\beta\) above. The remaining relation forces \(k=k_\beta\). Conversely, these identities make every coefficient of the residual zero, so the profile solves the equation classically on \(\xi<0\). On \(\xi>0\), the profile and all terms vanish. At \(\xi=0\), \(U\to0\), \(D(U)U'\to0\), and \(h(U)\to0\) from the left; these flux limits match the zero right-hand flux. Thus no Dirac mass occurs at the interface, and the profile is a weak traveling wave on the whole line. The limits are \(U(-\infty)=1\) and \(U(0)=0\), as required.

The parameter conditions are necessary as well as sufficient for this ansatz because the residual is a polynomial in \(U\) that must vanish on the entire interval \((0,1)\). This does not establish a classification beyond the ansatz.

## Verification

The included `verify.py` symbolically factors the traveling-wave residual, substitutes the parameter curve, and checks the interface flux conditions. Its output is preserved in `verification_output.txt`. The exact algebraic proof above is the primary verification; the script is a reproducibility check, not a substitute for the proof.

## Relationship to prior work

Sánchez-Garduño and Pérez-Velázquez study the same degenerate model family \(D(u)=u+\beta u^2\), \(h'(u)=u+ku^2\), and \(g(u)=u(1-u)\), and discuss sharp-wave speeds using phase-plane analysis and numerical exploration. The present contribution is the explicit parameter curve and profile obtained by an exact ansatz calculation; it does not claim a new general existence theory. Earlier Abel-equation methods give exact waves under specified integrability relations, but the explicit subclasses inspected do not state this quadratic-convection parameter curve. The limiting boundary \(\beta=0\) is excluded from the claim and is not used to infer the interior result.

## Limitations

The proof establishes the displayed weak wave and the if-and-only-if condition within the exponential-front ansatz. It does not independently prove uniqueness of sharp waves among all possible profiles, exclude other wave speeds, establish stability, or infer convergence of general initial data to this wave. The novelty search was bounded rather than exhaustive; a general exact-wave method may encode equivalent formulas without stating this particular parameter curve.

## References

1. F. Sánchez-Garduño and J. Pérez-Velázquez, “Reactive-Diffusive-Advective Traveling Waves in a Family of Degenerate Nonlinear Equations,” *The Scientific World Journal* (2016), Article 5620839. First published 2016-09-01. DOI: 10.1155/2016/5620839.
2. T. Harko and M. K. Mak, “Exact travelling wave solutions of non-linear reaction-convection-diffusion equations — an Abel equation based approach,” arXiv:1510.08163v1 (2015-10-28).
3. J. A. Sherratt, “On the Form of Smooth-Front Travelling Waves in a Reaction-Diffusion Equation with Degenerate Nonlinear Diffusion,” *Mathematical Modelling of Natural Phenomena* 5 (2010), 64–79. DOI: 10.1051/mmnp/20105505.
