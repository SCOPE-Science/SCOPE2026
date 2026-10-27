# Polynomial pullback Bergman polynomials and infinite exactness of capacity least squares

## Finding

The monic planar Bergman polynomials on polynomial inverse images obey a family of **exact**, non-asymptotic transfer identities. Fix a monic polynomial \(P\) of degree \(d\ge1\), a bounded Borel set \(E\subset\mathbb C\) of positive area, and an integer \(m\ge0\). Let \(Q_m^E\) be the unique monic degree-\(m\) polynomial orthogonal on \(E\), with respect to the unnormalized area measure \(dA=dx\,dy\), to all polynomials of lower degree. Set \(K=P^{-1}(E)\). The unique monic Bergman polynomial on \(K\) at the indicated degree and its norm are

\[
B^K_{d(m+1)-1}(z)=\frac{P'(z)}d\,Q_m^E(P(z)),
\qquad
\int_K|B^K_{d(m+1)-1}|^2\,dA=\frac1d\int_E|Q_m^E|^2\,dA.
\]

In particular, take the filled polynomial lemniscate
\[
K_{P,R}=\{z\in\mathbb C:|P(z)|\le R\},\qquad R>0.
\]
For every integer \(k\ge1\), write \(n=dk\). Then, **among all monic polynomials of degree \(n\)**,
\[
\boxed{\min_p\int_{K_{P,R}}|p'(z)|^2\,dA=\pi n R^{2k}.}
\]
The complete minimizing family is \(p(z)=P(z)^k+c\) for arbitrary complex constants \(c\). Since \(\operatorname{cap}(K_{P,R})=R^{1/d}\), this is equality in the recently established universal inequality
\[
\operatorname{cap}(K)^n\ge\frac1{\sqrt{\pi n}}\inf_{p\;\mathrm{monic},\,\deg p=n}\|p'\|_{L^2(K,dA)}.
\]
Thus every polynomial lemniscate, including noncircular and disconnected ones, exhibits equality at infinitely many degrees.

## Assumptions and scope

The polynomial \(P\) is monic with arbitrary complex coefficients and degree \(d\ge1\); it need not have simple roots or distinct critical values. The target \(E\) is a bounded Borel set of strictly positive, finite Lebesgue area, not necessarily connected or open. Its inverse image \(K=P^{-1}(E)\) also has finite positive area. Monic orthogonal polynomials are uniquely defined because the area integral of the squared modulus of a nonzero polynomial over a positive-area set is positive. No regularity of \(\partial E\) is required. In the capacity assertion the target is the closed disk of radius \(R>0\), so \(K_{P,R}\) is compact. All complex degrees \(d,m,k,n\) here are integers; the exponent \(m\) begins at zero, and the saturation degrees \(n=dk\) begin at \(d\). The statement makes no classification of exceptional equality at other degrees.

## Proof

**1. Polynomial fiber trace.** Fix \(m\ge0\), set \(n=d(m+1)-1\), and let \(s\) be any polynomial of degree at most \(n-1=d(m+1)-2\). Except at the finite set of critical values of \(P\), the fiber \(P^{-1}(w)\) consists of \(d\) simple roots, and define
\[
T_s(w)=\sum_{P(\zeta)=w}\frac{s(\zeta)}{P'(\zeta)}.
\]
For simple fibers, partial fractions (or the Lagrange interpolation formula) identify \(T_s(w)\) with the coefficient of \(z^{-1}\) in the Laurent expansion at infinity of \(s(z)/(P(z)-w)\). As a formal power series in \(w\), that coefficient equals
\[
\sum_{j\ge0}w^j[z^{-1}]\frac{s(z)}{P(z)^{j+1}}.
\]
If \(j\ge m\), the rational function in the coefficient has order \(O(z^{-2})\) at infinity: indeed \(\deg s\le d(m+1)-2\) and \(P\) is monic of degree \(d\). Its \(z^{-1}\) coefficient vanishes. Thus \(T_s\) is a genuine polynomial of degree at most \(m-1\); for \(m=0\) it is identically zero. This conclusion extends across critical values by polynomial continuation.

**2. Full orthogonality under area pullback.** Let \(Q=Q_m^E\), and set \(B(z)=P'(z)Q(P(z))/d\). This polynomial is monic of degree \(n\), since the leading coefficient of \(P'\) is \(d\). The complex area substitution formula for a proper degree-\(d\) polynomial map (the critical fibers are a measure-zero set) gives
\[
\begin{aligned}
\int_K s(z)\overline{B(z)}\,dA_z
&=\frac1d\int_E\overline{Q(w)}
\sum_{P(\zeta)=w}\frac{s(\zeta)}{P'(\zeta)}\,dA_w\\
&=\frac1d\int_E T_s(w)\overline{Q(w)}\,dA_w=0.
\end{aligned}
\]
The last equality is the defining orthogonality of \(Q_m^E\), because \(\deg T_s<m\). Thus \(B\) is orthogonal on \(K\) to every polynomial of degree less than \(n\), not merely to functions of \(P\). Positivity of the area inner product makes it the unique monic minimizer.

The norm follows from the same substitution, without the fiber trace:
\[
\begin{aligned}
\int_K|B|^2\,dA_z
&=\frac1{d^2}\int_K |P'(z)|^2|Q(P(z))|^2\,dA_z\\
&=\frac1{d^2}\int_E\sum_{P(\zeta)=w}|Q(w)|^2\,dA_w
=\frac1d\int_E|Q(w)|^2\,dA_w.
\end{aligned}
\]
The result holds for arbitrary bounded positive-area Borel targets by measurable area substitution; no boundary integration or transversality assumption appears.

**3. Closed disk targets and sharp least squares.** With \(E=\{|w|\le R\}\), the monic degree-\(k-1\) Bergman polynomial is \(Q_{k-1}(w)=w^{k-1}\), and a direct polar integral yields
\[
\int_E|Q_{k-1}(w)|^2\,dA_w
=\int_0^{2\pi}\int_0^R r^{2k-1}\,dr\,d\theta
=\frac{\pi R^{2k}}k.
\]
Substitute \(m=k-1\) into the transfer identity. For \(n=dk\), the unique monic minimizer of degree \(n-1\) for the area norm on \(K_{P,R}\) is
\[
B_{n-1}(z)=\frac1d P'(z)P(z)^{k-1},
\quad
\|B_{n-1}\|_{L^2(K_{P,R})}^2=\frac{\pi R^{2k}}{dk}=\frac{\pi R^{2k}}n.
\]
The derivative of any monic degree-\(n\) polynomial is \(n\) times a monic degree-\(n-1\) polynomial, and every such latter polynomial arises as a derivative divided by \(n\). Therefore the exact derivative minimum is \(n^2\|B_{n-1}\|^2=\pi nR^{2k}\). Equality forces \(p'=nB_{n-1}=kP'P^{k-1}=(P^k)'\), hence all and only the minimizers are \(P^k+c\).

**4. Capacity.** The polynomial-pullback property for logarithmic capacity gives \(\operatorname{cap}(P^{-1}(\overline{D(0,R)}))=R^{1/d}\) for monic \(P\). Equivalently, the exterior Green potential is \(g(z)=d^{-1}\log(|P(z)|/R)\) wherever \(|P(z)|>R\), vanishes on the lemniscate, and behaves as \(\log|z|-d^{-1}\log R+o(1)\) at infinity. In particular, \(\pi nR^{2k}=\pi n\operatorname{cap}(K_{P,R})^{2n}\), so equality holds in the exact normalization of the Ransford inequality. There is no reliance on an unproved regularity assumption: the Green potential and area-pullback derivation remain valid when critical values lie on the boundary.

## Verification

The companion `verify.py` is executable with SymPy. It checks the monicity and exact fiber-trace degree of \(P'P^m/d\) for five nonsymmetric integer polynomials of degrees one to five and exponents \(0\le m\le3\). For 130 monomial tests it independently compares the trace from polynomial remainders modulo \(P(z)-w\) with the \(z^{-1}\) Laurent coefficient of \(s(z)/(P(z)-w)\); it also checks the derivative identity for additional examples. The recorded result is `CHECK_OK`. These are finite algebraic diagnostics: the general statement for all degrees is established by the preceding symbolic-degree and change-of-variables proof, not by test coverage. The area normalization is ordinary \(dx\,dy\), without a factor \(1/\pi\).

## Relationship to prior work

Ransford [1], Theorems 1.1–1.2, proves the capacity lower bound for all compact sets and its asymptotic sharpness; he explicitly gives disks as equality cases. The inequality itself is prior work. Gustafsson–Putinar–Saff–Stylianopoulos [2], Proposition 7.2, already explicitly exhibits the special exact Bergman subsequence \(z^{d-1}(z^d-1)^m\) on the rotationally symmetric islands \(|z^d-1|<R\); **that special case is not new**. Simanek [3] studies Bergman shifts and ratio asymptotics for general polynomial lemniscate area measures, rather than exact finite-degree transfer identities. The contribution here is a general polynomial-fiber transfer law for arbitrary monic \(P\), all positive-area planar targets, and the resulting universal infinite-degree equality class for the newly established capacity least-squares inequality. A global priority claim beyond inspected sources is not made.

## Limitations

There may be earlier formulations of the polynomial-pullback identity under transfer operators, Bergman projection, or algebraic traces not captured by the literature comparison. Specific exact lemniscate special cases were established long ago. No uniqueness of *all* capacity equality sets, no result at degrees not divisible by \(d\), and no extension to non-polynomial proper maps are claimed. An independent scientific audit has not been performed.

## References

[1] T. Ransford, *A least-squares lower bound for capacity*, arXiv:2610.24702v1 (first public version 17 October 2026), Theorems 1.1–1.2, Lemma 2.1. https://arxiv.org/abs/2610.24702

[2] B. Gustafsson, M. Putinar, E. B. Saff, and N. Stylianopoulos, *Bergman polynomials on an Archipelago: Estimates, Zeros and Shape Reconstruction*, arXiv:0811.1715v1, Section 7 and Proposition 7.2. https://arxiv.org/abs/0811.1715

[3] B. Simanek, *The Bergman Shift Operator on Polynomial Lemniscates*, arXiv:1307.1941, Theorem 1.3 and Corollary 1.7. https://arxiv.org/abs/1307.1941
