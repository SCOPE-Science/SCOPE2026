# Complete spherical-harmonic sampling spectra on orthogonal regular circles

## Finding

For every integer \(m\ge 2\), two mutually orthogonal regular \(2m\)-gons on the unit three-sphere have a completely explicit evaluation spectrum in *every* exact spherical-harmonic degree \(\ell\ge0\). The spectrum is unaffected by rotating either polygon within its own circle. The combined configuration includes the binary dihedral (dicyclic) group of order \(4m\) in the unit quaternions.

Let \(n=2m\), and for each residue \(a\in\{0,\ldots,n-1\}\), define the nonnegative integer
\[
c_a(m,\ell)=\#\{j\in\{0,\ldots,\ell\}:\ell-2j\equiv a\pmod n\}.
\]
Put \(s_\ell=0\) when \(\ell\) is odd, and \(s_{2k}=(-1)^k\) for even degrees. The **entire** multiset of \(4m\) eigenvalues of the sample-space Gram matrix \(E_{m,\ell}E_{m,\ell}^{*}\), counting zeros, is
\[
\boxed{\left\{n(\ell+1)c_a(m,\ell)\ :\ 1\le a<n\right\}\text{ (each twice)},\quad n(\ell+1)(c_0(m,\ell)+s_\ell),\quad n(\ell+1)(c_0(m,\ell)-s_\ell).}
\]
Here “each twice” means that each listed residue contributes two eigenvalues, even when several listed numbers coincide. In particular, all Gram eigenvalues are nonnegative integers. The positive eigenvalues are also the eigenvalues of \(E_{m,\ell}^{*}E_{m,\ell}\); their square roots are the nonzero singular values of \(E_{m,\ell}\).

The **exact evaluation rank** is
\[
\boxed{\operatorname{rank}E_{m,\ell}=\begin{cases}
2\min\{m,\ell+1\},&\ell\text{ odd},\\
2\min\{m,\ell+1\}-1,&\ell\text{ even and }0\le\ell<2m,\\
2m,&\ell\text{ even and }\ell\ge2m.
\end{cases}}
\]
Thus the odd-degree evaluations first attain the antipodal upper bound \(2m\) at the smallest odd \(\ell\ge m-1\). Yet all even degrees below \(2m\) have a one-dimensional deficit after their Fourier modes fill the available residue classes. The deficit disappears at the even degree \(2m\). This yields genuine rank decreases with increasing *exact* harmonic degree: for \(m=4\), the ranks at degrees \(3,4,5\) are \(8,7,8\).

The singular spectrum has a useful **tightness transition** at three consecutive degrees. At \(\ell=2m-2\), all \(2m-1\) positive Gram eigenvalues equal \(4m(2m-1)\), with one additional zero after antipodal reduction. At \(\ell=2m-1\), all \(2m\) positive eigenvalues equal \(8m^2\), so the evaluation is exactly tight on the antipodal-compatible sample subspace. At \(\ell=2m\), one positive eigenvalue equals \(8m(2m+1)\) and the other \(2m-1\) positive eigenvalues equal \(4m(2m+1)\), so the nonzero singular-value condition number is exactly \(\sqrt2\). More generally, for fixed \(m\), as \(\ell\to\infty\) every positive Gram eigenvalue is \(2(\ell+1)^2+O_m(\ell)\), and the nonzero singular-value condition number tends to \(1\). This distinction concerns conditioning on the reachable antipodal sample-value subspace, not unique recovery of every harmonic coefficient.

There is also a precise relation explaining the deficit. For every even \(\ell=2k<2m\) and every \(H\in\mathcal H_{2k}(S^3)\),
\[
\boxed{\sum_{j=0}^{2m-1} H(e^{i(\alpha+\pi j/m)},0)
=(-1)^k\sum_{j=0}^{2m-1} H(0,e^{i(\beta+\pi j/m)}) .}
\]
This relation is the only extra row dependence after antipodal identification whenever \(\ell+1\ge m\) and \(\ell<2m\).

## Assumptions and scope

Identify \(S^3\) with \(\{(z,w)\in\mathbb C^2:|z|^2+|w|^2=1\}\) with the standard real inner product. For arbitrary real phases \(\alpha,\beta\), set
\[
X_{m;\alpha,\beta}=\{(e^{i(\alpha+\pi j/m)},0):0\le j<2m\}\ \cup\ \{(0,e^{i(\beta+\pi j/m)}):0\le j<2m\}.
\]
These are \(4m\) *distinct* points on two orthogonal great circles. The phases may be chosen independently; the spectrum does not depend on them. Setting the phases to zero yields the standard quaternionic binary-dihedral vertex set \(\{e^{\pi i j/m},j_{\!\mathbb H}e^{\pi i j/m}\}\), after possibly reversing the orientation of its second circle.

Let \(\mathcal H_\ell(S^3)\) be the complex, exactly-degree-\(\ell\) spherical-harmonic space, of dimension \((\ell+1)^2\). Equip it with the inner product from **probability surface measure** on \(S^3\), choose any orthonormal basis, and define \(E_{m,\ell}\) by evaluating those basis functions at the ordered sample points. The sampling matrix has \(4m\) rows and \((\ell+1)^2\) columns. Sample weights are all \(1\) (not divided by \(4m\)); this fixes the eigenvalue normalization. The conclusions concern a *single exact degree*, not the whole band of degrees at most \(\ell\).

## Proof

**1. Addition formula.** The reproducing kernel of \(\mathcal H_\ell(S^3)\), under probability-measure normalization, is
\[
K_\ell(x,y)=(\ell+1)U_\ell(\langle x,y\rangle_{\mathbb R^4}),
\]
where \(U_\ell\) is the Chebyshev polynomial of the second kind. Indeed \(U_\ell(1)=\ell+1\), so \(K_\ell(x,x)=(\ell+1)^2=\dim\mathcal H_\ell(S^3)\), fixing the normalization. Consequently \(E_{m,\ell}E_{m,\ell}^{*}\) is the matrix of \(K_\ell\) on the sample set.

**2. Two circulant blocks and constant coupling.** Put \(n=2m\). The real inner product of points with indices \(j,h\) in either single circle is \(\cos(2\pi(j-h)/n)\), irrespective of the phase. Points on different circles are orthogonal, so each cross-circle Gram entry equals \((\ell+1)U_\ell(0)\). Hence the Gram matrix has two identical \(n\)-by-\(n\) circulant diagonal blocks and two constant off-diagonal blocks. At zero inner product, the recurrence for \(U_\ell\) gives \(U_\ell(0)=s_\ell\).

**3. Exact diagonalization.** For every real \(\theta\), continuity at the removable singularities understood,
\[
U_\ell(\cos\theta)=\frac{\sin((\ell+1)\theta)}{\sin\theta}=\sum_{j=0}^{\ell} e^{i(\ell-2j)\theta}.
\]
The discrete Fourier character of residue \(a\in\mathbb Z/n\mathbb Z\) therefore has eigenvalue \(n(\ell+1)c_a(m,\ell)\) in each diagonal circulant block. A constant off-diagonal block kills every nonconstant Fourier character. Thus, for each \(1\le a<n\), two mutually independent Fourier vectors have the claimed eigenvalue. On the remaining two-dimensional subspace of vectors constant on each circle, the Gram operator is
\[
n(\ell+1)\begin{pmatrix}c_0(m,\ell)&s_\ell\\s_\ell&c_0(m,\ell)\end{pmatrix},
\]
whose eigenvalues are precisely the remaining two displayed numbers. This exhausts all \(2n=4m\) Gram eigenvalues and proves phase invariance.

**4. Rank and boundaries.** The frequencies \(\ell,\ell-2,\ldots,-\ell\), after division by their common parity, form \(\ell+1\) consecutive residue classes modulo \(m\). Hence exactly \(\min\{m,\ell+1\}\) of the \(c_a\)'s are positive, and they occupy residues with the same parity as \(\ell\).

If \(\ell\) is odd, then \(s_\ell=c_0=0\), and every occupied residue contributes two positive eigenvalues: the rank is \(2\min\{m,\ell+1\}\). If \(\ell=2k\) is even, residue zero is always occupied and
\[
c_0(m,2k)=1+2\lfloor k/m\rfloor.
\]
For \(k<m\), the two constant-mode eigenvalues are one positive number and zero; the other occupied residues contribute two each, giving rank \(2\min\{m,2k+1\}-1\). For \(k\ge m\), both constant eigenvalues are positive, all \(m\) even residues occur, and the rank is \(2m\). The cases \(m=2\) and \(\ell=0\) are included, with degree-zero rank \(1\).

**5. Tightness and asymptotic consequences.** When \(\ell=2m-2\), the \(2m-1\) consecutive even frequencies exhaust \(m\) residue classes: the zero residue has multiplicity one and each nonzero occupied residue has multiplicity two. Thus the positive constant-mode eigenvalue and all nonconstant positive eigenvalues are \(2n(\ell+1)\). For \(\ell=2m-1\), each occupied odd residue has multiplicity two. For \(\ell=2m\), the zero residue has multiplicity three and every other even residue has multiplicity two; the constant-mode pair consequently has scalar factors \(2,4\). These give the three claimed transition spectra. For arbitrary \(\ell\), each occupied residue count differs from \((\ell+1)/m\) by at most one. The extra constant-mode coupling has absolute size one, yielding the bound \(\lvert\lambda-2(\ell+1)^2\rvert\le4m(\ell+1)\) for each positive eigenvalue once \(\ell\ge2m\). This proves convergence of the nonzero singular-value condition number to one.

**6. Signed quadrature identity.** At every even degree \(2k<2m\), the null vector in the two-dimensional constant-mode subspace is proportional to \((\mathbf 1,-(-1)^k\mathbf 1)\). Since the Gram matrix is \(EE^*\), its nullspace equals the kernel of \(E^*\). Taking the inner product with the sample-value vector of any \(H\in\mathcal H_{2k}(S^3)\) gives the stated relation. For \(\ell+1\ge m\), the rank formula proves it is the only dependence in addition to the antipodal identifications.

## Verification

The standalone standard-library program `check_spectrum.py` performs two different finite checks. For \(2\le m\le20\) and \(0\le\ell\le120\), it uses integer arithmetic to test the complete eigenvalue list, the rank formula, nonnegativity, and the trace \(4m(\ell+1)^2\): \(2{,}299\) combinations. It also builds the raw addition-kernel matrix directly from cosine/sine coordinates and the independent three-term Chebyshev recurrence for \(357\) configurations, including three phase choices, and checks \(7{,}140\) predicted eigenpairs. All tests pass under the stated numerical tolerance. Reproduce with `python3 check_spectrum.py`. The all-parameter claim is established by the proof above, not by finite tests.

## Relationship to prior work

Classical spherical-code and harmonic-reproducing-kernel methods underlie the addition formula; Delsarte–Goethals–Seidel (1977) is foundational background. Kramer (arXiv:0901.0511, publicly submitted January 5, 2009) constructs invariant harmonics for the ordinary quaternion group as a deck transformation group of a spherical three-manifold. Dowker (arXiv:0909.3380, submitted September 18, 2009) develops harmonics on factored three-spheres and describes invariant bases for cyclic and dihedral groups. Those works treat harmonic invariance and quotient-manifold eigenmodes; the present result instead calculates *all* point-evaluation singular values for two complete polygonal orbits, including all \(m\), all \(\ell\), arbitrary independent phases, and the exact aliasing defects. The character-selection formulas in those works are relevant background but do not directly state this row-Gram spectrum. Classical spherical-design conditions address moment cancellation rather than the singular spectrum.

## Limitations

The result is for two equal-size regular polygons on orthogonal great circles of \(S^3\), unit sample weights, and exactly one harmonic degree. It does not classify arbitrary multi-ring configurations or conditioning of the entire degree-at-most-\(L\) space. The calculation uses standard reproducing-kernel and cyclic Fourier machinery, and equivalently formulated older results in representation-theoretic sampling literature remain an originality risk. A separate independent mathematical audit has not been performed.

## References

1. P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata **6** (1977), 363–388. DOI: 10.1007/BF03187604.
2. P. Kramer, *Platonic polyhedra tune the 3-sphere: II. Harmonic analysis on cubic spherical 3-manifolds*, arXiv:0901.0511 (first submitted 2009-01-05). https://arxiv.org/abs/0901.0511.
3. J. S. Dowker, *Harmonics on the factored three-sphere and the Hopf map*, arXiv:0909.3380 (first submitted 2009-09-18). https://arxiv.org/abs/0909.3380.
4. C. An, X. Chen, I. H. Sloan, R. S. Womersley, *Well conditioned spherical designs for integration and interpolation on the two-sphere*, SIAM J. Numer. Anal. **48** (2010), 2135–2157. DOI: 10.1137/100795140 (comparison of design-based interpolation objectives on a different sphere).
