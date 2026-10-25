# Sharp amplification threshold for projection-blended positive propagators

## Finding

For every finite-dimensional real or complex Hilbert space, every orthogonal projection \(P\), and every pair of self-adjoint positive semidefinite propagators \(F,G\) with \(0\preceq F,G\preceq qI\), the projection-blended operator
\[
H=G+(F-G)P=FP+G(I-P)
\]
satisfies the **sharp dimension-free inequality**
\[
\boxed{\|H\|_2\le Cq,\qquad C=\frac{1+\sqrt 2}{2}.}
\]
The bound is attained in dimension two by rank-one orthogonal projectors. Consequently the exact largest uniform contraction budget for all such choices is
\[
\boxed{q_{\mathrm{crit}}=\frac{2}{1+\sqrt2}=2(\sqrt2-1).}
\]
Precisely: if \(0\le q\le q_{\mathrm{crit}}\), every admissible \(H\) is Euclidean nonexpansive; if \(q>q_{\mathrm{crit}}\), the class has expansive \(H\) (and for \(q_{\mathrm{crit}}<q<1\), even with both propagators positive definite strict contractions). A rational, two-dimensional backward-Euler pair for the *same* positive-definite ODE also produces one-step expansion although both propagators are strict contractions and the blended operator is spectrally stable.

## Assumptions and scope

The operator norm is the induced Euclidean/Hilbert norm. The ordering \(0\preceq F\preceq qI\) means Hermitian positive semidefinite and all eigenvalues at most \(q\); likewise for \(G\). The projection satisfies \(P=P^*=P^2\). No commutativity of \(F,G,P\) is needed for the universal bound. The sharpness construction uses dimension two and is valid in all larger dimensions by direct sum. Dimension one has no such inflation because an orthogonal projector there is either zero or identity. The assertion concerns the linearized local propagation map, not the multi-time, multi-iteration convergence rate of a full time-parallel algorithm.

## Proof

**Upper bound.** Take any unit vector \(u\), put \(p=Pu\), \(z=(I-P)u\). Then \(p\perp z\), \(p+z=u\), and \(\|p\|_2^2+\|z\|_2^2=1\). The operator inequalities \(0\preceq F\preceq qI\) imply \(F^2\preceq qF\), and therefore
\[
\|Fp-\tfrac q2 p\|_2^2
=\langle p,(F^2-qF+\tfrac{q^2}{4}I)p\rangle
\le\tfrac{q^2}{4}\|p\|_2^2.
\]
The same argument gives \(\|Gz-\tfrac q2z\|_2\le(q/2)\|z\|_2\). Since
\[
Hu=\tfrac q2u+(F-\tfrac q2I)p+(G-\tfrac q2I)z,
\]
the triangle and Cauchy–Schwarz inequalities yield
\[
\|Hu\|_2\le\tfrac q2(1+\|p\|_2+\|z\|_2)
\le\tfrac q2(1+\sqrt2).
\]
Take the supremum over unit vectors. The argument also covers \(q=0\).

**Sharpness.** In \(\mathbb R^2\), set \(c=\cos(\pi/8)\), \(s=\sin(\pi/8)\), and
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
F_0=\begin{pmatrix}c^2&cs\\cs&s^2\end{pmatrix},\quad
G_0=\begin{pmatrix}s^2&cs\\cs&c^2\end{pmatrix}.
\]
Both \(F_0\) and \(G_0\) are rank-one orthogonal projections; in particular, they are positive contractions. But
\[
F_0P+G_0(I-P)=\begin{pmatrix}c^2&cs\\cs&c^2\end{pmatrix}
\]
has largest singular value \(c^2+cs=(1+\sqrt2)/2=C\). Scaling both propagators by \(q\) proves that the bound is sharp for every \(q\ge0\).

To obtain *positive definite* strict contractions when \(q_{\mathrm{crit}}<q<1\), set for \(0<\tau<1\)
\[
F=q((1-\tau)F_0+\tau I),\quad
G=q((1-\tau)G_0+\tau I).
\]
Their eigenvalues are exactly \(q\tau\) and \(q\), so \(0\prec F,G\prec I\). The blended map equals \(q((1-\tau)H_0+\tau I)\), and hence its norm is at least \(q((1-\tau)C+\tau)>1\) whenever \(0<\tau<(C-1/q)/(C-1)\). Since \(qC>1\), this interval is nonempty. The case \(q=q_{\mathrm{crit}}\) is nonexpansive, with equality attained by the rank-one witness.

**Both propagators arise from the same linear ODE.** Let
\[
A=\operatorname{diag}(1/2000,5),\qquad x'(t)=-Ax(t),
\]
with coarse time interval of length one. Let the fine propagator be two backward-Euler half steps and the coarse propagator one full backward-Euler step,
\[
F=(I+A/2)^{-2}=\operatorname{diag}(16000000/16008001,4/49),
\quad G=(I+A)^{-1}=\operatorname{diag}(2000/2001,1/6).
\]
For the orthogonal projector onto the first diagonal direction \((1,1)^{\mathsf T}\),
\[
P=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]
exact rational matrix multiplication gives
\[
H=G+(F-G)P=
\begin{pmatrix}
32016001000/32032010001&-1000/32032010001\\
-25/588&73/588
\end{pmatrix}.
\]
In particular,
\[
\boxed{\|He_1\|_2^2-1
=\frac{31863808011974591697209}{39416723919275164992358416}>0.}
\]
Nevertheless, the individual propagators satisfy \(0\prec F\prec G\prec I\) and commute. To see that the blended map is *spectrally stable*, put \(D=G-F\succ0\). Because \(G\) and \(D\) commute,
\[
D^{-1/2}HD^{1/2}=G-D^{1/2}PD^{1/2}.
\]
The right side is Hermitian and lies between \(F\) and \(G\) in the Loewner order: \(0\prec F\preceq G-D^{1/2}PD^{1/2}\preceq G\prec I\). Thus all eigenvalues of \(H\) are strictly between zero and one, while its Euclidean operator norm exceeds one. The phenomenon is transient nonnormal amplification, not asymptotic instability.

## Verification

Running `python3 check.py` with Python's standard library verifies the exact rational backward-Euler propagation matrices, the stated rational entries of \(H\), and the strictly positive squared-norm defect. It also checks the rank-one extremizer's eigenvalue and representative strict-positive-definite perturbations. The general inequality and sharpness follow from the analytical proof above; finite code checks are not used as an infinite-dimensional certification.

## Relationship to prior work

Tan, Xu, Zhang and Su [1], Section 2.3, equation (6), define a projection-corrected coarse map \(\mathcal H_P(x)=\mathcal G(x)+\mathcal F(Px)-\mathcal G(Px)\). Their Section 2.2, equation (4), gives the split-map formulation. For linear homogeneous propagators the two reduce to the \(H\) studied here. Their Theorem 2 gives an iteration-dependent error estimate, and their finite-step-exactness analysis is not contradicted by a one-step norm exceeding one. The sharper issue here is the *largest universal Euclidean one-step norm* under positive self-adjoint contraction hypotheses and its exact contractivity threshold.

Tan and collaborators' earlier periodic projection-based study [2] also uses mixed fine/coarse projected propagation, but its analysis concerns periodic convergence and Fourier-aware projection, not the uniform two-propagator norm envelope. Jin, Lin and Zhou [3] study optimal coarse solver stability through scalar spectral convergence factors for parabolic evolution, without deriving the projection-blended operator-norm threshold. The historical Krylov-enhanced formulation of Gander and Petcu [4] is acknowledged as the antecedent of the split linear map; the accessible historical source was insufficient to rule out every implicit equivalent. The exact coefficient \(C\), its sharp two-dimensional extremizer, and the same-ODE backward-Euler demonstration are the claimed additions, not the blended-map algorithm itself.

## Limitations

No assertion is made about random or history-dependent choices of \(P\), rate of a complete parareal iteration, nonlinear solver derivatives, convergence of arbitrary switched products, or finite-precision effects. The worst-case constant concerns the broad class \(0\preceq F,G\preceq qI\); it is not claimed to be attained within the smaller family of commuting backward-Euler propagators of a single fixed \(A\). The concrete backward-Euler example proves expansion of one step, not divergence of repeated application. Bibliographic coverage of older projection and operator-norm inequalities may be incomplete.

## References

[1] C. Tan, Y. Xu, Y. Zhang and Y. Su, “Projection-Based Parareal for Nonlinear Initial-Value Problems,” arXiv:2610.21680v1, 15 October 2026. https://arxiv.org/abs/2610.21680 ; https://arxiv.org/html/2610.21680v1

[2] C. Tan and collaborators, “A Fourier-Aware Projection-Based Periodic Parareal Method for Time-Periodic Problems,” arXiv:2607.12402, 14 July 2026. https://arxiv.org/abs/2607.12402 ; https://academ.us/article/2607.12402/

[3] B. Jin, Q. Lin and Z. Zhou, “Optimizing Coarse Propagators in Parareal Algorithms,” arXiv:2311.15320v2 (2025), *SIAM Journal on Scientific Computing* 47 (2025), DOI:10.1137/23M1619733. https://arxiv.org/html/2311.15320v2

[4] M. J. Gander and F. Petcu, “Analysis of a Krylov subspace enhanced parareal algorithm for linear problems,” *ESAIM: Proceedings* 25 (2008), DOI:10.1051/proc:082508. https://doi.org/10.1051/proc:082508
