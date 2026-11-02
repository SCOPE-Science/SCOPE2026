# Scientific review: exact six-term zero sums modulo \(36\)

## Correctness

**PASS.** The two integer-sum classes of the displayed twelve-term witness each total \(36\), proving the lower bound. The six-subset-sum recurrence is an exact Boolean dynamic program: the appended residue either is or is not used, and descending updates prevent reuse. A branch with a forbidden six-sum remains forbidden under all extensions. The generator visits every sorted admissible multiset not pruned by this sound rule, finding exactly 23,970 bad length-twelve cases. For every such case and every admissible thirteenth residue, it verifies the existence of a forbidden six-sum. An independently implemented direct index-combination checker validates the entire emitted table and the extension assertion; thus the universal length-thirteen statement follows. Exact orbit and profile counts are independently checked from the full table. The executable sources and their finite certificate are attached. No inference from sampled inputs is used.

## Originality

**PASS, with priority uncertainty.** Sun's original article [arXiv:2606.18234] gives the definition, lower bound, and the conjectured family \(s_1(n)=2n+1\); it does not supply the exact modulus-six evaluation or the full extremal statistics. Li–Ling–Sun–Zhu [arXiv:2610.19965] treat different rank-two and unrestricted-length results, while Gao and collaborators treat prime moduli. A published exact modulus-four classification does not imply the modulus-six count. Searches for the exact threshold, alternate fixed-length zero-sum descriptions, modulo-36 subset sums, broader implications, and matching tables found no stronger source. Searches alone do not rule out unpublished, implicit, or unindexed coverage; the modulus-four record was accessible only as a published summary.

## Mathematical value

**PASS.** Modulus six is the first squarefree composite test of an explicitly posed infinite conjecture, where neither a prime-modulus result nor a prime-power computation settles the case. Besides deciding the threshold, the result exhausts its maximal counterexample configurations and reveals a strong residue-class constraint (just eleven patterns, with a 361-orbit symmetry classification). This provides a complete small-composite benchmark for the inverse version of the new zero-sum problem, not a routine restatement of a general bound. It is finite and has no claimed implication for arbitrary moduli.

## Closest literature and limitations

Zhi-Wei Sun, *On zero-sum problems of two new types* (2026), arXiv:2606.18234; Yang Li, San Ling, Zhonghua Sun, and Shixin Zhu, *Proofs and disproofs of some conjectures on zero-sum problems of new types* (2026), arXiv:2610.19965; Gao et al., *A new problem from zero-sum theory* (2026); published exact modulus-four result. The remaining risk is undetected earlier numerical or theoretical coverage. The standalone certificate proves only its stated finite modulus-six classification. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
