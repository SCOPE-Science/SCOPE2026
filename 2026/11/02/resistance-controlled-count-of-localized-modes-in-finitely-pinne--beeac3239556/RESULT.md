# Resistance-controlled count of localized modes in finitely pinned square lattices

## Finding
Consider the infinite scalar nearest-neighbour mass-spring lattice on \(\mathbb Z^2\) with unit masses, unit inter-site spring stiffnesses, and a finite set of positive springs that pin selected sites to a fixed foundation. Arbitrarily weak positive foundation pinning generates at least one localized mode above the unpinned phonon band, but further modes require precise strength-and-geometry thresholds.

For any integer \(p\geq1\), distinct sites \(r_1,\ldots,r_p\in\mathbb Z^2\), and arbitrary strengths \(\kappa_1,\ldots,\kappa_p>0\), define the infinite square-grid unit-resistor effective resistance
\[
R(d)=\int_{[-\pi,\pi]^2}\frac{2[1-\cos(k\cdot d)]}{4-2\cos k_1-2\cos k_2}\,\frac{d^2k}{(2\pi)^2},\qquad R(0)=0.
\]
On the \((p-1)\)-dimensional real subspace \(E=\{y\in\mathbb R^p:\sum_i y_i=0\}\), form the quadratic form
\[
\mathcal Q(y)=-\frac12\sum_{i,j=1}^p y_i y_j R(r_i-r_j)-\sum_{i=1}^p\frac{y_i^2}{\kappa_i}.
\]
Then the **exact number of square-summable vibrational eigenmodes with squared frequency strictly above the unpinned band** (multiplicities included) is
\[
\boxed{N_{>8}=1+n_+(\mathcal Q|_E).}
\]
Here \(n_+\) denotes the number of strictly positive eigenvalues of the symmetric form. In particular, \(1\le N_{>8}\le p\), and a zero eigenvalue of \(\mathcal Q|_E\) contributes **no additional above-band mode**. The formula is valid for every finite configuration and does not assume equal pinning strengths or geometric symmetry.

For two pinned sites at displacement \(d\),
\[
\boxed{N_{>8}=1+\mathbf 1\{R(d)>\kappa_1^{-1}+\kappa_2^{-1}\}.}
\]
With equal strength \(\kappa\), adjacent sites have exactly two modes iff \(\kappa>4\), whereas diagonal neighbours have exactly two iff \(\kappa>\pi\). An exact three-site staircase holds for equally pinned right-angle corners \(r_1=(0,0),r_2=(1,0),r_3=(0,1)\):
\[
\boxed{N_{>8}=1+\mathbf1\{\kappa>\pi\}+\mathbf1\{\kappa>3\pi/(\pi-1)\}.}
\]
At each equality the lower mode count applies. The second corner threshold is approximately \(4.4008266208\).

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z^2)\). Write \(e_1=(1,0)\), \(e_2=(0,1)\) and
\[
(H_0u)(r)=4u(r)-u(r+e_1)-u(r-e_1)-u(r+e_2)-u(r-e_2).
\]
The operator of squared normal-mode frequencies is
\[
H=H_0+\sum_{i=1}^p\kappa_i\lvert\delta_{r_i}\rangle\langle\delta_{r_i}\rvert.
\]
The Fourier dispersion of \(H_0\) is \(4-2\cos k_1-2\cos k_2\), so its essential spectrum is \([0,8]\); the finite-rank perturbation preserves this essential spectrum. All pinning strengths are strictly positive; repeated sites must first be merged by summing their strengths. The count excludes threshold modes at squared frequency \(8\) and pertains only to the discrete spectrum \((8,\infty)\). No claim is made about a complete classification of threshold resonances, propagation bands of other lattices, or negative pinning.

## Proof
**Step 1: positive finite-dimensional resolvent.** For \(\mu>0\), the lattice unitary \((Uu)(r)=(-1)^{r_1+r_2}u(r)\) satisfies \(UH_0U=8I-H_0\). Thus
\[
(8+\mu-H_0)^{-1}=U(\mu+H_0)^{-1}U.
\]
Write \(C_\mu(d)=\langle\delta_0,(\mu+H_0)^{-1}\delta_d\rangle\), let \(D=\operatorname{diag}(\sqrt{\kappa_i})\), and set \(B_\mu=D[C_\mu(r_i-r_j)]_{i,j=1}^pD\). The finite-site staggering signs act by orthogonal similarity and therefore do not change the eigenvalues of this positive-definite matrix. The finite-rank Birman--Schwinger correspondence identifies \(8+\mu\) as an eigenvalue of \(H\) iff \(1\) is an eigenvalue of \(B_\mu\), with the same multiplicity. For every nonzero \(x\in\mathbb R^p\),
\[
\frac{d}{d\mu}\langle x,B_\mu x\rangle=-\left\| (\mu+H_0)^{-1}\sum_i\sqrt{\kappa_i}x_i\delta_{r_i}\right\|_2^2<0.
\]
Thus every ordered eigenvalue of \(B_\mu\) decreases strictly with \(\mu\), and all tend to zero as \(\mu\to\infty\). Accordingly, \(N_{>8}\) is the number of branches whose limits at \(\mu\downarrow0\) are strictly greater than one; branches with limit equal to one cannot cross one at positive \(\mu\).

**Step 2: resistance as the finite Green-kernel difference.** The Fourier integral gives
\[
C_\mu(d)=\int_{[-\pi,\pi]^2}\frac{e^{ik\cdot d}}{\mu+4-2\cos k_1-2\cos k_2}\,\frac{d^2k}{(2\pi)^2}.
\]
Its diagonal \(c_\mu=C_\mu(0)\) diverges to \(+\infty\) logarithmically because the two-dimensional dispersion is quadratic near \(k=0\). By dominated convergence after cancelling the common singularity,
\[
C_\mu(0)-C_\mu(d)\longrightarrow\frac12R(d).
\]
Indeed, \(1-\cos(k\cdot d)=O(|k|^2)\) and the denominator is comparable to \(|k|^2\) around zero. It follows entrywise, hence in finite-dimensional operator norm, that
\[
B_\mu=c_\mu vv^{\mathsf T}+M+o(1),\quad v_i=\sqrt{\kappa_i},\quad M_{ij}=-\tfrac12\sqrt{\kappa_i\kappa_j}R(r_i-r_j).
\]

**Step 3: singular rank-one separation and exact crossings.** The min--max principle, or block Gaussian elimination in the splitting \(\mathbb R^p=\operatorname{span}\{v\}\oplus v^\perp\), gives exactly one eigenvalue of \(B_\mu\) tending to \(+\infty\). All other eigenvalues tend, including multiplicities, to the eigenvalues of the compression \(P_{v^\perp}M|_{v^\perp}\). This follows because the divergent scalar diagonal block has inverse tending to zero, so its Schur-complement correction to the finite block vanishes.

The map \(x\mapsto y=Dx\) bijectively sends \(v^\perp\) to \(E=\{y:\sum_i y_i=0\}\). Under this map
\[
x^{\mathsf T}(M-I)x=-\frac12\sum_{ij}y_i y_jR(r_i-r_j)-\sum_i\frac{y_i^2}{\kappa_i}=\mathcal Q(y).
\]
Sylvester's law of inertia shows that the number of compressed limiting eigenvalues **strictly larger than one** is \(n_+(\mathcal Q|_E)\), independent of the nonorthogonal congruence. The one divergent branch adds one crossing. The strict monotonicity in Step 1 handles all equalities exactly and proves the stated formula.

**Step 4: explicit small configurations.** For two sites write \(y=(t,-t)\). Then \(\mathcal Q(y)=t^2[R(d)-1/\kappa_1-1/\kappa_2]\), giving the two-site criterion. Standard square-grid resistance integrals yield \(R(1,0)=1/2\) and \(R(1,1)=2/\pi\). For the three-pin corner, the form \(-[R(r_i-r_j)]/2\) on \(E\) has two eigenvalues \(1/\pi\) (arm-antisymmetric vector \((0,1,-1)\)) and \((\pi-1)/(3\pi)\) (corner-vs-arms vector \((-2,1,1)\)). With a common pin \(\kappa\), \(\mathcal Q\) shifts both eigenvalues by \(-1/\kappa\). Their positivity thresholds are, respectively, \(\kappa>\pi\) and \(\kappa>3\pi/(\pi-1)\), with strict inequalities.

Finally, every eigenvalue above eight lies outside the unperturbed band, and the resolvent Green kernel at that energy decays exponentially (by an analytic Fourier continuation or Combes--Thomas estimate). Therefore these \(\ell^2\) eigenvectors correspond to spatially localized normal modes.

## Verification
The independent script `check_square_pinning.py` computes the resistance integral by Fourier summation on increasingly large periodic grids; verifies the exact nearest-neighbour and diagonal resistances; checks compressed threshold inertias for the three-site corner at several coupling strengths; and independently diagonalizes a finite periodic mass-spring operator at three couplings. It passed 23 comparisons. In the \(70\times70\) periodic tests, couplings \(\kappa=2,3.5,6\) produced, respectively, one, two, and three squared-frequency eigenvalues exceeding eight. These finite-volume results are consistency tests only: the proof above establishes the arbitrary infinite-lattice statement and exact threshold-equality convention.

To reproduce, run `python check_square_pinning.py` with NumPy and SciPy installed. Finite grids are not used to establish the logarithmic divergence of the infinite resolvent or an infinite-dimensional mode count.

## Relationship to prior work
Cserti's 1999 open preprint calculates the infinite square-grid resistor Green function and the resistance values \(R(1,0)=1/2\) and \(R(1,1)=2/\pi\). Those are existing inputs, not claimed as new. Generic finite-rank Birman--Schwinger theory is likewise existing machinery. The claim assessed here is their **finite-configuration two-dimensional phonon mode-count consequence**: exactly one unconditional above-band mode plus an arbitrary-dimensional effective-resistance inertia count with strict equality rules, illustrated by the three-pin corner staircase.

Lipkin and Mannheim discuss impurity-phonon localization bounds for substitutional impurities and do not provide this arbitrary-site positive-ground-pinning exact count. Kutsenko develops a Floquet determinant method for periodic lattices with finite defects (including examples of mass and line defects), not the present all-finite-configuration effective-resistance inertia classification. Hiroshima, Muminov and Kuljanov study a two-parameter origin-and-nearest-neighbour delta-potential family and mostly lower-band threshold regimes; their parameter-restricted analysis does not imply the unequal-strength, arbitrary-site corner thresholds as stated. Thomas and colleagues' subsequent variational work provides sufficient existence criteria for mass perturbations in a two-dimensional spring lattice, rather than the exact number of positive-foundation-pinning modes. A published exact-threshold study of the Hiroshima--Muminov--Kuljanov special delta model was separately read; its parameter-specific lower-edge constants are different from and do not determine this general resistance-inertia count.

## Limitations
Historical priority is provisional. In particular, a general finite-support spectral-index theorem under other notation may already imply the resistance inertia law, since the proof uses established resolvent and inertia techniques. The searched accessible primary papers did not state the full arbitrary-configuration criterion or the explicit three-pin staircase, but absence from those papers is not a general novelty guarantee. The model has scalar out-of-plane displacements, equal masses and nearest-neighbour lattice springs, and strictly positive on-site foundation springs only. It does not classify band-edge resonances or more general mass, bond, damping, or vector-polarization defects. This is an analytical self-review only; no independent scientific audit has been performed.

## References
1. J. Cserti, *Application of the lattice Green's function for calculating the resistance of an infinite networks of resistors*, arXiv:cond-mat/9909120v1 (public 1999-09-08), https://arxiv.org/abs/cond-mat/9909120.
2. A. Kutsenko, *Periodic lattice with defects*, arXiv:1305.1228v1 (public 2013-05-06), https://arxiv.org/abs/1305.1228.
3. H. J. Lipkin and P. Mannheim, *Bounds on Localized Modes in the Crystal Impurity Problem*, arXiv:cond-mat/0510542 (2005), https://arxiv.org/abs/cond-mat/0510542.
4. F. Hiroshima, Z. Muminov, and U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on n-dimensional lattice*, arXiv:1804.05339v1 (2018), https://arxiv.org/html/1804.05339v1.
5. J. Thomas, R. Arrieta, S.-C. Yang, A. J. Parzygnat, and S. G. Johnson, *When can phonon modes be trapped by arbitrarily weak local defects? Rigorous sufficient conditions in a monatomic lattice*, arXiv:2511.03580v2 (2026), https://arxiv.org/html/2511.03580v2.
