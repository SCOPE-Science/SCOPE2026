# Zero-padding rigidity of reverse-multiple carry strings

## Finding
Consider a nontrivial base-\(b\) reverse multiple with multiplier \(n\). Write its canonical long-multiplication carries as \(c_0,c_1,\ldots,c_{k+1}\), starting and ending with \(c_0=c_{k+1}=0\). Then **the first interior carry is strictly positive**, and **the two highest interior carries cannot both be zero**:
\[
 c_1>0,\qquad (c_k,c_{k-1})\ne(0,0)\quad(k\ge2).
\]
Consequently, suppose a higher-base reverse multiple is constructed so that its finite carry string, written from highest to lowest, consists of an *unaltered, contiguous copy* of the nonzero-ended digit string of another reverse multiple, together with zero digits appended **only at its two outer ends**. Its outer zero padding, if any, must have precisely one zero on the low-index end and at most one zero on the high-index end. Thus among these zero-padded contiguous carry encodings the only possible shapes are
\[
(d_m,d_{m-1},\ldots,d_0,0)
\quad\text{or}\quad
(0,d_m,d_{m-1},\ldots,d_0,0),
\]
where the source has \(d_m,d_0>0\). These are necessary shapes, not claims that every source can be realized. This excludes all further outer-zero-padded third, fourth, or higher extensions in the sense made precise here.

## Assumptions and scope
Fix integers \(b\ge3\), \(2\le n<b\), and \(k\ge1\). Let \(d_0,\ldots,d_k\) be base-\(b\) digits with \(d_0d_k\ne0\). An \((n,b)\)-palintiple is an equality
\[
 \sum_{j=0}^{k}d_jb^j=n\sum_{j=0}^{k}d_{k-j}b^j.
\]
The nonzero end digits guarantee that both reversed representations have the indicated length. The carries \(c_j\) are defined uniquely by the grade-school multiplication of the reversed digit string by \(n\):
\[
 c_0=c_{k+1}=0,\qquad b c_{j+1}=n d_{k-j}+c_j-d_j\quad(0\le j\le k).
\]
The carry string **from highest to lowest** is \((c_k,c_{k-1},\ldots,c_1,c_0)\); note that \(c_{k+1}\) is the terminal carry beyond the represented digits and is not part of that string. The padding corollary refers only to a contiguous source digit string \((d_m,\ldots,d_0)\) with **outer** zeros; it makes no assertion about arbitrary inserted zeros, reordered digits, or other possible meanings of derived reverse multiples.

## Proof
First prove the standard carry bound without assuming the result. Every long-multiplication carry satisfies \(0\le c_j\le n-1\). This holds at \(j=0\); if it holds at \(j\), the usual quotient expression gives
\[
 c_{j+1}=\left\lfloor\frac{n d_{k-j}+c_j}{b}\right\rfloor
 \le \left\lfloor\frac{n(b-1)+(n-1)}{b}\right\rfloor=n-1.
\]
Set \(D=n^2-1\), a positive integer. Pairing the carry equation at \(j\) with that at \(k-j\) eliminates the reversed digit and yields, for every \(0\le j\le k\),
\[
 Dd_j=nbc_{k-j+1}-nc_{k-j}+bc_{j+1}-c_j. \tag{1}
\]
For completeness, the two equations are \(bc_{j+1}=nd_{k-j}+c_j-d_j\) and \(bc_{k-j+1}=nd_j+c_{k-j}-d_{k-j}\); substitution and collection of terms gives (1). No divisibility assumption beyond integrality of the digits has been added.

Putting \(j=k\) in (1) and using \(c_0=c_{k+1}=0\), we obtain
\[
 Dd_k=nbc_1-c_k.
\]
If \(c_1=0\), its right side is nonpositive although \(d_k>0\), a contradiction. Hence \(1\le c_1\le n-1\).

Assume now that \(k\ge2\) and that \(c_k=c_{k-1}=0\). Putting \(j=0\) and \(j=1\) in (1) gives, respectively,
\[
 Dd_0=bc_1,\qquad Dd_1=bc_2-c_1.
\]
Thus \(D\mid bc_1\) and \(D\mid(bc_2-c_1)\). Multiply the first divisibility by \(c_2\), the second by \(c_1\), and subtract to get
\[
 D\mid c_1^2.
\]
But \(1\le c_1\le n-1\) implies
\[
 0<c_1^2\le(n-1)^2<n^2-1=D.
\]
No positive integer strictly below \(D\) is divisible by \(D\); contradiction. This proves the carry-boundary theorem, uniformly for all admissible bases, multipliers, and lengths. The short case \(k=1\) already has \(c_1>0\).

For the padding corollary, write the candidate higher-base carry string as \((0^u,d_m,\ldots,d_0,0^v)\) with \(u,v\ge0\) and \(d_m,d_0>0\). The required last carry is \(c_0=0\), so \(v\ge1\); since \(c_1>0\), in fact \(v=1\). The two-top-carry exclusion says \(u\le1\). Therefore \((u,v)=(0,1)\) or \((1,1)\), which are exactly the two listed shapes. This is a necessary classification of outer-zero padding; it does not require the source digit string to satisfy any additional congruence beyond having nonzero ends.

## Verification
The proof uses exact integer equalities, carry bounds, and elementary divisibility. No finite computation is used to infer an infinite result. The standalone Python 3 file `verify.py` independently reconstructs base-\(b\) long-multiplication carries for every digit string of length 2 through 5 and bases 3 through 16 with nonzero endpoints. It checked 3,103,793 candidates, found 150 valid nontrivial reverse multiples, and found 56 valid cases whose highest interior carry is zero; none has two highest interior zeros. A separate test exhausts 117,810 tuples with bases up to 35 against the two critical modular necessary conditions, finding none. Run `python3 verify.py`; it needs only the standard library. These finite tests are additional regression checks, not a replacement for the proof.

## Relationship to prior work
Holt's 2014 paper, *Some General Results and Open Questions on Palintiple Numbers*, establishes the digit–carry identity in Corollary 2 and the carry bound in Theorem 3. Those are precisely the starting premises of equation (1); they are credited here, not claimed new. That paper also notes the positivity of the first interior carry. The contribution of the present argument is the **second-endpoint modular-square obstruction** \(D\mid c_1^2\), yielding the universal prohibition on two initial zero carries.

Holt's *Derived Palintiple Families and Their Palinomials* (first public version 2014-11-30, published 2016), Section 2, introduced singly-derived carries of shape \((d_m,\ldots,d_0,0)\) and doubly-derived carries of shape \((0,d_m,\ldots,d_0,0)\). Its Section 7 explicitly leaves possible third and fourth types open. The present theorem eliminates **all alternative patterns obtained by merely adding further outer zero carries to an unaltered source digit string**; it does not purport to settle broader derived constructions involving nontrivial modifications. Kendrick's *Young Graphs: 1089 et al* (first public version 2014-10-01) classifies important reverse-multiple carry graphs, but no statement of this universal two-highest-zero exclusion was identified in the inspected material. A stronger or equivalent unindexed prior result remains a priority risk.

## Limitations
The conclusion is a *necessary* carry-pattern obstruction, not a construction or sufficient criterion for singly- or doubly-derived palintiples. It addresses outer-zero padded **contiguous** copies, not internal zero insertions, permutation-based derived encodings, or all conceptually possible higher derivations. It does not classify every reverse multiple, every Young graph, or all open problems about derived palintiples. The literature comparison is not a proof of uniqueness or priority. The mathematical proof is exact; its novelty relative to unindexed literature remains subject to further comparison.

## References
1. B. V. Holt, *Some General Results and Open Questions on Palintiple Numbers*, Integers **14** (2014), #A42, published August 27, 2014, especially Corollary 2 and Theorem 3. https://math.colgate.edu/~integers/o42/o42.pdf
2. B. V. Holt, *Derived Palintiple Families and Their Palinomials*, arXiv:1412.0231 (first publicly submitted November 30, 2014); Integers **16** (2016), #A27, especially Sections 2 and 7. https://math.colgate.edu/~integers/q27/q27.pdf ; https://arxiv.org/abs/1412.0231
3. L. H. Kendrick, *Young Graphs: 1089 et al*, arXiv:1410.0106 (first publicly submitted October 1, 2014); Journal of Integer Sequences **18** (2015), Article 15.9.7. https://arxiv.org/abs/1410.0106
