# Complete rooted LZ78 phrase spectrum of binary order-five de Bruijn cycles

## Finding

A **binary de Bruijn cycle of order five** is a cyclic word of length \(32\) in which every binary five-letter word occurs as a circular factor exactly once. Cycles are identified under rotation, but not under reversal or bit complementation. For each cycle \(W\), form its \(32\) different rooted linear traversals \(W^{(j)}\), \(0\le j<32\). Write \(c(w)\) for the incremental LZ78 phrase count, including an already-known terminal suffix as a final phrase, as defined below.

**Complete finite classification.** Exactly \(2,048\) such cycles exist. Among their \(65,536\) rooted traversals, the exact numbers with \(c(w)=11,12,13,14\), respectively, are
\[
(80,\ 7{,}586,\ 55{,}690,\ 2{,}180),
\]
and no other phrase counts occur. More precisely, put
\[
L(W)=\min_{0\le j<32}c(W^{(j)}),\qquad
H(W)=\max_{0\le j<32}c(W^{(j)}).
\]
The complete joint distribution of \((L(W),H(W))\), over cycles up to rotation, is:

| \((L,H)\) | Number of cycles |
|---|---:|
| \((11,13)\) | 6 |
| \((11,14)\) | 44 |
| \((12,13)\) | 746 |
| \((12,14)\) | 1,172 |
| \((13,13)\) | 30 |
| \((13,14)\) | 50 |

Consequently the minimum over all rooted traversals is exactly \(11\), the maximum is exactly \(14\), and exactly \(30\) cycles have root-independent phrase count \(13\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), and a rooted traversal reads exactly one full period, without appending the initial four bits. Rooting is by all starting indices \(0,\ldots,31\). At each incremental LZ78 step, maintain a dictionary of previously completed *new* phrases, initially empty. Read the shortest nonempty prefix of the unconsumed suffix not yet in the dictionary, append it as a phrase and insert it. If the entire nonempty remaining suffix is already a dictionary phrase, append that suffix as one final (possibly repeated) phrase, without inserting it. There is no end-marker and no artificial final symbol. Every phrase counts once. This is the finite-input incremental convention, not LZ76 exhaustive-history complexity or LZ77 longest previous-factor parsing.

For clarity, every circular length-five factor is read with wraparound. No larger order or alternative LZ parsing convention is asserted.

## Proof

**1. Every cycle has one sixteen-bit feedback representation.** Identify a five-bit window \(x_0x_1x_2x_3x_4\) with a state \(s\in\{0,\ldots,31\}\); let \(t=x_1x_2x_3x_4\in\{0,\ldots,15\}\) be its suffix of length four. Following the windows of a de Bruijn cycle gives a permutation of the \(32\) states, necessarily a single cycle, and its transition sends \(x_0t\) to \(tb\) for some output bit \(b\). The two predecessors \(0t,1t\) must map bijectively to the two states \(t0,t1\). Hence a uniquely defined Boolean function \(g\) on the \(16\) four-bit suffixes satisfies
\[
F_g(x_0t)=t\bigl(x_0\mathbin{\oplus}g(t)\bigr).
\]
Conversely, for every one of the \(2^{16}\) choices of \(g\), \(F_g\) is a permutation of the \(32\) five-bit states. It corresponds to a de Bruijn cycle exactly when the orbit of state \(00000\) has length \(32\). The recorded leading bits of successive five-bit states then give the unique cyclic word rooted at its unique factor \(00000\). This proves a bijection between the accepted feedback functions and the required cycles; no isomorphism or rotation correction is missing.

**2. Independent exhaustive enumeration.** The attached standalone file `verify.py` implements all \(65,536\) functions. It traverses the orbit of \(00000\), rejects a function at the first repeated state before the full length, and retains those returning to \(00000\) after \(32\) distinct states. Exactly \(2,048\) functions remain. Independently, the same file exhausts all directed Euler tours on the binary order-four de Bruijn graph (vertices: four-bit words; directed edges: five-bit words). It fixes the unique edge \(00000\) first, then recursively takes each unused outgoing edge until all \(32\) edges have been used and the walk closes. A de Bruijn cycle is equivalent to exactly such a tour up to rotation, since its circular five-bit windows are precisely the edges. The two constructions yield exactly the same set of \(2,048\) canonical rooted words. Each included word is additionally checked to have all \(32\) circular five-bit windows distinct.

**3. Exact parsing and counting.** For each retained word, the checker constructs all \(32\) rotations and computes the LZ78 phrase count twice: (i) a set of previously completed phrases, extended until the shortest unseen prefix is found, and (ii) independent traversal and insertion of nodes in an LZ78 dictionary trie. Both implementations treat a terminal dictionary suffix as one phrase. Their values agree on every one of the \(65,536\) rooted words. Integer counters then tally every \(c\)-value and, separately, each cycle's minimum and maximum. The counters equal the values displayed in the Finding section. The sum of the four rooted counts is \(65,536\), and the sum of the six joint counts is \(2,048\). The code contains explicit assertions for all outputs and performs no random sampling or approximation.

**4. Finite-proof closure.** Step 1 proves that the finite sixteen-bit loop is a *complete* parametrization rather than a sample. Step 2 provides an independently characterized exhaustive list of all allowable cyclic objects. Step 3 computes the precisely defined deterministic function on *every* rooted traversal using two algorithmically distinct representations. Thus the finite counts, their extrema, and their absence outside the stated support follow exactly. This establishes the complete classification without an inference from a partial experiment.

## Verification

Run `python3 verify.py` in a standard Python 3 interpreter; the code has no third-party imports. It prints `VERIFY_OK`, the four rooted counts, the minimum/maximum and joint distributions, a deterministic SHA-256 of the sorted canonical words with their thirty-two parse counts, and six explicit witness words. The census hash is

`53b2490953189d216487bd858765bac029e88c9214b00570275f4225029ed144`.

The checker was run from the actual file and all its assertions passed. Its two cycle-enumeration methods and two parse methods are independent enough to expose common indexing or terminal-convention mistakes, although they do not replace an external audit.

## Relationship to prior work

Ziv and Lempel's 1978 formulation introduces incremental dictionary parsing. Dutta–Levi–Ron–Rubinfeld (2013, arXiv:1301.2495, Sections 1–2) spell out the trie version of LZ78 and study efficient random access to its encoding, not distributions on de Bruijn cycles. Cohn and Helfgott (1997) use truncations and concatenations of de Bruijn sequences to prove forward-versus-reversal *asymptotic* parsing separations; their Theorem 1 concerns telescoped words and does not enumerate rooted traversals of one order-five cycle. The exact finite joint distribution and the thirty root-invariant cycles are additional questions not answered by those inspected results. Searches of related published mathematical records did not reveal an equivalent complete table; this negative search alone cannot establish historical priority.

## Limitations

The theorem is a finite exact statement for binary order five only. It makes no conjecture about higher-order spectra or the asymptotic compression rate. Phrase count is an intrinsic parser statistic, not bit-length after assigning actual dictionary pointer codes. A different end-of-input convention may change the numerical table, and the convention used here is part of the theorem. The supporting algorithmic proof has been re-executed and reviewed internally but not independently audited or formally verified. Historical priority remains vulnerable to unindexed or inaccessible compression tables.

## References

1. J. Ziv and A. Lempel, *Compression of Individual Sequences via Variable-Rate Coding*, IEEE Transactions on Information Theory 24 (1978), 530–536. Full text: https://www.philippe-fournier-viger.com/spmf/lz78.pdf
2. M. Cohn and H. A. Helfgott, *Asymmetry in Ziv/Lempel '78 Parsing*, Compression and Complexity of Sequences (1997), DOI: https://doi.org/10.1109/SEQUEN.1997.666926 ; author-uploaded text: https://www.researchgate.net/publication/3741814_Asymmetry_in_ZivLempel_%2778_parsing
3. A. Dutta, R. Levi, D. Ron and R. Rubinfeld, *A simple online competitive adaptation of Lempel-Ziv compression with efficient random access support*, arXiv:1301.2495 (first posted 2013-01-11), https://arxiv.org/abs/1301.2495
4. J. Ziv, *A Constrained-Dictionary version of LZ78 asymptotically achieves the Finite-State Compressibility for any Individual Sequence with a Distortion measure*, arXiv:1409.1323 (first posted 2014-09-04), https://arxiv.org/abs/1409.1323
