# Mathematical review

## Correctness — PASS

The deterministic formula follows from an explicit one-symbol extension identity, whose intersection is computable in both equal- and unequal-last-letter cases. The conditional \(ABA\) law is justified for any alphabet by uniform independent increments and the fact that subsets of eligible adjacent edges form forests. Orthogonal squarefree centered Bernoulli monomials yield exact moments; substituting \(q=2\) matches the previously published binary variance. The local standard-library checker verifies exact deletion output sets, all conditional distributions for enumerated lengths, and rational moments. The proof covers the full infinite domain \(q\ge2\), \(n\ge2\). The checker is not mistaken for an infinite certificate.

## Originality — PASS (with residual literature risk)

The published binary two-deletion variance and the Swart–Ferreira binary per-input run formula are known and explicitly not claimed as new. The present claim concerns a closed nonbinary variance for every alphabet size and the conditional independent-binomial law for return triples, including the fact that such randomness disappears only at \(q=2\). The complete available primary text of Swart–Ferreira was inspected in its binary derivation and does not state the nonbinary random-source variance. The Bar-Lev–Etzion–Yaakobi and Wang–Wang full-text radius-one studies address fixed-length Levenshtein balls, not the exact-two-deletion output count. Liron–Langberg concerns binary subsequence bounds and does not provide this conditional q-ary law. Multiple semantic research-record searches found the known binary case but not a dominating q-ary moments theorem. Undiscovered equivalent results remain possible; the priority assessment is not a proof of novelty.

## Mathematical value — PASS

An exact variance quantifies how strongly the size of a deletion observation set varies across codeword centers, a natural finite-block parameter for deletion-channel sphere packing and reconstruction. The nonbinary conditional law gives the entire combinatorial distribution after fixing run boundaries, rather than merely transferring a binary number. The q-ary extension is substantive: the return probability is a genuine alphabet-sensitive factor, and the cubic coefficient differs from the binary coefficient. The theorem supplies exact all-length moments for arbitrary alphabet sizes and a useful decomposition for future distributional analyses without claiming such analyses already exist.

## Scope and risks

The proof applies to independent uniform sources with exactly two deletions and counted distinct outputs. It makes no claim concerning general Levenshtein balls, arbitrary nonuniform distributions, or further deletion radii. An unlocated general q-ary deletion-sphere moment formula or an equivalent conditional-increment result is the outstanding priority risk. The archived primary sources' scope comparison is limited to the materials actually inspected.

Self-review: passed. Independent audit: not yet performed.
