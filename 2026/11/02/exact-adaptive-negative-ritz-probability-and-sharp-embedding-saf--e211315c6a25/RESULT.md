# Exact adaptive negative-Ritz probability and sharp embedding-safety radius for Gaussian harmonic sketching

## Finding
For an SPD matrix \(A\) with distinct smallest and largest eigenvalues \(0<a<b\), the probability that a **single real Gaussian sketch admits at least one negative sketched harmonic Rayleigh quotient** on the extreme-eigenvector plane has the exact form
\[
\Pr\bigl(\exists v\in E\setminus\{0\}:\; h_S(v)<0\bigr)
=I_{\delta}\!\left(\frac{s-1}{2},\frac12\right),
\qquad \delta=\left(\frac{b-a}{b+a}\right)^2.
\]
Here the vector may be selected *after* the sketch is observed, and \(I\) is the regularized incomplete beta function. For \(s=3\), the probability simplifies to \(1-2\sqrt{ab}/(a+b)\). With \(b/a=9\), it equals \(2/5\). This is not the probability of failure at any fixed sketch-independent vector.

The companion deterministic statement is exact: \(\|W-I\|_2<\rho_*\), with \(\rho_*=2\sqrt{ab}/(a+b)\), ensures positivity of every sketched bilinear denominator \(\langle Av,Wv\rangle\) for every SPD \(W\); equality is the first possible zero, and any larger radius below one permits a negative denominator. For dimensions above two, the Gaussian formula concerns the extreme-eigenvector plane, not an asserted exact full-space risk.

## Assumptions and scope
Fix \(N\ge2\) and a real symmetric positive-definite \(N\times N\) matrix \(A\) with smallest and largest eigenvalues \(0<a<b\), each attained by orthonormal eigenvectors \(u_a,u_b\). Let \(E=\operatorname{span}\{u_a,u_b\}\). For integer \(s\ge2\), let \(S\in\mathbb R^{s\times N}\) have independent \(N(0,1)\) entries. For nonzero \(v\in E\) with nonzero denominator define
\[
h_S(v)=\frac{\|SAv\|_2^2}{\langle SAv,Sv\rangle}.
\]
No regularized or absolute-valued denominator is used. The sketch is sampled once, then the existentially quantified vector may depend on it. The relevant two columns of \(S\) have full rank almost surely when \(s\ge2\), so a negative denominator implies a strictly negative quotient. Standard Gaussian scaling by \(1/\sqrt s\) does not change signs.

For the deterministic result \(W\) is any real SPD matrix of size \(N\), unrelated to the rank of \(S\); its bound controls the bilinear denominator \(\langle Av,Wv\rangle\). If \(a=b\), that denominator is positive for every SPD \(W\) and the strict-frontier statement is inapplicable.

## Proof
**1. Reduction to one random correlation.** In the eigenbasis of \(E\), the sketch restriction \(G=S[u_a,u_b]\) has independent standard Gaussian entries and \(C=G^TG=\begin{pmatrix} c_{11}&c_{12}\\ c_{12}&c_{22}\end{pmatrix}\) is SPD almost surely. The denominator for \(v\in E\) is its quadratic form under
\[
H=\frac12\left(\begin{pmatrix}a&0\\0&b\end{pmatrix}C+C\begin{pmatrix}a&0\\0&b\end{pmatrix}\right)
=\begin{pmatrix}a c_{11}&(a+b)c_{12}/2\\(a+b)c_{12}/2&b c_{22}\end{pmatrix}.
\]
Both diagonal entries are positive. Therefore \(H\) has a negative eigenvalue if and only if \(\det H<0\), or equivalently
\[
\left|\frac{c_{12}}{\sqrt{c_{11}c_{22}}}\right|>\rho_*,\qquad
\rho_*=\frac{2\sqrt{ab}}{a+b}.
\]
Whenever \(H\) has a negative eigenvalue, its negative eigendirection has a negative quotient because \(G\) has rank two and the numerator is strictly positive for nonzero \(v\).

**2. Exact Gaussian law.** Write \(g_1,g_2\in\mathbb R^s\) for the two independent columns of \(G\). Their normalized inner product \(R=\langle g_1,g_2\rangle/(\|g_1\|\|g_2\|)\) is the first coordinate of an independent uniformly distributed direction on the unit sphere \(\mathbb S^{s-1}\), after rotation. Consequently \(R^2\sim\operatorname{Beta}(1/2,(s-1)/2)\). Since \(1-\rho_*^2=((b-a)/(b+a))^2\), the probability \(\Pr(R^2>\rho_*^2)\) is precisely
\[
I_{((b-a)/(b+a))^2}\left(\frac{s-1}2,\frac12\right).
\]
For \(s=3\), \(R\) is uniform on \([-1,1]\) and the expression is \(1-\rho_*\).

**3. Universal sharp deterministic threshold.** For every \(v\ne0\), set \(t=\langle Av,v\rangle/\|v\|^2\in[a,b]\). The spectral inequality \((A-aI)(bI-A)\succeq0\) implies
\[
\frac{\langle Av,v\rangle^2}{\|Av\|^2\|v\|^2}
\ge \frac{t^2}{(a+b)t-ab}\ge \frac{4ab}{(a+b)^2}=\rho_*^2.
\]
The scalar minimum occurs at \(t=2ab/(a+b)\). Therefore, writing \(W=I+E_W\),
\[
\langle Av,Wv\rangle
\ge (\rho_*-\|E_W\|_2)\,\|Av\|\,\|v\|>0
\]
whenever \(\|W-I\|_2<\rho_*\).

To show sharpness, choose unit \(v=\sqrt{b/(a+b)}\,u_a+\sqrt{a/(a+b)}\,u_b\) and unit \(x=Av/\|Av\|\); their inner product is \(\rho_*\). Define the symmetric orthogonal Householder reflector \(U=I-2zz^T\), where \(z=(v-x)/\|v-x\|\), so \(Uv=x\). For every \(0\le\varepsilon<1\) the matrix \(W_\varepsilon=I-\varepsilon U\) is SPD with \(\|W_\varepsilon-I\|_2=\varepsilon\), and
\[
\langle Av,W_\varepsilon v\rangle=\|Av\|(\rho_*-\varepsilon).
\]
It vanishes exactly at \(\varepsilon=\rho_*\), and is negative when \(\rho_*<\varepsilon<1\). This construction uses the two extreme modes and embeds unchanged in any ambient dimension.

## Verification
The companion self-contained `verify.py` checks the determinant criterion on 1,500 sampled SPD two-mode pairs, the sharp reflector construction on hundreds of synthetic spectra, and the beta probability against 480,000 seeded simulated sketches at sample dimensions 2, 3, 5 and 8, together with additional controlled norm calculations. The verifier reports 5,612 passed deterministic checks. Finite numerical checks are diagnostic: the universal claims rest on the determinant identity, exact spherical beta law, and spectral inequality established above. Requires Python with NumPy and SciPy; run `python verify.py` in the same directory.

## Relationship to prior work
Güttel, Liu and Nyman (2026) develop sketch-and-restart and sketched harmonic Arnoldi. The accessible abstract states their convergence result for Stieltjes functions on positive-real matrices; the motivating full text was unavailable for a decisive exhaustive comparison. A prior fixed-vector analysis of one-dimensional Gaussian-sketched harmonic Ritz values already gives an exact reciprocal Student law, heavy tails, and sharp **fixed-before-sketch** sign risk. It does *not*, by itself, yield the probability of the **single common sketch admitting some post-sketch selected vector** with a negative quotient, which is a different order of quantifiers. The present result is restricted to that uniform extreme-eigenplane event and its deterministic sharp distortion boundary. Classical spherical beta laws and the cosine inequality are ingredients, not claimed as discoveries.

## Limitations
This is an exact-arithmetic, real-Gaussian, SPD, one-dimensional harmonic-quotient theorem, not a convergence theorem for restarted Arnoldi or matrix-function approximation. When \(N>2\), the beta formula is a lower bound for the full-space existential failure event, not its full-space probability. The sketch-dependent vector need not arise in an actual fixed-start-vector Krylov iteration. The motivating 2026 full manuscript and some adjacent specialist literature could not be read in full, so independent historical-priority examination remains appropriate. The numerical verifier does not establish infinite-parameter claims; the proof does.

## References
1. S. Güttel, J. Liu, and L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354, originally submitted 11 July 2026.
2. *Sharp negative-Ritz risk and universal inverse tails for one-dimensional Gaussian-sketched harmonic Arnoldi*, prior mathematical finding, opaque identifier `16336c9a-1e80-4709-ae3a-89d629a714c3`. Its fixed-before-sketch guarantee is distinguished from the present uniform event.
3. *A homogeneous Rayleigh quotient with applications in gradient methods*, arXiv:2206.13457 (deterministic harmonic quotient background).
