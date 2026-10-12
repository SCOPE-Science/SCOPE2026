# The unique optimal binary length-five two-read single-deletion reconstruction code
## Finding
Let \(D_1(x)\) be the set of distinct length-four binary words obtained by deleting one coordinate from a length-five word \(x\). A code \(C\subseteq\{0,1\}^5\) is a two-read single-deletion reconstruction code when
\[
|D_1(x)\cap D_1(y)|\le 1
\]
for every two distinct \(x,y\in C\). This is the standard \((5,2;D_1)\)-reconstruction condition: no two codewords can be consistent with the same two distinct deletion reads.

The maximum possible size is \(20\), and the maximizing labeled code is unique:
\[
\begin{aligned}
C=\{&00000,00001,00011,00100,00110,00111,01001,01100,01101,01111,\\
&10000,10010,10011,10110,11000,11001,11011,11100,11110,11111\}.
\end{aligned}
\]
The unique optimum is fixed by reversal and by global bit complementation. Its weight profile is \((1,3,6,6,3,1)\) across weights \(0,1,2,3,4,5\).

## Assumptions and scope
The alphabet is binary, the block length is exactly five, and every channel output is obtained by exactly one deletion. Deletion balls are sets of distinct outputs, so deleting equal symbols in the same run does not create duplicate reads. The reconstruction requirement is the standard fixed-read-coverage condition \(
u(C;D_1)<2\), equivalently pairwise deletion-ball intersections of size at most one. The result is a finite exact statement only for these parameters; it makes no claim about larger lengths, other alphabets, repeated rather than distinct reads, or probabilistic channels.

## Proof
Create a graph \(G\) on the \(32\) binary length-five words. Join two vertices exactly when their single-deletion balls share at least two distinct length-four words. A subset of vertices is therefore a valid two-read reconstruction code exactly when it is an independent set of \(G\).

The graph was reconstructed in two independent ways. The first method directly forms every deletion ball and tests pairwise intersections. The second method iterates over unordered pairs of distinct length-four traces and joins every pair of length-five parents whose deletion balls contain that trace pair. Both constructions produce the same graph, with \(49\) conflict edges. Among the \(496\) unordered pairs of length-five words, \(305\) pairs have deletion-ball intersection size zero, \(142\) have size one, and \(49\) have size two.

Two exact search procedures are then applied to this graph. A memoized include/exclude recurrence computes the maximum independent-set size and the number of maximizers. Independently, a Bron--Kerbosch search enumerates maximal cliques in the compatibility graph, the complement of \(G\). Both procedures return maximum size \(20\) and exactly one maximizing vertex set, namely the code displayed above. Since every independent set is contained in a maximal independent set, the exhaustive maximal-clique search also excludes every code of size at least \(21\). A direct final pass checks the reconstruction predicate on all pairs inside the unique optimum.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The verifier regenerates all \(32\) words and their deletion balls, compares the two independently built conflict graphs, executes both exact optimization procedures, checks the unique codeword list, and verifies reversal/complement invariance and the weight profile. Its expected first output line is:

`VERIFY_OK maximum=20 labeled_maxima=1 read_coverage=1 reversal_invariant=true complement_invariant=true weight_profile=1,3,6,6,3,1`

The machine-readable optimizer and excluded-word lists are also stored in `census.json`.

## Relationship to prior work
Levenshtein's 2001 reconstruction work introduced the sequence-reconstruction viewpoint and solved the uncoded repeated-transmission problem for deletions and other error types. Later fixed-read reconstruction-code work defines \((n,N;B)\)-reconstruction codes through the maximum pairwise error-ball intersection and identifies the two-read single-deletion case as a fundamental code-design problem. It also characterizes exactly when two single-deletion balls intersect in two outputs (the Type-A-confusable condition) and derives asymptotically optimal redundancy bounds. The later deletion-channel converse paper again asks how large such a codebook can be and proves asymptotic bounds.

Those inspected sources supply the framework and the pairwise obstruction, but they do not state the finite equality \(M=20\) at length five or enumerate its equality case. Exact-title, parameter, Type-A-confusability, and notation-based searches likewise produced no source stating this finite optimizer. A later complete asymptotic treatment concerns a different parameterization in which the transmitted word is restricted by deletion-correcting distance and does not imply this unrestricted finite fixed-read codebook classification.

## Limitations
The novelty comparison is based on targeted database searches and inspection of the most directly relevant accessible primary texts; it is not a proof that no obscure table, thesis, or unpublished computation contains the same finite census. The Levenshtein IEEE article was inspected through its publisher metadata and abstract rather than full text, while the two directly relevant 2020 reconstruction-code papers were inspected in full-text HTML. The mathematical claim itself does not depend on any literature statement beyond the standard model definition: it is verified by exhaustive finite computation from first principles.

## References
1. V. I. Levenshtein, “Efficient reconstruction of sequences,” *IEEE Transactions on Information Theory* 47(1), 2–22 (2001), DOI `10.1109/18.904499`.
2. K. Cai, H. M. Kiah, T. T. Nguyen, E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:`2001.01376` (2020; later IEEE Transactions on Information Theory).
3. J. Chrisnata, H. M. Kiah, E. Yaakobi, “Optimal Reconstruction Codes for Deletion Channels,” arXiv:`2004.06032` (2020).
4. M. Mitzenmacher, “A survey of results for deletion channels and related synchronization channels,” *Probability Surveys* 6, 1–33 (2009), DOI `10.1214/08-PS141`; primary AMS classification 94B50.
