# Unique fastest step and stiff-limit slowdown of a two-step Patankar multistep integrator

## Finding

For the conservative two-species exchange equation and the two-step, order-two Modified Patankar Linear Multistep (MPLM) method with Modified Patankar Euler (MPE) weight denominators, the sharp local asymptotic relaxation factor at equilibrium has **one and only one fastest positive step size**. Although the discretization is positive and conservative at every step size, very large steps make its equilibrium relaxation arbitrarily slow.

Define, for \(h>0\),
\[
a(h)=\frac1{1+4h},\qquad b(h)=-\frac{8h^2}{(1+2h)(1+4h)},\qquad \rho(h)=\frac{-b(h)+\sqrt{b(h)^2+4a(h)}}2.
\]
Then \(\rho(h)\) is the exact local spectral contraction factor. The unique minimizer is the positive root of
\[
32h^4+32h^3-8h^2-8h-1=0,
\]
namely \(h_*=0.536566092485493\ldots\), with \(\rho(h_*)=0.767326987978960\ldots\). For every \(h>0\), \(\rho(h)>1/(1+2h)\), where the right-hand side is the MPE damping factor on the same scalar exchange mode. Moreover,
\[
\rho(h)=1-2h+10h^2+O(h^3)\quad(h\downarrow0),\qquad
\rho(h)=1-\frac1{2h}+\frac1{2h^2}+O(h^{-3})\quad(h\to\infty).
\]

## Assumptions and scope

Take \(y_1,y_2>0\), \(y_1+y_2=1\), and
\[
y'_1=y_2-y_1,\qquad y'_2=y_1-y_2.
\]
The exact imbalance \(u=y_1-1/2\) satisfies \(u'=-2u\). The step size \(h>0\) is constant. Assume two strictly positive normalized starting vectors. Apply the published MPLM formula (Izzo–Messina–Pezzella–Vecchio, equation (2.8)) with the *two-step nonnegative order-two coefficients* \(\alpha_1=0,\alpha_2=1,\beta_1=2,\beta_2=0\), and set the two Patankar denominators by one MPE predictor from the most recent vector (the source's equations (3.19)–(3.20)). All calculations use exact real arithmetic. For nonunit exchange rate \(\lambda>0\), replace \(h\) everywhere by \(\lambda h\).

## Proof

**Coefficient identification.** The source order conditions require \(\alpha_1+\alpha_2=1\), \(\alpha_1+2\alpha_2=\beta_1+\beta_2\), and \(\alpha_1+4\alpha_2=2\beta_1+4\beta_2\). Solving gives \(\beta_2=-\alpha_1/2\). With nonnegative coefficients, \(\alpha_1=\beta_2=0\), \(\alpha_2=1\), \(\beta_1=2\). These are exactly the source's tabulated two-step coefficients; their uniqueness here is elementary prior-input, not a separate novelty claim.

**Exact nonlinear recurrence.** Write \(v=u_{n-1}\), \(w=u_{n-2}\) and \(t=1+2h\). The MPE denominators are
\[
\sigma_1=\frac12+\frac{v}{t},\qquad\sigma_2=\frac12-\frac{v}{t}.
\]
Put \(A=(1/2-v)/\sigma_2\) and \(B=(1/2+v)/\sigma_1\). Direct solution of the two-by-two MPLM linear system gives
\[
u_n=\frac{w+h(A-B)}{1+2h(A+B)}
=\frac{w(t^2-4v^2)-8h^2tv}{t^2-4v^2+4ht(t-4v^2)}.
\]
Equivalently, the first component is \(y_1^n=((1/2+w)+2hA)/(1+2h(A+B))\), and \(y_2^n=1-y_1^n\). Both are strictly between zero and one whenever both preceding states are strictly positive; hence the step is positive and conservative for all \(h>0\).

**Exact spectrum.** Differentiating the two-dimensional recurrence at \((v,w)=(0,0)\) gives \(u_n=b(h)v+a(h)w+O(v^2+w^2)\), with the coefficients above. Its Jacobian \(\begin{psmallmatrix}b&a\\1&0\end{psmallmatrix}\) has characteristic polynomial \(p_h(z)=z^2-bz-a\). The inequalities \(p_h(0)=-a<0\), \(p_h(-1)=4h/((1+2h)(1+4h))>0\), and \(p_h(1)>0\) put the roots in \((-1,0)\) and \((0,1)\). Their sum \(b<0\) makes the negative root larger in modulus. Therefore \(\rho(h)\) is the exact sharp local asymptotic factor and the equilibrium is locally attracting for each finite step size. A real negative dominant eigenvalue yields alternating-sign generic local errors.

**Comparison and asymptotics.** Let \(m=1/(1+2h)\). Direct substitution gives \(p_h(m)=-12h^2/((1+2h)^2(1+4h))<0\), hence \(m<\rho\). Taylor and reciprocal-step expansions of the radical yield the two stated asymptotic formulas. The stiff-step relaxation length in iteration counts, \(-1/\log\rho(h)\), is asymptotic to \(2h\) as \(h\to\infty\), while the MPE factor tends to zero.

**Unique minimizer.** Implicit differentiation of \(\rho^2+b\rho-a=0\) yields
\[
\rho'(h)=\frac{a'(h)-b'(h)\rho(h)}{2\rho(h)+b(h)}.
\]
For \(h>0\), \(b'(h)<0\) and \(2\rho+b>0\). At a stationary point necessarily
\[
\rho=\frac{a'}{b'}=\frac{(1+2h)^2}{4h(1+3h)}=:r(h).
\]
Substituting into \(p_h(r)\) gives
\[
p_h(r(h))=-\frac{32h^4+32h^3-8h^2-8h-1}{16h^2(1+3h)^2}.
\]
The polynomial's descending coefficient sequence has exactly one sign change, and its values at zero and one have opposite signs. Descartes' rule proves precisely one positive root. Because \(r>0\), comparison to the unique positive root \(\rho\) of \(p_h\) shows \(\rho'<0\) before this root and \(\rho'>0\) after it. Thus the root is the unique global minimizer. The numerical values are evaluation results, not substitutes for uniqueness proof.

## Verification

The standalone `verify.py` reconstructs the recurrence symbolically, compares its Jacobian with the displayed coefficients, verifies the polynomial and stationary-point identities and asymptotic leading terms, checks uniqueness of the positive stationary-point root, and performs 392 distinct exact-rational two-component updates against an independently assembled MPE predictor and MPLM linear system. Run `python verify.py` with Python 3 and SymPy installed. Successful execution reports `OK symbolic identities, single positive optimal-step root, 392 exact-rational updates`. No finite set of rational checks proves the universal assertions; those follow from the preceding algebra and sign arguments.

## Relationship to prior work

Izzo, Messina, Pezzella, and Vecchio introduce MPLM methods, their nonnegative two-step coefficients, exact positivity/conservation, the MPE denominator embedding, and convergence at fixed step refinement. These are not claimed to be new. Torlo, Öffner, and Ranocha already demonstrate oscillations and robustness problems for other Patankar-type schemes on exchange models, and Zhu, Huang, and Yang study other Patankar multistep formulas. The present narrowly specified result identifies an exact equilibrium Jacobian and sharp *unique* optimal step, establishes a strict comparison with MPE, and calculates the stiff-step rate degradation for the source's specific two-step MPE-embedded MPLM algorithm.

## Limitations

This is a **local** equilibrium stability theorem for a symmetric two-component linear production-destruction system, not a global convergence theorem from arbitrary positive initial data. The fast/slow comparisons are per time step and do not account for competing computational costs. Alternative denominators, other coefficients, nonsymmetric exchange models, and higher-step MPLM methods are outside scope. Related stability literature could contain a statement equivalent to the displayed specialized formula; publication priority has not been independently established.

## References

1. G. Izzo, E. Messina, M. Pezzella, A. Vecchio, *Modified Patankar Linear Multistep methods for production-destruction systems*, arXiv:2407.12540v1 (first public version July 17, 2024), equations (2.7), (2.8), (3.19), (3.20), and Table 1. https://arxiv.org/html/2407.12540v1
2. D. Torlo, P. Öffner, H. Ranocha, *Issues with Positivity-Preserving Patankar-type Schemes*, arXiv:2108.07347 (2021), introduction and exchange-system stability sections. https://arxiv.org/abs/2108.07347
3. Zhu, Huang, Yang, *Bound-preserving discontinuous Galerkin methods with modified Patankar time integrations for chemical reacting flows*, arXiv:2211.05600 (2022), modified multistep formulation. https://arxiv.org/abs/2211.05600
