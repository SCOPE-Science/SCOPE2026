# Exact one-sided adjacent-transposition capacity in the binary weight-two layer

## Finding

For every integer \(n\ge2\), consider binary length-\(n\) words containing exactly two ones. The channel may leave its input unchanged or make **one** directed adjacent substitution of the two-symbol pattern `01` by `10` (equivalently, move one of the two ones exactly one place left, provided the intervening symbol is zero). Let \(M_n\) be the largest code size for unique correction: no two codewords may have a common possible output. Then

\[
\boxed{M_n=\left\lfloor\frac{n(n+1)}6\right\rfloor.}
\]

In zero-based positions, write the locations of the two ones as \((i,j)\), where \(0\le i<j<n\). An attaining code is the simple congruence class

\[
\boxed{\mathcal C_n=\{(i,j):0\le i<j<n,\quad i+2j\equiv2\pmod3\}.}
\]

Every received word in its error image has a unique possible parent in \(\mathcal C_n\), recoverable by testing at most three candidate pairs. The formula is exact at every block length, including boundary cases.

## Assumptions and scope

Words are *linear* (not cyclic); their positions are labeled. The alphabet is \(\{0,1\}\), the Hamming weight is **exactly two**, and the allowed operation is **only** `01` to `10`, at most once. The opposite operation `10` to `01` is not allowed. Adjacent equal bits cannot be swapped. Decoding receives the entire length-\(n\), weight-two output. This is not a claim about correction of an unrestricted adjacent transposition, two shifts, deletions, or other Hamming-weight layers.

Let \(P_n=\{(i,j):0\le i<j<n\}\). Define the exact error ball

\[
B(i,j)=\{(i,j)\}
\cup\bigl(\{(i-1,j)\}\text{ if }i>0\bigr)
\cup\bigl(\{(i,j-1)\}\text{ if }j>i+1\bigr).
\]

A code is feasible precisely when these sets are pairwise disjoint.

## Proof

**1. Local compatibility graph.** Make a graph \(G_n\) on \(P_n\); join distinct vertices when their error balls intersect. A direct examination of the three possible receiver positions proves that, for \(p=(i,j)\), \(q=(i',j')\),

\[
B(p)\cap B(q)\ne\varnothing
\quad\Longleftrightarrow\quad
(i'-i,j'-j)\in
\{(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)\}.
\]

Every listed displacement is realized by a shared receiver whenever both endpoints belong to \(P_n\): horizontal and vertical neighbors share one endpoint's unchanged word, and the diagonal displacement \((1,-1)\) shares the position pair reached by moving the first one left from one input and the second one left from the other. There are no other differences between two members of the same radius-one directed ball. Thus \(M_n=\alpha(G_n)\).

**2. A lower bound with explicit decoding.** The map \((i,j)\mapsto i+2j\pmod3\) is a proper three-coloring of \(G_n\): each of the six displacements in step 1 changes the residue nontrivially. In particular, \(\mathcal C_n\) is independent and corrects the channel. Given received \((a,b)\), its possible parents are among \((a,b)\), \((a+1,b)\) if \(a+1<b\), and \((a,b+1)\) if \(b+1<n\). Their residues are respectively \(a+2b\), \(a+2b+1\), and \(a+2b+2\pmod3\), so at most one belongs to \(\mathcal C_n\).

**3. A sharp three-row clique partition.** For each integer \(m\ge1\), define

\[
S_m=\{(i,j):j\in\{m,m+1,m+2\},\ 0\le i<j\}.
\]

It has a partition into exactly \(m+2\) cliques of \(G_{m+3}\). For every even integer \(i\) with \(0\le i\le m-2\), take the triangle

\[
\{(i,m),(i+1,m),(i,m+1)\}.
\]

For every odd integer \(i\) with \(1\le i\le m\), take the triangle

\[
\{(i,m+1),(i-1,m+2),(i,m+2)\}.
\]

All three pairwise differences in each triangle appear in step 1. These triangles are mutually disjoint and there are exactly \(m\) of them. The three remaining vertices consist of an edge plus a singleton. When \(m\) is odd, the edge is \(\{(m-1,m),(m-1,m+1)\}\); when \(m\) is even, it is \(\{(m,m+1),(m,m+2)\}\). In both cases the singleton is \(\{(m+1,m+2)\}\). Directly checking the three rows shows this list covers every vertex exactly once. Hence any independent set uses at most \(m+2\) vertices of \(S_m\).

The same strip contains exactly \(m+2\) vertices of color \(2\). Indeed, for each \(i\) from \(0\) to \(m-1\), the three positions with that first coordinate and second coordinate \(m,m+1,m+2\) have all three different residues. These contribute \(m\) color-\(2\) vertices. The three additional positions are \((m,m+1)\), \((m,m+2)\), and \((m+1,m+2)\), of respective colors \(2,1,2\).

**4. Induction and exact count.** The bases \(n=2,3,4\) have independence numbers \(1,2,3\), witnessed by their color-\(2\) vertices and bounded by direct inspection of \(G_n\). For \(n\ge5\), partition \(P_n\) into \(P_{n-3}\) and the strip \(S_{n-3}\). The clique partition gives

\[
\alpha(G_n)\le\alpha(G_{n-3})+(n-1),
\]

while the color-\(2\) construction contains exactly \(n-1\) new vertices in that strip, so equality holds. Finally,

\[
\left\lfloor\frac{n(n+1)}6\right\rfloor
-\left\lfloor\frac{(n-3)(n-2)}6\right\rfloor=n-1,
\]

and the bases match. This proves the theorem for every \(n\ge2\).

## Verification

The standalone standard-library script `verify.py` constructs the exact directed error balls, confirms the local six-displacement rule, checks pairwise disjointness of the displayed code through \(n=50\), checks the three-row clique partition through \(m=150\), and independently obtains exact maximum-independent-set sizes by exhaustive recursive search for \(2\le n\le9\). Run `python3 verify.py` from the folder containing the script. All tests passed in the delivered package. These finite tests corroborate, but do not replace, the all-\(n\) proof above.

## Relationship to prior work

Wang, Vu, and Tan (2023) formally distinguish `01` to `10` from its reverse and develop general constructions for asymmetric shift errors mixed with deletions; their main theorems give redundancy bounds, not this exact constant-weight-two one-direction optimum. Gómez Soto, Leaños, Ríos-Castro, and Rivera (2017 preprint, 2018 publication) solve the **bidirectional** adjacent-transposition code problem at weight two by packing the two-token graph of a path. This is a strictly stronger error channel: for example, at length \(4\) its optimum is \(2\) whereas the one-direction optimum here is \(3\). Thus their exact value does not imply the present value. Ndjatchi and collaborators (2024) study the bidirectional weight-three token-graph problem, also different. Kovačević (2018 preprint, 2019 publication) studies asymptotic shift-correcting codes with run-length constraints. Earlier work by Kløve on perfect constant-weight peak-shift codes is relevant but was available only through bibliographic description in the comparison.

The present result is a finite-blocklength exact theorem for a channel direction and input layer not covered by those inspected statements. An undiscovered equivalent result or implicit special case of older shift-coding results remains possible.

## Limitations

The formula is limited to Hamming weight two and at most one one-sided shift. It does not classify all maximum codebooks, prove uniqueness of the displayed construction, or address bidirectional shifts, multiple shifts, or nonbinary alphabets. No independent external mathematical validation is claimed.

## References

1. S. Wang, V. K. Vu, and V. Y. F. Tan, *Codes for Correcting Asymmetric Adjacent Transpositions and Deletions*, arXiv:2301.11680v2 (2023), https://arxiv.org/html/2301.11680v2.
2. J. M. Gómez Soto, J. Leaños, L. M. Ríos-Castro, and L. M. Rivera, *The packing number of the double vertex graph of the path graph*, arXiv:1711.03682 (2017), https://arxiv.org/abs/1711.03682.
3. C. Ndjatchi et al., *On the packing number of 3-token graph of the path graph*, AIMS Mathematics 9 (2024), 11644–11659, https://doi.org/10.3934/math.2024571.
4. M. Kovačević, *Runlength-Limited Sequences and Shift-Correcting Codes: Asymptotic Analysis*, arXiv:1803.06117 (2018), https://arxiv.org/abs/1803.06117.
5. T. Kløve, *Codes correcting a single insertion/deletion of a zero or a single peak-shift*, IEEE Transactions on Information Theory 41 (1995), 279–283, https://doi.org/10.1109/18.370100.
6. OEIS A085680, bidirectional weight-two adjacent-transposition optima, https://oeis.org/A085680.
