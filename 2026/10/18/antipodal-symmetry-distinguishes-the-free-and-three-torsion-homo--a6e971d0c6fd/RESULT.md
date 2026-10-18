# Antipodal symmetry distinguishes the free and three-torsion homology of the icosahedral matching complex

## Finding
Let \(I\) be the twelve-vertex icosahedral graph, and let \(X=\mathcal M(I)\) be its ordinary matching complex. Let \(\iota\) be the graph automorphism sending each vertex to its unique vertex at graph distance three, and let \(G=\operatorname{Aut}(I)\). Then
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}\mathbb Z^{64}\oplus\mathbb Z/3,&j=3,\\0,&j\ne3.\end{cases}
\]
On the unique order-three torsion subgroup \(T\subset\widetilde H_3(X;\mathbb Z)\), **antipodal inversion acts by negation**:
\[
\boxed{\iota_\ast|_T=-\operatorname{id}_T.}
\]
More precisely, \(G\) has order \(120\), its commutator subgroup \(G'\) has order \(60\), and \(\iota\notin G'\). The complete action of \(G\) on \(T\cong\mathbb Z/3\) is therefore the nontrivial quotient character \(G/G'\cong C_2\to\operatorname{Aut}(\mathbb Z/3)\cong C_2\): elements of \(G'\) act trivially and elements of its other coset act by negation. Under the classical identification \(G\cong A_5\times C_2\), the rotational factor fixes \(T\), while the antipodal factor negates it.

On rational third homology, the same involution has eigenspace dimensions
\[
\boxed{\dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)^{\iota=+1}=40,
\qquad \dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)^{\iota=-1}=24.}
\]
Thus the torsion class is inversion-odd even though most rational third homology is inversion-even. No generator of \(T\) is invariant under all graph automorphisms.

## Assumptions and scope
Use the explicit twelve-vertex graph with vertices \(0,11,u_i=1+i,v_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\). Its thirty unordered edges are precisely
\[
\{\{0,u_i\},\{11,v_i\},\{u_i,u_{i+1}\},\{v_i,v_{i+1}\},
\{u_i,v_i\},\{u_i,v_{i-1}\}:i\in\mathbb Z/5\mathbb Z\}.
\]
The matching complex has one vertex for each graph edge, with simplices the pairwise endpoint-disjoint edge sets; orientations are increasing orders of the thirty graph edges sorted lexicographically by endpoint pair. Integral homology is reduced. All finite-field homology uses the same simplicial chain complex with its empty-face augmentation. No assumption of a preferred geometric embedding is needed: \(\iota\) is defined intrinsically by distance three.

## Proof
**Integral homology from exact cancellations.** Exhaustive generation gives simplicial face counts in degrees zero through five
\[
(30,315,1400,2535,1482,125).
\]
The augmented signed chain complex has \(5888\) basis cells, including the empty face. Whenever the coefficient of a lower cell \(a\) in the boundary of an upper cell \(b\) is a unit \(\pm1\), perform the elementary integral cancellation \((a,b)\). Its Schur-complement update on remaining columns is
\[
\partial'c=\partial c-\frac{[a]\partial c}{[a]\partial b}\,\partial b
\]
for cells \(c\) of the dimension of \(b\), followed by deletion of the paired rows and columns; in the next dimension the removed \(b\)-row is deleted. This is an integral chain-homotopy equivalence (the pivot is a unit). The reproducible verifier chooses unit pivots deterministically by a sparsity cost and performs **\(2911\)** such cancellations, leaving exactly \(65\) degree-three cells and one degree-four cell, and no cells in any other degree. The surviving boundary is one nonzero integer column with \(35\) nonzero entries and gcd \(3\). Its Smith normal form is the single invariant factor \(3\), proving the integral homology formula above. The verifier starts from all simplicial faces and recomputes every pivot; no precomputed matrices or torsion assertions are inputs.

**Antipodal action in characteristic three.** The graph has six uniquely determined antipodal vertex pairs. Each matching simplex is sent to the simplex obtained by applying \(\iota\) to its graph edges, multiplied by the sign of the edge-order permutation. Over \(\mathbb F_3\), the chain complex splits exactly into \(\iota\)-even and \(\iota\)-odd subcomplexes, because \(2\) is invertible. An orbit of size two contributes one generator to each; a fixed oriented simplex contributes to the eigenspace given by its orientation sign. Exact sparse elimination gives

| Eigenspace | \(\dim C_4\) | \(\operatorname{rank}\partial_4\) | \(\operatorname{rank}\partial_5\) | \(\dim H_4(-;\mathbb F_3)\) |
| --- | ---: | ---: | ---: | ---: |
| \(\iota=+1\) | 741 | 686 | 55 | 0 |
| \(\iota=-1\) | 741 | 670 | 70 | 1 |

Thus \(\widetilde H_4(X;\mathbb F_3)\) is one-dimensional and \(\iota\) acts on it by \(-1\). The universal coefficient short exact sequence in degree four is natural for graph automorphisms:
\[
0\longrightarrow \widetilde H_4(X;\mathbb Z)\otimes\mathbb F_3
\longrightarrow \widetilde H_4(X;\mathbb F_3)
\longrightarrow\operatorname{Tor}_1^{\mathbb Z}(\widetilde H_3(X;\mathbb Z),\mathbb F_3)
\longrightarrow0.
\]
The left term vanishes by the integral calculation. On the cyclic order-three group \(T\), the natural \(\operatorname{Tor}_1\) functor carries multiplication by \(\pm1\) to multiplication by the same sign. Therefore \(\iota\) negates \(T\), as claimed.

**All graph symmetries.** A complete adjacency-preserving permutation search enumerates exactly \(120\) automorphisms. Computing every pairwise commutator gives a closed subgroup of order \(60\); \(\iota\) is central and is not in that subgroup. Any action of \(G\) on a cyclic group of order three factors through a homomorphism to \(C_2\) and must kill all commutators. Because the induced action of \(\iota\) is nontrivial, its kernel is exactly \(G'\), proving the full stated torsion character.

**Rational eigenspaces.** In the same explicit \(\iota\)-eigenspace chain models over \(\mathbb F_5\), exact elimination gives third-homology dimensions \(40\) and \(24\). The integral homology has no five-primary torsion, and the order-two involution is semisimple in characteristic five. Consequently these are also the multiplicities of its \(\pm1\) eigenvalues on rational third homology. Over \(\mathbb F_3\), the corresponding third-homology dimensions are \(40\) and \(25\); the extra inversion-odd dimension records the order-three torsion.

## Verification
Run `python3 verify_icosahedral_torsion.py` using Python 3.9+ and only its standard library. The verifier reconstructs the graph from the explicit edge formula, checks its twenty triangular faces, all matching simplices, and simplicial boundary compositions; performs full integral unit-pivot cancellations; enumerates all graph automorphisms and their commutators; constructs antipodal eigenspace chain complexes; and computes every finite-field rank from sparse exact arithmetic. It prints `ICOSAHEDRAL_TORSION_ACTION_PASS` only after all asserted invariants agree. The exact reduced boundary has \(35\) nonzero entries and gcd \(3\), not merely a rank discrepancy over finite fields. Every computation is finite and exhausts its explicitly stated input domain.

## Relationship to prior work
Engström's archival work on independence complexes of claw-free graphs supplies a topological framework; \(\mathcal M(I)=\operatorname{Ind}(L(I))\), with \(L(I)\) the line graph. His connectivity results do not identify the natural action on this torsion group. Shareshian and Wachs study the homology and torsion of complete-graph matching complexes and chessboard complexes, not the icosahedral subgraph complex. Bayer, Jelić Milutinović, and Vega's outerplanar theorem and proposed planar extension concern nonequivariant homotopy types. The closest publicly recorded same-object calculation, *Three-torsion in the icosahedral matching complex: a planar counterexample*, determines the nonequivariant homotopy type \(\bigvee^{64}S^3\vee M(\mathbb Z/3,3)\), but not either antipodal eigenspace multiplicity or the torsion sign. An abstract Moore-space summand can support both degree \(+1\) and degree \(-1\) self-maps, so its nonequivariant homotopy type does **not** imply the stated sign.

## Limitations
This theorem determines the action on the unique torsion subgroup under every graph automorphism, and the rational eigenspace dimensions under antipodal inversion only. It does not classify the full \(64\)-dimensional rational representation of \(G\), the full integral free lattice, or any analogous graph family. The proof relies on independently reproducible, finite exact chain calculations and elementary homological algebra; it is not a formal proof in a theorem prover. The literature search cannot exclude an equivalent calculation in unindexed sources, and an independent scientific audit has not been conducted.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420, first public 2005-12-17, primary MSC 57M15, https://arxiv.org/abs/math/0512420 .
2. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first public 2004-09-03, https://arxiv.org/abs/math/0409054 .
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (originally submitted 2024-11-07; inspected v2), https://arxiv.org/html/2411.04601v2 .
4. *Three-torsion in the icosahedral matching complex: a planar counterexample*, public result record `28565ad1ea1a` (2026-10-11), public-result:28565ad1ea1a .
