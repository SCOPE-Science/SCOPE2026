# Positive exact Strang-order mixing for two-state Markov generators and a sharp three-state obstruction

## Finding

A convex random choice between the two opposite palindromic Strang orders can reproduce **exactly**, for every positive step size, the transition matrix of an arbitrary two-state continuous-time Markov generator split into two parts. Its unique mixing probability depends only on the two total exit-rate scales. When these scales agree, a fair choice between the orders is exact even if the two generators do not commute. Three states are already enough to prevent such exactness: for a symmetric three-state path with its two edge generators split apart, both Strang orders have the same strictly excessive trace, so not even an affine (signed) mixture of the two orders equals the exact transition matrix.

## Assumptions and scope

Use **column** probability vectors and column-sum-zero generators. Let \(a,b,c,d,h>0\), and set
\[
A=\begin{pmatrix}-a&b\\a&-b\end{pmatrix},\qquad
B=\begin{pmatrix}-c&d\\c&-d\end{pmatrix},\qquad
s=a+b,\quad t=c+d.
\]
Define the forward and reversed palindromic propagators
\[
P_h=e^{hA/2}e^{hB}e^{hA/2},\qquad
Q_h=e^{hB/2}e^{hA}e^{hB/2},
\]
and dimensionless coefficients
\[
u_h=\frac{\sinh(th/2)}{\sinh((s+t)h/2)},\qquad
v_h=\frac{\sinh(sh/2)}{\sinh((s+t)h/2)},\qquad
w_h=\frac{\frac{s}{s+t}-v_h}{1-u_h-v_h}.
\]
Then \(0<w_h<1\) and
\[
\boxed{\ e^{h(A+B)}=w_hP_h+(1-w_h)Q_h\ }.
\]
If \(s=t\), then \(w_h=1/2\). If \(b/s\ne d/t\), the coefficient \(w_h\) is uniquely determined by this identity. If \(b/s=d/t\), then \(A\) and \(B\) commute and the two Strang products already equal the exact propagator individually, so uniqueness is not asserted.

For the sharp three-state contrast, set
\[
A_3=\begin{pmatrix}-1&1&0\\1&-1&0\\0&0&0\end{pmatrix},\quad
B_3=\begin{pmatrix}0&0&0\\0&-1&1\\0&1&-1\end{pmatrix},
\]
with \(P_{3,h}=e^{hA_3/2}e^{hB_3}e^{hA_3/2}\) and \(Q_{3,h}=e^{hB_3/2}e^{hA_3}e^{hB_3/2}\). For every \(h>0\),
\[
\boxed{\ \operatorname{tr}P_{3,h}=\operatorname{tr}Q_{3,h}
=\operatorname{tr}e^{h(A_3+B_3)}+\frac{(1-e^{-h})^4}{4}.\ }
\]
Consequently no \(w\in\mathbb R\) has \(e^{h(A_3+B_3)}=wP_{3,h}+(1-w)Q_{3,h}\). The full generator \(A_3+B_3\) is irreducible and symmetric; each split edge generator is a valid (reducible) Markov generator.

## Proof

**Binary transition structure.** The first-state probability \(x\in[0,1]\) under \(e^{\tau A}\) evolves by the affine map
\[
x\longmapsto p_A+e^{-s\tau}(x-p_A),\qquad p_A=b/s.
\]
Likewise \(B\) has \(p_B=d/t\) and decay rate \(t\). Any composition of the stated binary Markov semigroups has the same scalar contraction factor \(q=e^{-(s+t)h}\). An affine contraction with fixed point \(p\) is \(x\mapsto p+q(x-p)\), and is determined by \(p\) and \(q\).

Multiplication of the scalar affine maps gives the stationary points
\[
p_P=p_A+u_h(p_B-p_A),\qquad
p_Q=p_B+v_h(p_A-p_B).
\]
For example, writing \(r=e^{-sh/2}\) and \(k=e^{-th}\), the coefficient of \(p_B-p_A\) in the first palindromic order is
\[
\frac{r(1-k)}{1-r^2k}
=\frac{\sinh(th/2)}{\sinh((s+t)h/2)}=u_h.
\]
The exact combined generator has stationary first-state probability
\[
p_*=\frac{b+d}{s+t}=p_A+\frac{t}{s+t}(p_B-p_A).
\]
For \(X=(s+t)h/2>0\), strict convexity of \(\sinh\), with \(\sinh(0)=0\), implies
\[
0<u_h<\frac{t}{s+t},\qquad 0<v_h<\frac{s}{s+t}.
\]
In particular \(1-u_h-v_h>0\) and \(0<w_h<1\). By direct substitution, the weighted average of the two palindromic stationary intercepts has the exact combined intercept:
\[
w_h p_P+(1-w_h)p_Q=p_*.
\]
Because both palindromic maps have slope \(q\), their convex mixture also has slope \(q\). It therefore coincides with the exact semigroup on every probability vector, hence as a matrix on \(\mathbb R^2\). If \(p_A\ne p_B\), then \(p_P-p_Q=(u_h+v_h-1)(p_B-p_A)\ne0\), so the weight is unique. If \(p_A=p_B\), both generators are scalar multiples of the same rank-one Markov generator and commute. Finally, when \(s=t\), one has \(u_h=v_h\) and hence \(w_h=1/2\).

**Three-state trace obstruction.** Put \(z=e^{-h}\in(0,1)\). The two edge generators satisfy \(A_3^2=-2A_3\) and \(B_3^2=-2B_3\), giving exact exponentials
\[
e^{hA_3/2}=I+\tfrac{1-z}{2}A_3,\qquad
e^{hB_3}=I+\tfrac{1-z^2}{2}B_3,
\]
and analogous reversed expressions. Exact multiplication yields
\[
\operatorname{tr}P_{3,h}=\operatorname{tr}Q_{3,h}
=\frac{(1+z^2)(5+z^2)}{4}.
\]
The combined generator is the negative path-graph Laplacian, whose eigenvalues are \(0,-1,-3\), hence
\[
\operatorname{tr}e^{h(A_3+B_3)}=1+z+z^3.
\]
Subtracting gives the *identity* \((1+z^2)(5+z^2)/4-(1+z+z^3)=(1-z)^4/4>0\). Since the trace of every affine mixture of the two products equals their common trace, equality with the exact propagator is impossible. All claims hold at every positive step size; no asymptotic or finite-search argument is needed.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 standard library only. The program checks the binary identity on 300 reproducible positive-rate sets and 15 equal-rate examples, verifies the three-state trace identities with exact rational arithmetic, and checks the strict trace defect numerically at four positive step sizes. Its five distinct exact interpolation nodes establish the two polynomial trace identities of degree at most four. The analytic proof above, not the numerical experiments, establishes the universal binary assertion.

## Relationship to prior work

Battestini, Caliari and Cassini (2026, arXiv:2610.07989v1) analyze Lie–Trotter and Strang splitting errors of noncommuting exponential integrators, including errors of individual fixed orders. Li, Liu and Wan (2026, arXiv:2603.27654) study quasi-random operator ordering in multiphysics splitting, emphasizing convergence and accuracy rather than the exact positive two-state identity. Eisenmann and Stillfjord (2022 preprint, arXiv:2210.05375) analyze a different randomized operator splitting with finite-order convergence. These works motivate the question but, in the material checked, do not state the exact rate-only positive Strang-order mixture or the three-state trace obstruction. This comparison is not a claim of exhaustive historical priority.

## Limitations

The identity concerns **one-step transition matrices** of a two-state continuous-time Markov chain with positive component rates; it does not give pathwise equality of full continuous-time sample paths. The exceptional commuting case has nonunique mixing weights. The three-state obstruction concerns the two *specified* palindromic orders for the *specified* edge split; it does not exclude other integrator families, multistage randomizations, or additional positive mixtures. This is an exact-arithmetic statement; finite-precision conditioning and computational savings are not analyzed. An older equivalent result on low-dimensional Markov splitting may exist and requires independent priority verification.

## References

1. L. Battestini, M. Caliari and F. Cassini, *Analysis of split exponential integrators for semilinear problems with noncommuting operators*, arXiv:2610.07989v1, first public October 6, 2026. https://arxiv.org/abs/2610.07989
2. Y. Li, L. Liu and J. Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation*, arXiv:2603.27654, first public March 29, 2026. https://arxiv.org/abs/2603.27654
3. M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375, first public 2022. https://arxiv.org/abs/2210.05375
