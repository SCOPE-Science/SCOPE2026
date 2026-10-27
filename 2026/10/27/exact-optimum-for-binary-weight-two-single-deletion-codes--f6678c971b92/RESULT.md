# Exact optimum for binary weight-two single-deletion codes

## Finding

For every integer \(n\ge2\), let \(A_2(n)\) be the largest size of a code \(C\subseteq\{0,1\}^n\) in which each codeword has exactly two ones and the *single-deletion descendant sets* of distinct codewords are disjoint. If \(D_1(w)\) is the set of distinct length-\(n-1\) words obtained by deleting one symbol from \(w\), the condition is
\[
D_1(u)\cap D_1(v)=\varnothing\qquad(u,v\in C,\ u\ne v).
\]
Then the exact optimum is
\[
\boxed{A_2(n)=\left\lfloor\frac{3n-2}{4}\right\rfloor\quad(n\ge2).}
\]
The first values, from length \(2\) onward, are \(1,1,2,3,4,4,5,6,7,7,8,9\). An explicit optimal code is given below, with no search or large precomputed data. In particular, \(A_2(n)=3n/4+O(1)\); its fraction among the \(\binom n2\) admissible words is asymptotic to \(3/(2n)\).

## Assumptions and scope

Words are linear, not cyclic; the alphabet is exactly \(\{0,1\}\); Hamming weight is exactly two; symbol deletions may remove either zeros or ones; distinct outputs are counted without multiplicity. Positions are zero-based and range from \(0\) to \(n-1\). For \(0\le i<j<n\), write \(w_{i,j}\) for the binary length-\(n\) word having its ones exactly at \(i,j\). No assertion concerns weights other than two, multiple deletions, or deletion/insertion channels with a different error model.

## Proof

**Step 1: the weight-one outputs.** Let \(0\le i<j<n\). Deleting the first one of \(w_{i,j}\) gives a unique one at position \(j-1\); deleting the second one gives a unique one at position \(i\). Thus the set of weight-one members of \(D_1(w_{i,j})\) has one element when \(j=i+1\) and two distinct elements otherwise. There are exactly \(n-1\) possible length-\(n-1\) words of weight one.

For any admissible code let \(L\) count its words of the form \(w_{i,i+1}\), and let \(S\) count its remaining (nonadjacent) weight-two words. Since the sets of deletion outputs must be disjoint, Step 1 gives
\[
L+2S\le n-1.\tag{1}
\]

**Step 2: adjacent-pair separation.** Two words \(w_{i,i+1}\) and \(w_{i+1,i+2}\), for \(0\le i\le n-3\), have the same weight-two deletion output: from the first word delete the zero at \(i+2\), and from the second word delete the zero at \(i\). The two survivors have ones at positions \(i,i+1\). Therefore starts of selected adjacent-pair words cannot be consecutive in the path on positions \(0,\ldots,n-2\). In particular,
\[
L\le\left\lceil\frac{n-1}{2}\right\rceil.\tag{2}
\]
For \(n=2\) this also holds (there is just one start).

**Step 3: upper bound.** Combining (1) and (2),
\[
|C|=L+S\le L+\left\lfloor\frac{n-1-L}{2}\right\rfloor
=\left\lfloor\frac{n-1+L}{2}\right\rfloor
\le\left\lfloor\frac{n-1+\lceil(n-1)/2\rceil}{2}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\]
The final equality is obtained by checking the four residues of \(n-1\) modulo four.

**Step 4: matching construction.** Put
\[
C_n=\bigl\{w_{2j,2j+1}:j\ge0,\ 2j+1<n\bigr\}
\ \cup\ 
\bigl\{w_{4h+1,4h+4}:h\ge0,\ 4h+4<n\bigr\}.
\]
The first group contains \(\lceil(n-1)/2\rceil\) words and the second \(\lfloor\lfloor(n-1)/2\rfloor/2\rfloor\) words. The first group has weight-one deletion outputs at precisely the even positions \(0,2,4,\ldots<n-1\). The second group has weight-one deletion outputs at position pairs \(\{4h+1,4h+3\}\), all odd and mutually disjoint. Thus no weight-one deletion output is shared.

Deleting a zero from a word in the first group leaves its two ones adjacent. Deleting a zero from a word in the second group, where the original two ones have gap three, leaves a gap of two or three, never one. Thus the groups share no weight-two output. Finally, for any second-group word \(w_{i,i+3}\), a weight-two descendant has its *first* one in \(\{i-1,i\}\) (according to which zero is deleted). Distinct second-group values of \(i\) differ by four, so these sets do not overlap; weight-two deletion outputs from different second-group words are distinct. The sets \(D_1(w)\) of all members of \(C_n\) are therefore pairwise disjoint.

The construction meets the upper bound:
\[
|C_n|=\left\lceil\frac{n-1}{2}\right\rceil+
\left\lfloor\frac{\lfloor(n-1)/2\rfloor}{2}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\]
This includes \(n=2\), proving the theorem. \(\square\)

## Verification

The included standard-library script `check.py` constructs deletion descendants directly from strings, without using the proof's classification as its deletion routine. It directly verifies all weight-one descendant identities for every weight-two word at lengths \(2\) through \(40\), enumerates exact maximum independent sets at lengths \(2\) through \(8\), and checks the explicit code's complete pairwise deletion disjointness at the same lengths and at several larger lengths through \(200\). Execute `python3 check.py` from the directory containing the script. The infinite statement follows from the preceding proof; finite checks do not replace it.

## Relationship to prior work

Sloane (2002) formulated single-deletion correction as independence in the deletion-confusability graph and studied unrestricted optimum sizes and Varshamov–Tenengolts codes. Cullina, Kulkarni and Kiyavash (2012) studied constant-weight induced graphs, proved optimal *colorings* for single deletion, and constructed code families. The coloring number \(\chi(L_{1,n,2})\) is different from the independence number \(\alpha(L_{1,n,2})=A_2(n)\): optimal coloring by itself does not determine the largest code. The present exact weight-two optimum follows from the direct one- and two-marker packing argument above, not from an optimal-coloring assertion.

## Limitations

This exact formula is confined to the binary weight-two slice under a single arbitrary deletion. It does not resolve the unrestricted binary single-deletion code optimum, and it does not classify every optimal weight-two code. An earlier independently published equivalent special-case formula cannot be categorically excluded; the claimed distinction is from the primary works inspected in the references, not a proof of absolute historical priority. The computational checks cover finite lengths only.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes* (2002), arXiv:math/0207197, https://arxiv.org/abs/math/0207197. Original arXiv posting 22 July 2002.
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *A coloring approach to constructing deletion correcting codes from constant weight subgraphs*, IEEE International Symposium on Information Theory (2012), DOI:10.1109/ISIT.2012.6284242.
3. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings* (2012), arXiv:1211.4056, https://arxiv.org/abs/1211.4056. Original arXiv posting 16 November 2012.
