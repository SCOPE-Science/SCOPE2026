# Arithmetic flux-switching of dark survival on a cycle with two absorbing vertices

## Finding

Consider a nearest-neighbor continuous-time coherent walk on an \(N\)-cycle, \(N\geq3\), with two positive-rate Lindblad absorbers at vertices \(0\) and \(a\), \(1\leq a<N\), and magnetic flux \(\Phi\). Set \(g=\gcd(N,a)\) and \(Q=N/g\). The exact nonabsorbing subspace dimension \(d_\Phi\) and limiting survival probability \(S_\Phi(x)\) from any vertex \(x\) are independent of the hopping strength and the positive absorber rates.

For all \(\Phi\not\equiv0,\pi\pmod{2\pi}\), \(d_\Phi=S_\Phi(x)=0\). For \(\Phi\equiv0\pmod{2\pi}\),
\[
d_0=\begin{cases}
g-1,&Q\text{ even},\\
(g-1)/2,&Q\text{ odd and }g\text{ odd},\\
(g-2)/2,&Q\text{ odd and }g\text{ even},
\end{cases}
\qquad
S_0(x)=\begin{cases}
\dfrac{g}{N}\bigl(1-\mathbf1_{g\mid x}\bigr),&Q\text{ even},\\
\dfrac{g}{2N}\bigl(1-\mathbf1_{g\mid2x}\bigr),&Q\text{ odd}.
\end{cases}
\]
For \(\Phi\equiv\pi\pmod{2\pi}\),
\[
d_\pi=\begin{cases}
0,&Q\text{ even},\\
(g-1)/2,&Q\text{ odd and }g\text{ odd},\\
g/2,&Q\text{ odd and }g\text{ even},
\end{cases}
\qquad
S_\pi(x)=\begin{cases}
0,&Q\text{ even},\\
\dfrac{g}{2N}\left[1-\mathbf1_{g\mid2x}\cos\left(\dfrac{2\pi x}{g}\right)\right],&Q\text{ odd}.
\end{cases}
\]
Here \(\mathbf1_{g\mid y}\) equals one when the integer \(g\) divides \(y\), and zero otherwise. In particular, **every initial excitation is absorbed at every magnetic flux precisely when \(\gcd(N,a)=1\)**. If \(Q\) is even, half-integer flux eliminates all surviving dark modes, even when zero flux supports them. If \(Q\) is odd and \(g\) is even, changing zero flux to half flux switches vertex class \(x\equiv g/2\pmod g\) from zero asymptotic survival to exactly \(g/N\).

## Assumptions and scope

The Hilbert space of a surviving single excitation is \(\mathcal H=\mathbb C^N\), with orthonormal vertex basis \(\{|j\rangle:j\in\mathbb Z/N\mathbb Z\}\). Fix \(J>0\) and \(\kappa_0,\kappa_a>0\). The Hamiltonian is
\[
H_\Phi=-J\sum_{j=0}^{N-1}\left(e^{i\Phi/N}|j\rangle\langle j+1|+e^{-i\Phi/N}|j+1\rangle\langle j|\right),
\]
indices modulo \(N\). The jump operators remove the excitation into orthogonal absorber states: \(L_0=\sqrt{\kappa_0}|\mathrm{vac}_0\rangle\langle0|\) and \(L_a=\sqrt{\kappa_a}|\mathrm{vac}_a\rangle\langle a|\). Write \(\Gamma=\kappa_0|0\rangle\langle0|+\kappa_a|a\rangle\langle a|\) and \(B_\Phi=-iH_\Phi-\Gamma/2\). For a vertex input \(|x\rangle\), survival is \(S_{\Phi,t}(x)=\|e^{tB_\Phi}|x\rangle\|^2\), and \(S_\Phi(x)=\lim_{t\to\infty}S_{\Phi,t}(x)\). For a general initial density operator \(\rho\) on \(\mathcal H\), the asymptotic survival is \(\operatorname{Tr}(P_\Phi\rho)\), with \(P_\Phi\) the spectral projection onto eigenvectors of \(H_\Phi\) vanishing at both sink sites. Flux is physically understood modulo \(2\pi\): adding a flux quantum is a diagonal unitary gauge transformation fixing every site probability.

## Proof

**(1) Asymptotic survival equals dark projection.** In the no-jump sector the density operator evolves as \(e^{tB_\Phi}\rho e^{tB_\Phi^\dagger}\). Every vector \(\psi_t=e^{tB_\Phi}\psi\) satisfies
\[
\frac{d}{dt}\|\psi_t\|^2=-\kappa_0|\langle0|\psi_t\rangle|^2-\kappa_a|\langle a|\psi_t\rangle|^2\leq0.
\]
If \(B_\Phi v=zv\) with \(\operatorname{Re}z=0\), the right-hand side forces \(\Gamma v=0\), and consequently \(H_\Phi v=i z v\). Conversely every \(H_\Phi\)-eigenvector in \(\ker\Gamma\) is a purely imaginary eigenvector of \(B_\Phi\). Their span \(\mathcal D_\Phi\) reduces both \(H_\Phi\) and \(\Gamma\), hence also \(B_\Phi\), because each such eigenvector is simultaneously an eigenvector of \(B_\Phi\) and \(B_\Phi^\dagger\). On its orthogonal complement all eigenvalues of \(B_\Phi\) have strictly negative real part: a zero-real-part eigenvector would lie in \(\mathcal D_\Phi\), and a positive-real-part eigenvalue contradicts contraction. Finite-dimensional matrix exponential asymptotics therefore imply
\[
\lim_{t\to\infty}\operatorname{Tr}(e^{tB_\Phi}\rho e^{tB_\Phi^\dagger})=\operatorname{Tr}(P_\Phi\rho).
\]
This general dissipative spectral step is standard and is not itself claimed as novel.

**(2) Fourier pair criterion.** Let \(f_m(j)=N^{-1/2}e^{2\pi i m j/N}\), with \(0\leq m<N\). Direct substitution yields
\[
H_\Phi f_m=-2J\cos\left(\frac{2\pi m+\Phi}{N}\right)f_m.
\]
A nontrivial energy degeneracy requires \(\Phi\equiv0\) or \(\pi\pmod{2\pi}\); otherwise each eigenvector is a single Fourier wave with nonzero amplitude at \(0\), so the dark subspace is zero. In the two exceptional flux classes write \(\Phi=s\pi\), \(s\in\{0,1\}\). The distinct Fourier indices in each twofold degenerate eigenspace are \(m\) and \(m'\equiv-m-s\pmod N\). The unique normalized vector in that eigenspace vanishing at \(0\) is \(v_{m,m'}=(f_m-f_{m'})/\sqrt2\). It vanishes at \(a\) exactly when
\[
e^{2\pi i(m-m')a/N}=1
\quad\Longleftrightarrow\quad
N\mid a(2m+s)
\quad\Longleftrightarrow\quad
Q\mid2m+s.
\]
The last equivalence uses \(a/g\) coprime to \(Q=N/g\). Single, nondegenerate Fourier modes never vanish at a sink. Choosing one index from each qualifying distinct pair therefore gives a complete orthonormal basis of \(\mathcal D_\Phi\).

**(3) Exact counts.** For \(s=0\), if \(Q\) is even there are \(2g\) indices satisfying \(Q\mid2m\), of which exactly two solve \(2m\equiv0\pmod N\). Pairing the other indices gives \(g-1\) dark vectors. If \(Q\) is odd, the qualifying congruence has \(g\) solutions; its involution has one fixed point when \(N\) is odd and two when \(N\) is even, yielding \((g-1)/2\) or \((g-2)/2\). For \(s=1\), \(Q\) even gives no solution. If \(Q\) is odd, there are \(g\) qualifying indices and one fixed point for odd \(N\), none for even \(N\), yielding the stated dimensions.

**(4) Site-resolved weights.** Each accepted twofold eigenspace contributes
\[
|\langle x|v_{m,m'}\rangle|^2
=\frac1N\left[1-\cos\left(\frac{2\pi(2m+s)x}{N}\right)\right].
\]
Counting both members of each pair but dividing by two does not change this formula, because fixed points contribute zero. If \(Q\) is even and \(s=0\), write the qualifying \(2m=Qt\) with \(t\) ranging over \(2g\) consecutive integers. The usual roots-of-unity sum then gives \(S_0(x)=g(1-\mathbf1_{g\mid x})/N\). When \(Q\) is odd and \(s=0\), the qualifying \(t\) are even and the same sum gives \(S_0(x)=g(1-\mathbf1_{g\mid2x})/(2N)\). When \(Q\) is odd and \(s=1\), the qualifying \(t\) are odd; the sum is \(g\cos(2\pi x/g)\) when \(g\mid2x\) and zero otherwise. This gives exactly \(S_\pi(x)\) as displayed. Since all surviving weights are diagonal entries of an orthogonal projection, they lie in \([0,1]\). The coprime criterion and flux switches follow by reading off the displayed cases. \(\square\)

## Verification

Run `python verify.py` with Python, NumPy and SciPy. The script independently enumerates all admissible Fourier pairs and their local weights for \(3\leq N\leq120\); uses direct numerical eigenvalue/eigenspace calculations for \(3\leq N\leq24\), every absorber separation and both exceptional fluxes as well as a generic flux; and tests contraction under full non-Hermitian propagation for selected unequal absorber rates. Recorded checks: 1,151,916 combinatorial/Fourier cases, 9,471 direct spectral-projector cases (maximum weight discrepancy less than \(10^{-15}\)), and 24 finite-time propagation cases. These finite checks do not establish the theorem for arbitrary \(N\); the proof above does.

## Relationship to prior work

Riberi [1] studies an exactly solvable **single-boundary** Lindblad absorber on a semi-infinite tight-binding line and discusses further absorber geometries; it does not derive the two-absorber finite-cycle arithmetic phase diagram. Thiel and collaborators [2] explain dark eigenstates and flux-induced lifting of degeneracies for a **single repeatedly measured detector** on a cycle. Their eigenmode insight is an important precursor, but their detector protocol, sink count, and conclusions differ from the present exact two-Lindblad-sink sitewise formulas. Razzoli, Paris, and Bordone [3] give a general graph transport/dark-subspace treatment with a **single** trap; the present proof uses the known dark-projection principle and derives the previously unspecified two-site gcd and flux-resolved classification. Xu [4] studies coherent trapping on long-range-interacting cycles and numerical survival changes; it does not state these two-local-sink nearest-neighbor magnetic formulas. Thus the dark-state method itself is prior knowledge; the parameter-uniform explicit arithmetic classification is the claimed contribution.

## Limitations

The assumptions require a single excitation, a homogeneous finite nearest-neighbor cycle, coherent uniform Peierls flux, and **both** absorber rates strictly positive. No conclusion is claimed for one absorber switched off, finite observation times or absorption-time distributions, disorder, next-nearest-neighbor hopping, nonlocal jump operators, interactions, or coherent injection. The asymptotic probabilities do not assert uniform convergence rates near resonant fluxes. General symmetry/observability results beyond the inspected literature might already imply particular cases; a novelty search is not a priority certificate. Independent audit and independent validation have not been performed.

## References

[1] F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056v1, first public 2026-05-08, https://arxiv.org/abs/2605.08056.

[2] F. Thiel, I. Mualem, D. Meidan, E. Barkai and D. A. Kessler, *Dark states of quantum search cause imperfect detection*, arXiv:1906.08112, https://arxiv.org/abs/1906.08112.

[3] L. Razzoli, M. G. A. Paris and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794, https://arxiv.org/abs/2011.13794.

[4] X. Xu, *Coherent exciton transport and trapping on long-range interacting cycles*, arXiv:0812.3452, https://arxiv.org/abs/0812.3452.
