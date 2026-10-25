# Arithmetic entropy bifurcation in stride-three coupled cat maps

## Finding

For each integer \(n\ge 3\), let \(S_n\) be the **stride-three connection set**

\[
S_n=\{k\in\{1,\ldots,n-1\}: k\equiv1\pmod 3\ \text{or}\ n-k\equiv1\pmod 3\},
\]

and let \(C_n\) be the symmetric circulant adjacency matrix on \(\mathbb Z/n\mathbb Z\) with \((C_n)_{ab}=\mathbf 1_{\{(b-a)\bmod n\in S_n\}}\). Let the associated integral symplectic toral automorphism be induced by

\[
M_n=\begin{pmatrix}I_n&C_n\\C_n&I_n+C_n^2\end{pmatrix}.
\]

Write \(h_n\) for its Kolmogorov–Sinai entropy relative to normalized Haar measure, use natural logarithms, and set \(\Phi(t)=2\operatorname{arsinh}(|t|/2)\). There are three **exact spectral and asymptotic regimes**:

1. For \(n=3m\), \(m\ge1\), the adjacency spectrum is \(2m,-m,-m\) and \(n-3\) zeros, so
\[
h_{3m}=\Phi(2m)+2\Phi(m)=6\log m+2\log2+o(1).
\]
2. For \(n=3m+1\), \(m\ge1\), the adjacency spectrum consists of \(2m\) and
\[
d_j=-\frac{2\cos(2\pi j/n)}{1+2\cos(2\pi j/n)},\qquad 1\le j<n.
\]
3. For \(n=3m+2\), \(m\ge1\), the adjacency spectrum consists of \(m+1\) and
\[
d_j=\frac{1}{1+2\cos(2\pi j/n)},\qquad 1\le j<n.
\]

For \(a=1,2\), define the finite, strictly positive improper integrals
\[
\begin{aligned}
c_1&=\frac1{2\pi}\int_0^{2\pi}\Phi\!\left(-\frac{2\cos\theta}{1+2\cos\theta}\right)d\theta,\\
c_2&=\frac1{2\pi}\int_0^{2\pi}\Phi\!\left(\frac1{1+2\cos\theta}\right)d\theta.
\end{aligned}
\]
Then
\[
\lim_{m\to\infty}\frac{h_{3m+1}}{3m+1}=c_1>0,\qquad
\lim_{m\to\infty}\frac{h_{3m+2}}{3m+2}=c_2>0,
\]
where numerical quadrature suggests \(c_1\approx1.39098\) and \(c_2\approx1.27372\). In particular, \(C_{3m}\) and \(C_{3m+1}\) both have **exact vertex degree \(2m\)**, yet their entropies are respectively logarithmic and asymptotically linear in the number of sites. Equivalently,
\[
h_{3m+1}-h_{3m}\sim 3c_1m.
\]
This is a size-congruence transition in entropy scaling at fixed degree, within one canonical stride construction.

## Assumptions and scope

The adjacency entries are precisely zero or one; self-loops are excluded. The torus is \((\mathbb R/\mathbb Z)^{2n}\), with the continuous deterministic update induced by \(M_n\). Its measure is the normalized Haar probability; no hyperbolicity assumption is imposed. The entropy is not divided by the number of sites unless explicitly indicated. The stride definition is the union of the two congruence conditions; changing the convention or adding self-loops may change the answer. The two displayed integrals are interpreted as improper integrals at \(\theta=2\pi/3\) and \(\theta=4\pi/3\).

## Proof

**1. Entropy from the adjacency spectrum.** The symmetric matrix \(C_n\) is orthogonally diagonalizable, with real eigenvalues \(d_j\). On the two-dimensional real block for one eigenvalue \(d\), \(M_n\) is
\[
B(d)=\begin{pmatrix}1&d\\d&1+d^2\end{pmatrix},\qquad \det B(d)=1.
\]
Its characteristic polynomial is \(\lambda^2-(2+d^2)\lambda+1\); the larger eigenvalue is \(\exp(\Phi(d))\). Thus the standard entropy formula for an integral toral automorphism (counting expanding eigenvalues with multiplicity) gives
\[
h_n=\sum_{j=0}^{n-1}\Phi(d_j).
\]
The formula includes \(d_j=0\), for which the corresponding block is the identity and contributes zero entropy. It applies to Haar entropy without requiring Haar ergodicity.

**2. Exact divisible case.** If \(n=3m\), the connection residues are \(1\) and \(2\) modulo three, so the graph is the balanced complete tripartite graph with three parts of size \(m\). Its adjacency spectrum is \(2m,-m,-m,0\) (the last eigenvalue with multiplicity \(3m-3\)). Substituting it into the preceding entropy formula gives the exact answer. Since \(\Phi(t)=2\log t+O(t^{-2})\) for positive \(t\to\infty\), the stated logarithmic asymptotic follows.

**3. Exact nondivisible spectra.** Put \(P_n(z)=\sum_{k\in S_n}z^k\) and \(Q_n(z)=1+z+\cdots+z^{n-1}\). If \(n=3m+1\), the connection set is \(\{1+3\ell,3+3\ell:0\le\ell<m\}\), and direct polynomial multiplication gives the identity
\[
(1+z+z^2)P_n(z)+(1+z^2)=(1+z^2)Q_n(z).
\]
If \(n=3m+2\), the connection set is \(\{1+3\ell:0\le\ell\le m\}\), and the corresponding polynomial identity is
\[
(1+z+z^2)P_n(z)-z=z^2Q_n(z).
\]
These are identities in \(\mathbb Z[z]\), not approximations. At each nontrivial \(n\)-th root of unity \(z=\exp(2\pi i j/n)\), \(Q_n(z)=0\). Moreover \(1+z+z^2\ne0\), since \(3\nmid n\). The two identities consequently yield respectively
\[
P_n(z)=-\frac{1+z^2}{1+z+z^2}=-\frac{2\cos(2\pi j/n)}{1+2\cos(2\pi j/n)}
\]
and
\[
P_n(z)=\frac{z}{1+z+z^2}=\frac{1}{1+2\cos(2\pi j/n)}.
\]
The Fourier mode at \(j=0\) equals the vertex degree, respectively \(2m\) and \(m+1\). This proves the entire finite-size spectrum. In particular, the degrees of the consecutive graphs \(C_{3m}\) and \(C_{3m+1}\) coincide.

**4. Passage to the singular integral.** For each \(a\in\{1,2\}\), write \(f_a(\theta)=\Phi(R_a(\theta))\), where \(R_a\) is the corresponding rational trigonometric expression above. Its only poles on the circle are at \(2\pi/3\) and \(4\pi/3\). Near either pole, \(|R_a(\theta)|\) has at most a simple pole, and therefore
\[
0\le f_a(\theta)\le A+B\log^+\!\left(\frac1{\operatorname{dist}(\theta,\{2\pi/3,4\pi/3\})}\right)
\]
for fixed finite constants \(A,B\) away from the pole points. This majorant is integrable. On any closed arcs staying a fixed distance from the poles, the equally spaced Riemann sums of \(f_a\) converge to their integrals. Since \(3\nmid n\), each sampled angle lies at least \(2\pi/(3n)\) from each pole. The total normalized contribution from samples at distance at most \(\delta\) from one pole is bounded, uniformly up to a vanishing \(O(\log n/n)\) term, by a constant multiple of
\[
\frac1n\sum_{k=1}^{\lceil\delta n\rceil}\left[1+\log\left(\frac{n}{k}\right)\right]
=O\bigl(\delta(1+|\log\delta|)\bigr)+O(\log n/n).
\]
The corresponding integral contribution obeys the same vanishing bound as \(\delta\downarrow0\). Truncation followed by this uniform-integrability estimate proves convergence of the full Riemann sums to the improper integrals. The distinguished degree eigenvalue contributes \(\Phi(2m)/n\) or \(\Phi(m+1)/n\), both tending to zero. Thus \(h_{3m+a}/(3m+a)\to c_a\). Both constants are positive because the integrands are nonnegative and nonzero on sets of positive measure.

**5. Degree-preserving contrast.** The two consecutive sizes \(3m\) and \(3m+1\) have the same degree \(2m\). Their entropies are \(O(\log m)\) and \(c_1(3m+1)+o(m)\), respectively, proving the last asymptotic.

## Verification

The standalone standard-library script `checks/verify_stride3.py` verifies the polynomial identities with exact integer coefficients for \(3\le n\le500\), the complete discrete Fourier spectra for \(3\le n\le120\), and the equal-degree identity for \(1\le m<100\). It also performs numerical quadrature and large-site entropy diagnostics. Execute `python3 checks/verify_stride3.py` from the package root; recorded output is in `checks/output.txt`. The exact universal proof is the polynomial and Riemann-sum argument above, not finite extrapolation. The numerical integral estimates are descriptive, not certified bounds.

## Relationship to prior work

Manolas and Floratos (arXiv:2605.00965, Sections 3–4 and Appendix B) introduce these symplectic circulant cat maps, define the stride connection sets in their Eq. (43), and give the general finite-dimensional Fourier–Lyapunov entropy formula. They document numerically how structured connectivity suppresses entropy; they do not state the modulo-three entropy-scaling transition, the exact rational spectra along the two nondivisible size classes, or the equal-degree logarithmic-versus-extensive comparison. The general entropy formula is an essential starting point; the contribution claimed here is the **arithmetic asymptotic classification**, not invention of the map or its entropy formula. Axenides, Floratos and Nicolis (arXiv:2208.03267, Sections 3–5 and Appendix B) supply the underlying symplectic cat-map lattice theory and zero-mode background, without this stride-three size-residue law. An indexed independent result, *Exact powers-of-two torus orders for all-to-all coupled cat maps*, treats permutation orders modulo powers of two for complete graphs, not Haar entropy in the stride-three family. Standard circulant spectral theory already supplies the Fourier diagonalization; it does not itself evaluate the nonuniform three-class limits.

## Limitations

The theorem is restricted to the stated binary stride-three adjacency family, its corresponding integral toral map, and Haar entropy. It does not imply positive entropy density for other stride patterns, arbitrary weighted circulants, or random graph sequences. The divisible-size matrices have many neutral modes, so these systems need not be ergodic with respect to Haar measure. Values of the two improper integrals were estimated numerically; neither an elementary closed form nor a proved inequality between the constants is asserted. The literature comparison cannot exclude an earlier equivalent thermodynamic-limit calculation under other terminology; the finite-size entropy formula predates this analysis.

## References

1. K. Manolas and E. Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965v2, first submitted May 1, 2026; Sections 3–5 and Appendix B. https://arxiv.org/html/2605.00965v2
2. M. Axenides, E. Floratos and S. Nicolis, *Arnol'd cat map lattices*, arXiv:2208.03267, first submitted August 5, 2022; Sections 3–5 and Appendix B. https://arxiv.org/abs/2208.03267
3. *Exact powers-of-two torus orders for all-to-all coupled cat maps*, public research record, October 11, 2026; statement and proof compared for a distinct finite-torus invariant. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-powers-of-two-torus-orders-for-all-to-all-coupled-cat-maps--6ce73c0ff68d
