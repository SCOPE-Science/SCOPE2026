# Exact two-point face-vector law for random central sections of the four-cube

## Finding
Let \(Q=[-1,1]^4\), and let \(H=u^\perp\) for a Haar-uniform unit normal \(u\in S^3\). Write \((f_0,f_1,f_2)\) for the vertex, edge and facet numbers of the three-polytope \(Q\cap H\). Then the entire joint face-vector distribution is
\[
\mathbb P\bigl((f_0,f_1,f_2)=(8,12,6)\bigr)=\frac13,\qquad
\mathbb P\bigl((f_0,f_1,f_2)=(12,18,8)\bigr)=\frac23.
\]
These are the only possibilities with positive probability. More precisely, for every normal whose coordinate entries are nonzero and whose signed coordinate sums are nonzero, write \(d=\max_i|u_i|\) and \(S=\sum_i|u_i|\). If \(2d>S\) then the section has the first face vector; if \(2d<S\) it has the second. The equality \(2d=S\) belongs to a null exceptional set.

## Assumptions and scope
A central hyperplane is a three-dimensional linear subspace through the center of \(Q\). Haar probability on hyperplanes is induced by uniform spherical measure on \(S^3\), with \(u\) and \(-u\) representing the same hyperplane. The statement is about central sections, not arbitrary affine sections, and is not a claim about lower-dimensional nongeneric normals.

## Proof
**1. Vertex counting by crossing cube edges.** For normals outside the finite union of exceptional hyperplanes \(u_i=0\) and \(\sum_i\epsilon_i u_i=0\), every vertex of \(Q\cap u^\perp\) is the intersection with exactly one edge of the four-cube joining opposite signed values of the functional \(x\mapsto u\cdot x\). Thus its vertex count equals the number of cube edges whose endpoint signs are opposite. We may change signs and permute coordinates and assume the four normal coordinates are positive, \(a\le b\le c\le d\). Set \(T=a+b+c\).

If \(d>T\), the sign of the functional at each cube vertex is determined solely by its last coordinate. Exactly the eight cube edges parallel to that coordinate cross the hyperplane, and \(f_0=8\).

If \(d<T\), each cube vertex having at least three positive coordinates has positive functional value; each with at most one positive coordinate has negative value. Exactly three of the six cube vertices with two positive coordinates have positive functional value and three have negative functional value, because antipodal vertices occur in complementary pairs. There are no cube edges joining two vertices at the same positive-coordinate level. Each positive level-two vertex has exactly two neighbors at level one, both negative; each negative level-two vertex has exactly two neighbors at level three, both positive. No other edges connect opposite signs. Hence there are \(3\cdot2+3\cdot2=12\) crossings and \(f_0=12\).

**2. Probability from a Cauchy ratio.** Let \(G_1,\ldots,G_4\) be independent standard Gaussian random variables. The normal \(G/\|G\|\) is Haar-uniform. A specified edge parallel to the first coordinate, with fixed other-coordinate signs \(\epsilon_2,\epsilon_3,\epsilon_4\), crosses precisely when
\[
 |G_1|> |\epsilon_2G_2+\epsilon_3G_3+\epsilon_4G_4|.
\]
The sum on the right is independent of \(G_1\) and has Gaussian variance \(3\). The ratio of these independent Gaussians is standard Cauchy after division by \(\sqrt3\). Consequently, the crossing probability is
\[
 \mathbb P\bigl(|C|>\sqrt3\bigr)=1-\frac2\pi\arctan(\sqrt3)=\frac13,
\]
where \(C\) is standard Cauchy. By linearity over all \(32\) edges,
\[\mathbb E f_0=\frac{32}{3}.\]
Since \(f_0\) has only the two values \(8\) and \(12\) almost surely, \(8p+12(1-p)=32/3\) gives \(p=1/3\).

**3. The complete face vector.** Every generic section vertex lies in the relative interior of one cube edge and hence belongs to exactly three of the section's facet-supporting hyperplanes (the three cube facets incident with the edge). These three facets are locally independent, so the section is a simple three-polytope. The handshaking identity gives \(2f_1=3f_0\), while Euler's relation gives \(f_0-f_1+f_2=2\). Thus \(f_1=3f_0/2\) and \(f_2=f_0/2+2\), yielding respectively \((8,12,6)\) and \((12,18,8)\).

## Verification
The standalone `verify.py` uses only the Python standard library. It enumerates all nonexceptional ordered positive integer normals in the integer box from \(1\) to \(8\) in each coordinate, explicitly counts crossed edges and section face-vector values, and checks the predicted phase inequality. It also performs a seeded Gaussian-sampling check of the probability. The exact finite checks are not a substitute for the infinite spherical probability proof or for the generic-sign argument above. Execute `python3 verify.py` and require `VERIFY_OK`.

## Relationship to prior work
De Loera, Lopez-Campos and Torres study which vertex counts can be attained by hyperplane sections of polytopes and characterize attainable counts of hypercube sections; their results concern combinatorial possibility, not the Haar distribution for central sections. Lonke's earlier random-cube-section work, and Kabluchko and Seidel's results for regular polytopes, address expected face numbers; those broader expectation theorems cover the expectation derived here, which is not asserted as novel. The new assertion is the two-point *joint law* together with the explicit normal-cone phase criterion in the central four-dimensional case.

## Limitations
This law is specific to central hyperplane sections of \(Q\subset\mathbb R^4\); it does not enumerate all possible affine section combinatorial types, address other dimensions, or claim uniqueness of its geometric derivation. The rarity of nongeneric normals matters: on exceptional hyperplanes, vertex coalescences may occur. Older unindexed stereology or hypercube-section classifications may contain an equivalent distribution; no independence or priority determination is claimed.

## References
1. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public version 2024-12-17), https://arxiv.org/abs/2412.12419.
2. Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123, https://arxiv.org/abs/math/9812123.
3. Z. Kabluchko and H. Seidel, *Convex Cones Spanned by Regular Polytopes*, arXiv:2006.09492, https://arxiv.org/abs/2006.09492.
4. H. Fukuda, N. Muto, K. Goto and G. Nakamura, *Sections of Hyper-Cube in Five Dimensions*, FORMA 12 (1997), 15–33 (relevant classification reference; complete text not verified here).
