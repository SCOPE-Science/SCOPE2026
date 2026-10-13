# Exact classification of optimal binary length-five single-insertion coverings

## Finding
For the binary alphabet \(\Sigma=\{0,1\}\), a set \(C\subseteq\Sigma^5\) is a one-insertion covering code when every \(y\in\Sigma^6\) admits at least one \(x\in C\) obtainable by deleting one position of \(y\). The smallest size is exactly \(12\). There are exactly **six labeled codes** attaining this size, forming exactly **three equivalence classes** under global binary-symbol complementation and coordinate-order reversal. Every equivalence class has two labeled members.

The three representatives, encoded as five-character binary strings, are:

- `00000 00011 00110 01001 01100 01111 10000 10011 10110 11001 11100 11111`
- `00000 00011 00101 00110 01000 01111 10000 10111 11001 11010 11100 11111`
- `00000 00011 00100 00111 01101 01110 10001 10110 11000 11011 11100 11111`

## Assumptions and scope
Only ordinary binary words are considered, not linear subspaces or multisets. Positions are ordered, and deleting any one of the six positions of a received word is allowed. The code is a set, so a repeated center is counted once. Alphabet complementation and word reversal preserve this covering relation. No other coordinate permutations are assumed to be symmetries.

## Proof
There are \(32\) candidate length-five words and \(64\) target length-six words. For each target \(y\), define its predecessor set \(P(y)\) as all **distinct** words produced by deleting precisely one position of \(y\). For each candidate \(x\), define its insertion ball \(B(x)=\{y:x\in P(y)\}\). A direct position count, or inspection of all possible insertions, shows \(|B(x)|=7\) for every binary word of length five. This ball-size property is also independently checked for all \(32\) candidates in both supplied programs.

The following finite-search lemma is exhaustive: given a covered-target set \(U\), a selected-center set \(F\), and a remaining capacity \(r\), choose any target \(y\notin U\). Every covering extension of \(F\) must select at least one candidate in \(P(y)\). Branch once for every candidate in \(P(y)\setminus F\), adding that candidate and its entire insertion ball. If there are more than \(7r\) uncovered targets, prune: even \(r\) further centers cannot cover them. A branch at zero remaining capacity fails unless every target is covered. Thus exhaustive recursion checks **every** covering set of size at most the given capacity. Its branches have finite depth at most that capacity, use all legal predecessor choices, and use only the proved ball-size pruning inequality. Distinct completed center sets are stored canonically, avoiding duplicate counts from different branch orders.

`verify.cpp` builds the predecessor relation directly by deletion from each of the \(64\) targets; `verify.py` builds it independently using binary-string slicing. Both exhaustively exclude coverings with at most \(11\) centers. At capacity \(12\), both enumerate precisely six distinct complete coverings and individually check that each has \(12\) centers and covers every target. The three displayed representatives occur in the enumeration. Complementation and reversal generate precisely two codes from each representative; the resulting three pairs are disjoint and exhaust the six enumerated codes. Hence minimum size, labeled enumeration and equivalence classification follow.

## Verification
From the directory containing the two supplied source files, run `g++ -O2 -std=c++20 verify.cpp -o verify` followed by `./verify`, and separately run `python3 verify.py`. Both checks finish with `VERIFY_OK`; their code does not rely on external data or optimization solvers. The finite search is exact rather than sampled. The C++ checker visits \(10{,}955\) recursion states across capacities \(0\) through \(12\); the separately written Python checker visits \(10{,}841\) states at capacities \(11\) and \(12\).

## Relationship to prior work
Xie, Sun and Ge (2026) study insertion/deletion covering codes over large alphabets, giving general bounds and asymptotic results. Pikhurko, Verbitsky and Zhukovskii (first public preprint 2024) investigate the large-alphabet density and cite Grozea's exact optimal ternary length-three insertion covering classification. Grozea's public table concerns covering four-symbol words by **three-symbol** codewords, for several alphabet sizes; that parameter is not the present binary length-five problem. Lenz and collaborators (2021) give general bounds and constructions, not a classification of these six length-five optimizers in the inspected sections. The distinction from classical Hamming covering codes, and from non-overlapping and deletion-correcting codes, is substantive: their admissibility relations are different.

## Limitations
The theorem is restricted to binary, one-insertion covering with centers of length five. It does not assert a formula for arbitrary lengths, other alphabets, or one-deletion covering. Earlier unpublished or unindexed finite enumerations may exist; the mathematical classification is established here only by the complete independently replayable finite searches, not by a general symbolic classification theorem. No independent external audit has been performed.

## References
1. C. Xie, J. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first publicly available June 13, 2026. https://arxiv.org/abs/2606.15379
2. O. Pikhurko, O. Verbitsky and M. Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density*, arXiv:2409.06425, first preprint 2024. https://arxiv.org/abs/2409.06425
3. A. Lenz, C. Rashtchian, P. H. Siegel and E. Yaakobi, *Covering Codes Using Insertions or Deletions*, IEEE Trans. Inform. Theory 67 (2021), 3376–3388. https://arxiv.org/abs/1911.09944
4. C. Grozea, *Combinatorial data on optimal three-symbol-length single-insertion codes*, reported 2024. https://www.brainsignals.de/users/cristian.grozea/combinatorial.html
