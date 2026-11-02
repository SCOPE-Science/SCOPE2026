# Nine minimal noncommutative nilpotent obstructions for full power semirings

## Finding

Let \(S\) range over **finite noncommutative nilpotent semigroups with zero**. Its full power semiring \(\mathcal P(S)\) consists of **all** subsets of \(S\), including the empty subset, with union and setwise multiplication, in the constant-free signature with two binary operations. The least possible size of \(S\) for which \(\mathcal P(S)\) has no finite equational basis is **five**. Up to semigroup isomorphism, **exactly nine** noncommutative five-element nilpotent semigroups have this property.

Eight classes are of the following form. Let \(G\) be a loopless directed graph on three generators \(a,b,c\), and define \(S_G=\{a,b,c,t,0\}\) by \(uv=t\) for precisely the directed arcs \(u\to v\) of \(G\); all other products are \(0\). With arcs read in the order `ab, ac, ba, bc, ca, cb`, the eight isomorphism types whose full power semirings are nonfinitely based are exactly

`000110, 000111, 001111, 010101, 011001, 011011, 011110, 011111`.

The ninth class is \(S_*=\{a,b,t,u,0\}\), with \(ab=t\), \(ba=u\), and every other product zero. All nine have nilpotency index three. Notably, the acyclic support graph with arcs \(a\to b\) and \(b\to c\) already gives a nonfinitely based full power semiring; a directed cycle is not necessary.

## Assumptions and scope

A semigroup \(S\) with zero is nilpotent of index \(d\) when \(S^d=\{0\}\) and \(S^{d-1}\ne\{0\}\). A finite equational basis is a finite collection of identities in the signature \(\{+,\cdot\}\) deriving all identities of \(\mathcal P(S)\). The semiring contains the empty set as an **element**, not as a distinguished constant symbol. The count nine concerns semigroup isomorphism, not labeled multiplication tables, and only **noncommutative** nilpotent semigroups are included. Nilpotent **groups** and nil semirings with different operations are outside the claim.

We use two previously proved theorems: Wang–Yin–Wang's nilpotent-semigroup criterion \(\mathcal P(S)\) finitely based if and only if the nonzero-product relational structure \(\mathbf N(S)\) has finite homomorphism duality; and Larose–Loten–Tardif's criterion that the square of its finite core dismantles to the diagonal exactly in the finite-duality case. We also use Wang–Yin–Wang's sufficient condition: if some \(x^{d-1}\ne0\), then \(\mathcal P(S)\) has a finite basis. These general results are prior work, not part of the novelty claim.

## Proof

**1. Exhaustion below five elements.** For a finite nilpotent semigroup, the power chain \(S\supsetneq S^2\supsetneq\cdots\supsetneq S^d=\{0\}\) is strictly decreasing: equality at one step would persist, contradicting nilpotence. With at most four elements, index at most four. Index two gives null multiplication, hence commutativity. Index four forces one generator, hence a commutative monogenic semigroup. At index three, if any square is nonzero then the published sufficient condition applies. Otherwise all squares vanish; nonzero products lie in the annihilator \(S^2\setminus\{0\}\). For a noncommutative semigroup of size at most four, there are at most two generators and at most one nonzero product value. Its support is therefore one directed arc between the generators (the two opposite arcs together would give a commutative semigroup). The corresponding relational template is homomorphically equivalent to a single directed edge: its homomorphism class is characterized by absence of directed walks of length two, a single finite obstruction. The published criterion proves finite basability.

**2. Reduction of five-element possibilities.** Again index two is commutative, and index five is monogenic. At index four, the power layers of a nonmonogenic five-element semigroup necessarily have sizes \(2,1,1,1\). Let \(a,b\) represent the two generators, \(c\) the nonzero second layer, and \(d\) the nonzero third layer. If a triple of generators has nonzero product, each adjacent binary product must equal \(c\). A triple with adjacent repeated generators, such as \(aab\), forces \(a^3=d\) by associativity; a triple with alternating generators, such as \(aba\), forces \(ab=ba=c\), hence the entire two-generated semigroup is commutative. The other patterns are symmetric. Thus every noncommutative index-four case has a nonzero cube and is finitely based by the published sufficient condition.

It remains to classify five-element index-three semigroups with every square zero. Their nonzero products are annihilators. There are precisely two possibilities for the number of nonzero values in \(S^2\): either one, leaving three generators, or two, leaving two generators. If there were more than two nonzero values, there would be at most one generator, contradicting noncommutativity. In the two-value case the only four generator products are \(aa,ab,ba,bb\); both squares vanish, so both mixed products must be nonzero and distinct. This gives exactly \(S_*\). Its relational structure has a bidirected-edge core, which fails finite duality; hence its full power semiring is nonfinitely based.

**3. Three-generator graph census.** In the one-value case the multiplication is exactly \(S_G\) as defined above, and is automatically associative because every product lies in \(\{0,t\}\), both annihilators. The unique nonzero product value and the zero are characteristic, so semigroup isomorphisms are precisely isomorphisms of the support digraph \(G\). All squares vanish, so \(G\) is loopless. A nonempty three-vertex loopless digraph has 15 isomorphism types. Three are symmetric and yield commutative semigroups. The other twelve yield noncommutative semigroups.

For each directed graph, compute an induced core by testing all retractions. Form its categorical square and delete an off-diagonal vertex only if some other remaining vertex dominates it in both incoming and outgoing incidences. Exhaustively search **all** such deletion orders; finite duality holds precisely if one reaches the diagonal. The results for the twelve noncommutative support graphs are:

| Finite basis? | Canonical six-bit arc strings | Count |
| --- | --- | ---: |
| Yes | `000001`, `000011`, `001010`, `001011` | 4 |
| No | `000110`, `000111`, `001111`, `010101`, `011001`, `011011`, `011110`, `011111` | 8 |

The remaining three, symmetric graph types all fail finite duality, but are excluded by the noncommutativity hypothesis. Thus there are eight cases of the graph form, plus \(S_*\), giving nine classes in total.

**4. Acyclic obstruction, independently of enumeration.** For the directed path \(a\to b\to c\), a digraph homomorphism into the path is equivalent to a height map into \(\{0,1,2\}\) increasing by one on every directed edge. Consider an odd undirected cycle whose cyclically ordered edges have alternating forward/backward directions except for one adjacent repeated direction. Its signed increments sum to one, so it has no height map. Every proper induced subgraph is a disjoint union of paths whose signed partial-sum range is at most two and therefore admits a height map. These give arbitrarily large minimal homomorphism obstructions; finite duality fails. This explains why even a support digraph with no directed cycle occurs among the nine nonfinitely based semigroups.

## Verification

Run `python3 verify.py` from the directory containing this document. The self-contained verifier enumerates the 63 nonempty labeled loopless digraphs on three vertices, reduces them to 15 isomorphism types, exhaustively searches core-square dismantlings, verifies associativity of every graph semigroup, and independently checks all 1,296 filtration-compatible labeled-layer multiplication candidates of index four. It also verifies the two-generator/two-output construction. Its expected final lines are `TOTAL_MINIMAL_NONCOMMUTATIVE_NFB_CLASSES: 9` and `VERIFY_OK`.

The finite search is **exhaustive because the proof establishes the structural forms of every relevant multiplication table**. It is not an enumeration of arbitrary five-element binary operations. Application of the previously proved finite-duality and finite-basis theorems supplies the required infinite equational conclusion; no finite table calculation alone proves nonfinite basability.

## Relationship to prior work

Wang, Yin, and Wang (arXiv:2610.01329v1, October 1, 2026) establish a complete **general decision criterion** for finite nilpotent semigroups and give a four-element noncommutative finitely based example, a four-element commutative nonfinitely based example, and a **commutative, nonnilpotent** five-element example with a two-element group ideal. They do not state the sharp noncommutative nilpotent cardinality five or the nine isomorphism-class census. Their general theorem is essential to this derivation; the finite numerical classification is not offered as a new general criterion.

Larose, Loten, and Tardif establish the core-square dismantling theorem used in the finite graph check. Jackson, Ren, and Zhao study nonfinite bases of ai-semirings and formulate the power-semiring finite-basis question, but do not enumerate these five-element nilpotent instances. The work of Wu and Zhao on **nonempty** power semirings of commutative nil-semigroups is not equivalent to the full power-semiring problem here. Earlier descriptions of three-vertex digraph homomorphism classes could imply some graph steps; no assertion of absolute historical priority for those intermediate steps is made.

## Limitations

The nine isomorphism types and the sharp threshold are derived from **existing** general theorems plus a complete small-order reduction. The result does not classify arbitrary five-element semigroups, groups, or nonnilpotent examples, and it does not produce short explicit equational bases for the four positive graph cases. Independent mathematical validation and an exhaustive historical search of all finite-semigroup tables have not been performed. Potential prior publication of the exact small-order census remains a priority risk.

## References

1. L. Wang, Q. Yin, A. Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, arXiv:2610.01329v1 (first public October 1, 2026), especially Theorem 1.1, Proposition 4.2, Corollary 4.6, Examples 4.4–4.5, and Section 7. https://arxiv.org/html/2610.01329v1
2. B. Larose, C. Loten, C. Tardif, *A Characterisation of First-Order Constraint Satisfaction Problems*, Logical Methods in Computer Science 3(4:6) (2007), arXiv:0707.2562. https://arxiv.org/abs/0707.2562
3. M. Jackson, M. Ren, X. Zhao, *Nonfinitely based ai-semirings with finitely based semigroup reducts*, Journal of Algebra 611 (2022), arXiv:2112.13918v1. https://arxiv.org/html/2112.13918v1
4. Y. N. Wu, X. Z. Zhao, *Some nil-ai-semiring varieties*, Semigroup Forum 108 (2024), 258–271, DOI:10.1007/s00233-024-10411-3.
