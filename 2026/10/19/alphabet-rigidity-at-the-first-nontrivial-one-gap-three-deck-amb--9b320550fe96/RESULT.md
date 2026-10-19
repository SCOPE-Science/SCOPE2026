# Alphabet rigidity at the first nontrivial one-gap three-deck ambiguity

## Finding

For an arbitrary fixed alphabet \(\Sigma\) of size \(q\ge 2\), let the **one-gap three-deck** of a word retain, with multiplicity, every ordered subsequence of lengths one, two, and three whose successive selected indices differ by at least two. Two words are observationally equivalent when their complete decks agree. Let \(C_q(n)\) be the number of equivalence classes in \(\Sigma^n\).

**Theorem.** Every word of length \(3\le n\le 12\) is uniquely reconstructible. At length \(13\), precisely \(4\binom q2\) equivalence classes have cardinality two, every other class is a singleton, and **each nonsingleton pair uses exactly two distinct symbols in its combined support**. For each unordered pair of alphabet symbols there are exactly four such doubletons, obtained by relabeling the binary ambiguity pairs. Consequently

\[
C_q(13)=q^{13}-4\binom q2,
\]

and the maximum size of a zero-error one-gap three-deck reconstruction code of length \(13\) equals this number. Exactly \(2^{4\binom q2}\) distinct maximum *labeled* codebooks exist (one choice from each doubleton). In particular, the four-symbol alphabet has \(67{,}108{,}840\) distinct decks, and the number of maximum codebooks is \(2^{24}\).

The length-two case is exceptional: the deck has no admissible two- or three-symbol subsequences, so any two distinct-symbol words in opposite orders are equivalent. At length one the observation is injective. The theorem does **not** assert injectivity at length two or for lengths exceeding thirteen.

## Assumptions and scope

Write \(w=w_0\cdots w_{n-1}\), with positions numbered from zero. For \(r\in\{1,2,3\}\) and \(u=(u_1,\ldots,u_r)\in\Sigma^r\), define

\[
N_w(u)=\#\{(i_1,\ldots,i_r):0\le i_1<\cdots<i_r<n,\ i_{j+1}-i_j\ge2,\ w_{i_j}=u_j\}.
\]

The deck is the full vector \((N_w(u))_{1\le |u|\le3}\), not merely the set of observed subsequences or the exact-length-three deck. Alphabet symbols are labeled; codebooks are subsets of \(\Sigma^{13}\). The enumerated base case involves exactly three symbolic letters and words of lengths at most thirteen; the extension to any finite \(q\) is a mathematical projection argument rather than an extrapolation from experiments.

## Proof

**Finite ternary lemma, with exhaustive exact certificate.** For the alphabet \(\{0,1,2\}\), the one-gap three-deck map is injective at every length \(3\le n\le12\). At \(n=13\), exactly twelve unordered pairs share a deck; all twelve classes have size two, and each pair uses exactly two distinct letters across its two words. Each of the three two-symbol subalphabets supports exactly four of these pairs.

A standalone certificate `verify_gapped_qary.cpp` proves the finite lemma by *two complete enumerations*, rather than by random sampling. The first enumerates all \(3^n\) words at each \(1\le n\le13\) and counts each admissible one-, two-, and three-position subsequence by nested loops. The second generates all words recursively and independently updates single counts, gapped-pair counts, and gapped-triple counts. Profiles are represented by ordered arrays with \(3+9+27=39\) exact integer coordinates. Both methods sort these arrays using full lexicographic comparisons, group equal profiles, and compare the actual pairs of word indices; no hashes, floating-point tests, or truncation by search are used. The certificate checks all cardinalities, the twelve doubletons and their supports, and independently reproduces every class list. Each coordinate fits in one unsigned byte: a length-thirteen word has at most \(13\) admissible single indices, \(66\) admissible pairs, and \(\binom{11}{3}=165\) admissible triples. The certificate's arrays therefore encode exact counts without overflow.

For transparency, the incremental algorithm uses the following exact update. Before appending \(x\), let \(S_a\) be the number of occurrences of \(a\), let \(P_{ab}\) be the number of gapped pairs \((a,b)\), and let \(E_{ab}\) count those pairs whose second index is the previous last position. Denote the old final symbol by \(z\), if any. Appending \(x\) creates \(S_a-\mathbf1_{a=z}\) new pairs \((a,x)\) and \(P_{ab}-E_{ab}\) new triples \((a,b,x)\); the old coordinates persist, and the new \(E'_{ax}\) is the new pair count ending in \(x\). Direct position enumeration uses no such recurrence, making it a separate computational derivation. The output is \(C_3(13)=1{,}594{,}311\), consisting of \(1{,}594{,}299\) singleton classes and twelve doubletons.

**Reduction to arbitrary alphabets.** If \(\phi:\Sigma\to\Gamma\) is any letter-to-letter map, equality of the full decks of \(v,w\in\Sigma^n\) implies equality of the decks of \(\phi(v),\phi(w)\): for any pattern \(t\) over \(\Gamma\), its count is the sum of the counts of all patterns over \(\Sigma\) mapped to \(t\). This identity holds separately for each permitted length and preserves the position-gap condition.

Suppose distinct \(v,w\in\Sigma^n\), \(3\le n\le12\), share a deck. At a position where they differ, map the two letters to \(0\) and \(1\), and every other letter to \(2\). Their ternary images remain distinct while having equal decks, contradicting the finite ternary lemma.

Now suppose \(v\ne w\in\Sigma^{13}\) share a deck and their *combined* alphabet contains three different letters. Choose two letters \(a\ne b\) that occur opposite one another at a differing position and a third distinct letter \(c\) occurring somewhere in either word. Map \(a\mapsto0\), \(b\mapsto1\), \(c\mapsto2\), and any remaining letters to \(0\). The resulting ternary images remain different, have the same deck, and collectively use all three symbols. This contradicts the support-two property in the finite ternary lemma. Hence all ambiguous pairs use exactly two letters. On each chosen two-letter alphabet, the ternary lemma identifies exactly four doubletons; different two-letter supports cannot coincide because singleton letter counts reveal the support. Thus there are precisely \(4\binom q2\) doubletons and no larger classes.

Finally, a zero-error code contains at most one word per observational equivalence class, with equality attained by choosing one representative from each. Every singleton is forced and every doubleton admits exactly two choices. This proves both codebook formulas. \(\square\)

## Verification

From the package directory, run `c++ -O2 -std=c++17 verify_gapped_qary.cpp -o verify_gapped_qary && ./verify_gapped_qary`. The expected final line is `PASS: two complete exact enumerators; arbitrary-alphabet reduction is mathematical.` In the verification, lengths \(3\) through \(12\) each have \(3^n\) distinct ternary profiles, and length thirteen has \(1{,}594{,}311\) profiles and twelve doubletons. The independent update derivations, full-array exact comparisons, and finite alphabet reduction are all needed for the theorem.

## Relationship to prior work

Golm, Nahvi, Gabrys, and Milenkovic introduced the gapped-deck reconstruction problem and reported the binary threshold \(G(3)=13\), together with a witness collision; their general results do not enumerate the complete ternary fibers or establish the alphabet-independent support-rigidity conclusion. A previous binary length-thirteen classification already determines the **four binary doubletons**; the binary case is prior work, not new here. Rigo, Stipulanti, and Whiteland formalized \((g,k)\)-binomial equivalence and studied complexity on Thue–Morse and Sturmian languages, rather than this complete finite-length fiber census. The present contribution is the exact ternary obstruction exclusion and the resulting **all-alphabet theorem**, not the prior binary collisions or threshold.

## Limitations

The proof is an exhaustive finite computation for one base alphabet, followed by an elementary exact alphabet-projection reduction. It does not give a hand-enumerated symbolic classification of all ternary words and does not address larger lengths, larger gaps, higher deck orders, or the design of computationally efficient encoders. The rarity of ambiguity at length thirteen does not itself imply resilience to noisy observations. Despite targeted prior-art searches, an equivalent enumeration outside indexed sources cannot be excluded. Independent expert verification remains to be performed.

## References

1. J. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first posted 2022-01-29; full text at https://arxiv.org/html/2201.12671v2 (2022).
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, ISIT 2023, https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf (2023).
