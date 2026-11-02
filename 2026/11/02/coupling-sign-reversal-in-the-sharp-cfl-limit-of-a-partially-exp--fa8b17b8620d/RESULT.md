# Coupling-sign reversal in the sharp CFL limit of a partially explicit two-mode wave scheme

## Finding
Consider the two-mode semidiscrete wave equation \(\ddot q+Kq=0\), where \(K=\begin{pmatrix}A&C\\ C&B\end{pmatrix}\) is real positive definite: \(A,B>0\), \(C^2<AB\). Use the orthogonal unit-mass split into the two coordinate modes and the second-order partially explicit scheme of the next section, with \(0\le\omega\le1\).

The numerical sequence is power bounded for **every** pair of initial states if and only if its positive time step \(h\) satisfies
\[
0<h^2<T_\star(\omega),\qquad
T_\star(\omega)=\frac{8}{\sqrt{(A+B)^2+4(2\omega-1)C^2}-(A-B)}.
\]
At equality, an initial state has an \(n(-1)^n\) growing component; above equality, some initial state grows exponentially. If \(C\ne0\), the sharp squared-step ceiling is strictly decreasing with \(\omega\). In particular,
\[
T_\star(\tfrac12)=\frac4B,\quad T_\star(0)>\frac4B>T_\star(1).
\]
Thus the *same* off-diagonal stiffness coupling stabilizes the \(\omega=0\) temporal placement and destabilizes the \(\omega=1\) placement, with a coupling-independent separator at \(\omega=1/2\). If \(C=0\), all weights have the ceiling \(4/B\).

The effect can be arbitrarily large within the positive-definite class: for \(A=B=\beta>0\), \(0<|C|<\beta\),
\[
T_\star(0)=\frac4{\sqrt{\beta^2-C^2}},\qquad
T_\star(\tfrac12)=\frac4\beta,
\]
and their ratio diverges as \(|C|\uparrow\beta\). This is a power-boundedness assertion, not an accuracy or convergence-efficiency guarantee.

## Assumptions and scope
Let \(q^n=(q_1^n,q_2^n)^{\mathsf T}\in\mathbb R^2\) and \(h>0\). For every integer \(n\ge1\), define \(q^{n+1}\) by
\[
q_1^{n+1}-2q_1^n+q_1^{n-1}
+\frac{h^2}{2}\left[A(q_1^{n+1}+q_1^{n-1})+2Cq_2^n\right]=0,
\]
\[
q_2^{n+1}-2q_2^n+q_2^{n-1}
+h^2\left[C\left(\omega q_1^n+\frac{1-\omega}{2}(q_1^{n+1}+q_1^{n-1})\right)+Bq_2^n\right]=0.
\]
The first equation uniquely determines \(q_1^{n+1}\), then the second determines \(q_2^{n+1}\). These equations are the two-scalar-mode specialization of the weighted splitting (3.1) in the motivating reference. Here power bounded means \(\sup_{n\ge0}\|q^n\|_2<\infty\) for *every* prescribed \((q^0,q^1)\in\mathbb R^2\times\mathbb R^2\). The word ``strict'' always refers to the open time-step condition; marginal stability at a double temporal root is not accepted. The stiffness matrix must be strictly positive definite; the singular limiting matrix is not included.

## Proof
Set \(t=h^2\), \(a=tA\), \(b=tB\), \(c=tC\), \(p=1+a/2\), and \(\eta=1-\omega\). With \(\Delta q^n=q^{n+1}-2q^n+q^{n-1}\), the two equations are equivalent to
\[
W\Delta q^n+tKq^n=0,\qquad
W=\begin{pmatrix}p&0\\\eta c/2&1\end{pmatrix}.
\]
This nonsymmetric modified mass is the reason the usual symmetric generalized-eigenvalue CFL test cannot simply be applied without further argument.

For a separated solution \(q^n=z^n v\), set \(x=2-z-z^{-1}\). The spatial dispersion polynomial is
\[
P(x)=\det(tK-xW)=px^2-Sx+R,
\quad S=a+pb-\frac{\eta c^2}{2},\quad R=ab-c^2>0.
\]
We have \(S>a+b>0\) when \(c\ne0\) (and \(S=a+pb>0\) when \(c=0\)). Its discriminant is the exact sum of squares
\[
S^2-4pR=\left(a-pb+\frac{\eta c^2}{2}\right)^2+(4+2a\omega)c^2.
\]
Consequently, when \(c\ne0\), the two roots \(0<x_-<x_+\) are distinct and real. Also
\[
x_-<\frac ap<2,
\]
because the discriminant's square root exceeds the absolute value of the first displayed square-root term. When \(c=0\), the system decouples and the two modal parameters are exactly \(a/p\in(0,2)\) and \(b>0\), so the subsequent conclusion also applies.

For a real positive modal parameter \(x\), the temporal characteristic equation is \(z^2-(2-x)z+1=0\). Both characteristic multipliers are distinct and on the unit circle precisely when \(0<x<4\). For \(x=4\), the double multiplier \(z=-1\) admits the linearly growing solution \(n(-1)^n\); for \(x>4\), a multiplier has modulus greater than one. Thus, because the smaller spatial root is always below two, all solutions are bounded precisely when \(x_+<4\). The distinct spatial eigenvectors for \(c\ne0\) diagonalize the second-order recurrence; for \(c=0\), its explicit coordinate decoupling supplies the same assertion even if the two modal parameters coincide.

Since \(p>0\) and \(x_-<2\), the condition \(x_+<4\) is equivalent to \(P(4)>0\). Direct expansion gives
\[
P(4)=(4+a)(4-b)+(1-2\omega)c^2
=16+4(A-B)t-\bigl[AB+(2\omega-1)C^2\bigr]t^2.
\]
For \(0\le\omega\le1\), \(AB+(2\omega-1)C^2\ge AB-C^2>0\). The last expression starts positive, is a strictly concave quadratic in \(t\), and has exactly one positive zero. Rationalizing that zero yields \(T_\star(\omega)\) as displayed. At the zero, \(x_+=4\) and the \(n(-1)^n\) mode occurs; above it, \(x_+>4\), proving necessity as well as sufficiency.

Finally, if \(C\ne0\), the denominator defining \(T_\star\) increases strictly with \(\omega\), establishing the reversal and the threshold at \(\omega=1/2\). For \(A=B=\beta\) and \(\omega=0\), substitution gives the stated divergent ratio.

## Verification
A standalone checker `verify.py` uses exact SymPy polynomial arithmetic to verify the characteristic polynomial, discriminant sum of squares, boundary factor and three closed-form critical time-step values. It also checks 880 finite parameter/weight/time-step combinations against independently evaluated modal roots. Execute `python verify.py` with SymPy 1.10 or newer. Expected last line: `VERIFY_OK: 5 symbolic identities, 3 exact boundary values, 880 independent modal grids`. The infinite-domain claims are proved above; the finite grid is only a reproducibility check.

As an exact illustration, set \(A=B=1\) and \(C=3/5\). Then \(T_\star(0)=5\), \(T_\star(1/2)=4\), and \(T_\star(1)=20/\sqrt{34}\). In particular, \(h^2=9/2\) is strictly power stable for \(\omega=0\) and unstable for \(\omega=1/2\) and \(\omega=1\).

## Relationship to prior work
Chung, Efendiev, Leung and Vabishchevich introduced precisely the weighted partially explicit wave scheme in their equation (3.1), analyzed the \(\omega=1\) case in Section 3 and the \(\omega=0\) case in Appendix A, and supplied sufficient energy conditions for stable time steps. The present result derives an *if-and-only-if* step ceiling and a continuous-weight coupling-sign transition for an orthogonal, unit-mass two-mode specialization. Neither the scheme nor the general principle of modal CFL analysis is claimed as new. The addition is the sharp, weight-dependent classification and the arbitrarily large separation possible near a rank-one stiffness limit. Standard central-difference modal CFL theory covers uncoupled scalar modes but does not by itself state this weighted, coupled two-equation frontier.

## Limitations
The result concerns a constant real symmetric positive-definite \(2\times2\) stiffness, orthogonal unit-mass subspaces, fixed step size, \(0\le\omega\le1\), exact arithmetic and linear undamped dynamics. It does not imply that larger admissible time steps improve phase accuracy, energy conservation in the usual physical norm or nonlinear stability. The constant-step result does not cover general mass-coupled finite-element spaces, arbitrary matrix block sizes, nonperiodic grids or indefinite stiffness. An independently discovered equivalent specialized condition elsewhere remains possible; no independent audit has been performed.

## References
1. E. T. Chung, Y. Efendiev, W. T. Leung and P. N. Vabishchevich, *Contrast-independent partially explicit time discretizations for multiscale wave problems*, first public arXiv version dated 2021-02-25, arXiv:2102.13198, especially Eq. (3.1), Section 3 and Appendix A. https://arxiv.org/abs/2102.13198 . Author-posted complete text: https://www.researchgate.net/publication/349682557_Contrast-independent_partially_explicit_time_discretizations_for_multiscale_wave_problems .
2. Background comparator: conventional central-difference CFL stability bound for an uncoupled oscillator, e.g. *Explicit Scheme Stability*, Altair Radioss documentation, https://2024.help.altair.com/2024/hwsolvers/rad/topics/solvers/rad/theory_dynamic_analysis_explicit_scheme_stability_r.htm .
