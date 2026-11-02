# A universal one-sixteenth projection defect for harmonic concentration on conformal annuli

## Finding
Fix any \(0<a<1\), and put \(L=\log(1/a)\). On the planar annulus \(A_a=\{z\in\mathbb C:a<|z|<1\}\), let \(\mathcal H_a\) be the complex-valued harmonic subspace of \(L^2(A_a,|z|^{-2}dA(z))\). Let \(P_a\) be its orthogonal projection and let \(T_a=P_a\mathbf 1_{\{a<|z|<\sqrt a\}}|_{\mathcal H_a}\). The operator is a positive contraction.

Its complete point spectrum consists of the two simple eigenvalues
\[
\lambda_{0,\pm}=\frac{2\pm\sqrt3}{4}
\]
and, for every integer \(n\ge1\), the paired eigenvalues
\[
\lambda_{n,\pm}=\frac12\left(1\pm
\frac{\cosh(nL)-1}{\sqrt{\sinh^2(nL)-(nL)^2}}\right),
\]
each with complex multiplicity two (the angular Fourier frequencies \(n\) and \(-n\)). Every eigenvalue lies strictly between zero and one. The pairs sum to one, their lower branches decrease strictly with \(n\), and
\[
\sigma(T_a)=\{0,1\}\cup\{\lambda_{0,-},\lambda_{0,+}\}
 \cup \{\lambda_{n,\pm}:n\ge1\}.
\]
In particular, the universal projection-defect identity
\[
\boxed{\ \|T_a-T_a^2\|=\frac1{16}\ }
\]
holds for *every* modulus. The supremum is attained only on the two-dimensional zero-angular-frequency subspace; there is a uniform open forbidden spectral interval \(\big((2-\sqrt3)/4,(2+\sqrt3)/4\big)\).

Let \(Q_a=\mathbf 1_{(1/2,1]}(T_a)\) be the spectral projection onto the upper branch. The compact defect \(D_a=T_a-Q_a\) belongs to every Schatten class \(S_p\) for \(p>0\), and its positive singular values satisfy
\[
\lambda_{n,-}\sim e^{-nL}\quad(n\longrightarrow\infty),\qquad
N_{D_a}(\varepsilon)=\frac4L\log\frac1\varepsilon+O_a(1)
\quad(\varepsilon\downarrow0),
\]
where \(N_{D_a}(\varepsilon)=\#\{k:s_k(D_a)>\varepsilon\}\), counting multiplicities. Hence this spectral counting coefficient recovers the conformal modulus \(L\).

Among all concentric cuts \(\{a<|z|<b\}\) with \(a<b<1\), the cut \(b=\sqrt a\) is uniquely characterized by the property that the two eigenvalues in **every** angular Fourier block sum to one.

## Assumptions and scope
The measure is precisely the cylindrical/conformally invariant volume \(|z|^{-2}dA(z)\), not ordinary Euclidean area. Harmonic means \(\Delta u=0\), permitting the harmonic logarithmic mode; it does not mean holomorphic. The Hilbert inner product is complex linear in one argument and its normalization by an overall positive constant has no spectral effect. All statements hold for every real \(L>0\), with no small- or large-modulus assumption. The eigenvalues are for \(T_a\) as an operator on the *full infinite-dimensional* harmonic Bergman space.

## Proof
**1. Cylinder coordinates and complete Fourier decomposition.** Put \(s=\log(|z|/\sqrt a)\) and \(h=L/2\). Then \(s\in(-h,h)\), \(|z|^{-2}dA(z)=ds\,d\theta\), and the selected inner half-annulus corresponds to \(-h<s<0\). Harmonic functions obey \((\partial_s^2+\partial_\theta^2)u=0\). Angular Fourier decomposition is orthogonal both for the full norm and for the truncated norm. In degree \(n\neq0\) a basis is \(e^{|n|s}e^{in\theta}\), \(e^{-|n|s}e^{in\theta}\); in degree zero a basis is \(1,s\). By Fourier orthogonality, these blocks span the Hilbert space densely. The concentration operator is the orthogonal sum of the two-by-two generalized Gram operators for these bases.

**2. Nonzero Fourier degrees.** Fix \(n=|m|\ge1\), suppress the harmless angular factor \(2\pi\), and use basis \((e^{ns},e^{-ns})\). The full Gram matrix and inner-half Gram matrix are
\[
G_n=\begin{pmatrix}\sinh(nL)/n&L\\L&\sinh(nL)/n\end{pmatrix},\quad
H_n=\begin{pmatrix}(1-e^{-nL})/(2n)&L/2\\L/2&(e^{nL}-1)/(2n)\end{pmatrix}.
\]
Thus \(H_n-G_n/2=\operatorname{diag}(-d_n,d_n)\), with \(d_n=(\cosh(nL)-1)/(2n)\). Since \(G_n\) is positive definite with
\(\det G_n=(\sinh^2(nL)-(nL)^2)/n^2\), the generalized eigenvalues of \((H_n,G_n)\) are \(1/2\pm d_n/\sqrt{\det G_n}\). This proves the stated pair exactly. The degrees \(m=n\) and \(m=-n\) are distinct and identical blocks, so each such eigenvalue has multiplicity two.

**3. Zero degree.** In basis \((1,s)\), the full Gram matrix is diagonal with entries \(L,L^3/12\). The half-cylinder matrix is
\[
H_0=\begin{pmatrix}L/2&-L^2/8\\-L^2/8&L^3/24\end{pmatrix}.
\]
After Gram normalization the matrix is \(\begin{pmatrix}1/2&-\sqrt3/4\\-\sqrt3/4&1/2\end{pmatrix}\), proving \(\lambda_{0,\pm}\).

**4. Strict ordering and forbidden interval.** Let
\(q(x)=(\cosh x-1)/\sqrt{\sinh^2x-x^2}\) for \(x>0\). Its continuous extension has \(q(0)=\sqrt3/2\), by Taylor expansion. Since
\[
\sinh^2x-x^2-(\cosh x-1)^2=2(\cosh x-1)-x^2>0,
\]
we have \(0<q(x)<1\) for every \(x>0\). The sign of \(q'(x)\) is the sign of
\[
F(x)=(\cosh x-1)(\sinh x+x)-x^2\sinh x
=\sum_{k=3}^{\infty}\frac{4^k-4k^2}{(2k+1)!}x^{2k+1}>0.
\]
Every coefficient is strictly positive because \(2^k>2k\) for integers \(k\ge3\). Hence \(q\) grows strictly from \(\sqrt3/2\) to one. Each \(\lambda_{n,-}\) for \(n\ge1\) is strictly smaller than \(\lambda_{0,-}\), and each \(\lambda_{n,+}\) strictly larger than \(\lambda_{0,+}\); no mid-gap eigenvalues exist. As \(t(1-t)\) is largest within these two spectral branches at their closest points to \(1/2\), we have \(\|T_a-T_a^2\|=\lambda_{0,-}\lambda_{0,+}=1/16\); only zero-frequency eigenvectors attain this norm.

**5. Essential spectrum and logarithmic counting.** Elementary expansion as \(x\to\infty\) gives \(q(x)=1-2e^{-x}+O(x^2e^{-2x})\). Therefore \(\lambda_{n,-}=e^{-nL}(1+O((nL)^2e^{-nL}))\) for fixed \(L>0\), and \(\lambda_{n,+}=1-\lambda_{n,-}\). The closure of the direct-sum eigenvalue list adds exactly the two accumulation points zero and one, which constitute the essential spectrum. Every block of \(D_a=T_a-Q_a\) has two eigenvalues equal in absolute value to \(\lambda_{n,-}\) (both zero-degree eigenvalues for \(n=0\)), with angular multiplicity two for each \(n\ge1\). Hence \(D_a\) has singular values \(\lambda_{0,-}\) twice and \(\lambda_{n,-}\) four times for each \(n\ge1\). Its \(S_p\) summability follows from exponential decay. The count of degrees satisfying \(\lambda_{n,-}>\varepsilon\) is \(L^{-1}\log(1/\varepsilon)+O_a(1)\), proving the fourfold counting law.

**6. Uniqueness of the balanced cut.** For a general concentric radius \(a<b<1\), put \(c=\log(b/\sqrt a)\), so \(-L/2<c<L/2\). Restricting the zero-frequency Gram form to \((-L/2,c)\), its generalized trace is
\[
\operatorname{tr}(G_0^{-1}H_{0,c})
=1+\frac{c}{L}+4\left(\frac{c}{L}\right)^3.
\]
The trace equals one if and only if \(c=0\), because \(u+4u^3=0\) has only the real solution \(u=0\). The geometric-middle cut makes every frequency trace one by steps 2–3, and any competing cut with that property must have zero-frequency trace one. Thus it is unique.

## Verification
The standalone \(\texttt{verify.py}\) uses no third-party dependencies. It independently constructs full and truncated two-by-two Gram matrices by Simpson quadrature, solves their generalized characteristic polynomials, compares results with the closed formulas at five moduli and nine degrees, and checks finite ordering and endpoint behavior. Running \(\texttt{python3 verify.py}\) produced **271 passing finite assertions**. These tests do not verify infinitely many modes; the infinite-dimensional claims are proved analytically in the preceding steps.

## Relationship to prior work
Harmonic Bergman-space constructions and Toeplitz-operator methods are established for real hyperbolic balls and harmonic Bergman–Besov spaces. Üreyen's 2023 preprint studies atomic decompositions, interpolation and inclusion of such spaces; Doğan's 2022 preprint studies positive Toeplitz operators and Carleson/Schatten criteria on harmonic balls. Those general frameworks do not assert the displayed half-log-annulus matrix spectrum, universal one-sixteenth defect, or inverse-modulus counting law. Earlier Toeplitz/Hankel work on annuli uses holomorphic weighted Bergman spaces, which are not the present full harmonic cylinder space. The present proof is self-contained once the Fourier decomposition of harmonic functions on a cylinder is recalled. These comparisons support provisional originality, not a claim that all historical literature has been exhausted.

## Limitations
The metric \(|z|^{-2}dA\) and the central logarithmic cut are essential for the universal constant and exact complementary pairing. Ordinary-area harmonic Bergman annuli, off-centre cuts, nonconcentric observation sets and noncircular domains are not covered by the universal formula. The logarithmic counting law is asymptotic for each fixed annulus and is not a uniform thin-annulus statement. A plausible older annular Toeplitz paper was available only as an extract; its complete text has not been examined. No independent mathematical audit or validation has been performed.

## References
1. İ. Üreyen, *Harmonic Bergman Spaces on the Real Hyperbolic Ball: Atomic Decomposition, Interpolation and Inclusion Relations*, arXiv:2303.12137v1, first publicly posted 2023-03-21. https://arxiv.org/abs/2303.12137
2. Ö. F. Doğan, *Positive Toeplitz Operators from a Harmonic Bergman-Besov space into Another*, arXiv:2202.12771v1, first publicly posted 2022-02-25. https://arxiv.org/abs/2202.12771
3. Z. Jiang and L. Peng, *Toeplitz and Hankel type operators on an annulus*, 1994; publisher extract consulted, full text not inspected. https://www.cambridge.org/core/search?q=Toeplitz%20and%20Hankel%20type%20operators%20on%20an%20annulus
