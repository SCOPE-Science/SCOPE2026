# Sharp minimum lengths for overlap-free binary products of up to nine squares

## Finding

Write \(m_k\) for the minimum length of an overlap-free binary word that is a concatenation of exactly \(k\) nonempty squares. Write \(c_k\) for the number of distinct words of length \(m_k\) with such a factorization. Then, for \(1\le k\le9\),

\[
(m_1,\ldots,m_9)=(2,4,6,8,14,16,18,24,48),
\]
\[
(c_1,\ldots,c_9)=(2,2,2,2,6,4,2,8,2).
\]

Moreover, each of these \(c_k\) minimum-length words admits **exactly one** factorization into \(k\) nonempty squares. In particular, the shortest overlap-free binary concatenation of nine squares has length \(48\), and the only two minimizers are

```text
001001101001011010011001011001101001011010011011
110110010110100101100110100110010110100101100100
```

which are bitwise complements. A nine-square decomposition of the first is

\[
(001)^2(10)^2(01)^2(10)^2(011001)^2(10)^2(01)^2(10)^2(011)^2.
\]

The existence of this particular decomposition and the fact that ten squares always force an overlap are established in the cited source. The **minimum-length lower bound**, classification of all minimum-length products, unique factorization of each minimizer, and full nine-entry minimum spectrum are the claims established here.

## Assumptions and scope

All words are finite, over \(\{0,1\}\). A **square** is \(uu\), where \(u\) is a nonempty word. An **overlap** is \(axaxa\), where \(a\in\{0,1\}\) and \(x\) may be empty. A word is overlap-free if it has no contiguous factor of this form. A square factorization is an **ordered sequence** of nonempty squares whose concatenation is the word; different cuts count as different factorizations. The minimum and number of minimizers concern exactly \(k\) factors, not at most \(k\) factors. Only \(1\le k\le9\) is asserted.

## Proof

We give a finite exhaustive certificate with an independently implemented second enumeration. The finite reduction and the completeness of both enumerations are proved below; the accompanying standalone program performs all indicated exact operations.

**1. Exhausting all overlap-free words.** Let \(B_0=\{\varepsilon\}\). For each \(n\ge0\), form \(B_{n+1}\) from the two one-bit extensions \(wb\) of each \(w\in B_n\), retaining an extension if and only if it has no overlap ending at its last position. For a string \(s\) of length \(N\), an overlap ending at its final position has length \(2p+1\) and period \(p\), for some integer \(p\ge1\) with \(2p+1\le N\). It is therefore present precisely when

\[
s[N-2p-1:N-p]=s[N-p-1:N].
\]

Here the intervals denote zero-based, half-open substring indices. An overlap newly introduced by appending one bit must end at that bit, since every proper prefix was already overlap-free. Consequently, by induction on \(n\), this construction enumerates every overlap-free binary word of length \(n\), once and only once. The standalone program also checks each retained/rejected extension against a separate all-start-position overlap predicate, not just the terminal condition. It exhausts \(B_n\) for \(0\le n\le48\), with \(|B_{48}|=416\).

**2. Counting all square factorizations.** Define \(F_r(s)\) to be the number of ordered factorizations of \(s\) into exactly \(r\) nonempty squares. The boundary values are \(F_0(\varepsilon)=1\), \(F_r(\varepsilon)=0\) for \(r>0\), and \(F_0(s)=0\) for nonempty \(s\). For \(r\ge1\), splitting off the uniquely determined final square gives

\[
F_r(s)=\sum_{\substack{1\le h\le |s|/2\\s[|s|-2h:|s|-h]=s[|s|-h:|s|]}}
F_{r-1}(s[0:|s|-2h]).
\]

Each term represents a distinct final cut and is neither missed nor repeated. Thus dynamic programming on increasing prefix lengths computes **exact**, not sampled, factorization counts for every word in every even-length \(B_n\) through \(n=48\). The first length \(n\) with \(F_k(s)>0\) for some \(s\in B_n\) gives \(m_k\). The number of such strings gives \(c_k\), and the values \(F_k(s)\) distinguish unique from multiple factorizations. The exhaustive computation yields the two displayed vectors. For each minimum-length word, \(F_k(s)=1\). At \(k=9\), exactly the two displayed words have positive \(F_9\), and both values equal one.

**3. Independent square-block enumeration.** A separate search first collects all overlap-free square words of length at most \(48\), exactly \(122\) of them. It starts with the empty word and, at stage \(k\), appends each such square to every surviving overlap-free product of \(k-1\) squares, discarding products with overlaps and lengths greater than \(48\). The search maintains exact multiplicities for products with multiple factorizations. Every factor in any overlap-free product must itself be overlap-free, so every admissible factorization of total length at most \(48\) appears in this enumeration. The search independently reproduces every quadruple \((m_k,c_k,\sum F_k,\max F_k)\) for \(1\le k\le9\), and both nine-square minimizers.

Finally, each asserted minimum \(m_k\) is at most \(48\), and all binary overlap-free words of every smaller length have been exhausted. Therefore no shorter word can be omitted. This closes all finite lower bounds and uniqueness claims.

## Verification

Run `python3 verify.py` in the same directory as this document. No third-party packages, external data, search databases, or network access are needed. The checked output is in `verification_output.txt`; it ends with `INDEPENDENT_BFS_AGREEMENT: PASS` and `VERIFY_OK`. This exhausts all binary overlap-free words through length \(48\), checks two equivalent overlap predicates, evaluates the factorization recurrence, and repeats the answer with a separate complete square-block breadth-first search. The source program embeds the expected table and the two length-\(48\) words as assertions.

## Relationship to prior work

Jeffrey Shallit's *Ten Squares Force an Overlap* (arXiv:2605.28570v1, first submitted May 27, 2026) proves that ten nonempty binary squares cannot concatenate to an overlap-free word and gives the first displayed length-\(48\) product of nine squares. Its finite search in Lemma 7 concerns a restricted four-block alphabet used in the proof; that table is not a complete minimum-length enumeration for unrestricted square factors. In particular, the exhibited \(48\)-letter witness supplies an upper bound, not a published all-word proof of the matching lower bound or the uniqueness statement. The present classification fills this distinct extremal-enumeration question. Related overlap-free factorization results, including the Restivo–Salemi theorem quoted in that source, provide structural background but are not used as uniqueness certificates here.

## Limitations

This is a finite exhaustive proof, with reproducibility dependent on executing the accompanying small Python program as specified, not a short analytic closed-form derivation. Its results apply only to binary words, exactly \(1\) through \(9\) square factors, and minimum-length words for the uniqueness assertion. It does not classify all longer words having \(k\) square factors or draw conclusions for larger alphabets. The source paper settles the separate ten-square exclusion. Literature searches cannot exclude every unindexed or unpublished exact enumeration; independent mathematical review has not been performed.

## References

1. Jeffrey Shallit, *Ten Squares Force an Overlap*, arXiv:2605.28570v1 (submitted 2026-05-27), https://arxiv.org/abs/2605.28570.
2. The executable `verify.py` and its exact recorded output `verification_output.txt`, included alongside this manuscript.
