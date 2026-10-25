# Integral symmetry and sharp twenty-four-square homology generators for two particles on complete bipartite graphs

## Finding
For every integer \(n\ge4\), let \(X_n=\operatorname{UConf}_2(|K_{3,n}|)\) be the unordered, collision-free configuration space of two points on the geometric realization of the complete bipartite graph. Let \(E_n\) be the free abelian group on the two-subsets of \(\{1,\ldots,n\}\), and let the **unsigned incidence** map \(J:E_n\to\mathbb Z^n\) send the basis element \(u_{\{i,j\}}\) to \(v_i+v_j\). There is a natural isomorphism of integral \(S_3\times S_n\)-modules
\[
H_2(X_n;\mathbb Z)\ \cong\ \operatorname{sgn}_{S_3}\boxtimes\ker J.
\]
In particular, \(H_2(X_n;\mathbb Z)\) is free of rank \(n(n-3)/2\), and its rational representation is \(\operatorname{sgn}_{S_3}\boxtimes S^{(n-2,2)}\).

In the canonical unordered deleted-product cubical model, every nonzero integral 2-cycle uses at least **24 square cells**. Equality occurs precisely for nonzero integer multiples of the alternating four-cycle chains supported on four vertices of the \(n\)-vertex part. There are exactly \(3\binom n4\) primitive minimum-support cycles up to a global sign, and these cycles generate \(H_2(X_n;\mathbb Z)\) **integrally**. No two vertex-disjoint graph cycles exist in \(K_{3,n}\), so none of these homology classes comes from a product torus of two disjoint graph cycles.

The sharp support count refers to cellular chains in this explicitly defined cubical model; it does not claim a metric-independent or singular-simplex filling norm.

## Assumptions and scope
Take disjoint vertex sets \(A=\{0,1,2\}\) and \(B=\{1,\ldots,n\}\); orient each edge \(e_{ai}\) from \(a\in A\) to \(i\in B\). Let \(D_n\) be the standard unordered deleted-product cubical model: its unordered zero-cells are pairs of distinct vertices, one-cells have an open graph edge as one factor and a nonincident vertex as the other, and two-cells comprise unordered pairs of closed edges without a common endpoint. The two-cells exist exactly for \(a\ne b\) and \(i\ne j\) and are oriented by \(e_{ai}\wedge e_{bj}\), antisymmetric when the two factors are exchanged. There are no cubical cells in dimension above two.

Define the skew matrix \(\varepsilon\) by \(\varepsilon_{01}=\varepsilon_{12}=\varepsilon_{20}=1\), \(\varepsilon_{ba}=-\varepsilon_{ab}\) and \(\varepsilon_{aa}=0\). For an integral symmetric array \(y=(y_{ij})\) with \(y_{ii}=0\) and \(\sum_{j\ne i}y_{ij}=0\) for each \(i\), set the cellular two-chain coefficients to
\[
Z(y)_{ai,bj}=\varepsilon_{ab}y_{ij}.
\]
Here \(Z(y)_{ai,bj}\) is the coefficient on the oriented square \(e_{ai}\wedge e_{bj}\) and is extended to reversed order by antisymmetry. The symmetric arrays with the stated row constraints are precisely \(\ker J\). All statements are over the integers, including generation and minimal support.

## Proof
**1. Cubical reduction and signed boundary.** The standard deleted-product strong deformation retraction for two distinct particles on a finite graph, as in Barnett–Farber, applies to this simple graph; quotienting the equivariant ordered retraction by the free particle swap yields the unordered cubical model \(D_n\simeq X_n\). Its oriented two-cell boundary is
\[
\partial(e_{ai}\wedge e_{bj})=(i,e_{bj})-(a,e_{bj})-(j,e_{ai})+(b,e_{ai}).
\]
Each term denotes a vertex/edge one-cell; orientations of edges follow the fixed left-to-right convention. No three-dimensional cubical cells exist, hence \(H_2(X_n;\mathbb Z)=\ker(\partial_2:C_2(D_n)\to C_1(D_n))\) without a further quotient.

**2. Solve all integer two-cycle equations.** Extend square coefficients \(x_{ai,bj}\) skew-symmetrically in the two edge labels, setting coefficients with \(a=b\) or \(i=j\) to zero. For any distinct right vertices \(i,j\), the coefficients of one-cells \((i,e_{bj})\) and \((j,e_{ai})\) in the cellular boundary force the row and column sums of the \(3\times3\) matrix \((x_{ai,bj})_{a,b}\) to vanish. Every zero-diagonal integer \(3\times3\) matrix whose row and column sums vanish is an **integer** multiple of \(\varepsilon\): the equations express its six off-diagonal entries as three equal cyclic entries and three opposite entries. Thus
\[
x_{ai,bj}=\varepsilon_{ab}y_{ij}.
\]
Antisymmetry of the square-factor order gives \(y_{ij}=y_{ji}\). The coefficients at left-vertex one-cells \((a,e_{bj})\) then give exactly \(\sum_{i\ne j}y_{ij}=0\) for each \(j\). Conversely these equations cause every displayed boundary coefficient to vanish. The correspondence \(y\mapsto Z(y)\) is therefore a bijection on the exact integral kernel lattices, not merely after tensoring with a field.

**3. Natural symmetry action.** Under \(\sigma\in S_3\), the antisymmetric rank-two tensor \(\varepsilon_{ab}\) is multiplied by \(\operatorname{sgn}(\sigma)\); under \(\tau\in S_n\), the unordered-pair entries \(y_{ij}\) are permuted. Edge orientations are preserved by these part-preserving graph automorphisms. This proves the asserted integral module isomorphism. Over \(\mathbb Q\), \(J\) is surjective since for any three distinct \(i,j,k\) the vector \(v_i\) equals one-half of \((v_i+v_j)+(v_i+v_k)-(v_j+v_k)\). Consequently \(\operatorname{rank}\ker J=\binom n2-n=n(n-3)/2\). The classical decomposition of the permutation representation on two-subsets into \(S^{(n)}\oplus S^{(n-1,1)}\oplus S^{(n-2,2)}\), and the fact that \(J\) maps onto the first two summands, give the rational Specht-module statement.

**4. Sharp support and all minimizers.** Regard the nonzero entries \(y_{ij}\) as weighted edges of the simple complete graph on \(B\). The zero row-sum equations imply that the support graph has no degree-one vertices. Any nonempty simple graph with at most three edges and minimum positive degree at least two must be a triangle; the triangle's three row equations force all weights zero over \(\mathbb Z\). Thus every nonzero array has at least four nonzero pair entries. Exactly four entries with no leaves necessarily form a simple four-cycle; the row equations force the four weights to alternate \(t,-t,t,-t\) for a nonzero integer \(t\). Each nonzero pair \(\{i,j\}\) appears in exactly six oriented squares, one for each of the three choices of unordered distinct \(a,b\) and the two assignments of \(i,j\). Hence the minimum number of squares is \(6\times4=24\). For each four-subset of \(B\), there are exactly three simple four-cycles, and primitive arrays occur at \(t=\pm1\), yielding \(3\binom n4\) classes up to sign.

**5. Integral generation, without rational saturation assumptions.** Every alternating four-cycle array belongs to \(\ker J\). Conversely fix \(y\in\ker J\), choose a distinguished vertex \(v\) and a second vertex \(b\), and consider any \(a\notin\{v,b\}\) with \(y_{va}\ne0\). Choose a fourth, distinct vertex \(k\). The alternating four-cycle array with entries \(+1\) at \(va,bk\) and \(-1\) at \(vb,ak\) transfers an arbitrary integer coefficient from entry \(va\) to entry \(vb\), without changing any previously cleared entry incident to \(v\). Repeating clears all entries \(va\) for \(a\ne b\). The row-sum equation at \(v\) forces the remaining entry \(vb\) to be zero. The residual array lies in the identical kernel on the remaining \(n-1\) vertices. Induction terminates at three vertices, where the integral kernel is zero. Thus the alternating four-cycles span the **whole integral** lattice \(\ker J\), proving the theorem.

Finally, two cycles in \(K_{3,n}\) would each require at least two distinct vertices in \(A\), but \(A\) has only three vertices. They cannot be vertex-disjoint, so the displayed generators are necessarily outside the particular construction by products of vertex-disjoint graph cycles.

## Verification
The accompanying standard-library program `verify.py` independently constructs all unordered cubical cells, verifies their integer boundaries, constructs all primitive quadrilateral cycles, checks that their square-cell support is 24, and computes modular boundary ranks for \(4\le n\le8\). The second-boundary ranks over odd primes agree with the uniform exact-integer kernel formula; characteristic two has one additional kernel direction, consistent with possible first-homology two-torsion. The supplemental exact Smith-form program `saturation_check.py` verifies that the quadrilateral lattices for \(n=4,5,6\) have all nonzero Smith factors equal to one, confirming integer saturation in those cases. These finite computations corroborate, but do not substitute for, the all-parameter integral proof above. Reproduce with `python3 verify.py`; its recorded output is `verify_output.txt`. For the supplemental integer Smith checks, install `requirements.txt` and run `python3 saturation_check.py`; its output is `saturation_output.txt`.

## Relationship to prior work
Barnett–Farber's two-particle deleted-product construction supplies the finite topological model. Farber–Hanbury's results for mature complete bipartite graphs determine **ordered** configuration-space Betti numbers; thus neither a numerical rank alone nor the existence of high-dimensional homology is presented as new. The result here is the precise **unordered integral equivariant lattice**, a sharp square-chain systolic bound and complete integral generation by those minimizers. Ramos–Yun study rational stable symmetry representations for **balanced** complete bipartite graphs; their results do not directly entail this fixed-three-part integral module or cubical minimal-support statement. Work allowing sinks at graph vertices studies a different configuration space and does not supply this conclusion.

## Limitations
The support minimization is relative to the canonical deleted-product cubical CW structure, not a universal singular-chain or metric statement. The theorem does not classify fundamental groups or a full homotopy type. The degree-two rational rank is in line with previously known ordered-space computations and is not claimed independently novel. A plausibly relevant 2010 dissertation on two-particle configurations of complete bipartite graphs could not be inspected in full; an equivalent integral generator statement there or in unindexed work remains a bibliographic uncertainty. No external independent audit has been performed.

## References
- K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (first public posting 2009-03-12), especially the deleted-product retraction.
- M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (first public posting 2010-05-13), especially mature complete bipartite graphs and the ordered Betti-number formula.
- E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813, especially the rational balanced-bipartite representation calculations.
- K. Barnett, 2010 dissertation concerning two-particle graph configuration spaces, Durham research repository; full text not available during this inspection.
