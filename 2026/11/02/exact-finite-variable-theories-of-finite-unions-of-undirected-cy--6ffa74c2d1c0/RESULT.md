# Exact finite-variable theories of finite unions of undirected cycles

## Finding

Let \(G,H\) be nonempty finite simple undirected graphs in which every vertex has degree two. For each integer \(n\ge3\), let \(c_G(n)\) denote the number of components of \(G\) isomorphic to the cycle \(C_n\). Write \(G\equiv_{\mathrm{FO}^{k}}H\) when \(G\) and \(H\) satisfy the same counting-free first-order sentences using at most \(k\) reusable variable symbols, allowing arbitrary quantifier depth. Then:

1. Every pair \(G,H\) is \(\mathrm{FO}^{1}\)-equivalent.
2. \(G\equiv_{\mathrm{FO}^{2}}H\) if and only if both graphs are \(C_3\), or neither is \(C_3\).
3. For every integer \(k\ge3\),
   \[
   G\equiv_{\mathrm{FO}^{k}}H\quad\Longleftrightarrow\quad
   \min(c_G(n),k)=\min(c_H(n),k)\text{ for every }n\ge3.
   \]

Each class at width \(k\ge3\) has a unique smallest member up to isomorphism: the graph containing precisely \(\min(c_G(n),k)\) copies of \(C_n\) for each \(n\ge3\). The variable hierarchy is strict at every width: \(\mathrm{FO}^{k+1}\) distinguishes some graphs equivalent in \(\mathrm{FO}^{k}\).

## Assumptions and scope

Graphs are nonempty, finite, undirected, loopless, and without multiple edges, in a relational signature containing only binary adjacency and equality. Every vertex has degree exactly two. No extra unary predicates, constants, orientation, order, counting quantifiers, or restrictions on quantifier rank are present. A graph satisfying the degree condition is a finite disjoint union of simple cycles of lengths at least three.

## Proof

**One variable.** On any one-variable assignment, the only available atomic formulas are equality of the variable to itself (true) and its self-adjacency (false). Quantification over a nonempty domain never distinguishes the graphs. Induction on formulas proves assertion 1.

**Two variables.** \(C_3\) is complete and every other finite two-regular graph is noncomplete. The sentence \(\forall x\forall y\,(x=y\lor E(x,y))\) therefore separates the two classes. If the graph is not \(C_3\), each vertex has a distinct neighbor and also a distinct nonneighbor. Duplicator maintains the equality and adjacency relation between the two active pebbles and can answer any move in an arbitrarily long two-pebble game by selecting the required one of three responses: the same vertex, an adjacent distinct vertex, or a nonadjacent distinct vertex. This proves assertion 2.

**Defining exact cycle lengths with three variables.** Let \(D_r(x,y)\) express existence of an adjacency walk of length at most \(r\) from \(x\) to \(y\), where \(D_0(x,y)\) is \(x=y\) and
\[
D_{r+1}(x,y):=D_r(x,y)\lor\exists z\,(E(x,z)\land D_r(z,y)).
\]
Every \(D_r\) uses only three reusable variable names. To expand the recursive occurrence, systematically alpha-rename its bound variable to the name currently not free in that occurrence. Define \(\Delta_r(x,y):=D_r(x,y)\land\neg D_{r-1}(x,y)\) for \(r\ge1\). Thus \(\Delta_r\) means distance exactly \(r\).

For \(d\ge2\), set
\[
P_{2d}(x):=\exists y\,\Delta_d(x,y)\land
\forall y\forall z\,((\Delta_d(x,y)\land\Delta_d(x,z))\to y=z).
\]
For \(d\ge1\), set
\[
P_{2d+1}(x):=\exists y\exists z\,(y\ne z\land\Delta_d(x,y)\land\Delta_d(x,z))\land\neg\exists y\,\Delta_{d+1}(x,y).
\]
Parentheses enclose the entire displayed conjunctions. These formulas also use only three variable names: bound variables in a distance subformula may locally shadow names from an enclosing formula after capture-avoiding renaming. In a cycle of length \(m\), the layer at distance \(r\) from a vertex is empty when \(r>\lfloor m/2\rfloor\), consists of one vertex exactly when \(m=2r\), and otherwise consists of two vertices when \(1\le r\le\lfloor m/2\rfloor\). It follows that \(P_n(x)\) holds exactly for vertices in components isomorphic to \(C_n\).

For \(n\ge3\) and \(1\le s\le k\), the sentence
\[
\exists x_1\cdots\exists x_s\left(
\bigwedge_i P_n(x_i)\ \land\
\bigwedge_{i<j}\neg D_{\lfloor n/2\rfloor}(x_i,x_j)
\right)
\]
holds exactly when \(c_G(n)\ge s\). Vertices of a common \(C_n\) are always at distance at most \(\lfloor n/2\rfloor\); vertices in different components have no connecting walk. Each \(P_n\) and \(D_r\) can use the at-most-three variable names already among \(x_1,\ldots,x_s\) when \(s\ge3\), shadowing outer bindings only within subformulas and preserving their free endpoints. For \(s<3\) the unused names are available. Hence the complete sentence uses at most \(\max(s,3)\le k\) variable symbols. Any disagreement among truncated cycle multiplicities is therefore detected by \(\mathrm{FO}^k\), proving necessity.

**Sufficiency by a permanent pebble invariant.** Assume the truncated multiplicity profiles agree. Duplicator maintains a partial matching between the cycle components containing pebbles, pairing only equal-length cycles and retaining an isomorphism between each matched pair that respects all active pebble positions. When a pebble is lifted, forget matched components no longer holding any pebble. If Spoiler chooses a vertex in an already matched component, respond through its fixed cycle isomorphism. Otherwise select an as-yet-unmatched component of the same length, choose an isomorphism sending the new position to its response, and extend the matching. There are at most \(k-1\) occupied components before each response. If the total number of components of that length is less than \(k\), the two counts agree exactly; if the number is at least \(k\), at least one unused corresponding component remains. The strategy works symmetrically and indefinitely and preserves equality and adjacency. The finite-variable pebble-game characterization now gives \(G\equiv_{\mathrm{FO}^{k}}H\), proving sufficiency.

**Minimum representatives and sharpness.** The profile determines the minimum possible number of each component needed in an equivalence class, which is \(\min(c_G(n),k)\). The resulting disjoint union is uniquely determined up to isomorphism, and every other representative has at least as many vertices. For the width-one versus width-two boundary use \(C_3\) and \(C_4\). For width two versus three use \(C_4\) and \(C_5\). For every \(k\ge3\) use the disjoint unions of \(k\) and \(k+1\) copies of \(C_3\); they agree after truncation at \(k\), but a width-\(k+1\) sentence asserts \(k+1\) distinct triangle components. This proves strictness at every width.

## Verification

The accompanying standard-library Python programs inspect finite cycle unions without using the proof as an oracle. Run \(\texttt{python3 verify_cycle_profiles.py}\), \(\texttt{python3 verify_cycle_pebbles.py}\), and \(\texttt{python3 verify_cycle_census.py}\) in the directory containing all three scripts. Compare stdout with the corresponding \(\texttt{profile_output.txt}\), \(\texttt{pebble_output.txt}\), and \(\texttt{census_output.txt}\).

The profile checker treats all 84 multisets of zero through three cycle lengths from three to eight, a total of 1,188 vertices, and independently tests 9,504 evaluations of the length predicates. The two other programs use a joint fixed-point refinement of non-counting \(k\)-tuple types, including 570 graph-pair comparisons at widths one, two, and three, plus 10 targeted comparisons including width four. Outputs are finite cross-checks, not proofs of the all-length or unrestricted-depth statements.

## Relationship to prior work

Brown and Hoshino (2007) study Ehrenfeucht–Fraïssé games on individual paths and cycles under bounded quantifier rank. Their cycle classification varies quantifier rank while leaving the available variable set unrestricted; it is not the unbounded-depth fixed-variable classification of arbitrary disjoint cycle unions above. Grohe and Otto (2012) give general finite-variable pebble-game methods but not the specific truncated cycle-multiplicity theorem. Kotek and Makowsky (2013) give general disjoint-union composition/smoothness machinery; their investigated rank-sensitive framework is distinct from the stated uniform fixed-variable canonical profile. The proof here is elementary, and an unidentified stronger general component-composition result could imply portions of it. No priority claim beyond the documented comparisons is asserted.

## Limitations

This classification assumes every vertex has degree two and uses the pure undirected adjacency language, without counting. It does not treat paths, directed cycles, labeled or ordered graphs, or fixed-rank rather than fixed-variable equivalence. The proof is mathematical; finite checks cannot by themselves establish its unrestricted quantifier-depth assertions. Independent audit and exhaustive historical-priority verification have not been performed.

## References

- Jason Brown and Richard Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf (publisher page reports 2007-04-30).
- Martin Grohe and Martin Otto, “Pebble Games and Linear Equations,” arXiv:1204.1990 (2012-04-09); *CSL 2012*. https://arxiv.org/abs/1204.1990
- Tomer Kotek and Johann A. Makowsky, “Connection Matrices and the Definability of Graph Parameters,” arXiv:1308.3654 (2013-08-16). https://arxiv.org/abs/1308.3654
