# A sharp strong-coupling window for a two-colour travelling wave

## Finding
For every even integer \(N\ge 2\), consider the nearest-neighbour Chebyshev lattice on the periodic ring \(\mathbb Z/N\mathbb Z\):
\[
(\mathcal F_a(x))_j=(1-a)(2x_j^2-1)+\frac a2(x_{j-1}+x_{j+1}),\qquad 0\le a\le1.
\]
Indices are cyclic, with both contributions retained when \(N=2\). Set
\[
u=\frac{\sqrt5-1}{4},\qquad v=-\frac{\sqrt5+1}{4}.
\]
The spatial checkerboard \(X=(u,v,u,v,\ldots)\) and its translate \(Y=(v,u,v,u,\ldots)\) constitute a primitive temporal period-two orbit \(\mathcal F_a(X)=Y\), \(\mathcal F_a(Y)=X\) **for every** \(0\le a\le1\). If \(M_{a,N}=D\mathcal F_a(Y)D\mathcal F_a(X)\) is its two-step Floquet matrix, then
\[
\boxed{\rho(M_{a,N})=4(1-a)^2+a^2=5a^2-8a+4,}
\]
independently of the even ring size. Consequently, the checkerboard is locally asymptotically attracting precisely when \(3/5<a<1\) among the parameters with strictly contracting Floquet spectrum; it is linearly unstable for \(0\le a<3/5\). At \(a=3/5\) and \(a=1\) the spectrum meets the unit circle, so the linear criterion alone does not classify nonlinear stability there. The Floquet spectral radius has the unique minimum \(4/5\), attained at the optimal coupling \(a=4/5\).

The same spectral-radius formula holds on the infinite two-colour lattice for the return operator acting on \(\ell^2(\mathbb Z)\). The checkerboard orbit is locally attracting under sufficiently small \(\ell^2\) perturbations whenever \(3/5<a<1\).

## Assumptions and scope
The local polynomial is \(f(x)=2x^2-1\), and the coupling uses the **neighbouring states** rather than their nonlinear images (the backward-coupling, positive-sign convention). The phase space for each finite lattice is the invariant cube \([-1,1]^N\). The orbit has spatial period two and temporal period two, not spatial synchrony. ``Locally attracting'' means local asymptotic stability of the two-step return dynamics near \(X\), and its time-shifted counterpart near \(Y\). For the infinite lattice, the relevant phase space is the affine perturbation class around this two-periodic spatial background, with perturbations measured in \(\ell^2\), not convergence to a point in \(\ell^2\) itself.

## Proof
**1. Exact orbit, independent of coupling.** Direct substitution yields \(f(u)=v\) and \(f(v)=u\); the points are distinct and lie strictly inside \((-1,1)\). Every neighbour of an even site in \(X\) has value \(v\), which is also \(f(u)\). Hence both the local term and the two-neighbour average equal \(v\), making the next even-site value \(v\), for every \(a\). The odd sites similarly become \(u\). A second iteration returns to \(X\). The two points are distinct, so the temporal period is primitive. Convexity of the update also shows invariance of the cube when \(0\le a\le1\).

**2. Block diagonalization.** Write \(c=1-a\), \(\alpha=f'(u)=\sqrt5-1\), and \(\gamma=f'(v)=-\sqrt5-1\). Thus \(\alpha\gamma=-4\). At \(X\), the Jacobian has diagonal entries alternating between \(c\alpha\) and \(c\gamma\), and nearest-neighbour coefficients \(a/2\). At \(Y\), the diagonal entries swap. Decompose into Fourier sectors for translation by two sites. Taking the representative wave numbers \(k=2\pi m/N\) for integers \(0\le m<N/2\), and factoring out \(e^{ikj}\), the two one-step matrices are
\[
H_0(k)=\begin{pmatrix}c\alpha&a\cos k\\a\cos k&c\gamma\end{pmatrix},\qquad
H_1(k)=\begin{pmatrix}c\gamma&a\cos k\\a\cos k&c\alpha\end{pmatrix}.
\]
The formula remains valid on the two-site ring because the two coincident neighbours each have weight \(a/2\). Their product has identical diagonal entries \(K=a^2\cos^2 k-4c^2\), with off-diagonal entries \(2ac\gamma\cos k\) and \(2ac\alpha\cos k\):
\[
H_1(k)H_0(k)=\begin{pmatrix}
K&2ac\gamma\cos k\\2ac\alpha\cos k&K
\end{pmatrix}.
\]
Since \(\alpha\gamma=-4\), its unordered eigenvalues are
\[
\lambda_{\pm}(k)=a^2\cos^2 k-4(1-a)^2\ \pm\ 4ia(1-a)\cos k.
\]
The formula also includes \(\cos k=0\), when the two eigenvalues coincide and the block is scalar. A direct identity gives
\[
|\lambda_\pm(k)|=a^2\cos^2 k+4(1-a)^2.
\]
The discrete sector \(k=0\) always occurs and has \(|\cos k|=1\). Maximizing over all the Fourier sectors therefore yields the asserted radius, without dependence on \(N\).

**3. Stability and optimum.** Factor
\[
\rho(M_{a,N})-1=(a-1)(5a-3).
\]
On \(0\le a\le1\), this is negative exactly for \(3/5<a<1\), and positive for \(a<3/5\). A smooth finite-dimensional fixed-point theorem applied to \(\mathcal F_a^2\) gives local asymptotic attraction when every Floquet multiplier has modulus below one; a multiplier outside the unit disk implies instability. At the boundary we assert only neutral linear spectrum. Differentiating the strictly convex quadratic \(5a^2-8a+4\) gives its unique minimum at \(a=4/5\), with value \(4/5\).

**4. Infinite lattice.** Translation by two admits the unitary two-sublattice Fourier transform on \(\ell^2(\mathbb Z)\). Under that transform, the two-step derivative is multiplication by the continuous matrices \(H_1(k)H_0(k)\) on a compact frequency circle. The spectrum of this decomposable operator is the union (with closure) of the spectra of its fibres, so its spectral radius is the maximum of the displayed \(|\lambda_\pm(k)|\), again \(4(1-a)^2+a^2\). For perturbations \(h\in\ell^2\), the pointwise quadratic remainder satisfies \(\|h^2\|_2\le\|h\|_2^2\), showing that the nonlinear return map is continuously differentiable near the background in its affine \(\ell^2\) class. If the derivative has spectral radius below one, a suitable power of the return map is a local contraction in an equivalent norm, proving local attraction. This makes no assertion about perturbations outside the chosen normed class.

## Verification
The standalone Python 3 script `verify_checker.py` directly constructs and composes the full finite-lattice Jacobians (rather than merely applying the proposed spectrum). It tests all Fourier sectors for six even ring sizes and eight coupling strengths, the two-step orbit identities, matrix block entries, and determinant/modulus relations. It completed 997 finite diagnostics. The all-size and infinite-lattice conclusions follow from the displayed algebra and Fourier argument, not from the finite tests. To reproduce from a directory containing the embedded files, run `python3 verify_checker.py`.

## Relationship to prior work
Lippolis (2026; first publicly posted October 14, 2025) analyzes *spatially synchronized* fixed points and two-cycles of this same Chebyshev lattice, finding a lower-coupling stability window for the synchronized two-cycle and noting that its real branch disappears by \(a=1/3\). The present orbit instead alternates in space and travels by one site each step; it remains real and is stable for \(a>3/5\). The full Fourier stability of this distinct orbit, the size-independent sharp window, and its optimal coupling are not implied by the synchronized-orbit conclusions.

Dettmann and Lippolis (2005, initially disseminated as a 2003 preprint) study two-site coupled Chebyshev orbit enumeration and cycle expansions at weak coupling (with figures and detailed computations for \(a\le0.1\)); their general map includes this backward-coupling convention, but the inspected text does not give the all-even-ring exact checkerboard multiplier or its strong-coupling threshold. Dettmann (2002) concerns stable *synchronized* states; an accessible full-text comparison for that paper could not be completed. General spatiotemporal Floquet block methods are established; the claim is not to invent Fourier analysis, but to identify an exact travelling pattern with an unexpected cancellation of the full two-step spectrum.

## Limitations
This is a local spectral and local nonlinear stability theorem, not a global basin classification, a claim that the checkerboard is the only attractor, or a nonlinear classification of the neutral threshold at \(a=3/5\). The result assumes the specified coupling convention and even spatial period. Other degrees of the local Chebyshev map and nonlinear neighbour coupling are not included. Although relevant published sources were compared, no literature search can rule out every equivalent calculation in unindexed prior work; the unresolved full-text access to the 2002 reference is a residual priority risk. No independent scientific audit has been performed.

## References
1. D. Lippolis, *Spatiotemporal stability of synchronized coupled map lattice states*, arXiv:2510.12532 (first posted 2025-10-14), *Physica D* 2026, DOI:10.1016/j.physd.2026.135148. Preprint: https://arxiv.org/html/2510.12532.
2. C. P. Dettmann and D. Lippolis, *Periodic orbit theory of two coupled Tchebyscheff maps*, *Chaos, Solitons & Fractals* 23 (2005), 43–54, DOI:10.1016/j.chaos.2004.04.017. Author-posted manuscript: https://people.maths.bris.ac.uk/~macpd/stc/lippolis.pdf.
3. C. P. Dettmann, *Stable synchronised states of coupled Tchebyscheff maps*, *Physica D* 172 (2002), 88–102, DOI:10.1016/S0167-2789(02)00624-3; preprint arXiv:nlin/0110007.
4. N. Chatterjee and N. Gupte, *Analysis of spatiotemporally periodic behavior in lattices of coupled piecewise monotonic maps*, *Phys. Rev. E* 63 (2001), 017202, DOI:10.1103/PhysRevE.63.017202.
