# Sharp isolation gap for Kuhn-packet ball radii on the body-centered cubic lattice

## Finding

Let \(L=\mathbb Z^3\cup(\mathbb Z^3+(1/2,1/2,1/2))\) be the unscaled body-centered cubic lattice. For any ordered linearly independent triple \(B=(b_1,b_2,b_3)\) of vectors in \(L\), write
\[
T_\sigma(B)=\operatorname{conv}\{0,b_{\sigma(1)},b_{\sigma(1)}+b_{\sigma(2)},b_1+b_2+b_3\},\qquad \sigma\in S_3,
\]
and let \(R(T)=\min_{c\in\mathbb R^3}\max_{x\in T}\|x-c\|\), the minimum radius of a ball containing the *entire* simplex. Define the six-simplex certificate radius
\[
\mathcal R(B)=\max_{\sigma\in S_3}R(T_\sigma(B)).
\]
Then every independent lattice triple satisfies the *sharp isolated-minimum law*
\[
\boxed{\mathcal R(B)=\sqrt5/4\quad\hbox{or}\quad \mathcal R(B)\ge1/\sqrt2.}
\]
Equality at \(\sqrt5/4\) holds if and only if the three vectors are distinct elements of the same four-vector set
\[
H_\eta=\{(\epsilon_1,\epsilon_2,\epsilon_3)/2:\epsilon_i\in\{-1,1\},\ \epsilon_1\epsilon_2\epsilon_3=\eta\},\quad\eta\in\{-1,1\}.
\]
There are exactly eight unordered and 48 ordered minimizer triples. Every minimizing triple is automatically a basis of \(L\), although the theorem allows independent triples which only span sublattices. The second threshold \(1/\sqrt2\) is attained, for instance by \(B=(e_1,e_2,(-1/2,-1/2,1/2))\), so the multiplicative isolation factor \(\sqrt{8/5}\) cannot be improved.

## Assumptions and scope

Vectors are measured in the ordinary Euclidean norm, without rescaling the BCC lattice, and \(B\) ranges over *all* ordered linearly independent lattice triples, not merely a finite enumeration or reduced bases. The radius is a minimum **enclosing-ball** radius, not the circumsphere radius when a tetrahedron is obtuse. The six prefix simplices are formed with one common frame and all permutations; their minimum enclosing balls may have different centers. The finding concerns this explicit finite-simplex certificate, and does not assert an analogous gap for all triangulations or for the intrinsic covering radius of every nearby lattice.

The June 2026 Kuhn covering construction provides the motivation: if \(B\) is a basis of \(L\) and a Euclidean ball of radius \(r\) contains a translate of each of the six \(T_\sigma(B)\), the Kuhn-triangulation covering principle implies that translates of the ball by \(L\) cover space. The theorem is a quantitative rigidity statement for that natural certificate.

## Proof

**1. Short subset sums are necessary.** Set \(r=\mathcal R(B)\). For each nonempty subset \(I\subseteq\{1,2,3\}\), its sum \(s_I=\sum_{i\in I}b_i\) appears as a prefix vertex of one \(T_\sigma(B)\). The same simplex contains the origin. Hence \(\|s_I\|\le2r\). If \(r<1/\sqrt2\), every such sum satisfies \(\|s_I\|^2<2\).

**2. Classify the short lattice vectors.** A nonzero vector of \(L\) with squared norm strictly below \(2\) is either one of the six signed coordinate units \(\pm e_j\), or one of the eight half-diagonals \((\pm1/2,\pm1/2,\pm1/2)\). This follows coordinatewise: nonzero integral vectors of squared norm below two are coordinate units, while the smallest possible squared norm of a half-integral vector is \(3/4\) and every other half-integral vector has squared norm at least \(11/4\).

No two independent coordinate units can occur: they are on distinct coordinate axes and their sum has squared norm two, contradicting Step 1. If exactly one unit \(se_j\) occurs along with two half-diagonals \(v,w\), then \(\|se_j+v\|^2<2\) and \(\|se_j+w\|^2<2\) force \(v_j=w_j=-s/2\). The further requirement \(\|v+w\|^2<2\) forces the other two signs of \(v\) and \(w\) to be opposite in both coordinates; otherwise the squared norm is at least two. Consequently \(v+w=-se_j\), contradicting independence. Thus all three frame vectors must be half-diagonals.

For distinct half-diagonals \(v,w\), the condition \(\|v+w\|^2<2\), together with their linear independence, means they differ in precisely two signs: one-sign differences give squared sum two, and three-sign differences make them antipodal. A triple of sign vectors with all pairwise Hamming distances two belongs to one common parity class \(H_\eta\). Thus every independent frame with \(r<1/\sqrt2\) consists of three distinct members of a single \(H_\eta\).

**3. Each surviving frame has exactly the smaller radius.** For any such three vectors \(u,v,w\), their Gram matrix has diagonal \(3/4\) and off-diagonal \(-1/4\); it is positive definite with eigenvalues \(1,1,1/4\). Each prefix tetrahedron has four vertices \(p_0=0\), \(p_1=u\), \(p_2=u+v\), \(p_3=u+v+w\), up to permutation. The squared lengths of its six edges are four copies of \(3/4\) and two copies of \(1\). Its centroid \(m=(p_0+p_1+p_2+p_3)/4\) has squared distance \(5/16\) from each vertex. For every prospective ball center \(c\),
\[
\frac14\sum_{j=0}^{3}\|p_j-c\|^2=\frac5{16}+\|m-c\|^2.
\]
Consequently no enclosing radius can be below \(\sqrt5/4\), while the ball centered at \(m\) attains it. This applies to all six permutations. Every \(H_\eta\) has four vectors, giving \(2\binom43=8\) unordered choices and 48 ordered choices; each choice has determinant magnitude \(1/2\), equal to the covolume of \(L\), so is a lattice basis.

**4. Exclusion gap and sharpness.** Step 2 proves the contrapositive: every other independent frame has \(\mathcal R(B)\ge1/\sqrt2\). For \(B=(e_1,e_2,v)\), \(v=(-1/2,-1/2,1/2)\), a prefix simplex contains both \(0\) and \(e_1+e_2\), whose separation is \(\sqrt2\), forcing the radius at least \(1/\sqrt2\). For orderings ending in \(v\), the respective tetrahedra fit in a radius-\(1/\sqrt2\) ball centered at \((1/2,1/2,0)\); for orderings beginning in \(v\), use center \((0,0,1/2)\). For the two orderings with \(v\) in the middle, use centers \((1/2,0,1/4)\) and \((0,1/2,1/4)\), respectively; their squared radii are \(5/16\). Therefore \(\mathcal R(B)=1/\sqrt2\). This proves optimality of both thresholds and completes the proof.

For context, the usual Euclidean covering radius of this scaled BCC lattice also equals \(\sqrt5/4\). The lower bound follows from the point \((1/2,1/4,0)\), whose distance to both cosets of \(L\) is at least \(\sqrt5/4\); the upper bound follows from a minimizing frame and the classical Kuhn covering lemma quoted above. This last identity is background, not claimed as new.

## Verification

The standalone `verify_bcc.py` uses `fractions.Fraction` throughout. It solves the exact affine Gram systems for candidate one-, two-, three-, and four-point enclosing spheres, tests containment, and computes all six permutation radii for every independent triple chosen from the 14 nonzero BCC vectors of squared length less than two. It reports 232 independent unordered triples, eight minimizers of squared radius \(5/16\), and 48 other short-vector frames reaching squared radius \(1/2\); it also verifies an explicit sharp second-threshold frame. All those finite tests passed. The mathematical argument in Steps 1–4, not this finite enumeration, proves the result for *every* lattice triple.

Run from the extracted package directory using `python verify_bcc.py` (Python standard library only). The code uses no random input or external files.

## Relationship to prior work

Lian and Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings* (arXiv:2606.14584, first posted June 12, 2026), Theorem 1.1 and Section 2, develop the six Kuhn simplices and their lattice-covering criterion. Their actual theorem addresses **existence of coverings and structure of minimal covering bodies**, not a sharp discrete gap among Euclidean minimum-enclosing-ball radii of all BCC lattice frames.

Choudhary, Kachanovich, and Wintraecken, *Coxeter Triangulations Have Good Quality* (2020), Section 1.2 and subsequent quality formulas, identify the BCC lattice with the three-dimensional Coxeter triangulation and its familiar Sommerville tetrahedron. Its well-known optimum tetrahedral geometry is not presented here as a discovery. The gap and all-frame exclusion are additional statements: a good Coxeter frame by itself does not rule out other frames with certificate radii strictly between the two stated thresholds.

Labelle, *Tetrahedral Mesh Generation with Good Dihedral Angles Using Point Lattices* (2007), Chapter 3, discusses the BCC Delaunay tetrahedron and mesh quality. This earlier work supports the geometric baseline, not the global sharp second-threshold classification. No equivalence with a known stronger all-frame result was identified in the materials inspected; this is a bounded historical-priority assessment, not a proof of absolute novelty.

## Limitations

The isolated gap applies only to the fixed, unscaled BCC lattice in three dimensions and to six-prefix-simplex ball certificates, not arbitrary coverings or other lattices. It does not claim a classification of **all** frames exactly attaining the second threshold, only one explicit attainer. It does not assert that the intrinsic BCC covering radius itself is isolated under lattice deformations. The exact-rational check is finite corroboration; the proof handles the infinite lattice. Independent validation and a comprehensive historical-priority audit have not been performed.

## References

1. Y. Lian and F. Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584v1 (first public June 12, 2026), Sections 1–2, especially Theorem 1.1 and Lemma 2.6. https://arxiv.org/abs/2606.14584
2. A. Choudhary, S. Kachanovich and M. Wintraecken, *Coxeter Triangulations Have Good Quality*, Mathematics in Computer Science 14 (2020), 141–176, doi:10.1007/s11786-020-00461-5. https://link.springer.com/article/10.1007/s11786-020-00461-5
3. F. Labelle, *Tetrahedral Mesh Generation with Good Dihedral Angles Using Point Lattices*, dissertation, University of California, Berkeley (2007), Chapter 3. https://www2.eecs.berkeley.edu/Pubs/TechRpts/2007/EECS-2007-104.pdf
