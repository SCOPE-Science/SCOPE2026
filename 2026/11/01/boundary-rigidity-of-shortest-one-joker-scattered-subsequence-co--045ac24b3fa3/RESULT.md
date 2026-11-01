# Boundary rigidity of shortest one-joker scattered-subsequence covers

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(q\ge 2\), an integer \(k\ge 1\), and one extra symbol \(\diamond\). A partial word \(w\in(\Sigma\cup\{\diamond\})^*\) with **exactly one** \(\diamond\) *covers* a target \(v\in\Sigma^k\) when some length-\(k\) scattered subsequence of \(w\) agrees with \(v\) at all ordinary symbols, while its optional selected \(\diamond\) agrees with whichever single target letter occupies that position. The value matched by the joker may differ between targets. Call \(w\) \(k\)-covering if it covers every \(v\in\Sigma^k\).

**Theorem.** The minimum length of a \(k\)-covering partial word with exactly one joker is
\[
 L(q,k)=q(k-1)+1.
\]
Every partial word attaining this minimum is, **if and only if**, of the form
\[
 w=\pi_1\pi_2\cdots\pi_t\,\diamond\,\pi_{t+1}\cdots\pi_{k-1},
 \qquad 0\le t\le k-1,
\]
where each \(\pi_i\) is a permutation of \(\Sigma\). Hence the exact number of labeled shortest covers is
\[
 C(q,k)=k(q!)^{k-1}.
\]
For \(k=1\), this reads \(w=\diamond\) and \(C(q,1)=1\).

Thus the joker cannot be placed inside any of the complete permutation rounds in a shortest cover: its position must be at one of their \(k\) boundaries.

## Assumptions and scope

The host is linear, not cyclic. A scattered subsequence uses strictly increasing distinct host positions; gaps are unrestricted. There is exactly one joker position, which represents a single arbitrary alphabet symbol per embedding, not an empty string and not an arbitrary-length string. The same joker position may match different alphabet letters in different target embeddings. The alphabet is labeled and all its symbols are distinct. The theorem holds for every \(q\ge 2\), \(k\ge 1\); it concerns covering at least once, not uniquely occurring targets.

## Proof

**1. Minimal length and exact fixed multiplicities.** The target \(a^k\) must be covered for every \(a\in\Sigma\). A single joker contributes at most one \(a\) to such an embedding, so every ordinary symbol \(a\) occurs at least \(k-1\) times in \(w\). With exactly one joker, \(|w|\ge q(k-1)+1\). Equality forces each ordinary symbol to occur **exactly** \(k-1\) times. The claimed construction realizes this length, since any target of \(k\) letters can place its first \(t\) letters in the first \(t\) permutation rounds, its next letter at the joker, and its remaining \(k-1-t\) letters in the last rounds.

**2. Pairwise balance at the joker.** Suppose \(w=x\diamond y\) has minimum length and is \(k\)-covering. Write \(c_a\) for the number of copies of \(a\) in \(x\). For distinct symbols \(a,b\), suppose \(c_a>c_b=r\). Since there are only \(r\) ordinary copies of \(b\) before the joker, any embedding of the length-\(k\) target
\[
 b^{r+1}a^{k-r-1}
\]
would need to match the last \(b\) at or after the joker. The following \(k-r-1\) copies of \(a\) would then have to come strictly after the joker and cannot use it. But the suffix has only \(k-1-c_a\le k-r-2\) copies of \(a\). Contradiction. (Here \(r\le k-2\), since \(c_a\le k-1\).) Therefore \(c_a=c_b\) for all distinct \(a,b\). For some \(t\in\{0,\ldots,k-1\}\), the prefix \(x\) has exactly \(t\) occurrences of every symbol and the suffix \(y\) exactly \(k-1-t\).

**3. Both ordinary portions are universally covered.** We prove that \(x\) is an ordinary \(t\)-universal word, meaning it contains all \(\Sigma^t\) as scattered subsequences. For \(t=0\), this is vacuous. Otherwise, suppose a target \(p\in\Sigma^t\) is absent from \(x\), and let \(a\) be the last letter of \(p\). Consider the target
\[
 p\,a^{k-t}\in\Sigma^k.
\]
In any purported embedding into \(x\diamond y\), the last letter of \(p\) must be matched at or after the joker. That letter consumes one of at most \(k-t\) possible \(a\)-positions among the joker and \(y\), while the trailing block still requires another \(k-t\) such positions strictly later. This is impossible. Thus \(x\) is \(t\)-universal. Reversing both host and targets preserves the covering property, so the identical argument shows that \(y\) is ordinary \((k-1-t)\)-universal.

**4. Ordinary minimum-length universality lemma.** If an ordinary word \(u\) over \(\Sigma\), with exactly \(s\) occurrences of each symbol, contains all \(\Sigma^s\) as scattered subsequences, then \(u\) is a concatenation of exactly \(s\) permutations of \(\Sigma\). Indeed, greedily split off the shortest prefix containing every alphabet letter, and repeat. Each complete block requires at least \(q\) letters. If the greedy splitting produces only \(r<s\) complete blocks, let \(b_i\) be the symbol whose **first appearance within block \(i\)** is its final position, and let \(c\) be a symbol missing in the terminal remainder. The target \(b_1\cdots b_rc\) is absent: greedy subsequence matching of its first \(r\) symbols reaches precisely those block endings, and there is no \(c\) afterward. Because an \(s\)-universal word contains every shorter target as well, this is a contradiction. Hence there are at least \(s\) blocks. The total ordinary length is \(qs\), so there are exactly \(s\), each of length \(q\), with no remainder; every block is a permutation. The converse is immediate by matching one letter in each permutation block. The case \(s=0\) means the empty word.

Apply the lemma to \(x\) and \(y\) from step 3. These pieces are respectively \(t\) and \(k-1-t\) permutation rounds. This proves necessity of the displayed shape; step 1 proved sufficiency.

**5. Enumeration.** There are exactly \(k\) choices of \(t\), and each of the \(k-1\) ordered length-\(q\) rounds has \(q!\) possibilities. The representations are distinct because the joker position determines \(t\) and the fixed block boundaries. Consequently \(C(q,k)=k(q!)^{k-1}\), including \(k=1\). All quantifiers and endpoint cases are covered.

## Verification

The standalone standard-library program `verify.py` independently enumerates *every* host at the lower-bound length with exactly \(k-1\) fixed occurrences of each alphabet symbol, inserts a joker in each position, and tests all \(q^k\) targets by greedy matching. It compares the exact set of universal hosts with the structural characterization and checks the count. The exhaustive parameters are \(q=2,\ 1\le k\le7\); \(q=3,\ 1\le k\le4\); \(q=4,\ 1\le k\le3\); and \(q=5,6,\ 1\le k\le2\). This is \(61{,}609\) hosts across \(18\) parameter pairs, with \(5{,}213\) covering hosts. A separately implemented dynamic-programming subsequence matcher agrees with the greedy matcher in \(1{,}625{,}493\) further cases.

Run: `python3 verify.py`. The final line is

```text
VERIFY_OK parameter_cases=18 exhaustive_hosts=61609 satisfying_hosts=5213 matcher_agreement_cases=1625493
```

These finite tests corroborate but do not replace the all-parameter proof above.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka, *Scattered Factor-Universality of Words* (2020), develop ordinary scattered-subsequence universality and arch factorization and observe the ordinary shortest length \(qk\). Their model does not admit a wildcard host symbol. Adamson, *Ranking and Unranking k-subsequence universal words* (2023), counts and ranks ordinary \(k\)-universal words and similarly does not count wildcard hosts.

Chen, Kitaev, Mütze and Sun, *On universal partial words* (first posted 2016), investigate a joker host symbol but require every target to occur **exactly once as a contiguous factor**. Their objects therefore differ from partial-word *scattered subsequence* coverage. Adamson and coauthors, *k-Universality of Regular Languages* (2023), consider existence and counting of individually universal ordinary words within regular languages, whereas a joker host here may use a different completion for each target; this is not equivalent to asking for one universal completion.

The theorem combines the two notions (joker hosts and scattered subsequence covers) into an exact minimum-length classification, using a new pairwise balance argument to force joker placement between ordinary permutation rounds. These specific structural and enumeration conclusions were not located in the examined sources. A differently named equivalent result outside the inspected literature remains possible.

## Limitations

Only one joker is permitted. The result does not classify hosts with extra ordinary symbols, multiple jokers, cyclic matching, contiguous factors, or unique-occurrence coverings. The exact count uses labeled words, not reversal or alphabet-permutation orbits. Exhaustive enumeration covers the finite ranges stated above; it is not an independent infinite-family certification. The literature comparison is necessarily bounded and does not prove absolute novelty.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1 (first posted 2020-03-10), https://arxiv.org/html/2003.04629v1 .
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (first posted 2023-04-10), https://arxiv.org/abs/2304.04583 .
3. H. Z. Q. Chen, S. Kitaev, T. Mütze, and B. Y. Sun, *On universal partial words*, arXiv:1601.06456 (first posted 2016-01-25), https://arxiv.org/html/1601.06456v4 .
4. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1 (first posted 2023-11-17), https://arxiv.org/abs/2311.10658 .
