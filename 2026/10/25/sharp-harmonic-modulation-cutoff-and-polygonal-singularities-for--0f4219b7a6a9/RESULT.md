# Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and \(P_r(t)=(1-r^2)/(1-2r\cos t+r^2)\). For every \(0<r<1\), positive integer \(k\), and real \(\varepsilon\), define the continuous real symmetric kernel
\[
K_{r,k,\varepsilon}(x,y)=P_r(x-y)\bigl(1+\varepsilon\cos(k(x+y))\bigr).
\]
**Theorem.** This kernel is positive semidefinite on every finite subset of the circle if and only if
\[
|\varepsilon|\le E_k(r):=\frac{2r^k}{1+r^{2k}}.
\]
For strict inequality it is strictly positive definite on every finite set of pairwise distinct sites. At \(\varepsilon=E_k(r)\), let \(\alpha=\pi/(2k)\); at \(\varepsilon=-E_k(r)\), let \(\alpha=0\). Define the regular \(2k\)-gon
\[
\mathcal P_{k,\alpha}=\{\alpha+j\pi/k:\;0\le j<2k\}\pmod{2\pi}.
\]
At either nonzero boundary amplitude, a finite Gram matrix on pairwise distinct sites is singular **if and only if** the set of sites contains all the vertices of \(\mathcal P_{k,\alpha}\). Its nullspace is then one-dimensional, given by the coefficient vector equal to \((-1)^j\) at those vertices (in their cyclic indexing) and zero at the other sites. In particular, the maximal allowable nonstationary modulation decays as \(E_k(r)=2r^k(1+O(r^{2k}))\) for fixed \(r\) as \(k\to\infty\).

## Assumptions and scope
Angles are taken modulo \(2\pi\). A complex Hermitian Gram form is nonnegative for every integer size, every set of distinct circle sites, and every complex coefficient vector exactly when the kernel is positive semidefinite. The multiplication by \(\cos(k(x+y))\) is nonstationary; the kernel is not an isotropic function of angular separation for \(\varepsilon\ne0\). Both signs of the modulation and equality cases are included. The Poisson normalization above is essential for the stated intermediate formulas, though a common positive scalar does not change positivity.

## Proof
**Fourier reduction.** The absolutely uniformly convergent Fourier expansion is
\[
P_r(t)=\sum_{n\in\mathbb Z}r^{|n|}e^{int}.
\]
For a finite complex signed measure \(\mu=\sum_{j=1}^N z_j\delta_{x_j}\), put \(F_n=\sum_j z_j e^{-inx_j}\) and \(v_n=r^{|n|/2}F_n\). Since the \(F_n\) are bounded, \(v\in\ell^2(\mathbb Z)\). Expanding the Fourier series in the quadratic form gives the **exact identity**
\[
Q_{r,k,\varepsilon}(\mu)=\sum_n|v_n|^2+\varepsilon\operatorname{Re}\sum_{\ell\in\mathbb Z}w_\ell\overline{v_{\ell+k}}v_{\ell-k},\qquad
w_\ell=r^{|\ell|-(|\ell+k|+|\ell-k|)/2}.
\]
Thus \(w_\ell=1\) when \(|\ell|\ge k\), and \(w_\ell=r^{-(k-|\ell|)}\) when \(|\ell|<k\). All exchanges are legitimate since \(r^{|n|}\) is summable.

**Defect-bond lemma.** Let \(A_J\) be the symmetric nearest-neighbor adjacency operator on \(\ell^2(\mathbb Z)\), with all edge weights \(1\) except the edge between vertices \(0\) and \(1\), whose weight is \(J\ge1\). Then
\[
\|A_J\|=J+J^{-1}.
\]
For \(J=1\), this follows from the Fourier transform of the two-sided path, or from the norm bound \(2\) and long approximately constant vectors. For \(J>1\), the strictly positive square-summable vector \(\phi_n=J^{-\operatorname{dist}(n,\{0,1\})}\) satisfies \(A_J\phi=(J+J^{-1})\phi\). The ground-state identity
\[
(J+J^{-1})\sum_n|u_n|^2-\langle u,A_Ju\rangle
=\sum_{\{m,n\}\text{ edge}}a_{mn}\phi_m\phi_n
\left|\frac{u_m}{\phi_m}-\frac{u_n}{\phi_n}\right|^2
\]
for finite-support \(u\), followed by density, proves the upper bound and shows that equality is one-dimensional. Conjugating \(A_J\) by the parity-sign operator changes its sign. Therefore its negative extremal eigenspace is also one-dimensional, spanned by alternating signs times \(\phi\). This proves the lemma.

**Sufficiency.** In the formula for \(Q\), indices \(n\) are connected only to \(n+2k\). Hence the Fourier quadratic form splits orthogonally into \(2k\) residue classes modulo \(2k\). In each class the matrix is \(I+(\varepsilon/2)A_J\), with one defect bond and ordinary weights elsewhere. The defect is \(J=r^{-(k-|\ell|)}\) for its unique edge centered at an integer \(\ell\) with \(-k<\ell\le k\), interpreted as \(J=1\) at \(\ell=k\). Its maximum is the unique bond centered at \(\ell=0\), with \(J_{\max}=r^{-k}>1\). Since \(J+J^{-1}\) is increasing for \(J\ge1\), the operator norm of the full adjacency is exactly \(r^{-k}+r^k\); the unique maximizing positive and negative bound-state eigenspaces belong to the class \(n\equiv k\pmod{2k}\). Consequently
\[
Q_{r,k,\varepsilon}(\mu)\ge
\left(1-\frac{|\varepsilon|}{2}(r^{-k}+r^k)\right)
\sum_n r^{|n|}|F_n|^2.
\]
This is nonnegative precisely for \(|\varepsilon|\le E_k(r)\), and is strictly positive below that value for each nonzero finite atomic measure, since Fourier coefficients uniquely determine a finite measure.

**Necessity and the singular set.** Put \(M=2k\), take \(x_j=\alpha+j\pi/k\) for \(0\le j<M\), and coefficients \(z_j=(-1)^j\). Fourier summation on the regular polygon yields
\[
Q_{r,k,\varepsilon}(\mu)=\frac{M^2}{1-r^{2k}}
\left[2r^k+\varepsilon\cos(2k\alpha)(1+r^{2k})\right].
\]
Choosing \(\cos(2k\alpha)=-\operatorname{sgn}(\varepsilon)\) makes this negative whenever \(|\varepsilon|>E_k(r)\), proving necessity. At equality it vanishes. The only zero spectral block at equality is the one-dimensional defect mode centered at \(\ell=0\). The polygon's Fourier sequence is nonzero only when \(n\equiv k\pmod{2k}\), and the displayed equality shows it spans that zero mode. If another finite atomic \(\mu\) has zero energy, its weighted Fourier sequence is a scalar multiple of this polygon's sequence, whence its unweighted Fourier coefficients are also proportional at **all** integers. Uniqueness of Fourier coefficients for finite complex measures (density of trigonometric polynomials in \(C(\mathbb T)\)) implies \(\mu\) is proportional to the signed polygon measure. Thus a distinct-site Gram matrix has exactly the claimed nullspace when all vertices are present, and is strictly positive otherwise.

## Verification
The included standalone standard-library script `CHECKER.py` executes 198 deterministic checks: direct spatial quadratic forms against Fourier-series expressions for multiple \((r,k,\varepsilon)\), the equality and failure signed-polygon energies for both signs, the boundary null-vector row identities, and an exact rational four-site example. Run `python3 CHECKER.py`; the expected final line begins `PASS:`. The analytic arguments above, not the finite checks, establish the infinite-dimensional criterion.

For the exact example \(r=1/2\), \(k=2\), \(\varepsilon=8/17\), and sites \(\pi/4+j\pi/2\), the Gram matrix is
\[
\frac1{17}\begin{pmatrix}27&15&3&15\\15&27&15&3\\3&15&27&15\\15&3&15&27\end{pmatrix},
\]
with eigenvalues \(0,24/17,24/17,60/17\), and null vector \((1,-1,1,-1)^T\).

## Relationship to prior work
Guella, Menegatto and Peron (2015, arXiv:1505.01169, §§1–3, especially Theorem 3.5) give a Fourier-support characterization of strict positive definiteness for **isotropic** kernels on a product of circles. The kernel here is **nonisotropic on a single circle** and its Fourier coefficient matrix has nonzero off-diagonal couplings, so the theorem does not supply this admissibility threshold. Jäger (2020, arXiv:2005.02798, §§1–3) develops general Fourier-matrix criteria for nonisotropic kernels on the **two-sphere**, and an eigenvalue-block characterization; that general framework does not give the present circle Poisson defect-bond norm or the exact alternating polygon singularity. The classical Poisson expansion supplies the analytic input; the all-harmonic sharp threshold and complete finite-configuration boundary are the additional statements established here.

## Limitations
Only \(0<r<1\), positive integer \(k\), and real \(\varepsilon\) are treated; no endpoint kernel at \(r=1\) is asserted, and no classification for arbitrary nonstationary perturbations is claimed. Although the threshold is analytic, novelty has been assessed against a bounded set of relevant records and inspected sources, not independently certified; related unindexed covariance constructions or equivalent Jacobi calculations may exist. Scientific validation outside the included proof and reproducibility checks remains outstanding.

## References
1. J. C. Guella, V. A. Menegatto, A. P. Peron, *Strictly positive definite kernels on a product of circles* (first arXiv submission 2015-05-05), arXiv:1505.01169, https://arxiv.org/abs/1505.01169.
2. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry* (first arXiv submission 2020-05-06), arXiv:2005.02798, https://arxiv.org/abs/2005.02798.
