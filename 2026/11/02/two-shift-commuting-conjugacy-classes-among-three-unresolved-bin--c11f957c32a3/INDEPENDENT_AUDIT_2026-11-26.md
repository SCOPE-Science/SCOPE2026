# Independent mathematical audit

## correctness

PASS

In the primary Appendix B the first three binary five-site question-mark entries are the displayed A, B, C with the same coordinate order; its surrounding text identifies the open two-to-one cases. Over the Boolean ring, (1+c+d)(d+e)=cd+(c+d+1)e verifies A=PD, and adding consecutive P outputs gives B=DP. Both directions of the stated inverse were independently checked on every one of the 128 seven-bit contexts covering their dependence, so they hold on the full shift. Equivalently, if σx_i=x_{i+1}, the rule σ^{-1}P flips x_i when (x_{i−1},x_{i+1},x_{i+2})=(1,0,1); every active flip leaves its own three trigger bits fixed, and a flip of a trigger bit for another site forces a different required trigger bit there to stay at a prohibiting value. Thus the mask is invariant and σ^{-1}P is an involution. Consequently A∘P=P∘B with P an invertible shift-commuting sliding block map. An independently written exhaustive checker confirmed both factorizations, the inverse and the conjugacy identities, and all 32 cyclic transitions per rule on X5. Temporal cycle lengths are (1,10), (1,10), (1,5), giving fifth fixed counts (1,1,6). A shift-commuting homeomorphism and its inverse preserve X5, and a dynamical conjugacy must preserve these counts. On spatial rings 1–4 the three temporal cycle spectra agree, supporting minimality for this temporal-spectrum comparison only. LEO is invariant under homeomorphic conjugacy; no LEO status or arbitrary non-shift-commuting conjugacy obstruction is inferred. Independent replay: /workspace/branches/b21bc157-3c8a-4481-b87a-c8f3e98df3fe/independent_check.py and independent_check_output.txt. The supplied verifier and recorded output are reference evidence, not the independent replay.

## originality

PASS

The Appendix B representatives and reversibility of P are established prior facts. Other indexed records contain the exact factorizations separately, so the positive A/B comparison is a direct consequence once those are combined; those records are catalogued later and do not establish prior publication of the comparison. Crucially, the complete two-class result also uses a period-five temporal obstruction separating C; the checked structural and table records do not give it or imply it from their stated invariants.

## value

PASS

The objects are a naturally specified list of unresolved cases from a published classification, and the invariant directly tests the equivalences that can transfer LEO status. Showing that two decisions coincide by conjugacy and that the third cannot be folded in by a shift-commuting conjugacy gives a concrete reduction and an exact obstruction a researcher can reuse. The claim is useful without deciding LEO or equating inequivalence with unequal LEO status.

The dated certificate retains the supplied scientific assessment, sources and limitations.
