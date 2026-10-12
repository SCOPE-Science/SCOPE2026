# Sharp length-four consecutive-two-deletion covering for alternating alphabets

## Finding
Let \(X\) and \(Y\) be finite alphabets with respective sizes \(m,n\ge 2\). A length-four code \(C\subseteq X\times Y\times X\times Y\) is called a *consecutive-two-deletion cover* when every received pair in \(X\times Y\) results from deleting one of the three adjacent position-pairs of at least one word in \(C\). Let \(B(m,n)\) denote its minimum possible cardinality. Then, for all integers \(m,n\ge 2\),

\[
 B(m,n)=\left\lceil\frac{mn}{3}\right\rceil.
\]

In particular, for an ordinary \(q\)-symbol alphabet in all four coordinates, \(B(q,q)=\lceil q^2/3\rceil\) for every integer \(q\ge2\). An explicit constructive procedure attaining the bound appears below and in `verify.py`.

## Assumptions and scope
The alphabets are sets, with no field structure assumed. Deletions remove *exactly two consecutive positions*, at positions \((1,2)\), \((2,3)\), or \((3,4)\); the two remaining symbols preserve their order. Consequently, the received domain is \(X\times Y\) in each case. Codes are sets of distinct words, not multisets. The result concerns covering (every received pair has at least one preimage), not correction or unique decoding, and says nothing about arbitrary nonconsecutive deletions or other blocklengths.

## Proof
Write a codeword as \((a,b,c,d)\) with \(a,c\in X\) and \(b,d\in Y\). Its possible received pairs form the set

\[
 \{(c,d),(a,d),(a,b)\}.
\]

At most three pairs can arise from any codeword. Since \(mn\) distinct received pairs are required, \(|C|\ge\lceil mn/3\rceil\).

For the upper bound, regard \(X\times Y\) as the edge set of the complete bipartite graph with parts \(X\) and \(Y\). If \(a\ne c\) and \(b\ne d\), the three pairs in the displayed set are the edges of a four-vertex path, and conversely every such path can be represented by a codeword. We therefore construct a cover of all edges by exactly \(\lceil mn/3\rceil\) three-edge paths.

**A rectangular tiling lemma.** Every \(3\)-by-\(t\) complete bipartite edge rectangle with \(t\ge 2\) admits a partition into exactly \(t\) three-edge paths. Indeed, partition its \(t\) columns into groups of sizes two and three, which is always possible for \(t\ge2\). For three rows and two columns, the words \((1,1,0,0)\) and \((2,0,0,1)\) partition the six edges. For three rows and three columns, use the three words

\[
 (i,i+1,i+1,i),\qquad i=0,1,2,
\]

where the column and row additions are reduced modulo three. Each of the nine edges occurs once. Relabel these two patterns on each group; their union partitions the rectangle.

**Finite bases.** The remaining rectangles with both side lengths at most four have exact covers of the required cardinalities. For \((m,n)=(2,2)\), use \((0,1,1,0)\), \((1,1,0,0)\). For \((2,3)\), use \((0,0,1,2)\), \((1,0,0,1)\). For \((2,4)\), use \((0,3,1,0)\), \((1,0,0,1)\), \((1,3,0,2)\). For \((3,3)\) and \((3,4)\), the rectangular tiling lemma supplies respectively three and four words. For \((4,4)\), use

\[
 \begin{aligned}
 &(0,0,3,1),\quad(0,2,1,3),\quad(1,1,2,0),\\
 &(2,1,1,2),\quad(2,3,3,0),\quad(3,2,1,3).
 \end{aligned}
\]

All output pairs are covered in each finite base (checked directly in `verify.py`). Transposition of the bipartite graph transports a word \((a,b,c,d)\) to \((d,c,b,a)\). Hence the reversed rectangular base cases are also covered.

**Induction.** Induct on \(m+n\). If \(m\ge5\), separate the last three rows of the \(m\)-by-\(n\) edge rectangle. By induction the remaining \((m-3)\)-by-\(n\) block has a cover with \(\lceil(m-3)n/3\rceil\) paths. The rectangular tiling lemma gives exactly \(n\) additional, edge-disjoint paths covering the new three rows. Thus the combined cover has

\[
 \left\lceil\frac{(m-3)n}{3}\right\rceil+n
 =\left\lceil\frac{mn}{3}\right\rceil
\]

paths. If instead \(m\le4\) and \(n\ge5\), remove the last three columns, apply induction to the remaining rectangle, and apply the transposed tiling lemma to the new columns; exactly \(m\) paths are added. This yields the same cardinality. Since every smaller rectangle has both sides at least two, induction reaches one of the finite bases. Taking the corresponding codeword for each path gives the required cover. This proves the equality for all \(m,n\ge2\).

A further numerical consequence is that optimal covers use precisely \(3\lceil mn/3\rceil-mn\) repeated pair-incidences when all selected codewords have three distinct deletion outputs. Thus one or two repeated incidences suffice and are necessary whenever \(3\) does not divide \(mn\).

## Verification
The self-contained standard-library `verify.py` constructs the base cases, the \(3\)-by-\(t\) tilings, and both induction steps. Its `burst_shadow` routine independently enumerates the three deletion outputs, and its checks verify alphabets, codeword uniqueness, the exact target cardinality, and full coverage. Running `python3 verify.py` checked all \(2401\) pairs \((m,n)\) with \(2\le m,n\le50\) and printed `VERIFY_OK 2401 rectangular parameter pairs`. Finite tests validate the construction, while the preceding symbolic induction is the proof for unrestricted alphabets.

## Relationship to prior work
Xie, Sun and Ge (arXiv:2606.15379, first public 13 June 2026), Section VI, establish two-burst-deletion covering constructions at arbitrary blocklength, including perfect binary differential-VT covers and a nonbinary upper bound \(q^4/(8\lfloor q/2\rfloor^2)\) when specialized to length four. That bound does not entail the exact \(\lceil q^2/3\rceil\) classification, which is asymptotically two-thirds as large. Their binary length-four case is already covered and is not claimed as new here.

Teypaz and Rapine, *Graph decomposition into paths under length constraints* (Section 4, Theorem 4.1), establish that a complete bipartite graph with both parts of size at least two can be partitioned into three-edge paths if and only if the number of edges is a multiple of three. Consequently the divisible-by-three cases of the path-counting argument are prior-covered. The new component is the optimal *overlapping* path-cover construction when \(3\) does not divide \(mn\), together with the exact all-alphabet synchronization-covering statement. The earlier insertion/deletion covering paper by Lenz, Rashtchian, Siegel and Yaakobi (arXiv:1911.09944) treats unconstrained deletions and asymptotic bounds rather than this exact adjacent-two-deletion problem.

## Limitations
The theorem only concerns length four and one burst of exactly two deletions; no assertion is made about multiple bursts, unique decodability, nonadjacent deletions or longer blocks. The divisible-by-three graph decomposition was already established; novelty is specifically the sharp complete covering classification in the remaining congruence classes and its coding-theory consequence. Graph-cover literature could contain a prior equivalent small-path covering theorem that was not indexed in the consulted searches; independent literature review is still necessary.

## References
1. C. Xie, Y. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (13 June 2026), especially Section VI. https://arxiv.org/pdf/2606.15379
2. N. Teypaz and C. Rapine, *Graph decomposition into paths under length constraints*, Section 4, Theorem 4.1. https://cahiersleibniz.g-scop.grenoble-inp.fr/wp-content/uploads/2019/05/Cahier165.pdf
3. A. Lenz, C. Rashtchian, P. H. Siegel and E. Yaakobi, *Covering codes using insertions or deletions*, arXiv:1911.09944; later IEEE Transactions on Information Theory **67** (2021), 3376–3388. https://arxiv.org/pdf/1911.09944
