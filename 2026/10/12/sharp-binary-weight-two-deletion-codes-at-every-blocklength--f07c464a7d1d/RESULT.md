# Sharp binary weight-two deletion codes at every blocklength
## Finding
For an integer \(n\ge2\), let \(\mathcal W_{n,2}\) be the set of binary words of length \(n\) having exactly two ones. Write \(D_1(w)\) for the set of distinct \((n-1)\)-symbol words obtained by deleting exactly one coordinate of \(w\). Define
\[
M_2(n)=\max\big\{|C|:C\subseteq\mathcal W_{n,2},\ D_1(x)\cap D_1(y)=\varnothing\text{ for distinct }x,y\in C\big\}.
\]
Then, **for every integer \(n\ge2\)**,
\[
\boxed{M_2(n)=\left\lfloor\frac{3n-2}{4}\right\rfloor
=\left\lfloor\frac n2\right\rfloor+\left\lfloor\frac{n-1}{4}\right\rfloor.}
\]
A maximum code is explicitly given by the support pairs
\[
\mathcal C_n=\{(2j,2j+1):0\le2j+1<n\}\ \cup\ \{(4j+1,4j+4):0\le4j+4<n\},
\]
where a support pair \((a,b)\) represents the unique word with ones at the zero-based positions \(a,b\).

In comparison, the largest single color class of the modified Varshamov--Tenengolts coloring \(\sum_{i=0}^{n-1}(i+1)w_i\pmod{n-1}\) of this layer has size exactly \(\lceil n/2\rceil\) for \(n\ge4\). Therefore the sharp optimum is asymptotically \(3/2\) times the size of the largest class in that standard optimal coloring. The coloring and its optimality as a coloring are earlier results; the new assertion concerns maximum independent-set size.

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\), length \(n\) is an integer at least two, and every codeword has Hamming weight exactly two. The channel deletes precisely one symbol at an unknown position. Repeated deletion outputs of one input are identified as a set, not counted with multiplicity. Decoding requires disjoint deletion-output sets for distinct inputs. The theorem does not claim anything about other weights, multiple deletions, arbitrary-weight binary codes, or larger alphabets.

## Proof
**1. A sharp obstruction from weight-one descendants.** Represent a weight-two word by the positions \(0\le a<b<n\) of its two ones. Deleting its rightmost one produces a weight-one word whose one is at position \(a\) in the output; deleting its leftmost one produces one at position \(b-1\). Consequently the set of weight-one descendants has size one if \(b=a+1\), and size two otherwise. All \(n-1\) possible weight-one descendants must be disjoint across codewords. If \(t\) codewords have adjacent ones and \(s\) have separated ones, then
\[
t+2s\le n-1.\tag{1}
\]
Moreover two adjacent-one words supported at \((a,a+1)\) and \((a+1,a+2)\) cannot coexist: deleting a zero after the first run and deleting a zero before the second run give the same weight-two output, supported at \((a,a+1)\), whenever both input supports are valid. Hence the \(t\) adjacent starts form a nonconsecutive subset of \(\{0,\ldots,n-2\}\), and
\[
t\le\left\lceil\frac{n-1}{2}\right\rceil=\left\lfloor\frac n2\right\rfloor.\tag{2}
\]
Since \(s\) is an integer, (1)--(2) imply
\[
|C|=t+s\le\left\lfloor\frac{n-1+t}{2}\right\rfloor\le
\left\lfloor\frac{n-1+\lfloor n/2\rfloor}{2}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.\tag{3}
\]

**2. A construction meeting the obstruction.** Take every even-start adjacent pair \((2j,2j+1)\), and every separated pair \((4j+1,4j+4)\), subject to the index ranges in the finding. Their numbers are \(\lfloor n/2\rfloor\) and \(\lfloor(n-1)/4\rfloor\), respectively.

Their weight-one descendant positions are respectively the distinct even positions \(2j\) and the disjoint pairs of odd positions \(4j+1,4j+3\). Thus no weight-one descendant is shared. For weight-two descendants, deletion of a zero from an adjacent pair yields another adjacent pair (distance one between its surviving ones), whereas deletion of a zero from \((4j+1,4j+4)\) yields one of \((4j,4j+3)\), \((4j+1,4j+3)\), or \((4j+1,4j+4)\). These have distance two or three between surviving ones, and their first coordinates for different \(j\) belong to disjoint two-element sets \(\{4j,4j+1\}\). The weight-two descendants of different even-start adjacent pairs are also distinct, since they have supports drawn from \((2j-1,2j)\) or \((2j,2j+1)\); neither ordered pair can occur for a different \(j\). At boundaries some listed possibilities disappear, never introduce new collisions. Therefore all deletion sets are pairwise disjoint, so construction and (3) prove the equality for every \(n\ge2\).

**3. Exact comparison with the known coloring.** For \(n\ge4\), let \(m=n-1\). The \(n\) index weights \(1,\ldots,n\) modulo \(m\) comprise each residue once, plus a second copy of residue \(1\). For a target checksum residue \(r\), pair residues \(u\) with \(r-u\). Starting from one of each residue, there are \((m-f_r)/2\) unordered pairs of distinct positions, where \(f_r=|\{u\in\mathbb Z_m:2u=r\}|\). The duplicated residue \(1\) adds exactly one further pair (also when it pairs with itself). If \(m\) is odd, \(f_r=1\) for every \(r\); if \(m\) is even, \(f_r=0\) for odd \(r\) and \(f_r=2\) for even \(r\). Thus the maximum class size is \(\lceil n/2\rceil\). Since the exact optimum equals \(3n/4+O(1)\), the ratio tends to \(3/2\). No claim is made that the known coloring ceases to be optimal as a coloring.

## Verification
The standalone standard-library program `verify.py` generates the proposed code at each length \(2\le n\le64\), independently simulates every deletion position of every constructed word, and checks disjointness and the claimed size. It also exactly searches the finite compatibility graph for \(2\le n\le9\) by a branch-and-bound maximum-clique algorithm and directly enumerates all modified-VT residue-class sizes for \(4\le n\le64\). The result is:

`VERIFY_OK construction n=2..64; exhaustive maxima n=2..9; modified VT classes n=4..64`

These checks test the construction and small instances, but the theorem for unbounded \(n\) rests exclusively on the foregoing combinatorial proof.

## Relationship to prior work
Cullina, Kulkarni and Kiyavash (arXiv:1211.4056v1, 16 November 2012), Section IV, prove that the modified Varshamov--Tenengolts checksum gives an optimal coloring of each binary constant-weight one-deletion confusability graph, with chromatic number \(\max(k,n-k)+1\). That coloring theorem does not determine the independence number of the weight-two layer; the present result gives an exact value and an explicit maximum independent set, showing a linear-size gap between the optimum and the largest modified-VT color class.

Kulkarni and Kiyavash (arXiv:1211.3128v1, 13 November 2012) give deletion-code packing bounds, including unrestricted and constrained-source results. The particular closed weight-two independence number and construction above are not supplied by those general bounds. A later thesis by Cullina (2015), *Constant composition deletion correcting codes*, is especially relevant; its bibliographic page and abstract were accessible, but a complete reliable full-text reading was not possible, so potential overlap remains a bibliographic risk.

## Limitations
No uniqueness of the construction, classification of all maximizers, decoding-complexity optimum, or claim about other weights is asserted. Mathematical correctness is shown by a direct proof, but formal machine certification and independent external audit have not been performed. Literature discovery cannot exclude obscure or unindexed earlier statements, particularly inside the inaccessible complete thesis just noted.

## References
1. D. Cullina, A. A. Kulkarni, and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056v1, 2012, especially Section IV and Theorem 5. https://arxiv.org/abs/1211.4056
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, 2012; IEEE Trans. Inf. Theory 59 (2013), 5115--5130. https://arxiv.org/abs/1211.3128
3. D. Cullina, *Constant composition deletion correcting codes*, M.S. thesis, University of Illinois, repository record dated 2015-01-21, https://www.ideals.illinois.edu/items/73103 . Complete text not reliably inspected.
