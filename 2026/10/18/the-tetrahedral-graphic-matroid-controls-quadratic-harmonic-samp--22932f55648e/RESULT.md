# The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron

## Finding
Let \(X\subset S^2\) be the twelve vertices of the cuboctahedron, and let \(\mathcal H_{\le 2}\) be the nine-dimensional space spanned by spherical harmonics of degrees zero, one, and two. For each erased set \(T\subseteq X\), construct a simple graph \(G_T\) on vertices \(\{1,2,3,4\}\) as follows: label the six antipodal pairs of \(X\) by the six edges of the complete graph on four vertices according to the explicit table below, and include an edge in \(G_T\) exactly when at least one of its corresponding two points is erased. Write \(c(G_T)\) for its number of connected components, counting isolated vertices. Then the evaluation map on the surviving nodes has the exact rank

\[
\boxed{\operatorname{rank}\!\left(\mathcal H_{\le2}\longrightarrow\mathbb C^{X\setminus T}\right)
=13-|T|-c(G_T).}
\]

This holds for **every** one of the \(2^{12}=4096\) erasure patterns, including the empty and total erasures. Thus the full sampling-rank matroid has a Gale-dual representation that is a twofold parallel extension of the graphic matroid of the tetrahedron (the two parallel vectors for each edge have opposite signs).

In particular, of the \(\binom{12}{3}=220\) three-node erasures, exactly \(128\) preserve unique reconstruction of all degree-at-most-two harmonics, and exactly \(92\) destroy it. Three deletions are recoverable precisely when they meet three different antipodal pairs and the associated three edges do not form a triangle. Of the \(66\) two-node erasures, exactly \(60\) are recoverable; the six unrecoverable pairs are the antipodal pairs.

## Assumptions and scope
Coordinates in the table are *unnormalized*: the actual spherical point is \(v/\sqrt2\), and the antipodal pair is \(\{v/\sqrt2,-v/\sqrt2\}\). Each edge is included in \(G_T\) once, regardless of whether one or both members of its pair are erased.

| Edge | Representative \(v\) |
| --- | --- |
| \(12\) | \((-1,1,0)\) |
| \(13\) | \((1,0,1)\) |
| \(14\) | \((0,-1,-1)\) |
| \(23\) | \((0,1,-1)\) |
| \(24\) | \((-1,0,1)\) |
| \(34\) | \((1,1,0)\) |

The evaluation rank is over \(\mathbb C\) (and is equal to the real rank in the displayed real basis). No noise robustness or singular-value bound is asserted: the theorem is an exact identifiability statement for noiseless samples at these twelve fixed nodes.

## Proof
**1. Harmonic evaluation matrix.** Put \(Y=\sqrt2X\). At \(Y\), evaluate the nine polynomials
\[
1,\ x,\ y,\ z,\ x^2-y^2,\ x^2+y^2-2z^2,\ xy,\ xz,\ yz.
\]
Their restrictions to the sphere differ from a real basis of \(\mathcal H_{\le2}\) only by invertible column scalings. Let \(E\) be the resulting \(12\)-by-\(9\) matrix. It has column rank \(9\): a polynomial in their span vanishing on all twelve points has zero linear part by comparison of antipodal values; comparison among the four sign choices in each coordinate plane then eliminates \(xy,xz,yz\); the three remaining plane-sum equations eliminate the constant and both trace-free diagonal quadratics.

**2. An explicit Gale kernel.** Define four potential vectors in \(\mathbb Z^3\) by
\[
 t_1=(0,1,1),\quad t_2=(-1,0,0),\quad
 t_3=(0,0,1),\quad t_4=(0,0,0).
\]
The three vectors \(t_1,t_2,t_3\) are linearly independent. Define a \(12\)-by-\(3\) matrix \(B\) with row \(t_i-t_j\) at the positive representative \(v_{ij}\) from the table, and its negative at the antipodal point. Direct substitution gives \(B^{\mathsf T}E=0\). One can check this without expanding every polynomial: opposite points cancel all even-degree columns, while the remaining linear columns vanish because
\[
\sum_{1\le i<j\le4}(t_i-t_j)v_{ij}^{\mathsf T}=0_{3\times3}.
\]
The matrix \(B\) has rank \(3\), so, because \(E\) has rank \(9\), its columns form a basis of the entire left kernel of \(E\).

**3. Graph incidence and erasure duality.** For an erased set \(T\), the submatrix \(B_T\) consists of the rows indexed by \(T\). Up to nonzero signs and parallel duplicate rows, these are \(t_i-t_j\) for the edge set of \(G_T\). The independent potential differences identify the rank of this edge-vector matrix with that of the usual incidence matrix of \(G_T\), namely \(4-c(G_T)\).

Every linear relation among the retained rows of \(E\) is a vector in the left nullspace of \(E\) whose coordinates vanish on \(T\). Since the full left nullspace has the representation \(B\), the space of those relations has dimension \(3-\operatorname{rank}B_T\). Consequently,
\[
\begin{aligned}
\operatorname{rank}E_{X\setminus T}
&=(12-|T|)-(3-\operatorname{rank}B_T)\\
&=9-|T|+4-c(G_T)\\
&=13-|T|-c(G_T),
\end{aligned}
\]
as claimed. The two- and three-erasure descriptions follow because any pair of distinct tetrahedron edges is independent, while a triple is dependent exactly when it forms a triangle. Counting the three-deletion failures gives \(6\cdot10+4\cdot2^3=92\), hence \(128\) successes.

**4. Full exact rank census.** More generally, let \(u\) mark the number of erased *nodes* and let \(z\) mark the rank of the erased-edge incidence matrix. Each active edge has node-deletion weight \(w=2u+u^2\). Enumerating the \(64\) edge subsets of the tetrahedron gives the exact finite polynomial
\[
\begin{aligned}
F(w,z)={}&1+6wz+15w^2z^2+4w^3z^2\\
&+16w^3z^3+15w^4z^3+6w^5z^3+w^6z^3.
\end{aligned}
\]
After substituting \(w=2u+u^2\), the coefficient of \(u^t z^r\) is the number of \(t\)-node erasures with edge-incidence rank \(r\); the retained sampling rank is \(9-t+r\). This proves the following **complete** distribution, not merely a set of sampled cases.

| Erased nodes | Available-sample rank and count |
| ---: | --- |
| 0 | rank 9: 1 |
| 1 | rank 9: 12 |
| 2 | rank 8: 6; rank 9: 60 |
| 3 | rank 8: 92; rank 9: 128 |
| 4 | rank 7: 63; rank 8: 432 |
| 5 | rank 6: 24; rank 7: 768 |
| 6 | rank 5: 4; rank 6: 920 |
| 7 | rank 5: 792 |
| 8 | rank 4: 495 |
| 9 | rank 3: 220 |
| 10 | rank 2: 66 |
| 11 | rank 1: 12 |
| 12 | rank 0: 1 |

## Verification
The accompanying standalone standard-library Python file `verify_cuboctahedral_erasure.py` constructs the rational harmonic matrix and the integer Gale vectors from the table. It verifies the two matrix ranks, checks all \(27\) identities in \(B^{\mathsf T}E=0\), and independently computes exact rational Gaussian-elimination ranks for **all 4096** subsets of the twelve nodes. Every rank matches the graph-connectivity prediction, and all thirteen rows of the count table are reproduced. Run `python3 verify_cuboctahedral_erasure.py` in the directory containing the script. The finite enumeration is exhaustive for the specified twelve-node problem, and the algebraic graph-incidence argument proves the formula independently.

## Relationship to prior work
Womersley and Sloan develop the general framework of degree-bounded spherical-polynomial interpolation, fundamental systems, and operator norms. Keiner, Kunis, and Potts study rank and conditioning of spherical Fourier matrices under geometric density and separation hypotheses. Rupright studies the recovery of spherical harmonic amplitudes from gridded observations, while Ahrens and Beylkin investigate symmetry-adapted spherical quadratures. These establish motivation and methods but do not state this fixed-node tetrahedral graphic-matroid rule or the all-erasure census. Studies of harmonics on equiangular cubed-sphere grids use different node sets and degree truncations; a cuboctahedral equivalent under another encoding remains a prior-literature risk. The present statement concerns exact ranks, not the convergence or condition numbers addressed in the cited work.

## Limitations
The theorem applies only to the regular cuboctahedron (the twelve normalized type-\(A_3\) roots) and the entire harmonic band of degrees zero through two. It does not assert stability constants, optimality among spherical sample grids, or extensions to higher harmonic degrees. Searches cannot prove the absence of an unrecognized equivalent theorem, and the literature comparison is subject to independent review.

## References
1. R. S. Womersley and I. H. Sloan, *How Good Can Polynomial Interpolation on the Sphere Be?*, manuscript dated April 21, 2001, publicly accessible at https://web.maths.unsw.edu.au/~rsw/Papers/hgood.pdf .
2. J. Keiner, S. Kunis and D. Potts, *Efficient Reconstruction of Functions on the Sphere from Scattered Data*, Technische Universität Chemnitz preprint 22 (2006), https://www.tu-chemnitz.de/mathematik/preprint/2006/PREPRINT_22.pdf .
3. M. E. Rupright, *Spherical Harmonic Amplitudes From Grid Data*, arXiv:gr-qc/0606127, initial public submission June 29, 2006, https://arxiv.org/abs/gr-qc/0606127 .
4. C. Ahrens and G. Beylkin, *Rotationally Invariant Quadratures for the Sphere*, Proceedings of the Royal Society A 465 (2009), 3103–3125, https://amath.colorado.edu/faculty/beylkin/papers/AHR-BEY-2009net.pdf .
