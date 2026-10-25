# Complete ternary three-mer minimum decycling-set census and sharp avoidance lengths

## Finding

For the directed ternary de Bruijn graph whose vertices are the \(27\) length-three words on \(\{0,1,2\}\), a **decycling set** is a vertex set whose removal leaves no directed cycle. There are exactly \(84\) labeled minimum decycling sets, all of cardinality \(11\). For each, let \(h\) be the maximum number of vertices in a directed path of the residual acyclic graph. Precisely \(60\) minima have \(h=6\), and precisely \(24\) have \(h=7\). Thus the sharp smallest value of \(h\) among minimum-cardinality decycling sets is \(6\).

Equivalently, each of the \(60\) optimal sets of eleven length-three patterns hits **every** ternary word of length \(9\), and some ternary word of length \(8\) avoids it. For each of the other \(24\) sets, the corresponding sharp lengths are \(10\) and \(9\). Under all six alphabet permutations together with word reversal, the \(84\) labeled sets partition into exactly **seven orbits of size \(12\)**, of which five have the better length-nine guarantee and two have length ten.

There is a compact exact obstruction test specific to this parameter: a choice of exactly one representative from each cyclic rotation class of ternary length-three words is a decycling set **if and only if** it hits all \(3\) directed two-cycles and all \(18\) directed four-cycles of the graph. This is a proved *finite classification*, not a proposed test at other orders or alphabet sizes.

## Assumptions and scope

The alphabet is exactly \(\Sigma=\{0,1,2\}\), and all words are linear unless explicitly called cyclic. Represent vertex \(abc\) by the integer \(9a+3b+c\). There is an arc \(abc\to bcd\) for each \(d\in\Sigma\); loops count as directed cycles. A rotation class means the class of a three-letter word under cyclic rotation, not under reversal. The path statistic \(h\) counts **vertices** rather than edges. The avoidance length \(h+2\) has \(h\) overlapping length-three windows, and the first guaranteed-hit length is \(h+3\).

An individual decycling set is recorded by the \(27\)-bit mask whose selected bits are exactly its removed vertices. The accompanying `min_decycling_sets.csv` contains all \(84\) masks, their eleven removed patterns, residual path lengths, guaranteed lengths and orbit numbers. `short_cycles.csv` contains the \(21\) obstruction masks. Orbit representatives, in hexadecimal vertex-mask notation and sorted with shorter guaranteed length first, are:

| Orbit | Sharp guaranteed word length | Representative | Eleven selected patterns |
| --- | ---: | --- | --- |
| 1 | 9 | `0x40321f9` | `000 010 011 012 020 021 022 111 121 122 222` |
| 2 | 9 | `0x403a1d9` | `000 010 011 020 021 022 111 120 121 122 222` |
| 3 | 9 | `0x403a5c3` | `000 001 020 021 022 101 111 120 121 122 222` |
| 4 | 9 | `0x40b25c3` | `000 001 020 021 022 101 111 121 122 201 222` |
| 5 | 9 | `0x413ae05` | `000 002 100 101 102 111 120 121 122 202 222` |
| 6 | 10 | `0x413283d` | `000 002 010 011 012 102 111 121 122 202 222` |
| 7 | 10 | `0x413a81d` | `000 002 010 011 102 111 120 121 122 202 222` |

## Proof

**1. Complete candidate reduction.** Every cyclic rotation orbit of length-three words traces a directed cycle in the de Bruijn graph: sliding from \(abc\) to \(bca\) rotates the word. There are exactly three length-one rotation classes (the constant words) and eight length-three classes. These eleven directed cycles are vertex-disjoint and jointly partition all \(27\) vertices. Every decycling set must meet each, so its size is at least \(11\). There is an eleven-vertex decycling set (any listed witness), so this lower bound is sharp. A size-eleven decycling set therefore selects *exactly one* vertex from each rotation class. The full candidate universe consists of exactly \(3^8=6561\) transversals; there are no other possible cardinality-eleven decycling sets.

**2. Exhaustive and reconstructible cyclic test.** The program `verify.py` builds the eleven rotation classes, iterates their Cartesian product, and forms the \(27\)-bit deletion mask for each choice. It independently tests acyclicity using Kahn's topological elimination algorithm on the induced graph of the remaining sixteen vertices. The queue consumes all remaining vertices exactly when the graph is a DAG. On every DAG, the recurrence \(d(v)=1+\max_{u\to v}d(u)\), with source values \(1\), computes the longest number of vertices on any directed path; topological order makes that recurrence exact. The executed exhaustive count is \(84\) acyclic cases, split into \(60\) with \(h=6\) and \(24\) with \(h=7\); the other \(6477\) candidates are cyclic. The program does not sample candidates, extrapolate from smaller cases or cap a search by a timeout.

**3. Small-cycle obstruction characterization.** The same checker enumerates circular words of periods two and four; it converts their successive length-three circular windows into directed-cycle vertex masks and retains only simple cycles. There are exactly \(3\) distinct masks of length two and \(18\) of length four. Among the \(6561\) transversals, \(5436\) leave a two-cycle intact; of the remaining transversals, \(1041\) leave a four-cycle intact; the remaining \(84\) are acyclic. The checker also applies the independent topological-cycle test to **every** candidate, verifying that these three classes exhaust the \(6561\) possibilities. Therefore meeting the \(21\) short cycles is necessary and sufficient *within the established transversal class*. The explicit masks in `short_cycles.csv` give the finite certificate.

**4. Symmetry classification.** Each of the six alphabet permutations acts on every ternary triple, and reversal acts by reversing the order of its three letters. Both operations preserve the set of decycling sets and preserve residual longest-path length; reversal reverses arcs. The checker forms every image under the resulting twelve transformations, partitions all \(84\) minima into orbits, and checks their cardinalities. Exactly seven orbits occur, all of size twelve. Five orbits have \(h=6\), two have \(h=7\), with the representatives displayed above. The CSV records every labeled member, so the classification is complete.

**5. Sharp word-length interpretation.** A ternary word of length \(n\ge3\) traces a directed walk of \(n-2\) length-three windows. It avoids a selected pattern set exactly when the walk stays in the residual graph. Because the graph is acyclic, each such walk is a simple directed path. A longest residual path on \(h\) vertices corresponds to an avoiding word of length \(h+2\); a longer avoiding word would contradict maximality of \(h\). Hence the first unavoidable word length is exactly \(h+3\). This proves sharpness for all \(84\) sets and establishes nine characters as the optimum among all minimum-cardinality sets.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. It recomputes all \(6561\) transversals, Kahn tests, the precise \(5436/1041/84\) cycle-test partition, the \(60/24\) longest-path distribution and the seven twelve-member symmetry orbits. It independently enumerates every ternary word of lengths \(8\), \(9\) and \(10\) and verifies the claimed existence or absence of avoiding words for **all** \(84\) sets. It regenerates `min_decycling_sets.csv` and `short_cycles.csv` deterministically.

The observed success line was:

`TERNARY_3MER_MDS_PASS candidates=6561 optimum=11 minima=84 latency9=60 latency10=24 symmetry_orbits=7 short_cycles=3+18`

The finite enumeration is a rigorous exhaustive certificate because Step 1 proves that all possible optimum-cardinality sets lie among precisely those \(6561\) choices. The direct word checks provide a separate implementation of the length translation but are not used to infer a theorem beyond this finite parameter.

## Relationship to prior work

Marçais, DeBlasio, and Kingsford [1] established the minimum-decycling-set/sequence-sketching framework, the importance of remaining path length, and algorithms for exploring minimum sets. Their full preprint discusses exhaustive counts for **binary** alphabets and sampled or constructed examples for the **four-symbol** DNA alphabet; its Tables 1 and 2 do not give the exact three-symbol, length-three cardinality, latency distribution, symmetry classes, or twenty-one-cycle test proved here. Those general foundations and algorithms are not claimed as new. Orenstein and colleagues [2] investigated universal hitting sets for sequencing, and Zheng, Kingsford, and Marçais [3] studied remaining-path bounds; these motivate the precise footprint/window tradeoff. The present work is a complete small-parameter classification rather than an asymptotic theorem or improved general algorithm.

## Limitations

This result concerns precisely the three-symbol alphabet and three-letter patterns. No assertion is made about all alphabet sizes, larger pattern orders, other selection mechanisms or a global optimum in a larger class of context-dependent sketching schemes. The claimed originality is limited to the combined exact ternary census, sharp length spectrum, orbit classification and short-cycle characterization. Unindexed prior computations or supplemental software could contain equivalent numbers. An independent mathematical audit has not been performed.

## References

[1] G. Marçais, D. DeBlasio, C. Kingsford, *Sketching methods with small window guarantee using minimum decycling sets*, arXiv:2311.03592, first posted 2023-11-06; *Journal of Computational Biology* 31 (2024), 597–615. https://arxiv.org/abs/2311.03592 ; https://doi.org/10.1089/cmb.2024.0544

[2] Y. Orenstein and colleagues, *Designing small universal k-mer hitting sets for improved analysis of high-throughput sequencing*, 2017.

[3] H. Zheng, C. Kingsford, G. Marçais, *Lower density selection schemes via small universal hitting sets with short remaining path length*, arXiv:2001.06550, 2020.
