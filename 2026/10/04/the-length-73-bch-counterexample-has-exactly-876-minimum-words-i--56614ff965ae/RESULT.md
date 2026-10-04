# The length-73 BCH counterexample has exactly 876 minimum words in twelve cyclic orbits
## Finding

For the binary narrow-sense BCH code \(C=\mathcal C_{(2,73,5,1)}\), the exact parameters are \([73,55,6]\), and the number of minimum-weight codewords is \(A_6=876\). The 876 weight-six supports split into exactly twelve cyclic-shift orbits, each of size \(73\).

## Assumptions and scope

Let \(C=\mathcal C_{(2,73,5,1)}\) denote the binary narrow-sense BCH code of length \(73\) with designed distance \(5\). Let \(	heta\) be a primitive \(73\)-rd root of unity in \(\mathbb F_{2^9}\). The defining cyclotomic cosets are \(C_1\) and \(C_3\), each of size \(9\), so \(C\) has dimension \(73-18=55\). Equivalently, a binary support \(S\subseteq\mathbb Z/73\mathbb Z\) is a codeword support exactly when
\[
\sum_{i\in S}	heta^i=0,\qquad \sum_{i\in S}	heta^{3i}=0.
\]

The 2026 source reports by computer algebra that this exceptional \(s=3\) member has minimum distance \(6\), in contrast to the weight-five families it proves for many other \(s\). The claim here determines the exact number and cyclic structure of its minimum words and independently rechecks the distance.

## Proof

The BCH bound gives \(d(C)\ge5\), since the defining zero set contains four consecutive powers \(	heta,	heta^2,	heta^3,	heta^4\).

To exclude weight \(5\), cyclically shift a hypothetical support so that \(0\in S\). Write its remaining four positions as two disjoint pairs \(\{a,b}\) and \(\{c,d}\). The two syndrome equations imply
\[
(	heta^a+	heta^b,	heta^{3a}+	heta^{3b})
+(	heta^c+	heta^d,	heta^{3c}+	heta^{3d})=(1,1).
\]
The certificate exhausts all \(inom{72}{2}\) pairs of nonzero positions and finds no two disjoint pairs with complementary signatures. Hence no weight-five word exists.

For weight \(6\), assign to every triple \(T\subseteq\mathbb Z/73\mathbb Z\) the signature
\[
\sigma(T)=\left(\sum_{i\in T}	heta^i,\sum_{i\in T}	heta^{3i}ight).
\]
Two disjoint triples \(A,B\) have \(\sigma(A)=\sigma(B)\) exactly when their union is the support of a weight-six codeword. Conversely every weight-six support has exactly
\[
rac12inom63=10
\]
unordered partitions into two triples, and every one is an equal-signature pair. Exhausting all \(inom{73}{3}=62196\) triples gives exactly \(8760\) unordered disjoint equal-signature pairs. Dividing by \(10\) yields
\[
A_6=876.
\]
Thus weight six occurs and, with the weight-five exclusion, \(d(C)=6\).

Finally, cyclic shift acts freely on every nonempty proper support because \(73\) is prime. Canonicalizing the \(876\) weight-six supports under this action gives exactly \(12\) orbits, all of size \(73\). Their representatives are stored in `artifacts/certificate.json`.

## Verification

`artifacts/verify.py` uses only the Python standard library. It constructs a field of \(512\) elements as \(\mathbb F_2[x]/(x^9+x^4+1)\). It checks that the residue class of \(x\) has order \(511\), which also certifies that every nonzero residue is a unit and hence that the quotient is a field. It sets \(	heta=x^7\), verifies that \(	heta\) has order \(73\), reconstructs the two defining cyclotomic cosets, and checks the displayed generator polynomial.

The verifier then independently performs the normalized weight-five exclusion, rebuilds all \(62196\) triple signatures, verifies all \(8760\) disjoint collisions, checks every resulting support directly against both BCH syndromes, confirms multiplicity \(10\) for every support, and recomputes the twelve cyclic orbits. A successful replay prints `VERIFY_OK`.

## Relationship to prior work

Wang, He, Yi, and Zheng study the family \(\mathcal C_{(2,2^{2s}+2^s+1,5,1)}\). They construct weight-five words for several infinite classes of \(s\), while their exceptional \(s=3\) remark records only that \(\mathcal C_{(2,73,5,1)}\) has minimum distance \(6\) by Magma. Their statement does not give \(A_6\), a weight enumerator, or a cyclic-orbit classification of minimum words.

Searches for the exact parameters, the code notation, the generator polynomial, and the integer \(876\) found no source stating this minimum-word multiplicity. Closely related cyclic-code literature emphasizes that exact weight distributions are generally difficult and useful for error-probability calculations, but the general results inspected do not specialize to this BCH defining set in a way that determines \(A_6\).

## Limitations

Only the first nonzero weight coefficient and its cyclic-orbit decomposition are determined; this is not a complete weight enumerator. No formula is asserted for other values of \(s\). The originality conclusion is based on statement-level searches of the recent BCH source and relevant weight-distribution literature; an unindexed code table could contain the same coefficient.

## References

1. Xiaoqiang Wang, Jiawei He, Boru Yi, and Dabin Zheng, *Solutions to Three Conjectures and an Open Problem on Binary BCH Codes*, arXiv:2609.00532v1, first public version 2026-09-01.
2. Hai Q. Dinh, Chengju Li, and Qin Yue, *Recent progress on weight distributions of cyclic codes over finite fields*, Journal of Algebra Combinatorics Discrete Structures and Applications 2 (2015), 39–63, DOI 10.13069/jacodesmath.36866.
