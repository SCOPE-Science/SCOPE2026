# Integral degree-one generation and a torsion cup product for Petersen two-particle configurations

## Finding

Let \(P=KG(5,2)\) be the Petersen graph, and let \(X=\operatorname{UConf}_2(|P|)\) be the space of two distinct unordered particles on its geometric realization. There are natural integral classes \(\alpha_8,\alpha_{10},\alpha_{11},\alpha_{12},\alpha_{13},\alpha_{14}\) forming a basis of \(H^1(X;\mathbb Z)\). The **integral cup-product map**
\[
\bigwedge\nolimits^2 H^1(X;\mathbb Z)\;\xrightarrow{\ \smile\ }\;H^2(X;\mathbb Z)
\]
is **surjective**. Although \(H^2(X;\mathbb Z)\cong\mathbb Z^5\oplus\mathbb Z/2\mathbb Z\), its entire unique torsion subgroup is attained by products of ordinary integral degree-one classes. In the basis defined below, the explicit nonzero order-two class is
\[
\boxed{\tau=-\alpha_8\smile\alpha_{10}+\alpha_8\smile\alpha_{14}+\alpha_{10}\smile\alpha_{13},\qquad 2\tau=0\ne\tau.}
\]
As \(H^k(X;\mathbb Z)=0\) for \(k\ge3\), the full positive-degree integral cohomology ring is generated in degree one. The known abstract homology groups and rational symmetry representations alone do not determine these assertions.

## Assumptions and scope

Index the ten graph vertices by the lexicographically ordered two-subsets of \(\{0,1,2,3,4\}\), numbered \(0,\ldots,9\). An edge joins two vertices if their underlying two-subsets are disjoint. Give each of the fifteen graph edges \(e_0,\ldots,e_{14}\) its lexicographic order and orientation from its smaller to its larger endpoint. The nine edges with indices \(0,1,2,3,4,5,6,7,9\) form a spanning tree. The remaining six chord edges, with indices \(8,10,11,12,13,14\), determine the standard basis of \(H^1(P;\mathbb Z)\), dual to their fundamental cycles.

The particle-sum map \(s:X\to (S^1)^6\) is obtained by collapsing the spanning tree, mapping each oriented chord once around its separate circle, then adding the images of the two unordered particles in the torus group. Define \(\alpha_i\) to be the pullback of the positive generator of the \(i\)-th circle. These classes, and their integral cup products, are independent of the particular cellular model. Their coordinate labels depend on the declared indexing.

The standard unordered discrete configuration complex \(UD_2(P)\), consisting of pairs of disjoint open graph cells, is a deformation retract of \(X\): the Petersen graph has no short cycle (girth five) and satisfies the usual two-particle subdivision condition. Equivariant deleted-product retractions and the equivalent cubical model are established in the early graph-configuration literature.

## Proof

**Cellular model.** The cells of \(UD_2(P)\) are \(45\) unordered pairs of distinct vertices, \(120\) pairs \((e,v)\) with \(v\notin e\), and \(75\) pairs \((e_i,e_j)\) with vertex-disjoint edges \(i<j\). Orient a one-cell along its graph edge and a two-cell by the ordered product of its smaller-indexed and larger-indexed graph edges. For an edge \(e_i=[a_i,b_i]\) (\(a_i<b_i\)), the boundaries are
\[
\partial_1(e_i,v)=\{b_i,v\}-\{a_i,v\},
\]
\[
\partial_2(e_i,e_j)=(e_j,b_i)-(e_j,a_i)-(e_i,b_j)+(e_i,a_j),\qquad i<j.
\]
The standalone verifier reconstructs these matrices and checks \(\partial_1\partial_2=0\). The one-skeleton is connected, so \(\operatorname{rank}\partial_1=44\).

**Exact homology and cohomology.** Write \(D=\partial_2^{\mathsf T}\), a \(75\)-by-\(120\) integer matrix. Five independent fundamental classes of product tori from disjoint pentagon pairs lie in \(\ker\partial_2\), so \(\operatorname{rank}_{\mathbb Q}D\le70\). A specified \(70\)-by-\(70\) minor of \(D\), using the row and column indices listed in `verify.py`, has determinant \(-2\); hence \(\operatorname{rank}_{\mathbb Q}D=70\). Exact Gaussian elimination modulo two gives \(\operatorname{rank}_{\mathbb F_2}D=69\). Every \(70\)-minor is therefore even, and one has absolute value two. The top determinantal divisor is exactly two, so the Smith factors of \(D\) are sixty-nine ones and one two. Hence
\[
H_1(X;\mathbb Z)\cong\mathbb Z^6\oplus\mathbb Z/2,\qquad
H_2(X;\mathbb Z)\cong\mathbb Z^5,\qquad
H^2(X;\mathbb Z)\cong\mathbb Z^5\oplus\mathbb Z/2.
\]

**Degree-one basis.** Each of the six fundamental graph cycles associated with a chord leaves at least one graph vertex unused; their spare-vertex indices in chord order are \((3,0,5,0,2,2)\). Holding a second particle at such a spare vertex while the first traverses the cycle proves that the total-motion map \(H_1(X;\mathbb Z)\to H_1(P;\mathbb Z)\) is surjective. Its source and target have the same free rank six, and the target has no torsion. Thus it induces an integral isomorphism on free parts. The six \(\alpha_i\) are therefore an integral basis of \(H^1(X;\mathbb Z)\).

**Integral cup-product certificate.** On an oriented two-cell \((e_i,e_j)\) with \(i<j\), the map \(s\) gives the standard torus cochain identity
\[
(\alpha_p\smile\alpha_q)(e_i,e_j)
=\delta_{p,i}\delta_{q,j}-\delta_{p,j}\delta_{q,i}.
\]
Let \(C\) be the \(75\)-by-\(15\) matrix collecting these evaluations for \(p<q\) among the six chord indices. This formula is obtained by pulling back exterior products on \((S^1)^6\), not by assuming a ring structure from Betti numbers. The verifier builds \(A=[D\mid C]\), an integer \(75\)-by-\(135\) matrix, and extracts the explicitly listed seventy-five columns forming a determinant-\(-1\) minor. Thus \(\operatorname{im}D+\operatorname{im}C=\mathbb Z^{75}\), exactly over the integers. Since no cellular three-cells exist,
\[
H^2(X;\mathbb Z)=\mathbb Z^{75}/\operatorname{im}D
=\operatorname{im}\big(\bigwedge\nolimits^2 H^1(X;\mathbb Z)\big),
\]
which proves integral cup-product surjectivity, including its torsion.

**An explicit nonzero torsion cup product.** Put \(\tau=-\alpha_8\smile\alpha_{10}+\alpha_8\smile\alpha_{14}+\alpha_{10}\smile\alpha_{13}\). Its cellular representative pairs to zero against each of the six product-torus cycles. Those cycles have rational span of dimension five, equal to the entire second-homology dimension, so \(\tau\) is rationally zero and therefore represents a torsion cohomology class. Modulo two, adjoining its cochain to the columns of \(D\) increases the rank from \(69\) to \(70\), proving that it is not an integral coboundary. As the entire torsion subgroup of \(H^2\) is exactly \(\mathbb Z/2\), this nonzero class has exact order two. The source dimensions and vanishing of higher cohomology establish the final ring-generation statement.

## Verification

`verify.py` uses only the Python standard library. It independently enumerates every graph vertex, edge, discrete configuration cell, signed boundary, graph fundamental cycle, product torus, and cup representative. It verifies connectivity, the chain identity, integral determinants \(-2\) and \(-1\), the modular ranks, the torus spanning rank, and both rational and mod-two nontriviality tests for \(\tau\). Run `python3 verify.py`; successful output begins `VERIFY_OK`. No floating-point arithmetic, randomized pivoting, external data file, or finite-to-infinite extrapolation is involved. The determinant certificates are reproducible from complete reconstructed matrices and declared column choices, not merely from precomputed logs.

## Relationship to prior work

Barnett and Farber (2009, `arXiv:0903.2180v1`) introduce an intersection theory and compute cup products for the **ordered** two-point configuration space, principally for **planar** graphs (especially their §8). Farber and Hanbury (2010, `arXiv:1005.2300v1`) develop ordered two-point homology for mature/non-planar graphs. Neither inspected treatment gives the present unordered Petersen **integral ring** or its degree-one torsion cup class.

The publicly indexed mathematical note *Two-particle Petersen configuration homology as an \(S_5\)-module* (opaque identifier `2bac82e0590d`) establishes the same abstract homology groups and the rational \(S_5\)-modules, which are treated as prior knowledge rather than new. Its full `RESULT.md` explicitly leaves the ring structure undetermined. Knowing an abstract \(\mathbb Z/2\)-summand in \(H^2\) does **not** show that it lies in the image of integral degree-one cup products, nor identify an explicit product attaining it. The present result adds precisely this multiplicative datum and a surjectivity certificate.

## Limitations

This theorem concerns exactly two unordered particles on the ten-vertex Petersen graph, with the explicitly indexed basis; it asserts neither a graph-family theorem nor a presentation of the braid fundamental group or equivariant multiplicative structure. It does not classify all ring relations in a minimal human-readable set; instead, the finite integral matrix \([D\mid C]\) specifies them algorithmically. The calculation supplies a self-contained exact arithmetic proof but no independent scientific validation. An equivalent computation in specialized unindexed literature remains possible, and some archival theses were available only at abstract level.

## References

1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, `arXiv:0903.2180v1` (first public 2009-03-12), especially Lemma 1.1 and §8.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, `arXiv:1005.2300v1` (first public 2010-05-13), especially §§1–2 and the mature-graph theorems.
3. *Two-particle Petersen configuration homology as an \(S_5\)-module*, publicly indexed mathematical note (2026), opaque identifier `2bac82e0590d`, `RESULT.md` §§Finding, Proof, Limitations.
