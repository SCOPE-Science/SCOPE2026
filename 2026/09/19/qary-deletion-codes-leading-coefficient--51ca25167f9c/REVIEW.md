# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The claimed q-ary extension was checked against the primary proof of En Gad's binary theorem, including the dense k-unique family, shared-source lemma, local bubble construction, exceptional-conflict count, bounded-witness extraction, generating-set count, and final code selection.

The only genuinely binary steps are local and admit direct q-ary replacements. First, two length-k windows of a uniform q-ary word agree with probability exactly q^{-k}, even when they overlap, so the original choice `k=2 ceil(log_2 n)+2` retains at least a 7/8 fraction of all q-ary words. Second, around an edited symbol `d`, the binary requirement that both boundary bits equal `1-d` is stronger than necessary: the proof only uses that the left and right boundary symbols are each unequal to `d`. This preserves the bubble property and the {-1,0,1} rule coordinates. Third, exceptional-alignment records replace a factor `2^d` by `q^d`. Fourth, the generating-set description replaces the edited bit in each header and at most one extra transferred bit per instruction by q-ary symbols. Since there are only O_t(R) such symbol choices for R rules, this contributes `q^{O_t(R)}` and is cancelled by a `q^{A_t}` factor in the hash range.

After these replacements, the bounded-witness lemmas are unchanged: they use only rational linear dependence, {-1,0,1} coordinates, support connectivity, and the de Bruijn path structure. Choosing `Q = Theta_t(q^{A_t} n^{2t-1} L^{B_t})` therefore preserves the `n^{2t-1}` exponent in both the witness union bound and the exceptional-conflict bound. The final largest-label-class step yields `|C| >= c_t q^n/Q`, proving the stated redundancy.

Adversarial checks considered overlapping k-windows, q-ary boundary symbols that differ from each other, insertion into a gap with no adjacent copy of the inserted symbol, run length one, whether larger q changes the rule coordinate magnitudes, whether the random-hash lemma depends on the spectrum dimension, and whether the witness-recovery instructions require more than O_t(R) unconstrained alphabet symbols. None changes the claimed asymptotics. The q-ary de Bruijn graph is larger, but the hash argument depends only on finiteness and integer linear independence, not on the number of coordinates.

The standalone verifier reports PASS. It exhaustively checks 42 small equal-window counting cases and 532 boundary-symbol choices across alphabet sizes 2 through 7. These checks support, but do not replace, the analytic proof.

## Originality

**PASS, to the best of our knowledge.** En Gad, arXiv:2609.19493v1, was inspected at theorem and proof level. The paper proves the `(2t-1) log_2 n` upper bound for binary deletion codes. Section 8 explicitly identifies codes over a fixed larger alphabet as a setting that appears to share the method's properties and asks whether the coefficient `2t-1` holds there. Thus the motivating source itself treats the nonbinary extension as open rather than covered.

Targeted searches used exact and synonymous formulations including q-ary/nonbinary deletion codes, two-deletion redundancy `3 log n`, the coefficient `2t-1`, substring-spectrum hashing, and the motivating arXiv identifier. They found existing q-ary two-deletion constructions with leading coefficient 5 and burst-deletion results, but no ordinary q-ary t-deletion theorem with the claimed `2t-1` leading coefficient. The 2024/2026 work of Ye--Sun--Yu--Ge--Elishco gives q-ary two-deletion codes with `5 log n + O(log log n)` redundancy, while Song--Cai gives earlier nonbinary two-deletion constructions at the same leading coefficient for even q. These do not imply the present existential coefficient 3 result.

The current SCOPE archive was searched by the motivating arXiv identifier, q-ary deletion terminology, substring-count terminology, and the `2t-1` claim family. No overlapping successful record was found.

No novelty is assigned to substring spectra, q-ary de Bruijn graphs, k-unique/repeat-free words, random linear hashing, the binary bounded-witness argument, or the existing q-ary deletion-code literature. The originality claim is only the q-ary transfer of the existential `2t-1` coefficient and the resulting uniform `O_t(log q)` dependence in bit redundancy.

### Residual literature risk

No specific inaccessible paper was identified as a high-probability source of prior coverage. The principal risk is near-simultaneous discovery: the motivating preprint is extremely recent and explicitly highlights the larger-alphabet question. There is also a meaningful folklore risk because, after the binary proof is decomposed into its alphabet-sensitive steps, the extension is short.

## Value

**PASS.** The result resolves an explicit open direction from a new deletion-coding theorem. It shows that the factor-of-n improvement over the greedy existential bound is not tied to binary complements: the same leading coefficient applies to every finite alphabet. For two deletions this lowers the known existential leading coefficient for fixed nonbinary alphabets from the generic 4 to 3, while currently available explicit q-ary constructions have larger leading coefficients. The uniform form also makes the alphabet-size dependence explicit: only `O_t(log q)` additional bits are needed beyond the binary leading term.

## Limitations

The construction remains existential and randomized; it does not provide efficient encoding or decoding. It does not improve the leading coefficient below `2t-1`, sharpen the `O(log log n)` correction for fixed q, or settle the exact optimal redundancy. The proof addresses ordinary adversarial deletions on equal-length codewords; specialized burst, localized, read-channel, or list-decoding models are different problems and are not subsumed by this statement.
