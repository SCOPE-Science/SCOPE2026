# Self-review

The proof was checked in five parts. First, for infinite \(\kappa\), direct products preserve cardinality: if \(|A|=|B|=\kappa\), then \(|A\times B|=\kappa\), so the exact-cardinality frame remains directed and validates \(\mathsf{S4.2}\).

Second, Berger--Block--Löwe's control statements were checked in the source. The button \(\beta_p\) is the existence of nonzero \(p\)-torsion, the switch \(\sigma_q\) is \(q\)-divisibility of the whole group, and Lemma 3.2 states independence for arbitrary finite disjoint prime sets.

Third, the cardinal-correction step was checked carefully. Given the source-produced extension \(A\le B\), identify \(A\) with its image and apply downward Löwenheim--Skolem to \(B\) with parameter set \(A\). In the countable group language this gives \(A\subseteq C\preccurlyeq B\) with \(|C|\le\kappa\); containment of \(A\) forces \(|C|=\kappa\). As a substructure of a group, \(C\) is a subgroup.

Fourth, because every control is a first-order sentence, \(C\preccurlyeq B\) preserves the complete finite control pattern. Hence independence survives on the exact-cardinality layer, allowing direct application of the Hamkins--Löwe upper-bound theorem.

Fifth, the robustness conclusion was checked by the standard inclusion of validity sets between arbitrary valuations, adequate-language valuations, and first-order structure valuations.

The closest broader result, Saveliev--Shapirovsky Theorem 22, concerns structures of cardinality at most \(\kappa\), not exactly \(\kappa\). Its conclusion therefore does not logically subsume the present claim: a subframe restriction can validate additional modal formulas.

Self-review: passed. Independent audit: not yet performed.
