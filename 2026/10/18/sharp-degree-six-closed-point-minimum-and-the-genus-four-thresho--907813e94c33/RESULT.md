# Sharp degree-six closed-point minimum and the genus-four threshold over \(\mathbf F_2\)

## Finding
Let \(C\) be a smooth, projective, geometrically integral genus-four curve over \(\mathbf F_2\). Write \(N_n(C)=\#C(\mathbf F_{2^n})\), and let \(B_n(C)\) denote the number of closed points of degree exactly \(n\). Then
\[
\min_C B_6(C)=1.
\]
The sole rational Jacobian isogeny class attaining equality has
\[
(N_1,N_2,N_3,N_4)=(3,9,9,45),\qquad
L_C(T)=1+2T^2+9T^4+8T^6+16T^8.
\]
It follows that the *uniform eventual closed-point threshold* of Aubry, Herbaut and Monaldi is
\[
\rho(2,4)=6.
\]
The assertion of uniqueness refers to the \(\mathbf F_2\)-isogeny class of the Jacobian, not to uniqueness of the abstract curve.

## Assumptions and scope
Here a curve always means a geometrically integral smooth projective curve over \(\mathbf F_2\) of genus exactly four. A closed point of degree \(n\) is a Frobenius orbit of cardinality \(n\), so \(N_n=\sum_{d\mid n}dB_d\). The threshold \(\rho(2,4)\) is the least positive integer \(m\) for which *every* such curve has \(B_n>0\) for *every* integer \(n\ge m\). In particular, an assertion solely about \(n=6\) does not itself prove the threshold.

The proof uses the exhaustive genus-four \(\mathbf F_2\) curve classification of Xarles [2], specifically the 620 Weil-polynomial classes in its original source table. Its correctness is assumed, rather than a new independent enumeration of isomorphism classes. The arithmetic extraction from that table is independently replayable here.

## Proof
**Step 1: Recover degree-six counts from the classified data.** For each genus-four curve write \(L_C(T)=\sum_{j=0}^{8}c_jT^j\) with \(c_0=1\). Put \(s_n=2^n+1-N_n\). Newton's identities determine the first four coefficients from \((N_1,N_2,N_3,N_4)\):
\[
 c_k=-\frac1k\left(s_k+\sum_{j=1}^{k-1}c_js_{k-j}\right),\quad 1\le k\le4.
\]
The functional equation gives \(c_5=2c_3\), \(c_6=4c_2\), \(c_7=8c_1\), and \(c_8=16\). Thus \(s_5\) and \(s_6\) follow by Newton's identities, and
\[
 B_6=\frac{N_6-N_3-N_2+N_1}{6},\qquad N_6=65-s_6.
\]
The complete source classification comprises exactly 620 different vectors, one for each rational Jacobian isogeny class [2, Theorem 10 and its associated data]. Decode `DATA.b64` as successive unsigned octets grouped four at a time and run `python3 verify_closed_points_genus4.py` in the same directory. All 620 vectors are verified to be distinct and lexicographically ordered, and all integer Newton recurrences are checked. The exact resulting frequency histogram of \(B_6\), with frequencies indexed by value \(1,2,\dots,19\), is
\[
(1,3,6,22,26,52,46,80,94,55,78,58,37,26,17,10,7,1,1).
\]
Their sum is 620. The *unique* row with \(B_6=1\) has \((N_1,N_2,N_3,N_4)=(3,9,9,45)\). Newton's identities give the Weil numerator displayed in the finding and \(N_6=21\), whence \((21-9-9+3)/6=1\). Since each row is realized by a curve in the complete census, existence and the sharp lower bound follow. The checker also recomputes \(N_6\) by a second expression in the degree-four real Weil polynomial, providing an independent recurrence cross-check.

**Step 2: A curve with no degree-five closed point.** Consider the smooth projective model of
\[
D:\quad y^2+y=x^9+x^5+1
\]
over \(\mathbf F_2\). The Artin--Schreier function has a single pole of odd order nine, so the cover is separable, has one rational point above infinity and has genus \((9-1)/2=4\). Over \(\mathbf F_{32}\), the absolute trace satisfies
\[
\operatorname{Tr}(x^9)=\operatorname{Tr}(x^{36})=\operatorname{Tr}(x^5),\qquad \operatorname{Tr}(1)=1,
\]
where \(x^{36}=x^5\) for \(x\in\mathbf F_{32}\). Therefore \(y^2+y=x^9+x^5+1\) has no affine \(\mathbf F_{32}\)-point. The same holds over \(\mathbf F_2\). Consequently \(N_5(D)=N_1(D)=1\), and \(B_5(D)=(N_5-N_1)/5=0\); so \(\rho(2,4)\ge6\). This specific Artin--Schreier example appeared in earlier diophantine-stability examples [3], and is not claimed as a new example.

**Step 3: All degrees beyond six.** For prime degree seven, \(7B_7=N_7-N_1\). Weil's estimates for genus four imply
\[
N_7-N_1\ge(129-8\cdot2^{7/2})-(3+8\sqrt2)=126-72\sqrt2>0.
\]
Thus every curve has a closed point of degree seven. For every integer \(n\ge8\), the Aubry--Haloui--Lachaud bound as stated in [1, Proposition 2.2 and preceding inequality] gives \(B_n>0\) whenever \((2^{n/4}-1)^2\ge 2g=8\). At \(n=8\) the left side is nine and increases thereafter. Step 1 covers \(n=6\), establishing \(\rho(2,4)\le6\). Combining with Step 2 proves equality.

## Verification
The standalone Python 3 checker requires only the standard library and the co-located compact derived table `DATA.b64`. Invocation: `python3 verify_closed_points_genus4.py`. It asserts the 620-entry table size/uniqueness, exact integrality of coefficient recurrences, equality of two independent \(N_6\) calculations, the complete \(B_6\) frequency histogram and the sole minimizer's data. It independently enumerates \(\mathbf F_{32}\) using the irreducible polynomial \(z^5+z^2+1\), checks the Artin--Schreier trace condition for every field element, and tests the stated numerical inequalities. All checks passed when executed from the embedded artifact paths. This is an exact arithmetic verification conditional on the exhaustiveness of the published census; it does not separately re-enumerate all genus-four curves.

## Relationship to prior work
Aubry--Herbaut--Monaldi [1] define the uniform eventual threshold and determine it for genera one through three; their general bound gives the existence of degree-\(n\) points for all \(n\ge8\) here, but does not settle genus four at degrees six or seven. Xarles [2] classifies the 1044 isomorphism classes and 620 Jacobian isogeny classes of genus-four curves over \(\mathbf F_2\), giving the complete quadruple list in his source repository; neither his theorem nor his displayed small-degree tables state the degree-six minimum or the threshold. This result extracts the first genus-four threshold and its sharp degree-six arithmetic extremum from his exhaustive classification. The witness for missing degree-five points belongs to the prior diophantine-stability literature [3]. The contribution is the precise threshold and sharp minimum, not a new curve census or a new example of the witness curve.

## Limitations
The uniqueness claim is at the level of \(\mathbf F_2\)-rational isogeny classes, not of curves. The proof depends on the correctness and completeness of the externally published census [2], which has not been independently re-created in the supplied script. The compact table is a lossless encoding of the 620 four-tuples extracted from the original dataset, not a substitute for that complete original source. Prior work may contain an unindexed equivalent computation; no independent external mathematical audit has been performed. This theorem addresses only genus four over \(\mathbf F_2\), not other field sizes or genera.

## References
[1] Y. Aubry, F. Herbaut and J. Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218v1, first posted 2023-10-17, especially Definition in Section 1 and Proposition 2.2. https://arxiv.org/abs/2310.11218

[2] X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822, Theorem 10 and tables; original companion repository, `ListCurvesGenus4p2.txt`, blob SHA `99610bd76b48b74b1ebf59c2df8052ff74d6e278`. https://github.com/XavierXarles/Censusforgenus4curvesoverF2

[3] J.-C. Lario, *Diophantine stability over finite fields*, example of a genus-four curve stable under the quintic extension. https://web.mat.upc.edu/joan.carles.lario/DS.html
