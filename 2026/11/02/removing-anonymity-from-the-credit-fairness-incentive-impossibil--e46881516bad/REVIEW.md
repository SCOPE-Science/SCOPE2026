# Self-review

## Correctness — PASS

The statement is for labeled agents, equal endowments, five rounds, real-valued online allocations, and the original CF1–CF5. Every round of every constructed reported history has demand at least available supply. The credit identity follows directly from PE, CF1, CF2, and CF3. CF4 and CF5 then uniquely constrain truthful rounds 1, 2, and 5, while PE determines rounds 3 and 4. The two deviating histories share the first two report vectors at identical agent labels, fixing one common \(x\in[1,2]\) without relying on anonymity. Forcing the final-round allocations using CF5 proves exactly \(\Delta_A=x-1\) and \(\Delta_B=2-x\). Direct exact-rational checks replay all axioms on an illustrative 101-point grid, but analytical inequalities establish the universal claim. Risk: mechanism class assumes no information about future reports, as in the cited model; no extension to anticipating mechanisms is implied.

## Originality — PASS

The most relevant source is Zahedi–Freeman (arXiv:2601.17944v1 and v2; IJCAI 2026). Its actual theorem assumes anonymity, and both full preprint versions rely on anonymity to fix the deviator's second-round quantity. Version 2 explicitly calls removing anonymity an open question. The v1 abstract uses broader informal wording, but the v1 theorem and proof still assume anonymity; it therefore does not imply the present unrestricted conclusion. The proof here instead compares two fixed-label truthful profiles with a common deviating prefix, causing gains whose sum is one. Published research-record searches about this precise axiom system and anonymity-free impossibility, along with indexed-literature searches, identified no source implying the theorem. Residual risk: unindexed work or later updates could contain an equivalent construction; independent literature review is not performed.

## Value — PASS

This removes an explicit mathematical hypothesis from a central incentive/fairness impossibility in a recent resource-allocation paper. The two-history coupling also yields an explicit worst-profile manipulation guarantee of one-half for this witness, and the proof is constructive and short. The quantitative bound is not asserted to be globally optimal.

## Closest literature and limits

Zahedi and Freeman (2026), arXiv:2601.17944, section 4.2 and the theorem on anonymous impossibility, are the closest work; this result assumes their model and credit-fairness axioms and strengthens the quantifier over mechanisms. It does not address online-myopic strategyproofness, generalized demands/utilities, or uniqueness/optimality of the two-profile witness.

Self-review: passed. Independent audit: not yet performed.
