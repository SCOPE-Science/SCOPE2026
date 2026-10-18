# Exact Fibonacci relative-mixing norms on the commuting locus of quaternionic cat-map lifts

## Finding
Let \(A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\) and let \(F\) be any quaternionic Nielsen diffeomorphism of \(\mathrm{SU}(2)^2\) whose abelianization has row-exponent matrix \(A\). Let \(\mathcal C\) denote the closed invariant locus of commuting pairs of unit quaternions. There is a canonical invariant probability measure \(\nu\) on \(\mathcal C\), defined below, which is not ergodic. Its ergodic decomposition is the family of Haar measures on the invariant maximal two-tori, indexed by the unoriented axes \(\mathbb{RP}^2\).

For every \(0<\rho<1\), define the analytic fiber Hilbert norm \(\|\cdot\|_\rho\) and projection \(P\) below. The **optimal conditional correlation error at every integer time \(n\ge0\)** is exactly
\[
\sup_{\|f\|_\rho,\|g\|_\rho\le1}
\left|\int_{\mathcal C}(f\circ F^n)\overline g\,d\nu
-\int_{\mathcal C}(Pf)\overline{Pg}\,d\nu\right|
=\rho^{F_{n+3}},
\]
where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\) are Fibonacci numbers. Every bound is attained by a pair of real analytic cosine observables constant in the quaternionic-axis variable. The first decay exponents are \(2,3,5,8,13,21,\ldots\). All quaternionic Nielsen lifts of the same matrix have this identical optimal conditional-mixing profile.

Consequently, although \((\mathcal C,F,\nu)\) fails ordinary mixing, it is mixing relative to its invariant-axis factor. For any \(f,g\in L^2(\nu)\), the displayed correlation difference tends to zero, with the stated sharp double-exponential rate for the specified analytic class.

## Assumptions and scope
Identify \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), and write \(\sigma\) for normalized spherical area on \(S^2\) and \(m\) for normalized Haar measure on \(\mathbb T^2\). Define the continuous surjection
\[
\Psi:S^2\times\mathbb T^2\longrightarrow\mathcal C,
\qquad \Psi(u,(s,t))=(e^{2\pi u s},e^{2\pi u t}),
\]
where \(u\) is a purely imaginary unit quaternion. Away from the four central quaternion pairs, the sole ambiguity is \((u,z)\sim(-u,-z)\). Put \(\nu=\Psi_*(\sigma\otimes m)\). The Nielsen word-map property gives
\[F(\Psi(u,z))=\Psi(u,Az).\]
Thus a \(\nu\)-measurable observable \(f\) is represented by a function \(\widetilde f(u,z)=f(\Psi(u,z))\) satisfying \(\widetilde f(-u,-z)=\widetilde f(u,z)\). Let \(\widehat f_u(k)=\int_{\mathbb T^2}\widetilde f(u,z)e^{-2\pi i k\cdot z}\,dm(z)\). For \(0<\rho<1\) let
\[
\|f\|_\rho^2=\int_{S^2}\sum_{k\in\mathbb Z^2}
\rho^{-2\|k\|_1}|\widehat f_u(k)|^2\,d\sigma(u),
\quad\|k\|_1=|k_1|+|k_2|.
\]
The Hilbert space \(\mathcal H_\rho\) consists of classes of observables of finite such norm. The orthogonal projection onto the invariant-axis factor is \(Pf\) with pullback \(\widetilde{Pf}(u,z)=\widehat f_u(0)\). The axis function is even in \(u\), so this is well-defined. For each \(u\), the Fourier series of a member of \(\mathcal H_\rho\) is analytic in a uniform positive complex strip in \(z\), in the Hilbert/fiberwise sense. Statements concern \(\nu\), which is singular relative to six-dimensional product Haar volume; no conclusion about ambient Haar mixing is made.

## Proof
**Invariant measure and ergodic components.** Every quaternionic Nielsen lift with exponent matrix \(A\) restricts to \(z\mapsto Az\) on each commuting maximal torus. Therefore \(\nu\) is invariant. The symmetric hyperbolic integral matrix \(A\) is a toral automorphism, and its nonzero Fourier characters move to infinity under iteration; it is mixing for \(m\). For each unoriented axis \([u]\in\mathbb{RP}^2\), Haar measure on \(\Psi(\{u\}\times\mathbb T^2)\) is an ergodic probability. The disintegration of \(\nu\) over \(\mathbb{RP}^2\) is exactly these probabilities. Hence the invariant \(L^2(\nu)\) subspace consists of functions of \([u]\), and its conditional expectation is \(P\). Since \(\mathbb{RP}^2\) carries a nontrivial probability space, \(\nu\) is not ergodic.

**Fourier diagonalization.** For finite Fourier series, orthogonality on each torus and symmetry of \(A\) give the exact identity
\[
\langle f\circ F^n,g\rangle_{L^2(\nu)}-\langle Pf,Pg\rangle_{L^2(\nu)}
=\int_{S^2}\sum_{k\ne0}\widehat f_u(k)\overline{\widehat g_u(A^n k)}\,d\sigma(u).
\]
The indexing \(k\mapsto A^n k\) permutes the nonzero lattice. By Cauchy--Schwarz in the weighted Fourier spaces, the corresponding bilinear operator norm is at most
\[
\rho^{D_n},\qquad
D_n:=\min_{k\in\mathbb Z^2\setminus\{0\}}
\bigl(\|k\|_1+\|A^nk\|_1\bigr).
\]
This argument extends by density to all \(f,g\in\mathcal H_\rho\). For any minimizing \(k\), take
\[
\widetilde f(u,z)=\sqrt2\,\rho^{\|k\|_1}\cos(2\pi k\cdot z),
\qquad \widetilde g(u,z)=\sqrt2\,\rho^{\|A^nk\|_1}\cos(2\pi(A^nk)\cdot z).
\]
These are invariant under \((u,z)\mapsto(-u,-z)\), have Hilbert norms one, have zero conditional means, and attain the value \(\rho^{D_n}\). Therefore this is the exact operator norm, not merely an upper bound.

**Exact lattice minimum.** Set \(M=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), so \(A=M^2\) and \(\det M=-1\). Write \(v=M^nk\), a bijection on the nonzero integer lattice. Then
\[
D_n=\min_{v\in\mathbb Z^2\setminus\{0\}}
\bigl(\|M^{-n}v\|_1+\|M^nv\|_1\bigr).
\]
For \(n\ge1\), Fibonacci identities give
\[
M^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix},
\quad M^{-n}=(-1)^n\begin{pmatrix}F_{n-1}&-F_n\\-F_n&F_{n+1}\end{pmatrix}.
\]
For \(v=(a,b)\) and \(L_n=F_{n+1}+F_{n-1}\), the triangle inequality applied to pairs of coordinates implies
\[
\|M^nv\|_1+\|M^{-n}v\|_1\ge L_n(|a|+|b|).
\]
Indeed, pairing the first coordinate of \(M^nv\) with the first coordinate of \((-1)^nM^{-n}v\) cancels the \(F_nb\) terms and gives \(L_n|a|\); pairing second coordinates cancels the \(F_na\) terms and gives \(L_n|b|\). When \(v\in\{\pm e_1,\pm e_2\}\), the cost equals
\(L_n+2F_n=F_{n+3}\).

For \(n\ge2\), \(n\ne3\), we have \(L_n>2F_n\). Any \(v\) with \(\|v\|_1\ge2\) therefore has cost at least \(2L_n>F_{n+3}\). For \(n=3\), \(L_3=4\), the vectors with \(\|v\|_1\ge3\) have cost at least 12, while the four sign-classes with \(\|v\|_1=2\) have respective costs 16 (coordinate vectors) and 10 (diagonal vectors), all greater than \(F_6=8\). For \(n=1\), direct evaluation yields
\[
\|M^{-1}(a,b)\|_1+\|M(a,b)\|_1
=|a|+|b|+|a+b|+|a-b|
=|a|+|b|+2\max(|a|,|b|),
\]
whose nonzero minimum is \(3=F_4\), only at \(\pm e_1,\pm e_2\). At \(n=0\), the minimum is \(2=F_3\). Thus, for all \(n\ge0\),
\[
D_n=F_{n+3},\qquad
\{k:\|k\|_1+\|A^nk\|_1=D_n\}=\{\pm M^{-n}e_1,\pm M^{-n}e_2\}.
\]
This also supplies every sharp cosine witness claimed above.

**Relative mixing.** Finite Fourier series in the torus coordinate are dense in \(L^2(\nu)\), respecting the symmetry by averaging each series over the sign involution. For each nonzero Fourier character, \(A^nk\) eventually leaves any fixed finite frequency set, so the relative correlation vanishes for polynomial tests after finitely many sufficiently large times. By \(L^2\)-approximation and unitarity of composition on \(L^2(\nu)\), the relative correlation tends to zero for all \(f,g\in L^2(\nu)\).

## Verification
The accompanying executable `verify.py` checks the Fibonacci matrix-power identities, the lattice minimum and its minimizing modes for a range of times by bounded exact-integer enumeration, as well as the sharp Fourier witnesses. These are finite consistency checks: the universal result follows from the preceding inequality proof and the explicit treatment of its exceptional values.

## Relationship to prior work
Verjovsky's 2026 construction establishes invariant maximal tori, quaternionic lifts of integral matrices and their geometric commuting locus. Its explicit Fibonacci cat map is the dynamical input; the source does not state a quantitative conditional-mixing theorem or the all-time sharp Fibonacci correlation norm. Slipantschuk, Bandtlow and Just study explicit transfer spectra and analytic-observable correlations for a family of Anosov toral maps using anisotropic Hilbert spaces; their results do not identify the symmetric exponential Fourier norm on this nonergodic commuting-locus disintegration. The contribution here is the exact relative spectral norm and its arithmetically classified sharp witnesses, rather than the already known existence of invariant tori or qualitative mixing of a hyperbolic torus automorphism.

## Limitations
The invariant measure \(\nu\) is supported on the commuting locus of zero ambient six-dimensional Haar measure; the result says nothing about ergodicity or mixing of product Haar measure on \(\mathrm{SU}(2)^2\). The formula applies to the indicated Fourier analytic Hilbert norm and the fixed Fibonacci matrix, not arbitrary analytic norms or exponent matrices. The general method of Fourier weighted minimization is classical; a prior specialization of the final Fibonacci minimization is possible and has not been ruled out by exhaustive bibliography.

## References
1. A. Verjovsky, *Quaternionic Extensions of Hyperbolic Toral Automorphisms*, arXiv:2608.08252, initial public posting 2026-08-08, especially Sections 3, 5--8. https://arxiv.org/abs/2608.08252
2. J. Slipantschuk, O. F. Bandtlow and W. Just, *Complete spectral data for analytic Anosov maps of the torus*, arXiv:1605.02883 (2016), Sections 2 and 4. https://arxiv.org/html/1605.02883v1
