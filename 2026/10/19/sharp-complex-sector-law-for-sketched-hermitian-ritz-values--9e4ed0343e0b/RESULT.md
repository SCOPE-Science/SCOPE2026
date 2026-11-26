# Sharp angular bound for ordinary sketched Hermitian Ritz values

## Finding

Let \(A=A^*\in\mathbb C^{n\times n}\) satisfy \(0<\mu I\preceq A\preceq LI\), and put \(\kappa=L/\mu\). Let \(B\in\mathbb C^{n\times m}\) have full column rank, with \(1\le m\le n\). Let \(S\in\mathbb C^{s\times n}\) preserve squared norms on \(\mathcal U=\operatorname{range}([B,AB])\) to distortion \(0\le\varepsilon<1\):
\[
(1-\varepsilon)\|x\|^2\le \|Sx\|^2\le(1+\varepsilon)\|x\|^2\qquad (x\in\mathcal U).
\]
For every eigenvalue \(\lambda\) of the ordinary sketched Rayleigh–Ritz matrix \(M=(SB)^\dagger(SAB)\), if \(\varepsilon<2\sqrt\kappa/(\kappa+1)\),
\[
|\arg\lambda|\le
\arcsin\!\left(\frac{\varepsilon(\kappa-1)}{2\sqrt\kappa\sqrt{1-\varepsilon^2}}\right).
\]
The argument is the principal argument and the angle is strictly less than \(\pi/2\). For each \(\kappa>1\) and each strictly positive distortion in this range, both signs of the extremal angle are attained by one-vector trials, including with a dimension-reducing \(2\times3\) complex sketch. For \(\kappa=1\), \(M=\mu I\). The original contribution asserted here is the sharp angular refinement, not the strict right-half-plane threshold itself.

## Proof

Write \(T=S^*S\). The embedding gives \(B^*TB\succ0\). For any eigenpair \(My=\lambda y\) with \(y\ne0\), let \(u=By/\|By\|\) and left-multiply the generalized eigenvalue equation by \(y^*\) to obtain
\[
\lambda=\frac{u^*TAu}{u^*Tu}.
\]
Thus no diagonalizability assumption is needed. Put \(a=u^*Au>0\) and \(b=\|Au-au\|\); if \(b=0\) the quotient is \(a\). Otherwise \(v=(Au-au)/b\) is unit and perpendicular to \(u\), and \(u,v\in\mathcal U\). In this ordered orthonormal basis, let \(h=H_{11}\) and \(z=H_{12}\), where \(H\) is the two-dimensional compression of \(T-I\). Since \(H\) is Hermitian and \(\|H\|\le\varepsilon\), its first column gives \(h^2+|z|^2\le\varepsilon^2\). The quotient is
\[
\lambda=a+\frac{b z}{1+h}.
\]
The denominator is positive, and the identity
\[
\varepsilon^2(1+h)^2-(1-\varepsilon^2)(\varepsilon^2-h^2)=(h+\varepsilon^2)^2
\]
shows that the quotient lies in the disk with real center \(a\) and radius \(R=b\varepsilon/\sqrt{1-\varepsilon^2}\). This disk of possible quotients for the fixed trial direction is exact: set \(h=-\varepsilon^2\) and take any \(z\) of modulus at most \(\varepsilon\sqrt{1-\varepsilon^2}\). The traceless completion
\[
H=\begin{pmatrix}h&z\\\overline z&-h\end{pmatrix}
\]
has norm at most \(\varepsilon\). Extend it by zero off the plane when necessary and take a square root of \(I+H\) as a sketch. For the one-vector trial with basis \(u\), every point of the disk is then an actual Ritz value. When \(R<a\), all disk points have positive real part, and the extreme angle satisfies \(\sin\Theta=R/a\) by tangency to the disk (with angle zero if \(R=0\)).

The positive-semidefinite polynomial \((A-\mu I)(LI-A)\succeq0\) gives
\[
\frac{b^2}{a^2}\le \frac{\mu+L}{a}-\frac{\mu L}{a^2}-1\le\frac{(L-\mu)^2}{4\mu L}.
\]
The second inequality is the maximum of this quadratic in \(1/a\), reached at \(a=2\mu L/(\mu+L)\). The subcritical distortion condition ensures \(R<a\) uniformly, since \(1+(\kappa-1)^2/(4\kappa)=(\kappa+1)^2/(4\kappa)\). Combining the inequalities yields the angular bound.

For equality, use \(A_0=\operatorname{diag}(\mu,L)\) and \(u=(\sqrt L,\sqrt\mu)^{\mathsf T}/\sqrt{L+\mu}\). The spectral inequality is then an equality. Realize a tangent point of the disk by the explicit traceless completion above, representing \(H\) in the \((u,v)\) basis before taking the square root to obtain the sketch \(S_0\). The two tangent points are conjugate. A third diagonal eigenvalue in \([\mu,L]\), a zero appended to the trial vector and the sketch \([S_0\ \ 0]\) give the dimension-reducing witness without changing \(\mathcal U\) on the first two coordinates. As a concrete case in the original eigenbasis, for \(A_0=\operatorname{diag}(1,9)\) and \(u=(3,1)^{\mathsf T}/\sqrt{10}\) take
\[
T_0=\begin{pmatrix}1&(-1+2\sqrt2\,i)/15\\(-1-2\sqrt2\,i)/15&1\end{pmatrix}.
\]
Its eigenvalues are \(4/5,6/5\). Direct evaluation gives \(u^*T_0u=24/25\) and \(u^*T_0A_0u=8/5+8\sqrt2\,i/25\). The resulting Ritz value \((5+\sqrt2\,i)/3\) has argument \(\arctan(\sqrt2/5)\), equal to the claimed bound at \(\kappa=9,\varepsilon=1/5\).

## Prior coverage and scope of the angular refinement

The sharp strict-positivity frontier and its failure witnesses are already consequences of the earlier sketched harmonic Ritz result [4], despite the different estimators for a fixed \(A,B\). In that result set the input matrix to \(A^{-1}\) and the trial basis to \(AB\). Its image basis is then \(B\), the joint embedded space is unchanged, and the spectral ratio remains \(\kappa\) using the reciprocal endpoints. In the prior normalization \(G=(S\,\mathrm{image})^*(S\,\mathrm{trial})\), \(F=(S\,\mathrm{image})^*(S\,\mathrm{image})\), the harmonic matrix is \(G^{-1}F=M^{-1}\) whenever defined. A singular harmonic denominator is equivalent to a zero eigenvalue of \(M\); for a nonzero eigenvalue, inversion preserves the sign of its real part. Thus the prior exact singular and negative examples also transfer. The present result strengthens the strict-positivity statement below that *known* frontier by giving the optimal angular location, not just its sign.

The ordinary sketched Ritz estimator and subspace-embedding setting are established in [1,2], and [2, §6.8] notes nonreal values for Hermitian inputs. The sharp residual-to-Rayleigh-quotient ratio for a positive operator is classical operator-angle mathematics; see [3] for the antieigenvalue and product-accretivity context. Here the extra step for the angular refinement is to keep the exact feasible complex perturbations of the normalized Ritz quotient, then show that the extreme angle remains attainable by a sketch on the joint space. Possible equivalent results in older matrix-angle or product numerical-range literature are not ruled out by these comparisons.

The result uses exact arithmetic. It does not imply finite-precision behavior, probability under a sketch distribution, eigenvector error bounds, or Krylov convergence. Embedding the trial space alone is not the hypothesis. The inequality applies in the real setting too, but the attainment assertion uses complex sketches, not a real one-vector subclass.

## Verification

The proof above establishes the universal result. The unchanged companion `verify.py` checks the explicit algebraic example, samples finite complex two-mode cases, and also checks example zero and negative Ritz values at or beyond the previously known frontier. The latter checks are consistency tests, not evidence of originality. No finite sample is used to prove the angular bound.

## References

1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1, §§2.4 and 3. https://arxiv.org/html/2604.07158v1
2. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2, §§6.3, 6.6 and 6.8. https://arxiv.org/html/2111.00113v2
3. K. Gustafson, *The angle of an operator and positive operator products*, Bulletin of the American Mathematical Society 74 (1968), 488–492. DOI:10.1090/S0002-9904-1968-11974-3.
4. *Sharp embedding-distortion frontier for sketched harmonic Ritz positivity*, Resultary `2026/10/12/SCOPE-sharp-embedding-distortion-frontier-for-sketched-harmonic-ritz-p--f6a519d77ab4`, Finding, Assumptions and scope, and Proof §§2–3. https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-sharp-embedding-distortion-frontier-for-sketched-harmonic-ritz-p--f6a519d77ab4/RESULT.md
