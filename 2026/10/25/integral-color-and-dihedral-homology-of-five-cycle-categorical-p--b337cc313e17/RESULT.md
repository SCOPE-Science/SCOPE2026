# Integral color and dihedral homology of five-cycle categorical products

## Finding

Let \(n\geq 2\), let \(G_n=C_5\times K_n\) be the *categorical* graph product, and put \(X_n=\operatorname{Ind}(G_n)\). The naturally acting group is \(S_n\times D_5\), where \(S_n\) permutes the complete-graph colors and \(D_5\) acts on the cycle positions. Write
\[
 A_n=\ker\!\left(\mathbb Z^{[n]}\xrightarrow{\text{sum}}\mathbb Z\right)
\]
for the integral augmentation lattice, and let \(\varepsilon:D_5\to\{\pm1\}\) equal \(+1\) on rotations and \(-1\) on reflections. There is an isomorphism of integral \(\mathbb Z[S_n\times D_5]\)-modules
\[
 \boxed{\widetilde H_2(X_n;\mathbb Z)\cong A_n\boxtimes\mathbb Z_{\varepsilon}.}
\]
Every other reduced integral homology group vanishes. The isomorphism is given by explicit two-color spherical cycles: if \(z_{ab}\) is the image of one fixed fundamental class of \(\operatorname{Ind}(C_5\times K_2)\) under insertion of the ordered distinct colors \(a,b\), then
\[
 z_{ab}=-z_{ba},\qquad z_{ab}+z_{bc}=z_{ac},\qquad
 \{z_{1n},\ldots,z_{n-1,n}\}\text{ is an integral basis}.
\]
For \(r\) a cycle rotation, \(s\) a reflection, \(\sigma\in S_n\), and any integer \(j\), the complete rational trace is
\[
 \operatorname{tr}\!\left((\sigma,r^js^b)\mid\widetilde H_2(X_n;\mathbb Q)\right)
 =(-1)^b\bigl(|\operatorname{Fix}_{[n]}(\sigma)|-1\bigr),\qquad b\in\{0,1\}.
\]
In particular, the rotation subgroup acts trivially, each reflection acts by negative identity, and there are no nonzero classes invariant under the whole group.

## Assumptions and scope

The graph has vertices \((i,a)\) for \(i\in\mathbb Z/5\mathbb Z\), \(a\in[n]\), and an edge from \((i,a)\) to \((j,b)\) exactly when \(i-j\equiv\pm1\pmod5\) *and* \(a\ne b\). Its independence complex contains all independent vertex subsets. This is not the Cartesian or lexicographic product. Homology is reduced simplicial homology with the indicated coefficients. No restrictions on the integer \(n\) occur beyond \(n\ge2\). The stated group is the specified natural product action; no assertion about additional abstract graph automorphisms is needed. The integral module identification depends on choosing a common orientation of the base two-sphere, hence is canonical up to simultaneous sign.

## Proof

**1. An integral spherical generator with two colors.** Order the vertices of \(C_5\times K_2\) as \(v_j=(j\bmod5,j\bmod2)\) for \(j=0,\ldots,9\), with the two colors denoted \(0,1\). The graph is the ordinary ten-cycle in this order. Its independence complex \(Y\) has \(122\) nonempty simplices and admits \(48\) elementary collapse pairs to the induced subcomplex on
\[
 \{v_0,v_1,v_3,v_4,v_6,v_7\}.
\]
Those six vertices induce precisely three disjoint graph edges, \(\{v_0,v_1\}\), \(\{v_3,v_4\}\), and \(\{v_6,v_7\}\). Their independence complex is the join of three copies of \(S^0\), hence is the boundary of an octahedron, \(S^2\). A deterministic pair-by-pair certificate is reproduced and checked in `verify.py`: among faces not in the target, take the first in decreasing cardinality and lexicographic order having a unique remaining immediate coface outside the target, remove that free pair, and repeat. The checker verifies the uniqueness condition at all \(48\) steps and equality of the final \(26\)-face subcomplex with the target. Thus the oriented octahedral fundamental cycle
\[
 \eta=(v_1-v_0)*(v_4-v_3)*(v_7-v_6)
\]
is a primitive generator of \(\widetilde H_2(Y;\mathbb Z)\cong\mathbb Z\). Here the asterisk denotes the oriented simplicial join of chains.

**2. Signs of the two-color symmetries.** Color exchange on \(Y\) sends \(v_j\) to \(v_{j+5}\), indices modulo ten. Its five vertex-orbits form a conflict graph \(C_5\): a collection of orbits can be selected as an invariant independent simplex exactly when it is an independent subset of that conflict graph. A cycle reflection \(i\mapsto-i\) with colors unchanged sends \(v_j\) to \(v_{-j}\). Its six vertex-orbits form a conflict graph \(P_6\), a path on six vertices. In either case every vertex-orbit is internally independent. For any finite simplicial complex acted on by a permutation, the signed augmented Lefschetz sum is minus the independence polynomial at \(-1\) of this orbit-conflict graph: each selected vertex-orbit contributes \(-1\), including the orientation sign of its cyclic permutation. Both independence polynomials evaluate to \(+1\): for \(C_5\), the count is \(1-5+5=1\); for \(P_6\), the recurrence \(F_m=F_{m-1}-F_{m-2}\), with \(F_0=1\), \(F_1=0\), gives \(F_6=1\). Since all reduced homology of \(Y\) is in even degree two, the resulting Lefschetz traces \(-1\) are the degrees of color exchange and reflection. Cycle rotation has order five and acts on a rank-one integral module, so its degree is \(+1\).

**3. Integral rank in every size.** Antolín Camarena and Carnero Bravo, Proposition 12 of arXiv:2307.12401, prove the nonequivariant homotopy equivalence
\[
 X_n\simeq\bigvee^{n-1}S^2\qquad(n\ge2).
\]
In particular, \(\widetilde H_2(X_n;\mathbb Z)\) is free of rank \(n-1\), and other reduced homology vanishes. This previously published topological calculation is an input, not a new claim here.

**4. Color merges and an integral basis.** Any map of color sets \(f:[n]\to[2]\) induces a simplicial map \(F_f:X_n\to Y\), sending \((i,a)\mapsto(i,f(a))\). Indeed, whenever two *different* positions are adjacent on the cycle, an independent face can use vertices at both positions only when every selected color is the same; applying \(f\) preserves this property. Vertices identified by \(f\) cause no difficulty for simplicial maps.

For ordered distinct colors \(a,b\), define \(\iota_{ab}:Y\to X_n\) by replacing binary colors \(0,1\) with \(a,b\), respectively, and set \(z_{ab}=(\iota_{ab})_*\eta\). For each \(j=1,\ldots,n-1\) use the color-merging map \(p_j:X_n\to Y\) that sends the single color \(j\) to binary color \(0\) and *every other color* to binary color \(1\). Then
\[
 (p_j)_*(z_{i,n})=\delta_{ij}\eta \qquad(1\le i,j<n).
\]
For \(i=j\) the composite is the identity on \(Y\). For \(i\ne j\) the composite factors through the full simplex on the five vertices of one binary color, so it is zero on degree-two homology. The \(n-1\) classes \(z_{i,n}\) therefore span a split free sublattice of rank \(n-1\). By Step 3 the ambient homology is free of exactly this rank, so these classes are an integral basis, not merely a rational basis.

Color swap in Step 2 shows \(z_{ba}=-z_{ab}\). Applying every \((p_j)_*\) gives
\[
 (p_j)_*z_{ab}=(\mathbf1_{a=j}-\mathbf1_{b=j})\eta.
\]
As the coordinate maps jointly identify the basis, this yields \(z_{ab}=z_{a,n}-z_{b,n}\) with \(z_{n,n}:=0\). Thus \(e_a-e_b\mapsto z_{ab}\) gives an integral augmentation-lattice isomorphism.

**5. Group action.** A color permutation \(\sigma\) sends \(z_{ab}\) to \(z_{\sigma(a),\sigma(b)}\), proving the \(S_n\) action is the permutation action on the augmentation lattice. A position rotation or reflection commutes with all inclusions \(\iota_{ab}\); by Step 2 it acts on every basis class as \(+1\) or \(-1\), respectively. This proves the integral module formula. Over \(\mathbb Q\), the trace of \(\sigma\) on \(A_n\) is its number of fixed colors minus one, giving the displayed character and invariant consequences.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It reconstructs the \(122\)-face base complex, checks each of the \(48\) relative elementary collapses, checks the color-merging property for all \(36,888\) tested face/map pairs across \(n=2,3,4,5\), independently computes the signed augmented Lefschetz traces for all \(1,520\) elements of \(S_n\times D_5\) in these sizes, and verifies the mod-two reduced Betti numbers by bitset boundary-matrix elimination. The completed run prints `C5_PRODUCT_INTEGRAL_MODULE_CHECKS_OK`. The finite tests check the foundational mechanisms; the unbounded integral statement follows from the proof above and the cited published rank theorem.

## Relationship to prior work

Antolín Camarena and Carnero Bravo determined \(X_n\simeq\bigvee^{n-1}S^2\) (Proposition 12), and their Proposition 11 treats the two-color case via cycle independence complexes. These nonequivariant results provide rank and homotopy type but do not state the joint integral \(S_n\times D_5\) module, the primitive two-color basis, or the reflection action. Their results for cycle lengths divisible by three concern different graph families and do not cover the five-cycle. The proof here uses the homotopy classification as a clearly identified input and derives the stronger symmetry information by color-merging retractions and exact orientation signs.

## Limitations

This is a top-dimensional integral homology representation theorem, not an equivariant homotopy splitting or a classification of the entire automorphism group of \(G_n\). The integral character calculation depends on a validated finite two-color collapse and the published all-\(n\) nonequivariant rank theorem. The mathematical originality comparison cannot exclude every inaccessible or unindexed source. No independent mathematical audit has been performed.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (first public version 23 July 2023), particularly Propositions 11–12, https://arxiv.org/abs/2307.12401 and https://arxiv.org/pdf/2307.12401.
2. The same authors, published version, *Homology, Homotopy and Applications* **26** (2024), https://doi.org/10.4310/HHA.2024.v26.n2.a17. This is another version of reference 1, not independent supporting literature.
