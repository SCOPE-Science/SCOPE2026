# Five rank-three theories of finite Brandt matrix-unit semigroups

## Finding
For each integer \(n\ge 1\), let \(B_n=\{0\}\cup\{e_{ij}:1\le i,j\le n\}\) be the finite Brandt semigroup of matrix units, with absorbing zero and multiplication
\[
e_{ij}e_{k\ell}=\begin{cases}e_{i\ell},&j=k,\\0,&j\ne k.\end{cases}
\]
Work in the *relational* first-order signature \(\{0,M\}\), with named zero, equality, and \(M(a,b,c)\) interpreted as \(ab=c\). For first-order equivalence through quantifier rank three, the complete classification is
\[
 B_m\equiv_3 B_n\quad\Longleftrightarrow\quad
 \bigl(m=n\in\{1,2,3,4\}\bigr)\ \lor\ \bigl(m\ge5\ \land\ n\ge5\bigr).
\]
There are **exactly five rank-three theories** in this family. Their smallest representatives have index-set sizes \(1,2,3,4,5\), equivalently semigroup cardinalities \(2,5,10,17,26\). The sharp stabilization threshold is index-set size five.

## Assumptions and scope
All \(n\) are positive integers. The constant \(0\) is an element of the domain and the absorbing element; it is *named*. The multiplication relation \(M\) is ternary, not a binary function symbol. Consequently, nested products are **not** available as atomic terms. Neither an inversion operation nor additional predicates are included. Two structures are \(\equiv_3\) when they agree on all sentences of quantifier rank at most three, equivalently when Duplicator wins the three-round Ehrenfeucht–Fraïssé game with the named constants respected.

For a nonzero idempotent \(z\), introduce quantifier-free abbreviations
\[
 I(z)\ :=\ (z\ne0)\wedge M(z,z,z),\qquad
 P(z,x)\ :=\ M(z,x,x)\vee M(x,z,x).
\]
When \(x=e_{ij}\ne0\) and \(z=e_{tt}\), the condition \(P(z,x)\) holds if and only if \(t=i\) or \(t=j\). In all uses of \(P\) below the covered element \(x\) is required to be nonzero, since \(P(z,0)\) is always true.

## Proof
**1. Four sharp lower boundaries.** Define these sentences (all displayed additional parentheses are logical grouping; the abbreviations \(I\) and \(P\) are quantifier-free):
\[
\begin{aligned}
\phi_1&:=\neg\exists x\,[x\ne0\wedge M(x,x,0)],\\
\phi_2&:=\exists x\,[x\ne0\wedge\forall y\,(I(y)\Rightarrow P(y,x))],\\
\phi_3&:=\exists x\,\exists y\,[x\ne0\wedge I(y)\wedge\forall z\,(I(z)\Rightarrow (P(z,x)\vee z=y))],\\
\phi_4&:=\exists x\,\exists y\,[x\ne0\wedge y\ne0\wedge\forall z\,(I(z)\Rightarrow (P(z,x)\vee P(z,y)))].
\end{aligned}
\]
Their quantifier ranks are respectively \(1,2,3,3\). The nonzero idempotents are precisely \(e_{11},\ldots,e_{nn}\). A nonzero matrix unit has at most two index endpoints; a nonzero idempotent has exactly one. Thus \(\phi_2\) means that at most two indices are needed, \(\phi_3\) means that one pair plus a singleton covers every index, and \(\phi_4\) means that two pairs cover every index. Such covers exist whenever the corresponding upper bound is met. Hence
\[
 B_n\models\phi_j\quad\Longleftrightarrow\quad n\le j,\qquad j\in\{1,2,3,4\}.
\]
For \(\phi_1\), if \(n=1\), every nonzero element is idempotent, whereas for \(n\ge2\), an off-diagonal matrix unit is nonzero and squares to zero. These four sentences distinguish the five asserted classes from one another.

**2. One game strategy for the infinite tail.** Let \(m,n\ge5\). Duplicator uses the following strategy in the three-round game between \(B_m\) and \(B_n\). On each of the first two moves, choose zero in response to zero, and otherwise choose a matrix unit so that all coordinate-index equalities among the nonzero chosen units are copied *exactly*. This is possible because at most four distinct indices appear in two units, and both index sets have at least five elements. These first two moves therefore preserve all atomic formulas.

In the third round, if the new selected element is zero or introduces at most one previously unused coordinate index, copy the entire coordinate-equality pattern exactly. At most five distinct indices are then required. The only remaining case is that the earlier two elements use four *pairwise distinct* indices and the third element uses two further distinct, previously unused indices. This case can arise on a side with at least six indices. Up to relabeling of indices, its three nonzero selected units are
\[
 x=e_{12},\qquad y=e_{34},\qquad z=e_{56}.
\]
On a side with only five available indices, respond by
\[
 x'=e_{12},\qquad y'=e_{34},\qquad z'=e_{15}.
\]
In *both* triples, the selected nonzero elements are pairwise distinct, all their pairwise products (including the three squares) are zero, and every product involving the named zero is zero. Hence the two triples have the same complete atomic diagram for equality, the constant zero, and all instances of \(M\). No third-round response requires preserving equalities of row indices with other row indices when those equalities are invisible to the atomic diagram. If the responding side also has six indices available, Duplicator may instead copy all indices exactly.

This proves that Duplicator maintains a partial isomorphism after all three rounds in either direction, hence \(B_m\equiv_3 B_n\) for all \(m,n\ge5\). Combining with Step 1 yields the classification and sharpness. \(\square\)

## Verification
Three independent reproducibility programs are included in this package. The direct finite-type recursion `verify_direct.py` computes complete atomic diagrams over the named zero and all triples, then performs full one-element-extension refinement. It gives distinct root types at indices \(1,2,3,4,5\) and identical root types at \(5,6,7\). The orbit-compressed recursion `verify_orbits.py` works with canonical equality patterns of matrix-unit coordinates and verifies equality of rank-three root types throughout \(5\le n\le14\). Both compare canonical *types*, not merely type counts. The explicit formula evaluator `verify_boundary.py` verifies all four threshold sentences through index size nine and checks the two exceptional atomic triples above. Recorded outputs are `direct_output.txt`, `orbits_output.txt`, and `boundary_output.txt`.

Finite enumeration is confirmatory and checks the sharp small cases. **The infinite tail is established by the three-round strategy in the proof**, not by extrapolation from the computations.

## Relationship to prior work
Jackson and Volkov, *The algebra of adjacency patterns: Rees matrix semigroups with reversion* (first arXiv posting 15 July 2009), investigate universal Horn/variety relationships for Rees matrix semigroups over the trivial group and unary reversion, not the exact three-round theory of finite Brandt matrix-unit semigroups. Maysami Sadr, *Morita Equivalence of Brandt Semigroup Algebras* (2012), treats Morita equivalence of associated Banach algebras; it does not identify finite first-order logical-depth classes. Gould and Quinn-Gregson, *\(\aleph_0\)-categoricity of semigroups* (2018 preprint, published 2019), classify categoricity of Brandt semigroups and describe coordinate-permutation automorphism orbits. Their Theorem 4.2 and Proposition 4.1 provide natural context for coordinate patterns but do not give the sharp finite index threshold five at relational rank three. In particular, \(\aleph_0\)-categoricity and Morita equivalence are not rank-three elementary equivalence. The cited works were compared for logical implication, not merely for matching terminology.

## Limitations
This is a theorem for Brandt semigroups over the *trivial group*, in the *zero-named ternary relational* signature. It does not classify arbitrary Brandt semigroups over nontrivial groups, finite inverse semigroups in general, semigroups in the functional multiplication signature, ranks above three, or formulas with extra predicates. Literature searches and inspection of the most closely related accessible full texts did not establish a previously published covering statement, but unindexed or older equivalent formulations remain a historical-priority risk. No independent mathematical audit has been performed.

## References
1. M. Jackson and M. V. Volkov, *The algebra of adjacency patterns: Rees matrix semigroups with reversion*, arXiv:0907.2634v1 (15 July 2009), https://arxiv.org/abs/0907.2634.
2. M. Maysami Sadr, *Morita Equivalence of Brandt Semigroup Algebras*, International Journal of Mathematics and Mathematical Sciences (2012), Article 280636, https://doi.org/10.1155/2012/280636.
3. V. Gould and T. Quinn-Gregson, *\(\aleph_0\)-categoricity of semigroups*, arXiv:1802.05703 (2018); Semigroup Forum 99 (2019), 260–292, https://doi.org/10.1007/s00233-019-10002-7.
