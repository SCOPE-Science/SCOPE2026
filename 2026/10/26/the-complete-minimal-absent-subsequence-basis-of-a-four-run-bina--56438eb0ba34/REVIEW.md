# Scientific review: four-run minimal absent scattered subsequences

## Correctness

**PASS.** The theorem fixes the binary alphabet and all four run lengths as positive integers. Its five unconditional and three conditional templates are verified individually to be absent and to become present after any one-symbol deletion. The exhaustive proof partitions an arbitrary absent word by number and orientation of constant runs, establishes exact subsequence-embedding inequalities in each case, and reduces every failure to one of the templates. This proves there are no missing minimal obstructions. The length polynomial and the compositions of fixed total length then follow by counting distinct templates. An independent finite enumerator based on all position subsets agrees for every quadruple with run lengths in \(\{1,2,3,4\}\); larger-run witness checks and finite-length composition counts were also performed. The finite enumerations do not substitute for the universal argument.

## Originality

**PASS, with a specifically identified residual risk.** The relevant full text of Kosche--Koß--Manea--Siemer, arXiv:2108.13968 (2021), establishes general necessary-and-sufficient conditions for minimal absent subsequences (Theorem 3.1) and a general enumeration data structure (Section 4.2), but does not give the displayed four-run symbolic basis, its five/six/eight threshold, or the full length/fixed-length spectrum. Thus general instance-wise computability is prior art; the asserted contribution is a closed family-wise formula. Searches for the exact templates, aliases such as minimal forbidden scattered subwords and forbidden subsequence antichains, and published-finding corpus records did not identify matching coverage. A published shortest-absent-subsequence Fibonacci result concerns the shortest layer rather than the whole set of minimal absent subsequences, and a previously studied alternating \((01)^k\) family covers only a special slice. Petković--Ćirić--Bogdanović (2004) studies minimal forbidden subwords, with particular attention to binary alphabets. Only its abstract was accessible: it remains a plausible uninspected source, not a source established to be non-covering. There may be an equivalent statement in that article or elsewhere.

## Mathematical value

**PASS.** Minimal absent scattered subsequences are the canonical finite antichain generating the complement of the subsequence ideal. For four-run words of arbitrarily large length, the entire antichain has at most eight members; the two interior run lengths alone control the abrupt transition among five, six, and eight. The explicit generator list is a compact exact certificate of all absent words, while the length polynomial and fixed-length distribution distinguish this result from a count based on a few examples. This is a complete classification of a natural fixed-run family, not a claim of an improved generic enumeration algorithm or a paper-sized general theorem.

## Limitations and closest sources

The positive four-run restriction is essential to the proof. The complete source comparison with the 2004 binary-alphabet paper was not possible, so novelty remains contingent on that literature risk; absent search hits alone are not a uniqueness proof. The 2021 general theorem algorithmically covers individual instances. The stated formula and its proof, rather than numerical tests, establish all-parameter correctness. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
