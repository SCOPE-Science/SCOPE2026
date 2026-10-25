# Exact paired bound states and resistance-controlled weak binding for neutral lattice defects

## Finding

For any fixed \(r\in\mathbb Z^2\setminus\{0\}\) and every \(\lambda>0\), the square-lattice operator \(H_{\lambda,r}=4I-\sum_{|e|_1=1}T_e-\lambda|0\rangle\langle0|+\lambda|r\rangle\langle r|\) on \(\ell^2(\mathbb Z^2)\) has exactly one simple eigenvalue below \([0,8]\) and exactly one simple eigenvalue above \([0,8]\), situated at \(-\kappa_r(\lambda)\) and \(8+\kappa_r(\lambda)\), respectively. With \(h(k)=4-2\cos k_1-2\cos k_2\), \(G_s(\kappa)=\int_{[-\pi,\pi]^2}\cos(k\cdot s)/(h(k)+\kappa)\,dk/(2\pi)^2\), and \(R_r=\int_{[-\pi,\pi]^2}(1-\cos(k\cdot r))/h(k)\,dk/(2\pi)^2>0\), \(\kappa_r\) is the unique positive solution of \(\lambda^2\left(G_0(\kappa)^2-G_r(\kappa)^2\right)=1\) and satisfies \(\kappa_r(\lambda)=32\exp(-2\pi R_r)\exp(-2\pi/(R_r\lambda^2))(1+o(1))\) as \(\lambda\downarrow0\). For nearest-neighbor \(r=(1,0)\), \(R_r=1/4\), hence \(\kappa_r(\lambda)\sim32e^{-\pi/2}e^{-8\pi/\lambda^2}\).

## Assumptions and scope

Work on the infinite square lattice \(\mathbb Z^2\) with the nearest-neighbor combinatorial Laplacian, in hopping-energy units equal to one. Here \(T_e\) denotes translation by the unit coordinate vector \(e\), and \(r\) is a fixed nonzero lattice displacement. The onsite perturbation is attractive at \(0\), repulsive at \(r\), and has exactly zero total strength. All couplings are real and strictly positive. The result concerns discrete eigenvalues strictly **outside** the free interval \([0,8]\); it does not assert absence of embedded eigenvalues within that interval.

## Proof

**Free spectrum and Green functions.** The Fourier transform maps \(H_0\) to multiplication by \(h(k)=4-2\cos k_1-2\cos k_2\), with spectrum \([0,8]\). For \(\kappa>0\), define \(G_s(\kappa)=\langle\delta_0,(H_0+\kappa)^{-1}\delta_s\rangle\) as the real Fourier integral in the finding. Positivity of the continuous-time simple-random-walk heat kernel gives \(G_r(\kappa)>0\) for fixed \(r\). Both quantities
\[
G_0(\kappa)\pm G_r(\kappa)
=\int_{[-\pi,\pi]^2}\frac{1\pm\cos(k\cdot r)}{h(k)+\kappa}\frac{d^2k}{(2\pi)^2}
\]
are strictly positive and strictly decreasing in \(\kappa\): their integrands are nonnegative, not identically zero, and decrease strictly wherever positive. Both tend to zero as \(\kappa\to\infty\).

**Two-site determinant and uniqueness.** The eigenvalue equation at \(-\kappa\), restricted by the free resolvent to the two perturbation sites, is equivalent to the nullity of
\[
\begin{pmatrix}1-\lambda G_0(\kappa)&\lambda G_r(\kappa)\\
-\lambda G_r(\kappa)&1+\lambda G_0(\kappa)\end{pmatrix}.
\]
Its determinant is \(1-\lambda^2(G_0-G_r)(G_0+G_r)\). Since the two factors are positive and strictly decreasing, the determinant equation has at most one positive solution. Its root is simple as an eigenvalue: the displayed matrix has rank one rather than rank zero because its off-diagonal entries are nonzero. The rank-two resolvent reduction loses no eigenfunctions outside the free spectrum.

**Weak spectral-edge singularity.** The cancellation in the difference has finite positive limit
\[
R_r=\lim_{\kappa\downarrow0}(G_0-G_r)
=\int_{[-\pi,\pi]^2}\frac{1-\cos(k\cdot r)}{h(k)}\frac{d^2k}{(2\pi)^2}>0.
\]
The integrand extends boundedly in angular order near \(k=0\), because its numerator vanishes quadratically; hence the integral converges. The diagonal Green function, by the elementary square-lattice Watson integral, is
\[
G_0(\kappa)=\frac{2}{\pi(4+\kappa)}K\left(\frac4{4+\kappa}\right),\qquad
K(t)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-t^2\sin^2\theta}}.
\]
As \(t\uparrow1\), \(K(t)=\log(4/\sqrt{1-t^2})+O((1-t^2)|\log(1-t^2)|)\). It follows that
\[
G_0(\kappa)=\frac1{4\pi}\log\frac{32}{\kappa}+O(\kappa|\log\kappa|).
\]
For each fixed \(r\), subtracting the \(\kappa=0\) integral and splitting the Brillouin zone into \(|k|\le\frac12\) and its complement gives \(G_0(\kappa)-G_r(\kappa)=R_r+O(\kappa|\log\kappa|)\). Indeed, the difference of integrands is \(\kappa(1-\cos(k\cdot r))/(h(k)(h(k)+\kappa))\), whose radial integral near the origin is bounded by a constant times \(\kappa\int_0^{1/2}t/(t^2+\kappa)\,dt\). Consequently
\[
G_0(\kappa)^2-G_r(\kappa)^2
=\frac{R_r}{2\pi}\log\frac{32}{\kappa}-R_r^2+o(1).
\]
This tends to infinity, establishing the existence of the unique root for every coupling. It also gives
\[
\log\frac{32}{\kappa_r(\lambda)}
=\frac{2\pi}{R_r\lambda^2}+2\pi R_r+o(1),\qquad\lambda\downarrow0,
\]
and exponentiating proves the full prefactor stated in the finding. Here \(r\) is fixed in the limit; no uniformity as \(|r|\to\infty\) is claimed.

**Mirror state and essential spectrum.** Let \(R\psi(x)=\psi(r-x)\) be reflection about the defect midpoint and \(S\psi(x)=(-1)^{x_1+x_2}\psi(x)\) the bipartite sign unitary. Then \(U=SR\) is unitary and
\[
UH_{\lambda,r}U^{-1}=8I-H_{\lambda,r}.
\]
Reflection interchanges the attractive and repulsive sites; the bipartite sign conjugates \(H_0\) to \(8I-H_0\). Thus the sole lower eigenvalue \(-\kappa_r\) has a partner at \(8+\kappa_r\), with equal multiplicity. There can be no further eigenvalues above the band because they would map to additional eigenvalues below. The finite-rank potential preserves the free essential spectrum \([0,8]\).

**Nearest-neighbor normalization.** For \(r=e_1=(1,0)\), the resolvent identity at the origin is \((4+\kappa)G_0(\kappa)-4G_{e_1}(\kappa)=1\). Since \(\kappa G_0(\kappa)\to0\), it yields \(R_{e_1}=1/4\). The general formula therefore specializes to \(\kappa_{e_1}\sim32e^{-\pi/2}\exp(-8\pi/\lambda^2)\). This is an exact limit, not a numerical fit.

## Verification

The proof reduces the full infinite-lattice problem to a two-site determinant and establishes the limiting coefficients from the exact Watson integral. A standalone numerical checker evaluates the elliptic formula at high precision for nearest-neighbor separation and checks both the resolvent identity and the predicted asymptotic ratio at decreasing couplings. Finite floating-point checks are supplementary and are not used to infer existence or uniqueness. For a second lattice orientation, direct convergent Brillouin-zone quadrature gives \(R_{(1,1)}=1/\pi\) numerically; no exact diagonal resistance evaluation is needed for the theorem.

## Relationship to prior work

Simon (1976) already establishes the anomalous inverse-square-coupling exponential scale for zero-integral continuum planar potentials; that exponent **alone is not an originality claim**. Chadan–Khuri–Martin–Wu (2002) analyze low-dimensional continuum bound-state counting. McCutcheon (2004) gives the square-lattice elliptic Green function and the single-site defect method. The lattice Green-function handbook tabulates the free resolvent and recurrence mechanisms. The inspected texts do not state an all-coupling classification for a balanced attractive–repulsive **pair of lattice sites** at arbitrary fixed separation, its exact unitary pairing about the band center, or the explicit resistance-controlled prefactor \(32e^{-2\pi R_r}\). Those results require combining a signed two-site determinant, monotonicity, and a precise subleading Green-function expansion.

## Limitations

The result applies to the single-particle nearest-neighbor tight-binding model on \(\mathbb Z^2\), with equal and opposite onsite strengths. No statement is made about higher-dimensional lattices, finite volumes, extra defects, embedded eigenvalues, or uniformity in the separation while the coupling vanishes. The exponential law is not new as a general continuum phenomenon; the proposed contribution is its exact discrete signed-defect classification and separation-dependent normalization. Closely related literature outside the inspected source set may contain an equivalent rank-two lattice result, so independent literature audit remains useful.

## References

1. B. Simon, “The Bound State of Weakly Coupled Schrödinger Operators in One and Two Dimensions,” *Annals of Physics* **97** (1976), 279–288, DOI: 10.1016/0003-4916(76)90038-5. Authorized author copy: https://math.caltech.edu/SimonPapers/70.pdf.
2. K. Chadan, N. N. Khuri, A. Martin, and T. T. Wu, “Bound States in one and two Spatial Dimensions,” arXiv:math-ph/0208011, first posted 2002-08-06. https://arxiv.org/abs/math-ph/0208011.
3. M. McCutcheon, “A Green’s Function Analysis of Defect States in Periodic Hamiltonians,” University of British Columbia report dated 2004-12-01. https://phas.ubc.ca/~berciu/TEACHING/PHYS503/PROJECTS/P503_impurity.pdf.
4. A. Zhugayevych, *Handbook on Lattice Green’s Functions*, https://cmsos.github.io/lgf/LGF.pdf (consulted for free-lattice resolvent identities, not for the original defect claim).
