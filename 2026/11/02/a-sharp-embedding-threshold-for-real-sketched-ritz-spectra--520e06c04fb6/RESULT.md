# A sharp embedding threshold for real sketched Ritz spectra

## Finding

Let \(A\in\mathbb R^{m\times m}\) be symmetric, let \(V\in\mathbb R^{m\times k}\) have orthonormal columns, and define the ordinary Ritz matrix and subspace residual by
\[
B=V^{\mathsf T}AV,\qquad R=AV-VB.
\]
Let \(S\) be a real sketch satisfying, for one fixed \(0<\varepsilon<1\),
\[
(1-\varepsilon)\|u\|_2^2\le\|Su\|_2^2\le(1+\varepsilon)\|u\|_2^2
\qquad (u\in\operatorname{span}\{V,AV\}).
\]
The sketched Rayleigh--Ritz matrix \(H=(SV)^\dagger SAV\) then obeys the **sharp universal inequality**
\[
\boxed{\|H-B\|_2\le\frac{\varepsilon}{\sqrt{1-\varepsilon^2}}\|R\|_2.}\tag{1}
\]
If \(k\ge2\), the eigenvalues of \(B\) are pairwise distinct, and their minimum separation is \(\Delta>0\), then **all eigenvalues of \(H\) are real and simple** provided
\[
\boxed{\frac{\varepsilon}{\sqrt{1-\varepsilon^2}}\|R\|_2<\frac\Delta2.}\tag{2}
\]
Both the constant in (1) and the strict threshold in (2) are best possible jointly. Indeed, for any \(\delta,\gamma>0\) and \(\beta>\delta+\gamma\), there exist explicit positive-definite \(4\times4\) matrices \(A\) and sketches with precisely \(\varepsilon\)-distortion for which \(\Delta=2\delta\), \(\|R\|_2=\gamma\), equality holds in (1), and the sketched Ritz eigenvalues are
\[
\boxed{\beta\pm\sqrt{\delta^2-\frac{\gamma^2\varepsilon^2}{1-\varepsilon^2}}.}\tag{3}
\]
Thus they are real and distinct below \(\varepsilon_*=\delta/\sqrt{\delta^2+\gamma^2}\), coalesce to one defective real eigenvalue at \(\varepsilon_*\), and form a nonreal conjugate pair above \(\varepsilon_*\). The example embeds unchanged into any ambient dimension \(m\ge4\), using only four sketch rows.

## Assumptions and scope

All assertions are over the real numbers in exact arithmetic. An \(\varepsilon\)-embedding is required on the **joint subspace** \(\operatorname{span}\{V,AV\}\), not merely on \(\operatorname{span}\{V\}\). No randomness, distributional assumption, or full-space embedding is required. The sufficient reality condition requires simple eigenvalues of the ordinary Ritz matrix. When \(k=1\), the sketched Ritz value is automatically real. The sharp example uses symmetric positive-definite \(A\), although (1)--(2) hold for every symmetric \(A\).

## Proof

**Step 1: An exact sketch error identity.** Because the embedding is injective on \(\operatorname{range}(V)\), put \(M=V^{\mathsf T}S^{\mathsf T}SV\succ0\). The Moore--Penrose formula and \(AV=VB+R\), \(V^{\mathsf T}R=0\), imply
\[
H=M^{-1}V^{\mathsf T}S^{\mathsf T}SAV
 =B+M^{-1}V^{\mathsf T}S^{\mathsf T}SR.
\]
Choose an orthonormal basis \(Q\) for \(\operatorname{range}(R)\) and write \(R=QT\). Relative to the orthogonal decomposition of \(\operatorname{span}\{V,AV\}\) into \(\operatorname{range}(V)\oplus\operatorname{range}(R)\), set \(C=V^{\mathsf T}S^{\mathsf T}SQ\). Then \(H-B=M^{-1}CT\) and \(\|T\|_2=\|R\|_2\). If \(R=0\), the assertion is immediate.

**Step 2: Sharp block bound for an almost-isometry.** On the joint subspace let \(G\) be the positive Gram operator induced by \(S^{\mathsf T}S\). Its spectrum lies in \([1-\varepsilon,1+\varepsilon]\). For any \(z\in\mathbb R^k\) with \(\|z\|_2=1\), write \(u=M^{-1}z\), \(x=Vu\), and
\[
t=\frac{x^{\mathsf T}Gx}{\|x\|_2^2}\in[1-\varepsilon,1+\varepsilon].
\]
The bound \(\|G-I\|_2\le\varepsilon\), together with the component of \((G-I)x\) along \(x\), gives
\[
\|Q^{\mathsf T}Gx\|_2^2
\le \|x\|_2^2\bigl(\varepsilon^2-(t-1)^2\bigr).
\]
On the other hand, \(z=Mu\) and Cauchy--Schwarz imply
\[
1=\|Mu\|_2\ge \frac{u^{\mathsf T}Mu}{\|u\|_2}=t\|x\|_2.
\]
Consequently
\[
\|C^{\mathsf T}M^{-1}z\|_2
\le\frac{\sqrt{\varepsilon^2-(t-1)^2}}{t}
\le\frac{\varepsilon}{\sqrt{1-\varepsilon^2}}.
\]
The last scalar maximum is attained at \(t=1-\varepsilon^2\), as follows by differentiating its square. Taking the supremum over \(z\) proves \(\|M^{-1}C\|_2\le\varepsilon/\sqrt{1-\varepsilon^2}\), and hence (1).

**Step 3: Spectral reality from separated Ritz values.** Write \(F=H-B\). Because \(B\) is real symmetric, every eigenvalue of \(B+sF\), for \(0\le s\le1\), lies in the union of radius-\(s\|F\|_2\) disks about the eigenvalues of \(B\). This follows from the resolvent bound for a normal matrix (or by the Neumann series outside these disks). Under (2), disks of radius \(\|F\|_2\) about distinct Ritz values are disjoint. Continuously varying \(s\) from zero to one, each disk retains exactly one eigenvalue counted with multiplicity. A nonreal eigenvalue of the real matrix \(B+F\) would bring its complex conjugate into the same real-centered disk, contradicting that count. Thus all eigenvalues are real and simple.

**Step 4: Attaining the bound and the exact nonreality threshold.** Put
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
D=\begin{pmatrix}-\delta&0\\0&\delta\end{pmatrix},\quad
A_0=\begin{pmatrix}\beta I_2+D&\gamma I_2\\\gamma I_2&\beta I_2\end{pmatrix},\quad
V_0=\begin{pmatrix}I_2\\0\end{pmatrix}.
\]
The perturbation of \(\beta I_4\) in \(A_0\) has spectral norm no greater than \(\delta+\gamma\); hence \(A_0\succ0\). Directly, \(B_0=\beta I_2+D\) and \(R_0=(0,\gamma I_2)^{\mathsf T}\).

For \(0<\varepsilon<1\), define
\[
a=1-\varepsilon^2,\quad z=1+\varepsilon^2,\quad b=\varepsilon\sqrt{1-\varepsilon^2},\quad
G_0=\begin{pmatrix}aI_2&bJ\\-bJ&zI_2\end{pmatrix}.
\]
The matrix \(G_0\) is symmetric and \((G_0-I_4)^2=\varepsilon^2I_4\). Thus \(G_0\succ0\) and its eigenvalues are exactly \(1-\varepsilon\) and \(1+\varepsilon\), each twice. Take \(S_0=G_0^{1/2}\), the positive-definite square root. It is an exact \(\varepsilon\)-embedding. The projected matrix is
\[
H_0=\beta I_2+D+\frac{\gamma b}{a}J
=\begin{pmatrix}\beta-\delta&-\gamma\varepsilon/\sqrt{1-\varepsilon^2}\\
\gamma\varepsilon/\sqrt{1-\varepsilon^2}&\beta+\delta\end{pmatrix}.
\]
The skew perturbation has norm \(\gamma\varepsilon/\sqrt{1-\varepsilon^2}\), so equality holds in (1). Its characteristic polynomial is \((\lambda-\beta)^2-\delta^2+\gamma^2\varepsilon^2/(1-\varepsilon^2)\), proving (3). At \(\varepsilon=\varepsilon_*\), \(H_0-\beta I_2\) is a nonzero square-zero matrix, so the repeated eigenvalue is defective. For ambient \(m>4\), append a \(\beta I_{m-4}\) block to \(A_0\), zero rows to \(V_0\), and zero columns to \(S_0\). The same joint four-dimensional subspace and calculation remain valid.

## Verification

The standalone file `verify.py` checks the exact rational instance \(\beta=3\), \(\delta=1/2\), \(\gamma=1\), \(\varepsilon=3/5\). Here \(a=16/25\), \(b=12/25\), \(z=34/25\), \(H_0=\bigl(\begin{smallmatrix}5/2&-3/4\\3/4&7/2\end{smallmatrix}\bigr)\), and the two eigenvalues are \(3\pm i\sqrt5/4\). The script also checks the analytic threshold identities for rational parameter pairs and tests the perturbation bound and reality implication on seeded random symmetric positive-definite matrices. These finite tests are supplementary: the universal proof is Steps 1--4, not the computations.

To reproduce: run `python verify.py` with Python 3 and NumPy installed. No external data or online service is used.

## Relationship to prior work

Liu and Liu (arXiv:2610.22261, first posted October 15, 2026) develop a real-Schur remedy for the possibly complex sRR eigenpairs and prove local characteristic-subspace selection estimates; their Section 3.1 and Section 5.3 do not provide (1), the all-Ritz-real criterion (2), or the attained transition (3). Nakatsukasa and Tropp (SIAM J. Matrix Anal. Appl. 2024, Section 6.8) already note that sRR for symmetric matrices can yield nonreal eigenvalue estimates and motivate use of spectral perturbation theory. The new distinction here is an exact residual-and-distortion threshold for **absence** of such pairs, including an attained worst case. Classical oblique-projection perturbation theory and spectral disk arguments provide the background ingredients and may encompass intermediate lemmas; the claimed contribution is their joint sharp application to sRR, not invention of the underlying perturbation principles.

## Limitations

The embedding requirement covers \(\operatorname{span}\{V,AV\}; no conclusion of this strength is claimed under an embedding of \(\operatorname{range}(V)\) alone. The guarantee is a sufficient global reality test; it does not classify every individual sketch outside the threshold. Sharpness means minimax attainment across admissible symmetric problems and embeddings with specified Ritz gap and residual, not that every problem becomes complex at the threshold. There is no bound on floating-point effects or probability of the sketch satisfying the embedding hypothesis. The exact critical collision may be ill-conditioned. Exhaustive historical-priority confirmation and independent mathematical validation are outstanding.

## References

1. J. Liu and Y. Liu, *Real-Arithmetic Sketched Eigensolvers for Symmetric Matrices*, arXiv:2610.22261v1, first posted October 15, 2026, Sections 3.1 and 5.3. https://arxiv.org/abs/2610.22261
2. Y. Nakatsukasa and J. A. Tropp, *Fast and Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, SIAM J. Matrix Anal. Appl. **45** (2024), 1183--1214, especially Sections 6.3 and 6.8. https://doi.org/10.1137/23M1565413
3. G. W. Stewart, *On the Numerical Analysis of Oblique Projectors*, SIAM J. Matrix Anal. Appl. **32** (2011), 309--348. https://doi.org/10.1137/100792093
