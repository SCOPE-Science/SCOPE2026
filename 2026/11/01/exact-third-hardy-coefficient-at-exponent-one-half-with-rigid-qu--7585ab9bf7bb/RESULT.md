# Exact third Hardy coefficient at exponent one-half, with rigid quartic optimizers

## Finding
Let \(H^{1/2}(\mathbb D)\) be the analytic Hardy quasi-Banach space, with \(\|f\|_{H^{1/2}}=\big(\int_0^{2\pi}|f(e^{i\theta})|^{1/2}\,d\theta/(2\pi)\big)^2\). Its sharp third Taylor coefficient constant is
\[
C(3,1/2)=\sup_{\|f\|_{H^{1/2}}=1}|[z^3]f(z)|
=\left\{\frac{729(5t_*+1)^3}{16(3-t_*)(9t_*^2+20t_*+3)^2}\right\}^{1/2}
=2.0889657962257755\ldots,
\]
where \(t_*\) is the unique zero in \((2/3,1)\) of
\[
5t^3+22t^2-27t+4=0.
\]
Moreover, **every** unit-norm extremizer is of the form
\[
f(z)=e^{i\gamma}\,P_*(e^{i\phi}z)^4,\qquad \gamma,\phi\in\mathbb R,
\]
with the explicit real-coefficient outer cubic
\[
P_*(z)=A\left(1+\sqrt{t_*}z+
\frac{3\sqrt{t_*}}{y_*}z^2+\frac{1}{y_*}z^3\right),
\quad y_*:=\frac32\left(\sqrt{t_*}+\sqrt{t_*+4}\right),
\quad A:=\left(1+t_*+\frac{9t_*+1}{y_*^2}\right)^{-1/2}.
\]
In particular, up to scalar phase and disk rotation, the extremizer is unique, and its cubic root has no zeros in the closed disk.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \([z^3]f\) denotes the coefficient of \(z^3\) in the Taylor expansion at zero. The usual radial-limit Hardy quasi-norm is used. The theorem concerns only the third coefficient and the exponent \(p=1/2\); it does not determine arbitrary coefficient orders or Hardy exponents.

The existence and outer-polynomial representation of coefficient extremizers are invoked from Brevig and Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, Corollary 3 (arXiv:2610.21788v1, October 15, 2026). That corollary states: each norm-one extremizer of the \(k\)-th coefficient functional at \(0<p<1\) equals an outer polynomial of degree \(k\), raised to the power \(2/p\). Here \(k=3\) and \(2/p=4\).

## Proof
**Reduction and norm.** By the cited corollary, any extremizer is \(f=P^4\) for an outer cubic \(P(z)=a+bz+cz^2+dz^3\). Conversely, every cubic produces an admissible \(H^{1/2}\) function. Parseval gives the exact normalization
\[
\|P^4\|_{H^{1/2}}=\left(\int_{\mathbb T}|P|^2\right)^2
=(|a|^2+|b|^2+|c|^2+|d|^2)^2.
\]
The coefficient formula is
\[
[z^3]P^4=4a^3d+12a^2bc+4ab^3.
\]
Thus the sharp constant is at most the maximum on the real nonnegative unit sphere of
\[
Q(a,b,c,d)=4a^3d+12a^2bc+4ab^3,
\qquad a^2+b^2+c^2+d^2=1.
\]
Equality in the complex triangle inequality is attainable by the positive coefficients, so this real maximum is exactly the desired constant once its positive maximizer is checked to be outer.

**An interior maximizer.** The nonnegative sphere is compact. If \(a=0\), then \(Q=0\). If \(b=0\), then \(Q=4a^3d\le3\sqrt3/4\), because \(a^2+d^2\le1\). But \((a,b,c,d)=(3,3,2,1)/\sqrt{23}\) gives \(Q=1080/529>2\). Hence every global maximizer has \(a,b>0\). If \(c=0\), the one-sided derivative \(\partial Q/\partial c=12a^2b>0\); if \(d=0\), the one-sided derivative \(\partial Q/\partial d=4a^3>0\). A small positive perturbation in the vanishing coordinate followed by normalization increases \(Q\), since the normalization changes only at quadratic order. Therefore every maximizer has all four coordinates strictly positive.

**Stationarity and uniqueness.** Put \(q=Q(a,b,c,d)\). Degree-four homogeneity shows that the Lagrange equations at an interior maximizing unit vector are \(\nabla Q=4q(a,b,c,d)\). Explicitly,
\[
\begin{aligned}
3a^2d+6abc+b^3&=qa,\\
3a^2c+3ab^2&=qb,\\
3a^2b&=qc,\\
a^3&=qd.
\end{aligned}
\]
Set \(x=b/a>0\) and \(y=q/a^2>0\). The last two equations give \(c/a=3x/y\) and \(d/a=1/y\). Substituting into the first two gives
\[
y^2-3xy-9=0,\qquad y^2-x^3y-3-18x^2=0,
\]
so subtraction yields
\[
xy(3-x^2)=6(3x^2-1).
\]
Positivity forces \(1/3<x^2<3\). Set \(t=x^2\). Replacing \(xy\) by \(6(3t-1)/(3-t)\) in the first stationarity equation, and clearing the positive denominator \((3-t)^2\), gives
\[
9\{5t^3+22t^2-27t+4\}=0.
\]
Call the bracket \(F(t)\). Directly \(F(1/3)=-64/27<0\), \(F(2/3)=-74/27<0\), \(F(1)=4>0\), and \(F''(t)=30t+44>0\) for \(t>0\). Strict convexity and the negativity of the endpoint values exclude zeros on \([1/3,2/3]\). On \([2/3,\infty)\), \(F'(2/3)=9>0\) and \(F'\) is increasing; hence \(F\) has exactly one zero on \((2/3,1)\) and none on \([1,3)\). Consequently there is **exactly one** positive critical unit vector, with \(x=\sqrt{t_*}\), \(y=(3/2)(x+\sqrt{x^2+4})\), and the coefficients stated above. Since a global maximum must exist and be positive critical, this vector is the unique maximizer.

**Sharp value.** Write \(D=1+t_*+(9t_*+1)/y_*^2\). Normalization gives \(a^2=1/D\) and \(q=y_*/D\). By the stationarity identity,
\[
y_*^2=\frac{9(5t_*+1)}{3-t_*},\qquad
D=\frac{4(9t_*^2+20t_*+3)}{9(5t_*+1)},
\]
from which the displayed exact formula for \(C(3,1/2)=q\) follows.

**Outer property and all complex equality cases.** Since \(t_*\in(2/3,1)\), we have \(1>x>3x/y>1/y>0\): \(y>3\) is immediate from its formula, and \(3x>1\) follows from \(x>\sqrt{2/3}\). The coefficients of \(P_*\) are therefore strictly decreasing. The Eneström–Kakeya theorem, applied to the reversed polynomial, implies that every zero of \(P_*\) has modulus greater than one, so \(P_*\) is outer and is admissible. For an arbitrary complex-coefficient optimizer, the coefficient moduli must equal the unique positive maximizing vector. All three nonzero summands of \([z^3]P^4\) must then have identical argument, which forces the coefficient arguments \(\vartheta_j\equiv\vartheta_0+j\phi\pmod{2\pi}\) for \(j=0,1,2,3\). Thus \(P(z)=e^{i\vartheta_0}P_*(e^{i\phi}z)\), proving precisely the claimed extremizer family. This also establishes that no other extremizers exist. \(\square\)

## Verification
All numerical values are optional reproducibility aids, not substitutes for the proof. The standalone `checker.py` evaluates the defining algebraic equation, checks the exact elimination identity using integer-polynomial arithmetic, brackets its unique admissible root, and checks the numerical coefficient formula and the computed normalized quartic. It requires only Python's standard library and may be run as `python3 checker.py`. The analytical proof provides the global and infinite-dimensional justification.

For orientation, \(t_*=0.8492633853612398\ldots\), \(y_*=4.685488773346371\ldots\), and the normalized coefficient vector is approximately \((0.667710512306,0.615331876880,0.393981443546,0.142506053179)\).

## Relationship to prior work
Brevig and Saksman (arXiv:1905.09547, released May 23, 2019) determine the exact \(C(2,p)\) for all \(0<p<1\) and \(C(3,2/3)\), with equality cases. The exponent \(p=1/2\) at coefficient order three is not among those explicit results. Brevig and Søvik (arXiv:2610.21788v1, released October 15, 2026) prove the key outer-extremizer theorem and structural representation, but their stated results do not provide the maximization, algebraic constant, or rigid optimizer described here. Brevig, Grepstad, and Instanes (2022) address a different constrained Hardy extremal problem (fixing the constant coefficient) and do not state this exact third-coefficient value. These distinctions concern implications of the underlying theorems, not solely titles or parameter wording.

## Limitations
The exact constant and uniqueness depend on the cited, independently published existence/outer-polynomial reduction theorem. No claim is made for other \(p\), for all coefficient orders, or for a uniform stability modulus near the optimizer. Historical coverage could still be implicit in older unexamined extremal-function literature; in particular, the full 1990 Suffridge chapter was not accessible for direct inspection. No independent mathematical audit has been performed.

## References
1. O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788v1, first released 2026-10-15, Corollary 3. https://arxiv.org/html/2610.21788v1
2. O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547, first released 2019-05-23, published in Proceedings of the American Mathematical Society 148 (2020), 3911–3924. https://arxiv.org/abs/1905.09547
3. O. F. Brevig, S. Grepstad and S. M. Instanes, *F. Wiener's trick and an extremal problem for \(H^p\)*, computational and analytic Hardy extremal questions, DOI:10.1007/s40315-022-00469-x (2022). https://doi.org/10.1007/s40315-022-00469-x
4. T. J. Suffridge, *Extremal problems for nonvanishing \(H^p\) functions*, Lecture Notes in Mathematics 1435 (1990), 177–190. The full chapter was not available in the consulted lawful sources.
