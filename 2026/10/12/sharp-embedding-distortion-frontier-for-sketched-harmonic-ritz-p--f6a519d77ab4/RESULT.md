# Sharp embedding-distortion frontier for sketched harmonic Ritz positivity

## Finding

Consider a Hermitian positive-definite matrix and the sketched harmonic Ritz pencil used in matrix-function Krylov methods. Among all sketches satisfying a symmetric subspace-embedding distortion bound, the sharp universal right-half-plane threshold is

\[
\boxed{\varepsilon_{\mathrm{crit}}=\frac{2\sqrt{\kappa}}{\kappa+1}},
\qquad \kappa=\frac{L}{\mu}.
\]

For every \(0\leq\varepsilon<\varepsilon_{\mathrm{crit}}\), the harmonic pencil is well-defined and every sketched harmonic Ritz value has positive real part, regardless of trial dimension. For each \(\kappa>1\), equality admits a singular harmonic denominator; every larger allowed distortion admits a negative sketched harmonic Ritz value in dimension two. Thus the strict inequality is both sufficient and sharp as a condition-number-only guarantee.

The existing general positive-real-matrix sufficient condition, when restricted to this Hermitian case, asks for \(\varepsilon<1/\kappa\). The sharp frontier is strictly less restrictive for \(\kappa>1\), improving the allowable distortion by a factor asymptotic to \(2\sqrt{\kappa}\). The previously known pencil and embedding model are not new; the contribution is the sharp universal frontier and its matching failure construction.

## Assumptions and scope

Let \(\mathbb F\) equal \(\mathbb R\) or \(\mathbb C\). Let \(n\geq2\), \(1\leq m\leq n\), and \(A\in\mathbb F^{n\times n}\) satisfy

\[
0<\mu I\preceq A\preceq LI,\qquad
\kappa=L/\mu\geq1.
\]

The supplied endpoints \(\mu,L\) need only enclose the spectrum; the sharpness construction uses both endpoints as eigenvalues. Let \(B\in\mathbb F^{n\times m}\) have full column rank. Put \(W=AB\), and let \(U=\operatorname{range}[B\;W]\). Let \(S\in\mathbb F^{s\times n}\) be any linear map satisfying, for every \(u\in U\),

\[
(1-\varepsilon)\|u\|_2^2\leq\|Su\|_2^2
\leq(1+\varepsilon)\|u\|_2^2,
\qquad 0\leq\varepsilon<1.
\]

Define the sketched harmonic Gram matrices

\[
G=(SW)^*(SB),\qquad F=(SW)^*(SW).
\]

If \(G\) is invertible, let \(H=G^{-1}F\). Its eigenvalues are the generalized eigenvalues of the sketched harmonic pencil \((F,G)\), in the normalization used for harmonic Ritz values in the motivating work. The theorem concerns these eigenvalues, not the eigenvalues of ordinary sketched Rayleigh--Ritz or the unconditional convergence of an entire restarted algorithm.

## Proof

**1. The sharp acute-angle inequality.** Set \(C=A^{-1}\), \(a=1/L\), and \(b=1/\mu\). The matrix \(C\) is Hermitian, with spectrum contained in \([a,b]\). For any unit vector \(x\), write \(t=x^*Cx\). Functional calculus gives

\[
(C-aI)(bI-C)\succeq0,
\qquad x^*C^2x\leq(a+b)t-ab.
\]

Because

\[
(a+b)^2t^2-4ab((a+b)t-ab)
=((a+b)t-2ab)^2\geq0,
\]

we have

\[
\frac{x^*Cx}{\|x\|_2\|Cx\|_2}
\geq\frac{2\sqrt{ab}}{a+b}
=\frac{2\sqrt{\kappa}}{\kappa+1}
=:c_\kappa.
\tag{1}
\]

This classical inverse-positive-vector angular inequality is sharp in a two-dimensional eigenspace spanned by eigenvectors for the spectral endpoints. The elementary derivation fixes the constant and the normalization relevant here.

**2. The pencil is strictly accretive below the frontier.** The embedding hypothesis says that the Hermitian compression of \(S^*S-I\) to \(U\) has operator norm at most \(\varepsilon\). Consequently, for any \(u,v\in U\),

\[
|\langle Su,Sv\rangle-\langle u,v\rangle|
\leq\varepsilon\|u\|_2\|v\|_2.
\tag{2}
\]

For any nonzero coefficient vector \(y\in\mathbb F^m\), set \(x=W y\ne0\). Since \(Cx=By\in U\) and \(x\in U\), equations (1)--(2) imply

\[
\begin{aligned}
\operatorname{Re}(y^*Gy)
&=\operatorname{Re}\langle Sx,SCx\rangle\\
&\geq x^*Cx-\varepsilon\|x\|_2\|Cx\|_2\\
&\geq(c_\kappa-\varepsilon)\|x\|_2\|Cx\|_2>0.
\end{aligned}
\tag{3}
\]

Thus the Hermitian part \((G+G^*)/2\) is positive definite; in particular \(G\) is invertible. Also \(F\succ0\): for \(y\ne0\), \(y^*Fy=\|SWy\|_2^2\geq(1-\varepsilon)\|Wy\|_2^2>0\).

If \(Hy=\theta y\) with \(y\ne0\), then \(Fy=\theta Gy\), hence

\[
\theta=\frac{y^*Fy}{y^*Gy}.
\]

The numerator is strictly positive real and the denominator has strictly positive real part by (3); therefore \(\operatorname{Re}\theta>0\). This proves the assertion in every trial dimension and for real or complex matrices.

**3. Exact sharpness at and above the threshold.** Fix any \(\kappa>1\), and let \(q=\sqrt{\kappa}>1\). Use the real two-dimensional matrices and vectors

\[
A=\begin{pmatrix}1&0\\0&q^{-2}\end{pmatrix},\qquad
x=\frac1{\sqrt{q^2+1}}\begin{pmatrix}q\\1\end{pmatrix},
\qquad B=A^{-1}x.
\]

For every \(0\leq\varepsilon<1\), choose a real \(2\times2\) matrix \(S\) with

\[
S^{\mathsf T}S=I-\varepsilon J,
\qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Such a matrix exists because \(I-\varepsilon J\succ0\). Its squared singular values are exactly \(1-\varepsilon\) and \(1+\varepsilon\), so it satisfies the required embedding property on the entire plane with *exact* distortion \(\varepsilon\). Since \(AB=x\), direct multiplication gives

\[
G=x^{\mathsf T}(I-\varepsilon J)A^{-1}x
=q(c_\kappa-\varepsilon),
\qquad
F=x^{\mathsf T}(I-\varepsilon J)x
=1-\varepsilon c_\kappa>0.
\]

At \(\varepsilon=c_\kappa<1\), the harmonic denominator \(G\) vanishes. For \(c_\kappa<\varepsilon<1\), \(G<0\) and the unique harmonic Ritz value is

\[
\theta=\frac{1-\varepsilon c_\kappa}
{q(c_\kappa-\varepsilon)}<0.
\tag{4}
\]

For an exact rational illustration, take \(\kappa=9\), \(c_\kappa=3/5\), and \(\varepsilon=2/3\). Equation (4) yields \(\theta=-3\), even though \(A\succ0\) and \(S\) is a valid embedding. The witness can be made *dimension reducing*: embed the two matrices into a three-dimensional \(A=\operatorname{diag}(1,q^{-2},1)\), pad \(B\) with a zero third entry, and take \(S=(I-\varepsilon J)^{1/2}[I_2\;0]\in\mathbb R^{2\times3}\); the pencil and its critical behavior are unchanged. For \(\kappa=1\), the threshold is one, the maximal distortion allowed by the hypothesis, so no larger admissible distortion needs a witness.

This proves necessity of the strict threshold for a universal guarantee and completes the proof.

## Verification

The accompanying `verify.py` uses Python's exact rational arithmetic only. It directly forms the sketch Gram matrices for two-mode witnesses, checks all three regimes (positive, singular, and negative) across multiple condition numbers, and checks positive definiteness of the Hermitian part of \(G\) and of \(F\) for reproducible three-dimensional two-column trial bases below the frontier. The checks complement, but do not replace, the symbolic proof of all-dimension sufficiency and exact sharpness.

Reproduction: run `python verify.py` using Python 3 with no third-party dependencies. The expected output begins with `VERIFY_OK` and reports the actual checked case counts.

## Relationship to prior work

Güttel, Liu, and Nyman (2026, arXiv:2607.10354v1) introduce the sketched harmonic Arnoldi pencil \((F,G)\), derive its generalized eigenvalue relation in Section 5.3, and prove right-half-plane inclusion under \(\varepsilon\|A^{-1}\|_2<\rho\), where \(\rho=\min_{\|x\|_2=1}\operatorname{Re}(x^*A^{-1}x)\). For a Hermitian positive-definite \(A\), this condition reduces to \(\varepsilon<1/\kappa\). The present result replaces that sufficient bound, **only in the Hermitian positive-definite class**, with the exact minimax frontier \(2\sqrt{\kappa}/(\kappa+1)\) and supplies singular/negative endpoint witnesses. The pencil formula and the subspace-embedding inner-product perturbation inequality are credited to that work and prior literature; the underlying angular inequality is classical.

Jang and Grigori (2025) discuss harmonic Ritz extraction in randomized Krylov settings and numerical orthogonalization, but do not state a condition-number-sharp positivity frontier for this sketched harmonic pencil. Nakatsukasa and Tropp (2021/2024) develop ordinary sketched Rayleigh--Ritz and GMRES; ordinary sketched Rayleigh--Ritz uses a different reduced operator and does not imply this harmonic-pencil frontier. Searches for the bound's equivalent cosine-angle, Kantorovich, and generalized-pencil formulations did not identify a previously published theorem matching both the universal threshold and its sharp witnesses. These negative search results cannot establish exhaustive novelty.

## Limitations

The guarantee is conditional on a deterministic embedding distortion bound over \(\operatorname{range}[B\;AB]\). It does not give the probability that a particular randomized sketch satisfies that bound. The sharp bad sketches are admissible deterministic embeddings, not samples asserted to be likely for a named sketch distribution. The result requires Hermitian positive-definite \(A\); a general positive-real nonnormal extension is not proved. The threshold guarantees only that sketched harmonic Ritz eigenvalues lie in the right half-plane; it does not by itself imply full restarted matrix-function convergence, which has additional hypotheses, nor stability in finite precision. The singular witness occurs exactly at the threshold; for strictly larger admissible distortions the explicit Ritz value is negative. Related older operator-angle or oblique projection results could offer equivalent statements not located in the available literature.

## References

1. S. Güttel, J. Liu, and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354v1, first submitted 11 July 2026. Complete preprint: https://arxiv.org/html/2607.10354v1, especially Sections 2.2, 5.2, and 5.3.
2. Y. Jang and L. Grigori, *Randomized Orthogonalization Process With Reorthogonalization*, Numerical Linear Algebra with Applications 32 (2025), e70029, https://doi.org/10.1002/nla.70029, especially Section 5.
3. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v1; journal version SIAM J. Matrix Anal. Appl. 45 (2024), 1183--1214, https://doi.org/10.1137/23M1565413, especially Sections 1.3, 6, and 7.
