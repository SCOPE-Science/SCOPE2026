# Sharp one-vector sketching envelope and positive-stability threshold for symmetric systems

## Finding

For a real symmetric positive-definite matrix whose spectrum lies in \([\mu,L]\), a squared-norm subspace embedding with distortion \(\varepsilon<1\) gives an **exact, sharp universal interval** for the one-vector sketched full-orthogonalization (FOM) Ritz scalar:

\[
\boxed{\frac{\mu+L}{2}-\frac{L-\mu}{2\sqrt{1-\varepsilon^2}}
\ \le\ h_S\ \le\
\frac{\mu+L}{2}+\frac{L-\mu}{2\sqrt{1-\varepsilon^2}}.}
\]

Both bounds are attainable already in dimension two, uniformly for every fixed \(0<\mu\le L\) and \(0\le\varepsilon<1\). In particular, for \(L>\mu\), the sharp **robust positive-stability threshold** is

\[
\boxed{\varepsilon_{\mathrm{crit}}=\frac{2\sqrt{\mu L}}{\mu+L}
=\frac{2\sqrt{\kappa}}{1+\kappa}},
\qquad \kappa=L/\mu.
\]

Every admissible sketch has \(h_S>0\) when \(\varepsilon<\varepsilon_{\mathrm{crit}}\). At equality, a sketch has \(h_S=0\); for larger permitted distortions, a sketch has \(h_S<0\). For \(L=\mu\), the scalar is always \(\mu\). The threshold is a stability guarantee, not an error bound.

## Assumptions and scope

Let \(n\ge2\), \(A=A^{\mathsf T}\in\mathbb R^{n\times n}\), and \(0<\mu I\preceq A\preceq L I\). Take \(b\in\mathbb R^n\setminus\{0\}\), \(S\in\mathbb R^{s\times n}\), and \(0\le\varepsilon<1\). Require the squared-norm embedding

\[
(1-\varepsilon)\|u\|_2^2\le\|Su\|_2^2\le
(1+\varepsilon)\|u\|_2^2\quad
\text{for every }u\in U:=\operatorname{span}\{b,Ab\}.
\]

No assumption is imposed on the action of the sketch outside \(U\). The one-vector sketched-FOM compression and matrix-exponential surrogate are

\[
h_S=\frac{(Sb)^{\mathsf T}(SAb)}{\|Sb\|_2^2},
\qquad \widetilde y(t)=e^{-t h_S}b\quad(t\ge0).
\]

The denominator is strictly positive. Only the real, one-vector compression and exact arithmetic are covered. The word *robust* means uniformity over all admissible matrices, vectors, and embeddings with given spectral bounds.

## Proof

**1. Reduction to an embedded two-dimensional metric.** Let \(P_U\) be the Euclidean orthogonal projector onto \(U\) and denote by \(M\) the self-adjoint operator \(P_US^{\mathsf T}SP_U\) restricted to \(U\). The embedding condition gives

\[
(1-\varepsilon)I_U\preceq M\preceq(1+\varepsilon)I_U.
\]

As \(b,Ab\in U\), \(h_S=\langle b,MAb\rangle/\langle b,Mb\rangle\); vectors outside \(U\) play no role. Scaling \(b\) does not change \(h_S\), so take \(\|b\|_2=1\).

**2. A sharp metric-angle inequality.** Set \(\gamma=1-\varepsilon^2>0\). The scalar polynomial \((x-(1-\varepsilon))(x-(1+\varepsilon))\le0\) throughout the spectrum of \(M\) gives

\[
M^2\preceq2M-\gamma I_U.
\]

Writing \(d=\langle b,Mb\rangle>0\), we deduce

\[
\frac{\|Mb\|_2^2}{d^2}
\le\frac{2d-\gamma}{d^2}\le\frac1\gamma,
\]

where the last inequality is exactly \((d-\gamma)^2\ge0\). Thus \(\|Mb\|_2/d\le1/\sqrt\gamma\).

**3. Universal spectral envelope.** Write \(\alpha=(\mu+L)/2\), \(\delta=(L-\mu)/2\) and \(A=\alpha I+T\), with real symmetric \(\|T\|_2\le\delta\). Since \(Tb\in U\), Cauchy–Schwarz and Step 2 imply

\[
|h_S-\alpha|
=\frac{|\langle Mb,Tb\rangle|}{d}
\le\delta\frac{\|Mb\|_2}{d}
\le\frac\delta{\sqrt{1-\varepsilon^2}}.
\]

This proves both inequalities for every admissible dimension and sketch. If \(\delta=0\) then \(A=\mu I\), and \(h_S=\mu\) exactly.

**4. Simultaneously sharp endpoints.** In dimension two take

\[
A=\begin{pmatrix}\mu&0\\0&L\end{pmatrix},
\qquad M=\begin{pmatrix}1&-\varepsilon\\-\varepsilon&1\end{pmatrix}.
\]

All eigenvalues of \(M\) equal \(1\pm\varepsilon\), so its positive square root gives a valid \(S\). Define the symmetric matrix \(B=(MA+AM)/2\). Its generalized Rayleigh quotient equals the sketched scalar because \(b^{\mathsf T}MA b=b^{\mathsf T}B b\). Direct determinant expansion shows

\[
\det(B-zM)
=(1-\varepsilon^2)(z-\alpha)^2-\delta^2.
\]

Since \(M\) is positive definite, the minimum and maximum generalized eigenvalues of the symmetric pencil \((B,M)\) are the extremal values of \(b^{\mathsf T}Bb/(b^{\mathsf T}Mb)\). The displayed determinant gives precisely \(\alpha\mp\delta/\sqrt{1-\varepsilon^2}\), attained by corresponding real nonzero generalized eigenvectors \(b\). At \(\varepsilon=0\), ordinary eigenvectors attain the endpoints.

**5. Sharp stability frontier.** If \(L>\mu\), the smallest universally attainable scalar is positive exactly when

\[
\sqrt{1-\varepsilon^2}>
\frac{L-\mu}{L+\mu}
\quad\Longleftrightarrow\quad
\varepsilon<\frac{2\sqrt{\mu L}}{\mu+L}.
\]

At equality the lower endpoint is zero; above it the lower endpoint is negative. In the explicit case \(\mu=1\), \(L=9\), \(\varepsilon=4/5\), \(b=(2,1)^{\mathsf T}\), the admissible metric above yields \(h_S=-5/3\), while \(A\succ0\). Hence the one-vector exponential surrogate grows as \(e^{5t/3}\|b\|_2\), whereas \(\|e^{-tA}b\|_2\le e^{-t}\|b\|_2\) for all \(t\ge0\). At the critical \(\varepsilon=3/5\), the choice \(b=(3,1)^{\mathsf T}\) makes \(h_S=0\). This completes the sharp classification.

## Verification

The standalone \(\texttt{verify.py}\) script checks the exact quadratic discriminant and characteristic coefficients with rational arithmetic, both extremal roots, numerical instantiations of the envelope and the critical signs. It completed with output \(\texttt{VERIFY\_OK\ 1254}\). These finite checks only corroborate the explicitly reconstructed determinant and analytic proof; they do not establish the universal claim independently.

## Relationship to prior work

Güttel and Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions* (first publicly available 2022-08-24), introduce the sketched-FOM compression and the squared-norm embedding assumption in their equation (1.1). Their Section 2.3, equation (2.7), already explains that sketched Ritz values may leave the usual numerical range, potentially entering the left half-plane. Thus qualitative possibility of spurious unstable Ritz values is **not** new. The result above supplies a sharp two-sided attainable interval and the exact necessary-and-sufficient robust positivity frontier for the specified one-vector symmetric-positive-definite setting, neither established in that paper.

Cortinovis, Kressner and Nakatsukasa (2022) study randomized Krylov compression and matrix-function approximation, without the present sharp embedding-distortion envelope. Simoncini and Wang (2025), Lemma 5.2, state a generic lower bound on cosine distortion under a subspace embedding, and Proposition 7.2 gives a general spectral-localization estimate. Their cosine bound, combined with the classical SPD acute-angle inequality, is sufficient to derive a **nonsharp-in-value positive-sign guarantee** at the threshold above. It does not yield the exact two-sided attainable Ritz-value envelope or provide both generalized-eigenvector extremizers. The sufficiency mechanism, on its own, is not claimed as novel. A corresponding classical Kantorovich-type inequality underlies Step 2; the use of this inequality is not claimed as new. Published analogous finite-Ritz miscertification examples and related sketched-FOM tail phenomena do not imply the deterministic embedding-conditioned sharp envelope.

## Limitations

The finding is restricted to real symmetric positive-definite matrices, a one-vector sketched-FOM compression, an embedding on \(\operatorname{span}\{b,Ab\}\), and exact arithmetic. It does not characterize complex or multi-vector sketched Ritz spectra, sketched GMRES, finite precision, sampling costs, or the approximation error at any fixed time. It does not claim that the simple positivity criterion is sufficient for a small matrix-function approximation error. The explicit two-dimensional construction shows sharpness over the full admissible class; it is not a statement about every individual sketch. Earlier algebraic treatments of generalized numerical ranges could imply an equivalent special case; no exhaustive originality guarantee is claimed.

## References

1. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447 (first posted 2022-08-24), especially (1.1), (2.3) and Section 2.3; https://arxiv.org/abs/2208.11447 .
2. A. Cortinovis, D. Kressner and Y. Nakatsukasa, *Speeding up Krylov subspace methods for computing f(A)b via randomization*, arXiv:2212.12758 (first posted 2022-12-24); https://arxiv.org/abs/2212.12758 .
3. V. Simoncini and Y. Wang, *Stabilized Krylov Subspace Recurrences via Randomized Sketching*, Numerical Linear Algebra with Applications (2025), DOI:10.1002/nla.70022; https://doi.org/10.1002/nla.70022 .
