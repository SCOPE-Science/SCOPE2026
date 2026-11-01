# Sharp rare-event law and conditional normal geometry for minimal central cube sections

## Finding
Let \(d\geq 3\), let \(Q_d=[-1,1]^d\), and let \(H_d\) be a Haar-uniform central hyperplane in \(\mathbb R^d\). Write \(N_d\) for the number of vertices of the section \(Q_d\cap H_d\), and put \(m=d-1\). With probability one, the hyperplane contains no cube vertex. Then
\[
N_d\geq 2^{d-1},\qquad
\{N_d=2^{d-1}\}=\left\{\max_i|U_i|>\sum_{j\ne i}|U_j|\text{ for some }i\right\},
\]
where \(U\) is either choice of unit normal to \(H_d\). The coordinate achieving the strict inequality is unique.

The probability \(p_d=\Pr\{N_d=2^{d-1}\}\) has the sharp two-term asymptotic
\[
\boxed{p_d=\frac{d\,2^{d-1}\Gamma(d/2)}{e\,\pi^{d/2}\Gamma(d)}
\left(1+\frac{7}{2(d-1)}+O(d^{-2})\right)}\qquad(d\to\infty).
\]
This is a relative expansion; its leading gamma-factor is not replaced by a less accurate Stirling approximation.

There is also an exact finite-dimensional representation. Let \(Q=(Q_1,\ldots,Q_m)\sim\operatorname{Dirichlet}(1,\ldots,1)\), \(Z^2\sim\chi^2_{m+1}\), and \(V\sim\operatorname{Uniform}[0,1]\), independently; set
\[
S=ZV^{1/m},\quad T=\frac{S^2}{2}\sum_{j=1}^m Q_j^2,\quad B_d=\frac{d\,2^{d-1}\Gamma(d/2)}{\pi^{d/2}\Gamma(d)}.
\]
Then \(p_d=B_d\,\mathbb E[e^{-T}]\) exactly for every \(d\ge3\). In particular, the limiting factor is \(\lim_{d\to\infty}p_d/B_d=e^{-1}\).

Condition on \(N_d=2^{d-1}\), choose its unique dominant index \(I\), and orient the unit normal so that \(U_I>0\). Relabel the other coordinates in increasing original-index order. For each fixed integer \(r\ge1\), as \(d\to\infty\) with \(m\ge r\),
\[
\boxed{\big(m|U_{j_1}|,\ldots,m|U_{j_r}|,\ m(1-U_I)\big)
\ \Longrightarrow\ (E_1,\ldots,E_r,1),}
\]
where \(E_1,\ldots,E_r\) are independent unit-rate exponential variables. Equivalently, the acute angle \(\theta_d=\arccos U_I\) satisfies \(\sqrt m\,\theta_d\to\sqrt2\) in conditional probability. These limits describe the distribution of the *rare normal directions*, not typical cube-section normals.

## Assumptions and scope
All dimensions are integers \(d\ge3\). Hyperplanes are linear, pass through the origin, and are distributed according to rotation-invariant probability on the Grassmannian; the cube has equal positive edge half-lengths. Every asserted exact equality involving a hyperplane holds almost surely; exceptional hyperplanes through cube vertices form a null set. For conditional coordinate statements the dominant index is chosen uniquely on the event and all other coordinate indices retain a deterministic order. The exponential and angle laws are conditional limits as the dimension grows.

## Proof
**1. Vertex minimum and its rigidity.** For a normal \(u\) with nonzero values at all cube vertices, define the sign function \(f:\{-1,1\}^d\to\{-1,1\}\) by \(f(x)=\operatorname{sgn}\langle u,x\rangle\). A cube edge intersects \(H_d\) exactly when its two endpoints have opposite signs. Each such edge meets the section in one vertex, and every section vertex arises from precisely one such edge; hence \(N_d\) is the edge boundary of the positive vertices of \(f\). With the standard orthonormal Walsh characters \(\chi_A(x)=\prod_{i\in A}x_i\), Parseval and the influence identity give
\[
N_d=2^{d-1}\sum_{i=1}^d\operatorname{Inf}_i(f)
=2^{d-1}\sum_{A\subseteq[d]}|A|\,\widehat f(A)^2.
\]
The function \(f\) is odd, so its constant Fourier coefficient vanishes; Parseval gives \(N_d\ge2^{d-1}\). At equality all nonzero coefficients have degree one. A Boolean linear form must be one signed coordinate: if \(f=\sum_i a_ix_i\), then the off-diagonal coefficients in \(f^2\equiv1\) force \(a_ia_j=0\) for all \(i\ne j\), and normalization forces the remaining coefficient to be \(\pm1\). The sign of a linear form is that coordinate function exactly when its corresponding absolute coefficient strictly exceeds the sum of the other absolute coefficients (excluding null boundaries). This proves the geometric equivalence and uniqueness. This is also an elementary proof of the relevant discrete cube edge-isoperimetric extremality.

**2. Gaussian cone and Dirichlet tilt.** Let \(G_0,G_1,\ldots,G_m\) be independent standard Gaussians. Gaussian normalization is Haar, and disjointness of the possible dominant coordinates gives
\[
p_d=2d\,\Pr\left\{G_0>\sum_{j=1}^m|G_j|\right\}.
\]
Put \(S_0=\sum_{j=1}^m|G_j|\) and \(Q_j=|G_j|/S_0\). Changing the half-normal vector to total mass and simplex coordinates has Jacobian \(s^{m-1}\). If \(\overline\Phi(s)=\Pr\{G_0>s\}\), this yields
\[
p_d=\frac{2d(2/\pi)^{m/2}}{(m-1)!}
\int_0^\infty s^{m-1}\overline\Phi(s)
\mathbb E_{Q}\left[\exp\left(-\frac{s^2}{2}\sum_jQ_j^2\right)\right]ds,
\]
where \(Q\) is the *uniform simplex* Dirichlet vector. Integration by parts gives
\[
I_m=\int_0^\infty s^{m-1}\overline\Phi(s)ds
=\frac{2^{(m-1)/2}\Gamma((m+1)/2)}{m\sqrt{2\pi}}.
\]
Under density \(s^{m-1}\overline\Phi(s)/I_m\), the variable \(s\) is distributed as \(S=ZV^{1/m}\), where \(Z^2\sim\chi^2_{m+1}\) and \(V\) is uniform on \([0,1]\), independent of \(Q\). Indeed, conditionally on \(Z=z\), the density of \(S\) is \(ms^{m-1}/z^m\) on \([0,z]\); integrating against the \(\chi_{m+1}\) density gives the claimed law. Substitution and simplification yield exactly \(p_d=B_d\mathbb E[e^{-T}]\).

**3. The two-term coefficient.** For each integer \(k\ge0\), the factorial moments of the uniform simplex give
\[
\mathbb E\!\left[\left(\sum_jQ_j^2\right)^k\right]
=\frac{k!}{m(m+1)\cdots(m+2k-1)}
[z^k]\left(\sum_{a=0}^k\frac{(2a)!}{a!}z^a\right)^m.
\]
Also \(\mathbb E[S^{2k}]=\frac{m}{m+2k}2^k((m+1)/2)_k\), with the usual rising factorial. Thus the first four exact moments of \(T\) are
\[
\mathbb ET=\frac{m}{m+2},\quad
\mathbb ET^2=\frac{m(m+5)}{(m+2)(m+4)},
\]
\[
\mathbb ET^3=\frac{m(m^2+15m+74)}{(m+2)(m+4)(m+6)},\qquad
\mathbb ET^4=\frac{m(m^3+30m^2+371m+2118)}{(m+2)(m+4)(m+6)(m+8)}.
\]
Writing \(\Delta=T-1\) and expanding these rational expressions gives
\[
\mathbb E\Delta=-\frac2m+O(m^{-2}),\quad
\mathbb E\Delta^2=\frac3m+O(m^{-2}),\quad
\mathbb E\Delta^3=O(m^{-2}),\quad
\mathbb E\Delta^4=O(m^{-2}).
\]
The fourth derivative of \(e^{-t}\) is bounded by one for \(t\ge0\), so Taylor's theorem around one, with a remainder bounded in expectation by \(\mathbb E\Delta^4/24\), yields
\[
\mathbb Ee^{-T}=e^{-1}\left(1-\mathbb E\Delta+\tfrac12\mathbb E\Delta^2-\tfrac16\mathbb E\Delta^3\right)+O(m^{-2})
=e^{-1}\left(1+\frac7{2m}+O(m^{-2})\right).
\]
This proves the probability expansion. (The exact fourth moments also imply \(T\to1\) in probability.)

**4. Conditional normal direction.** The probability law of \((S,Q)\), conditioned on a specified coordinate being strictly dominant and oriented positive, is the independent base law of step 2 multiplied by the normalized density \(e^{-T}/\mathbb Ee^{-T}\). Under the base law, take \(Q_j=Y_j/\sum_{k=1}^mY_k\) with independent \(Y_j\sim\operatorname{Exp}(1)\). The strong law of large numbers and the chi-square law of large numbers imply
\[
(mQ_1,\ldots,mQ_r)\Longrightarrow(E_1,\ldots,E_r),\quad
m\sum_jQ_j^2\to2,\quad S^2/m\to1
\]
in probability where appropriate. Consequently \(T\to1\) in probability. Since \(0\le e^{-T}\le1\), the tilted law and base law have total-variation distance tending to zero: \(\mathbb E|e^{-T}/\mathbb Ee^{-T}-1|\to0\). Conditional on \(S=s\), the positive dominant Gaussian \(G_0\) is standard normal conditioned to exceed \(s\); the Gaussian tail bound implies \(G_0/S\to1\) in probability as \(S\to\infty\). The normalized vector then has non-dominant magnitudes
\[
|U_j|=\frac{SQ_j}{\sqrt{G_0^2+S^2\sum_kQ_k^2}},\qquad
U_I=\frac{G_0}{\sqrt{G_0^2+S^2\sum_kQ_k^2}}.
\]
The first fraction is \(Q_j(1+o_{\Pr}(1))\), while
\[
m(1-U_I)=\frac{mS^2\sum_kQ_k^2}{2G_0^2}(1+o_{\Pr}(1))\to1.
\]
Permutation and sign symmetry transfer the conditional law from a specified dominant coordinate to the unique randomly chosen index. Slutsky's theorem gives the joint exponential-and-point-mass limit. The angle statement follows from \(1-\cos\theta\sim\theta^2/2\). All tail bounds and convergence arguments are uniform over the finitely many tracked non-dominant coordinates.

## Verification
The standalone standard-library program `VERIFY.py` reproduces exact symbolic moment identities using rational arithmetic for dimensions indexed by \(2\le m\le44\), checks cube-edge crossings and dominance equivalence for hundreds of generic Gaussian normals in each of dimensions three through seven, and performs seeded importance-sampling checks of the exact probability and large-dimensional conditional Dirichlet profile. Execute `python VERIFY.py`. Its expected terminal marker is `ALL_RARE_MINIMAL_CUBE_SECTION_CHECKS_PASSED`. The finite checks supplement the analytic proof; they are not proofs of the all-dimensional or asymptotic statements.

## Relationship to prior work
Kabluchko and Seidel (2020) explicitly evaluated the Gaussian solid angles of cones over regular crosspolytopes, including the *exact* Gaussian event \(\Pr\{G_0\ge\sum_j|G_j|\}\). Their paper also treats expected face numbers of random sections of regular polytopes. Accordingly, neither that Gaussian representation nor a general exact solid-angle expression is claimed as new. The distinct result here is the two-term large-dimensional asymptotic *of the rare minimum-vertex section event*, its Boolean geometric rigidity, and the conditional joint exponential profile of its normal coordinates.

König and Koldobsky (2018) investigate maximal surface area of central cube sections, not the rare Haar probability or its conditional directional law. Brandenburg and Meroni (2025) classify finite-dimensional combinatorial section types; their readily available abstract concerns dimensions up to seven for central sections and does not itself establish the displayed large-dimensional asymptotic. Their complete manuscript was not available in the material inspected here, so an implicit relation with those results remains a historical-priority risk. Other research may derive equivalent rare-cone asymptotics under different terminology.

## Limitations
The event is the **minimum vertex count**, not the minimum or maximum geometric volume or surface area. The theorem requires equal-sided cubes, central Haar-uniform sections and a fixed number of non-dominant coordinates for the conditional exponential limit. It does not quantify convergence in total variation of the full growing-dimensional normal vector; the total-variation statement pertains only to its auxiliary tilted simplex law. The asymptotic is not an estimate uniform over non-Haar distributions. Neither independent peer review nor exhaustive historical priority certification is claimed.

## References
1. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492 (first posted 2020-06-16), especially Sections 2.1, 4, and 5.5. https://arxiv.org/abs/2006.09492
2. H. König and A. Koldobsky, *On the maximal perimeter of sections of the cube*, arXiv:1806.08659 (first posted 2018-06-22). https://arxiv.org/abs/1806.08659
3. M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265 (first posted 2025-10-10). https://arxiv.org/abs/2510.09265
