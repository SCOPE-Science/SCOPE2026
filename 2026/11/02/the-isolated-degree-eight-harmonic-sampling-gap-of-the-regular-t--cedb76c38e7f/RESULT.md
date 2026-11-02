# The isolated degree-eight harmonic sampling gap of the regular truncated octahedron

## Finding
Let \(V\subset S^2\) be the 24 normalized signed coordinate permutations of \((0,1,2)/\sqrt5\), the vertex set of the regular truncated octahedron. Let \(\mathcal H_k\) denote the real spherical harmonics of *exactly* degree \(k\), and let \(E_k:\mathcal H_k\to\mathbb R^V\) denote evaluation. Then
\[
\operatorname{rank}E_k=
\begin{cases}
1,3,5,6,9,9,10,12,11&\text{respectively for }k=0,1,\ldots,8,\\
12&\text{for every }k\ge9.
\end{cases}
\]
All ranks are relative to the full 24-point evaluation; antipodal parity bounds each individual exact-degree rank by twelve. Thus the first full parity-compatible rank occurs at degree seven, full rank is lost again at degree eight, and **the exact permanent interpolation threshold is degree nine**.

At degree eight, the one-dimensional left kernel after antipodal quotient is spanned by
\[
w(x)=\operatorname{sgn}\big[(x_1^2-x_2^2)(x_1^2-x_3^2)(x_2^2-x_3^2)\big]\in\{+1,-1\}.
\]
This weight is antipodally even, has twelve positive and twelve negative entries on the full vertex set, and satisfies
\[\sum_{x\in V}w(x)Y(x)=0\quad\text{for every }Y\in\mathcal H_8.\]
Moreover, the **unweighted** sum is not a degree-eight annihilator. Accordingly, two natural twelve-point alternating-permutation classes have equal exact eighth-harmonic moment sums without either class being a harmonic-index-eight design by itself.

## Assumptions and scope
Coordinates are Euclidean, vectors are normalized to the unit sphere, and all harmonic spaces are over the reals. Every integer \(k\ge0\) is covered, with no truncation to finitely many degrees. In the stated rank the column-space dimension of evaluation is considered, not the dimension of the full harmonic polynomial space. The sign weight is well defined because each point has three distinct squared coordinates. For an antipodal half \(X\) choose the twelve representatives \(x\) satisfying lexicographic \(x>-x\); a different choice conjugates its odd-degree Gram by a diagonal sign matrix and does not change rank.

## Proof
**1. Parity and Gram matrix.** The real spherical addition theorem gives an exact positive scalar multiple of the evaluation Gram matrix for the full vertex set, with entries \(P_k(x\cdot y)\), where \(P_k\) is the ordinary Legendre polynomial normalized by \(P_k(1)=1\). Because \(Y(-x)=(-1)^kY(x)\), evaluating at the twelve representatives \(X\) has exactly the same rank as evaluating at all 24 vertices. Thus it suffices to examine the symmetric rational matrix
\[
G_k=\big(P_k(\langle x,y\rangle)\big)_{x,y\in X}\in\mathbb Q^{12\times12}.
\]
The off-diagonal inner products are among \(\{j/5:-4\le j\le4\}\), so \(|\langle x,y\rangle|\le4/5\) whenever \(x\ne y\) in \(X\).

**2. Exact finite range.** The normalized recurrence
\[P_0(t)=1,\qquad P_1(t)=t,\qquad (k+1)P_{k+1}(t)=(2k+1)tP_k(t)-kP_{k-1}(t)\]
computes every matrix entry exactly over \(\mathbb Q\). For \(0\le k\le8\), rational Gaussian elimination gives respectively
\[1,\ 3,\ 5,\ 6,\ 9,\ 9,\ 10,\ 12,\ 11.\]
In degree eight, direct multiplication verifies \(G_8w=0\), where \(w\) is the displayed alternating sign character, and rank eleven establishes uniqueness of its line. The all-ones vector is not in the kernel: direct calculation gives
\[G_8\mathbf 1=\frac{72171}{250000}\mathbf 1\ne0.\]
For each integer \(9\le k\le134\), the standalone checker evaluates the recurrence over the prime field \(\mathbb F_{1000003}\) and obtains rank twelve. The prime is larger than all recurrence denominators \(1,2,\ldots,135\) and is coprime to five, so every rational Legendre matrix entry has a well-defined reduction in this field. **A nonzero determinant modulo the prime implies the original rational determinant is nonzero.** This is an exhaustive finite exact certificate over the complete indicated range, not a floating-point rank test.

**3. Every remaining degree.** The classical Bernstein–Szegő inequality for the Legendre polynomials states, for every integer \(k\ge0\) and \(-1<t<1\),
\[
(1-t^2)^{1/4}|P_k(t)|\le\sqrt{\frac{2}{\pi(k+1/2)}}.
\]
For any distinct representatives \(x,y\in X\), one has \(1-\langle x,y\rangle^2\ge9/25\). Consequently, for every \(k\ge135\),
\[
\sum_{y\ne x}|P_k(\langle x,y\rangle)|
\le11\sqrt{\frac{2}{\pi(k+1/2)(3/5)}}
<11\sqrt{\frac{2}{3(135+1/2)(3/5)}}<1.
\]
Here the first strict inequality uses \(\pi>3\), and the last follows by squaring (\(242<243.9\)). Since \(G_k\) has diagonal one, strict diagonal dominance and symmetry imply it is positive definite for all such degrees. Together with the complete modular range, this proves the infinite-rank classification.

**4. Complete equality claim.** The sign weight is constant on antipodal pairs and alternates under any odd permutation of the coordinate positions. Its twelve positive and twelve negative occurrences are distinct. The unique one-dimensional Gram kernel in degree eight forces every annihilating functional on the parity quotient to be proportional to this sign vector. All other degrees \(k\ge9\) have no nonzero parity-compatible annihilators. This finishes the interpolation and alternating moment statements.

## Verification
The bundled `CHECK.py` uses only the Python standard library. Running `python3 CHECK.py` prints `TRUNCATED_OCTAHEDRON_RANK_CERTIFICATE_OK 19440 exact entries checked; finite degrees 0..134`. For low degrees it uses exact rational elimination. For degrees nine through 134 it uses Gaussian elimination modulo the stated prime, after computing the normalized recurrence in that field. It additionally verifies the degree-eight null-vector relation, its nontriviality and the explicit all-ones eigenvalue. The infinitely many degrees at and above 135 are handled by the analytic Bernstein–Szegő bound in the preceding proof, **not** by finite computation.

## Relationship to prior work
Classical octahedral invariants, root-orbit cubature, and harmonic-index spherical design theory motivate a natural question: which exact harmonic degrees can distinguish arbitrary data on an Archimedean orbit? Nozaki–Sawa (2011) treat group-invariant cubature constraints for reflection-group orbits, and Bannai–Okuda–Tagami (2013) formulate general harmonic-index design and reproduction-kernel methods. Neither of their inspected relevant sections provides this specific 24-vertex, all-degree interpolation-rank sequence. The eighth-degree obstruction here is **not invariant** under all coordinate permutations; its alternating character therefore does not follow from invariant moment conditions alone. The geometric identification with the regular truncated octahedron is standard. This establishes a comparison with these sources, not a proof that no other historical treatment exists.

## Limitations
The rank theorem is for one fixed regular truncated octahedron and the exact-degree spherical harmonics, not for perturbations of the vertices, arbitrary unions of degrees, or general Archimedean solids. Rank does not provide sharp condition numbers. The finite certificate depends on re-running the accompanying standard-library program; its modular nonvanishing proof and analytic tail bound are both essential. No independent audit is asserted. Older polyhedral representation-theory or numerical cubature literature could contain an equivalent rank calculation not located in the bounded source review.

## References
1. H. Nozaki and M. Sawa, *Note on cubature formulae and designs obtained from group orbits*, arXiv:1102.4891 (public preprint 2011-02-24), especially Sections 2 and 4.2.
2. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (public preprint 2013-08-23), especially the harmonic reproducing-kernel framework.
3. G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications 23, Section 7.3 (classical Bernstein inequality).
4. NIST Digital Library of Mathematical Functions, §14.30, spherical harmonic addition formula; §14, Legendre functions.
5. E. W. Weisstein, *Truncated Octahedron*, MathWorld, geometric coordinate conventions.
