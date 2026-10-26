# Optimal-delay enumeration of subsequence-universal words over variable alphabets

## Finding

**Theorem.** Let \(n,k\ge0\), \(q\ge1\), and \(\Sigma=\{1,\ldots,q\}\) with its natural order. A word \(w\in\Sigma^n\) is \(k\)-subsequence universal if every word of \(\Sigma^k\) occurs in \(w\) as a (not necessarily contiguous) subsequence. There exists a deterministic algorithm that outputs all such words once in lexicographic order with **\(O(n)\) worst-case delay** between explicit outputs, \(O(n+q)\) initialization, and \(O(n)\) auxiliary memory when the output family is nonempty. These are *uniform* bounds: constants do not depend on \(n\), \(k\), or \(q\). The algorithm immediately detects the empty case \(n<kq\).

For \(n>0\), the delay is asymptotically optimal under an explicit-output model, in which emitting \(n\) symbols requires \(\Omega(n)\) operations. The algorithm is lexicographic and does not require any rank/unrank tables.

## Assumptions and scope

A unit-cost RAM is assumed for alphabet-symbol indices of \(O(\log(q+n))\) bits; writing one output symbol costs constant time. The alphabet is given implicitly as the integer interval from one through \(q\). Preprocessing is limited to allocating a length-\(n\) buffer and (when \(k>0\) and feasible) a length-\(q\) linked-list structure. Output delay counts the worst-case interval between consecutive *complete explicitly materialized* words. When there are zero or one outputs, no between-output delay is needed; total traversal through the last output remains \(O(n)\) in nonempty instances. For \(k=0\), every word is admissible; the same generator handles this case without the missing-symbol structure. For \(n=0\), the empty word is emitted (for any \(k=0\)); all other cases are empty.

## Proof

**1. Greedy arches characterize universality.** Scan a word from left to right, ending an *arch* as soon as all \(q\) alphabet symbols have been encountered since the start of that arch. Continue scanning from the next position; the final unfinished suffix is the *remainder*. Let \(r(w)\) be the number of completed arches. Then \(w\) is \(k\)-subsequence universal if and only if \(r(w)\ge k\). For sufficiency, each completed arch contains any requested next letter, so one may choose the \(i\)-th target letter in the \(i\)-th arch. For necessity, if there are only \(r\) complete arches, select for each arch the symbol first appearing as that arch is completed, and select a symbol absent from the remainder. A greedy matching argument (or the standard arch lemma [1]) constructs a length-\(r+1\) absent subsequence: after the selected completing symbols, the missing remainder symbol cannot be matched. Thus no complete universality of level \(r+1\) is possible.

**2. Exact feasibility of a prefix.** After a prefix of length \(t\) with \(r<k\) completed arches and \(s\) distinct symbols already present in its current unfinished arch, at least \(q-s\) more letters are needed to finish this arch and at least \(q\) letters for each of the remaining \(k-r-1\) complete arches. Conversely, writing each currently unseen symbol once and then writing a complete alphabet permutation for each further required arch meets that lower bound. Therefore the *minimum necessary completion length* is exactly

\[
\delta=q(k-r)-s.
\]

The prefix admits an admissible extension to total length \(n\) if and only if \(h=n-t-\delta\ge0\). Once \(r\ge k\), every continuation works.

**3. Constant-time feasible next-letter enumeration.** Maintain \(h\) and an ordered doubly linked list of the symbols not yet seen in the current arch; membership is maintained in a Boolean array. If \(h=0\) and \(r<k\), appending a symbol seen in this arch makes \(h\) decrease by one and is impossible, while appending an unseen symbol leaves \(h\) unchanged. Only list elements need be traversed. If \(h>0\) or \(r\ge k\), every letter from one through \(q\) is possible. At a completed arch, open a fresh unseen-symbol list; changing arches takes \(O(q)\) time. Deleting an unseen letter from a linked list and restoring it on backtracking cost \(O(1)\). Every child produced in either mode is feasible, so the search never visits an unproductive subtree. Each node's next admissible child is generated in constant time, rather than scanning over forbidden letters.

**4. Worst-case delay and memory.** Perform iterative lexicographic depth-first search over feasible prefixes, outputting the buffer only at depth \(n\). Between two consecutive outputs, the search ascends at most \(n\) edges and descends at most \(n\) edges. All transitions cost \(O(1)\) apart from opening a new arch list. Along a root-to-leaf path, each complete arch consumes at least \(q\) word positions, so there are at most \(\lfloor n/q\rfloor\) such openings. Therefore list-initialization cost on the two path segments is at most \(O(q\lfloor n/q\rfloor)=O(n)\); writing the explicit output also costs \(O(n)\). Thus delay is \(O(n)\) uniformly even when \(q\) varies with \(n\). The DFS frames and output buffer take \(O(n)\) space. Each active arch list takes \(O(q)\) and their number is at most \(\lfloor n/q\rfloor\), so combined auxiliary space is \(O(n)\) for nonempty families; initial allocation costs \(O(n+q)\), which is \(O(n)\) if \(k\ge1\) and the family is nonempty. The \(k=0\) case has no arch structures and works in \(O(n)\) space for any \(q\). This completes the proof.

## Verification

The accompanying `universal_lex.py` implements the iterative DFS and the linked-list undo operations using only the Python standard library. Execute `python universal_lex.py` to compare every output tuple, in order, against independent lexicographic brute-force enumeration for all \(q\in\{1,2,3,4\}\), \(0\le n\le7\), and \(0\le k\le3\). The test covers 128 parameter triples and 38,984 emitted tuples. Additional tests instantiate \((q,k,n)=(21,1,21),(200,1,200),(53,2,106),(3,1,1500)\) and independently check the first three generated outputs of each case. The finite tests are regression checks; the general complexity and correctness conclusions are established by the preceding proof, not by experimental extrapolation.

## Relationship to prior work

Adamson [1] gives \(O(nq)\) enumeration delay with \(O(nkq)\) preprocessing and explicitly asks whether \(O(n)\) delay is achievable. The algorithm above meets that target, without a factor \(q\), for a *variable* alphabet size. The general regular-language treatment [2] addresses decision/counting/ranking problems with explicit automata but does not supply this implicit-alphabet linear-delay enumerator. The general walk enumerator [3] achieves succinct constant-delay outputs after preprocessing linear in the graph size. Direct representation of the present greedy-arch condition as a DFA tracking subsets of the variable alphabet has exponentially many subset states; thus [3] does not provide the claimed \(O(n+q)\)-preprocessing uniform guarantee. The absent-subsequence enumeration algorithms in [4] enumerate missing subsequences *of a given word*, rather than all length-\(n\) words satisfying a universal-subsequence constraint.

## Limitations

The theorem concerns explicit-output lexicographic enumeration, not lexicographic ranking/unranking, compression of the entire output, a \(q\)-independent alphabet encoding, or succinct constant-time delay. The time bounds use unit-cost operations on alphabet indices; arbitrary-length symbol labels have separate representation costs. No theorem about shortest absent subsequences or general regular languages is implied.

## References

[1] Duncan Adamson. *Ranking and Unranking k-subsequence universal words*. 2023, arXiv:2304.04583, version first made public 2023-04-10. https://arxiv.org/abs/2304.04583.

[2] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka. *k-Universality of Regular Languages*. 2023, arXiv:2311.10658. https://arxiv.org/abs/2311.10658.

[3] D. Adamson, P. Gawrychowski, and F. Manea. *Enumerating m-Length Walks in Directed Graphs with Constant Delay*. 2024, arXiv:2401.02163. https://arxiv.org/abs/2401.02163.

[4] *Tight Bounds for the Number of Absent Subsequences*. 2024, arXiv:2407.18599. https://arxiv.org/abs/2407.18599.
