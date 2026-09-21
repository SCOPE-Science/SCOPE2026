# Sharp Euclidean damping frontier for weighted Jacobi on 2×2 SPD systems

## Result

Let \(A\in\mathbb R^{n\times n}\) be symmetric positive definite, let
\(D=\operatorname{diag}(A)\), and consider weighted Jacobi
\[
 e^+ = T_\omega e,
 \qquad
 T_\omega=I-\omega D^{-1}A,
 \qquad \omega>0.
\]
Although \(D^{-1}A\) is similar to the SPD matrix \(D^{-1/2}AD^{-1/2}\), so sufficiently small positive damping always gives spectral convergence, Euclidean one-step contractivity can behave differently because \(D^{-1}A\) is generally nonnormal.

### Theorem 1 — exact Euclidean safety interval in any dimension

Define
\[
 \omega_E(A):=\lambda_{\min}\!\left(A^{-1}D+DA^{-1}\right).
\]
Then
\[
 \boxed{\ \|I-\omega D^{-1}A\|_2\le 1
 \iff 0<\omega\le \omega_E(A).\ }
\]
Here the right-hand interval is understood to be empty when \(\omega_E(A)\le0\). Thus a positive relaxation making one weighted-Jacobi step Euclidean nonexpansive exists **if and only if**
\[
 A^{-1}D+DA^{-1}\succ0.
\]
In particular, asymptotic convergence for small damping does not imply that any positive damping can make every single step Euclidean nonexpansive.

### Theorem 2 — exact 2×2 formula

For
\[
 A=\begin{pmatrix}a&c\\c&d\end{pmatrix}\succ0,
\]
Theorem 1 reduces to
\[
 \boxed{
 \omega_E(A)=
 \frac{2ad-|c|(a+d)}{ad-c^2}.
 }
\]
Consequently standard Jacobi (\(\omega=1\)) is Euclidean nonexpansive exactly when
\[
 |c|\le \min\{a,d\}.
\]

### Theorem 3 — sharp condition-number robust frontier in dimension two

Fix a spectral condition number \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\ge1\), and define the signed robust Euclidean safety margin
\[
 \Omega_2(\kappa)
 :=\inf\{\omega_E(A): A\in\mathbb R^{2\times2},\ A\succ0,\ \kappa_2(A)=\kappa\}.
\]
Then
\[
 \boxed{
 \Omega_2(\kappa)=
 \begin{cases}
 1+\kappa^{-1}, & 1\le\kappa\le3,\\[4pt]
 \dfrac{14\kappa-\kappa^2-1}{8\kappa}, & \kappa\ge3.
 \end{cases}}
\]
The bound is attained for every \(\kappa\). Hence:

1. A single positive damping depending only on \(\kappa\) can make **every** 2×2 SPD system of that condition number Euclidean nonexpansive exactly when
   \[
   \boxed{\kappa<7+4\sqrt3\approx13.9282032303.}
   \]
   Whenever this holds, every
   \(0<\omega\le\Omega_2(\kappa)\) is universally safe, and no larger common \(\omega\) is.

2. At and above \(\kappa=7+4\sqrt3\), there exists a 2×2 SPD matrix for which
   \[
   \|I-\omega D^{-1}A\|_2>1
   \qquad\text{for every }\omega>0.
   \]
   Thus arbitrarily strong damping cannot remove all Euclidean transient amplification, even though a sufficiently small damping still makes the iteration spectrally convergent.

3. Undamped Jacobi \((\omega=1)\) is universally Euclidean nonexpansive over the 2×2 condition-number class exactly when
   \[
   \boxed{\kappa\le3+2\sqrt2\approx5.82842712475.}
   \]
   Damping therefore enlarges the robust Euclidean-safety range from \(3+2\sqrt2\) up to, but not including, \(7+4\sqrt3\).

For example, at \(\kappa=9\), the sharp common safe ceiling is
\(\Omega_2(9)=11/18\): standard Jacobi can have a one-step Euclidean expansion, whereas every \(0<\omega\le11/18\) is safe for all 2×2 SPD systems with condition number 9.

## Proof

Set \(B=D^{-1}A\). For \(\omega>0\),
\[
 \|I-\omega B\|_2\le1
 \iff
 (I-\omega B)^T(I-\omega B)\preceq I.
\]
After expanding and dividing by \(\omega\), this is
\[
 B+B^T-\omega B^TB\succeq0.
\]
Congruence by \(B^{-T}\) and \(B^{-1}\) gives the equivalent condition
\[
 B^{-T}+B^{-1}-\omega I\succeq0.
\]
Since \(B^{-1}=A^{-1}D\), Theorem 1 follows immediately.

For the 2×2 case write
\[
 B=\begin{pmatrix}1&u\\v&1\end{pmatrix},
 \qquad u=\frac ca,
 \quad v=\frac cd,
 \quad q=uv=\frac{c^2}{ad}<1.
\]
Then
\[
 B^{-1}+B^{-T}
 =\frac1{1-q}
 \begin{pmatrix}
 2&-(u+v)\\
 -(u+v)&2
 \end{pmatrix}.
\]
Its smaller eigenvalue is
\[
 \frac{2-|u+v|}{1-q}
 =\frac{2ad-|c|(a+d)}{ad-c^2},
\]
proving Theorem 2.

For Theorem 3, scale \(A\) so its eigenvalues are \(1\) and \(\kappa\), which does not change \(D^{-1}A\). Put \(z=|c|\). Rotation of the eigenbasis gives exactly
\[
 0\le z\le\frac{\kappa-1}{2},
 \qquad
 a+d=\kappa+1,
 \qquad
 ad=\kappa+z^2.
\]
Substitution into Theorem 2 yields the convex quadratic
\[
 \omega_E(z)
 =2+\frac{2z^2-(\kappa+1)z}{\kappa}.
\]
Its unconstrained minimizer is \(z=(\kappa+1)/4\). This lies in the allowed interval exactly when \(\kappa\ge3\). Therefore:

- for \(1\le\kappa\le3\), the minimum occurs at \(z=(\kappa-1)/2\), giving \(1+1/\kappa\);
- for \(\kappa\ge3\), the minimum occurs at \(z=(\kappa+1)/4\), giving
  \((14\kappa-\kappa^2-1)/(8\kappa)\).

The second branch vanishes at the larger root of
\(\kappa^2-14\kappa+1=0\), namely \(7+4\sqrt3\), proving the no-positive-damping frontier. Requiring \(\Omega_2(\kappa)\ge1\) gives the larger root of
\(\kappa^2-6\kappa+1=0\), namely \(3+2\sqrt2\), proving the standard-Jacobi frontier. The extremizing values of \(z\) above are realized by rotations of \(\operatorname{diag}(1,\kappa)\), so all bounds are sharp.

## Relation to prior literature

Classical treatments develop Jacobi and weighted-Jacobi convergence primarily through the spectral radius or through norms naturally induced by the diagonal scaling. Saad's treatment places Jacobi among the basic stationary iterative methods. Varga and Young are broad classical references for matrix iterative analysis and relaxation methods. Arioli and Romani (1985) relate condition numbers to the **spectral radius** of the Jacobi matrix under additional diagonal-dominance assumptions. Hadjidimos and Neumann (1998) explicitly study Euclidean-norm optimization for SOR/MSOR operators, illustrating that Euclidean transient behavior is a distinct question from spectral-radius optimization.

The literature search located no statement of the exact fixed-matrix criterion
\(\lambda_{\min}(A^{-1}D+DA^{-1})\), the 2×2 robust envelope \(\Omega_2(\kappa)\), or the two sharp thresholds \(3+2\sqrt2\) and \(7+4\sqrt3\) in the weighted-Jacobi Euclidean-contractivity setting. This originality claim is to the best of our knowledge; see `REVIEW.md` for access limitations.

## Computational model and limitations

The result concerns exact arithmetic, real SPD matrices, simultaneous weighted-Jacobi iteration, and Euclidean one-step error amplification. The general fixed-matrix criterion is dimension-independent, but the condition-number-only sharp envelope and its two thresholds are proved only in dimension two. The result does not claim floating-point stability, optimal asymptotic convergence rate, smoothing efficiency, or performance superiority. For \(n>2\), a condition-number-only analogue is not established here.

The verification artifact checks the fixed-matrix identity, the sharp two-dimensional envelope over dense rotation grids, the threshold behavior, and an explicit ill-conditioned example where every positive damping has Euclidean norm above one while small damping remains spectrally convergent.

## References

1. Y. Saad, *Iterative Methods for Sparse Linear Systems*, 2nd ed., SIAM, 2003, Chapter 4. https://doi.org/10.1137/1.9780898718003.ch4
2. R. S. Varga, *Matrix Iterative Analysis*, 2nd ed., Springer, 2000. https://doi.org/10.1007/978-3-642-05156-2
3. D. M. Young, *Iterative Solution of Large Linear Systems*, Academic Press, 1971; Dover reprint, 2003. https://old.maa.org/press/maa-reviews/iterative-solution-of-large-linear-systems
4. M. Arioli and F. Romani, “Relations between condition numbers and the convergence of the Jacobi method for real positive definite matrices,” *Numerische Mathematik* 46 (1985), 31–42. https://doi.org/10.1007/BF01400253
5. A. Hadjidimos and M. Neumann, “Euclidean Norm Minimization of the SOR Operators,” *SIAM Journal on Matrix Analysis and Applications* 19 (1998), 191–204. https://doi.org/10.1137/S0895479896300498
