# Sharp Berezin cusp sections for origin-fixed symbols with nonreal multiplier

## Finding

Let \(0<s<1\) and let \(\mathcal D_s\) have reproducing kernel \(K_s(z,w)=(1-z\overline w)^{-s}\). Suppose \(\phi:\mathbb D\to\mathbb D\) is holomorphic, fixes zero, and induces a bounded unweighted composition operator on \(\mathcal D_s\). Suppose that \(\phi\) is nonlinear and has a nonreal multiplier \(a=\phi'(0)\), with
\[
\phi(z)=az+bz^{m+1}+O(z^{m+2}),\qquad b\ne0,\quad m\ge1.
\]
Put \(\vartheta=\arg(1-a)\), \(\nu=1+m/2\), and \(\kappa=|b|/(s^{m/2}|1-a|^\nu)\). Write the Berezin value at \(w\) as \(F(w)\), and use the coordinates \(x+iy=e^{-i\vartheta}(1-F(w))\). In a sufficiently small fixed neighborhood of the tip, the vertical section at every sufficiently small \(x>0\) is a closed interval \([Y_-(x),Y_+(x)]\) with
\[
Y_\pm(x)=h(x)\pm\kappa x^\nu+O(x^{\nu+1/2}).
\]
Here \(h\) is the real-analytic graph of the Berezin curve of the linear symbol \(z\mapsto az\) in the same coordinates near the tip. In particular
\[
h(x)=\frac{(s+1)\operatorname{Im}a}{2s|1-a|}x^2+O(x^3).
\]
For \(m\ge3\), this curvature displacement is larger in order than the half-width. The half-width, rather than each endpoint's distance from the tangent line, gives the first nonlinear degree \(m+1\) and, for known \(s,a\), the modulus \(|b|\).

## Assumptions and scope

This is a local section law for a bounded, unweighted composition operator with a nonlinear origin-fixed symbol and nonreal multiplier. It does not assert boundedness for arbitrary symbols, classify weighted operators, or assert a global range formula. No regularity at the disk boundary is assumed.

## Proof

Kernel evaluation gives \(F(w)=((1-|w|^2)/(1-\overline w\phi(w)))^s\) with the principal power. Schwarz's lemma gives \(|a|<1\), since equality forces a linear symbol. For \(r=|w|\), apply Schwarz–Pick to \(\phi(w)/w\) with the value \(a\) at zero. This gives
\[
|F(w)|^{1/s}\le
\frac{1-r^2}{1-r^2(|a|+r)/(1+|a|r)}
=1-\frac{(1-|a|)r^2}{1+r+r^2+|a|r}.
\]
Thus values near one can only come from small \(r\).

Put \(t=r^2\), \(w=\sqrt t\,e^{i\theta}\), and write \(U(t,\theta)=e^{-i\vartheta}(1-F(w))\). Define \(U_a(t)=e^{-i\vartheta}[1-((1-t)/(1-at))^s]\). The nonlinear jet gives, uniformly in angle,
\[
U(t,\theta)=U_a(t)-s e^{-i\vartheta}b\,t^\nu e^{im\theta}+O(t^{\nu+1/2}).
\]
The expansion is analytic in \(r\) near zero, with uniform remainder and derivative bounds on the angle circle. Consequently \(\partial_t\operatorname{Re}U(t,\theta)=s|1-a|+O(t^{1/2})>0\) for small positive \(t\). For each sufficiently small \(x>0\) there is exactly one small solution \(t(x,\theta)\) of \(\operatorname{Re}U=x\) at each angle, continuous in \(\theta\). If \(t_a(x)\) is the local analytic inverse of \(\operatorname{Re}U_a\), the positive derivative bound gives \(t(x,\theta)=t_a(x)+O(x^\nu)\) and \(t_a(x)=x/(s|1-a|)+O(x^2)\). All these small solutions lie in the chosen neighborhood for sufficiently small \(x\), and the localization inequality excludes other preimages there.

Set \(h(x)=\operatorname{Im}U_a(t_a(x))\). Since \(U_a'(0)=s|1-a|\) is real, \(\operatorname{Im}U_a'(t)=O(t)\). Substitution yields
\[
\operatorname{Im}U(t(x,\theta),\theta)=h(x)-s\operatorname{Im}(e^{-i\vartheta}be^{im\theta})\left(\frac{x}{s|1-a|}\right)^\nu+O(x^{\nu+1/2}).
\]
The continuous map from the angle circle has interval image, and its leading harmonic attains both extremes \(\pm|b|\) before rescaling. Comparing with these two angles gives both endpoint estimates, with \(s|b|(s|1-a|)^{-\nu}=\kappa\). Writing \(d=1-a\), the second coefficient of \(U_a(t)\) is \(s|d|[a-(s-1)d/2]\). Its imaginary part is \(s|d|(s+1)\operatorname{Im}a/2\), which gives the stated expansion of \(h\). Finally, if \(W(x)=(Y_+(x)-Y_-(x))/2\), then \(\log W(x)/\log x\to\nu\) and \(W(x)/x^\nu\to\kappa\). These recover the degree and modulus as asserted.

## Verification

The localization, angular inversion, leading coefficient, and interval assertion follow from the proof. The accompanying standard-library script `check_berezin_cusp.py` compares normalized endpoint estimates on twelve finite polynomial families at two small scales. These are numerical diagnostics, not the source of the estimates or a proof for all symbols.

## Relationship to prior work

Barik, Sen and Paul, arXiv:2602.09481v1, §5 and Theorem 1.12, gives the same weighted-Dirichlet linear-symbol curve and classifies its convexity. Bourdon, Le and Thompson, arXiv:2610.17634, Lemma 3.10, Theorem 3.11 and Remark 3.12(i), give tip localization and the qualitative cusp direction in the Hardy case. Both the all-origin-fixed Hardy convexity classification and the sharp Hardy width law at real interior multipliers are given in the respective indexed results *Convexity rigidity for all zero-fixing Hardy composition symbols* and *Sharp Taylor-jet cusp widths for zero-fixing Hardy composition operators*. Changing the kernel power raises the Hardy transform to the power \(s\); it does not by itself supply a transverse section theorem at a nonreal multiplier when the known quantitative Hardy theorem assumes a real one. The claim here is the exact section law with the curved linear-symbol centerline and first nonlinear transverse width at a nonreal multiplier, not a convexity classification or a claim of priority over the real-multiplier law.
