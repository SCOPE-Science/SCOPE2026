# Frobenius phases and minimal isogeny fields in a supersingular genus-six family

## Finding

Fix \(\alpha\in\mathbb F_4\) with \(\alpha^2+\alpha+1=0\). For each \(\lambda\in\mathbb F_4\), let \(C_\lambda/\mathbb F_4\) be the smooth projective model of the connected fibre product
\[
y^2+y=x^5,\qquad z^2+z=\alpha x^5+\lambda x^3.
\]
Each curve has genus \(6\). Write \(P_\lambda(T)\) for the numerator of its Hasse–Weil zeta function over \(\mathbb F_4\), and let \(\Phi_m(U)\) denote the \(m\)-th cyclotomic polynomial. The **complete four-parameter zeta classification** is
\[
\begin{aligned}
P_0(T)&=\Phi_4(2T)^6,\\
P_1(T)&=\Phi_4(2T)^2\Phi_{12}(2T)^2,\\
P_\alpha(T)=P_{\alpha^2}(T)&=\Phi_4(2T)^2\Phi_5(2T)^2.
\end{aligned}
\]
In particular, the corresponding orders of rational Jacobian groups are, in the same order, \(15625\), \(4225\), and \(24025\) (with the last value occurring twice).

For \(\lambda,\mu\in\{0,1,\alpha\}\) and positive integer \(r\), the Jacobians \(\operatorname{Jac}(C_\lambda)\) and \(\operatorname{Jac}(C_\mu)\) become isogenous over \(\mathbb F_{4^r}\) **if and only if** \(r\) is divisible by the following respective integer:
\[
\begin{array}{c|ccc}
\{\lambda,\mu\}&\{0,1\}&\{0,\alpha\}&\{1,\alpha\}\\\hline
\text{least }r&3&20&60.
\end{array}
\]
The specializations at \(\alpha\) and \(\alpha^2\) are already isogenous over \(\mathbb F_4\). Consequently all four Jacobians become mutually isogenous over \(\mathbb F_{4^{60}}\), and not over any proper subextension of this form. Although all four Jacobians are geometrically supersingular, their rational isogeny types over \(\mathbb F_4\) separate into three classes. In addition, the nonzero parameters all share the same geometric Ekedahl–Oort type by the cited source, despite exhibiting two different rational isogeny types.

## Assumptions and scope

All statements concern the four specified coefficients over the fixed field \(\mathbb F_4\); they do not classify parameters over larger base fields or assert isomorphisms of curves. An isogeny is over the indicated finite field, not merely over an algebraic closure. The zeta function is normalized as \(Z(C_\lambda,T)=P_\lambda(T)/((1-T)(1-4T))\). The field \(\mathbb F_{4^r}\) is an extension of \(\mathbb F_4\) of degree \(r\).

## Proof

For the three nonzero characters of the deck group \(G\cong(\mathbb Z/2)^2\), the associated quadratic quotient curves have equations
\[
D_1:y^2+y=x^5,\quad
D_{\alpha,\lambda}:z^2+z=\alpha x^5+\lambda x^3,\quad
D_{\alpha^2,\lambda}:w^2+w=\alpha^2x^5+\lambda x^3.
\]
Each right-hand side is a polynomial of degree \(5\) with nonzero leading coefficient. Each quadratic quotient is therefore smooth of genus \(2\), with one rational point above infinity. Their defining Artin–Schreier classes are independent because each nonzero \(\mathbb F_2\)-linear combination has a pole of odd order \(5\) at infinity and hence is not an Artin–Schreier coboundary. This establishes connectedness of the degree-four cover. The conductor–different formula (three nontrivial characters of conductor \(6\)) yields \(2g(C_\lambda)-2=-8+18=10\); thus \(g(C_\lambda)=6\).

For any auxiliary prime \(\ell\ne2\), the \(\ell\)-adic cohomology of \(C_\lambda\) decomposes into the three nontrivial character eigenspaces of \(G\); the trivial eigenspace is the cohomology of \(\mathbb P^1\) and vanishes in degree one. Taking Frobenius determinants gives the factorization
\[
P_\lambda(T)=P_{D_1}(T)P_{D_{\alpha,\lambda}}(T)P_{D_{\alpha^2,\lambda}}(T).
\]
This is the character-space explanation of the standard Jacobian isogeny decomposition for this fibre product.

It remains to compute three genus-two factors. Let \(N_j(\eta,c)\) be the number of points of the smooth projective model of \(v^2+v=\eta x^5+cx^3\) over \(\mathbb F_{4^j}\), for \(j=1,2\). The equation has exactly one point at infinity and, for each affine \(x\), exactly two solutions in \(v\) if and only if
\[
\operatorname{Tr}_{\mathbb F_{4^j}/\mathbb F_2}(\eta x^5+cx^3)=0.
\]
This yields the following **exhaustive finite-field table**. The three column pairs refer to \((\eta,c)=(1,0),(\alpha,\lambda),(\alpha^2,\lambda)\), respectively:

| \(\lambda\) | \((N_1,N_2)\) for \((1,0)\) | for \((\alpha,\lambda)\) | for \((\alpha^2,\lambda)\) |
|---|---|---|---|
| \(0\) | \((5,33)\) | \((5,33)\) | \((5,33)\) |
| \(1\) | \((5,33)\) | \((5,9)\) | \((5,9)\) |
| \(\alpha\) | \((5,33)\) | \((7,21)\) | \((7,21)\) |
| \(\alpha^2\) | \((5,33)\) | \((7,21)\) | \((7,21)\) |

The computations are fully reproducible with the included `verify.py`. For \(\mathbb F_4\), it represents the field as \(\mathbb F_2[u]/(u^2+u+1)\) with \(\alpha=u\). For \(\mathbb F_{16}\), it uses \(\mathbb F_2[v]/(v^4+v+1)\) with \(\alpha=v^2+v\). It enumerates all \(4\) or \(16\) values of \(x\) and computes the absolute trace exactly.

For genus \(2\), put \(s_j=4^j+1-N_j\). The Weil functional equation and the first two Newton identities yield
\[
P_D(T)=1-s_1T+\frac{s_1^2-s_2}{2}T^2-4s_1T^3+16T^4.
\]
The three possible genus-two polynomials in the table are
\[
\begin{aligned}
E(T)&=1+8T^2+16T^4=\Phi_4(2T)^2,\\
B(T)&=1-4T^2+16T^4=\Phi_{12}(2T),\\
D(T)&=1+2T+4T^2+8T^3+16T^4=\Phi_5(2T).
\end{aligned}
\]
They occur as \((E,E,E)\), \((E,B,B)\), and \((E,D,D)\), respectively, giving the claimed zeta functions and rational Jacobian cardinalities by evaluation at \(T=1\).

It remains to establish the **minimality** of the field extensions. Frobenius over \(\mathbb F_4\) has eigenvalues equal to \(2\) times primitive roots of orders \(4\), \(12\), or \(5\), with multiplicities visible from the three products above. Over \(\mathbb F_{4^r}\), the eigenvalues are their \(r\)-th powers. By the Tate isogeny criterion, the Jacobians become isogenous precisely when these powered multisets agree. For the pair \((0,1)\), the primitive twelfth roots power to the same multiset as the primitive fourth roots exactly when \(3\mid r\). For \((0,\alpha)\), no primitive fifth-root eigenvalue can match a fourth-root eigenvalue unless \(5\mid r\); then the fifth roots become \(1\), and equality additionally forces \(4\mid r\). For \((1,\alpha)\), the same fifth-root obstruction forces \(5\mid r\), producing eight eigenvalues equal to \(2^r\) on the \(\alpha\)-side. The twelfth-root part on the other side must then also become \(1\), forcing \(12\mid r\). All these divisibilities are sufficient by direct powering. They yield \(3\), \(20\), and \(60\), respectively.

## Verification

Running `python verify.py` with the six accompanying scientific files produces `VERIFY_OK`. It independently enumerates every input of the genus-two trace formulas over \(\mathbb F_4\) and \(\mathbb F_{16}\), reconstructs the degree-four factors, checks the degree-twelve products and Jacobian orders, and compares all powered Frobenius multisets through extension degree \(120\). The finite enumeration is exhaustive because these fields have exactly \(4\) and \(16\) elements. The proof of all extension-degree assertions comes from cyclotomic orders and Tate's theorem, not extrapolation from the finite checker.

## Relationship to prior work

Almeida Filho, Tafazolian and Vieira (2026), Proposition 10.4 and Proposition 10.6, construct the genus-six fibre-product family and prove supersingularity together with its \(a\)-number and Ekedahl–Oort stratification. Their Section 10.1 also recalls the character-factor Jacobian isogeny decomposition. Those geometric and structural inputs are taken as prior work; the present calculation adds explicit zeta numerators for every \(\mathbb F_4\) parameter and determines the exact least fields of mutual isogeny.

Maisner and Nart (2004), especially Sections 3–4, give a general constructive classification of zeta functions of supersingular genus-two curves in characteristic two, including families containing the three quotients here. Hence the genus-two computational method and the possible individual factor polynomials are not new. The distinguishing assertion is the **coupled arithmetic classification of the four genus-six fibre products**, including the cross-parameter minimal isogeny-extension degrees and their coexistence with constant generic Ekedahl–Oort type. The finite-field data is independently recomputed rather than claimed as an improvement of the general genus-two algorithm.

## Limitations

No classification is claimed for coefficients \(\lambda\) outside \(\mathbb F_4\), for geometric automorphism groups, or for curve isomorphisms. The decomposition is only up to isogeny. The source establishes the Ekedahl–Oort assertions, which are not reproved here. General genus-two zeta-classification techniques could make portions of the finite table straightforward to specialists; the precise coupled minimal-field statement was not located in the inspected sources, but an equivalent unindexed computation cannot be ruled out. There has been no independent mathematical review.

## References

1. G. B. Almeida Filho, S. Tafazolian and S. C. Vieira, *\(a\)-numbers of covers in characteristic two: semigroups and Riemann–Roch spaces*, arXiv:2610.22755v1 (first public version 15 October 2026), especially Sections 10.1, 10.4, 10.5. https://arxiv.org/html/2610.22755
2. D. Maisner and E. Nart, *Zeta functions of supersingular curves of genus 2*, arXiv:math/0408383 (2004), especially Sections 1, 3–4. https://arxiv.org/abs/math/0408383
3. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Inventiones Mathematicae 2 (1966), 134–144 (isogeny criterion).
