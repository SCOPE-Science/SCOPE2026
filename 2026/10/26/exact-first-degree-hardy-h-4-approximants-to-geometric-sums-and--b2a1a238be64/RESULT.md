# Exact first-degree Hardy \(H^4\) approximants to geometric sums and a sharp boundary-root approach

## Finding

For every integer \(n\ge1\), let \(f_n(z)=1+z+\cdots+z^n\). The unique minimizer of \(\|1-qf_n\|_{H^4}\) over complex polynomials \(q\) of degree at most one is
\[
q_n(z)=\frac{1+t_n}{2}+\frac{t_n-1}{2}z,
\]
where \(t_n\in(0,1)\) is the unique zero in that interval of
\[
(16n^3+48n^2+32n+9)t^3-(36n^2+72n+27)t^2+(36n+27)t-9=0.
\]
Its zero is \(\omega_n=(1+t_n)/(1-t_n)>1\). If \(c_*\) is the unique real root of \(16c^3-36c^2+36c-9=0\), then
\[
nt_n\longrightarrow c_*=0.357498368378205\ldots,\qquad
n(\omega_n-1)\longrightarrow 2c_*=0.714996736756410\ldots.
\]
Thus this fixed prescription for polynomial inputs gives an exact inverse-degree approach to the unit circle from outside.

## Assumptions and scope

The norm is \(\|g\|_{H^4}^4=\int_0^{2\pi}|g(e^{i\theta})|^4\,d\theta/(2\pi)\). The degree bound is at most one and the coefficients of \(q\) are unrestricted. The new formulas concern the specific inputs \(f_n\), not arbitrary \(H^4\) inputs or higher-degree approximants.

## Proof

**Uniqueness and symmetries.** The map \(q\mapsto1-qf_n\) is affine and injective. Integration of the strictly convex function \(w\mapsto |w|^4\) gives strict convexity of the fourth-power objective: distinct residual polynomials differ on a set of positive circle measure. Coercivity follows from norm equivalence on the finite-dimensional image of the linear map \(q\mapsto qf_n\). The minimizer exists and is unique. Conjugating the coefficients preserves the objective, so it is of the form \(q=a+bz\) with real \(a,b\).

Its residual has coefficient vector \((1-a,-(a+b),\ldots,-(a+b),-b)\), with \(n\) interior coefficients. Reversal of this vector preserves the norm by the circle substitution \(z\mapsto z^{-1}\) and gives the feasible residual for \(q'=(1+b)+(a-1)z\). Uniqueness forces \(1-a=-b\). Set \(t=a+b\) and \(s=(1-t)/2\). The residual is
\[
R_t(z)=s-t\sum_{j=1}^nz^j+sz^{n+1}.
\]

**Exact objective.** For real coefficients \(r_j\) of \(R_t\), set \(A_d=\sum_{j=0}^{n+1-d} r_jr_{j+d}\). Fourier orthogonality gives \(F_n(t)=\|R_t\|_{H^4}^4=A_0^2+2\sum_{d=1}^{n+1}A_d^2\). Here \(A_0=2s^2+nt^2\), \(A_d=(n-d)t^2-2st\) for \(1\le d\le n\), and \(A_{n+1}=s^2\). Summing the squares gives
\[
F_n(t)=6s^4+12ns^2t^2-4n(n-1)st^3+\frac{n(2n^2+1)}3t^4.
\]
Its derivative times six is the displayed cubic. At \(t=0\) it is \(-9\), and at \(t=1\) it is \(4n(4n^2+3n-1)>0\). The strict convexity of \(F_n\) makes its minimizing root unique. Since the unrestricted minimizer lies on this line, this also proves unrestricted optimality and the zero formula.

**Boundary rate.** For each fixed real \(c\), \(6F_n'(c/n)\) converges to \(P(c)=16c^3-36c^2+36c-9\). The derivative \(P'(c)=12(4c^2-6c+3)\) is strictly positive on the real line, and \(P(0)<0<P(1)\). For any sufficiently small \(\varepsilon>0\), the signs at \((c_*-\varepsilon)/n\) and \((c_*+\varepsilon)/n\) are eventually opposite, so \(nt_n\to c_*\). The identity \(n(\omega_n-1)=2nt_n/(1-t_n)\) gives the second limit.

## Verification

The accompanying standalone `check.py` compares the correlation computation against the closed quartic and numerically brackets the derivative root for representative degrees. The polynomial identity and limiting law are proved above for the entire family; the numerical checks are corroboration only.

## Relationship to prior work

Centner, Cheng, and Felder [1, Theorem 4.5] give general integral equations for first-degree optimal approximants, and [1, Theorem 5.16] proves a positive root-modulus lower bound for even \(p>2\). The general integral equations do not supply the explicit cubic and boundary-rate constant for these geometric sums.

The impossibility of a universal exclusion radius strictly greater than one over all \(H^p\) inputs is not new: the construction in Cheng and Felder [2, Proposition 3.2.3] takes \(f(z)=1/(z-w)\) for \(|w|>1\), with the exact zero-residual approximant \(q(z)=z-w\). The contribution here is the exact cubic and sharp inverse-degree root law for a prescribed family of polynomial generators, not the general obstruction. In particular, it does not decide whether degree-one roots for other \(H^4\) inputs can lie in the open disk.

## References

1. R. Centner, R. Cheng, and C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, arXiv:2305.16068.
2. R. Cheng and C. Felder, *More Properties of Optimal Polynomial Approximants in Hardy Spaces*, arXiv:2310.16010.
