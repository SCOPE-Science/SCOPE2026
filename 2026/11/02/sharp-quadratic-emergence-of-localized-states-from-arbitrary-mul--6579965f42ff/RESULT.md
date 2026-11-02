# Sharp quadratic emergence of localized states from arbitrary multi-impurity thresholds

## Finding

For every integer \(m\ge4\), every hopping strength \(J>0\), every set of distinct integer sites \(s_1<\cdots<s_m\), and every common positive impurity strength \(V\), consider the tight-binding operator on \(\ell^2(\mathbb Z)\)
\[
(H_V\psi)(n)=J\bigl(\psi(n-1)+\psi(n+1)\bigr)+V\sum_{i=1}^{m}\mathbf{1}_{\{n=s_i\}}\psi(n).
\]
Set the positive gaps \(d_i=s_{i+1}-s_i\) and let \(L\) be the weighted Neumann path Laplacian
\[
\langle u,Lu\rangle=\sum_{i=1}^{m-1}\frac{J}{d_i}|u_{i+1}-u_i|^2,
\qquad 0=\nu_0<\nu_1<\cdots<\nu_{m-1}.
\]
As background for the quantitative result, the spectrum of \(H_V\) outside the essential interval \([-2J,2J]\) consists of exactly
\[
N(V)=\#\{j\in\{0,\ldots,m-1\}:V>\nu_j\}
\]
**simple** eigenvalues, all strictly above \(2J\). The count is the weighted-path form of a known one-dimensional point-interaction inertia classification; it is included to fix normalization and is not asserted as the original contribution. At \(V=\nu_j\), where \(j\ge1\), the corresponding emerging mode is a bounded but nonsquare-summable threshold resonance, and hence does not count as a bound state.

**The new quantitative assertion is the exact coefficient of eigenvalue emergence in the discrete tight-binding energy.** For each normalized real eigenvector \(u^{(j)}\) of \(L\) with \(j\ge1\), define \(b_j=|u^{(j)}_1|^2+|u^{(j)}_m|^2>0\). The unique mode \(E_j(V)>2J\) born as \(V\) increases past \(\nu_j\) satisfies the sharp quadratic law
\[
\lim_{V\downarrow\nu_j}\frac{E_j(V)-2J}{(V-\nu_j)^2}=\frac{1}{Jb_j^2}.
\]
For equally spaced defects \(s_i=s_1+(i-1)d\), the critical strengths and coefficients are explicitly
\[
\nu_j=\frac{2J}{d}\left(1-\cos\frac{j\pi}{m}\right),\qquad
b_j=\frac4m\cos^2\frac{j\pi}{2m},\qquad 1\le j<m.
\]
The novelty assessment concerns the sharp energy-emergence coefficient at each nontrivial threshold, not the general Birman--Schwinger reduction, the finite-rank bound, or the already known inertia count by the analogous continuum point-interaction Jacobi matrix.

## Assumptions and scope

The lattice is bi-infinite and one-dimensional. Hopping is uniform and real, and all \(m\) defects are positive, equal, point-supported, and occupy distinct integer sites. The theorem concerns the discrete spectrum and bounded threshold solutions; it does not assert a finite-time transport rate, a many-body effect, or a localization law for unequal defect strengths. The free adjacency dispersion is \(2J\cos k\), fixing the band edge at \(2J\).

## Proof

**1. Free resolvent and finite-rank reduction.** For \(E>2J\), write \(E=2J\cosh\kappa\) with \(\kappa>0\). The compression of the free resolvent to the defect sites is the positive definite matrix
\[
G_{ij}(\kappa)=\langle\delta_{s_i},(E-H_0)^{-1}\delta_{s_j}\rangle=\frac{e^{-\kappa|s_i-s_j|}}{2J\sinh\kappa}.
\]
The Birman--Schwinger equation states that \(E\) is an eigenvalue of \(H_V\) if and only if \(V^{-1}\) is an eigenvalue of \(G(\kappa)\), with matching multiplicity. Equivalently, \(V\) is an eigenvalue of \(Q(\kappa)=G(\kappa)^{-1}\).

**2. The exact tridiagonal precision identity.** Put \(r_i=e^{-d_i\kappa}\). The correlation matrix \(R_{ij}=e^{-\kappa|s_i-s_j|}\) has successive correlations \(r_i\). Its inverse quadratic form is
\[
\langle u,R^{-1}u\rangle=|u_1|^2+\sum_{i=1}^{m-1}\frac{|u_{i+1}-r_iu_i|^2}{1-r_i^2}.
\]
This is an exact factorization: sequentially set \(z_1=u_1\) and \(z_{i+1}=(u_{i+1}-r_iu_i)/\sqrt{1-r_i^2}\). This triangular change of variables whitens the Gaussian covariance \(R\): its conditional innovations are independent because consecutive correlations are \(r_i\). Multiplication of the precision factors therefore gives the displayed exact inverse. Consequently
\[
\langle u,Q(\kappa)u\rangle=2J\sinh\kappa\left(|u_1|^2+\sum_{i=1}^{m-1}\frac{|u_{i+1}-r_iu_i|^2}{1-r_i^2}\right).
\]
Each off-diagonal entry of \(Q(\kappa)\) is strictly negative, so the real symmetric tridiagonal matrix has simple eigenvalues.

**3. The spectral threshold.** Expanding \(e^{-d_i\kappa}\) and \(\sinh\kappa\), with all gaps fixed, yields the matrix expansion
\[
Q(\kappa)=L+J\kappa(e_1e_1^{\mathsf T}+e_me_m^{\mathsf T})+O(\kappa^2),\qquad\kappa\downarrow0.
\]
In particular, \(Q(0)=L\). A positive-weight path Laplacian has the strictly simple eigenvalues \(0=\nu_0<\cdots<\nu_{m-1}\), and every eigenvector has nonzero first and last components: vanishing at one endpoint forces successive vanishing along the irreducible tridiagonal recurrence. Thus \(b_j>0\).

**4. Exactly one crossing per branch.** As \(E\) increases, \(G(E)\) is strictly decreasing in Loewner order because
\[
\frac{dG}{dE}=-P(E-H_0)^{-2}P^{\mathsf T}\prec0,
\]
where \(P\) evaluates a sequence at the defect sites. Consequently \(Q(E)=G(E)^{-1}\) increases strictly in Loewner order. Every ordered eigenvalue branch of \(Q(E)\) is continuous and strictly increasing, starts at \(\nu_j\) as \(E\downarrow2J\), and tends to infinity as \(E\to\infty\). Hence a branch crosses \(V\) exactly once if and only if \(V>\nu_j\). Simplicity follows from the tridiagonal form.

**5. Boundary and exclusion of other point spectrum.** A finite-rank perturbation preserves essential spectrum \([-2J,2J]\). Since \(H_V\ge H_0\ge-2J\), there is no eigenvalue below the band. At any energy inside or at the band, a free solution on a defect-free half-line is oscillatory or affine (alternating affine at the lower edge); square summability forces it to vanish on that half-line, and the second-order recurrence then forces global vanishing. At \(V=\nu_j\), an eigenvector of \(L\) defines a nonzero bounded solution of \(H_V\psi=2J\psi\): interpolate linearly between its endpoint values at the sites \(s_i\) and extend constantly to either exterior half-line. The defect equations are exactly \(Lu=Vu\). Endpoint nonvanishing makes this solution nonsquare-summable. Thus equality is a resonance, not an eigenvalue.

**6. Quadratic birth coefficient.** For a simple eigenpair of \(L\), standard finite-dimensional eigenvalue perturbation of the expansion in Step 3 gives
\[
\lambda_j(Q(\kappa))=\nu_j+Jb_j\kappa+O(\kappa^2).
\]
Solving \(\lambda_j(Q(\kappa))=V\) yields \(\kappa=(V-\nu_j)/(Jb_j)+O((V-\nu_j)^2)\). Since \(E-2J=J\kappa^2+O(\kappa^4)\), the stated limit follows. Finally, the discrete cosine basis diagonalizes an equally weighted Neumann path and yields the explicit formulas above.

## Verification

The bundled `verify.py` constructs the full free-resolvent matrix independently of its tridiagonal inverse, checks their product numerically, and compares the finite-dimensional secular energies to the eigenvalues of long finite chains. It also checks the first-order threshold matrix expansion, the quadratic birth prefactor where numerically conditioned, and the equispaced cosine formulas. `verify_output.txt` records a reproducible seeded run. These finite tests corroborate but do not replace the proof for all \(m\), placements and strengths.

As a concrete asymmetric four-impurity case, the sites \((0,2,5,9)\) with \(J=1\) have three positive thresholds, approximately \(0.1909830056\), \(0.6666666667\), and \(1.3090169944\). Their corresponding quadratic onset coefficients are approximately \(1.38286941\), \(5.97530864\), and \(17.28379725\).

## Relationship to prior work

Goloschapova and Oridoroga (2009), arXiv:0903.1180v1, Theorem 3.8, explicitly identify the negative-eigenvalue count of a continuum multi-point delta model with the inertia of a finite Jacobi matrix of interval distances and point strengths; its weighted-path count is mathematically equivalent to the count displayed here, and that part is **not** claimed as novel. The sharp quadratic emergence coefficient in the **discrete lattice energy** for arbitrary gaps is the assessed contribution. Hiroshima, Sasaki, Shirai and Suzuki (2012), arXiv:1209.0522v1, give discrete point-perturbation eigenvalue and edge analysis for a single site. Ito and Jensen (2013), arXiv:1312.1396v1, establish broad threshold-resolvent classifications, including general local potentials and resonance distinctions, but do not tabulate the arbitrary finite equal-strength defect thresholds in the weighted-path form. Hiroshima, Muminov and Kuljanov (2018), arXiv:1804.05339v1, obtain a detailed multi-parameter analysis for three neighboring lattice impurities in the one-dimensional case, rather than an arbitrary number at arbitrary gaps. Related continuum point-interaction negative-spectrum counting methods of Albeverio and Nizhnik and successors are particularly close structurally; the assessed claim is specifically the explicit endpoint-eigenvector quadratic discrete-lattice band-edge energy onset coefficient for arbitrarily many irregularly spaced equal defects, not the known point-interaction inertia or Birman--Schwinger classification.

## Limitations

The theorem does not address unequal strengths, infinite or random defect arrays, finite lattice boundaries, nonlinear interactions, or eigenvector localization lengths beyond their threshold asymptotic. Its historical originality is a best-evidence assessment; a specialized discrete Jacobi-operator treatment could already state the same sharp onset coefficient. The full 2003 continuum point-interaction paper was not available for a direct theorem-level comparison. No independent scientific audit has been performed.

## References

- N. Goloschapova and L. Oridoroga, *On the Negative Spectrum of One-Dimensional Schrödinger Operators with Point Interactions*, arXiv:0903.1180v1, first public 2009-03-06. https://arxiv.org/abs/0903.1180
- F. Hiroshima, I. Sasaki, T. Shirai and A. Suzuki, *Note on the spectrum of discrete Schrödinger operators*, arXiv:1209.0522v1, first public 2012-09-04. https://arxiv.org/abs/1209.0522
- K. Ito and A. Jensen, *A complete classification of threshold properties for one-dimensional discrete Schrödinger operators*, arXiv:1312.1396v1, first public 2013-12-05. https://arxiv.org/abs/1312.1396
- F. Hiroshima, Z. Muminov and U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on n-dimensional lattice*, arXiv:1804.05339v1, first public 2018-04-15. https://arxiv.org/abs/1804.05339
- S. Albeverio and L. Nizhnik, *On the Number of Negative Eigenvalues of a One-Dimensional Schrödinger Operator with Point Interactions*, *Letters in Mathematical Physics* 65 (2003), 27–35. https://doi.org/10.1023/A:1027396004785
