# Review of the meet-tree orbit-polynomial theorem

## Correctness — PASS

The source's finite-meet-tree Fraïssé theorem and explicit statement that finitely generated meet substructures consist of pairwise meets provide the two needed model-theoretic facts. The proof identifies a selected subset with the black-vertex set of its finitely generated meet-tree. Every omitted vertex is a genuine branching meet (not a unary or terminal vertex), and every such decorated finite tree embeds into the relevant generic structure. Ultrahomogeneity then upgrades classification of decorated closures to classification of subset orbits. The Pólya equation splits exactly on marked versus unmarked root, excluding unmarked roots with zero or one child. Coefficients are uniquely determined by total degree. The first-arity discrepancy proof exhausts all possibilities at \(k+1\) selected vertices; the overhead bound and its full support follow from the rooted-tree degree identity and a binary comb construction. The endpoint descriptions also follow with no asymptotic or finite-search premise.

The independent-of-proof computer checks compare a cycle-index series engine against explicit unordered-tree generation, rebuild all finite meets of selected vertices, and exhaust arities one through six and subset sizes one through six. The replay returned `VERIFY_OK 740 exact coefficient and combinatorial assertions; 421 independent rooted shapes; 6 arities`. This finite replay is not a proof for unbounded sizes.

## Originality — PASS, with explicit antecedent limitations

The strongest antecedents are concrete. Kaplan, Rzepecki and Siniora (arXiv:1904.05144, §§2.11–2.19) prove the generic meet-tree and bounded-arity ultrahomogeneity, not the subset-orbit polynomial or sharp arity signature. OEIS A052300 already counts unlabelled unrestricted rooted Greg trees; therefore its numerical totals are excluded from the novelty claim. OEIS A048160 and Flight's labelled Greg-tree enumeration already refine by black and white vertex counts **when the black vertices are labelled**; that is a different group-action quotient. Hoenen, Eger and Gehrke (MOL 2017, pp. 11–21) refine labelled Greg trees by **degree of the root**, not a global child-degree cap and not subset-orbit counts for generic meet-trees. Broad and targeted published searches plus the mathematical record index did not reveal the combined globally capped subset-orbit/closure-overhead theorem or the exact single-orbit arity separation at the first possible subset size.

The residual risk is that the theorem could be an unstated straightforward corollary in the general species or oligomorphic-group literature, or explicitly recorded in unindexed work. In particular, the cycle-index technique itself is classical, and the unlimited-arity ungraded census is not new.

## Mathematical value — PASS

The invariant is the natural oligomorphic profile of the explicit homogeneous meet-tree permutation groups, refined by the number of newly generated meet-points. The classification provides an exact calculational recurrence at *every* branching bound. The sharp threshold \(k+1\) and the coefficient-one witness prove that the full sequence of orbit polynomials detects the ambient branching arity at its first logically possible point, not only eventually. The entire overhead support and the two classical endpoint families describe a meaningful interpolation between ordinary rooted trees and full binary phylogenetic shapes. The first arity witness is not a routine restatement of an existing table; it relates model-theoretic group actions to a global degree-constrained unlabelled combinatorial species.

## Scientific limits

No externally independent mathematical referee has checked the argument. Computation covers sizes at most six. There is no claim of a new sequence for unrestricted rooted Greg trees, a new Pólya multiset identity, or an explicit asymptotic formula for bounded arities. The closest antecedents are publicly identified so a subsequent audit can test possible implicit prior coverage.

Self-review: passed. Independent audit: not yet performed.
