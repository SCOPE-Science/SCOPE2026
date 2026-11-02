# Mathematical review

## Correctness (C): PASS

The inverse list is precisely the set of distinct parents at even-palindrome starts. Parent equality for starts \(i<j\) is equivalent to \(y_t=y_{t+k}\) for all \(i+k\le t<j+k\). Composition of the two local palindrome reflections gives period \(2s\) on their union. Adjacent starts collapse because the central equality bridges parity; starts at distance \(s\ge2\) with \(2s\mid k\) collapse because the period spans the full parent-comparison interval. Representatives of different parents are thus separated by \(s_k\). A period-\(2s_k\) two-symbol witness places a pair of adjacent marked residues at the palindrome center; selected starts every \(s_k\) are feasible and yield distinct parents by an explicit symbol-mismatch test. The bounds meet for all \(k,m,q\) in the stated domain. The finite verifier independently tests the channel, collision rule and witness, but does not substitute for proof.

## Originality (O): PASS, with specified bibliographic risk

The closest primary source is Lenz–Wachter-Zeh–Yaakobi [1,2]. Its zero-column-run upper bound for palindromic deletion spheres and exact formulas for small block lengths are strictly less specific than a sharp all-length worst-case bound. The present proof adds an arithmetic exclusion of *nonadjacent* palindrome starts at every separation satisfying \(2s\mid k\), and a matching periodic construction. Those ingredients yield the exact maximum for all \(k\), not merely a new presentation of the small-length results. Yohananov–Schwartz [3] and Sun–Ge [4] address code capacity or constructions rather than this inverse-sphere extremum. The 2026 multiple-error abstract [5] describes forward descendants after two operations. Search failures alone are not proof of uniqueness: a hidden specialization of earlier structural theory and the unavailable complete [5] text remain explicit risks.

## Value (V): PASS

The exact worst-case inverse-list size governs the ambiguity of one palindromic DNA-duplication read before any code restriction. Its sharp, length-uniform value and binary witness are mathematically natural; the divisibility-dependent spacing \(s_k\) reveals an essential structural obstruction invisible to the simple adjacent-position bound. This is a complete infinite-parameter extremal classification with direct significance for list-decoding feasibility, without pretending to establish an optimal code size.

## Literature, verification and limits

Primary full materials read: [1] arXiv:1707.00052, sphere-size section, Lemma 6, Appendix 0.A; [2] arXiv:1712.09345, Lemmas 14–15, Appendix B; [3] arXiv:2312.00394, motivation, channel definitions and coding-capacity results; [4] arXiv:2602.01151, abstract and code-bound section. The abstract of [5] arXiv:2609.00779 was checked, but its complete text was unavailable. The standalone checker enumerates 832,346 short received words and many periodic and randomized instances. The result is restricted to exactly one duplication with prescribed length. No independent scientific audit is claimed.

Self-review: passed. Independent audit: not yet performed.

## References

[1] https://arxiv.org/abs/1707.00052

[2] https://arxiv.org/abs/1712.09345

[3] https://arxiv.org/abs/2312.00394

[4] https://arxiv.org/abs/2602.01151

[5] https://arxiv.org/abs/2609.00779
