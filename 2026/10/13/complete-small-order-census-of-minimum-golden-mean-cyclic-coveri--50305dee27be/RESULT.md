# Complete small-order census of minimum golden-mean cyclic covering words

## Finding
For each integer \(n\ge2\), let \(A_n\) be the set of all binary words of length \(n\) containing no adjacent `11` internally. A *cyclic covering word* of order \(n\) is a finite binary word \(c\) read cyclically so that (i) its periodic extension contains no `11`, including across the join, and (ii) the length-\(n\) cyclic windows starting at its positions together contain **every** word of \(A_n\). The target includes length-three `101`, since the target's two endpoints are not required to be mutually compatible. Covers may repeat factors; two positionally written words count as distinct if their strings differ, even when related by rotation.

The exact minimum cyclic length is \(F_{n+2}+F_n-1\), with \(F_0=0,F_1=1\) and the usual Fibonacci recurrence. The principal finding is the **complete finite census of all minimum-length cyclic covers**:

| Order \(n\) | Minimum cyclic length | Distinct labeled covers | Orbits under rotation and reversal | Orbit sizes |
|---:|---:|---:|---:|---|
| 2 | 3 | 3 | 1 | one of size 3 |
| 3 | 6 | 6 | 1 | one of size 6 |
| 4 | 10 | 20 | 1 | one of size 20 |
| 5 | 17 | 102 | 3 | three of size 34 |
| 6 | 28 | 2352 | **42** | forty-two of size 56 |

At order six there are \(21\) distinct admissible targets. Every optimal 28-bit cycle covers all 21 and repeats **exactly seven different factors one extra time each**; no factor occurs three times. Every optimal order-six cycle has minimal period 28 and has no reflection symmetry, which is equivalent to all 42 of its dihedral orbits having the full size \(2\cdot28=56\). The file `optimal_representatives.tsv` lists exactly one canonical representative per order-six orbit.

The counts and classification are **proved only for the five orders shown**. No extrapolation of this census to other orders is asserted.

## Assumptions and scope
The alphabet is `0,1`. All strings are positionally labeled, with the first bit considered position zero for enumeration. A cyclic factor of length \(n\) may cross the word boundary, with positions computed modulo the cycle length. Reversing a cycle and rotating it preserve admissibility and covering; bit complementation does **not** preserve the forbidden `11` language and is not treated as a symmetry. A canonical representative in the supplied table is selected by the smallest integer bitmask among all rotations and reversals when the first character is the least significant bit; this is not ordinary lexicographic ordering of the printed strings.

## Proof
**1. Independent length bound used to define optimality.** Form a directed overlap multigraph with as vertices the admissible \((n-1)\)-words and as edges all \(n\)-words of \(A_n\), directed from each prefix of length \(n-1\) to the corresponding suffix. Every cyclic cover corresponds to a closed directed walk traversing every edge, while this graph is strongly connected (zeros lead to the all-zero state; from there any admissible vertex can be appended).

For a vertex \(v\), its indegree is two when it starts with `0`, otherwise one; its outdegree is two when it ends with `0`, otherwise one. Each *deficit vertex* starts with `0`, ends with `1`, and has indegree one larger than outdegree. Every positive integer multiplicity augmentation making an edge-cover closed tour must send one extra unit of flow out of each deficit to a surplus vertex (which starts with `1` and ends with `0`). If a deficit begins with \(r\) zeros, any path to a surplus must first shift all those zeros out, so uses at least \(r\) edges. Summing run lengths over deficits gives \(F_n-1\): for each \(1\le k\le n-2\), precisely \(F_{n-1-k}\) deficits have at least \(k\) leading zeros. Conversely, for every deficit \(v=0^ru\), where \(u\) starts and ends with `1`, append exactly \(r\) zeros. This reaches the surplus \(u0^r\), bijectively matching all deficits and surpluses. The resulting balanced strongly connected augmented graph has an Eulerian circuit. Hence the minimum length is \(|A_n|+(F_n-1)=F_{n+2}+F_n-1\); \(n=2\) has no deficits. The formula is background for identifying exactly which cycles the census must enumerate; the originality claim here concerns the complete finite **number and orbit classification**.

**2. Exhaustive finite search.** For each of the five orders \(n=2,3,4,5,6\), fix the proved minimum length \(L\). Enumerate every binary string of length \(L\) using a recursion that branches to `0` always and to `1` only if the preceding symbol is `0`; at the leaf reject if both the first and last symbols are `1`. This visits **all and only** cyclic strings of length \(L\) avoiding `11`. For every survivor, compute exactly its \(L\) length-\(n\) cyclic windows and retain the string if and only if their set equals \(A_n\). No admissible cycle is pruned: the only early rejection is an internal `11`, which cannot be repaired by extension, and the final join check is exact.

Compute the canonical representative of each survivor under the dihedral action generated by length-\(L\) rotation and reversal; the orbit multiplicity is the number of labeled survivors having that representative. This is exhaustive because every valid cycle is constructed exactly once as a length-\(L\) labeled string, and because the finite dihedral set of transformations is explicitly traversed. The result is the complete table in the Finding section.

**3. Cross-validation of every optimizer.** Two separately written algorithms independently implement both the enumeration and dihedral quotient. One uses integer bitmasks in compiled C++; the other constructs ordinary Python strings. Their labeled cardinalities, orbit counts and orbit-size multisets agree for every order. The Python orbit canonicalization, based on lexicographic strings, was additionally shown to give precisely the same set of orbits as the 42 C++ bitmask representatives, after recanonicalization. Directly counting the length-six cyclic factors in each representative gives exactly fourteen factors once and seven factors twice, with the other seven admissible target factors present once; in other words, **every one of the 21 targets is present**, and seven are duplicated exactly once. No extraneous forbidden factor appears. Thus every claimed object is a genuine optimizer and every optimizer is included. \(\square\)

## Verification
Compile the standalone C++ checker by `g++ -O3 -std=c++17 verify_cyclic_cpp.cpp -o check_cycles` and run `./check_cycles`. It prints the canonical representatives to standard output and numerical counts for all five orders to standard error. Run `python verify_cyclic_python.py` to reconstruct the same census independently. The C++ checker uses integers and a bitmask of allowed factors, while the Python checker uses explicit string-factor sets and string-based rotations/reversals. The full order-six representative table is supplied separately as `optimal_representatives.tsv`; the numeric bitmask convention explains how to reproduce its ordering.

The checkers separately reconstruct the target language from the no-adjacent-ones rule and check the order-specific minimum lengths. A final cross-check independently recanonicalized all 42 C++ representatives with the Python group action and confirmed equality of orbit sets. These computations are exhaustive **only through order six**.

## Relationship to prior work
Wang and Shallit (1998) give the exact minimum length of a **linear** word realizing the Fibonacci subword-complexity sequence, \(F_{n+2}+F_n\), and a construction of at least one minimal example per order; they explicitly identify the complete enumeration of minimal linear words as an open question. Their theorem does not enumerate or classify shortest cyclic covering words at these orders. The numerical length relation is acknowledged, not claimed as the new result.

Moreno's de Bruijn work for a subshift (2003) and Moreno and Matamala (2007) address exact-once cycles for blocks that are admissible under periodic repetition, a **smaller** language than \(A_n\) when the endpoints are `1`. For example, `101` belongs to the current length-three target but its infinite periodic repetition is illegal. Their cycle-enumeration and lexicographic constructions are therefore not an equivalent census. Blanchet-Sadri and Lensmire (2011) discuss linear partial-word complexity and restate the Wang–Shallit length result, without an equivalent cyclic classification. All comparisons concern implications and underlying languages, not title similarity.

## Limitations
The computed optimizer classification stops at order six; no result is asserted for the number or symmetry types of optimal cycles for larger \(n\). The exact length expression is provided to certify minimality, not as a separate originality assertion. The symmetry group here contains rotations and reversal, not bit complementation. Possible unindexed datasets, separate enumerations, and an inaccessible full text of Moreno's 2005 general-language de Bruijn paper constitute residual originality risks. These files document a self-review; no independent external audit has been performed.

## References
- Ming-wei Wang and Jeffrey Shallit, *On Minimal Words With Given Subword Complexity*, Electronic Journal of Combinatorics 5 (1998), #R35; first published July 15, 1998. DOI 10.37236/1373; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v5i1r35/pdf/.
- Eduardo Moreno, *Lyndon Words and de Bruijn Sequences in a Subshift of Finite Type* (2003), article on restricted symbolic languages.
- Eduardo Moreno and Martín Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (2007), arXiv:0711.1695v1, November 12, 2007; full text: https://arxiv.org/pdf/0711.1695.
- Francine Blanchet-Sadri and John Lensmire, *On Minimal Sturmian Partial Words*, STACS 2011, pp. 225–236, DOI 10.4230/LIPIcs.STACS.2011.225; full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol009-stacs2011/LIPIcs.STACS.2011.225/LIPIcs.STACS.2011.225.pdf.

