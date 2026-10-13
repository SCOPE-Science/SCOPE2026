# Sharp positivity threshold for sketched FOM on SPD Krylov spaces

## Finding

The sketched full orthogonalization method (sketched FOM) has an exact, uniform embedding-distortion threshold for retaining positive-real Ritz values on real symmetric positive-definite systems. For a spectral interval \(0<\mu\le L\), put \(\kappa=L/\mu\) and
\[
\varepsilon_*(\kappa)=\frac{2\sqrt{\mu L}}{\mu+L}=\frac{2\sqrt\kappa}{1+\kappa}.
\]
If a linear sketch is a \(\varepsilon\)-subspace embedding of the next Krylov space and \(0\le\varepsilon<\varepsilon_*(\kappa)\), all eigenvalues \(\lambda\) of the sketched FOM compression obey
\[
\operatorname{Re}\lambda\ \ge\ \frac{\mu}{1+\varepsilon}\left(1-\frac{\varepsilon}{\varepsilon_*(\kappa)}\right)>0.
\]
The threshold, but not necessarily the displayed quantitative lower bound, is **sharp**: for every \(\kappa>1\), a three-dimensional SPD system with a two-row sketch loses invertibility exactly at \(\varepsilon=\varepsilon_*(\kappa)\) and has a negative sketched Ritz value for every \(\varepsilon\in(\varepsilon_*(\kappa),1)\). For \(\kappa=1\), the compression equals the scalar matrix \(\mu I\) for every \(\varepsilon<1\).

## Assumptions and scope

Let \(A\in\mathbb R^{N\times N}\) be symmetric positive definite with \(\mu I\preceq A\preceq LI\), \(b\ne0\), and let \(1\le m\le N\) satisfy \(\dim\mathcal K_m(A,b)=m\), where
\[
\mathcal K_j(A,b)=\operatorname{span}\{b,Ab,\ldots,A^{j-1}b\}.
\]
Take any full-column-rank \(V\in\mathbb R^{N\times m}\) spanning \(\mathcal K_m(A,b)\). Let \(S\in\mathbb R^{s\times N}\) (not necessarily randomly generated) satisfy, **for every** \(z\in\mathcal K_{m+1}(A,b)\),
\[
(1-\varepsilon)\|z\|_2^2\le\|Sz\|_2^2\le(1+\varepsilon)\|z\|_2^2,
\qquad 0\le\varepsilon<1.
\]
Here \(\mathcal K_{m+1}\) may coincide with \(\mathcal K_m\) after exact Krylov breakdown. Define
\[
B=(V^{\mathsf T}S^{\mathsf T}SV)^{-1}V^{\mathsf T}S^{\mathsf T}SAV.
\]
The first factor is invertible by the embedding hypothesis. Changing the basis \(V\) changes \(B\) by similarity, so its spectrum is intrinsic. The theorem concerns the spectral location of this **ordinary sketched FOM**, not harmonic Ritz values or error norms of sketched GMRES.

## Proof

**Step 1 (the sharp SPD angle inequality).** For any nonzero \(x\in\mathbb C^N\), put \(t=(x^*Ax)/(x^*x)\in[\mu,L]\). By functional calculus on the spectrum of \(A\),
\[
A^2\preceq(\mu+L)A-\mu L I,
\quad\text{hence}\quad
\frac{\|Ax\|_2^2}{\|x\|_2^2}\le(\mu+L)t-\mu L.
\]
Elementary minimization of \(t/\sqrt{(\mu+L)t-\mu L}\) on \([\mu,L]\) gives its minimum at \(t=2\mu L/(\mu+L)\), equal to \(2\sqrt{\mu L}/(\mu+L)\). Therefore
\[
\frac{x^*Ax}{\|x\|_2\,\|Ax\|_2}\ge\varepsilon_*(\kappa).
\tag{1}
\]
This calculation covers arbitrary complex \(x\), including generalized eigenvectors of the real but nonsymmetric matrix \(B\). Equality is possible on a two-eigenvalue SPD system.

**Step 2 (restricted bilinear perturbation).** Write \(W=S^{\mathsf T}S\). The embedding hypothesis implies that the Hermitian compression of \(W-I\) to \(\mathcal K_{m+1}\), extended to complex vectors, has operator norm at most \(\varepsilon\). Thus for all \(x,y\) in its complexification,
\[
|x^*(W-I)y|\le\varepsilon\|x\|_2\|y\|_2.
\]
For every nonzero \(x\in\mathcal K_m^{\mathbb C}\), both \(x\) and \(Ax\) belong to \(\mathcal K_{m+1}^{\mathbb C}\). Combining this with (1) gives
\[
\operatorname{Re}(x^*WAx)
\ge x^*Ax-\varepsilon\|x\|_2\|Ax\|_2
\ge \left(1-\frac\varepsilon{\varepsilon_*}\right)x^*Ax.
\tag{2}
\]
For \(\varepsilon<\varepsilon_*\), this is at least \(\mu(1-\varepsilon/\varepsilon_*)\|x\|_2^2\). Also \(0<x^*Wx\le(1+\varepsilon)\|x\|_2^2\).

**Step 3 (all projected eigenvalues).** If \(Bz=\lambda z\) over \(\mathbb C\) with \(z\ne0\), set \(x=Vz\ne0\). The definition of \(B\) implies
\[
\lambda=\frac{x^*WAx}{x^*Wx}.
\]
The positive denominator and (2) give the stated strict right-half-plane bound. In particular, \(B\) and all shifts \(B+tI\), \(t\ge0\), are nonsingular under the threshold.

**Step 4 (universal sharpness with genuine sketch compression).** Let \(q>1\), \(\mu=1\), \(L=q^2\), \(N=3\), \(m=1\), and set
\[
A=\operatorname{diag}(1,q^2,1),\qquad b=(q,1,0)^{\mathsf T},\qquad
S_\varepsilon=\begin{pmatrix}1&-\varepsilon&0\\0&\sqrt{1-\varepsilon^2}&0\end{pmatrix}.
\]
Since \(q>1\), the next Krylov space \(\mathcal K_2(A,b)\) equals \(\operatorname{span}\{e_1,e_2\}\). On that space \(S_\varepsilon^{\mathsf T}S_\varepsilon\) has eigenvalues \(1\pm\varepsilon\), so the stated embedding distortion is exact, even though \(S_\varepsilon\) has only two rows. Taking \(V=b\), the one-by-one sketched Ritz value is
\[
B_\varepsilon=\frac{2q^2-\varepsilon q(1+q^2)}{1+q^2-2\varepsilon q}.
\tag{3}
\]
The denominator is positive for \(0\le\varepsilon<1\), whereas the numerator changes sign exactly at \(\varepsilon=2q/(1+q^2)=\varepsilon_*(q^2)\). Scaling \(A\) by an arbitrary \(\mu>0\) covers any specified \(\mu,L\). This establishes the necessity of the strict threshold for a universal guarantee. If \(\kappa=1\), then \(A=\mu I\) and direct substitution gives \(B=\mu I\) for all admissible sketches.

## Verification

The standalone standard-library script `verify.py` checks, with exact rational arithmetic, the squared SPD angle inequality for many endpoint spectra and vectors; the sign and zero of (3) at its algebraic cutoff; the equality case of (1); the embedding inequalities on rational vectors; and the fixed \(q=3\) witness. It reports `EXACT_CHECKS_PASS 25308` when executed. These finite checks are diagnostics; the proof above establishes the statements for all dimensions, bases, vectors, and admissible sketches.

For \(q=3\), the cutoff is \(\varepsilon_*=3/5\). Equation (3) gives exactly \(B_{3/5}=0\), \(B_{4/5}=-15/13\), and \(B_{59/100}=15/323\). In particular, the reciprocal function \(f(z)=1/z\) becomes undefined at the zero Ritz value, despite a valid norm embedding with distortion \(3/5\).

To reproduce: place `verify.py` beside this document and execute `python3 verify.py` using a standard Python 3 interpreter; no third-party packages or external data are required.

## Relationship to prior work

Güttel and Schweitzer introduced this sketched FOM projection and showed that its Ritz values can move outside the positive-real region even for underlying positive-real matrices (Section 2, particularly their Eq. (9)). Their numerical-range enclosure and warnings do **not** give the condition-number-dependent sharp SPD positivity threshold or a matching minimal-dimensional obstruction derived here. The present result concerns the precise boundary for a prescribed embedding quality, not randomness of an embedding distribution.

Cortinovis, Kressner, and Nakatsukasa describe a mathematically equivalent randomized compression and analyze its approximation performance; the equivalence is acknowledged, not claimed as new. Timsit, Grigori, and Balabanov derive quasi-optimality criteria for randomized projection solvers, including a condition involving the inverse square root of a condition number. Their error and solution-subspace guarantees do not establish the iff criterion for **sketched FOM Ritz positivity**. Güttel, Liu, and Nyman later analyze the positivity of **sketched harmonic Ritz** values, arising from a different matrix pencil. A general classical SPD turning-angle inequality is used, but is not itself claimed as new.

## Limitations

The theorem gives a worst-case guarantee conditional on an embedding, not the probability that a particular random sketch meets it. It applies only to real SPD matrices and the ordinary sketched FOM compression with an embedding on \(\mathcal K_{m+1}\); it is not a classification for nonsymmetric or indefinite matrices, harmonic variants, or floating-point implementations. The sharp threshold is about positivity and nonsingularity, not an optimal approximation-error constant or solver iteration count. A broad equivalent theorem in other oblique-projection or perturbation terminology may exist outside the inspected literature; independent priority review remains open.

## References

1. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447v1 (first posted 2022-08-24), Sections 2 and 5. https://arxiv.org/abs/2208.11447
2. A. Cortinovis, D. Kressner, and Y. Nakatsukasa, *Speeding up Krylov subspace methods for computing \(f(A)b\) via randomization*, arXiv:2212.12758 (2022), especially Section 3.3. https://arxiv.org/abs/2212.12758
3. E. Timsit, L. Grigori, and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466 (2023), Proposition 3.1. https://arxiv.org/abs/2302.07466
4. S. Güttel, J. Liu, and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354 (2026), Section 5.3. https://arxiv.org/abs/2607.10354
