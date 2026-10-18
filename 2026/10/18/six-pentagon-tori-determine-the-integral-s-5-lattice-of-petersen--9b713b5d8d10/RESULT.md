# Six pentagon tori determine the integral \(S_5\)-lattice of Petersen two-point configurations

## Finding

Let \(P=KG(5,2)\) be the Petersen graph, let \(X=\operatorname{UConf}_2(|P|)\) be the space of unordered pairs of distinct points on its geometric realization, and let \(\Omega\) be the set of partitions of its ten vertices into two disjoint five-cycles. There are exactly six such partitions, naturally identified with the six Sylow-five subgroups of \(S_5=\operatorname{Aut}(P)\). Each pair of disjoint cycles determines an embedded product torus in \(X\).

The six torus fundamental cycles admit orientations \(\tau_\omega\) under which they are permuted *without signs* by \(S_5\), and the exact sequence of integral \(S_5\)-modules
\[
0\longrightarrow\mathbb Z\xrightarrow{\;1\mapsto\sum_{\omega\in\Omega}e_\omega\;}\mathbb Z[\Omega]\xrightarrow{\;e_\omega\mapsto[\tau_\omega]\;}H_2(X;\mathbb Z)\longrightarrow0
\]
is exact. In particular,
\[
H_2(X;\mathbb Z)\cong\mathbb Z[\Omega]/\mathbb Z\!\left(\sum_{\omega\in\Omega}e_\omega\right)\cong\mathbb Z^5.
\]
**Every five of the six embedded-torus classes form an integral basis**, and their displayed sum is their sole integral relation up to multiplication by an integer. The exact sequence does **not** split as a sequence of integral \(S_5\)-modules. This is an integral equivariant classification; the nonequivariant homology rank and rational irreducible character were previously known and are not claimed as new.

## Assumptions and scope

Use vertices indexed from zero by the lexicographic list of two-element subsets of \(\{0,1,2,3,4\}\). Graph vertices are adjacent precisely when their associated subsets are disjoint. Graph edges are sorted lexicographically and oriented from lower vertex index to higher. The chosen fundamental class of a product torus is the external product of two cyclic edge chains, with the sign introduced by ordering the two graph edges in each square.

In this convention, all six unordered pairs of pentagon vertex-cycles, in order, are:

```text
0: (0,7,3,4,9)  | (1,5,8,2,6)
1: (0,7,3,5,8)  | (1,6,2,4,9)
2: (0,7,6,1,9)  | (2,4,3,5,8)
3: (0,7,6,2,8)  | (1,5,3,4,9)
4: (0,8,2,4,9)  | (1,5,3,7,6)
5: (0,8,5,1,9)  | (2,4,3,7,6)
```

Orient each displayed cyclic traversal in the indicated direction and multiply its product torus by the respective signs \((+1,+1,-1,-1,-1,+1)\) to obtain \(\tau_0,\ldots,\tau_5\). All statements concern ordinary integral homology of the **unordered**, collision-free two-point configuration space. No localization or coefficient-field identification is assumed.

## Proof

**Cubical model and signed boundaries.** The Petersen graph satisfies the two-particle sufficient-subdivision hypotheses: its cycles have at least five edges and each path between distinct essential vertices has at least one edge. Its unordered Abrams complex is therefore a deformation retract of \(X\). Its zero-, one-, and two-cell counts are respectively \(45,120,75\), and there are no higher cells. Write \(e_i=(a_i,b_i)\) for an oriented graph edge, with \(a_i<b_i\). Orient a two-cube indexed by disjoint edges \(e_i,e_j\) with \(i<j\) in that order. Its boundary is
\[
\partial[e_i,e_j]=[e_j,b_i]-[e_j,a_i]-[e_i,b_j]+[e_i,a_j],
\]
where \([e,v]\) denotes an oriented moving-edge/occupied-vertex one-cell. The bundled checker reconstructs these boundaries directly and checks \(\partial_1\partial_2=0\).

**All geometric generators.** A canonical enumeration of graph five-cycles yields twelve, and an exhaustive comparison of their vertex sets yields precisely the six disjoint pairs displayed above. For each pair, the signed external product of its two oriented five-cycle chains contains exactly 25 oriented two-cubes, all with coefficients \(\pm1\). Its integer boundary vanishes. Writing these six 75-component columns as \(Z\), the orientation convention above gives the **chain identity** \(Z(1,1,1,1,1,1)^{\mathsf T}=0\), not merely a homological relation.

**Integral basis certificate.** Direct modular Gaussian elimination on the fully specified \(120\times75\) signed matrix \(\partial_2\) gives rank \(70\) over \(\mathbb F_3\). Conversely, the six displayed cycles contain five linearly independent kernel vectors, so the characteristic-zero boundary rank is at most \(75-5=70\). Thus its rank over \(\mathbb Q\) is exactly \(70\), and the integral kernel has rank five. There is no degree-three boundary.

More strongly, select the 75-by-6 cycle matrix rows numbered \(0,1,3,10,13\), where two-cubes are lexicographically ordered by their edge-index pairs. The resulting exact integer submatrix is
\[
\begin{pmatrix}
1&0&0&-1&0&0\\
-1&1&0&0&0&0\\
0&1&-1&0&0&0\\
0&0&0&1&-1&0\\
0&-1&0&0&0&1
\end{pmatrix}.
\]
The determinants obtained by deleting columns \(0,1,2,3,4,5\), respectively, are \((-1,1,-1,1,-1,1)\). Hence the projection of **any five** chosen torus columns onto these five coordinates is a unimodular \(5\times5\) matrix. Since the five cycles already span the rational kernel of \(\partial_2\), the unimodular projection ensures that every *integral* kernel vector has an integral expansion in those five columns. Therefore any five torus cycles form a \(\mathbb Z\)-basis of \(\ker\partial_2=H_2(X;\mathbb Z)\); the full relation lattice among six is exactly the diagonal line generated by the sum.

**Integral equivariance and Sylow identification.** Each order-five subgroup of the natural \(S_5\)-action on the ten graph vertices has exactly two orbits, each an induced pentagon. Distinct Sylow-five subgroups yield the six distinct pentagon partitions, as verified by exhaustive group enumeration. For each of all 120 permutations of the underlying five symbols, the checker applies the induced orientation signs on both graph edges and on ordered square factors; it confirms the *integer two-chain equalities* \(g\tau_\omega=\tau_{g\omega}\). The six torus classes thus realize the permutation module quotient in the finding, rather than only an equality of rational characters.

Finally, an equivariant splitting of the diagonal inclusion would require an \(S_5\)-invariant homomorphism \(\mathbb Z[\Omega]\to\mathbb Z\) taking \(\sum_\omega e_\omega\) to 1. Transitivity forces this homomorphism to take a common integer value on all six generators, so its value on their sum is divisible by six. No such splitting exists.

## Verification

Run `python3 verify.py` with Python 3.8 or later; no third-party packages or external data are required. The checker independently constructs the Petersen graph from the Kneser definition; enumerates all twelve pentagons, six pentagon partitions, and six Sylow-five subgroups; builds and verifies both signed cellular boundaries; checks the six integer torus cycles and their diagonal relation; computes the ranks over \(\mathbb F_2\) and \(\mathbb F_3\); certifies all six five-by-five determinants by exact integer Bareiss elimination; and checks all 120 symmetry actions at the integer-chain level. Its final line is `H2_EQUAL_Z6_MOD_DIAGONAL ANY_FIVE_TORI_INTEGRAL_BASIS`.

The characteristic-two rank of \(\partial_2\) is 69, whereas its characteristic-three rank is 70. Therefore mod-two rank alone must **not** be used to infer the integral rank. The unimodular minors, not just rational spanning, are essential for the integral conclusion.

## Relationship to prior work

Farley–Sabalka provide the classical graph-braid discrete-Morse framework. Barnett–Farber establish the deleted-product intersection framework for two points, with explicit results especially for planar graphs. Maciążek–Sawicki discuss general product-cycle generation of degree-two graph-configuration homology, so the existence of product torus classes is not new. An–Knudsen formulate broader questions about geometric degree-two generators and relations, with their principal generation theorem applying to planar graphs.

A previously published Petersen-specific computation establishes \(H_2(X;\mathbb Z)\cong\mathbb Z^5\) and identifies the rational \(S_5\)-character as the irreducible representation indexed by \((2,2,1)\). That **does not determine** the integral \(S_5\)-lattice or identify it with six shortest-cycle product tori and their unique integral relation. The present result supplies those additional facts and the stronger any-five geometric basis property. It does not claim priority for the Betti number, rational character, existence of torus classes, or general deleted-product methods.

## Limitations

The finding classifies the degree-two integral \(S_5\)-module for this particular unordered two-particle space, and the relations among these six selected embedded tori. It does not classify first-homology torsion, the fundamental group, other particle numbers, arbitrary embedded surfaces, or a global minimum for the number of cubes representing a nonzero degree-two class. The exact finite computation has an inspectable standalone verifier. The literature comparison cannot exclude an equivalent calculation in unindexed or inaccessible sources.

## References

1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first posted 2004-10-25); *Algebraic & Geometric Topology* 5 (2005), 1075–1109.
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (first posted 2009-03-12); *Algebraic & Geometric Topology* 9 (2009), 593–624.
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, *Communications in Mathematical Physics* 375 (2020), 743–769, DOI: 10.1007/s00220-019-03583-5.
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371.
5. *Two-particle Petersen configuration homology as an \(S_5\)-module*, previously published mathematical research record `2bac82e0590d` (2026); reports the nonequivariant groups and rational characters, not the integral torus presentation.
6. A. E. Brouwer, *Petersen graph* data sheet, `https://aeb.win.tue.nl/drg/graphs/Petersen.html` (six pentagon decompositions and symmetry data).
