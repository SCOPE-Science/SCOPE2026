# Binomial binding thresholds and band-edge states of hypercubic impurity arrays

## Finding

Let \(d\ge3\) and \(\ell\ge1\) be integers, and let \(\kappa>0\). On \(\ell^2(\mathbb Z^d)\), define the nearest-neighbor adjacency operator \(A_d\) and the finite positive on-site impurity Hamiltonian
\[
(A_df)(n)=\sum_{j=1}^{d}\bigl(f(n+e_j)+f(n-e_j)\bigr),\qquad
H_{d,\ell,\kappa}=A_d+\kappa\sum_{\epsilon\in\{0,1\}^d}|\delta_{\ell\epsilon}\rangle\langle\delta_{\ell\epsilon}|.
\]
The unperturbed spectrum is \([-2d,2d]\). Write \(I_j\) for the ordinary modified Bessel function of the first kind, and set, for every integer \(0\le k\le d\),
\[
\Lambda_{d,k}(\ell)=\int_0^\infty e^{-2dt}
 \bigl(I_0(2t)+I_\ell(2t)\bigr)^{d-k}
 \bigl(I_0(2t)-I_\ell(2t)\bigr)^k\,dt,
\qquad \kappa_{d,k}(\ell)=\Lambda_{d,k}(\ell)^{-1}.
\]
These integrals are finite and strictly positive and satisfy
\[
0<\kappa_{d,0}(\ell)<\kappa_{d,1}(\ell)<\cdots<\kappa_{d,d}(\ell).
\]
The exact number of eigenvalues *counted with multiplicity* strictly above the band edge \(2d\) is
\[
\boxed{N_{>2d}(\kappa)=\sum_{k=0}^{d}\binom dk\,\mathbf1_{\{\kappa>\kappa_{d,k}(\ell)\}}.}
\]
For each open coupling interval above the corresponding threshold, the associated branch has multiplicity \(\binom dk\), with no additional above-band eigenvalues. Thus the mode counts increase successively by the binomial coefficients and eventually reach \(2^d\).

At a critical equality \(\kappa=\kappa_{d,k}(\ell)\), the band-edge equation at energy \(2d\) has exactly \(\binom dk\) linearly independent Fourier-Green solutions from the critical sector. They are genuine square-summable threshold eigenfunctions exactly when \(d+2k>4\); when \(d+2k\le4\), they are non-square-summable threshold resonances. Critical equality never contributes to the strictly above-band count. In particular, for \(d=3,4\) only the first, fully symmetric critical mode is non-square-summable; in \(d\ge5\), all critical modes are square-summable.

For *adjacent* hypercube corners \(\ell=1\), the first two thresholds satisfy the exact dimension-only identity
\[
\boxed{\kappa_{d,1}(1)=\frac{d}{d-2}\,\kappa_{d,0}(1).}
\]
In the simple-cubic case \(d=3,\ell=1\), the successive critical couplings are approximately \(1.388740959246\), \(4.166222877738\), \(6.449383190154\), and \(8.581191985788\); above-band multiplicity steps are \(0,1,4,7,8\). The second threshold is exactly three times the first.

## Assumptions and scope

All nearest-neighbor hoppings have magnitude one, there is no magnetic flux, and the \(2^d\) perturbation sites are precisely the corners \(\ell\epsilon\) for binary vectors \(\epsilon\). Their on-site strengths are all the same strictly positive number \(\kappa\). The spatial lattice is infinite. Modes are counted algebraically and geometrically with their ordinary finite multiplicities; the Hamiltonian is self-adjoint. Only the component of the spectrum strictly greater than \(2d\) and its upper-edge critical solutions are classified here. The scale and sign convention are fixed by the formula for \(A_d\); switching to a positive graph Laplacian changes the energy origin but not the underlying threshold mechanism.

## Proof

**1. The free resolvent and a finite threshold matrix.** For real \(E>2d\), the free resolvent kernel is
\[
G_E(n)=\frac1{(2\pi)^d}\int_{[-\pi,\pi]^d}
\frac{e^{in\cdot\theta}}{E-2\sum_{j=1}^d\cos\theta_j}\,d\theta
=\int_0^\infty e^{-Et}\prod_{j=1}^d I_{|n_j|}(2t)\,dt.
\]
The equality is obtained by the resolvent semigroup integral and the tensor-product heat kernel. At \(E=2d\), the kernel entries for fixed \(n\) remain finite because the integrand decays as \(O(t^{-d/2})\) at infinity and \(d>2\). Denote by \(K_E\) the \(2^d\)-square matrix with entries \((K_E)_{\epsilon,\eta}=G_E(\ell(\epsilon-\eta))\).

The Birman–Schwinger relation states that \(E>2d\) is an eigenvalue of \(H_{d,\ell,\kappa}\) precisely when \(1\) is an eigenvalue of \(\kappa K_E\), preserving multiplicities. Indeed, the coefficient vector of any bound state on the impurity sites satisfies \(a=\kappa K_Ea\). Conversely, for such a nonzero coefficient vector the free resolvent applied to the corresponding finite-support source constructs an exponentially decaying eigenfunction. Injectivity follows because the resolvent and finite-support source map are injective on this subspace.

**2. Walsh diagonalization.** Index sites by \(\epsilon\in\{0,1\}^d\). Because \(I_{|\epsilon_j-\eta_j|\ell}\) equals \(I_0\) when the two bits agree and \(I_\ell\) when they differ, \(K_E\) is a positive integral of tensor products of \(2\)-by-\(2\) matrices whose diagonal entries are \(I_0(2t)\) and off-diagonal entries are \(I_\ell(2t)\). The Walsh vectors
\[
w_\chi(\epsilon)=(-1)^{\chi\cdot\epsilon},\qquad \chi\in\{0,1\}^d,
\]
form an orthogonal basis and diagonalize every such tensor product. If \(|\chi|=k\), its eigenvalue at energy \(E\) is
\[
\Lambda_{d,k}(\ell;E)=\int_0^\infty e^{-Et}
(I_0(2t)+I_\ell(2t))^{d-k}
(I_0(2t)-I_\ell(2t))^k\,dt.
\]
There are exactly \(\binom dk\) characters of weight \(k\).

For \(t>0\), \(I_\ell(2t)>0\), and \(I_0(2t)>I_\ell(2t)\). The first inequality follows from the Bessel power series; the second follows, for positive integer \(\ell\), from the strictly positive integral of \(e^{2t\cos\theta}(1-\cos(\ell\theta))\) over \([0,\pi]\). Consequently every \(\Lambda_{d,k}(\ell;E)\) is positive and strictly decreasing with \(E\), and the levels are strictly decreasing with \(k\). They tend to zero as \(E\to\infty\) and tend to the stated finite positive \(\Lambda_{d,k}(\ell)\) as \(E\downarrow2d\). The equation \(\kappa\Lambda_{d,k}(\ell;E)=1\) therefore has exactly one solution \(E>2d\) iff \(\kappa\Lambda_{d,k}(\ell)>1\), establishing the complete count, ordering, and multiplicities.

**3. What happens at equality.** At \(E=2d\) the Fourier transform of the prospective mode associated with \(w_\chi\) is, up to a nonzero scalar,
\[
\widehat\psi_\chi(\theta)=\frac{F_\chi(\theta)}{2d-2\sum_{j=1}^d\cos\theta_j},\quad
F_\chi(\theta)=\prod_{\chi_j=0}(1+e^{-i\ell\theta_j})
\prod_{\chi_j=1}(1-e^{-i\ell\theta_j}).
\]
The numerator vanishes to *precisely* order \(k\) at the sole singular point \(\theta=0\), whereas the denominator vanishes quadratically. The local square-integrability integral has the same convergence criterion as \(\int_0^1 r^{d+2k-5}\,dr\): it is finite exactly when \(d+2k>4\). A nonzero linear combination of characters of fixed weight \(k\) has a nonzero homogeneous leading term, because the degree-\(k\) squarefree coordinate monomials are linearly independent. Thus the criterion and dimension apply to the entire critical eigenspace, not just a selected basis. The Fourier-Green construction satisfies the edge equation by the finite matrix eigenrelation. There cannot be other square-summable edge modes: the free operator has none at its spectral maximum, so the impurity-site coefficient vector of any edge eigenmode is nonzero and must lie in the kernel of \(I-\kappa K_{2d}\). Strictly different threshold levels exclude extra character sectors. A mode at equality has energy exactly \(2d\), not greater.

**4. Exact adjacent-corner ratio.** Take \(\ell=1\), put \(a(t)=e^{-2t}I_0(2t)\), \(b(t)=e^{-2t}I_1(2t)\), and \(f(t)=a(t)+b(t)\). The standard Bessel recurrences give \(f'(t)=-b(t)/t\). Since \(d>2\), both endpoints of \(t f(t)^d\) vanish. Integration of its derivative yields
\[
\int_0^\infty f(t)^d\,dt
=d\int_0^\infty f(t)^{d-1}b(t)\,dt.
\]
But \(\Lambda_{d,0}(1)=\int f^d\) and
\[
\Lambda_{d,1}(1)=\int_0^\infty f^{d-1}(a-b)\,dt
=\Lambda_{d,0}(1)-2\int_0^\infty f^{d-1}b\,dt
=\frac{d-2}{d}\Lambda_{d,0}(1).
\]
Taking reciprocals proves the ratio.

## Verification

The accompanying executable `check.py` uses scaled Bessel quadrature for the threshold matrix sectors; an independent Brillouin-zone trapezoid quadrature at strictly outside-band energies; a direct finite periodic cubic-lattice Hamiltonian constructed with sparse Kronecker products; and numerical comparisons of the exact adjacent-corner identity for three dimensions and separations. It passed 79 explicitly asserted checks. In particular, the independent finite periodic lattice tests recover counts \(1,4,7,8\) at strengths \(3,5,7,10\), using an above-edge buffer to avoid finite-volume perturbative shifts. These computations are numerical corroboration, not a proof of the infinite-volume theorem. The threshold square-summability assertion is proved by Fourier-integrability analysis, not by finite-volume tests.

Reproduce by running `python check.py` with Python, NumPy, and SciPy. The numerical thresholds are approximate; the integral formula is exact.

## Relationship to prior work

Lattice Green functions for atomistic defect response are classical. Trinkle (2006) develops numerical treatment and long-distance behavior of lattice Green functions in defect mechanics. Slager, Rademaker, Zaanen and Balents (2015) use local Green-function zeros and impurity bound states to diagnose topological insulating phases, for a different multiband Hamiltonian and impurity geometry. Hiroshima, Muminov and Kuljanov (2018) explicitly establish Birman–Schwinger threshold and resonance classifications for an origin-plus-coordinate-neighbor delta-potential family, not for identical impurities on all vertices of a spaced hypercube. Their analysis establishes important antecedents for the method and for the distinction between threshold resonances and eigenfunctions.

The finite-rank resolvent reduction and Walsh diagonalization by themselves are standard tools. The contribution assessed here is their combined *exact geometry-specific conclusion*: a strictly ordered binomial sequence of impurity-binding thresholds for all dimensions \(d\ge3\) and separations \(\ell\ge1\), full critical-state classification, and the adjacent-corner dimension-only threshold ratio. A generic finite-rank criterion does not numerically specify these threshold sectors or their strict ordering without the additional heat-kernel analysis. No claim is made that the Green-function or Birman–Schwinger methods are newly discovered.

## Limitations

The theorem requires equal positive on-site couplings, a perfect hypercubic corner set, and uniform nearest-neighbor hopping on the infinite cubic lattice. It does not cover arbitrary irregular impurity arrays, unequal strengths, long-range hopping, spectral points inside the band, or interacting many-particle states. The band-edge critical modes need not be exponentially localized; their precise square-summability is classified separately. The first-publication priority of the combined geometry-specific classification has not been independently certified, and equivalent formulations in older specialized impurity literature remain a residual possibility.

## References

- Dallas R. Trinkle, *Lattice Green function for extended defect calculations: Computation and error estimation with long-range forces*, arXiv:cond-mat/0607388, first public 2006-07-14, https://arxiv.org/abs/cond-mat/0607388 .
- Robert-Jan Slager, Louk Rademaker, Jan Zaanen and Leon Balents, *Impurity Bound States and Greens Function Zeroes as Local Signatures of Topology*, arXiv:1504.04881, first public 2015-04-19, https://arxiv.org/abs/1504.04881 .
- Fumio Hiroshima, Zahriddin Muminov and Utkir Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on n-dimensional lattice*, arXiv:1804.05339, first public 2018-04-15, https://arxiv.org/abs/1804.05339 .
