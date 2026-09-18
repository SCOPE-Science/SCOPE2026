# Exact conditioning-dependent stability threshold for affine reflected gradient

## Statement

Let
\[
B(x)=Mx+b,\qquad M\in\mathbb R^{n\times n},
\]
with
\[
\frac{M+M^\top}{2}\succeq \sigma I,\qquad \|M\|_2\le L,
\qquad 0<\sigma\le L.
\]
Set
\[
q:=\frac{\sigma}{L}\in(0,1].
\]
Consider the unconstrained reflected-gradient iteration
\[
x_{k+1}=x_k-\lambda B(2x_k-x_{k-1}).
\]
For affine operators this is exactly optimistic gradient descent,
\[
x_{k+1}=x_k-2\lambda B(x_k)+\lambda B(x_{k-1}).
\]

Define \(\tau_*(q)\in[1/\sqrt3,2/3]\) as the unique solution of
\[
\boxed{
3\tau^3+4q\tau^2-\tau-2q=0
}
\]
in that interval. Equivalently,
\[
\boxed{
q=\frac{\tau_*(3\tau_*^2-1)}{2(1-2\tau_*^2)}.
}
\]
Then:

1. For every affine operator satisfying the assumptions above, every initialization converges R-linearly to the unique zero of \(B\) whenever
   \[
   \boxed{0<\lambda L<\tau_*(q).}
   \]
2. The threshold is sharp as a universal strict stability bound. At
   \(\lambda L=\tau_*(q)\), the two-dimensional normal operator
   \[
   \boxed{
   M_q=L
   \begin{pmatrix}
   q&-\sqrt{1-q^2}\\
   \sqrt{1-q^2}&q
   \end{pmatrix}
   }
   \]
   has strong-monotonicity modulus exactly \(\sigma=qL\), norm exactly \(L\), and a reflected-gradient characteristic root on the unit circle. Generic initial states therefore fail to converge.

The threshold interpolates monotonically between the sharp monotone affine constant and the scalar/symmetric endpoint:
\[
\lim_{q\downarrow0}\tau_*(q)=\frac1{\sqrt3},
\qquad
\tau_*(1)=\frac23.
\]
In particular, every positive strong-monotonicity margin strictly enlarges the affine stability range beyond \(1/(\sqrt3 L)\).

## Proof

Strong monotonicity makes \(M\) nonsingular, so \(B\) has a unique zero \(z=-M^{-1}b\). With \(e_k=x_k-z\), the iteration is
\[
e_{k+1}=(I-2\lambda M)e_k+\lambda M e_{k-1}.
\]
For a spectral value \(\mu\in\operatorname{spec}(M)\), a characteristic multiplier \(r\) satisfies
\[
\boxed{
(r^2-r)+\lambda(2r-1)\mu=0.
}
\]
This remains true without diagonalizability: the characteristic determinant of the companion state matrix is
\[
\det\bigl((r^2-r)I+\lambda(2r-1)M\bigr),
\]
so its zeros are the union of the roots of the scalar equations over \(\operatorname{spec}(M)\).

Scale
\[
\zeta=\frac{\mu}{L},\qquad \tau=\lambda L.
\]
The matrix assumptions imply the spectral enclosure
\[
\boxed{
\operatorname{Re}\zeta\ge q,\qquad |\zeta|\le1.
}
\]
Indeed, if \(Mv=\mu v\) for a complex eigenvector \(v\), then
\[
\operatorname{Re}\mu
=\frac{\operatorname{Re}(v^*Mv)}{\|v\|^2}\ge\sigma,
\qquad
|\mu|\le\|M\|_2\le L.
\]

A loss of Schur stability can occur only when a characteristic root reaches \(|r|=1\). Put \(r=e^{i\theta}\), \(c=\cos\theta\). Solving the characteristic equation for \(\zeta\) gives
\[
\zeta(r)=-\frac{r^2-r}{\tau(2r-1)}.
\]
Direct calculation yields
\[
\operatorname{Re}\zeta(r)
=\frac{A(c)}{\tau},
\qquad
|\zeta(r)|^2=\frac{B(c)}{\tau^2},
\]
where
\[
A(c)=\frac{(1-c)(1-2c)}{5-4c},
\qquad
B(c)=\frac{2(1-c)}{5-4c}.
\]
Because \(q>0\), admissibility forces \(c\le1/2\). Define
\[
t:=\sqrt{B(c)}\in\left[\frac1{\sqrt3},\frac23\right].
\]
Solving \(t^2=B(c)\) gives
\[
c(t)=\frac{5t^2-2}{2(2t^2-1)}.
\]
At a unit-circle contact, \(|\zeta|\le1\) requires \(\tau\ge t\), while \(\operatorname{Re}\zeta\ge q\) requires
\[
\tau\le\frac{A(c)}q.
\]
Hence a contact at parameter \(t\) is feasible only if
\[
q\le\phi(t):=\frac{A(c(t))}{t}
=\frac{t(3t^2-1)}{2(1-2t^2)}.
\]
Moreover,
\[
\phi'(t)
=\frac{(1-t^2)(6t^2-1)}{2(1-2t^2)^2}>0
\quad
\text{for }t\in\left[\frac1{\sqrt3},\frac23\right],
\]
and
\[
\phi(1/\sqrt3)=0,\qquad \phi(2/3)=1.
\]
Thus there is a unique \(t=\tau_*(q)\) such that \(\phi(t)=q\). Any unit-circle contact must obey
\[
\tau\ge t\ge\tau_*(q),
\]
so no characteristic multiplier can reach the unit circle for \(0<\tau<\tau_*(q)\).

For sufficiently small positive \(\tau\), the two characteristic roots are uniformly inside the unit disk: one is
\[
r_1=1-\tau\zeta+O(\tau^2)
\]
with \(\operatorname{Re}\zeta\ge q>0\), and the other is
\[
r_2=\tau\zeta+O(\tau^2).
\]
By continuity, and because there is no unit-circle crossing below \(\tau_*(q)\), every multiplier remains strictly inside the disk throughout that interval. In finite dimension the companion state matrix therefore has spectral radius below one, which implies R-linear convergence of \((e_k,e_{k-1})\), even when \(M\) is nonnormal or defective.

Finally, eliminating \(c\) at the first contact gives
\[
q=\phi(\tau_*)
=\frac{\tau_*(3\tau_*^2-1)}{2(1-2\tau_*^2)},
\]
which is equivalent to the cubic in the statement.

For sharpness, let
\[
\zeta_q=q+i\sqrt{1-q^2}.
\]
At \(\tau=\tau_*(q)\), the construction above supplies a unit-modulus root \(r\) mapped exactly to \(\zeta_q\). The matrix \(M_q\) has eigenvalues \(L\zeta_q\) and \(L\overline{\zeta_q}\), symmetric part \(qLI\), and norm \(L\). Hence its companion state matrix has a unit-circle eigenvalue, proving that the universal strict threshold cannot be increased. At \(q=1\), this reduces to \(M=LI\), \(\tau_*=2/3\), with the boundary multiplier \(r=-1\).

## Quantitative consequences

The threshold is strictly increasing with \(q=\sigma/L\). For example,
\[
q=\frac12
\quad\Longrightarrow\quad
\tau_*(q)\approx0.646488352862241.
\]
Thus the exact universal affine step ceiling is about \(0.64649/L\), rather than the monotone-class value \(1/(\sqrt3L)\approx0.57735/L\).

The September 2026 source paper tests strong monotonicity on
\[
B=(\sigma I+J),\qquad \sigma=2,
\qquad L=\sqrt5,
\]
where \(J\) is the planar quarter-turn. Here
\[
q=\frac2{\sqrt5},
\qquad
\tau_*\approx0.663636079378931,
\]
so the exact affine stability threshold is
\[
\boxed{
\lambda_*\approx0.296787077162547.
}
\]
The source paper's general affine monotone theorem already certifies
\(\lambda<1/(\sqrt3L)\approx0.258199\) on this instance. The conditioning-dependent result enlarges that exact affine range by about 14.95%. Its strong-monotonicity Lyapunov theorem uses the much smaller certified step \(\lambda=1/(32\sigma)=1/64\) for the same example; \(\lambda_*\) is approximately 18.99 times larger. This comparison concerns the affine pure reflected-gradient specialization only and does not enlarge the source theorem for nonlinear, projected, or filtered problems.

## Relation to earlier OGD/PRG theory

Malitsky (2015) proved R-linear convergence of projected reflected gradient under strong monotonicity, but did not give the conditioning-dependent sharp affine stability boundary above.

Anagnostides and Panageas (2021/2022) gave a sharp \(2/(3\widehat L)\) learning-rate boundary for optimistic gradient descent under the different hypothesis that the operator is strongly monotone and \(1/\widehat L\)-cocoercive. Strong monotonicity and \(L\)-Lipschitzness alone imply only
\[
\langle B(x)-B(y),x-y\rangle
\ge \frac{\sigma}{L^2}\|B(x)-B(y)\|^2,
\]
so their assumption can be invoked with \(\widehat L=L^2/\sigma\), yielding the sufficient step
\[
\lambda<\frac{2\sigma}{3L^2}=\frac{2q}{3L}.
\]
That does not cover the present sharp affine threshold. Conversely, their theorem applies to nonlinear cocoercive operators and is not subsumed by this affine result.

Huang and Zhang (2021/2026 revision) analyze strongly monotone Lipschitz VIs and include an OGDA direction in an accelerated extra-point framework, but their displayed OGDA guarantee uses separately tuned current-gradient and optimism coefficients rather than the pure reflected-gradient choice analyzed here.

## Limitations

The result is finite-dimensional, affine, unconstrained, constant-step, and deterministic. It does not establish a larger step range for nonlinear operators, projected variational inequalities, filtered reflected methods, adaptive steps, stochastic errors, or finite-precision arithmetic. The threshold is a sharp universal stability boundary; it is not claimed to be the stepsize that minimizes the worst-case contraction factor. The parameters \(\sigma\) and \(L\) are assumed known if the formula is used for tuning.

The spectral/root-locus calculation is elementary, and related control-theoretic OGD analyses are extensive. Originality is therefore asserted only to the best of our knowledge: the claimed contribution is the explicit sharp interpolation \(\tau_*(\sigma/L)\), its cubic characterization, and the matching rotation-dilation witness for the class of affine operators with symmetric part at least \(\sigma I\) and operator norm at most \(L\).

## Reproducibility

`artifacts/verify_threshold.py` symbolically verifies the unit-circle elimination, the cubic equation, monotonicity and endpoint identities, the \(q=1/2\) contact, the source-paper \((\sigma,L)=(2,\sqrt5)\) comparison, and the scalar \(q=1\) boundary. `artifacts/verification.txt` contains its executed output.

## References

1. Y. Shehu, *A Parameter-Free Adaptive Reflected Gradient Method for Monotone Variational Inequalities*, arXiv:2609.18355v1 (2026). https://arxiv.org/abs/2609.18355v1
2. Y. Malitsky, *Projected Reflected Gradient Methods for Monotone Variational Inequalities*, SIAM Journal on Optimization 25(1), 502--520 (2015). https://doi.org/10.1137/14097238X
3. I. Anagnostides and I. Panageas, *Frequency-Domain Representation of First-Order Methods: A Simple and Robust Framework of Analysis*, arXiv:2109.04603; SOSA 2022. https://arxiv.org/abs/2109.04603
4. K. Huang and S. Zhang, *A Unifying Framework of Accelerated First-Order Approach to Strongly Monotone Variational Inequalities*, arXiv:2103.15270. https://arxiv.org/abs/2103.15270
5. P. E. Maing\'e and M. L. Gobinddass, *Convergence of One-Step Projected Gradient Methods for Variational Inequalities*, Journal of Optimization Theory and Applications 171, 146--168 (2016). https://doi.org/10.1007/s10957-016-0972-4
6. J. Yang and H. Liu, *A Modified Projected Gradient Method for Monotone Variational Inequalities*, Journal of Optimization Theory and Applications 179, 197--211 (2018). https://doi.org/10.1007/s10957-018-1351-0
