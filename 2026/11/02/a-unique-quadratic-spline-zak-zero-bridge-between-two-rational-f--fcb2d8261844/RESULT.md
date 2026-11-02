# A unique quadratic-spline Zak-zero bridge between two rational frequencies

## Finding

Let \(B_3=B_1*B_1*B_1\) be the centered order-three (piecewise quadratic) cardinal B-spline, where \(B_1=\mathbf 1_{[-1/2,1/2]}\). For \(b>0\), use the Zak convention
\[
Z_{1/b}B_3(x,\nu)=b^{-1/2}\sum_{k\in\mathbb Z}B_3((x-k)/b)e^{2\pi i k\nu}.
\]
For every \(2<b<8/3\), the complete real-frequency zero set on the boundary line \(x=0\), modulo one, consists of exactly two distinct points:
\[
\{\nu\in[0,1):Z_{1/b}B_3(0,\nu)=0\}=\{\nu_b,1-\nu_b\},\qquad \frac13<\nu_b<\frac12.
\]
Writing \(t_b=\cos(2\pi\nu_b)\), the number \(t_b\) is the **unique** root in \([-1,1]\) of the explicit cubic
\[
P_b(t)=\frac{36b^2t^3+18b^2t^2-21b^2t-6b^2-144bt^3-48bt^2+108bt+24b+144t^3+32t^2-116t-16}{4b^2}.
\]
The zero curve is real analytic in the open interval and has distinct one-sided endpoint laws:
\[
\frac12-\nu_b=\frac{\sqrt{6+\sqrt{42}}}{2\sqrt2\,\pi}\sqrt{b-2}+O((b-2)^{3/2})\quad(b\downarrow2),
\]
\[
\nu_b-\frac13=\frac{9\sqrt3}{16\pi}\left(\frac83-b\right)^2+O\left(\left(\frac83-b\right)^3\right)\quad(b\uparrow8/3).
\]
Thus this symmetry-axis zero branch connects the half-frequency zero at integer scale \(b=2\) to the third-frequency zero at the next support-knot threshold \(b=8/3\), with square-root emergence at one end and quadratic attachment at the other. No conclusion about the whole two-dimensional Zak zero set, or the full Gabor frame set, is asserted.

## Assumptions and scope

The degree-two spline is explicitly
\[
B_3(y)=\begin{cases}\frac34-y^2,&|y|\le\frac12,\\
\frac12(\frac32-|y|)^2,&\frac12<|y|<\frac32,\\
0,&|y|\ge\frac32.
\end{cases}
\]
All parameters \(b\) are real, and all zero frequencies \(\nu\) are real modulo one. The strict interval \(2<b<8/3\) is the full interval after \(b=2\) and before the next symmetric summand \(k=\pm4\) activates at \(b=8/3\): the finite Zak sum on \(x=0\) has exactly the terms \(k=-3,-2,\ldots,3\) throughout. Here the spline order is three, not the cubic (order-four) spline.

## Proof

**1. Exact reduction.** Since \(3b/2\in(3,4)\), the only nonzero sampled values at \(x=0\) are \(B_3(k/b)\) for \(|k|\le3\). Write
\[
a_0=\frac34,\quad a_1=\frac34-\frac1{b^2},\quad
a_2=\frac12\left(\frac32-\frac2b\right)^2,\quad
a_3=\frac12\left(\frac32-\frac3b\right)^2.
\]
Evenness gives, with \(\theta=2\pi\nu\),
\[
\sqrt b\,Z_{1/b}B_3(0,\nu)=a_0+2a_1\cos\theta+2a_2\cos2\theta+2a_3\cos3\theta.
\]
Using \(\cos2\theta=2t^2-1\), \(\cos3\theta=4t^3-3t\), this equals \(P_b(t)\) with \(t=\cos\theta\), and direct expansion gives precisely the displayed cubic.

**2. An exactly one-root cubic.** The signs
\[
P_b(-1)=-\frac{3(b-2)^2}{4b^2}<0,\qquad
P_b(-\tfrac12)=\frac{(3b-8)^2}{8b^2}>0
\]
put at least one root in \((-1,-1/2)\). To exclude every other root in \([-1,1]\), make the bijective change \(t=(u-1)/(u+1)\), \(u>0\), and calculate
\[
(u+1)^3P_b\left(\frac{u-1}{u+1}\right)=c_0+c_1u+c_2u^2+c_3u^3,
\]
where
\[
\begin{aligned}
c_0&=-\frac{3(b-2)^2}{4b^2},&
c_1&=\frac{3(b-2)(31b-78)}{4b^2},\\
c_2&=-\frac{165b^2-660b+628}{4b^2},&
c_3&=\frac{27b^2-60b+44}{4b^2}>0.
\end{aligned}
\]
For \(2<b\le78/31\), the coefficient signs in increasing order are \((-,-,\pm,+)\), after omitting zeros. Descartes' rule of signs gives **at most one** positive real root, counted with multiplicity.

For \(78/31<b<8/3\), the derivative \(P_b'\), a quadratic with positive leading coefficient \(27(b-2)^2/b^2\), has discriminant
\[
\operatorname{disc}(P_b')=
\frac{8(9b^2-42b+47)(9b^2-36b+34)}{b^4}<0.
\]
Indeed the first quadratic is negative throughout this interval, whereas the second is positive, since \(78/31>(6+\sqrt2)/3\) and \(8/3<(7+\sqrt2)/3\). Hence \(P_b'>0\) on the real line, and there is exactly one real root. Combining the two cases, \(t_b\in(-1,-1/2)\) is the unique root in \([-1,1]\), and it is simple. Since \(\cos(2\pi\nu)=t_b\) has exactly the two solutions \(\nu_b\in(1/3,1/2)\) and \(1-\nu_b\) modulo one, the zero classification follows. Simplicity gives real-analytic dependence on \(b\) by the implicit-function theorem.

**3. Half-frequency endpoint.** At \(b=2\), direct factorization gives \(P_2(t)=\tfrac12(t+1)^2\). Put \(b=2+\epsilon\), \(t=-1+h\). The Taylor expansion, uniformly for small \(\epsilon,h\), is
\[
P_{2+\epsilon}(-1+h)=\frac{h^2}{2}-\frac{3\epsilon h}{2}-\frac{3\epsilon^2}{16}
+O(|h|^3+|\epsilon|h^2+\epsilon^2|h|+|\epsilon|^3).
\]
The unique physical root satisfies \(h=\epsilon[(6+\sqrt{42})/4+O(\epsilon)]\): substitution \(h=\epsilon y\) reduces the leading equation to \(8y^2-24y-3=0\), whose positive root is \((6+\sqrt{42})/4\). Because \(\cos(2\pi\nu_b)=-1+2\pi^2(1/2-\nu_b)^2+O((1/2-\nu_b)^4)\), this gives the stated square-root law with its \(O(\epsilon^{3/2})\) remainder.

**4. Third-frequency endpoint.** At \((b,t)=(8/3,-1/2)\), exact differentiation yields
\[
P_b(t)=0,\qquad \partial_tP_b(t)=\frac3{32},\qquad
\partial_bP_b(t)=0,\qquad \partial_b^2P_b(t)=\frac{81}{256}.
\]
The implicit-function theorem therefore gives
\[
t_b=-\frac12-\frac{27}{16}\left(\frac83-b\right)^2+O\left(\left(\frac83-b\right)^3\right).
\]
Finally, \(d[\arccos(t)/(2\pi)]/dt=-1/(\pi\sqrt3)\) at \(t=-1/2\). This yields the claimed quadratic attachment law.

## Verification

The standalone file `CHECKER.py` uses exact symbolic arithmetic to reproduce the finite Zak reduction, both endpoint sign identities, the Möbius/Descartes coefficients, the derivative discriminant, and the endpoint Taylor coefficients. It also checks sample direct finite Zak sums against the cubic and brackets roots at rational \(b\). Run `python CHECKER.py` with SymPy available. The checker is supplementary: the uniqueness and limiting assertions are proved analytically in the preceding sections, not by sampling.

## Relationship to prior work

Hasannasab and Lemvig, arXiv:2609.13116 (first public 2026-09-11), establish the one-point zero classification for \(\lambda\ge1\) and the full smaller-\(\lambda\) picture for \(B_2\), but explicitly leave richer odd-order zeros at \(x=0\) unclassified (their Remark 1 after Proposition 4.2). Their cubic-order discussion in Section 6 treats a different symmetry line, \(x=1/2\), and their rational horizontal-zero statements do not determine the moving irrational pair above. The present result resolves the first complete support-knot chamber on the line \(x=0\) for \(B_3\), not the unrestricted problem.

Lemvig and Nielsen, arXiv:1507.03982 (2015), and Lemvig, arXiv:2601.07642 (2026), establish Gabor nonframe obstructions concentrated at rational Zak frequencies and partition-of-unity configurations. Their inspected results neither state nor imply the unique moving \(x=0\) pair and its two endpoint exponents. Results for the hat spline \(B_2\) do not classify \(B_3\).

## Limitations

Only the symmetry line \(x=0\) and the scale chamber \(2<b<8/3\) are classified. Other zeros at \(x\ne0\) may exist. The derived zeros alone do not prove failure of any Gabor frame: that would require a suitably spaced collection of fiber zeros. No assertion of absolute historical priority or independent validation is made. Broader unpublished or differently formulated spline-zero results are a residual literature risk.

## References

1. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (submitted 2026-09-11), https://arxiv.org/abs/2609.13116 .
2. J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982 (first submitted 2015-07-14), https://arxiv.org/abs/1507.03982 .
3. J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642 (first submitted 2026-01-12), https://arxiv.org/abs/2601.07642 .
4. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (2026), https://arxiv.org/abs/2609.00481 (abstract-level comparison only).
