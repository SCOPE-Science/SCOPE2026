# Isolated gaps of the three-term progression \(\langle a,a+2,a+4\rangle\)

## Finding

Let \(a=2s+1\) be any odd integer with \(s\ge1\), and let
\[
S_a=\langle a,a+2,a+4\rangle
=\{ax+(a+2)y+(a+4)z:x,y,z\in\mathbb Z_{\ge0}\}.
\]
A *gap* is a positive integer outside \(S_a\). It is *isolated* when both its immediate neighbors belong to \(S_a\). The isolated-gap set is exactly
\[
\boxed{I(S_a)=\left\{au+2j:\ s+1\le j\le2s,\quad
\left\lceil\frac{j-s}{2}\right\rceil-1\le u\le
\left\lceil\frac j2\right\rceil-1,\quad j,u\in\mathbb Z\right\}.}
\]
Its cardinality, the genus, and the Frobenius number satisfy
\[
\boxed{|I(S_a)|=\left\lfloor\frac{s(s+2)}2\right\rfloor
=\left\lfloor\frac{g(S_a)}2\right\rfloor,\qquad
 g(S_a)=s(s+2),\qquad F(S_a)=\frac{a^2+a-4}{2}.}
\]
In particular, the smallest isolated gap is \(a+1\), the largest is \(F(S_a)\), and asymptotically one half of the gaps are isolated.

## Assumptions and scope

All statements hold for every odd integer \(a\ge3\); the generators are positive and relatively prime, so the complement of \(S_a\) in \(\mathbb Z_{\ge0}\) is finite. For such \(a\) these three generators are minimal (for \(a\ge5\), each is smaller than \(2a\); the case \(a=3\) is immediate). The result is a complete classification of isolated gaps for this three-generated family, not for arbitrary progressions or arbitrary numerical semigroups.

## Proof

**1. Residue minima.** Every element of \(S_a\) is of the form \(at+2r\) with integers \(t\ge0\) and \(0\le r\le2t\): with \(t\) coins one can achieve any increment \(r\) from \(0\) through \(2t\) by using increments \(0,1,2\). Consequently the least number of coins realizing a given \(r\) is \(\lceil r/2\rceil\). Because \(a\) is odd, the residues \(2j\pmod a\), for \(0\le j<a\), are distinct. In residue \(2j\), every possible nonnegative increment has the form \(j+ka\), \(k\ge0\), and increasing it increases the least attainable value. Thus the Apéry representative in this residue is
\[
w_j=a\left\lceil\frac j2\right\rceil+2j,
\qquad 0\le j\le2s.
\]
For any integer \(h\ge0\) congruent to \(2j\pmod a\), membership is equivalent to \(h\ge w_j\). Every gap in this residue can therefore be written uniquely as \(h=au+2j\) for some integer \(u<\lceil j/2\rceil\) with \(h>0\).

**2. Neighbor criterion.** Write \(j_-\) and \(j_+\) for the residue indices of \(h-1\) and \(h+1\), respectively. The inverse of \(2\pmod a\) is \(s+1\). If \(0\le j\le s\), then \(j_-=j+s\) and
\[
h-1=a(u-1)+2(j+s).
\]
Since \(u<\lceil j/2\rceil\), we have \(u-1<\lceil(j+s)/2\rceil\). Hence \(h-1\notin S_a\), and this residue contains no isolated gap.

If \(s+1\le j\le2s\), then \(j_-=j-s-1\), \(j_+=j-s\), and
\[
h-1=a(u+1)+2(j-s-1),\qquad
h+1=a(u+1)+2(j-s).
\]
Both neighbors lie in \(S_a\) precisely when
\[
u+1\ge\max\left\{\left\lceil\frac{j-s-1}{2}\right\rceil,
\left\lceil\frac{j-s}{2}\right\rceil\right\}
=\left\lceil\frac{j-s}{2}\right\rceil.
\]
Combining this inequality with the gap inequality \(u<\lceil j/2\rceil\) gives exactly the boxed isolated-gap set, including both endpoints of its integer \(u\)-interval. In particular \(u\ge0\), so all displayed values are positive.

**3. Counting.** For each admissible \(j\) there are
\[
\left\lceil\frac j2\right\rceil-
\left\lceil\frac{j-s}{2}\right\rceil+1
\]
isolated gaps. Because distinct \(j\) have different residues modulo \(a\), these counts do not overlap. The identities
\[
\sum_{j=1}^{2s}\left\lceil\frac j2\right\rceil=s(s+1),
\qquad
\sum_{j=1}^{s}\left\lceil\frac j2\right\rceil
=\left\lfloor\frac{(s+1)^2}{4}\right\rfloor
\]
yield
\[
|I(S_a)|=s(s+2)-2\left\lfloor\frac{(s+1)^2}{4}\right\rfloor
=\left\lfloor\frac{s(s+2)}2\right\rfloor.
\]
For the genus, residue \(2j\) contributes \(\lfloor w_j/a\rfloor\) gaps. As \(\lfloor2j/a\rfloor=0\) for \(0\le j\le s\) and \(1\) for \(s+1\le j\le2s\),
\[
g(S_a)=\sum_{j=1}^{2s}\left\lfloor\frac{w_j}{a}\right\rfloor
=s(s+1)+s=s(s+2).
\]
Finally, \(w_j\) strictly increases with \(j\), so the Frobenius number is \(w_{2s}-a=a(s-1)+4s=(a^2+a-4)/2\), represented in the isolated-gap formula by \(j=2s\), \(u=s-1\). The minimum isolated gap is obtained at \(j=s+1\), \(u=0\), giving \(a+1\). This completes the proof.

## Verification

The independent direct-enumeration script `verify.py` computes semigroup membership by dynamic programming through the asserted Frobenius bound. For all 150 odd values \(a=3,5,\ldots,301\), it compares the exact isolated-gap set from the theorem against membership of both neighbors of every enumerated gap, and separately checks the genus, Frobenius number, cardinality, and endpoints. It passed, testing 1,158,925 enumerated gaps and 579,425 isolated gaps. Run with `python verify.py` (Python 3, standard library only). This finite check supplements, but does not replace, the unrestricted proof above.

## Relationship to prior work

Isolated gaps and perfect numerical semigroups were developed by Moreno-Frías and Rosales. Their 2020 embedding-dimension-three paper classifies when there are **no** isolated gaps, via the Frobenius number and pseudo-Frobenius data; it does not give the above positive isolated-gap enumeration. Smith (2022) relates isolated gaps to Apéry representatives and treats embedding dimension two. Singh and Ram (first public preprint 2024-06-14) give a full enumeration for embedding dimension two; their stated and proved family does not include these three-generator semigroups. The present result gives an exact three-generator progression classification, with an identity connecting isolated gaps to genus. Prior general Apéry techniques are used and are not claimed to be new.

## Limitations

No theorem is asserted for even \(a\), for other step sizes, or for arbitrary three-generated semigroups. A complete bibliographic exclusion of implicit earlier deductions has not been established; in particular some related journal articles were not fully accessible. No independent mathematical audit has been performed. Exact novelty must be judged relative to the cited results, not merely to differing wording or numerical sequences.

## References

1. S. N. Singh and R. K. Ram, *On Isolated Gaps of Numerical Semigroups of Embedding Dimension Two*, arXiv:2406.09848v1 (first posted 2024-06-14), https://arxiv.org/abs/2406.09848.
2. M. A. Moreno-Frías and J. C. Rosales, *Perfect Numerical Semigroups with Embedding Dimension Three*, Publ. Math. Debrecen 97 (2020), 77–84, DOI:10.5486/PMD.2020.8699, https://rodin.uca.es/handle/10498/24618.
3. H. J. Smith, *On Isolated Gaps in Numerical Semigroups*, Turkish J. Math. 46 (2022), 123–129, DOI:10.3906/mat-2107-54, https://journals.tubitak.gov.tr/math/vol46/iss1/9/.
4. M. A. Moreno-Frías and J. C. Rosales, *The Covariety of Perfect Numerical Semigroups with Fixed Frobenius Number*, arXiv:2305.14967 (2023), https://arxiv.org/abs/2305.14967.
5. A. Çelik, *A Note on The Some Class of Symmetric Numerical Semigroups*, Adıyaman University J. Science 13 (2023), 18–27, DOI:10.37094/adyujsci.1229288, https://dergipark.org.tr/en/pub/adyujsci/article/1229288.
