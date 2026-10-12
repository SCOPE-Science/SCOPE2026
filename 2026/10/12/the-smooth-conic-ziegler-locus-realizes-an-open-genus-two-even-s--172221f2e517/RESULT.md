# The smooth-conic Ziegler locus realizes an open genus-two even-spin moduli space

## Finding
Let \(\mathcal Z^{\mathrm{sm}}\) be the projective-equivalence coarse moduli space of unlabelled nine-line arrangements obtained from six distinct vertices on a **smooth** conic, split into an unordered pair of three-element subsets, by joining every vertex in one subset to every vertex in the other. Require that the nine chords are distinct and that their entire intersection multiplicity profile is six ordinary triple points (the vertices) and eighteen ordinary double points. Then
\[
\boxed{\mathcal Z^{\mathrm{sm}}\simeq U\subset\mathcal S^+_2,\qquad \dim U=3,\qquad U\text{ irreducible},}
\]
where \(U\) is a nonempty Zariski-open subset of the **coarse** moduli of smooth genus-two curves with an even theta characteristic. The natural forgetful morphism \(U\to\mathcal M_2\) has generic degree \(10\), with its ten sheets indexed by the even theta characteristics. For a pair \((C,\vartheta)\in U\),
\[
\operatorname{Stab}_{\operatorname{PGL}_3}(\mathcal A)
\cong \operatorname{Aut}(C,\vartheta)/\langle\iota\rangle,
\]
where \(\iota\) is the hyperelliptic involution; the generic stabilizer is trivial. By Dimca--Sticlaru, every member of this locus has \(\operatorname{mdr}=5\) and is not \(2\)-formal. The last Jacobian statement is **prior work**; the result here is the reconstruction of the even-spin structure, the geometric moduli identification, and its degree/stabilizer consequences.

## Assumptions and scope
Work over \(\mathbb C\). Let \(Q\subset\mathbb P^2\) be a smooth conic and \(W\subset Q\) a reduced set of six distinct points. Let \(\{A,B\}\) be an unordered partition \(W=A\sqcup B\) with \(|A|=|B|=3\), and set
\[
\mathcal A(Q,W,\{A,B\})=\bigcup_{a\in A,\,b\in B}\overline{ab}.
\]
The open incidence condition \((*)\) requires nine different lines and exactly six multiplicity-three intersections at \(W\), with all remaining line intersections ordinary double points. Counting pairs gives \(36-6\binom32=18\) double points. No marked ordering of the lines, of \(W\), or of the two partition blocks is retained. The resulting graph with vertex set \(W\) and with edges given by its nine lines is \(K_{3,3}\). Its unique two-coloring (up to swapping colors) recovers \(\{A,B\}\).

Let \(\mathcal S^+_2\) denote the coarse moduli of pairs \((C,\vartheta)\) where \(C\) is a smooth complex genus-two curve and \(\vartheta\in\operatorname{Pic}^1(C)\) satisfies \(\vartheta^{\otimes2}\simeq\omega_C\) and \(h^0(C,\vartheta)\) is even. Its open subset \(U\) is defined by the cross-chord incidence condition \((*)\), applied to the unordered \(3+3\) partition corresponding to \(\vartheta\). The assertion is about **coarse moduli spaces** (not an identification of stacks or of compactified moduli).

## Proof
**1. Reconstruction from an unlabelled arrangement.** Under \((*)\), the six triple points are intrinsically the only multiplicity-three intersections and therefore recover \(W\). Any five distinct points on a smooth conic determine it uniquely, so the unordered arrangement also recovers \(Q\). Each arrangement line passes through precisely two of the six triple points, and the resulting adjacency graph is \(K_{3,3}\). Since this connected bipartite graph has exactly one bipartition up to interchange, the arrangement reconstructs \(\{A,B\}\). Conversely \((Q,W,\{A,B\})\) produces exactly the prescribed arrangement. An automorphism of a smooth conic is a Möbius transformation, and every such transformation extends via the quadratic Veronese representation to a projectivity of \(\mathbb P^2\) preserving the conic. This gives inverse projectively equivariant constructions.

**2. The spin structure.** Take the genus-two double cover \(\pi:C\to Q\simeq\mathbb P^1\) branched at \(W\), let \(W_w\) denote the ramification point above \(w\in W\), and let \(H\) be the hyperelliptic divisor of degree two. Thus \(K_C\sim H\), \(2W_w\sim H\), and \(\sum_{w\in W}W_w\sim3H\). Set
\[
\vartheta_A=\mathcal O_C\Bigl(\sum_{a\in A}W_a-H\Bigr).
\]
It has degree one and \(\vartheta_A^{\otimes2}\simeq\omega_C\). For the complementary block \(B\), the displayed divisor identities give \(\vartheta_A=\vartheta_B\). The classical genus-two Weierstrass-point classification states that these ten complementary pairs of triples give **all and only** the ten distinct even theta characteristics (Lange--Ortega, Section 3 and (7.1)); the six odd ones correspond to the individual Weierstrass points. Hence \((Q,W,\{A,B\})\leftrightarrow(C,\vartheta_A)\) is a natural bijection of geometric isomorphism classes. The cover and chord constructions are algebraic and equivariant in families; comparing the shared configuration-space quotients by \(\operatorname{PGL}_2\) and \((S_3\times S_3)\rtimes C_2\) yields an isomorphism of the indicated **coarse** moduli open spaces.

**3. Nonemptiness, dimension, degree, and automorphisms.** Incidence condition \((*)\) is Zariski open in the variety of six distinct ordered points on \(\mathbb P^1\), and invariant under the finite block-permutation group. It is nonempty: for parameters
\[
T=\{0,1,2,4,7,11\},\qquad P(t)=[1:t:t^2],
\]
every one of the ten unordered partitions gives nine distinct cross-chords, exactly six triple points, and eighteen double points. The accompanying exact-integer `verify.py` enumerates all ten partitions and all \(36\) pairs of lines per partition. It also checks that the only Möbius transformation preserving \(T\) is the identity, so the ten resulting arrangements are pairwise non-projectively-equivalent. The ambient ordered configuration space is irreducible of dimension six, and quotienting by the three-dimensional \(\operatorname{PGL}_2\) action and a finite group produces an irreducible three-dimensional open moduli space. At a general sextuple there is no nontrivial Möbius symmetry; all ten partitions satisfy \((*)\) on a dense open set (indeed the exhibited sextuple satisfies all ten). Thus the generic forgetful degree is \(\binom63/2=10\).

A projectivity stabilizing the unlabelled nine-line arrangement must preserve \(W,Q\), and its recovered unordered bipartition. Conversely every Möbius transformation of \(Q\) preserving \(W\) and \(\{A,B\}\) extends uniquely to an ambient projectivity. Each such Möbius transformation lifts to two automorphisms of \(C\), differing by \(\iota\), and preserves \(\vartheta_A\). These observations give the displayed stabilizer isomorphism, including special non-generic members of \(U\). The general one is trivial.

**4. The syzygy jump.** Reorder the two blocks alternately around a combinatorial six-cycle in \(K_{3,3}\). Its six edges are the six sides of a hexagon and the remaining three edges are the opposite long diagonals of Dimca--Sticlaru's construction. Their Corollary 1.7, under exactly the six-triple/eighteen-double incidence condition and the smooth-conic assumption, gives \(\operatorname{mdr}=5\) and non-\(2\)-formality. Their Theorem 1.8 gives \(\operatorname{mdr}=6\) off the conic condition in the corresponding general six-vertex hexagon family. Neither theorem is reproved or claimed new here.

## Verification
Run `python3 verify.py` with a standard-library Python interpreter. The program uses primitive integral line and point coordinates. It enumerates each of the ten unordered \(3+3\) partitions of the six rational parameters, all nine cross-chord equations, every pairwise intersection, and all \(120\) potential Möbius maps determined by the images of \((0,1,2)\). It returns:

`VERIFY_OK six_points=6 partitions=10 distinct_arrangements=10 every_incidence=6x3+18x2 base_mobius_stabilizer=1 fiber=10`

This **finite** computation is solely the exact nonemptiness and ten-sheet witness. Irreducibility, moduli reconstruction, the general degree, and stabilizer formula are justified by the preceding algebraic proof, not extrapolated from the witness.

## Relationship to prior work
Dimca--Sticlaru, *From Pascal's Theorem to the geometry of Ziegler's line arrangements*, Assumption 1.3, Corollary 1.7, and Theorem 1.8, give the nine-line incidence template and the known syzygy/formality dichotomy, but not its genus-two spin-moduli reconstruction. Dimca--Ibadula--Măcinic, *Numerical invariants and moduli spaces for line arrangements*, Remark 4.2, identifies a deformation between conic and non-conic examples but does not identify the conic locus with spin moduli. Lange--Ortega, *Pryms of non-cyclic triple coverings and log canonical models of the spin moduli space of genus 2*, Section 3 and Eq. (7.1), gives the preexisting \(3+3\) Weierstrass partition/even-theta dictionary and the quotient description of \(\mathcal S^+_2\), without reference to Ziegler's arrangements. Fei Ye's classification concerns the moduli and topology of nine-line intersection lattices, not this spin correspondence. The contribution is the intrinsic recovery of the spin marking from the **unlabelled nine-line arrangement** and the resulting geometric identification of its smooth-conic Jacobian-syzygy locus.

## Limitations
The original Ziegler example with a reducible conic is excluded. This is only the **smooth-conic open portion** of the syzygy-drop locus, not every conic degeneration, nor every nine-line lattice. No extension across coincident vertices, additional concurrences, reducible conics, boundary spin curves, or compactifications is asserted. The claim is at coarse-moduli level; automorphism stacks may retain scalar and hyperelliptic stabilizers. The novelty comparison does not rule out an unindexed treatment of nine-chord configurations described in older classical invariant-theoretic terminology.

## References
1. A. Dimca and G. Sticlaru, *From Pascal's Theorem to the geometry of Ziegler's line arrangements*, arXiv:2312.11928, first posted 19 December 2023, Assumption 1.3, Corollary 1.7 and Theorem 1.8. https://arxiv.org/pdf/2312.11928
2. H. Lange and A. Ortega, *Pryms of non-cyclic triple coverings and log canonical models of the spin moduli space of genus 2*, arXiv:1309.6984, Sections 3 and 7, especially (7.1). https://arxiv.org/pdf/1309.6984
3. A. Dimca, D. Ibadula and D. A. Măcinic, *Numerical invariants and moduli spaces for line arrangements*, arXiv:1609.06551, Section 4 and Remark 4.2. https://arxiv.org/pdf/1609.06551
4. F. Ye, *Classification of Moduli Spaces of Arrangements of 9 Projective Lines*, arXiv:1112.4306. https://arxiv.org/pdf/1112.4306
5. A. Dimca and P. Pokora, *On Ziegler pairs of line arrangements: from non-existence to abundance*, arXiv:2606.20421, related modern comparison. https://arxiv.org/abs/2606.20421
