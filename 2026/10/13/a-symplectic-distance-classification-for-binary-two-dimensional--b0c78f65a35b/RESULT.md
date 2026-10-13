# A symplectic distance classification for binary two-dimensional LCD neighbors

## Finding

For every integer \(n\ge4\), write \(\Gamma_n\) for the ordinary neighbor graph of all two-dimensional binary Euclidean LCD codes in \(\mathbb F_2^n\). Distinct codes are adjacent precisely when they intersect in dimension one. Define
\[
 p(a)=\sum_{i=1}^n a_i\pmod 2,\qquad
 \Omega(a,b)=a\cdot b+p(a)p(b),\qquad \epsilon=n\bmod2.
\]
For distinct vertices \(U,W\), their graph distance is
\[
 d_{\Gamma_n}(U,W)=
 \begin{cases}
 1,&\dim(U\cap W)=1,\\
 3,&\Omega(U,W)=0,\\
 2,&\text{otherwise},
 \end{cases}
\]
where \(\Omega(U,W)=0\) means \(\Omega(u,w)=0\) for every \(u\in U,w\in W\). In the second case the planes are necessarily disjoint. Every \(\Gamma_n\) has diameter exactly three.

The total number of vertices and the cardinalities \(S_j\) of the distance-\(j\) sphere about **any** vertex are
\[
 N_n=\frac{(2^n-2^\epsilon)2^{n-1}}6,\quad
 S_0=1,\quad S_1=3(2^{n-2}-1),\quad
 S_3=\frac{(2^{n-2}-2^\epsilon)2^{n-3}}6,\quad
 S_2=N_n-S_0-S_1-S_3.
\]
Thus the diameter-three sphere is exactly the set of nondegenerate planes lying in the alternating orthogonal complement of the starting plane.

## Assumptions and scope

The field is \(\mathbb F_2\), and \(n\) is any integer at least four. The Euclidean inner product is \(a\cdot b=\sum_i a_ib_i\). A two-dimensional linear code \(U\) is LCD when \(U\cap U^{\perp_{\cdot}}=\{0\}\), equivalently when its two-by-two Gram matrix is nonsingular. The graph uses **all** such codes, regardless of their Hamming minimum distance, and ordinary symmetric neighbor adjacency, not associated-neighbor orientations.

For a possibly degenerate alternating form on a finite binary vector space, a nondegenerate two-plane means a two-dimensional subspace on which the alternating form is nonsingular. Its radical has dimension zero or one in the spaces considered here.

## Proof

**Alternating reduction.** In characteristic two, \(p(a)=a\cdot a\). Therefore \(\Omega(a,a)=0\), so \(\Omega\) is alternating. For linearly independent vectors \(a,b\), the determinant of the Euclidean Gram matrix is
\[
 (a\cdot a)(b\cdot b)+(a\cdot b)^2
 =p(a)p(b)+a\cdot b=\Omega(a,b).
\]
Consequently, \(\Gamma_n\)'s vertices are exactly the nondegenerate two-planes for \(\Omega\). Relative to the standard basis the alternating form has matrix \(I+J\), with \(J\) the all-ones matrix. Solving \((I+J)x=0\) shows that the radical is trivial for even \(n\), and is the line spanned by the all-ones vector for odd \(n\); its dimension is \(\epsilon\).

**Vertex and first-sphere counts.** Every vector outside the radical has exactly \(2^{n-1}\) partners \(b\) with \(\Omega(a,b)=1\). Each nondegenerate two-plane has exactly six ordered bases: three choices of nonzero first vector and two choices of second vector. Hence \(N_n=((2^n-2^\epsilon)2^{n-1})/6\). Fixing a nonzero \(a\) in any such plane, the \(2^{n-1}\) partners split into pairs \(\{b,b+a\}\); these yield \(2^{n-2}\) nondegenerate planes through \(a\). The starting plane is one of them. The three nonzero vectors of the starting plane give disjoint lists of neighboring planes, so \(S_1=3(2^{n-2}-1)\).

**Shortest paths.** Suppose \(U,W\) are disjoint nondegenerate planes. A common neighbor must meet both in a line, hence is exactly \(\langle a,b\rangle\) for some nonzero \(a\in U\), \(b\in W\). Such an intermediate plane is a vertex exactly when \(\Omega(a,b)=1\). Thus a two-step path exists precisely when the cross-pairing \(\Omega|_{U\times W}\) is nonzero.

If the cross-pairing is zero, choose any nonzero \(a\in U\) and \(b\in W\). The linear functionals \(\Omega(a,-)\) and \(\Omega(b,-)\) are independent: if they coincided, their difference would put \(a+b\) in the radical, but \(b\in U^{\perp_\Omega}\) would then force \(a\) into the radical of \(\Omega|_U\), a contradiction. Hence a vector \(c\) exists with \(\Omega(a,c)=\Omega(b,c)=1\). The sequence
\[
 U\;--\;\langle a,c\rangle\;--\;\langle b,c\rangle\;--\;W
\]
is a valid three-step path, and a one- or two-step path is impossible. This proves the stated distance characterization and the universal upper bound three.

**Third sphere and sharpness.** Since \(U\) is nondegenerate, \(V=U\oplus U^{\perp_\Omega}\) as an orthogonal direct sum. The latter subspace has dimension \(n-2\), with radical of dimension \(\epsilon\), and its nondegenerate two-planes are exactly the vertices cross-orthogonal to \(U\). Applying the first counting argument in dimension \(n-2\), their number is
\[
 S_3=\frac{(2^{n-2}-2^\epsilon)2^{n-3}}6.
\]
It is positive for every \(n\ge4\), proving diameter exactly three; the remaining \(S_2\) follows by subtraction. All hypotheses and endpoints are included.

## Verification

The standalone script `VERIFY.py` independently generates every binary two-plane, tests LCD by the original Euclidean Gram determinant rather than by the alternating characterization, constructs ordinary neighbor adjacency, and performs a breadth-first search from **every** vertex. It also checks the cross-pairing distance criterion for every ordered pair. Executing `python VERIFY.py` gives:

```
n=4; planes=20; spheres=(1, 9, 9, 1); check=PASS
n=5; planes=80; spheres=(1, 21, 54, 4); check=PASS
n=6; planes=336; spheres=(1, 45, 270, 20); check=PASS
VERIFY_OK
```

These are finite consistency checks; the preceding algebraic argument, not the experiments, proves the assertions for all \(n\ge4\).

## Relationship to prior work

The neighbor graph and its ordinary (non-associated) adjacency come from de la Cruz, Horlemann, Newman, Vela Cabello and Willems, presented at the 5th Pythagorean Conference on June 5, 2025 and subsequently circulated in arXiv:2609.07580v1 (2026). Their paper proves regularity, connectivity, and detailed orbit-subgraph degree formulas in arbitrary dimensions. Its binary section does not give a full dimension-two distance characterization or the exact second- and third-distance sphere counts. The degree \(S_1\) is already obtainable from their general neighbor-count theorem: novelty is **not** claimed for degree or connectedness, but for the alternating-form distance criterion, the characteristic-two diameter of three, and the full distance distribution.

The ordinary Grassmann graph on all two-planes, by contrast, has distance two between disjoint planes; deleting the non-LCD planes can increase distance. A previous LCD-graph triangle/common-neighbor computation addresses a different local incidence invariant and does not determine the distance-three sphere.

## Limitations

The distance formula applies only in binary dimension two; higher-dimensional LCD graphs and other alphabets are not treated. It uses ordinary undirected LCD neighborship and does not measure graph distances in the directed associated-neighbor relation. The underlying symplectic-plane graph may have appeared under an earlier finite-geometric name; an unidentified equivalence would weaken originality. The work is self-reviewed, without independent audit.

## References

1. J. de la Cruz, A.-L. Horlemann, M. Newman, C. Vela Cabello, W. Willems, *The Neighbor Graph of Linear Complementary Dual (LCD) Codes*, arXiv:2609.07580v1, September 7, 2026, https://arxiv.org/abs/2609.07580. The accessible complete 32-page preprint was inspected, including Sections 3–6 and its reference list.
2. C. Vela Cabello, *The Neighbor Graph of Linear Complementary Dual Codes*, 5th Pythagorean Conference talk, June 5, 2025, https://cargo.wlu.ca/5thPythagorean/talks/Carlos_Vela.pdf. The 45-page presentation and its statements on regularity and diameter were read.
3. 5th Pythagorean Conference, *Book of Abstracts*, June 2025, p. 76, https://cargo.wlu.ca/5thPythagorean/5th_Pythagorean_Book_of_Abstracts.pdf.
4. A. E. Brouwer, A. M. Cohen, A. Neumaier, *Distance-Regular Graphs*, Springer, 1989 (classical Grassmann-graph context; not a prior claim of this theorem).
