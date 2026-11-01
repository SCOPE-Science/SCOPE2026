# Exact ternary two-deletion covering numbers through length six

## Finding

Write \(\Sigma=\{0,1,2\}\). For a word \(x\in\Sigma^n\), let \(\mathcal D_2(x)\) be the set of **distinct** length-\(n-2\) words obtained by retaining \(n-2\) positions of \(x\), in their original order. Let \(D(3,n,2)\) be the least size of \(C\subseteq\Sigma^n\) with \(\bigcup_{x\in C}\mathcal D_2(x)=\Sigma^{n-2}\).

**Theorem.** The initial nontrivial ternary two-deletion covering numbers are
\[
\bigl(D(3,4,2),D(3,5,2),D(3,6,2)\bigr)=(2,5,9).
\]
Moreover, four length-five words can cover at most \(26\) of the \(27\) possible three-letter outputs, and this one-hole bound is sharp.

For length six, a nine-word optimal covering is obtained by taking the three words `010010`, `010121`, `010202` and all their cyclic alphabet translates \(x\mapsto x+t\pmod 3\) for \(t\in\{0,1,2\}\). This covering contains nine distinct words.

## Assumptions and scope

The alphabet is **labeled**, has exactly three symbols, and deletions are of exactly two arbitrary, not necessarily adjacent, positions. Repeated embeddings of one output count once. The theorem concerns the minimum number of source words, not deletion-correcting packings or Hamming-metric covering. No assertion is made for lengths beyond six or different alphabets.

## Proof

The following upper bounds are witnessed by complete codebooks, with all words interpreted over \(\Sigma\):

| Source length | Codebook |
|---|---|
| \(4\) | `1201`, `2020` |
| \(5\) | `01010`, `12012`, `12101`, `20202`, `20212` |
| \(6\) | the nine alphabet translates of `010010`, `010121`, `010202` |

The standalone verifiers check directly that their deletion shadows cover respectively all \(9\), \(27\), and \(81\) target words.

**Length four.** One source has at most \(\binom42=6\) two-letter subsequences, fewer than \(3^2=9\). Thus at least two sources are necessary, and the displayed pair attains two.

**Length five.** If a word covers the target `aaa`, it must contain at least three instances of \(a\). Because a length-five source cannot contain three occurrences each of two different symbols, a covering of at most four sources must contain three distinct centers, one from each of
\[
M_a=\{x\in\Sigma^5:\#_a(x)\ge3\},\qquad a=0,1,2.
\]
Each \(M_a\) has exactly \(51\) members: \(\binom53 2^2+\binom54 2+1=51\). The three sets are disjoint. Thus it suffices to check the \(51^3=132651\) triples in \(M_0\times M_1\times M_2\) and all \(243\) possibilities for a fourth source.

For a target word \(y=y_1y_2y_3\), encode it by the bit indexed by \(9y_1+3y_2+y_3\). Form the 27-bit shadow mask \(s(x)\) by setting exactly the distinct descendants of \(x\). A triple \((u,v,w)\) can be completed by a fourth source if and only if the complement of \(s(u)\lor s(v)\lor s(w)\), within the 27-bit universe, is a submask of some \(s(z)\) with \(z\in\Sigma^5\). Enumerating all submasks of all 243 possible fourth-center masks gives a set of exactly \(15141\) submasks. Directly checking all \(132651\) triple complements finds **none** in that set. The independently written C++ verifier instead checks all \(32234193=51^3\cdot243\) quadruples and confirms the maximum union size is \(26\).

Sharpness of the last assertion is witnessed by `01001`, `12101`, `20202`, `10212`; their union misses only `221`. Consequently five, and not four, centers are needed, with the displayed five-center cover attaining five.

**Length six.** Define the restricted-growth equality pattern \(p(y)\) of a four-letter target by renaming the first distinct symbol \(0\), the next previously unseen symbol \(1\), and the next \(2\). Define \(g(y)\) to be the lexicographically smaller of \(p(y)\) and \(p(y^{\mathrm{rev}})\). The nonnegative integer weight \(w(y)\) depends only on \(g(y)\) as follows:

| \(g(y)\) | Number of targets | \(w(y)\) |
|---|---:|---:|
| `0000` | 3 | 2 |
| `0001` | 12 | 2 |
| `0010` | 12 | 1 |
| `0011` | 6 | 1 |
| `0012` | 12 | 2 |
| `0101` | 6 | 0 |
| `0102` | 12 | 0 |
| `0110` | 6 | 1 |
| `0112` | 6 | 1 |
| `0120` | 6 | 1 |

The complete table contains \(81\) targets and yields \(\sum_{y\in\Sigma^4}w(y)=90\). The finite shadow inequality
\[
\max_{x\in\Sigma^6}\ \sum_{y\in\mathcal D_2(x)}w(y)=11
\]
is verified exhaustively with exact integer sums by the included, independent Python and C++ programs. Each enumerates all \(3^6=729\) source words and all distinct two-deletion descendants, rather than relying on a solver optimization status. The inequality is a finite certificate (its complete weight table and verification code are part of this result).

For any covering \(C\), nonnegativity and the shadow inequality imply
\[
90=\sum_{y\in\Sigma^4}w(y)
\le\sum_{x\in C}\sum_{y\in\mathcal D_2(x)}w(y)
\le 11|C|.
\]
Hence \(|C|\ge\lceil90/11\rceil=9\). The displayed nine-center construction attains equality of the integer covering number.

## Verification

Two separately implemented verifiers are supplied: `verify_ternary_cover.py`, requiring only the Python standard library, and `verify_ternary_cover.cpp`, compilable with a C++17 compiler. Run them respectively with `python3 verify_ternary_cover.py` and `c++ -O2 -std=c++17 verify_ternary_cover.cpp -o verify_cover && ./verify_cover`. Their observed output is archived in `verification_output.txt`.

The Python checker tests each construction, enumerates the \(15141\)-element downset of all possible length-five fourth-center deletion masks, checks all \(132651\) necessary majority triples, and verifies all \(729\) length-six weighted-shadow inequalities. The independently written C++ checker enumerates \(32234193\) ordered candidate quadruples directly, without the downset reduction, as well as checking the constructions and the weight inequality. Each uses exact integer arithmetic and exhaustive finite loops. Neither is claimed to prove results outside the stated finite parameter range.

## Relationship to prior work

The relevant motivating work is Xie, Sun, and Ge (first public version June 13, 2026), which establishes large-alphabet asymptotics for general insertion/deletion coverings and explicit two-burst covering constructions. Its Section V assumes fixed length and deletion radius with alphabet size tending to infinity; the present theorem instead resolves exact small-alphabet **arbitrary** two-deletion coverings at three specific lengths. The large-alphabet theorem does not determine these integers.

Lenz, Rashtchian, Siegel, and Yaakobi (arXiv initial version November 22, 2019) develop general covering constructions and weighted lower bounds. Their Theorem 3 lower bound specializes to \(316/105\) for \((q,n,R)=(3,6,2)\), much smaller than the new sharp value \(9\). Their weighting method is a precedent, not a novelty claim; the exact finite certificate and matched construction are the contributions here. Results on binary two-deletion covering, ternary one-deletion covering, multiset deletion correction, or Hamming-metric covering are different problems and do not imply this ternary arbitrary-two-deletion profile.

## Limitations

The length-five exclusion uses a fully specified finite exhaustive certificate; there is no independent conceptual general-parameter impossibility theorem. The length-six bound uses a finite, integer-valued pattern-weight certificate and a complete check of its \(729\) source inequalities, not an infinite-parameter argument. Publication-priority comparisons are best-knowledge comparisons of inspected primary texts and indexed records; an earlier unindexed equivalent computation remains possible. There has been no independent mathematical audit.

## References

1. Chengfei Xie, Yubo Sun, Gennian Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first posted June 13, 2026. https://arxiv.org/abs/2606.15379
2. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, Eitan Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944v4 (originally November 22, 2019); IEEE Transactions on Information Theory 67 (2021), 3376–3388. https://arxiv.org/html/1911.09944v4
