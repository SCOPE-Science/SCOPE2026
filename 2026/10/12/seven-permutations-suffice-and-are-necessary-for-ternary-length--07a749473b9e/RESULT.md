# Seven permutations suffice and are necessary for ternary length-four shuffle coverings

## Finding
For the permutation-covering invariant \(m_k(n)\) of generalized shuffle squares, the exact value for three letters and half-length four is
\[
\boxed{m_3(4)=7}.
\]
An explicit optimal covering consists of the seven permutations, in one-line notation,
\[
1234,\quad1342,\quad2143,\quad2314,\quad2431,\quad3241,\quad3421.
\]

## Assumptions and scope
Let \(\Sigma=\{0,1,2\}\). An *even* length-eight word \(w\in\Sigma^8\) has an even number of occurrences of each symbol, including zero. For \(\pi\in S_4\), define \(w\) to be a shuffle \(\pi\)-square if its eight positions admit a partition into two increasing four-position subsequences \(U=(u_1,u_2,u_3,u_4)\) and \(V=(v_1,v_2,v_3,v_4)\) such that either \(u_j=v_{\pi(j)}\) for all \(j\in\{1,2,3,4\}\), or \(v_j=u_{\pi(j)}\) for all such \(j\). The number \(m_3(4)\) is the smallest cardinality of a set \(P\subseteq S_4\) for which every even \(w\in\Sigma^8\) is a shuffle \(\pi\)-square for some \(\pi\in P\). A permutation such as `1342` means \(\pi(1)=1,\pi(2)=3,\pi(3)=4,\pi(4)=2\).

## Proof
**Inversion reduction.** Shuffle \(\pi\)-similarity is unchanged when \(\pi\) is replaced by \(\pi^{-1}\), because the defining equality can be read with \(U\) and \(V\) interchanged. Therefore the \(24\) permutations fall into exactly \(17\) inverse-equivalence classes. Write each class using its lexicographically smallest one-line representative.

**Lower bound.** Each row below gives an even ternary word and *all* inverse-class representatives whose shuffle neighborhoods contain that word. They are computed directly from the definition by checking all \(\binom{8}{4}=70\) position choices and both directions; `verify.py` recomputes each neighborhood without consulting the table.

| Even word | Complete set of permitted inverse-class representatives |
| --- | --- |
| `00001122` | `1234`, `2134` |
| `00001221` | `1243`, `2143` |
| `00011022` | `1324`, `2314` |
| `00011220` | `1342`, `2341` |
| `00012210` | `1432`, `2431` |
| `01221000` | `3214`, `3241` |
| `01222210` | `3421`, `4231`, `4321` |

The seven displayed neighborhood sets are pairwise disjoint. Every covering family must choose at least one inverse class from each row. Consequently \(m_3(4)\ge7\), with no assumption about how other words are covered.

**Upper bound.** Take the seven permutations stated in the finding. Relabeling the alphabet preserves shuffle \(\pi\)-similarity, so it suffices to check one even word from each alphabet-relabeling class. Normalize symbols to \(0,1,2\) in their order of first appearance. There are exactly \(274\) such classes: one using one symbol; \(\binom82+\frac12\binom84=63\) using two symbols; and \(\frac{8!}{2!\,2!\,4!\,2!}=210\) using three symbols. These exhaust all even length-eight words because their positive letter multiplicities are even.

The following table gives the number of *previously uncovered* normalized words handled by each successive chosen permutation; the totals add to \(274\):

| Chosen permutation | Newly covered | Cumulative covered |
| --- | ---: | ---: |
| `1234` | 104 | 104 |
| `1342` | 76 | 180 |
| `2143` | 29 | 209 |
| `2314` | 34 | 243 |
| `2431` | 18 | 261 |
| `3241` | 9 | 270 |
| `3421` | 4 | 274 |

Every entry is reproducible from the direct predicate in `verify.py`, which checks all \(70\) choices of subsequence positions per word and permutation. Thus all \(274\) relabeling classes, and hence every even ternary length-eight word, are covered. It follows that \(m_3(4)\le7\). Combining both directions proves \(m_3(4)=7\).

## Verification
Run `python3 verify.py` using Python's standard library only. It enumerates all \(3^8=6561\) labeled words, filters to \(1641\) even words, independently constructs their \(274\) canonical relabeling classes, verifies the seven-permutation cover on both the canonical and full labeled universes, and recomputes the exact inverse-class neighborhood of each of the seven lower-bound witnesses. Its expected last line is:

```text
VERIFY_OK k=3 n=4 m=7 even_words=1641 canonical=274 inversion_classes=17 lower_witnesses=7
```

The proof is a finite complete enumeration with explicit lower and upper certificates, not an inference about unbounded word lengths.

## Relationship to prior work
Grytczuk, Pawlik and Pleszczyński defined \(m_k(n)\) and proved \(m_2(2)=2\), \(m_3(3)=5\), and \(m_4(4)=14\) in *Variations on shuffle squares* (2023), §2.4 and Proposition 2. Their table of canonical words treats the diagonal case \(k=n=3\), not the present off-diagonal invariant \(m_3(4)\). Their general linear-covering conjecture does not imply this exact value. The explicit seven-element cover and seven pairwise-disjoint neighborhood witnesses give a sharp finite answer beyond their listed cases.

The subsequent paper *More Variations on Shuffle Squares* (2023) studies constraint-graph and cutting-distance variations rather than asserting this minimum permutation covering number in its accessible abstract. A related 2025 article focuses on the graph structure of binary shuffle squares; its abstract likewise does not assert this value. Neither abstract substitutes for inspection of inaccessible full text, which remains a literature-priority limitation.

## Limitations
This result determines only \(m_3(4)\): it does not prove any all-length linear bound, determine \(m_3(n)\) for \(n>4\), classify all minimum covering sets, or establish universal dihedral-shuffle coverage. The computations verify a finite exhaustive statement. A missed equivalent theorem in an unindexed paper, inaccessible relevant passage, or unpublished work remains a residual originality risk; no independent audit is claimed.

## References
1. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first public 2023-08-26), especially §2.4 and Proposition 2. Full lawful preprint HTML: https://arxiv.org/html/2308.13882v2.
2. J. Grytczuk, B. Pawlik and M. Pleszczyński, *More Variations on Shuffle Squares*, *Symmetry* **15** (2023), article 1982, DOI:10.3390/sym15111982 (related constraint-graph and cutting-distance questions).
3. J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and ordered nest-free graphs*, arXiv:2503.22043 (2025; related but focused on binary shuffle squares).
