# Unrestricted complex half-plane stability of two-periodic variable-step BDF2 and its Crank–Nicolson limit

## Finding

For every pair of positive alternating time-step lengths, variable-step BDF2 applied to the scalar equation \(y'=-\kappa y\) is power-bounded when \(\kappa=0\) and strictly contracting from period to period when \(\operatorname{Re}\kappa\geq0\) and \(\kappa\ne0\). No upper bound on either adjacent step ratio is required **for this precisely alternating mesh**. Its two-period amplification polynomial depends on the ratio only through \(\chi=r+r^{-1}\). A singular large-ratio limit gives one vanishing multiplier and the Crank–Nicolson multiplier \((2-z)/(2+z)\), showing a sharp distinction between pointwise half-plane stability and uniform imaginary-axis damping.

More explicitly, for \(h>0\), \(r>0\), and \(z=\kappa h(1+r)\), the two Floquet multipliers are precisely the roots of
\[
\big[z^2+(\chi+4)z+2\chi+5\big]\mu^2-\big[2\chi+6-\chi z\big]\mu+1=0,\qquad \chi=r+r^{-1}\ge2.
\]
For every \(\operatorname{Re}z\ge0\) with \(z\ne0\), both roots have modulus strictly below one; at \(z=0\), the distinct roots are \(1\) and \(1/(2\chi+5)\). With \(z\) fixed and \(r\to\infty\), the two roots converge as an unordered pair to \(0\) and \((2-z)/(2+z)\). For fixed finite \(r\), both roots tend to zero as \(|z|\to\infty\) in the closed right half-plane.

## Assumptions and scope

The numerical method is the **standard variable-step BDF2 formula**, without stabilizing extra terms or nonlinear auxiliary variables. In a recurrence \(y_{n+1}\) computed from \(y_n,y_{n-1}\), let the current positive step be \(k\), the previous step be \(k/q\) and write the positive adjacent ratio as \(q\). The derivative approximation is
\[
\frac1k\left[\frac{1+2q}{1+q}y_{n+1}-(1+q)y_n+\frac{q^2}{1+q}y_{n-1}\right].
\]
The step sequence repeats the two lengths \(rh,h\) indefinitely (up to a cyclic shift), and the constant coefficient \(\kappa\in\mathbb C\) is arbitrary with \(\operatorname{Re}\kappa\ge0\). The exact algebra is in complex arithmetic. A linear scalar eigenmode of a diagonalizable linear system follows this analysis mode-by-mode, but no general matrix-norm bound uniform in spectral conditioning, no general nonlinear stability or energy claim, and no result for nonperiodic variable meshes is inferred.

## Proof

**Period matrix.** Solving the BDF2 update for the new value gives the companion matrix
\[
T(q,w)=\begin{pmatrix}
\dfrac{(1+q)^2}{1+2q+(1+q)w}&-\dfrac{q^2}{1+2q+(1+q)w}\\[4pt]
1&0
\end{pmatrix},\qquad w=\kappa k.
\]
The denominator is nonzero when \(q>0\) and \(\operatorname{Re}w\ge0\). The period matrix \(P=T(r^{-1},z/(1+r))T(r,rz/(1+r))\) has
\[
\det P=\frac1D,\qquad \operatorname{tr}P=\frac ND,
\]
where \(D=z^2+(\chi+4)z+2\chi+5\) and \(N=2\chi+6-\chi z\). Taking its characteristic polynomial proves the claimed closed form.

**Complex Schur test.** A complex monic quadratic \(\mu^2+a\mu+b\) has both zeros strictly inside the unit disk if and only if \(|b|<1\) and \(|a-\overline a b|<1-|b|^2\). For the present polynomial these conditions become
\[
|D|>1,\qquad |N\overline D-\overline N|<|D|^2-1.
\]
Put \(x=\operatorname{Re}z\ge0\), \(Q=|z|^2=x^2+(\operatorname{Im}z)^2\), and \(\chi\ge2\). Direct expansion gives
\[
\begin{aligned}
|D|^2-1={}&Q^2+2(\chi+4)xQ+(\chi^2+4\chi+6)Q\\
&+4(2\chi+5)x^2+2(\chi+4)(2\chi+5)x+(2\chi+5)^2-1,
\end{aligned}
\]
which is strictly positive. More decisively, set
\[
F=Q^2+2(\chi+4)xQ+4(2\chi+5)x^2+8(\chi+2)x
\]
and
\[
G=F+(\chi+2)(\chi+6)Q+12(\chi+2)^2x+4(\chi+2)^2(\chi+3).
\]
The exact polynomial identity
\[
\boxed{\big(|D|^2-1\big)^2-|N\overline D-\overline N|^2=FG}
\]
holds for all real \(x,\operatorname{Im}z,\chi\). If \(z\ne0\), then \(Q>0\), hence \(F>0\) and \(G>0\). Therefore both Schur inequalities hold and both multipliers have modulus below one for every nonzero \(z\) in the closed right half-plane.

**Zero frequency and limits.** At \(z=0\), the polynomial factors as \((\mu-1)((2\chi+5)\mu-1)\), with two distinct roots and thus a power-bounded period matrix. For fixed \(z\), dividing \(D,N\) by \(\chi\) and taking \(r\to\infty\) yields \(N/D\to(2-z)/(2+z)\) and \(1/D\to0\) (\(2+z\ne0\) on the stated half-plane). The limiting polynomial is therefore \(\mu[\mu-(2-z)/(2+z)]\). Finally, at fixed \(r\), \(N/D\to0\) and \(1/D\to0\) as \(|z|\to\infty\); the two roots then both tend to zero. On the imaginary axis with \(z\ne0\), \(|(2-z)/(2+z)|=1\), so the large-ratio family does **not** have damping uniform over all positive ratios. This completes the proof.

## Verification

The standalone `verify.py` checks symbolic formulas for the period determinant, trace, expanded Schur expressions and factorization, and both singular limits using SymPy. It also compares direct two-step matrix products against the closed polynomial on seeded complex test points; those numerical checks do not replace the analytic proof. Execute `python verify.py` in an environment with Python 3, SymPy and NumPy. The analytic positivity argument covers the full infinite parameter domain, unlike the finite test cases.

For example, at \(z=2i\), the leading multiplier magnitudes are approximately \(0.8710881981\) for ratio \(r=1\) and \(0.9995006264\) for ratio \(r=1000\). The limit of this magnitude as \(r\to\infty\) is exactly one.

## Relationship to prior work

Shergill and Williams (arXiv:2610.30454v1, Sections 2.3 and 4.3) employ the same variable-step BDF2 coefficients in adaptive SSAV gradient-flow integration and invoke the usual adjacent-ratio restriction \(\rho<1+\sqrt2\) for their second-order convergence discussion. The present theorem concerns only the homogeneous scalar test equation on **exactly period-two meshes**: its arbitrary-ratio, full complex-half-plane Floquet conclusion does not follow from that general-grid statement, nor does it establish stability of the coupled SSAV method for unrestricted ratios.

Li and Liao (arXiv:2201.00527v1) prove a different mesh-robust BDF2 perturbation stability under a sufficiently small maximum step dependent on the Lipschitz constant; that result does not itself imply unconditional test-equation damping for arbitrarily large \(|\kappa|h\), or the exact two-period multiplier law. Akrivis et al. (2024) establish parabolic stability estimates with bounded adjacent ratios (up to about \(1.9398\)), again a different statement. Classical constant-step BDF2 A-stability is well known but does not imply the present nonconstant two-step product result.

Bourgault and Garon (2022) study variable-step BDF-based **deferred-correction** schemes. Their accessible abstract does not settle whether they contain the exact unrestricted alternating-grid scalar result; the full text was not available for examination and is an outstanding historical-priority risk. No novelty claim is based on lack of search hits alone.

## Limitations

Only exactly alternating step sequences, scalar constant-coefficient equations, and exact arithmetic are proved. For each fixed ratio, strict period damping holds, but the damping factor cannot be bounded away from one uniformly over extreme ratios on the imaginary axis. No proof of second-order convergence for unrestricted-ratio arbitrary variable meshes, nonlinear gradient-flow energy dissipation, general matrix norms, or uniformly bounded error constants is supplied. Historical priority, particularly deferred-correction and periodic multistep literature, remains subject to fuller specialist comparison. Independent mathematical audit has not been performed.

## References

1. S. Shergill and J. F. Williams, *Energy-rate equidistribution for adaptive SSAV–BDF2 integration of gradient flows*, arXiv:2610.30454v1 (first submitted 21 October 2026). https://arxiv.org/html/2610.30454v1
2. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527v1 (2022). https://arxiv.org/html/2201.00527v1
3. G. Akrivis, M. Chen, J. Han, F. Yu, and Z. Zhang, *The variable two-step BDF method for parabolic equations*, BIT Numerical Mathematics 64, article 14 (2024). https://doi.org/10.1007/s10543-024-01007-y
4. Y. Bourgault and A. Garon, *Variable-step deferred correction methods based on backward differentiation formulae for ordinary differential equations*, BIT Numerical Mathematics (2022). https://doi.org/10.1007/s10543-022-00931-1
