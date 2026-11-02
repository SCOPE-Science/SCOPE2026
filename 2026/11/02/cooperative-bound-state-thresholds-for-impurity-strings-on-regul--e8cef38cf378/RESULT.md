# Cooperative bound-state thresholds for impurity strings on regular trees

## Finding

Let \(q\ge3\), \(d\ge1\), and \(p\ge1\) be integers. On the infinite \(q\)-regular tree, consider the adjacency tight-binding Hamiltonian with \(p\) identical positive on-site impurities of strength \(\kappa>0\), placed at successive distance-\(d\) positions on one geodesic. Write
\[
E_0=2\sqrt{q-1},\qquad r=(q-1)^{-d/2},\qquad c=\frac{\sqrt{q-1}}{q-2}.
\]
For each \(j=1,\ldots,p\), there is a unique \(\theta_j\in(0,\pi)\) satisfying
\[
(p-1)\theta_j+2\operatorname{Arg}(e^{i\theta_j}-r)=j\pi,
\]
where the argument is taken in \((0,\pi)\). Set
\[
\kappa_j=\frac{1+r^2-2r\cos\theta_j}{c(1-r^2)}.
\]
Then \(0<\kappa_1<\cdots<\kappa_p\), and the **exact number** of square-summable eigenmodes at energies strictly greater than \(E_0\), counted with multiplicity, is
\[
\boxed{N_p(\kappa)=\sum_{j=1}^p\mathbf 1_{\{\kappa>\kappa_j\}}.}
\]
Equality at any threshold gives **no new above-band mode**. Every above-band eigenvalue is simple.

Define the collective lower and upper couplings
\[
\kappa_-=\frac{1-r}{c(1+r)},\qquad
\kappa_+=\frac{1+r}{c(1-r)}.
\]
The first-mode threshold is strictly decreasing in \(p\), the all-mode threshold is strictly increasing, and
\[
\boxed{\kappa_1=\kappa_-\left(1+\frac{r\pi^2}{(1-r)^2p^2}+o(p^{-2})\right),\qquad
\kappa_p=\kappa_+\left(1-\frac{r\pi^2}{(1+r)^2p^2}+o(p^{-2})\right).}
\]
Here the notation \(\kappa_1,\kappa_p\) refers to the thresholds for a string of length \(p\). In particular, \(\kappa\le\kappa_-\) creates no above-band bound state for **any finite string**, whereas \(\kappa\ge\kappa_+\) creates exactly \(p\) such states for every \(p\). For intermediate fixed coupling,
\[
\boxed{\lim_{p\to\infty}\frac{N_p(\kappa)}p
=\frac1\pi\arccos\!\left(\frac{1+r^2-\kappa c(1-r^2)}{2r}\right)
\quad(\kappa_-<\kappa<\kappa_+).}
\]
The limiting fraction equals \(0\) at and below \(\kappa_-\), and \(1\) at and above \(\kappa_+\). This is a sharp cooperative binding phenomenon: a finite *array* can bind even when an isolated impurity of the same strength cannot.

For example, on the cubic regular tree \(q=3\) with nearest-neighbor-spaced impurities \(d=1\), a single impurity binds above the band only when \(\kappa>1/\sqrt2\), but four consecutive impurities already bind one mode at \(\kappa=0.3\) (the first threshold is approximately \(0.2571005345\)). At this same coupling the long-string bound-mode fraction tends to approximately \(0.1355736535\).

## Assumptions and scope

The graph is an **infinite** countably infinite \(q\)-regular tree with unweighted adjacency operator \(A\) on \(\ell^2(V)\); each edge has hopping amplitude one. Choose a bi-infinite geodesic and distinct vertices \(v_1,\ldots,v_p\) in that order, with graph distance \(\operatorname{dist}(v_i,v_j)=d|i-j|\). Let
\[
H=A+\kappa\sum_{j=1}^p|\delta_{v_j}\rangle\langle\delta_{v_j}|.
\]
Only \(q\ge3\), integer \(d,p\ge1\), and real \(\kappa>0\) are included. The unperturbed spectrum is \([-E_0,E_0]\). The statement counts eigenvalues in \((E_0,\infty)\) and makes **no** claim about states inside the band, at its edges, or below it under different-sign impurities. It concerns a finite string followed by an asymptotic sequence as its length grows; it does not assert the spectrum of an infinitely extended defect line.

## Proof

**1. Free tree Green function.** For real \(z>E_0\), removing the edge to the parent gives a branch cavity Green value
\[
h(z)=\frac{z-\sqrt{z^2-4(q-1)}}{2(q-1)},\qquad h(z)=\frac1{z-(q-1)h(z)}.
\]
The root diagonal Green value is \(g(z)=1/[z-qh(z)]\). Successive elimination along the unique path between two vertices gives
\[
\langle\delta_u,(z-A)^{-1}\delta_v\rangle=g(z)h(z)^{\operatorname{dist}(u,v)}.
\]
Both quantities are positive for \(z>E_0\). As \(z\downarrow E_0\), \(h(z)\uparrow(q-1)^{-1/2}\) and \(g(z)\uparrow c=\sqrt{q-1}/(q-2)\). Hence the finite impurity-site Green matrix tends to \(cC_p\), where \((C_p)_{ij}=r^{|i-j|}\).

**2. Exact Birman–Schwinger count.** For \(z>E_0\), the eigenvalue equation for \(H\) reduces bijectively to eigenvalue \(1\) of the positive symmetric matrix \(\kappa G_p(z)\), the compressed free Green matrix. For every nonzero \(y\in\mathbb R^p\),
\[
\frac{d}{dz}\langle y,G_p(z)y\rangle
=-\left\|(z-A)^{-1}\sum_i y_i\delta_{v_i}\right\|_2^2<0.
\]
Thus every ordered eigenvalue of \(G_p(z)\) decreases strictly from its edge value (the corresponding eigenvalue of \(cC_p\)) to zero as \(z\to\infty\). Each edge eigenvalue strictly greater than \(1/\kappa\) causes exactly one crossing and hence one eigenvalue in \((E_0,\infty)\). Equality at the edge causes no crossing above the edge. There are no other above-band eigenvalues because the reduction is bijective.

**3. Exact thresholds and simplicity.** For \(p\ge2\), direct multiplication shows
\[
(1-r^2)C_p^{-1}=\begin{pmatrix}
1&-r&&&\\
-r&1+r^2&-r&&\\
&\ddots&\ddots&\ddots&\\
&&-r&1+r^2&-r\\
&&&-r&1
\end{pmatrix}.
\]
The corresponding three-term recurrence has eigenvalues \(t(\theta)=1+r^2-2r\cos\theta\). The two end conditions give
\[
\sin((p+1)\theta)-2r\sin(p\theta)+r^2\sin((p-1)\theta)=0.
\]
This is equivalent, for \(0<\theta<\pi\), to
\[
(p-1)\theta+2\operatorname{Arg}(e^{i\theta}-r)=j\pi.
\]
Its left side increases strictly from \(0\) to \((p+1)\pi\), since
\[
\frac{d}{d\theta}\operatorname{Arg}(e^{i\theta}-r)
=\frac{1-r\cos\theta}{1+r^2-2r\cos\theta}>0.
\]
It therefore has exactly one solution for each \(j=1,\ldots,p\), in increasing order. As \(t(\theta)\) increases strictly, the corresponding \(C_p\)-eigenvalues \((1-r^2)/t(\theta_j)\) are distinct and strictly decreasing. The case \(p=1\) gives \(C_1=(1)\) and the same formula with \(\theta_1=\arccos r\). Hence each crossing is simple, and the claimed finite threshold formula follows.

**4. End thresholds and their finite-size shifts.** The Toeplitz integral identity for the absolutely summable positive kernel \(r^{|i-j|}\) gives
\[
\frac{1-r}{1+r}\,\|x\|^2
<\langle x,C_px\rangle
<\frac{1+r}{1-r}\,\|x\|^2
\]
for every nonzero finite vector (strictness follows because its Fourier polynomial cannot be concentrated at a single angle). The maximum eigenvalue increases strictly and the minimum decreases strictly with \(p\): principal-block interlacing is strict because the tridiagonal inverse is irreducible and none of its eigenvectors has a zero terminal component. Their limits are respectively \((1+r)/(1-r)\) and \((1-r)/(1+r)\), for example by long alternating and constant trial vectors. This proves the global coupling thresholds and monotonicity.

For the first angular root, \(\operatorname{Arg}(e^{i\theta}-r)=\theta/(1-r)+O(\theta^3)\) near zero. Hence \(\theta_1=\pi/p+O(p^{-2})\). At the other end \(\pi-\theta_p=\pi/p+O(p^{-2})\). Substituting \(t(\theta)= (1-r)^2+r\theta^2+O(\theta^4)\) and its counterpart \(t(\pi-\varepsilon)=(1+r)^2-r\varepsilon^2+O(\varepsilon^4)\) into the threshold formula gives both stated \(p^{-2}\) expansions.

**5. Mode density.** The root equation implies \(\theta_j=j\pi/p+O(p^{-1})\) uniformly away from the endpoints, so the \(\theta_j\) become equidistributed on \((0,\pi)\). The exact threshold condition is
\[
\cos\theta_j>\frac{1+r^2-\kappa c(1-r^2)}{2r}.
\]
Taking the relative count gives the stated arccosine phase law. This completes the proof for every admissible \(q,d,p,\kappa\).

## Verification

Run `python verify.py` with Python 3, NumPy, and SciPy. The standalone program compares the angular-root thresholds with independently diagonalized dense kernel matrices, checks tridiagonal inverses and mode counts, compares large-size spectral fractions and critical shifts, and independently approximates the free infinite-tree resolvent by finite Dirichlet balls. The program's finite-ball tests use deliberately bounded approximation tolerances; they are not proofs of infinite-tree convergence. The analytical derivation above proves the quantified theorem.

## Relationship to prior work

Kollar and collaborators (first available preprint 2005-04-25) developed Green-function methods for Bethe lattices, including finite connectivity; these free-resolvent ingredients are not new. Glasser (2017 preprint, 2019 open-access article) gave general finite-impurity Green-function/determinant identities; the finite-rank secular equation is not new. Kac–Murdock–Szegő matrix eigenvalue asymptotics and the Toeplitz spectral-distribution theorem are classical, as surveyed by Bourget, Alvarez Loya and McMillen (2016). This result combines these antecedents to obtain a specific **all-finite-string threshold staircase, quantitative cooperative-binding interval, sharp two-sided finite-size threshold shifts, and impurity-bound-mode density** for the regular-tree geodesic geometry. The underlying generic determinant, matrix kernel and spectral limit are not asserted to be independent discoveries.

## Limitations

The result uses identical positive site defects aligned on a geodesic and a scalar nearest-neighbor adjacency Hamiltonian. It does not cover arbitrary defect subsets, signed potentials, disorder, long-range hopping, multi-component sites, or infinite-line spectral bands. The spectral density refers to the *number of discrete above-band eigenvalues per finite impurity*, not to thermodynamic integrated density of states of a translation-invariant infinite-tree defect operator. Historical priority for this precise combined physical classification remains provisional; the generic constituent tools already exist. There has been no independent scientific audit.

## References

1. M. Kollar et al., *Green functions for nearest- and next-nearest-neighbor hopping on the Bethe lattice*, arXiv:cond-mat/0504637 (first posted 2005-04-25), https://arxiv.org/abs/cond-mat/0504637 .
2. M. L. Glasser, *A Note on the Exact Green Function for a Quantum System Decorated by Two or More Impurities*, arXiv:1702.05111 (first posted 2017-02-16), *Frontiers in Physics* 7:7 (2019), https://doi.org/10.3389/fphy.2019.00007 .
3. A. Bourget, A. Alvarez Loya, T. McMillen, *Spectral Asymptotics for Kac-Murdock-Szegő Matrices*, arXiv:1610.00084 (first posted 2016-10-01), https://arxiv.org/abs/1610.00084 .
