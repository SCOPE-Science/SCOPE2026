# Four forcing spectra among shortest five-letter crucial Abelian-square-free words

## Finding
Let \(\Sigma=\{0,1,2,3,4\}\). A word is **right-crucial Abelian-square-free** if it contains no contiguous Abelian square but appending any letter of \(\Sigma\) creates one. A contiguous Abelian square is the concatenation of two nonempty, equally long factors having the same letter-count vector.

**Theorem.** Exactly \(1{,}680\) labeled right-crucial Abelian-square-free words over \(\Sigma\) have the shortest possible length \(13\). They form precisely \(14\) classes under permutation of the five symbols. Furthermore, for every such word \(w\) and every appended letter \(x\), the extended word \(wx\) ends in exactly one Abelian square. If \(h_x\) is the half-length of that square, the multiset \(\{h_x:x\in\Sigma\}\) belongs to exactly four types, with the following complete distribution among the \(14\) classes:

| Increasingly sorted half-lengths | Number of relabeling classes |
| --- | ---: |
| \((1,2,3,6,7)\) | 8 |
| \((1,2,3,5,7)\) | 3 |
| \((1,4,5,6,7)\) | 2 |
| \((1,2,5,6,7)\) | 1 |

Each class has exactly \(5!=120\) labeled representatives. The \(14\) canonical words, obtained by labeling symbols in order of first appearance, are:

```
0102343104303
0120324023024
0120324023204
0120343020343
0120343104303
0121343014313
0123243024323
0123243034232
0123423024323
0123423034232
0123424023424
0123424043242
0123432024323
0123432034232
```

The companion table `canonical_representatives.csv` gives the half-length for each appended letter separately.

## Assumptions and scope
Words are finite ordered strings; factors are contiguous and half-blocks have positive length. The alphabet has exactly five *distinguishable* letters, and appending any of those five letters is tested. The classification identifies words only under global alphabet relabeling, not reversal or cyclic rotation. The displayed half-lengths lie in \(\{1,\ldots,7\}\) because extensions have length \(14\). This is a complete **finite** length-\(13\) classification, not a claim about arbitrary alphabet size or length.

The established sharp minimum for right-crucial Abelian-square-free words on \(q\ge3\) letters is \(4q-7\) [1, Theorem 5]. Consequently, length \(13\) is indeed shortest at \(q=5\). The minimum-length theorem is credited to [1]; the enumeration and forcing-spectrum classification above are the separate claims proved here.

## Proof
**1. Prefix-extension test.** Let \(p_j(c)\) be the number of occurrences of symbol \(c\) in the first \(j\) positions of a word, with \(p_0(c)=0\). Its final \(2h\) letters form an Abelian square precisely when, for every \(c\in\Sigma\),
\[
p_{n}(c)-p_{n-h}(c)=p_{n-h}(c)-p_{n-2h}(c).
\]
All variables in this equality are integers. A new square appearing after a single letter is appended must end at the new last position: otherwise it was already present before appending. Thus a candidate prefix is Abelian-square-free exactly when none of its nonempty prefixes ends in a square. Repeated application of the displayed test detects **every** forbidden factor.

**2. Exhaustive symmetry reduction.** In a word using all five symbols, rename its first new symbol \(0\), its next previously unseen symbol \(1\), and so on. Exactly one word in every orbit under alphabet permutations has this *first-appearance canonical* form. It starts with \(0\). If the current largest symbol is \(m\), its next symbol lies in \(\{0,\ldots,\min(m+1,4)\}\); there is no other possibility for a canonical word, and each such extension gives one distinct canonical prefix. A crucial word must use all five symbols, since appending an absent symbol could not create an Abelian square: that symbol would occur only once, whereas each symbol occurs an even number of times in a square.

**3. Complete exact search.** Apply the deterministic recursion in `check_census.py`: start from the one-letter word \(0\); branch over the permitted canonical next letters; reject a branch if the new prefix ends in an Abelian square by Step 1. At length \(13\), retain only words containing all five symbols. For each \(x\in\Sigma\), append \(x\) and list all \(h\in\{1,\ldots,7\}\) satisfying the displayed equality on the extended word. Retain the word if every appended letter has at least one such witness. Each test is an exact comparison of five integer differences.

The exact completed enumeration visits \(297{,}588\) square-free canonical prefixes, of which \(205{,}424\) are length-\(13\) words using all five symbols. Exactly \(14\) survive all five extension tests, and they are the \(14\) words shown above. For each survivor and appended letter, the computed witness set has cardinality exactly one. Sorting the five witnesses yields the four rows of the table with frequencies \(8,3,2,1\). These counts and representatives are asserted and checked explicitly in the source, so an erroneous or incomplete enumeration produces a failed assertion.

By induction on prefix length, Step 1 keeps all and only Abelian-square-free canonical prefixes, and Step 2 visits every such prefix exactly once. Step 3 therefore exhausts the full finite search space rather than a sample. Each of the five symbols appears in every retained word, so its relabeling orbit has size \(5!\), establishing \(14\cdot120=1{,}680\). Finally [1, Theorem 5] supplies minimality of length \(13\), completing the proof.

## Verification
Run `python3 check_census.py` (standard library only). It reports exact canonical-orbit counts \(1,5,14\) for alphabets of size \(3,4,5\); for size five it checks all \(14\) literal representatives, the \(205{,}424\) five-letter square-free terminal prefixes, all five unique extension witnesses, and all four sorted signature frequencies. A separately written implementation uses direct signed symbol-count differences instead of Parikh-prefix tables: compile `independent_census.cpp` using `g++ -O2 -std=c++17 independent_census.cpp -o independent_census` and execute `./independent_census`. The two implementations agree on all fourteen representatives and on every reported count. The CSV table enumerates the actual appended-letter witnesses.

These exhaustive computations form a reproducible finite certificate when used together with the elementary prefix-and-canonicalization argument above. Merely running code without the exhaustiveness argument would not prove the classification.

## Relationship to prior work
Evdokimov and Kitaev [1] proved the sharp general minimum length \(4q-7\), presented explicit examples, and derived restrictions on letter multiplicities; none of those known statements is claimed as new here. Glen, Halldórsson, and Kitaev [2] discuss crucial Abelian powers and general constructions. Avgustinovich, Glen, Halldórsson, and Kitaev [3] prove additional lower bounds for higher powers; in particular they reiterate the known square case. These sources provide the exact boundary at which the finite classification is taken, but their constructions and length theorems do not state or immediately yield the \(14\)-orbit list, \(1{,}680\)-word census, or the four all-extension forcing signatures. This work counts all minimizers rather than constructing a single one.

## Limitations
No count is asserted for six or more letters. Only the right-crucial property is studied; the stronger condition of being unextendable on **both** sides is different. The finite calculation is exhaustive for the stated domain, but external mathematical audit and exhaustive historical-priority verification have not been performed. An unindexed earlier equivalent census or classification cannot be completely excluded.

## References
[1] A. Evdokimov and S. Kitaev, *Crucial Words and the Complexity of Some Extremal Problems for Sets of Prohibited Words*, arXiv:math/0205217v1 (first public preprint 20 May 2002), Theorem 5. https://arxiv.org/abs/math/0205217

[2] A. Glen, B. V. Halldórsson, and S. Kitaev, *Crucial Words for Abelian Powers*, arXiv:0812.4730v1 (27 December 2008). https://arxiv.org/abs/0812.4730

[3] S. Avgustinovich, A. Glen, B. V. Halldórsson, and S. Kitaev, *On Shortest Crucial Words Avoiding Abelian Powers*, *Discrete Applied Mathematics* 158 (2010), 605–607. https://spider-v.science.strath.ac.uk/sergey.kitaev/Papers/AGHK.pdf
