# Two arithmetic symmetry types of all-smooth conic nets over \(\mathbf F_5\)

## Finding
Let \(V=\mathbf F_5[X,Y,Z]_2\), with ordered basis \((X^2,Y^2,Z^2,XY,XZ,YZ)\). A *smooth net* means a three-dimensional \(\mathbf F_5\)-linear subspace \(W\subset V\) for which every nonzero \(F\in W\) defines a geometrically smooth conic in \(\mathbf P^2\). There are **exactly \(8{,}000\) smooth nets**, forming **two orbits of size \(4{,}000\)** under \(\operatorname{PGL}_3(\mathbf F_5)\). Each has stabilizer order \(93\).

The two orbits have the following reduced-row-echelon representatives, given in the ordered monomial basis above:

\[
W_A=\left\langle X^2+4XY+3XZ+3YZ,\quad Y^2+3XY+XZ,\quad Z^2+XY\right\rangle,
\]
\[
W_B=\left\langle X^2+2XZ+4YZ,\quad Y^2+3XY+XZ,\quad Z^2+XY\right\rangle.
\]

An intrinsic geometric distinction separates the orbits. Over \(\overline{\mathbf F}_5\), the projective plane \(\mathbf P(W_A)\) meets the rank-one quadratic Veronese variety at **three distinct points**, permuted transitively by Frobenius, whereas \(\mathbf P(W_B)\) does **not meet** that variety at all. Thus the first net has exactly one closed degree-three double-line locus and the second has none.

There are exactly \(124{,}000\) two-dimensional subspaces \(U\subset V\) whose six rational projective conics are all geometrically smooth. **Every such pencil is contained in precisely two smooth nets, one from each of the two net orbits.** For either net orbit, its associated quadratic map \(\mathbf P^2(\mathbf F_5)\longrightarrow\mathbf P^2(\mathbf F_5)\) defined by a basis permutes the 31 rational points.

## Assumptions and scope
All counts concern actual \(\mathbf F_5\)-linear subspaces, not ordered bases, and geometric smoothness over the algebraic closure, not merely absence of rational singularities. Isomorphism of nets is simultaneous change of projective source coordinates by \(\operatorname{PGL}_3(\mathbf F_5)\); a change of basis within a net is immaterial. The quadratic-point permutation assertion is on rational points only, not a claim that the quadratic map is a biregular automorphism over the algebraic closure.

## Proof
**Finite exhaustive parameterization.** The unique reduced-row-echelon representation of each three-dimensional subspace of the six-dimensional \(\mathbf F_5\)-space has three pivot columns \(p_1<p_2<p_3\). Enumerate all pivot triples and their unconstrained entries to obtain exactly \(2{,}558{,}556\) nets. For a conic
\[
F=AX^2+BY^2+CZ^2+DXY+EXZ+FYZ
\]
the associated symmetric matrix multiplied by two is
\[
S_F=\begin{pmatrix}2A&D&E\\D&2B&F\\E&F&2C\end{pmatrix}.
\]
Because the characteristic is odd, \(F=0\) is geometrically smooth if and only if \(\det S_F\neq0\). Each net contains exactly 31 rational projective members: \((1,a,b)\) for \(a,b\in\mathbf F_5\), \((0,1,b)\) for \(b\in\mathbf F_5\), and \((0,0,1)\). Exhausting all nets and applying this exact determinant test to all 31 members leaves precisely 8,000. The compiled integer program `census_nets.cpp` outputs the complete canonical 8,000-entry catalogue `conic_nets_q5.bin`; independently `independent_net_census.py` repeats the full sweep using vectorized arithmetic and a separately expanded determinant. The sets of RREF records coincide exactly.

**Projective orbits.** Substitute the source-variable generating transformations: the transposition of the first two coordinates, their three-cycle, the shear \(X\mapsto X+Y\), and \(X\mapsto2X\). These generate \(\operatorname{PGL}_3(\mathbf F_5)\). Exact six-coefficient substitution, RREF reduction, and breadth-first traversal of all 8,000 net records produce exactly two connected orbits, of 4,000 records each. As \(|\operatorname{PGL}_3(\mathbf F_5)|=372{,}000\), orbit-stabilizer gives stabilizers of order 93. The corresponding canonical first orbit representatives are precisely \(W_A\) and \(W_B\).

**Geometric rank-one distinction.** Rank-one quadratics correspond to double lines over the algebraic closure, equivalently to the vanishing of every \(2\times2\) minor of \(S_F\). Write a member \(F=uQ_1+vQ_2+wQ_3\) in each displayed representative. Exact Gröbner reduction on the chart \(u=1\), with variables \(v,w\), gives the following reduced ideals over \(\mathbf F_5\):
\[
I_A=(v+w^2-w+1,\;w^3-w^2+w+1),\qquad I_B=(1).
\]
The cubic \(w^3-w^2+w+1\) has no root in \(\mathbf F_5\), hence is irreducible of degree three and separable. On the chart \(u=0,v=1\), both ideals are \((1)\), and the remaining point \([u:v:w]=[0:0:1]\) fails the rank-one minor equations. Consequently the intersections have three reduced geometric points in orbit A and none in orbit B. This also directly proves that the two discovered group orbits are geometrically distinct.

**Pencil incidence and unique opposite-type extensions.** Independent RREF enumeration of all \(508{,}431\) two-dimensional subspaces of \(V\), testing all six projective members by the determinant, finds exactly 124,000 all-smooth pencils (`census_pencils.cpp`). Each of the 8,000 nets contains exactly 31 two-dimensional subspaces. Exhausting all 248,000 net–pencil incidences (`verify_structure.py`) gives exactly 124,000 distinct pencils, each occurring twice, with orbit-label multiset \(\{A,B\}\). As each pencil in a smooth net is smooth and the independent count exhausts all smooth pencils, the asserted exact extension property follows.

**Rational permutation maps.** For either representative, evaluate its three displayed basis quadratics at each of the 31 normalized rational projective points. No output is zero, and the 31 projective output triples are pairwise distinct. Projective coordinate changes conjugate the induced action on rational points, while a net basis change postcomposes with a projective target automorphism. Therefore the same rational-point bijectivity holds for all 8,000 nets.

## Verification
From the directory containing all accompanying artifacts, compile the two C++17 programs with an optimizing compiler, run `census_nets.cpp` to regenerate `conic_nets_q5.bin`, and run `census_pencils.cpp`. With Python 3, NumPy, and SymPy, execute `independent_net_census.py`, `verify_structure.py`, and `rankone_groebner.py`. They check the census, the independently reproduced canonical catalogue, the two orbit sizes, all pencil-extension multiplicities and orbit labels, rational-point permutations, and the exact geometric rank-one ideals. `VERIFY_OUTPUT.txt` records the direct outputs. The SHA-256 hash of the canonically sorted 8,000 concatenated 18-byte coefficient records is `37347f26110e3ad1ca7ff144c981519c39ee07fc144ad002d0d3022b9ffb94dc`.

## Relationship to prior work
Asgarli, Ghioca, and Reichstein (2022) construct linear systems of smooth hypersurfaces over finite fields, including smooth nets of conics. Their existence and construction do not count all such nets over \(\mathbf F_5\), identify the second rank-one-free orbit, or classify opposite-orbit extensions of every smooth pencil. Asgarli and Ghioca (2022) prove existence statements for smooth pencils and discuss their base loci, without the stated fixed-field net census. Lavrauw, Popiel, and Sheekey (2020) classify odd-field nets containing an \(\mathbf F_q\)-rational rank-one conic; such nets are excluded here since all rational members are smooth. These distinctions concern mathematical statement coverage, not merely titles.

## Limitations
The theorem concerns only \(\mathbf F_5\), the full space of ternary quadratics, and the stated projective equivalence relation. It is an exhaustive computer-assisted finite classification, not a formula for arbitrary finite fields. The intrinsic rank-one certificates, counting programs, and outputs are included, but independent human or external audit has not been performed. Earlier unindexed finite-field net classifications could affect priority; the inspected sources and searched records do not provide a guarantee of worldwide uniqueness of this result.

## References
1. S. Asgarli, D. Ghioca, and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918 (first public 2022-07-02), especially Theorem 2 and Section 3.
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (2022), especially the finite-field pencil and conic examples.
3. M. Lavrauw, T. Popiel, and J. Sheekey, *Combinatorial invariants for nets of conics in PG(2, q)*, arXiv:2010.00177 (2020), especially Theorem 1.1 and its restriction to nets of rank one.
