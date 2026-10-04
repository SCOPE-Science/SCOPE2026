# Dipole–quadrupole spatial tails at two square-lattice threshold states
## Finding
Let \(E(p)=2-\cos p_1-\cos p_2\) on \(\mathbb T^2=[-\pi,\pi]^2\). For \(x\in\mathbb Z^2\), define
\[
R_j(x)=\frac{1}{(2\pi)^2}\int_{\mathbb T^2} e^{i p\cdot x}\frac{\sin p_j}{E(p)}\,dp,\qquad j=1,2,
\]
and
\[
Q(x)=\frac{1}{(2\pi)^2}\int_{\mathbb T^2} e^{i p\cdot x}\frac{\cos p_1-\cos p_2}{E(p)}\,dp.
\]
Then, as \(r=|x|_2\to\infty\) through \(\mathbb Z^2\), uniformly in direction,
\[
R_j(x)=\frac{i x_j}{\pi r^2}+O(r^{-3}),
\qquad
Q(x)=\frac{x_1^2-x_2^2}{\pi r^4}+O(r^{-4}).
\]
The functions \(R_1,R_2\) are the normalized coordinate-space profiles corresponding to the two odd threshold-resonance momentum factors \(\sin p_j/E(p)\), and \(Q\) is the normalized coordinate-space profile corresponding to the even threshold-eigenfunction momentum factor \((\cos p_1-\cos p_2)/E(p)\). Thus the two-dimensional threshold resonance has a dipole tail of order \(r^{-1}\), while the threshold eigenstate has a quadrupole tail of order \(r^{-2}\).

## Assumptions and scope
The free dispersion is exactly \(E(p)=2-\cos p_1-\cos p_2\), the normalization used in the cited square-lattice model. The result concerns the lower threshold \(0\) in dimension two. It states asymptotics for the normalized inverse-Fourier kernels above; source eigenfunctions differ only by nonzero scalar factors determined by the source coupling and Fourier normalization. The asymptotics are spatial, not statements about eigenvalue motion away from threshold.

## Proof
Let \(a(x)\) be the potential kernel of the simple symmetric random walk on \(\mathbb Z^2\), normalized by
\[
a(x)=\frac{1}{(2\pi)^2}\int_{\mathbb T^2}
\frac{1-\cos(p\cdot x)}{1-\tfrac12(\cos p_1+\cos p_2)}\,dp.
\]
Since \(E(p)=2[1-\tfrac12(\cos p_1+\cos p_2)]\), if \(G\) denotes the formal zero-energy Green kernel, then all differences below are finite and
\[
G(x)=C-\frac12 a(x)
\]
for an irrelevant divergent constant \(C\).

The square-lattice potential kernel has the classical expansion
\[
a(x)=\frac{2}{\pi}\log r+\kappa-\frac{1}{6\pi}\frac{\operatorname{Re}(x_1+i x_2)^4}{r^6}+O(r^{-4}).
\]
In particular the correction after the logarithm is a smooth homogeneous term of order \(r^{-2}\), followed by \(O(r^{-4})\).

Using \(\sin p_j=(e^{ip_j}-e^{-ip_j})/(2i)\),
\[
R_j(x)=\frac{G(x+e_j)-G(x-e_j)}{2i}
=\frac{a(x-e_j)-a(x+e_j)}{4i}.
\]
For \(f(x)=\log|x|_2\), Taylor expansion of the centered first difference gives
\[
f(x-e_j)-f(x+e_j)=-2\,\frac{x_j}{r^2}+O(r^{-3}).
\]
The order-
\(r^{-2}\) angular correction to \(a\) contributes only \(O(r^{-3})\), and the displayed remainder contributes no larger term. Therefore
\[
R_j(x)=\frac{i x_j}{\pi r^2}+O(r^{-3}).
\]

Similarly, using the cosine shifts,
\[
Q(x)=-\frac14\left[a(x+e_1)+a(x-e_1)-a(x+e_2)-a(x-e_2)\right].
\]
The constant cancels. For \(f=\log r\), the difference of centered second differences is
\[
(\partial_1^2-\partial_2^2)f
=-2\frac{x_1^2-x_2^2}{r^4},
\]
with centered-difference error \(O(r^{-4})\). The \(r^{-2}\) angular correction in \(a\) also contributes \(O(r^{-4})\). Hence
\[
Q(x)=\frac{x_1^2-x_2^2}{\pi r^4}+O(r^{-4}).
\]
This proves both formulas.

## Verification
The source paper gives the odd threshold solutions in dimension two as scalar multiples of \(\sin p_j/E(p)\), and the even threshold solution as a scalar multiple of \((\cos p_1-\cos p_2)/E(p)\). The standard square-lattice potential-kernel expansion supplies the analytic input for the coordinate-space calculation. The bundled checker independently replays the finite-difference identities and verifies numerically that the logarithmic leading term approaches the coefficients \(i/\pi\) and \(1/\pi\) along several non-nodal lattice rays. These finite checks corroborate, but do not replace, the asymptotic proof.

## Relationship to prior work
Hiroshima, Muminov, and Kuljanov explicitly classify the dimension-two threshold resonance/eigenvalue in momentum space and state their \(L^1\) versus \(L^2\) character, but the inspected text does not state coordinate-space far-field multipoles. Kholmatov, Lakaev, and Almuratov later give a broader momentum-space threshold classification for two-dimensional one-range lattice perturbations; the inspected material likewise characterizes threshold functions in momentum variables rather than the dipole/quadrupole spatial coefficients above. The random-walk literature contains the potential-kernel expansion used here, but does not identify these two Hamiltonian threshold states with the stated multipole profiles.

## Limitations
The claim is only for the nearest-neighbor square-lattice dispersion and these normalized threshold profiles. It does not assert analogous coefficients for a general hopping matrix, does not describe off-threshold bound states, and does not claim that no equivalent coordinate-space derivation exists in unindexed literature. The leading term vanishes on the natural nodal directions; the uniform error bounds remain valid there.

## References
1. F. Hiroshima, Z. Muminov, U. Kuljanov, “Threshold of discrete Schrödinger operators with delta potentials on \(n\)-dimensional lattice,” arXiv:1804.05339; Linear and Multilinear Algebra 70 (2022), 919–954, DOI 10.1080/03081087.2020.1750547.
2. Sh. Yu. Kholmatov, S. N. Lakaev, F. M. Almuratov, “On the spectrum of Schrödinger-type operators on two dimensional lattices,” Journal of Mathematical Analysis and Applications 514 (2022), 126363, DOI 10.1016/j.jmaa.2022.126363.
3. T. Friedrich, L. Levine, “Fast simulation of large-scale growth models,” arXiv:1006.1003; Random Structures & Algorithms 42 (2013), 185–213. The paper records the simple-square-lattice potential-kernel expansion used above.
4. Y. Fukai, K. Uchiyama, “Potential kernel for two-dimensional random walk,” Annals of Probability 24 (1996), 1979–1992, DOI 10.1214/aop/1041903213.
