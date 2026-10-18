# Complete degree-wise harmonic interpolation on the ten dodecahedral axes

## Finding

Let \(X=\{x_1,\ldots,x_{10}\}\subset S^2\) contain exactly one endpoint of each antipodal pair of vertices of a regular dodecahedron, normalized to the unit sphere. For every integer \(\ell\ge0\), let \(E_\ell:\mathcal H_\ell(S^2)\to\mathbb C^{10}\) evaluate complex spherical harmonics of homogeneous degree \(\ell\) on \(X\). Its ranks, in increasing degrees \(0\le\ell\le14\), are
\[
(1,3,5,7,9,6,10,10,9,10,10,10,10,10,9).
\]
Moreover \(\operatorname{rank}E_\ell=10\) for **every** \(\ell\ge15\). Thus degree \(6\) first allows arbitrary pointwise interpolation, degrees \(8\) and \(14\) lose exactly the constant-data direction, and degree \(15\) is the sharp permanent-recovery cutoff. In particular, the rank collapses from \(9\) at degree \(4\) to \(6\) at degree \(5\), despite the strictly increasing dimension of the harmonic space.

The complete nonzero and zero Gram spectra for every degree are given next. Let \(P_\ell\) be the Legendre polynomial with \(P_\ell(1)=1\), and set \(p_\ell=P_\ell(1/3)\) and
\[
q_\ell=\begin{cases}
P_\ell(\sqrt5/3),&\ell\text{ even},\\
P_\ell(\sqrt5/3)/\sqrt5,&\ell\text{ odd}.
\end{cases}
\]
With probability-normalized spherical measure, the evaluation Gram matrix is \(G_\ell=((2\ell+1)P_\ell(x_i\cdot x_j))_{i,j}\). For even \(\ell\), its eigenvalues divided by \(2\ell+1\), followed by multiplicities, are
\[
\begin{array}{c|c}
1+3q_\ell+6p_\ell&1\\
1+q_\ell-2p_\ell&5\\
1-2q_\ell+p_\ell&4
\end{array}.
\]
For odd \(\ell\), they are
\[
\begin{array}{c|c}
1+5q_\ell+2p_\ell&3\\
1-5q_\ell+2p_\ell&3\\
1-3p_\ell&4
\end{array}.
\]
All the displayed values are rational. A zero eigenvalue specifies the exact orthogonal obstruction to interpolating arbitrary ten-vectors. For even \(\ell\in\{4,8,14\}\), this is precisely \(\sum_{j=1}^{10}y_j=0\). For every attainable \(y\), the unique harmonic interpolant of least \(L^2\) norm is
\[
f_y(x)=\sum_{j=1}^{10}(G_\ell^\dagger y)_j(2\ell+1)P_\ell(x\cdot x_j),
\qquad \|f_y\|_2^2=y^*G_\ell^\dagger y.
\]

## Assumptions and scope

Work on the ordinary round \(S^2\) with rotation-invariant **probability** surface measure. Define \(\varphi=(1+\sqrt5)/2\). The twenty vertices before normalization are the eight triples \((\pm1,\pm1,\pm1)\) and the twelve triples obtained from \((0,\pm\varphi^{-1},\pm\varphi)\) by cyclic coordinate permutation, with both signs chosen independently. Every vertex has squared norm \(3\). Choose one vector from each pair \(\{v,-v\}\), divide by \(\sqrt3\), and enumerate them as \(x_j\). Any other choices merely conjugate odd-degree Gram matrices by a diagonal sign matrix; all rank/spectral assertions are orientation-independent. No bandlimit sum of degrees is involved: the interpolation space is one **fixed** homogeneous harmonic degree, of dimension \(2\ell+1\).

## Proof

**1. Two exact signed adjacency algebras.** For unequal indices, the dot product \(x_i\cdot x_j\) belongs to \(\{\pm1/3,\pm\sqrt5/3\}\). Let \(D\) be the unsigned adjacency matrix marking \(|x_i\cdot x_j|=\sqrt5/3\). Let \(U\) mark the same edges with sign \(\operatorname{sgn}(x_i\cdot x_j)\); let \(W\) analogously sign the edges with absolute dot product \(1/3\). Their diagonals are zero. Direct substitution of the displayed twenty vectors, using \(\varphi^2=\varphi+1\), yields the exact ten-by-ten identities
\[
D^2=2I-D+J,\qquad U^2=3I+W,\qquad UW=2U,
\]
where \(J\) is the all-ones matrix. Every row of \(D\) has degree three, every row of \(W\) has six nonzero entries, and all matrices are symmetric. The first identity makes \(D\) a Petersen adjacency matrix with eigenvalues \(3,1,-2\) and multiplicities \(1,5,4\). The next two identities imply \(U^3=5U\). As \(\operatorname{tr}U=0\) and \(\operatorname{tr}U^2=30\), its eigenvalues are \(\sqrt5,-\sqrt5,0\) with multiplicities \(3,3,4\). The matrix \(W=U^2-3I\) has eigenvalue \(2\) in the first two sectors and \(-3\) in the last.

**2. Reproducing-kernel diagonalization.** The spherical addition formula in the stipulated measure gives \(Z_\ell(x,y)=(2\ell+1)P_\ell(x\cdot y)\). Since \(P_\ell(-t)=(-1)^\ell P_\ell(t)\), the normalized Gram matrix becomes
\[
\frac{G_\ell}{2\ell+1}=\begin{cases}
I+q_\ell D+p_\ell(J-I-D),&\ell\text{ even},\\
I+\sqrt5q_\ell U+p_\ell W,&\ell\text{ odd}.
\end{cases}
\]
Applying the preceding eigenspace decompositions produces exactly the six formulas in the Finding. The rank of \(E_\ell\) equals the rank of \(G_\ell=E_\ell E_\ell^*\).

**3. Exact rational recurrence and small degrees.** Both scalar sequences are rational. They start \(p_0=q_0=1\), \(p_1=q_1=1/3\) and satisfy, for \(n\ge1\),
\[
(n+1)p_{n+1}=\frac{2n+1}{3}p_n-np_{n-1},
\]
\[
(n+1)q_{n+1}=\frac{(2n+1)c_n}{3}q_n-nq_{n-1},\qquad
c_n=\begin{cases}5,&n\text{ odd},\\1,&n\text{ even}.\end{cases}
\]
The complete fractions for degrees \(0\) through \(14\) are computed and asserted by the accompanying self-contained `verify.py`; they give precisely the displayed rank sequence. The same exact recurrence verifies that **every** eigenvalue is strictly positive in degrees \(15\) through \(61\). These are exact rational comparisons, not floating-point rank thresholds.

**4. Uniform strict positivity for all remaining degrees.** The classical Bernstein inequality for Legendre polynomials states, for \(\ell\ge0\) and \(-1<t<1\),
\[
|P_\ell(t)|\le \sqrt{\frac{2}{\pi(\ell+1/2)\sqrt{1-t^2}}}.
\]
Each row of \(G_\ell/(2\ell+1)\) has precisely six off-diagonal values of absolute magnitude \(|P_\ell(1/3)|\) and three of absolute magnitude \(|P_\ell(\sqrt5/3)|\). Their sum is at most
\[
\frac{6\sqrt{3/(\pi\sqrt2)}+3\sqrt{3/\pi}}{\sqrt{\ell+1/2}}.
\]
For \(\ell\ge62\), this is strictly below one. In fact, use \(\pi>157/50\) and \(\sqrt2>707/500\), and bound the first two square-root coefficients above by \(103/125\) and \(49/50\), respectively. Their weighted sum is \(1971/250\), whose square is less than \(125/2\). Hence strict diagonal dominance and Hermitian positivity give \(\operatorname{rank}G_\ell=10\) for every \(\ell\ge62\). Together with Step 3 this proves the all-degree classification and sharp permanent cutoff.

**5. Interpolation and exact missing-data sectors.** The orthogonal range of \(E_\ell\) equals that of the Gram matrix. Its pseudoinverse spectral decomposition therefore both tests data feasibility and produces the unique minimum-norm solution in the Finding. In even degrees the constant sector is \(\mathbb C\mathbf1\); this proves the stated mean-zero constraints at degrees \(4,8,14\). For odd degrees, the exact signed sectors are the \(\sqrt5,-\sqrt5,0\) eigenspaces of \(U\); for example the degree-five image is the six-dimensional image of \(U\).

## Verification

The supplied `verify.py` is Python standard-library-only. Run `python verify.py`. It reconstructs the twenty vectors in \(\mathbb Q(\sqrt5)^3\), chooses the ten antipodal lines, directly checks all dot products and the three adjacency identities, evaluates the Legendre polynomials independently at every pair of points for every degree through \(61\), verifies the six rational sector formulas and rank pattern, and checks the strict rational inequalities used in the uniform large-degree bound. It reported **6386 exact component comparisons** on execution. The check is finite only where a finite check is mathematically needed; Step 4 covers all larger degrees.

## Relationship to prior work

Bannai–Okuda–Tagami's 2013 preprint (published 2015) establishes the harmonic-index design framework and discusses the known vanishing of degree-eight and degree-fourteen averages on the **six** icosahedral vertex lines, via the icosahedral Molien series. Dodecahedral symmetry also explains the analogous invariant mean-zero obstructions here. Such vanishing-moment information concerns only one possible Gram sector and does not supply the other sectors, the degree-five rank collapse, all-degree pointwise range, or the exact permanent interpolation threshold on the ten dodecahedral vertex lines.

Cohan (1958) and Zheng–Doerschuk (1994, 2000) construct symmetry-adapted harmonic bases for icosahedral rotations. Their accessible descriptions concern harmonic representations, not a complete evaluation Gram spectrum for this ten-line configuration. Womersley (2001) develops general spherical polynomial interpolation and reproducing-kernel matrices for all degrees up to a bandlimit, not the individual-degree rank question here. Known geometric facts about the Petersen graph furnish the unsigned adjacency algebra but not the signed odd-degree spectral decomposition and Legendre positivity certificate. The precise statement/implication comparisons and access limits are in `AUDIT.json`.

## Limitations

The finding classifies ten antipodal **dodecahedral vertex** lines only; it does not classify arbitrary perturbed nodes, other polyhedra, stability under measurement noise, or sampling with multiple degrees. The finite arithmetic and geometric identities are fully reproducible. A 1958 full text and a 1994 technical-report download were not accessible through the available scholarly routes; implicit earlier representation-theoretic equivalents remain a priority risk. No independent mathematical audit or publication-priority certification has been performed.

## References

1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, initially public 2013-08-23; Journal of Approximation Theory **195** (2015), 1–18, DOI:10.1016/j.jat.2014.06.010.
2. N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Mathematical Proceedings of the Cambridge Philosophical Society **54** (1958), 28–38, DOI:10.1017/S0305004100033156.
3. Y. Zheng, P. C. Doerschuk, *Explicit orthonormal bases for functions exhibiting the rotational symmetries of a Platonic solid*, Purdue technical report (1994), record: https://docs.lib.purdue.edu/ecetr/203/.
4. Y. Zheng, P. C. Doerschuk, *Explicit computation of orthonormal symmetrized harmonics with application to the identity representation of the icosahedral group*, SIAM Journal on Mathematical Analysis **32** (2000), 538–554, DOI:10.1137/S0036141098341770.
5. R. S. Womersley, *How good can polynomial interpolation on the sphere be?*, preprint (2001), Section 2, https://web.maths.unsw.edu.au/~rsw/Papers/hgood.pdf.
6. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society Colloquium Publications, vol. 23, on Legendre polynomial bounds and recurrences.
