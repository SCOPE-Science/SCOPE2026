# Three mod-three Moore summands in the \(\mathrm{PG}(2,3)\) cap complex

## Finding

Let \(P\) be the thirteen-point projective plane \(\mathrm{PG}(2,3)\). Define the **cap complex** \(K\) to be the abstract simplicial complex whose faces are subsets of \(P\) containing no three distinct collinear points. Then

\[
K\simeq\left(\bigvee_{j=1}^{3}M(\mathbb Z/3,2)\right)\vee\left(\bigvee_{i=1}^{66}S^3\right),
\]

where \(M(\mathbb Z/3,2)=S^2\cup_{3}e^3\) is the degree-three Moore space. Equivalently, the only nonzero reduced integral homology groups are

\[
\widetilde H_2(K;\mathbb Z)\cong(\mathbb Z/3)^3,
\qquad
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{66}.
\]

The complex is simply connected. In particular, its nonzero lower-dimensional homology is **genuine integral three-torsion**, not a rational Betti number. No equivariance or assertion for higher-order projective planes is claimed.

## Assumptions and scope

Identify points with one-dimensional subspaces of \(\mathbb F_3^3\), represented by the lexicographically sorted thirteen triples whose first nonzero coordinate is one. A projective line has equation \(a x+b y+c z=0\), for a nonzero triple \((a,b,c)\) modulo scalars. A finite set is a cap when no three of its points belong to one such line. Faces are unordered sets, and simplicial chains use increasing-vertex orientations. In particular, **the chain complex is the alternating simplicial chain complex**, not the free chain complex of *all ordered injective tuples*.

The result concerns precisely the ordinary geometric realization \(|K|\) of this finite abstract simplicial complex, with integral coefficients.

## Proof

**1. The finite incidence structure and all dimensions.** There are thirteen projective points and thirteen lines, each containing four points; every pair of points determines exactly one line. The four-entry line table and the intrinsic finite-field reconstruction are both checked in `verify_cap.py`. Consequently every vertex and every edge is a face, while exactly \(13\binom{4}{3}=52\) of the \(\binom{13}{3}=286\) triples are excluded. The number of allowed triangles is \(234\). For each noncollinear triple, the union of its three secant lines has nine points, leaving exactly four points that can extend it to a four-cap. There are therefore \(234\) four-caps. Direct enumeration confirms that no five-cap exists. Thus \(K\) is three-dimensional with face vector

\[
(f_0,f_1,f_2,f_3)=(13,78,234,234).
\]

**2. The second skeleton is simply connected.** Its one-skeleton is the complete graph on thirteen vertices. Every loop in that graph is a product of triangular loops. If a triple is noncollinear, its triangle is already a two-face. If it is collinear, choose any projective point outside its line and cone its three edges to this point; all three cone triangles are noncollinear and hence present. Every triangular loop is therefore null-homotopic in the second skeleton. Thus \(\pi_1(K^{(2)})=0\), and so \(\pi_1(K)=0\).

**3. Exact integral boundary calculation.** Let \(C_d\) be the free abelian group on increasing \((d+1)\)-tuples that are faces. With the usual boundary \(\partial_d[v_0,\ldots,v_d]=\sum_{j=0}^d(-1)^j[v_0,\ldots,\widehat v_j,\ldots,v_d]\), direct exact integer Smith reduction gives

\[
\begin{aligned}
\operatorname{SNF}(\partial_1)&=(1^{12},0),\\
\operatorname{SNF}(\partial_2)&=(1^{66},0^{12}),\\
\operatorname{SNF}(\partial_3)&=(1^{165},3^3,0^{66}).
\end{aligned}
\]

These are invariant-factor multiplicities, with zero padding to the number of rows; in the last line the matrix is square. The standalone script reconstructs **all** faces and all three integral matrices from the field operations and computes their Smith normal forms without approximate linear algebra. It also verifies \(\partial_1\partial_2=\partial_2\partial_3=0\), the line incidence structure, absence of five-caps, and the independent rank \(165\) for \(\partial_3\) modulo three.

Because the image of \(\partial_2\) has rank \(66\), its kernel in \(C_2\cong\mathbb Z^{234}\) has rank \(168\). This kernel is a primitive sublattice: it is the kernel of a map to a free group. The \(168\) nonzero invariant factors of \(\partial_3\) are therefore also the invariant factors of its map into this kernel. There are \(165\) unit factors and three factors equal to three, leaving \(66\) zero source directions. The stated reduced homology follows, with no hidden torsion or unexamined dimensions.

**4. Upgrade to homotopy type.** Since \(K^{(2)}\) is simply connected and two-dimensional, the Hurewicz theorem and homological Whitehead theorem give a homotopy equivalence \(K^{(2)}\simeq\bigvee^{168}S^2\). The attaching maps of its \(234\) three-cells are classified by their degrees in \(\pi_2(\bigvee^{168}S^2)\cong\mathbb Z^{168}\). Their degree matrix has precisely the Smith factors obtained above. Unimodular basis changes of target and source are realizable by homotopy equivalences of wedges of two-spheres; homotopy cofibers are invariant under these equivalences. Diagonalizing the degree matrix gives \(165\) contractible cell pairs, three degree-three Moore attachments, and \(66\) zero-degree three-cell attachments. Hence the displayed wedge equivalence follows.

## Verification

From the containing directory run `python3 verify_cap.py` after installing the pinned dependency in `requirements.txt`. The program uses exact integer arithmetic and a canonical finite-field reconstruction, verifies all faces (including exclusions and maximum dimension), and prints `VERIFY_OK` only after both chain identities, all Smith factors, and the mod-three rank assertion pass. The actual output is in `verification.out`.

The reproducible finite calculation establishes every numerical premise used above. The topological lifting step is the explicit Hurewicz–Whitehead and homotopy-cofiber argument; no finite sampling or assumption that rational homology determines integral homotopy is used.

## Relationship to prior work

Finite projective arcs and their maximal sizes are classical: Ball's 1996 paper concerns arc and blocking-set sizes, not this associated integral homotopy type. Das and O'Connor study *continuous* configuration spaces of noncollinear points in the **complex** projective plane, with rational cohomology and point counts over finite fields; those are not the finite thirteen-vertex simplicial cap complex. Lew studies representability and boxicity of simplicial complexes, including an **affine** Steiner-triple example on nine points, not the homology of the present projective complex.

A 2022 mathematical question considers noncollinear configurations over finite fields but uses a free chain complex on **ordered tuples**. The present alternating simplicial chain complex is a different integral chain object; the result neither solves that ordered question nor follows from its formulation. The newly observed three-torsion demonstrates why retaining the integral chain convention matters. Related calculations on the seven-point projective plane and the nine-point affine plane concern different incidence sets and do not imply the thirteen-point calculation.

## Limitations

The displayed wedge equivalence is nonequivariant. No homotopy classification is asserted for \(\mathrm{PG}(2,q)\) with \(q\ne3\), for an ordered-injective-word chain complex, or for a complex-projective configuration space. A direct noncomputational explanation of the three Smith factors equal to three is not provided; those factors are certified by exhaustive exact finite integer arithmetic. Independent replication and comprehensive publication-priority checking remain outstanding.

## References

1. S. Ball, “Multiple Blocking Sets and Arcs in Finite Planes,” *Journal of the London Mathematical Society* 54 (1996), 581–593, doi:10.1112/jlms/54.3.581 (published 1996-12-01).
2. R. Das and B. O'Connor, “Configurations of noncollinear points in the projective plane,” arXiv:1904.11409 (first public 2019-04-25; HTML full text at https://arxiv.org/html/1904.11409v2).
3. A. Lew, “Representability and boxicity of simplicial complexes,” arXiv:2008.09997 (first public 2020-08-23; HTML full text at https://arxiv.org/html/2008.09997v1).
4. “Almost acyclicity of the complex of configuration spaces of noncollinear points in projective plane over finite fields,” MathOverflow question 422219 (posted 2022-05-10): https://mathoverflow.net/questions/422219/almost-acyclicity-of-the-complex-of-configuration-spaces-of-noncollinear-points.
