# The Chilean conic configuration has a \(24\)-fold combinatorial–projective symmetry gap
## Finding
For every nondegenerate complex Chilean configuration \(\mathcal C\) of twelve conics arising from an index-two Hesse-type Halphen pencil, let \(P\) be its set of nine points at which eight conics meet. Then
\[
\operatorname{Aut}_{\mathrm{inc}}(P,\mathcal C)\cong \operatorname{AGL}(2,3),
\qquad |\operatorname{Aut}_{\mathrm{inc}}(P,\mathcal C)|=432,
\]
while the full projective stabilizer of the realized conic arrangement is
\[
\operatorname{Stab}_{\operatorname{PGL}_3(\mathbb C)}(\mathcal C)\cong G_{18},
\qquad |G_{18}|=18.
\]

Moreover, the four triples of conics that are the reducible fibers are determined by the abstract point–conic incidence relation itself. Two conics lie in the same triple exactly when they share three points of \(P\); conics in different triples share four points of \(P\). Therefore the action on the four intrinsic triples gives an exact sequence
\[
1\longrightarrow G_{18}\longrightarrow \operatorname{AGL}(2,3)\longrightarrow S_4\longrightarrow 1.
\]
In particular, the abstract incidence symmetry group is larger than the projectively realized symmetry group by the exact factor \(24\).

## Assumptions and scope
The ground field is \(\mathbb C\). The configuration is one of the nondegenerate Chilean configurations constructed from an index-two Hesse-type Halphen pencil in Dolgachev–Laface–Persson–Urzúa. Degenerate specializations in which conic components become lines or components collide are excluded. The claim concerns the incidence structure on the nine eightfold base points and the twelve conics, together with the projective stabilizer of that realized twelve-conic set.

## Proof
Dolgachev–Laface–Persson–Urzúa identify the nine relevant sections with the affine plane \(\mathbb F_3^2\) and the twelve components of the Hesse fibers with its twelve affine lines. In the index-two construction, a Chilean conic is obtained from two disjoint cosets in one parallel class. Since each parallel class has exactly three affine lines, such a conic is equivalently indexed by the unique omitted affine line \(L\). Thus, after identifying \(P=\mathbb F_3^2\), its incidence block is
\[
B_L=P\setminus L.
\]
Hence the twelve six-point conic blocks are exactly the complements of the twelve affine lines.

A permutation of the nine points preserves the conic blocks if and only if it preserves their complements, hence if and only if it preserves the affine lines of \(\operatorname{AG}(2,3)\). The full automorphism group of this incidence structure is therefore \(\operatorname{AGL}(2,3)\). The included verifier independently exhausts all \(9!\) point permutations and finds exactly \(432\) incidence automorphisms; it separately generates all affine maps and verifies equality with that exhaustive set.

The reducible-fiber partition is also visible without coordinates. If \(L\) and \(M\) are distinct parallel affine lines, then \(L\cap M=\varnothing\), so
\[
|B_L\cap B_M|=9-|L\cup M|=3.
\]
If they are nonparallel, then \(|L\cap M|=1\), so
\[
|B_L\cap B_M|=9-|L\cup M|=4.
\]
Thus the graph on the twelve conics joining pairs with three common base points is exactly four disjoint triangles. Those triangles are the four reducible Halphen fibers.

The action of \(\operatorname{AGL}(2,3)=\mathbb F_3^2\rtimes\operatorname{GL}(2,3)\) on the four parallel classes factors through the natural action of \(\operatorname{GL}(2,3)\) on \(\mathbb P^1(\mathbb F_3)\). Its kernel is
\[
\mathbb F_3^2\rtimes\{\pm I\},
\]
of order \(18\), and the quotient is \(\operatorname{PGL}(2,3)\cong S_4\).

It remains to identify that kernel with the actual projective stabilizer. Dolgachev–Laface–Persson–Urzúa prove that every automorphism of an index-two Hesse-type Halphen surface descends under the chosen blow-down to a projective transformation of \(\mathbb P^2\), and that the complete surface automorphism group is precisely \(G_{18}\cong (\mathbb Z/3\mathbb Z)^2\rtimes(\mathbb Z/2\mathbb Z)\). They also explain that every surface automorphism preserves the Halphen pencil. Therefore these eighteen transformations permute the twelve conic components and fix each of the four reducible fibers setwise.

Conversely, any projective transformation stabilizing the twelve-conic arrangement preserves the nine multiplicity-eight points, since the other singularities of the union are ordinary double points. It therefore lifts to the blow-up at those nine points, hence to an automorphism of the corresponding Halphen surface. The source theorem bounds the projective stabilizer by \(G_{18}\), while the preceding paragraph supplies all eighteen elements. Thus the projective stabilizer is exactly \(G_{18}\), and because this group fixes the four fiber triples, it is exactly the kernel of the abstract \(S_4\)-action.

## Verification
Run `python verify.py`. It reconstructs \(\operatorname{AG}(2,3)\), forms the twelve complement blocks, checks block size \(6\) and point degree \(8\), checks that block-pair intersection sizes are \(3\) or \(4\) with the size-\(3\) graph equal to four triangles, exhausts all \(9!\) point permutations, and independently generates every affine transformation. The two automorphism sets agree and have cardinality \(432\). It also checks \(432/18=24\).

The projective order \(18\) is not inferred computationally: it is the published complete automorphism-group theorem for the associated Halphen surface, together with the source's descent to \(\mathbb P^2\). The proof above explains why this theorem gives both the upper and lower bounds for the projective stabilizer of the conic arrangement.

## Relationship to prior work
Dolgachev–Laface–Persson–Urzúa construct the Chilean configuration, encode the Hesse data by \(\mathbb F_3^2\), and prove \(\operatorname{Aut}(S)\cong G_{18}\) for the associated Halphen surface. They do not state the full abstract automorphism group of the \((12_6,9_8)\) point–conic incidence structure or identify the projective group as the kernel of its action on the four incidence-recoverable conic triples.

Kohel–Roulleau–Sarti independently study the same twelve conics through a generalized-Kummer double cover. They explicitly encounter \(\operatorname{AGL}_2(\mathbb F_3)\) in the lattice symmetry of the natural \(9\mathbf A_2\)-configuration and record the \(3\)-versus-\(4\) common-point pattern among the conics. Their \(G_{432}\) acts in the K3/lattice setting; their discussion does not identify the projective stabilizer of the plane twelve-conic realization with the kernel of the four-triangle action. Pokora–Szemberg study freeness and log geometry of the Chilean and extended Chilean arrangements, and Dimca–Pokora–Sticlaru study their Alexander polynomials; neither supplies this symmetry comparison.

## Limitations
The statement is about the nondegenerate complex family. It does not classify automorphisms of degenerate specializations, automorphisms of the complement as an abstract variety, or birational self-maps that fail to preserve the realized conic set. The exhaustive computation concerns only the finite incidence structure; the projective-stabilizer identification uses the published Halphen-surface automorphism theorem.

## References
1. I. Dolgachev, A. Laface, U. Persson, G. Urzúa, *Chilean configuration of conics, lines and points*, arXiv:2008.09627; Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 23 (2022), 877–914, DOI 10.2422/2036-2145.202011_005. See Section 4 and Corollary 4.2.
2. D. Kohel, X. Roulleau, A. Sarti, *A special configuration of \(12\) conics and generalized Kummer surfaces*, arXiv:2004.11421.
3. P. Pokora, T. Szemberg, *Conic-line arrangements in the complex projective plane*, arXiv:2002.01760.
4. A. Dimca, P. Pokora, G. Sticlaru, *On the Alexander polynomials of conic-line arrangements*, arXiv:2305.01450.
