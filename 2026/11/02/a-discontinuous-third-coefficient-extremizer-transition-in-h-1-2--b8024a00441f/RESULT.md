# A discontinuous third-coefficient extremizer transition in \(H^{1/2}\)

## Finding

Let \(f(z)=\sum_{n\geq0}a_n(f)z^n\) be holomorphic in the open unit disc, and put
\[
\mathcal H(t)=\sup_{\|f\|_{H^{1/2}}\leq1}|a_0(f)+t a_3(f)|,\qquad t\geq0.
\]
Let \(x(t)\) be the unique nonnegative solution of
\[
 t=\frac{x}{1-3x^2},\qquad 0\leq x<1/\sqrt3,
\]
with \(x(0)=0\), and define the **binomial profile**
\[
\mathcal E(t)=\frac{1+4t x(t)}{(1+x(t)^2)^2}.
\]
This is exactly the largest value of \(|a_0+t a_3|\) among unit-norm fourth powers of two-term Hardy polynomials \(A+D z^3\).

There exists a mathematically defined *first-departure parameter*
\[
 t_*:=\inf\{t>0:\mathcal H(t)>\mathcal E(t)\}
 \quad\text{with}\quad \boxed{\frac15<t_*<\frac{47}{100}}.
\]
The following claims hold:

1. For \(0\leq t<t_*\), \(\mathcal H(t)=\mathcal E(t)\). In particular, for every \(0<t\leq1/5\), the only maximizing function, up to an overall unimodular multiple, is
   \[
   f_t(z)=\left(\frac{1+x(t)z^3}{\sqrt{1+x(t)^2}}\right)^4.
   \]
2. Every binomial extremizer above remains a **strict local maximizer** of the finite-dimensional coefficient optimization for \(0<t<1/2\), even at parameters where the binomial family is no longer globally optimal.
3. At \(t=t_*\), a binomial maximizing fourth power coexists with a genuinely non-binomial maximizing fourth power \((A+Bz+Cz^2+Dz^3)^4\), where \(A,B,C,D>0\) and \(A^2+B^2+C^2+D^2=1\). The non-binomial branch arrives a positive distance away in the coefficient-vector topology: along maximizers immediately beyond the first-departure parameter, the first-degree root coefficient \(B\) is bounded away from zero.
4. At the special local-instability parameter \(t=1/2\), the exact rational witness
   \[
   g(z)=\frac{3+z+z^2+z^3}{\sqrt{12}},\qquad
   |a_0(g^4)+\tfrac12a_3(g^4)|=\frac{65}{48}>
   \frac{27}{20}=\mathcal E(1/2)
   \]
   shows strict global failure of the binomial branch. Thus the **first global departure precedes the loss of local stability**; the transition is discontinuous in the extremizer shape. This does not determine the numerical value of \(t_*\) or exclude later changes in the full optimizer landscape.

## Assumptions and scope

The ordinary analytic Hardy quasi-norm is normalized by
\[
\|f\|_{H^{1/2}}=
\left(\lim_{r\uparrow1}\int_0^{2\pi}|f(re^{i\theta})|^{1/2}\,\frac{d\theta}{2\pi}\right)^2.
\]
The functional includes only the constant and third Taylor coefficients. The weight \(t\) is real and nonnegative; complex weights reduce to this case by global scaling and a rotation of the disc. Statements about local maxima concern the normalized nonnegative fourth-root coefficient model described below, not a claim of local convexity of the quasi-norm ball. The parameter \(t_*\) is *defined by a strict inequality*, not asserted to have a known closed form.

## Proof

**1. Exact finite-dimensional reduction.** The sharp coefficient functional is bounded and has an extremizer by standard coefficient estimates and normal families. The 2026 outer-extremal theorem of Brevig and Søvik says that every extremizer of a nontrivial bounded linear functional on \(H^p\), \(0<p<1\), is outer. At \(p=1/2\) this permits the analytic fourth root \(f=g^4\), with \(g\in H^2\) and \(\|f\|_{H^{1/2}}=\|g\|_{H^2}^4\). Only the first four Taylor coefficients of \(g\) contribute to \(a_0(f)\) and \(a_3(f)\). Truncating after degree three preserves the functional and cannot increase the \(H^2\) norm. Hence, at the maximum, it suffices to consider \(g=A+Bz+Cz^2+Dz^3\) with \(|A|^2+|B|^2+|C|^2+|D|^2=1\). The exact identity is
\[
 a_0(g^4)=A^4,\qquad a_3(g^4)=4A^3D+12A^2BC+4AB^3.
\]
Taking absolute values coefficientwise gives an upper bound attained by real nonnegative coefficients. Consequently
\[
\mathcal H(t)=\max_{A,B,C,D\geq0\atop A^2+B^2+C^2+D^2=1}
\bigl[A^4+t(4A^3D+12A^2BC+4AB^3)\bigr].\tag{1}
\]
For \(t\geq0\), \(A=0\) gives zero and cannot maximize. Every maximizing nonnegative cubic coefficient vector therefore has \(A>0\).

**2. Binomial branch and the exact small-weight regime.** Restricting (1) to \(B=C=0\), set \(x=D/A\). The objective equals \((1+4tx)/(1+x^2)^2\). Its derivative has the sign of \(t-x-3tx^2\), so there is one global maximum, attained at the specified \(x(t)\); this proves the expression for \(\mathcal E\). In particular, \(\mathcal E(t)>1\) for all \(t>0\).

For general coefficients in (1), set \(s=A^2+D^2\). The binomial terms satisfy
\[
 A^4+4tA^3D\leq s^2\mathcal E(t).
\]
Using \(2BC\leq B^2+C^2\), \(A^2\leq s\), \(A\leq\sqrt{s}\), and \(B\leq1\), the remaining terms obey
\[
12tA^2BC+4tAB^3
\leq t(6s+4\sqrt{s})(B^2+C^2)
=t(6s+4\sqrt{s})(1-s).
\]
For \(0\leq s\leq1\), \(6s+4\sqrt{s}\leq5(1+s)\). If \(0<t\leq1/5\), the latter is at most \(1-s^2\). Therefore (1) is bounded by
\[
s^2\mathcal E(t)+(1-s^2)\leq\mathcal E(t).
\]
As \(\mathcal E(t)>1\), equality for \(t>0\) forces \(s=1\), hence \(B=C=0\). The binomial optimizer is unique in this nonnegative model. In the original complex problem, equality in the triangle inequality forces the two nonzero root coefficients to have the same phase, leaving only an overall unimodular factor. At \(t=0\), the constant unit function is the unique extremizer up to phase.

**3. Strict local stability of the binomial branch.** For \(A,B>0\), optimize first over \(C,D\) with fixed \(A,B\) and fixed \(C^2+D^2\). Cauchy--Schwarz gives the maximizing ratio \(C:D=3B:A\). Writing \(v=B/A\), \(x=\sqrt{C^2+D^2}/A\), the resulting objective is
\[
F_t(v,x)=\frac{1+4t\bigl[x\sqrt{1+9v^2}+v^3\bigr]}{(1+v^2+x^2)^2},\qquad v,x\geq0.\tag{2}
\]
The formula extends continuously to \(v=0\). At the binomial optimizer \(v=0,x=x(t)\), the quadratic coefficient in the transverse variable is
\[
 [v^2]F_t(v,x)=\frac{2(9tx^3+5tx-1)}{(1+x^2)^3}.
\]
Substituting \(t=x/(1-3x^2)\) simplifies this coefficient to
\[
\frac{2(9x^2-1)}{(1-3x^2)(1+x^2)^2}.\tag{3}
\]
For \(0<t<1/2\), \(x(t)<1/3\), so (3) is strictly negative. The tangential second derivative in \(x\) is also strictly negative at the unique binomial maximum, while the mixed second derivative vanishes. Thus \(v=0,x=x(t)\) is a strict local maximizer of (2). The coefficientwise modulus reduction shows the same non-improvement under nearby complex fourth-root perturbations. At \(t=1/2\), (3) vanishes but the coefficient of \(v^3\) in (2), at \(x=1/3\), is strictly positive. This identifies the loss of local stability.

**4. A certified strict competitor already below \(1/2\).** At \(t=47/100\), consider the normalized outer cubic
\[
 g_0(z)=\frac{18+6z+5z^2+5z^3}{\sqrt{410}}.
\]
It has no zero in the closed disc because \(18>6+5+5\). Exact expansion gives
\[
 a_0(g_0^4)+\frac{47}{100}a_3(g_0^4)
 =\frac{1387044}{1050625}
 =\frac{33}{25}+\frac{219}{1050625}>\frac{33}{25}.\tag{4}
\]
On the other hand, the claim \(\mathcal E(47/100)<33/25\) is equivalent to strict positivity on \(x\geq0\) of
\[
 Q(x)=33x^4+66x^2-47x+8.
\]
Indeed, multiply the inequality \((1+(47/25)x)/(1+x^2)^2<33/25\) by the positive denominator. Since \(Q''(x)=396x^2+132\geq132\) for \(x\geq0\), Taylor's integral inequality around \(r=8/25\) gives
\[
Q(x)\geq Q(r)+Q'(r)(x-r)+66(x-r)^2
\geq Q(r)-\frac{Q'(r)^2}{264}
=\frac{4106602319}{64453125000}>0.\tag{5}
\]
Thus \(\mathcal H(47/100)>\mathcal E(47/100)\) with a wholly rational certificate. A simpler independent witness at \(t=1/2\) is stated above.

**5. Existence of a separated coexistence threshold.** By (1), \(\mathcal H\) is the maximum of a continuous function on a fixed compact sphere, so \(\mathcal H\) is continuous; \(\mathcal E\) is continuous by its explicit formula. In addition \(\mathcal H\geq\mathcal E\). Step 2 shows equality through \(1/5\), and step 4 gives strict inequality at \(47/100\). The strictness of the *lower* bound needs one further point: the binomial maximizer at \(t=1/5\) is unique, and by step 3 it is a strict local maximizer uniformly for nearby parameters. If there were parameters tending down to \(1/5\) with \(\mathcal H>\mathcal E\), compactness would force their maximizing root vectors to converge to this unique binomial maximizer, contradicting uniform local strictness. Thus equality persists on a whole interval to the right of \(1/5\). Likewise, by continuity the strict inequality at \(47/100\) persists a little to its left. The first-departure threshold \(t_*\) is therefore well-defined and satisfies the asserted **strict** bounds. Its definition gives \(\mathcal H(t_*)=\mathcal E(t_*)\) and equality for every \(0\leq t<t_*\).

Choose parameters \(t_j\downarrow t_*\) with \(\mathcal H(t_j)>\mathcal E(t_j)\), and select maximizing nonnegative cubic coefficient vectors \((A_j,B_j,C_j,D_j)\). Compactness gives a convergent subsequence to a maximizer at \(t_*\). This limiting vector cannot be binomial: if \(B_j\to0\), then \(C_j\to0\) at the maximum (otherwise its norm is wasted), and the limit must equal the unique binomial vector at \(t_*\). But step 3 gives a *uniform* strict local maximum near this vector for all parameters in a compact interval around \(t_*<1/2\), contradicting \(\mathcal H(t_j)>\mathcal E(t_j)\). Therefore the limiting root has \(B>0\), and the Cauchy--Schwarz maximizing relation in step 3 then gives \(C>0\). It is a non-binomial global extremizer at \(t_*\), coexisting with the binomial one. The uniform local argument supplies the claimed positive separation.

This establishes the discontinuous first departure without assuming that \(t_*\) is the only transition parameter.

## Verification

The independent standard-library program `CHECK.py` recomputes the coefficient convolution, the two rational witnesses, the exact positivity certificate (5), and finite rational tests of the local quadratic formula. A deterministic random stress test checks the claimed small-weight envelope for thousands of positive cubics. The run printed `CHECK_OK 6022`. The analytical inequalities, the outer-extremal theorem, and compactness—not sampling—establish the universal statements. To reproduce the supplementary checks, run `python CHECK.py` with a standard Python 3 interpreter.

## Relationship to prior work

Brevig and Søvik, arXiv:2610.21788 (publicly submitted 15 October 2026), establish that every extremizer for a bounded linear functional on \(H^p\), \(0<p<1\), is outer. Their general structural theorem is a premise here; it does **not** assert the third-coefficient coexistence boundary or the rational bound for \(t_*\). Brevig and Saksman, arXiv:1905.09547, establish single-coefficient constants (not this mixed coefficient boundary). Brevig, Grepstad, and Instanes, arXiv:2011.07790, treat fixed-constant-term coefficient problems, solving the first coefficient and identifying higher-degree regimes as unresolved for \(p<1\). The present support-function transition is not a solution of their entire fixed-constant-term problem.

Other known mixed support profiles at \(H^{1/2}\) involve the constant plus the *second* coefficient, or the first plus the second coefficient; their formulas and optimizer shapes do not imply the first/third coexistence proved here. The critical distinction here is that the third-coefficient convolution introduces the positive cubic term \(4AB^3\), yielding coexistence while the binomial branch is still locally stable. Search-based noncoverage does not constitute a uniqueness certificate; analogous phase-transition analyses could exist elsewhere.

## Limitations

The exact numerical value of \(t_*\), uniqueness of a non-binomial optimizer at coexistence, the number of later transitions, and the complete sharp function \(\mathcal H(t)\) outside the binomial regime are **not proved**. Only the first departure and the listed bounds/coexistence/local-stability conclusions are established. There is no claim of independent audit, computer-assisted proof of the infinite-dimensional statements, or novelty beyond the inspected sources.

## References

- O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788v1 (15 October 2026), https://arxiv.org/abs/2610.21788.
- O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547, https://arxiv.org/abs/1905.09547.
- O. F. Brevig, S. Grepstad, and S. M. Instanes, *F. Wiener's trick and an extremal problem for \(H^p\)*, arXiv:2011.07790, https://arxiv.org/abs/2011.07790, later published in *Computational Methods and Function Theory* (2022).
