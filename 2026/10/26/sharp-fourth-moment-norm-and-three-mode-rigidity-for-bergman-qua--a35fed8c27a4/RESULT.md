# Sharp fourth-moment norm and three-mode rigidity for Bergman quadratics

## Finding

Let \(dA_0(z)=\pi^{-1}\,dx\,dy\) be probability area measure on the unit disk \(\mathbb D\), and write \(\|f\|_p=(\int_{\mathbb D}|f|^p\,dA_0)^{1/p}\). For every nonzero analytic polynomial \(f(z)=a+bz+cz^2\) of degree at most two,
\[
\frac{\|f\|_4^4}{\|f\|_2^4}\le K=2.679775542207614429\ldots.
\]
Precisely, \(s_*\) is the unique positive zero of
\[
4s^3+5s^2-35s-30=0,
\]
and the sharp constant is
\[
K=\frac{9(11s_*^4+40s_*^3+60s_*^2+80s_*+40)}{43s_*^4+120s_*^3+150s_*^2+360s_*+225}.
\]
Equivalently, \(K\) is the largest real zero of \(19070K^3-110975K^2+206145K-122472=0\). Equality holds **if and only if**
\[
f(z)=\lambda\bigl(1+\sqrt{s_*+3}\,e^{i\theta}z+s_*e^{2i\theta}z^2\bigr),
\qquad \lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.
\]
In particular, every extremizer uses all three monomials. The sharp ratio among polynomials supported on at most two of these three monomials is strictly smaller, namely \(99/43\).

## Assumptions and scope

The norms have the **same** unweighted Bergman area measure and are not Hardy boundary norms or norms with two different radial weights. The claim concerns the complete complex three-dimensional space \(\operatorname{span}\{1,z,z^2\}\), with arbitrary complex coefficients; it does not assert a result for degree three or arbitrary analytic functions. The factor \(\pi^{-1}\) makes the disk area a probability measure. Zero polynomials are excluded from the ratio, although the homogeneous inequality holds for zero.

## Proof

Orthogonality of disk monomials gives \(\|z^j\|_2^2=1/(j+1)\). Applying this to \(f^2\) yields the exact identity
\[
\|f\|_4^4=|a|^4+2|ab|^2+\tfrac13|b^2+2ac|^2+|bc|^2+\tfrac15|c|^4,
\qquad \|f\|_2^2=|a|^2+\tfrac12|b|^2+\tfrac13|c|^2.
\]
For fixed coefficient magnitudes, the sole phase-dependent term is bounded by \(|b^2+2ac|\le|b|^2+2|a||c|\). Equality when all three magnitudes are positive requires \(2\arg b\equiv\arg a+\arg c\pmod{2\pi}\), and this is realized precisely by a common complex scalar and a rotation of the variable.

Assume first \(|a|>0\). Put \(s=|c|/|a|\ge0\) and \(r=|b|^2/|a|^2\ge0\). The phase-aligned fourth-power ratio is
\[
J(r,s)=\frac{r^2/3+(2+4s/3+s^2)r+(1+4s^2/3+s^4/5)}{(1+r/2+s^2/3)^2}.
\]
With \(U=1+s^2/3\), \(B=2+4s/3+s^2\), and \(C=1+4s^2/3+s^4/5\), the sign of the partial derivative \(\partial_rJ\) is the sign of
\[
(2U/3-B/2)r+(BU-C).
\]
Here \(B-4U/3=2/3+4s/3+5s^2/9>0\), whereas \(BU-C=1+4s/3+s^2/3+4s^3/9+2s^4/15>0\). Thus for each \(s\ge0\), \(J\) increases and then decreases as \(r\) varies, with the **unique** maximizer
\[
r_*(s)=\frac{2(6s^4+20s^3+15s^2+60s+45)}{5(5s^2+12s+6)}.
\]
Substitution simplifies exactly to
\[
F(s)=J(r_*(s),s)=\frac{9(11s^4+40s^3+60s^2+80s+40)}{43s^4+120s^3+150s^2+360s+225}.
\]
Its derivative is
\[
F'(s)=\frac{-180(s+1)(5s^2+12s+6)(4s^3+5s^2-35s-30)}{(43s^4+120s^3+150s^2+360s+225)^2}.
\]
The cubic has exactly one positive real zero by Descartes' sign rule and continuity. It is negative at zero and eventually positive. Therefore \(F\) strictly increases until \(s_*\), then strictly decreases. Furthermore,
\[
r_*(s)-s-3=\frac{3s(4s^3+5s^2-35s-30)}{5(5s^2+12s+6)},
\]
so \(r_*(s_*)=s_*+3\). This proves the stated constant and rigid equality family for \(|a|>0\).

The boundary \(a=0\) is handled without assuming a limiting maximizer: setting \(v=|b|^2/|c|^2\) for \(c\ne0\) gives
\[
\frac{\|bz+cz^2\|_4^4}{\|bz+cz^2\|_2^4}
=\frac{v^2/3+v+1/5}{(v/2+1/3)^2}\le\frac{99}{43},
\]
with equality precisely when \(v=12/25\). When \(a=c=0\), the value is \(4/3\). Directly setting \(s=0\) gives the \(\{1,z\}\) optimum \(8/5\); setting \(b=0\) gives the \(\{1,z^2\}\) optimum \(11/6\). Thus \(99/43\) is also the maximum over all two-term supports. Since \(F(s_*)>F(0)=8/5\) and \(F(s_*)>\lim_{s\to\infty}F(s)=99/43\), no boundary coefficients attain the global maximum. The resultant elimination of \(s_*\) yields the displayed cubic for \(K\); the positive maximizer selects its largest root.

## Verification

The standalone `verify.py` uses exact symbolic arithmetic to check the differentiation, unique-in-\(r\) critical point, rational reduction, derivative factorization, cubic resultant, boundary values and optimizer identity. It also performs 2,500 seeded complex-coefficient consistency trials. Running `python verify.py` produced `PASS 8 exact symbolic checks, 4 numerical critical checks, 2500 deterministic complex trials.` All infinite and global statements above are justified analytically, not by those finite trials.

## Relationship to prior work

Melentijević's 2022 work proves sharp Bergman hypercontractive inequalities under a fixed dilation; those compare \(f(rz)\) with \(f(z)\) and do not give the exact *undilated* finite-degree same-measure constant here. Wang and Zhang's 2025 degree-sensitive Nikol'skiĭ estimate yields, for degree two, the nonsharp upper bound \(\|f\|_4/\|f\|_2\le2\), whereas the present sharp factor is \(K^{1/4}=1.27945378901685\ldots\). Contemporary exact Nikolskiĭ results for analytic quadratics on the **circle**, with a different target exponent, do not imply the present area-integral fourth moment. The contribution is the exact global norm together with the complete nontrivial three-coefficient extremizer classification and two-term sharp gap, not a new infinite-dimensional embedding theorem.

## Limitations

The proof is specific to unweighted disk area and polynomial degree at most two; the same coefficients need not optimize other radial weights or higher degrees. The historical-priority comparison is limited to the literature and searchable records named below; undiscovered earlier equivalent finite-degree calculations remain possible. No independent audit or external validation has been performed.

## References

1. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655 (first submitted 2022-11-07), https://arxiv.org/abs/2211.03655.
2. Z. Wang and K. Zhang, *Hypercontractive inequalities and Nikol'skiĭ-type inequalities on weighted Bergman spaces*, arXiv:2505.12760 (first submitted 2025-05-19), https://arxiv.org/abs/2505.12760.
